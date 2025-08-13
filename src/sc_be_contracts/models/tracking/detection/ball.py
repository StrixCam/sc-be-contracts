from dataclasses import dataclass

from src.sc_be_contracts.models.tracking.boundaries import Point


@dataclass
class BallDetection:
    center: Point
    confidence: float
