from dataclasses import dataclass

@dataclass
class powerValue:
    from datetime import datetime

    power_meter: float
    power_pv: float = 0
    time: datetime = None

    def power_total(self) -> float:
        return self.power_meter + self.power_pv

