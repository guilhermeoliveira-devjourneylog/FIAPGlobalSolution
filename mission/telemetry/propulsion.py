import numpy as np

class PropulsionModel:
    """
    Modelo simplificado de telemetria de propulsão da missão.

    Esta classe fornece métodos estáticos para simular o comportamento
    do sistema de propulsão da espaçonave, incluindo o consumo de
    combustível ao longo do tempo e os níveis de empuxo produzidos
    pelos motores.

    Os dados gerados podem ser utilizados para monitoramento de missão,
    análises de desempenho, detecção de anomalias e algoritmos de
    prognóstico durante diferentes fases operacionais.

    Methods
    -------
    fuel_profile(start, end, samples)
        Gera uma curva linear de consumo de combustível.

    engine_thrust(samples)
        Gera amostras simuladas de empuxo dos motores.
    """

    @staticmethod
    def fuel_profile(start, end, samples):
        """
        Gera uma série temporal de combustível disponível.

        Parameters
        ----------
        start : float
            Quantidade inicial de combustível (% ou unidade definida
            pela aplicação).

        end : float
            Quantidade final de combustível.

        samples : int
            Número de amostras a serem geradas.

        Returns
        -------
        numpy.ndarray
            Vetor contendo a evolução linear do combustível entre
            os valores inicial e final.
        """
        return np.linspace(
            start,
            end,
            samples
        )

    @staticmethod
    def engine_thrust(samples):
        """
        Gera amostras simuladas de empuxo dos motores.

        O empuxo é modelado por uma distribuição normal com média
        de 95% e desvio padrão de 2%, representando pequenas
        oscilações operacionais. Os valores são limitados ao
        intervalo de 0% a 100%.

        Parameters
        ----------
        samples : int
            Quantidade de amostras a serem geradas.

        Returns
        -------
        numpy.ndarray
            Vetor contendo valores de empuxo do motor em percentual.
        """
        return np.clip(
            np.random.normal(
                95,
                2,
                samples
            ),
            0,
            100
        )