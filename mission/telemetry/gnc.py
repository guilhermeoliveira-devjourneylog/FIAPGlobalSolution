import numpy as np

class GNCModel:

    @staticmethod
    def navigation_error(samples):

        return np.abs(
            np.random.normal(
                1,
                0.3,
                samples
            )
        )

    @staticmethod
    def attitude(samples):

        return (
            np.random.normal(0,0.5,samples),
            np.random.normal(0,0.5,samples),
            np.random.normal(0,0.5,samples)
        )
