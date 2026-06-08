"""
mission/phases/anomaly_detection.py

Sistema de Detecção de Anomalias para o Artemis Mission Control System.

Este módulo implementa uma arquitetura extensível para detecção de
anomalias em cada fase da missão Artemis. O objetivo é identificar
desvios operacionais, inconsistências de telemetria e comportamentos
inesperados nos datasets gerados pelos simuladores de missão.

Cada fase possui um detector especializado responsável por validar
a integridade dos dados e aplicar regras específicas de análise
baseadas em limites físicos, tendências temporais e métodos
estatísticos.

Fases suportadas
----------------

LAUNCH
    Detecta:

    - ALTITUDE_DROP
    - VELOCITY_DROP
    - ALTITUDE_STALL
    - VELOCITY_STALL

LEO
    Detecta:

    - ORBITAL_DRIFT

TRANSLUNAR
    Detecta:

    - FUEL_INCREASE
    - EXCESSIVE_FUEL_CONSUMPTION
    - POWER_OUTLIER

NRHO
    Detecta:

    - ORBITAL_DRIFT

RENDEZVOUS
    Detecta:

    - DISTANCE_INCREASE
    - DOCKING_FAILURE

LANDING
    Detecta:

    - ALTITUDE_RISE
    - SURFACE_NOT_REACHED
    - LANDING_FAILURE

SURFACE
    Detecta:

    - POWER_LOSS

Arquitetura
-----------

O módulo utiliza o padrão Strategy através da classe abstrata
``PhaseAnomalyDetector``. Cada fase da missão implementa sua própria
estratégia de detecção, permitindo expansão futura sem modificar
o núcleo do sistema.

O roteamento automático para o detector correto é realizado pela
classe ``MissionAnomalyDetector``.

Métodos de Detecção
-------------------

O sistema combina diferentes abordagens de análise:

1. Regras Físicas
   Verificação de comportamentos impossíveis ou improváveis,
   como aumento de altitude durante o pouso ou aumento de
   distância durante um rendezvous.

2. Análise de Tendência
   Avaliação da evolução temporal de métricas críticas através
   de diferenças sucessivas (delta).

3. Detecção Estatística
   Identificação de outliers utilizando limites baseados em
   múltiplos do desvio padrão (σ).

4. Validação Estrutural
   Verificação automática da presença das colunas obrigatórias
   para cada fase da missão.

Estrutura das Anomalias
-----------------------

Todas as anomalias retornadas seguem o formato:

    {
        "phase": str,
        "index": int,
        "severity": str,
        "anomaly": str
    }

Onde:

- phase:
    Fase da missão onde a anomalia foi detectada.

- index:
    Índice da amostra no DataFrame original.

- severity:
    Nível de criticidade da ocorrência.

    Valores suportados:

    - WARNING
    - CRITICAL

- anomaly:
    Código identificador da anomalia.

Exemplo
-------

>>> anomalies = MissionAnomalyDetector.detect(df)

>>> for anomaly in anomalies:
...     print(anomaly)

Aplicações
----------

Este módulo pode ser utilizado para:

- Monitoramento de missões simuladas.
- Testes de sistemas de telemetria.
- Geração de alertas operacionais.
- Estudos de confiabilidade.
- Demonstrações educacionais.
- Validação de cenários de falha.
- Integração com dashboards de missão.

Notas
-----

Os detectores foram calibrados para os modelos sintéticos utilizados
pelo simulador Artemis Mission Control System. Os limiares e métodos
estatísticos podem ser ajustados para cenários operacionais mais
realistas ou para missões futuras.

Este sistema possui finalidade educacional e de pesquisa, não
representando procedimentos oficiais da NASA ou de outras agências
espaciais.
"""

from abc import ABC, abstractmethod
from typing import List, TypedDict

import pandas as pd


# =====================================================
# TYPES
# =====================================================

class Anomaly(TypedDict):

    phase: str
    index: int
    severity: str
    anomaly: str


# =====================================================
# BASE
# =====================================================

class PhaseAnomalyDetector(ABC):

    REQUIRED_COLUMNS: List[str] = []

    def validate(
        self,
        df: pd.DataFrame
    ) -> None:

        if df.empty:

            raise ValueError(
                "Empty dataframe"
            )

        missing = [

            column

            for column in self.REQUIRED_COLUMNS

            if column not in df.columns

        ]

        if missing:

            raise ValueError(

                f"Missing columns: {missing}"

            )

    @abstractmethod
    def detect(
        self,
        df: pd.DataFrame
    ) -> List[Anomaly]:
        pass


# =====================================================
# LAUNCH
# =====================================================

