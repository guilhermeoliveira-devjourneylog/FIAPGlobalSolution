from rich.panel import Panel

from mission.visualization.charts import (
    TelemetryChart
)


class TelemetryPanel:

    @staticmethod
    def build(
        title: str,
        metric_name: str,
        values
    ):

        values = list(values)

        # coluna vazia
        if len(values) == 0:

            return Panel(
                "[yellow]No telemetry data available[/yellow]",
                title=title,
                border_style="yellow"
            )

        # reduz amostragem para manter o console leve
        step = max(
            1,
            len(values) // 50
        )

        sample = values[::step]

        return TelemetryChart.panel(
            title=title,
            values=sample
        )