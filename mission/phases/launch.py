import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

class LaunchPhase(MissionPhase):

    def generate(self):

        t = np.arange(0,601)

        altitude = t * 0.45

        velocity = t * 20

        return pd.DataFrame({

            "phase":"LAUNCH",

            "time_s":t,

            "altitude_km":altitude,

            "velocity_ms":velocity
        })