class LaunchDetector(
    PhaseAnomalyDetector
):

    REQUIRED_COLUMNS = [

        "altitude_km",
        "velocity_ms"

    ]

    ALTITUDE_DROP_LIMIT = -0.5

    VELOCITY_DROP_LIMIT = -10

    def detect(
        self,
        df: pd.DataFrame
    ) -> List[Anomaly]:

        self.validate(df)

        anomalies = []

        altitude_delta = (
            df["altitude_km"]
            .diff()
            .fillna(0)
        )

        velocity_delta = (
            df["velocity_ms"]
            .diff()
            .fillna(0)
        )

        altitude_drop = (
            altitude_delta
            < self.ALTITUDE_DROP_LIMIT
        )

        velocity_drop = (
            velocity_delta
            < self.VELOCITY_DROP_LIMIT
        )

        altitude_stall = (
            altitude_delta <= 0
        )

        velocity_stall = (
            velocity_delta <= 0
        )

        for idx in df[altitude_drop].index:

            anomalies.append({

                "phase": "LAUNCH",
                "index": int(idx),
                "severity": "CRITICAL",
                "anomaly": "ALTITUDE_DROP"

            })

        for idx in df[velocity_drop].index:

            anomalies.append({

                "phase": "LAUNCH",
                "index": int(idx),
                "severity": "CRITICAL",
                "anomaly": "VELOCITY_DROP"

            })

        for idx in df[altitude_stall].index:

            anomalies.append({

                "phase": "LAUNCH",
                "index": int(idx),
                "severity": "WARNING",
                "anomaly": "ALTITUDE_STALL"

            })

        for idx in df[velocity_stall].index:

            anomalies.append({

                "phase": "LAUNCH",
                "index": int(idx),
                "severity": "WARNING",
                "anomaly": "VELOCITY_STALL"

            })

        return anomalies


# =====================================================
# LEO
# =====================================================

class LEODetector(
    PhaseAnomalyDetector
):

    REQUIRED_COLUMNS = [

        "altitude_km"

    ]

    SIGMA_FACTOR = 3

    def detect(
        self,
        df: pd.DataFrame
    ) -> List[Anomaly]:

        self.validate(df)

        anomalies = []

        mean_alt = (
            df["altitude_km"]
            .mean()
        )

        std_alt = (
            df["altitude_km"]
            .std()
        )

        if std_alt == 0:

            return anomalies

        drift = (

            (
                df["altitude_km"]
                - mean_alt
            ).abs()

            >

            (
                self.SIGMA_FACTOR
                * std_alt
            )

        )

        for idx in df[drift].index:

            anomalies.append({

                "phase": "LEO",
                "index": int(idx),
                "severity": "WARNING",
                "anomaly": "ORBITAL_DRIFT"

            })

        return anomalies


# =====================================================
# TRANSLUNAR
# =====================================================

class TranslunarDetector(
    PhaseAnomalyDetector
):

    REQUIRED_COLUMNS = [

        "fuel_pct",
        "power_kw"

    ]

    FUEL_DELTA_LIMIT = 0.5

    SIGMA_FACTOR = 3

    def detect(
        self,
        df: pd.DataFrame
    ) -> List[Anomaly]:

        self.validate(df)

        anomalies = []

        fuel_delta = (

            df["fuel_pct"]
            .diff()
            .fillna(0)

        )

        fuel_increase = (
            fuel_delta > 0
        )

        excessive_fuel = (
            fuel_delta.abs()
            > self.FUEL_DELTA_LIMIT
        )

        mean_power = (
            df["power_kw"]
            .mean()
        )

        std_power = (
            df["power_kw"]
            .std()
        )

        power_problem = pd.Series(
            False,
            index=df.index
        )

        if std_power > 0:

            power_problem = (

                (
                    df["power_kw"]
                    - mean_power
                ).abs()

                >

                (
                    self.SIGMA_FACTOR
                    * std_power
                )

            )

        for idx in df[fuel_increase].index:

            anomalies.append({

                "phase": "TRANSLUNAR",
                "index": int(idx),
                "severity": "CRITICAL",
                "anomaly": "FUEL_INCREASE"

            })

        for idx in df[excessive_fuel].index:

            anomalies.append({

                "phase": "TRANSLUNAR",
                "index": int(idx),
                "severity": "WARNING",
                "anomaly": "EXCESSIVE_FUEL_CONSUMPTION"

            })

        for idx in df[power_problem].index:

            anomalies.append({

                "phase": "TRANSLUNAR",
                "index": int(idx),
                "severity": "WARNING",
                "anomaly": "POWER_OUTLIER"

            })

        return anomalies


# =====================================================
# NRHO
# =====================================================

