import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

class NRHOPhase(MissionPhase):

    def generate(self):

        t = np.arange(0,7*24*60)

        return pd.DataFrame({

            "phase":"NRHO",

            "time_min":t,

            "altitude_km":
            np.random.normal(
                70000,
                500,
                len(t)
            )
        })