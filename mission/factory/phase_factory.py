from mission.phases.launch import LaunchPhase
from mission.phases.leo import LEOPhase
from mission.phases.translunar import TranslunarPhase
from mission.phases.nrho import NRHOPhase
from mission.phases.rendezvous import RendezvousPhase
from mission.phases.landing import LandingPhase
from mission.phases.surface import SurfacePhase

class PhaseFactory:
    """
    Fábrica de Fases da Missão Artemis.

    Esta classe implementa o padrão de projeto Factory,
    sendo responsável por instanciar dinamicamente a
    fase correspondente da missão a partir de um nome
    informado pelo usuário ou sistema.

    Fases suportadas:
        - launch       : Lançamento da missão.
        - leo          : Órbita Baixa da Terra (LEO).
        - translunar   : Transferência Terra-Lua.
        - nrho         : Órbita Near Rectilinear Halo Orbit.
        - rendezvous   : Encontro e acoplamento orbital.
        - landing      : Pouso lunar.
        - surface      : Operações na superfície lunar.

    Methods
    -------
    create(name: str)
        Cria e retorna uma instância da fase solicitada.

    Parameters
    ----------
    name : str
        Nome da fase da missão.

    Returns
    -------
    MissionPhase
        Instância da fase correspondente.

    Raises
    ------
    KeyError
        Caso o nome informado não corresponda a uma
        fase registrada na fábrica.

    Examples
    --------
    >>> phase = PhaseFactory.create("launch")
    >>> phase.generate()

    >>> phase = PhaseFactory.create("landing")
    >>> df = phase.generate()
    """

    @staticmethod
    def create(name):
        """
        Cria uma instância da fase especificada.

        Parameters
        ----------
        name : str
            Nome identificador da fase.

        Returns
        -------
        MissionPhase
            Objeto da fase correspondente.

        Raises
        ------
        KeyError
            Se a fase informada não existir.
        """
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