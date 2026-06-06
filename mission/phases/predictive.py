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

    metric: str

    current_value: float

    predicted_value: float

    risk: str

    health_score: int


class PredictiveAnalyzer:

    FORECAST_STEPS = 30

    @staticmethod
    def predict_metric(values):

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
    def risk_level(
        current,
        predicted
    ):

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

        if risk == "LOW":

            return 95

        if risk == "MEDIUM":

            return 75

        return 45

    @classmethod
    def analyze(
        cls,
        df
    ):

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