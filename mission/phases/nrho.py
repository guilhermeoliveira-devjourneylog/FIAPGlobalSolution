import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

class NRHOPhase(MissionPhase):
    """
    Representa a fase de órbita quase retilínea de halo
    (Near Rectilinear Halo Orbit - NRHO).

    Esta fase simula a permanência da espaçonave na órbita NRHO
    ao redor da Lua, órbita selecionada para o programa Artemis
    devido à sua elevada estabilidade dinâmica, baixo consumo de
    combustível para manutenção orbital e facilidade de acesso à
    superfície lunar e ao Gateway.

    Durante esta etapa, a espaçonave permanece em órbita lunar por
    aproximadamente uma semana, permitindo operações de transferência,
    observação, acoplamento e preparação para missões de pouso lunar.

    Methods
    -------
    generate()
        Gera os dados sintéticos da fase NRHO.
    """

    def generate(self):
        """
        Gera os dados da fase de órbita NRHO.

        Cria uma série temporal correspondente a sete dias de operação
        contínua em órbita lunar. A altitude é simulada utilizando uma
        distribuição normal para representar pequenas variações orbitais
        ao longo da missão.

        Returns
        -------
        pandas.DataFrame
            DataFrame contendo:

            - phase : str
                Nome da fase da missão ("NRHO").
            - time_min : int
                Tempo transcorrido na fase, em minutos.
            - altitude_km : float
                Altitude simulada da espaçonave em relação à Lua,
                expressa em quilômetros.

        Notes
        -----
        Os valores de altitude são gerados utilizando uma distribuição
        normal:

        - altitude_km ~ N(70000, 500)

        Onde:

        - 70.000 km representa a altitude média da órbita NRHO.
        - 500 km representa a variação padrão da altitude.

        A órbita NRHO é uma órbita altamente elíptica associada ao
        sistema gravitacional Terra-Lua e foi escolhida como órbita
        operacional do Gateway devido à sua estabilidade e eficiência
        para missões Artemis.

        Este modelo possui finalidade educacional e de simulação,
        não representando efemérides reais ou parâmetros orbitais
        exatos da missão.
        """

        t = np.arange(0, 7 * 24 * 60)

        return pd.DataFrame({

            "phase": "NRHO",

            "time_min": t,

            "altitude_km":
            np.random.normal(
                70000,
                500,
                len(t)
            )
        })