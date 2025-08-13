from abc import ABC, abstractmethod

from src.models.capturer.frame import Frame


class ICamera(ABC):
	@abstractmethod
	def __init__(self, camera_index: int) -> None: ...

	@abstractmethod
	def start(self) -> None: ...

	@abstractmethod
	def get_frame(self) -> Frame: ...

	@abstractmethod
	def stop(self) -> None: ...

	@abstractmethod
	def restart(self) -> None: ...

	@abstractmethod
	def status(self) -> str: ...
	
	@abstractmethod
	def focus(self) -> None: ...
