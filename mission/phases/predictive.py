"""
mission/phases/predictive.py

Sistema de Prognóstico e Predição de Anomalias
para o Artemis Mission Control System.
"""

from dataclasses import dataclass

import numpy as np

from sklearn.linear_model import LinearRegression


@dataclass
class PredictionResult:
    """
    Representa o resultado da análise preditiva de uma métrica
    de telemetria da missão.

    Attributes
    ----------
    metric : str
        Nome da métrica analisada.

    current_value : float
        Último valor observado da métrica.

    predicted_value : float
        Valor estimado para a métrica após o horizonte
        de previsão definido.

    risk : str
        Nível de risco calculado com base na diferença
        entre o valor atual e o valor previsto.

        Valores possíveis:
        - LOW
        - MEDIUM
        - HIGH

    health_score : int
        Índice de saúde atribuído à métrica conforme
        o nível de risco identificado.
    """

    metric: str

    current_value: float

    predicted_value: float

    risk: str

    health_score: int


class PredictiveAnalyzer:
    """
    Sistema de prognóstico e predição de anomalias para o
    Artemis Mission Control System.

    O analisador utiliza regressão linear para identificar
    tendências futuras nas métricas de telemetria geradas
    pelas fases da missão.

    Funcionalidades
    ---------------
    - Previsão de valores futuros.
    - Cálculo de tendência (slope).
    - Classificação de risco operacional.
    - Cálculo de score de saúde.
    - Avaliação automática de todas as métricas numéricas
      de uma fase da missão.

    Attributes
    ----------
    FORECAST_STEPS : int
        Horizonte de previsão utilizado pelo modelo,
        expresso em amostras futuras.
    """

    FORECAST_STEPS = 30

    @staticmethod
    def predict_metric(values):
        """
        Realiza a previsão de uma métrica utilizando
        regressão linear simples.

        O método remove valores ausentes (NaN), ajusta um
        modelo de regressão linear sobre a série temporal
        e projeta o valor esperado após o número de passos
        definido em FORECAST_STEPS.

        Parameters
        ----------
        values : array-like
            Série histórica da métrica.

        Returns
        -------
        tuple[float, float]
            Tupla contendo:

            - predicted_value:
            Valor previsto para o horizonte futuro.

            - slope:
            Inclinação da reta de regressão, indicando
            a tendência da métrica.

        Notes
        -----
        Casos especiais:

        - Série vazia:
        retorna (0.0, 0.0)

        - Série com apenas um valor:
        retorna (valor_atual, 0.0)
        """

        values = np.asarray(
            values,
            dtype=float
        )

        values = values[
            ~np.isnan(values)
        ]

        if len(values) == 0:

            return 0.0, 0.0

        if len(values) == 1:

            return (
                float(values[0]),
                0.0
            )

        x = np.arange(
            len(values)
        ).reshape(-1, 1)

        model = LinearRegression()

        model.fit(
            x,
            values
        )

        future_x = np.array(
            [
                len(values)
                + PredictiveAnalyzer.FORECAST_STEPS
            ]
        ).reshape(-1, 1)

        prediction = model.predict(
            future_x
        )[0]

        slope = float(
            model.coef_[0]
        )

        return (
            float(prediction),
            slope
        )

    @staticmethod
    def risk_level(current, predicted):
        """
        Determina o nível de risco associado à previsão.

        O risco é calculado a partir da variação percentual
        entre o valor atual e o valor previsto.

        Parameters
        ----------
        current : float
            Valor atual da métrica.

        predicted : float
            Valor previsto para a métrica.

        Returns
        -------
        str
            Nível de risco:

            - LOW
            - MEDIUM
            - HIGH

        Rules
        -----
        - Variação > 30% → HIGH
        - Variação > 15% → MEDIUM
        - Caso contrário → LOW
        """

        if current == 0:

            return "LOW"

        variation = abs(
            predicted - current
        ) / abs(current)

        if variation > 0.30:

            return "HIGH"

        if variation > 0.15:

            return "MEDIUM"

        return "LOW"

    @staticmethod
    def health_score(risk):
        """
        Converte um nível de risco em um score de saúde.

        Parameters
        ----------
        risk : str
            Classificação de risco.

        Returns
        -------
        int
            Pontuação de saúde correspondente.

        Mapping
        -------
        LOW    -> 95
        MEDIUM -> 75
        HIGH   -> 45
        """

        if risk == "LOW":

            return 95

        if risk == "MEDIUM":

            return 75

        return 45

    @classmethod
    def analyze(cls, df):
        """
        Executa a análise preditiva de todas as métricas
        numéricas presentes em um dataset de missão.

        Colunas operacionais e eventos são ignorados,
        sendo analisadas apenas métricas numéricas de
        telemetria.

        Para cada métrica válida o método:

        1. Obtém a série histórica.
        2. Calcula a previsão futura.
        3. Determina o nível de risco.
        4. Calcula o score de saúde.
        5. Gera um objeto PredictionResult.

        Parameters
        ----------
        df : pandas.DataFrame
            Dataset contendo os dados da fase da missão.

        Returns
        -------
        tuple[list[PredictionResult], int]

            predictions :
                Lista de resultados preditivos para
                cada métrica analisada.

            phase_score :
                Score médio de saúde da fase.

        Notes
        -----
        As seguintes colunas são ignoradas:

        - phase
        - status
        - eva
        - burn
        - touchdown

        O score da fase é calculado pela média dos
        scores individuais de saúde das métricas.
        """

        predictions = []

        ignored = {
            "phase",
            "status",
            "eva",
            "burn",
            "touchdown"
        }

        numeric_columns = [

            col

            for col in df.columns

            if col not in ignored
            and np.issubdtype(
                df[col].dtype,
                np.number
            )
        ]

        for metric in numeric_columns:

            series = (
                df[metric]
                .dropna()
            )

            if len(series) < 2:

                continue

            current = float(
                series.iloc[-1]
            )

            predicted, slope = (
                cls.predict_metric(
                    series.values
                )
            )

            risk = cls.risk_level(
                current,
                predicted
            )

            health = cls.health_score(
                risk
            )

            predictions.append(

                PredictionResult(
                    metric=metric,
                    current_value=round(
                        current,
                        2
                    ),
                    predicted_value=round(
                        predicted,
                        2
                    ),
                    risk=risk,
                    health_score=health
                )
            )

        if not predictions:

            return [], 0

        phase_score = int(
            np.mean(
                [
                    p.health_score
                    for p in predictions
                ]
            )
        )

        return (
            predictions,
            phase_score
        )