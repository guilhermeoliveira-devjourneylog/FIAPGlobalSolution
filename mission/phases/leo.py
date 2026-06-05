import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

class LEOPhase(MissionPhase):

    def generate(self):

        t = np.arange(0,181)

        return pd.DataFrame({

            "phase":"LEO",

            "time_min":t,

            "altitude_km":
            np.random.normal(
                185,
                1,
                len(t)
            ),

            "velocity_kmh":
            np.random.normal(
                28000,
                50,
                len(t)
            )
        })