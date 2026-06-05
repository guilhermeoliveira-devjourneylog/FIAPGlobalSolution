from rich.columns import Columns
from rich.panel import Panel

from mission.visualization.telemetry_panel import (
    TelemetryPanel
)


class MissionDashboard:

    MAX_PANELS = 6

    @staticmethod
    def build(df):

        numeric_columns = [

            column

            for column in df.columns

            if (
                str(df[column].dtype).startswith(
                    ("int", "float")
                )
                and
                not df[column].dropna().empty
            )
        ]

        if not numeric_columns:

            return Panel(
                "[yellow]No telemetry metrics available[/yellow]",
                title="MISSION DASHBOARD",
                border_style="yellow"
            )

        panels = []

        for column in numeric_columns[
            :MissionDashboard.MAX_PANELS
        ]:

            try:

                panels.append(

                    TelemetryPanel.build(
                        title=column.upper(),
                        metric_name=column,
                        values=df[column].dropna()
                    )
                )

            except Exception as exc:

                panels.append(

                    Panel(
                        f"[red]{exc}[/red]",
                        title=column.upper(),
                        border_style="red"
                    )
                )

        return Columns(
            panels,
            equal=True,
            expand=True
        )