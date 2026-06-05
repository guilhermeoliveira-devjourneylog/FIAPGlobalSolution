import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

from mission.telemetry.propulsion import PropulsionModel
from mission.telemetry.power import PowerModel
from mission.events.burns import BurnEvent

class TranslunarPhase(MissionPhase):

    def generate(self):

        t = np.arange(0,72*60)

        n = len(t)

        return pd.DataFrame({

            "phase":"TRANSLUNAR",

            "time_min":t,

            "distance_km":
            np.linspace(
                200000,
                384400,
                n
            ),

            "fuel_pct":
            PropulsionModel.fuel_profile(
                100,
                65,
                n
            ),

            "power_kw":
            PowerModel.power_kw(n),

            "burn":
            BurnEvent.generate(n)
        })