class NRHODetector(
    PhaseAnomalyDetector
):

    REQUIRED_COLUMNS = [

        "altitude_km"

    ]

    WINDOW = 120

    SIGMA_FACTOR = 3

    def detect(
        self,
        df: pd.DataFrame
    ) -> List[Anomaly]:

        self.validate(df)

        anomalies = []

        rolling_mean = (

            df["altitude_km"]

            .rolling(
                window=self.WINDOW,
                min_periods=10
            )

            .mean()

        )

        rolling_std = (

            df["altitude_km"]

            .rolling(
                window=self.WINDOW,
                min_periods=10
            )

            .std()

            .fillna(0)

        )

        drift = (

            (
                df["altitude_km"]
                - rolling_mean
            ).abs()

            >

            (
                self.SIGMA_FACTOR
                * rolling_std
            )

        )

        drift = drift.fillna(False)

        for idx in df[drift].index:

            anomalies.append({

                "phase": "NRHO",
                "index": int(idx),
                "severity": "WARNING",
                "anomaly": "ORBITAL_DRIFT"

            })

        return anomalies


# =====================================================
# RENDEZVOUS
# =====================================================

class RendezvousDetector(
    PhaseAnomalyDetector
):

    REQUIRED_COLUMNS = [

        "distance_m",
        "status"

    ]

    def detect(
        self,
        df: pd.DataFrame
    ) -> List[Anomaly]:

        self.validate(df)

        anomalies = []

        distance_delta = (

            df["distance_m"]
            .diff()
            .fillna(0)

        )

        distance_increase = (
            distance_delta > 0
        )

        for idx in df[distance_increase].index:

            anomalies.append({

                "phase": "RENDEZVOUS",
                "index": int(idx),
                "severity": "CRITICAL",
                "anomaly": "DISTANCE_INCREASE"

            })

        final_status = str(
            df.iloc[-1]["status"]
        ).upper()

        if final_status != "DOCKED":

            anomalies.append({

                "phase": "RENDEZVOUS",
                "index": len(df) - 1,
                "severity": "CRITICAL",
                "anomaly": "DOCKING_FAILURE"

            })

        return anomalies


# =====================================================
# LANDING
# =====================================================

class LandingDetector(
    PhaseAnomalyDetector
):

    REQUIRED_COLUMNS = [

        "altitude_m",
        "touchdown"

    ]

    def detect(
        self,
        df: pd.DataFrame
    ) -> List[Anomaly]:

        self.validate(df)

        anomalies = []

        altitude_delta = (

            df["altitude_m"]
            .diff()
            .fillna(0)

        )

        altitude_rise = (
            altitude_delta > 0
        )

        for idx in df[altitude_rise].index:

            anomalies.append({

                "phase": "LANDING",
                "index": int(idx),
                "severity": "CRITICAL",
                "anomaly": "ALTITUDE_RISE"

            })

        final_altitude = float(
            df["altitude_m"].iloc[-1]
        )

        if final_altitude > 0:

            anomalies.append({

                "phase": "LANDING",
                "index": len(df) - 1,
                "severity": "CRITICAL",
                "anomaly": "SURFACE_NOT_REACHED"

            })

        touchdown = bool(
            pd.notna(
                df.iloc[-1]["touchdown"]
            )
        )

        if not touchdown:

            anomalies.append({

                "phase": "LANDING",
                "index": len(df) - 1,
                "severity": "CRITICAL",
                "anomaly": "LANDING_FAILURE"

            })

        return anomalies


# =====================================================
# SURFACE
# =====================================================

class SurfaceDetector(
    PhaseAnomalyDetector
):

    REQUIRED_COLUMNS = [

        "solar_power_kw"

    ]

    SIGMA_FACTOR = 3

    def detect(
        self,
        df: pd.DataFrame
    ) -> List[Anomaly]:

        self.validate(df)

        anomalies = []

        mean_power = (
            df["solar_power_kw"]
            .mean()
        )

        std_power = (
            df["solar_power_kw"]
            .std()
        )

        if std_power == 0:

            return anomalies

        power_loss = (

            df["solar_power_kw"]

            <

            (
                mean_power
                - self.SIGMA_FACTOR
                * std_power
            )

        )

        for idx in df[power_loss].index:

            anomalies.append({

                "phase": "SURFACE",
                "index": int(idx),
                "severity": "WARNING",
                "anomaly": "POWER_LOSS"

            })

        return anomalies


# =====================================================
# MAIN DETECTOR
# =====================================================

class MissionAnomalyDetector:

    DETECTORS = {

        "LAUNCH":
            LaunchDetector(),

        "LEO":
            LEODetector(),

        "TRANSLUNAR":
            TranslunarDetector(),

        "NRHO":
            NRHODetector(),

        "RENDEZVOUS":
            RendezvousDetector(),

        "LANDING":
            LandingDetector(),

        "SURFACE":
            SurfaceDetector()

    }

    @classmethod
    def detect(
        cls,
        df: pd.DataFrame
    ) -> List[Anomaly]:

        if df.empty:
            return []

        phase = str(
            df["phase"].iloc[0]
        )

        detector = (
            cls.DETECTORS.get(
                phase
            )
        )

        if detector is None:

            raise ValueError(
                f"Unsupported phase: {phase}"
            )

        return detector.detect(df)