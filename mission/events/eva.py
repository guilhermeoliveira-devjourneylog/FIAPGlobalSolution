import numpy as np

class EVAEvent:

    @staticmethod
    def activity(samples):

        eva = np.array(
            ["IDLE"] * samples
        )

        eva[int(samples*0.6):] = "ACTIVE"

        return eva