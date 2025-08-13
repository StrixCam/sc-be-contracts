from abc import ABC, abstractmethod
from collections.abc import Generator

from src.sc_be_contracts.models.capturer import Frame
from src.sc_be_contracts.models.stream import StreamProtocol


class IStreamProvider(ABC):
    def __init__(self, provider: StreamProtocol, active: bool) -> None: ...

    @abstractmethod
    def start(
        self,
        feed: Generator[Frame, None, None],
        url: str,
    ) -> None: ...

    @abstractmethod
    def stop(self) -> None: ...

    @abstractmethod
    def _rtmp(
        self,
        feed: Generator[Frame, None, None],
        url: str,
    ) -> None: ...
