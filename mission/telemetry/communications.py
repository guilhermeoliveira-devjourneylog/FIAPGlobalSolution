import numpy as np

class CommunicationModel:
    """
    Modelo simplificado de telemetria de comunicações da missão.

    Esta classe fornece métodos para simular o desempenho do sistema
    de comunicação da espaçonave, gerando métricas relacionadas à
    qualidade do sinal entre a nave, satélites de retransmissão,
    estações terrestres ou infraestrutura orbital.

    Os dados produzidos podem ser utilizados para monitoramento de
    enlace, análise operacional, detecção de degradações e sistemas
    de prognóstico durante as diferentes fases da missão.

    Methods
    -------
    signal(samples)
        Gera amostras simuladas da qualidade do sinal de comunicação.
    """

    @staticmethod
    def signal(samples):
        """
        Gera amostras simuladas de qualidade do sinal.

        A qualidade do sinal é modelada por uma distribuição normal
        com média de 98% e desvio padrão de 0,8%, representando
        pequenas flutuações típicas dos enlaces de comunicação
        espaciais.

        Parameters
        ----------
        samples : int
            Quantidade de amostras a serem geradas.

        Returns
        -------
        numpy.ndarray
            Vetor contendo os valores simulados de qualidade do sinal.

        Notes
        -----
        Os valores podem representar métricas como intensidade do sinal,
        disponibilidade do enlace, qualidade da comunicação ou outro
        indicador equivalente definido pela aplicação.
        """
        return np.random.normal(
            98,
            0.8,
            samples
        )