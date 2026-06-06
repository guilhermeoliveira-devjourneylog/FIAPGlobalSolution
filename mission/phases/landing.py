import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

from mission.events.landing import LandingEvent


class LandingPhase(MissionPhase):
    """
    Representa a fase de pouso (Landing) da missão.

    Esta fase simula a descida controlada da espaçonave em direção
    à superfície lunar, desde a altitude inicial de aproximação até
    o momento do toque no solo (touchdown).

    Durante essa etapa são monitorados parâmetros críticos de voo,
    como altitude e estado do sistema de pouso, permitindo avaliar
    a segurança e o sucesso da manobra de descida.

    Methods
    -------
    generate()
        Gera os dados sintéticos da fase de pouso.
    """

    def generate(self):
        """
        Gera os dados da fase de pouso lunar.

        Cria uma série temporal de 900 segundos representando a
        sequência de descida da espaçonave. A altitude diminui
        progressivamente até atingir a superfície lunar, enquanto
        eventos de pouso são registrados ao longo da operação.

        Returns
        -------
        pandas.DataFrame
            DataFrame contendo:

            - phase : str
                Nome da fase da missão ("LANDING").
            - time_s : int
                Tempo transcorrido durante a descida, em segundos.
            - altitude_m : float
                Altitude da espaçonave em relação à superfície lunar,
                expressa em metros.
            - touchdown : str
                Estado ou evento relacionado ao processo de pouso.

        Notes
        -----
        A altitude é calculada por interpolação linear:

        - altitude_m ∈ [15000, 0]

        Onde:

        - 15.000 m representa a altitude inicial da descida.
        - 0 m representa o contato com a superfície lunar.

        Os eventos de pouso são gerados por
        ``LandingEvent.touchdown()`` e podem representar etapas como:

        - Início da descida.
        - Desaceleração controlada.
        - Aproximação final.
        - Hover de inspeção.
        - Contato com a superfície.
        - Touchdown confirmado.

        Esta fase corresponde a uma das etapas mais críticas da missão,
        exigindo controle preciso de navegação, propulsão e orientação
        para garantir um pouso seguro.

        Este modelo possui finalidade educacional e de simulação,
        não representando perfis reais de descida utilizados pela NASA.
        """

        t = np.arange(0, 901)

        return pd.DataFrame({

            "phase": "LANDING",

            "time_s": t,

            "altitude_m":
            np.linspace(
                15000,
                0,
                len(t)
            ),

            "touchdown":
            LandingEvent.touchdown(
                len(t)
            )
        })