from abc import ABC, abstractmethod

from src.models.capturer import Frame
from src.models.tracking import DetectionData


class ITracker(ABC):
    @abstractmethod
    def start(self) -> None: ...

    @abstractmethod
    def stop(self) -> None: ...

    @abstractmethod
    def reset(self) -> None: ...

    @abstractmethod
    def detect(self, frame: Frame) -> DetectionData: ...
