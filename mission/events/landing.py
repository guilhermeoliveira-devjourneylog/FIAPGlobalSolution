import numpy as np

class LandingEvent:

    @staticmethod
    def touchdown(samples):

        status = np.array(
            ["NO"] * samples
        )

        status[int(samples*0.98):] = "YES"

        return status