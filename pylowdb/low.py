from typing import TypeVar
from adapters import Adapter
from errors import MissingAdapterError

T = TypeVar('T')


class Low:
    def __init__(self, adapter: Adapter):
        if adapter is None:
            raise MissingAdapterError('You must provite an adapter.')

        if not isinstance(adapter, Adapter):
            raise TypeError("{} must be of Adapter type, not {}".format(
                adapter, adapter.__class__.__qualname__))

        self.adapter: Adapter = adapter
        self.data: T = None

    def read(self) -> None:
        self.data = self.adapter.read()

    def write(self) -> None:
        if self.data and self.data is not None:
            self.adapter.write(self.data)