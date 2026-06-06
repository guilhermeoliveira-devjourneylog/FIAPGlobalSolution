from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.align import Align
from rich.table import Table

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

    # =====================================================
    # LEGENDA DAS FASES
    # =====================================================

    def render_phase_legend(self):

        table = Table.grid(
            padding=(0, 2)
        )

        table.add_column(
            style="bold cyan",
            width=14
        )

        table.add_column()

        table.add_row(
            "🚀 LAUNCH",
            "Lançamento, subida e saída da Terra."
        )

        table.add_row(
            "🌍 LEO",
            "Órbita Baixa da Terra (Low Earth Orbit) para verificação dos sistemas."
        )

        table.add_row(
            "🌙 TRANSLUNAR",
            "Trajetória de transferência da Terra para a Lua."
        )

        table.add_row(
            "🛰 NRHO",
            "Órbita Halo Retilínea Próxima (Near Rectilinear Halo Orbit) ao redor da Lua."
        )

        table.add_row(
            "🤝 RENDEZVOUS",
            "Acoplamento e transferência de tripulação entre veículos."
        )

        table.add_row(
            "📍 LANDING",
            "Descida controlada e pouso na superfície lunar."
        )

        table.add_row(
            "🔬 SURFACE",
            "Operações científicas e exploração da superfície da Lua."
        )

        self.console.print(

            Panel(
                table,
                title="REFERÊNCIA DAS FASES DA MISSÃO",
                border_style=self.PHASE_COLOR
            )
        )

    # =====================================================
    # FASE INDIVIDUAL
    # =====================================================

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

    # =====================================================
    # RESUMO
    # =====================================================

    def render_summary(
        self,
        phase_name,
        dataframe
    ):

        panel = Panel(

            Align.center(

                f"Linhas   : {len(dataframe)}\n"
                f"Colunas  : {len(dataframe.columns)}"

            ),

            title=(
                f"RESUMO - "
                f"{phase_name.upper()}"
            ),

            border_style=self.SUCCESS_COLOR
        )

        self.console.print(panel)

    # =====================================================
    # TIMELINE
    # =====================================================

    def render_timeline(
        self,
        phases
    ):

        self.console.print(

            MissionTimeline.build(
                phases
            )
        )

    # =====================================================
    # MISSÃO COMPLETA
    # =====================================================

    def render_mission(
        self,
        mission_df
    ):

        if mission_df is None:

            self.console.print(

                Panel(
                    "Dataset da missão é nulo.",
                    border_style=self.ERROR_COLOR
                )
            )

            return

        if mission_df.empty:

            self.console.print(

                Panel(
                    "Dataset da missão está vazio.",
                    border_style=self.ERROR_COLOR
                )
            )

            return

        if "phase" not in mission_df.columns:

            self.console.print(

                Panel(
                    "Coluna 'phase' não encontrada.",
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
                    "ARTEMIS MISSION TELEMETRY OVERVIEW"
                    "[/]"

                ),

                border_style=self.HEADER_COLOR
            )
        )

        # ==========================================
        # LEGENDA DAS FASES
        # ==========================================

        self.render_phase_legend()

        self.console.print()

        # ==========================================
        # TIMELINE
        # ==========================================

        self.render_timeline(
            phases
        )

        # ==========================================
        # DASHBOARDS
        # ==========================================

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
                    "VISUALIZAÇÃO DA MISSÃO CONCLUÍDA"
                    f"[/{self.SUCCESS_COLOR}]"

                ),

                border_style=self.SUCCESS_COLOR
            )
        )