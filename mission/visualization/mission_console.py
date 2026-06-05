from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.align import Align

from mission.visualization.dashboard import (
    MissionDashboard
)

from mission.visualization.timeline import (
    MissionTimeline
)


class MissionConsole:

    HEADER_COLOR = "white"
    PHASE_COLOR = "cyan"
    SUCCESS_COLOR = "green"
    ERROR_COLOR = "red"

    def __init__(self):

        self.console = Console()

    def render_phase(
        self,
        phase_name,
        dataframe
    ):

        self.console.print()

        self.console.print(
            Rule(
                f"[bold {self.PHASE_COLOR}]"
                f"{phase_name.upper()}"
            )
        )

        try:

            self.console.print(
                MissionDashboard.build(
                    dataframe
                )
            )

            self.render_summary(
                phase_name,
                dataframe
            )

        except Exception as exc:

            self.console.print(

                Panel(
                    str(exc),
                    title=f"{phase_name.upper()} ERROR",
                    border_style=self.ERROR_COLOR
                )
            )

    def render_summary(
        self,
        phase_name,
        dataframe
    ):

        panel = Panel(

            Align.center(

                f"Rows      : {len(dataframe)}\n"
                f"Columns   : {len(dataframe.columns)}"

            ),

            title=(
                f"{phase_name.upper()} "
                f"SUMMARY"
            ),

            border_style=self.SUCCESS_COLOR
        )

        self.console.print(panel)

    def render_timeline(
        self,
        phases
    ):

        self.console.print(
            MissionTimeline.build(
                phases
            )
        )

    def render_mission(
        self,
        mission_df
    ):

        if mission_df is None:

            self.console.print(

                Panel(
                    "Mission dataset is None.",
                    border_style=self.ERROR_COLOR
                )
            )

            return

        if mission_df.empty:

            self.console.print(

                Panel(
                    "Mission dataset is empty.",
                    border_style=self.ERROR_COLOR
                )
            )

            return

        if "phase" not in mission_df.columns:

            self.console.print(

                Panel(
                    "Column 'phase' not found.",
                    border_style=self.ERROR_COLOR
                )
            )

            return

        phases = [

            phase

            for phase in mission_df[
                "phase"
            ].dropna().unique()

        ]

        self.console.print()

        self.console.print(

            Panel(

                Align.center(
                    "[bold white]"
                    "MISSION TELEMETRY OVERVIEW"
                    "[/]"
                ),

                border_style=self.HEADER_COLOR
            )
        )

        self.console.print()

        self.render_timeline(
            phases
        )

        for phase in phases:

            phase_df = mission_df[
                mission_df["phase"] == phase
            ]

            self.render_phase(
                phase,
                phase_df
            )

        self.console.print()

        self.console.print(

            Panel(

                Align.center(

                    f"[{self.SUCCESS_COLOR}]"
                    "MISSION VISUALIZATION COMPLETE"
                    f"[/{self.SUCCESS_COLOR}]"

                ),

                border_style=self.SUCCESS_COLOR
            )
        )