import numpy as np

class DockingEvent:

    @staticmethod
    def status(samples):

        status = np.array(
            ["APPROACH"] * samples
        )

        status[int(samples*0.95):] = "DOCKED"

        return status