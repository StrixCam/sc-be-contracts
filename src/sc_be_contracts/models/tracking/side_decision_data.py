from dataclasses import dataclass

from src.sc_be_contracts.models.general.sides import Sides


@dataclass
class SideDecisionData:
    side: Sides
    confidence: float = 0.0
