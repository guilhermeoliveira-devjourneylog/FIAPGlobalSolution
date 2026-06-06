# =========================================================
# ARTEMIS MISSION CONTROL SYSTEM
# =========================================================
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mission.builders.mission_builder import MissionBuilder

from mission.exporters.csv import CSVExporter
from mission.exporters.parquet import ParquetExporter

from mission.visualization.mission_console import (
    MissionConsole
)

from mission.phases.anomaly_detection import (
    MissionAnomalyDetector
)

from mission.phases.predictive import (
    PredictiveAnalyzer
)

viewer = MissionConsole()

viewer.render_boot_screen()

viewer.render_dataset_generation()

mission = (
    MissionBuilder()
    .add_phase("launch")
    .add_phase("leo")
    .add_phase("translunar")
    .add_phase("nrho")
    .add_phase("rendezvous")
    .add_phase("landing")
    .add_phase("surface")
    .build()
)

CSVExporter.export(
    mission,
    "./data/artemis_mission.csv"
)

ParquetExporter.export(
    mission,
    "./data/artemis_mission.parquet"
)

viewer.render_mission(
    mission
)

viewer.render_prediction()

for phase_name in mission["phase"].unique():

    phase_df = mission[
        mission["phase"] == phase_name
    ]

    predictions, phase_score = (
        PredictiveAnalyzer.analyze(
            phase_df
        )
    )

    viewer.render_predictions_viewer(
        phase_name,
        predictions,
        phase_score
    )

viewer.render_anomaly_detection()

all_anomalies = []

for phase_name in mission["phase"].unique():

    phase_df = mission[
        mission["phase"] == phase_name
    ]

    all_anomalies.extend(

        MissionAnomalyDetector
        .detect(
            phase_df
        )
    )

viewer.render_anomaly_viewer(
    all_anomalies
)