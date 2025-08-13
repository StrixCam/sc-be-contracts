from dataclasses import dataclass

from src.sc_be_contracts.models.tracking.detection import BallDetection, CourtDetection, PlayerDetection


@dataclass
class DetectionData:
    ball: BallDetection
    court: CourtDetection
    players: list[PlayerDetection]
