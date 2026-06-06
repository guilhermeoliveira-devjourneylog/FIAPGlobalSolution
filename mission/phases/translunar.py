import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

from mission.telemetry.propulsion import PropulsionModel
from mission.telemetry.power import PowerModel
from mission.events.burns import BurnEvent


class TranslunarPhase(MissionPhase):
    """
    Representa a fase de transferência translunar (Trans-Lunar Injection - TLI).

    Esta fase simula a viagem entre a órbita terrestre e a esfera de
    influência lunar após a execução da manobra de injeção translunar.
    Durante esse período, a espaçonave percorre centenas de milhares
    de quilômetros até alcançar a Lua, realizando correções de trajetória
    e monitoramento contínuo dos sistemas de bordo.

    Os dados gerados incluem distância percorrida, consumo de combustível,
    geração de energia elétrica e eventos de queima dos propulsores.

    Methods
    -------
    generate()
        Gera os dados sintéticos da fase de transferência translunar.
    """

    def generate(self):
        """
        Gera os dados da fase de transferência translunar.

        Cria uma série temporal correspondente a aproximadamente
        72 horas de viagem entre a Terra e a Lua. Durante a simulação,
        são monitorados parâmetros relacionados à navegação, propulsão,
        energia e execução de manobras orbitais.

        Returns
        -------
        pandas.DataFrame
            DataFrame contendo:

            - phase : str
                Nome da fase da missão ("TRANSLUNAR").
            - time_min : int
                Tempo transcorrido na fase, em minutos.
            - distance_km : float
                Distância simulada percorrida em direção à Lua,
                expressa em quilômetros.
            - fuel_pct : float
                Percentual restante de combustível.
            - power_kw : float
                Potência elétrica disponível, em quilowatts.
            - burn : str
                Evento ou estado relacionado às queimas dos motores.

        Notes
        -----
        A distância é calculada por interpolação linear:

        - distance_km ∈ [200000, 384400]

        Onde:

        - 200.000 km representa a posição inicial da fase.
        - 384.400 km representa aproximadamente a distância média
          entre a Terra e a Lua.

        O perfil de combustível é gerado por:

        - ``PropulsionModel.fuel_profile(100, 65, n)``

        simulando a redução gradual do combustível de 100% para 65%
        ao longo da transferência.

        A potência elétrica é obtida por:

        - ``PowerModel.power_kw(n)``

        representando a produção energética dos sistemas da espaçonave.

        Os eventos de propulsão são produzidos por:

        - ``BurnEvent.generate(n)``

        podendo representar:

        - Injeção translunar (TLI).
        - Correções de trajetória (MCC).
        - Ajustes de atitude.
        - Queimas programadas.
        - Períodos de voo balístico.

        Esta fase é fundamental para garantir que a espaçonave alcance
        corretamente a órbita lunar com consumo otimizado de combustível.

        Este modelo possui finalidade educacional e de simulação,
        não representando trajetórias reais, efemérides ou parâmetros
        operacionais da missão Artemis.
        """

        t = np.arange(0, 72 * 60)

        n = len(t)

        return pd.DataFrame({

            "phase": "TRANSLUNAR",

            "time_min": t,

            "distance_km":
            np.linspace(
                200000,
                384400,
                n
            ),

            "fuel_pct":
            PropulsionModel.fuel_profile(
                100,
                65,
                n
            ),

            "power_kw":
            PowerModel.power_kw(n),

            "burn":
            BurnEvent.generate(n)
        })