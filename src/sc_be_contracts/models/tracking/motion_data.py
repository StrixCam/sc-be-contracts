from dataclasses import dataclass

from src.sc_be_contracts.models.tracking.boundaries import Point


@dataclass
class MotionData:
    position: Point
    velocity: Point
    acceleration: Point

    def speed(self) -> float:
        return (self.velocity.x**2 + self.velocity.y**2) ** 0.5

    def acc(self) -> float:
        return (self.acceleration.x**2 + self.acceleration.y**2) ** 0.5
