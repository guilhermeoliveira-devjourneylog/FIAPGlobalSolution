from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.align import Align


class SparkLine:

    CHARS = "▁▂▃▄▅▆▇█"

    @classmethod
    def render(cls, values):

        values = list(values)

        if len(values) == 0:
            return ""

        minimum = min(values)
        maximum = max(values)

        span = maximum - minimum

        if span == 0:
            return cls.CHARS[0] * len(values)

        result = []

        for value in values:

            index = int(
                ((value - minimum) / span)
                * (len(cls.CHARS) - 1)
            )

            index = max(
                0,
                min(index, len(cls.CHARS) - 1)
            )

            result.append(
                cls.CHARS[index]
            )

        return "".join(result)

    @classmethod
    def rich(
        cls,
        values,
        style="cyan"
    ):

        return Text(
            cls.render(values),
            style=style
        )


class HorizontalBar:

    @staticmethod
    def render(
        value,
        maximum,
        width=30
    ):

        if maximum <= 0:
            return "░" * width

        ratio = value / maximum

        ratio = max(
            0.0,
            min(ratio, 1.0)
        )

        filled = int(
            width * ratio
        )

        return (
            "█" * filled
            +
            "░" * (width - filled)
        )


class VerticalBar:

    @staticmethod
    def render(
        values,
        height=8
    ):

        values = list(values)

        if len(values) == 0:
            return ""

        max_value = max(values)

        if max_value <= 0:
            return ""

        rows = []

        for level in range(
            height,
            0,
            -1
        ):

            threshold = (
                max_value
                * level
                / height
            )

            row = ""

            for value in values:

                if value >= threshold:
                    row += "█ "
                else:
                    row += "  "

            rows.append(row)

        return "\n".join(rows)


class Gauge:

    @staticmethod
    def render(
        value,
        maximum=100,
        width=30
    ):

        if maximum <= 0:
            maximum = 1

        ratio = value / maximum

        ratio = max(
            0.0,
            min(ratio, 1.0)
        )

        filled = int(
            ratio * width
        )

        bar = (
            "█" * filled
            +
            "░" * (width - filled)
        )

        return (
            f"[{bar}] "
            f"{ratio * 100:.1f}%"
        )


class FuelGauge:

    @staticmethod
    def panel(
        fuel_percent
    ):

        return Panel(
            Align.center(
                Gauge.render(
                    fuel_percent,
                    100,
                    25
                )
            ),
            title="FUEL",
            border_style="yellow"
        )


class BatteryGauge:

    @staticmethod
    def panel(
        battery_percent
    ):

        return Panel(
            Align.center(
                Gauge.render(
                    battery_percent,
                    100,
                    25
                )
            ),
            title="BATTERY",
            border_style="green"
        )


class Histogram:

    @staticmethod
    def build(values):

        values = list(values)

        if len(values) == 0:

            return Panel(
                "No Data",
                title="Histogram"
            )

        maximum = max(values)

        table = Table.grid()

        for i, value in enumerate(values):

            table.add_row(
                f"{i:02}",
                HorizontalBar.render(
                    value,
                    maximum,
                    20
                )
            )

        return table


class TelemetryChart:

    @staticmethod
    def panel(
        title,
        values,
        color="cyan"
    ):

        values = list(values)

        if len(values) == 0:

            return Panel(
                Align.center(
                    "[yellow]No telemetry data[/yellow]"
                ),
                title=title,
                border_style="yellow"
            )

        spark = SparkLine.render(
            values
        )

        current = values[-1]

        maximum = max(values)

        minimum = min(values)

        avg = (
            sum(values)
            / len(values)
        )

        stats = Table.grid(
            expand=True
        )

        stats.add_row(
            "Current",
            f"{current:.2f}"
        )

        stats.add_row(
            "Average",
            f"{avg:.2f}"
        )

        stats.add_row(
            "Maximum",
            f"{maximum:.2f}"
        )

        stats.add_row(
            "Minimum",
            f"{minimum:.2f}"
        )

        content = Table.grid()

        content.add_row(
            Text(
                spark,
                style=color
            )
        )

        content.add_row("")
        content.add_row(stats)

        return Panel(
            content,
            title=title,
            border_style=color
        )