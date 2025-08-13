from dataclasses import dataclass

from src.models.tracking.boundaries import Court


@dataclass
class CourtDetection:
    court: Court
    confidence: float
