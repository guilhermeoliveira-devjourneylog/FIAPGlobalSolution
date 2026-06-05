from mission.phases.launch import LaunchPhase
from mission.phases.leo import LEOPhase
from mission.phases.translunar import TranslunarPhase
from mission.phases.nrho import NRHOPhase
from mission.phases.rendezvous import RendezvousPhase
from mission.phases.landing import LandingPhase
from mission.phases.surface import SurfacePhase

class PhaseFactory:

    @staticmethod
    def create(name):

        phases = {

            "launch": LaunchPhase,
            "leo": LEOPhase,
            "translunar": TranslunarPhase,
            "nrho": NRHOPhase,
            "rendezvous": RendezvousPhase,
            "landing": LandingPhase,
            "surface": SurfacePhase
        }

        return phases[name]()