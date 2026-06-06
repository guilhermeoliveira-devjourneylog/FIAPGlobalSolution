import numpy as np

class PropulsionModel:

    @staticmethod
    def fuel_profile(start, end, samples):

        return np.linspace(
            start,
            end,
            samples
        )

    @staticmethod
    def engine_thrust(samples):

        return np.clip(
            np.random.normal(
                95,
                2,
                samples
            ),
            0,
            100
        )