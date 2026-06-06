import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

class LEOPhase(MissionPhase):
    """
    Representa a fase de órbita baixa da Terra (Low Earth Orbit - LEO).

    Esta fase simula a permanência da espaçonave em órbita terrestre
    baixa após a inserção orbital. Durante esse período, os sistemas
    da missão realizam verificações operacionais, validação de
    subsistemas e preparação para as próximas manobras orbitais.

    Os dados gerados incluem altitude e velocidade orbital ao longo
    do tempo, incorporando pequenas variações aleatórias para simular
    oscilações naturais observadas em missões espaciais reais.

    Methods
    -------
    generate()
        Gera os dados sintéticos da fase de órbita baixa da Terra.
    """

    def generate(self):
        """
        Gera os dados da fase de órbita terrestre baixa (LEO).

        Cria uma série temporal de 181 minutos representando a
        permanência da espaçonave em órbita baixa da Terra. Os valores
        de altitude e velocidade são simulados por distribuições
        normais para reproduzir pequenas flutuações operacionais.

        Returns
        -------
        pandas.DataFrame
            DataFrame contendo:

            - phase : str
                Nome da fase da missão ("LEO").
            - time_min : int
                Tempo transcorrido na fase, em minutos.
            - altitude_km : float
                Altitude orbital simulada, em quilômetros.
            - velocity_kmh : float
                Velocidade orbital simulada, em quilômetros por hora.

        Notes
        -----
        Os valores são gerados utilizando distribuições normais:

        - altitude_km ~ N(185, 1)
        - velocity_kmh ~ N(28000, 50)

        Onde:

        - 185 km representa a altitude média da órbita.
        - 1 km representa a variação padrão da altitude.
        - 28.000 km/h representa a velocidade orbital média.
        - 50 km/h representa a variação padrão da velocidade.

        Este modelo possui finalidade educacional e de simulação,
        não representando dados reais de uma missão Artemis.
        """

        t = np.arange(0, 181)

        return pd.DataFrame({

            "phase": "LEO",

            "time_min": t,

            "altitude_km":
            np.random.normal(
                185,
                1,
                len(t)
            ),

            "velocity_kmh":
            np.random.normal(
                28000,
                50,
                len(t)
            )
        })