import pandas as pd

from mission.factory.phase_factory import PhaseFactory

class MissionBuilder:

    def __init__(self):

        self.datasets = []

    def add_phase(self, name):

        phase = PhaseFactory.create(name)

        self.datasets.append(
            phase.generate()
        )

        return self

    def build(self):

        return pd.concat(
            self.datasets,
            ignore_index=True,
            sort=False
        )