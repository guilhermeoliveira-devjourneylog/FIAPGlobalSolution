import numpy as np

class BurnEvent:

    @staticmethod
    def generate(samples, quantity=3):

        burn = np.zeros(samples)

        idx = np.random.choice(
            np.arange(50, samples-50),
            quantity,
            replace=False
        )

        burn[idx] = 1

        return burn