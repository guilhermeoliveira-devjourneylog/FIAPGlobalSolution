import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

from mission.events.eva import EVAEvent

class SurfacePhase(MissionPhase):

    def generate(self):

        t = np.arange(0,5000)

        return pd.DataFrame({

            "phase":"SURFACE",

            "time_step":t,

            "solar_power_kw":
            np.random.normal(
                95,
                5,
                len(t)
            ),

            "eva":
            EVAEvent.activity(
                len(t)
            )
        })