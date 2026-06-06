import numpy as np

class GNCModel:
    """
    Modelo simplificado de telemetria de Guiagem, Navegação e Controle (GNC).

    Esta classe fornece métodos para simular parâmetros críticos do
    sistema GNC da espaçonave, incluindo erros de navegação e atitudes
    (orientação angular) nos três eixos principais.

    Os dados gerados podem ser utilizados para monitoramento operacional,
    validação de algoritmos de controle, análise de desempenho de missão
    e sistemas de prognóstico e detecção de anomalias.

    Methods
    -------
    navigation_error(samples)
        Gera amostras de erro de navegação.

    attitude(samples)
        Gera amostras de atitude nos eixos Roll, Pitch e Yaw.
    """

    @staticmethod
    def navigation_error(samples):
        """
        Gera amostras simuladas de erro de navegação.

        O erro é modelado por uma distribuição normal com média de
        1 unidade e desvio padrão de 0,3. O valor absoluto é aplicado
        para garantir que os erros permaneçam não negativos.

        Parameters
        ----------
        samples : int
            Quantidade de amostras a serem geradas.

        Returns
        -------
        numpy.ndarray
            Vetor contendo os valores simulados de erro de navegação.
        """
        return np.abs(
            np.random.normal(
                1,
                0.3,
                samples
            )
        )

    @staticmethod
    def attitude(samples):
        """
        Gera amostras simuladas da atitude da espaçonave.

        A atitude é representada por três séries independentes,
        correspondentes aos eixos Roll, Pitch e Yaw. Cada eixo é
        modelado por uma distribuição normal centrada em zero,
        representando pequenas oscilações em torno da orientação
        nominal.

        Parameters
        ----------
        samples : int
            Quantidade de amostras a serem geradas para cada eixo.

        Returns
        -------
        tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]
            Tupla contendo três vetores correspondentes aos ângulos
            de Roll, Pitch e Yaw, respectivamente.

        Notes
        -----
        A unidade angular (graus ou radianos) depende da convenção
        adotada pela aplicação e deve permanecer consistente em todo
        o sistema.
        """
        return (
            np.random.normal(0, 0.5, samples),
            np.random.normal(0, 0.5, samples),
            np.random.normal(0, 0.5, samples)
        )