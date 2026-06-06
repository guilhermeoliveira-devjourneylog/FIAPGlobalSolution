import numpy as np

class PowerModel:

    @staticmethod
    def battery(start, end, samples):

        return np.linspace(
            start,
            end,
            samples
        )

    @staticmethod
    def power_kw(samples):

        return np.random.normal(
            22,
            0.5,
            samples
        )