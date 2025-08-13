from dataclasses import dataclass

from src.models.tracking.boundaries import Point


@dataclass
class BallDetection:
    center: Point
    confidence: float
