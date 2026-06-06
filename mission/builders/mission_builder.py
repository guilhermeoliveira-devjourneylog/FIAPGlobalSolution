import pandas as pd

from mission.factory.phase_factory import PhaseFactory

class MissionBuilder:
    """
    Constrói o dataset completo da missão por meio da composição
    sequencial de múltiplas fases.

    A classe utiliza o padrão Builder para permitir a adição encadeada
    de fases da missão e, ao final, consolidar todos os DataFrames
    gerados em um único conjunto de dados cronológico.

    Cada fase é criada dinamicamente pela ``PhaseFactory`` e deve
    implementar o método ``generate()``, responsável por retornar
    um ``pandas.DataFrame`` contendo os eventos, métricas e estados
    daquela etapa da missão.

    Attributes
    ----------
    datasets : list[pandas.DataFrame]
        Lista de DataFrames gerados pelas fases adicionadas ao builder.

    Examples
    --------
    >>> mission = (
    ...     MissionBuilder()
    ...     .add_phase("LAUNCH")
    ...     .add_phase("LEO")
    ...     .add_phase("TRANSLUNAR")
    ...     .build()
    ... )

    >>> print(mission.head())

    Notes
    -----
    O método ``add_phase()`` retorna a própria instância do builder,
    permitindo a construção fluente (method chaining).

    Returns
    -------
    pandas.DataFrame
        DataFrame consolidado contendo todas as fases da missão.
    """

    def __init__(self):
        """
        Inicializa o construtor da missão.

        Cria uma lista vazia que armazenará os DataFrames gerados
        por cada fase adicionada ao fluxo da missão.
        """
        self.datasets = []

    def add_phase(self, name):
        """
        Adiciona uma fase ao fluxo da missão.

        A fase é instanciada através da ``PhaseFactory`` e seu
        dataset é gerado automaticamente por meio do método
        ``generate()``.

        Parameters
        ----------
        name : str
            Nome da fase da missão a ser adicionada.

        Returns
        -------
        MissionBuilder
            A própria instância do builder para permitir
            encadeamento de chamadas.

        Raises
        ------
        ValueError
            Caso a fase informada não esteja registrada
            na ``PhaseFactory``.
        """
        phase = PhaseFactory.create(name)

        self.datasets.append(
            phase.generate()
        )

        return self

    def build(self):
        """
        Consolida todas as fases adicionadas em um único DataFrame.

        Os datasets são concatenados preservando a ordem de inserção
        das fases e reiniciando os índices do resultado final.

        Returns
        -------
        pandas.DataFrame
            Dataset completo da missão contendo todas as fases
            adicionadas ao builder.

        Notes
        -----
        Utiliza ``pandas.concat()`` com:

        - ``ignore_index=True`` para recriar os índices;
        - ``sort=False`` para preservar a estrutura original
          das colunas sem ordenação automática.
        """
        return pd.concat(
            self.datasets,
            ignore_index=True,
            sort=False
        )