from abc import ABC, abstractmethod

from src.sc_be_contracts.interfaces.capturer.video import IVideoService
from src.sc_be_contracts.models.stream import StreamProtocol

from .provider import IStreamProvider


class IStreamService(ABC):
    @abstractmethod
    def __init__(
        self, video_service: IVideoService, provider: StreamProtocol
    ) -> None: ...

    @abstractmethod
    def start(self) -> None: ...

    @abstractmethod
    def stop(self) -> None: ...

    @abstractmethod
    def get_status(self) -> str: ...

    @abstractmethod
    def focus(self) -> None: ...

    @abstractmethod
    def feed(
        self,
        stream_provider: IStreamProvider,
        url: str,
    ) -> None: ...
