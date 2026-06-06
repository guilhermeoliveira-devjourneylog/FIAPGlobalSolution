import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

from mission.events.docking import DockingEvent


class RendezvousPhase(MissionPhase):
    """
    Representa a fase de rendezvous e acoplamento da missão.

    Esta fase simula a aproximação controlada da espaçonave em direção
    ao seu veículo-alvo, como o Gateway lunar, módulo de pouso ou outra
    espaçonave. Durante a operação, a distância relativa entre os
    veículos é gradualmente reduzida até atingir a condição necessária
    para o acoplamento.

    Além da distância relativa, são gerados estados operacionais que
    representam o progresso da sequência de aproximação e docking.

    Methods
    -------
    generate()
        Gera os dados sintéticos da fase de rendezvous e acoplamento.
    """

    def generate(self):
        """
        Gera os dados da fase de rendezvous.

        Cria uma série temporal de 1.800 segundos representando a
        aproximação progressiva da espaçonave ao alvo orbital. A
        distância relativa diminui linearmente até atingir zero,
        simulando o momento do acoplamento.

        O estado operacional da manobra é obtido através do gerador
        de eventos de docking.

        Returns
        -------
        pandas.DataFrame
            DataFrame contendo:

            - phase : str
                Nome da fase da missão ("RENDEZVOUS").
            - time_s : int
                Tempo transcorrido na fase, em segundos.
            - distance_m : float
                Distância relativa ao alvo, em metros.
            - status : str
                Estado operacional da sequência de aproximação e
                acoplamento.

        Notes
        -----
        A distância relativa é calculada por interpolação linear:

        - distance_m ∈ [1000, 0]

        Onde:

        - 1000 m representa a separação inicial.
        - 0 m representa a condição de contato/acoplamento.

        Os estados operacionais são produzidos por
        ``DockingEvent.status()`` e podem representar etapas como:

        - Aproximação inicial.
        - Aproximação final.
        - Estação de espera.
        - Captura suave (Soft Capture).
        - Acoplamento concluído (Hard Docking).

        Este modelo possui finalidade educacional e de simulação,
        não reproduzindo algoritmos reais de navegação relativa,
        sensores de proximidade ou sistemas automáticos de docking.
        """

        t = np.arange(0, 1801)

        return pd.DataFrame({

            "phase": "RENDEZVOUS",

            "time_s": t,

            "distance_m":
            np.linspace(
                1000,
                0,
                len(t)
            ),

            "status":
            DockingEvent.status(
                len(t)
            )
        })