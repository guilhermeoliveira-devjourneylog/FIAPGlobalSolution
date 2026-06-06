import numpy as np

class PowerModel:
    """
    Modelo simplificado de geração de telemetria elétrica da missão.

    Esta classe fornece métodos estáticos para simular o comportamento
    do sistema de potência da espaçonave, incluindo a descarga da bateria
    ao longo do tempo e o consumo instantâneo de energia.

    Os dados gerados são utilizados pelas fases da missão para compor
    conjuntos de telemetria realistas destinados a análises operacionais,
    monitoramento de saúde do sistema e algoritmos de prognóstico.

    Methods
    -------
    battery(start, end, samples)
        Gera uma curva linear de carga da bateria entre dois valores.

    power_kw(samples)
        Gera amostras de consumo elétrico em quilowatts utilizando
        distribuição normal.
    """

    @staticmethod
    def battery(start, end, samples):
        """
        Gera uma série temporal de carga da bateria.

        Parameters
        ----------
        start : float
            Valor inicial da carga da bateria (%).

        end : float
            Valor final da carga da bateria (%).

        samples : int
            Quantidade de amostras a serem geradas.

        Returns
        -------
        numpy.ndarray
            Vetor contendo a evolução linear da carga da bateria
            entre os valores especificados.
        """
        return np.linspace(
            start,
            end,
            samples
        )

    @staticmethod
    def power_kw(samples):
        """
        Gera amostras simuladas de consumo elétrico.

        O consumo é modelado por uma distribuição normal com média
        de 22 kW e desvio padrão de 0,5 kW, representando pequenas
        variações operacionais do sistema elétrico da missão.

        Parameters
        ----------
        samples : int
            Quantidade de amostras a serem geradas.

        Returns
        -------
        numpy.ndarray
            Vetor contendo valores de potência elétrica em kW.
        """
        return np.random.normal(
            22,
            0.5,
            samples
        )