from typing import (
    TypeVar,
    Union,
)
from abc import ABC, abstractmethod
import os
from os import path
import json

__all__ = [
    'Adapter',
    'TextFile',
    'JsonFile',
    'Memory',
]

T = TypeVar('T')


class Adapter(ABC):

    @abstractmethod
    def read(self) -> T:
        raise NotImplementedError('To be overridden!')

    @abstractmethod
    def write(self, data: T) -> None:
        raise NotImplementedError('To be overridden!')


class TextFile(Adapter):
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename: str = filename
        self.tmp_filename: str = path.join(
            path.dirname(filename),
            f'.{path.basename(filename)}.tmp'
        )
        with open(self.filename, 'a'):
            os.utime(self.filename)

    def read(self) -> Union[str, None]:
        try:
            with open(self.filename, mode='r+', encoding='utf-8') as f:
                data = f.read()
        except Exception as e:
            print(e)
            return None
        else:
            return data

    def write(self, data: str) -> None:
        with open(self.tmp_filename, 'w') as f:
            f.write(data)
            os.remove(self.filename)
            os.rename(self.tmp_filename, self.filename)


class JsonFile(Adapter):
    def __init__(self, filename: str) -> None:
        self.adapter: Adapter = TextFile(filename=filename)

    def read(self) -> Union[T, None]:
        data = self.adapter.read()

        if not data or data is None:
            return None
        else:
            return json.loads(data)

    def write(self, data: T) -> None:
        self.adapter.write(json.dumps(data))


class Memory(Adapter):
    def __init__(self) -> None:
        super().__init__()
        self.data: T = None

    def read(self) -> T:
        return self.data or None

    def write(self, data: T) -> None:
        self.data = data
