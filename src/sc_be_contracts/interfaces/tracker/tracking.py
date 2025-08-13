from abc import ABC, abstractmethod

from src.sc_be_contracts.models.capturer import Frame
from src.sc_be_contracts.models.tracking import DetectionData


class ITracker(ABC):
    @abstractmethod
    def start(self) -> None: ...

    @abstractmethod
    def stop(self) -> None: ...

    @abstractmethod
    def reset(self) -> None: ...

    @abstractmethod
    def detect(self, frame: Frame) -> DetectionData: ...
