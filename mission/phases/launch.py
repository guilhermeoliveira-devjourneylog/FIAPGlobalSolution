import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

class LaunchPhase(MissionPhase):
    """
    Representa a fase de lançamento (Launch) da missão Artemis.

    Esta fase simula os primeiros 600 segundos da missão, abrangendo
    a decolagem e a ascensão inicial do veículo lançador. Os dados
    gerados incluem tempo de missão, altitude e velocidade, permitindo
    análises de desempenho e visualização da evolução dos parâmetros
    de voo durante o lançamento.

    A implementação utiliza um modelo simplificado com crescimento
    linear de altitude e velocidade ao longo do tempo.

    Methods
    -------
    generate()
        Gera os dados sintéticos da fase de lançamento.
    """

    def generate(self):
        """
        Gera os dados da fase de lançamento.

        Cria uma série temporal de 0 a 600 segundos contendo
        informações simuladas de altitude e velocidade durante
        a ascensão inicial da missão.

        Returns
        -------
        pandas.DataFrame
            DataFrame contendo:

            - phase : str
                Nome da fase da missão ("LAUNCH").
            - time_s : int
                Tempo transcorrido desde o lançamento, em segundos.
            - altitude_km : float
                Altitude estimada da espaçonave, em quilômetros.
            - velocity_ms : float
                Velocidade estimada da espaçonave, em metros por segundo.

        Notes
        -----
        As métricas são calculadas utilizando relações lineares:

        - altitude_km = time_s × 0.45
        - velocity_ms = time_s × 20

        Este modelo tem finalidade educacional e de simulação,
        não representando dados reais de desempenho de veículos
        espaciais.
        """

        t = np.arange(0, 601)

        altitude = t * 0.45

        velocity = t * 20

        return pd.DataFrame({

            "phase": "LAUNCH",

            "time_s": t,

            "altitude_km": altitude,

            "velocity_ms": velocity
        })