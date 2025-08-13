from dataclasses import dataclass

from src.sc_be_contracts.models.tracking.boundaries import Court


@dataclass
class CourtDetection:
    court: Court
    confidence: float
