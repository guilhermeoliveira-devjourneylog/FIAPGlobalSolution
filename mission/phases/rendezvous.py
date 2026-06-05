import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

from mission.events.docking import DockingEvent

class RendezvousPhase(MissionPhase):

    def generate(self):

        t = np.arange(0,1801)

        return pd.DataFrame({

            "phase":"RENDEZVOUS",

            "time_s":t,

            "distance_m":
            np.linspace(
                1000,
                0,
                len(t)
            ),

            "status":
            DockingEvent.status(
                len(t)
            )
        })