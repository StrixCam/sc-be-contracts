from dataclasses import dataclass

from src.sc_be_contracts.models.tracking.boundaries import Point


@dataclass
class ZoomData:
    center: Point
    zoom_level: float
