import numpy as np

class ThermalModel:
    """
    Modelo simplificado de telemetria térmica da missão.

    Esta classe fornece métodos para simular o comportamento térmico
    de subsistemas da espaçonave, gerando amostras de temperatura com
    base em distribuições estatísticas.

    O modelo pode ser utilizado para representar temperaturas de
    componentes críticos, como baterias, computadores de bordo,
    tanques de propelente, sistemas de potência e módulos habitáveis.

    Methods
    -------
    temperature(mean, sigma, samples)
        Gera amostras de temperatura seguindo uma distribuição normal.
    """

    @staticmethod
    def temperature(
        mean,
        sigma,
        samples
    ):
        """
        Gera uma série temporal de temperaturas simuladas.

        Os valores são produzidos a partir de uma distribuição normal,
        permitindo representar variações térmicas naturais observadas
        durante as operações da missão.

        Parameters
        ----------
        mean : float
            Temperatura média esperada.

        sigma : float
            Desvio padrão da temperatura.

        samples : int
            Quantidade de amostras a serem geradas.

        Returns
        -------
        numpy.ndarray
            Vetor contendo valores simulados de temperatura.

        Notes
        -----
        A unidade de temperatura (°C, K ou °F) depende do contexto
        da aplicação e deve ser mantida consistente ao longo da missão.
        """
        return np.random.normal(
            mean,
            sigma,
            samples
        )