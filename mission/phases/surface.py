import numpy as np
import pandas as pd

from mission.phases.base import MissionPhase

from mission.events.eva import EVAEvent


class SurfacePhase(MissionPhase):
    """
    Representa a fase de operações na superfície lunar.

    Esta fase simula as atividades executadas após o pouso bem-sucedido
    na Lua. Durante este período, astronautas realizam atividades
    extraveiculares (EVAs), experimentos científicos, coleta de amostras,
    manutenção de equipamentos e operações de suporte à futura presença
    humana sustentável na superfície lunar.

    Os dados gerados incluem a produção de energia solar da base ou
    módulo de superfície e o estado das atividades EVA ao longo da missão.

    Methods
    -------
    generate()
        Gera os dados sintéticos da fase de operações na superfície lunar.
    """

    def generate(self):
        """
        Gera os dados da fase de superfície lunar.

        Cria uma série temporal representando as operações realizadas
        na superfície da Lua, incluindo monitoramento da geração de
        energia solar e registro das atividades extraveiculares (EVAs)
        realizadas pela tripulação.

        Returns
        -------
        pandas.DataFrame
            DataFrame contendo:

            - phase : str
                Nome da fase da missão ("SURFACE").
            - time_step : int
                Unidade temporal da simulação.
            - solar_power_kw : float
                Potência gerada pelo sistema solar da missão,
                expressa em quilowatts.
            - eva : str
                Estado ou atividade EVA executada pela tripulação.

        Notes
        -----
        A geração de energia é simulada utilizando uma distribuição
        normal:

        - solar_power_kw ~ N(95, 5)

        Onde:

        - 95 kW representa a potência média disponível.
        - 5 kW representa a variação operacional da geração.

        As atividades EVA são produzidas por
        ``EVAEvent.activity()`` e podem representar eventos como:

        - Preparação para EVA.
        - Saída da tripulação.
        - Exploração científica.
        - Coleta de amostras.
        - Instalação de equipamentos.
        - Retorno ao habitat.

        Esta fase representa um dos principais objetivos do programa
        Artemis: estabelecer uma presença humana sustentável na Lua
        e preparar futuras missões para Marte.

        Este modelo possui finalidade educacional e de simulação,
        não representando cronogramas ou operações reais da NASA.
        """

        t = np.arange(0, 5000)

        return pd.DataFrame({

            "phase": "SURFACE",

            "time_step": t,

            "solar_power_kw":
            np.random.normal(
                95,
                5,
                len(t)
            ),

            "eva":
            EVAEvent.activity(
                len(t)
            )
        })