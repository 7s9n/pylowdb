from typing import (
    TypeVar,
    Union,
)
from abc import ABC, abstractmethod
import os
from os import path
import json

try:
    import yaml
except ImportError as e:
    print('yaml is not installed, please install it with pip install PyYAML')
except Exception:
    print('Error cannot import yaml')

__all__ = [
    'Adapter',
    'TextFile',
    'JsonFile',
    'Memory',
    'YAMLFile',
]

T = TypeVar('T')


class Adapter(ABC):
    """
    The abstract base class for all Adapters.

    An Adapter (de)serializes the current state of the database and stores it in
    some place (memory, file on disk, ...).
    """
    @abstractmethod
    def read(self) -> T:
        """
        Any kind of deserialization should go here.

        Return ``None`` here to indicate that the storage is empty.
        """
        raise NotImplementedError('To be overridden!')

    @abstractmethod
    def write(self, data: T) -> None:
        """
        Any kind of serialization should go here.
        """
        raise NotImplementedError('To be overridden!')


class TextFile(Adapter):
    """
    Adapter for reading and writing text. Useful for creating custom adapters.

    """

    def __init__(self, filename: str) -> None:
        """
        Create a new instance.

        Also creates the storage file, if it doesn't exist.

        :param filename: Where to store the data.
        :type filename: str
        """
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
            return data or None

    def write(self, data: str) -> None:
        with open(self.tmp_filename, 'w') as f:
            f.write(data)
        os.remove(self.filename)
        os.rename(self.tmp_filename, self.filename)


class JSONFile(Adapter):
    """
    Adapter for reading and writing JSON files.
    """

    def __init__(self, filename: str) -> None:
        """
        Create a new instance.

        Also creates the storage file, if it doesn't exist.

        :param filename: Where to store the JSON data.
        :type filename: str
        """
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
    """
    In-memory adapter. Useful for speeding up unit tests.

    Store the data as it is in memory.
    """

    def __init__(self) -> None:
        """
        Create a new instance.
        """
        super().__init__()
        self.data: T = None

    def read(self) -> T:
        return self.data or None

    def write(self, data: T) -> None:
        self.data = data


class YAMLFile(Adapter):
    """
    Adapter for reading and writing YAML files.
    """

    def __init__(self, filename: str) -> None:
        """
        Create a new instance.

        Also creates the storage file, if it doesn't exist.

        :param filename: Where to store the YAML data.
        :type filename: str
        """
        super().__init__()
        self.adapter: Adapter = TextFile(filename)

    def read(self) -> Union[T, None]:
        data = self.adapter.read()

        if not data or data is None:
            return None
        else:
            return yaml.safe_load(data)

    def write(self, data: T) -> None:
        self.adapter.write(yaml.dump(data))
