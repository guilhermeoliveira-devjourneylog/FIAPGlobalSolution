"""
mission/phases/anomaly_detection.py

Sistema de detecção de anomalias para a missão Artemis.
"""

from typing import List, Dict

import pandas as pd


class MissionAnomalyDetector:
    """
    Sistema centralizado de detecção de anomalias para a missão Artemis.

    Esta classe é responsável por analisar os datasets gerados pelas
    diferentes fases da missão e identificar comportamentos anormais
    que possam indicar falhas operacionais, degradação de sistemas,
    desvios de trajetória ou condições críticas de missão.

    O detector utiliza regras determinísticas específicas para cada
    fase, avaliando métricas de telemetria como altitude, velocidade,
    combustível, potência, distância de aproximação e status
    operacional.

    Fases suportadas
    ----------------
    - LAUNCH
        * ALTITUDE_DROP
        * VELOCITY_DROP

    - LEO
        * ORBITAL_DRIFT

    - TRANSLUNAR
        * FUEL_INCREASE
        * EXCESSIVE_FUEL_CONSUMPTION
        * POWER_OUT_OF_RANGE

    - NRHO
        * ORBITAL_DRIFT

    - RENDEZVOUS
        * DISTANCE_INCREASE
        * DOCKING_FAILURE

    - LANDING
        * ALTITUDE_RISE
        * LANDING_FAILURE

    - SURFACE
        * POWER_LOSS

    Severidades
    ------------
    WARNING
        Indica uma condição fora do comportamento esperado que deve
        ser monitorada, mas que não representa falha imediata.

    CRITICAL
        Indica uma condição potencialmente perigosa que pode
        comprometer o sucesso da missão ou a segurança da nave.

    Estrutura da anomalia retornada
    --------------------------------
    Cada anomalia é representada por um dicionário contendo:

    - phase:
        Nome da fase da missão.

    - index:
        Índice da amostra onde a anomalia foi detectada.

    - severity:
        Nível de criticidade da ocorrência.

    - anomaly:
        Código identificador da anomalia.

    Exemplo
    --------
    >>> anomalies = MissionAnomalyDetector.detect(df)

    >>> anomalies[0]
    {
        "phase": "TRANSLUNAR",
        "index": 532,
        "severity": "CRITICAL",
        "anomaly": "FUEL_INCREASE"
    }

    Notes
    -----
    - O detector assume que o DataFrame recebido contém dados de
      apenas uma fase da missão.
    - Caso o DataFrame esteja vazio, nenhuma anomalia é retornada.
    - As regras implementadas são baseadas em limites operacionais e
      comportamentos físicos esperados para cada etapa da missão.
    - O sistema pode ser expandido futuramente para incluir métodos
      estatísticos, aprendizado de máquina e análise preditiva.
    """

    @staticmethod
    def detect(df: pd.DataFrame) -> List[Dict]:
        """
        Executa a detecção de anomalias.

        Parameters
        ----------
        df : pandas.DataFrame
            Dataset da fase da missão.

        Returns
        -------
        list[dict]
            Lista contendo todas as anomalias encontradas.
        """

        anomalies = []

        if df.empty:
            return anomalies

        phase = df["phase"].iloc[0]

        # =====================================================
        # LAUNCH
        # =====================================================

        if phase == "LAUNCH":

            altitude_drop = (
                df["altitude_km"].diff() < 0
            )

            velocity_drop = (
                df["velocity_ms"].diff() < 0
            )

            for idx in df[altitude_drop].index:

                anomalies.append({

                    "phase": phase,
                    "index": int(idx),
                    "severity": "CRITICAL",
                    "anomaly": "ALTITUDE_DROP"

                })

            for idx in df[velocity_drop].index:

                anomalies.append({

                    "phase": phase,
                    "index": int(idx),
                    "severity": "CRITICAL",
                    "anomaly": "VELOCITY_DROP"

                })

        # =====================================================
        # LEO
        # =====================================================

        elif phase == "LEO":

            rolling_mean = (
                df["altitude_km"]
                .rolling(
                    window=20,
                    min_periods=1
                )
                .mean()
            )

            orbital_drift = (

                (
                    df["altitude_km"]
                    - rolling_mean
                )
                .abs()
                > 3

            )

            for idx in df[orbital_drift].index:

                anomalies.append({

                    "phase": phase,
                    "index": int(idx),
                    "severity": "WARNING",
                    "anomaly": "ORBITAL_DRIFT"

                })

        # =====================================================
        # TRANSLUNAR
        # =====================================================

        elif phase == "TRANSLUNAR":

            fuel_delta = (
                df["fuel_pct"]
                .diff()
            )

            fuel_increase = (
                fuel_delta > 0
            )

            excessive_fuel = (
                fuel_delta.abs() > 0.10
            )

            power_problem = (

                (df["power_kw"] < 70)
                |
                (df["power_kw"] > 120)

            )

            for idx in df[fuel_increase].index:

                anomalies.append({

                    "phase": phase,
                    "index": int(idx),
                    "severity": "CRITICAL",
                    "anomaly": "FUEL_INCREASE"

                })

            for idx in df[excessive_fuel].index:

                anomalies.append({

                    "phase": phase,
                    "index": int(idx),
                    "severity": "WARNING",
                    "anomaly": "EXCESSIVE_FUEL_CONSUMPTION"

                })

            for idx in df[power_problem].index:

                anomalies.append({

                    "phase": phase,
                    "index": int(idx),
                    "severity": "WARNING",
                    "anomaly": "POWER_OUT_OF_RANGE"

                })

        # =====================================================
        # NRHO
        # =====================================================

        elif phase == "NRHO":

            rolling_mean = (
                df["altitude_km"]
                .rolling(
                    window=120,
                    min_periods=1
                )
                .mean()
            )

            orbital_drift = (

                (
                    df["altitude_km"]
                    - rolling_mean
                )
                .abs()
                > 3000

            )

            for idx in df[orbital_drift].index:

                anomalies.append({

                    "phase": phase,
                    "index": int(idx),
                    "severity": "WARNING",
                    "anomaly": "ORBITAL_DRIFT"

                })

        # =====================================================
        # RENDEZVOUS
        # =====================================================

        elif phase == "RENDEZVOUS":

            distance_increase = (

                df["distance_m"]
                .diff()
                > 0

            )

            for idx in df[distance_increase].index:

                anomalies.append({

                    "phase": phase,
                    "index": int(idx),
                    "severity": "CRITICAL",
                    "anomaly": "DISTANCE_INCREASE"

                })

            if df.iloc[-1]["status"] != "DOCKED":

                anomalies.append({

                    "phase": phase,
                    "index": len(df) - 1,
                    "severity": "CRITICAL",
                    "anomaly": "DOCKING_FAILURE"

                })

        # =====================================================
        # LANDING
        # =====================================================

        elif phase == "LANDING":

            altitude_rise = (

                df["altitude_m"]
                .diff()
                > 0

            )

            for idx in df[altitude_rise].index:

                anomalies.append({

                    "phase": phase,
                    "index": int(idx),
                    "severity": "CRITICAL",
                    "anomaly": "ALTITUDE_RISE"

                })

            touchdown = bool(
                df.iloc[-1]["touchdown"]
            )

            if not touchdown:

                anomalies.append({

                    "phase": phase,
                    "index": len(df) - 1,
                    "severity": "CRITICAL",
                    "anomaly": "LANDING_FAILURE"

                })

        # =====================================================
        # SURFACE
        # =====================================================

        elif phase == "SURFACE":

            power_loss = (

                df["solar_power_kw"]
                < 70

            )

            for idx in df[power_loss].index:

                anomalies.append({

                    "phase": phase,
                    "index": int(idx),
                    "severity": "WARNING",
                    "anomaly": "POWER_LOSS"

                })

        return anomalies