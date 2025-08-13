from dataclasses import dataclass

from src.models.tracking.boundaries import Point


@dataclass
class ZoomData:
    center: Point
    zoom_level: float
