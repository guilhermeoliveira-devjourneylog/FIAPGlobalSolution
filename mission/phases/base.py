from abc import ABC, abstractmethod

class MissionPhase(ABC):
    """
    Classe abstrata base para todas as fases da missão.

    Esta interface define o contrato que deve ser implementado por
    qualquer fase do sistema de simulação da missão Artemis. Cada
    fase é responsável por gerar e retornar um conjunto de dados
    sintéticos representando métricas, eventos e telemetria do
    respectivo estágio da missão.

    Classes derivadas devem implementar o método ``generate()``,
    retornando normalmente um objeto ``pandas.DataFrame`` contendo
    os dados da fase.

    Examples
    --------
    >>> class LaunchPhase(MissionPhase):
    ...     def generate(self):
    ...         return dataframe

    Methods
    -------
    generate()
        Gera os dados correspondentes à fase da missão.
    """

    @abstractmethod
    def generate(self):
        """
        Gera os dados da fase da missão.

        Este método deve ser implementado pelas subclasses para criar
        e retornar os dados de telemetria, eventos e indicadores
        específicos da fase representada.

        Returns
        -------
        pandas.DataFrame
            DataFrame contendo os dados gerados para a fase da missão.

        Raises
        ------
        NotImplementedError
            Caso o método não seja implementado pela subclasse.
        """
        pass