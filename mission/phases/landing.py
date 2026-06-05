import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

from mission.events.landing import LandingEvent

class LandingPhase(MissionPhase):

    def generate(self):

        t = np.arange(0,901)

        return pd.DataFrame({

            "phase":"LANDING",

            "time_s":t,

            "altitude_m":
            np.linspace(
                15000,
                0,
                len(t)
            ),

            "touchdown":
            LandingEvent.touchdown(
                len(t)
            )
        })