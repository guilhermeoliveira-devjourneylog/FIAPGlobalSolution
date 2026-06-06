import numpy as np

class CommunicationModel:

    @staticmethod
    def signal(samples):

        return np.random.normal(
            98,
            0.8,
            samples
        )
