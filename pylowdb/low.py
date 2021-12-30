from typing import TypeVar
from adapters import Adapter
from errors import MissingAdapterError

T = TypeVar('T')


class Low:
    """
    The main class of pylowdb.

    Gives access to the database, provides methods to read and write
    to the database.
    """

    def __init__(self, adapter: Adapter):
        """
        Create a new instance of pylowdb.

        :param adapter: The class of the adapter to use.
        """
        if adapter is None:
            raise MissingAdapterError('You must provite an adapter.')

        if not isinstance(adapter, Adapter):
            raise TypeError("{} must be of Adapter type, not {}".format(
                adapter, adapter.__class__.__qualname__))

        self.adapter: Adapter = adapter
        self.data: T = None

    def read(self) -> None:
        """
        Reading access to the DB.

        Calls adapter.read() and sets self.data.
        """
        self.data = self.adapter.read()

    def write(self) -> None:
        """
        Writing access to the DB.

        Calls adapter.write(self.data).
        """
        if self.data and self.data is not None:
            self.adapter.write(self.data)
