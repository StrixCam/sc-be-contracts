from abc import ABC, abstractmethod
from collections.abc import Generator

from src.interfaces.capturer.camera import ICamera
from src.models.capturer.frame import Frame


class IVideoService(ABC):
    @abstractmethod
    def __init__(self, cam0: ICamera, cam1: ICamera) -> None: ...

    @abstractmethod
    def start(self) -> None: ...

    @abstractmethod
    def stop(self) -> None: ...

    @abstractmethod
    def status(self) -> bool: ...

    @abstractmethod
    def _focus(self) -> None: ...

    @abstractmethod
    def _get_frames(self) -> None: ...
    
    @abstractmethod
    def _preprocess(self) -> None: ...

    @abstractmethod
    def _postprocess(self) -> None: ...
    
    @abstractmethod
    def _transform(self) -> None: ...
    
    @abstractmethod
    def _track(self) -> None: ...

    @abstractmethod
    def _frames(
    ) -> Generator[Frame, None, None]: ...
    
    @abstractmethod
    def feed(self) -> Generator[Frame, None, None]: ...