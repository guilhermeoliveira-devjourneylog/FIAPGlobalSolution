import numpy as np

class ThermalModel:

    @staticmethod
    def temperature(
        mean,
        sigma,
        samples
    ):
        return np.random.normal(
            mean,
            sigma,
            samples
        )
