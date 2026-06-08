from rich.console import (
    Console,
    Group
)

from rich.panel import Panel
from rich.rule import Rule
from rich.align import Align
from rich.table import Table
from rich.columns import Columns
from rich.text import Text
from rich import box

from mission.visualization.dashboard import (
    MissionDashboard
)

from mission.visualization.timeline import (
    MissionTimeline
)


class MissionConsole:

    PRIMARY = "white"
    SECONDARY = "bright_black"

    HEADER_COLOR = "white"
    PHASE_COLOR = "cyan"
    SUCCESS_COLOR = "green"
    ERROR_COLOR = "red"

    PAGE_SIZE = 25

    def __init__(self):

        self.console = Console()

    # =====================================================
    # BOOT SCREEN
    # =====================================================

    def render_boot_screen(self):

        self.render_header()
        self.render_strategy()
        self.render_roadmap()
        self.render_operational_sequence()
        self.render_subsystems()
        self.render_footer()
        self.render_ascii_art()

    # =====================================================
    # HEADER
    # =====================================================

    def render_header(self):

        title = Text(
            "ARTEMIS MISSION CONTROL SYSTEM",
            style=f"bold {self.PRIMARY}",
            justify="center"
        )

        subtitle = Text(
            "Exploração Lunar • Orion • SLS • Moon Base",
            style=self.SECONDARY,
            justify="center"
        )

        self.console.print()

        self.console.print(
            Panel(
                Align.center(title),
                border_style=self.PRIMARY,
                box=box.DOUBLE,
                padding=(1, 4)
            )
        )

        self.console.print(subtitle)

        self.console.print(
            Rule(
                characters="─",
                style=self.SECONDARY
            )
        )

    # =====================================================
    # FOOTER
    # =====================================================

    def render_footer(self):

        self.console.print()

        self.console.print(
            Rule(
                characters="─",
                style=self.SECONDARY
            )
        )

        self.console.print()

        self.console.print(
            Panel(
                Align.center(
                    "[bold white]SIMULAR MISSÃO[/]\n\n"
                    "[bright_black]"
                    "Aguardando autorização para início "
                    "das operações espaciais."
                    "[/]"
                ),
                border_style=self.PRIMARY,
                box=box.DOUBLE,
                padding=(1, 4)
            )
        )

        self.console.print()

    # =====================================================
    # MISSION STRATEGY
    # =====================================================

    def render_strategy(self):

        strategy = """
Estabelecer presença humana permanente na Lua
como preparação para futuras missões tripuladas a Marte.

Objetivos Estratégicos:

• Exploração Científica
• Autonomia Operacional
• Utilização de Recursos Locais (ISRU)
• Desenvolvimento Tecnológico
• Expansão da Presença Humana no Espaço
"""

        self.console.print(
            Panel(
                strategy.strip(),
                title="[bold white]MISSÃO ESTRATÉGICA[/]",
                border_style=self.SECONDARY,
                box=box.ROUNDED,
                padding=(1, 2)
            )
        )

        self.console.print()

    # =====================================================
    # ROADMAP
    # =====================================================

    def render_roadmap(self):

        roadmap = """
[bold white]✓ Artemis I[/]
Teste não tripulado da cápsula Orion

[bold white]✓ Artemis II[/]
Missão tripulada circumlunar

► Artemis III
Validação do Human Landing System

► Artemis IV
Retorno à superfície lunar

► Artemis V
Expansão das operações lunares

► Artemis VI+
Construção da Moon Base
"""

        self.console.print(
            Panel(
                roadmap.strip(),
                title="[bold white]ARTEMIS ROADMAP[/]",
                border_style=self.SECONDARY,
                box=box.ROUNDED,
                padding=(1, 2)
            )
        )

    # =====================================================
    # OPERATIONAL SEQUENCE
    # =====================================================

    def render_operational_sequence(self):

        pipeline = Group(

            Panel(
                "[bold white]LANÇAMENTO SLS[/]\n\n"
                "• Motores RS-25\n"
                "• Boosters sólidos\n"
                "• Core Stage\n"
                "• Telemetria crítica\n"
                "• Janela de lançamento",
                border_style=self.SECONDARY,
                box=box.ROUNDED
            ),

            Panel(
                "[bold white]ÓRBITA TERRESTRE[/]\n\n"
                "• Validação dos sistemas\n"
                "• Navegação orbital\n"
                "• Comunicação com a Terra\n"
                "• Preparação para TLI",
                border_style=self.SECONDARY,
                box=box.ROUNDED
            ),

            Panel(
                "[bold white]TRANSFERÊNCIA CISLUNAR[/]\n\n"
                "• Correções de trajetória\n"
                "• Consumo de propelente\n"
                "• Controle de atitude\n"
                "• Monitoramento da Orion",
                border_style=self.SECONDARY,
                box=box.ROUNDED
            ),

            Panel(
                "[bold white]RENDEZVOUS HLS[/]\n\n"
                "• Acoplamento orbital\n"
                "• Transferência de tripulação\n"
                "• Verificação dos sistemas",
                border_style=self.SECONDARY,
                box=box.ROUNDED
            ),

            Panel(
                "[bold white]POUSO LUNAR[/]\n\n"
                "• Navegação terminal\n"
                "• Sensores de terreno\n"
                "• Controle de descida",
                border_style=self.SECONDARY,
                box=box.ROUNDED
            ),

            Panel(
                "[bold white]OPERAÇÕES DE SUPERFÍCIE[/]\n\n"
                "• Energia\n"
                "• Habitats\n"
                "• ISRU\n"
                "• Experimentos",
                border_style=self.SECONDARY,
                box=box.ROUNDED
            ),

            Panel(
                "[bold white]RETORNO À TERRA[/]\n\n"
                "• Decolagem lunar\n"
                "• Acoplamento Orion\n"
                "• Reentrada",
                border_style=self.SECONDARY,
                box=box.ROUNDED
            )
        )

        self.console.print(
            Panel(
                pipeline,
                title="[bold white]SEQUÊNCIA OPERACIONAL[/]",
                border_style=self.PRIMARY,
                box=box.DOUBLE_EDGE
            )
        )

    # =====================================================
    # SUBSYSTEMS
    # =====================================================

    def render_subsystems(self):

        subsystems = [

            Panel(
                "[bold white]⚡ ENERGIA[/]\n\n"
                "Painéis Solares\n"
                "Baterias\n"
                "Reatores",
                border_style=self.SECONDARY
            ),

            Panel(
                "[bold white]🧭 NAVEGAÇÃO[/]\n\n"
                "GN&C\n"
                "Órbita\n"
                "Delta-V",
                border_style=self.SECONDARY
            ),

            Panel(
                "[bold white]📡 COMUNICAÇÕES[/]\n\n"
                "DSN\n"
                "Gateway\n"
                "Telemetria",
                border_style=self.SECONDARY
            ),

            Panel(
                "[bold white]🧪 LIFE SUPPORT[/]\n\n"
                "Oxigênio\n"
                "Água\n"
                "Temperatura",
                border_style=self.SECONDARY
            ),

            Panel(
                "[bold white]🌕 SURFACE OPS[/]\n\n"
                "Rovers\n"
                "ISRU\n"
                "Habitats",
                border_style=self.SECONDARY
            ),

            Panel(
                "[bold white]🛡 SAFETY[/]\n\n"
                "Radiação\n"
                "Alertas\n"
                "Emergências",
                border_style=self.SECONDARY
            )
        ]

        self.console.print(
            Panel(
                Columns(
                    subsystems,
                    equal=True,
                    expand=True
                ),
                title="[bold white]SUBSISTEMAS MONITORADOS[/]",
                border_style=self.PRIMARY,
                box=box.DOUBLE_EDGE
            )
        )

    # =====================================================
    # ASCII ART
    # =====================================================

    def render_ascii_art(self):

        self.console.print(
            Panel(
                Align.center(
                    """
█████╗ ██████╗ ████████╗███████╗███╗   ███╗██╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗ ████║██║██╔════╝
███████║██████╔╝   ██║   █████╗  ██╔████╔██║██║███████╗
██╔══██║██╔══██╗   ██║   ██╔══╝  ██║╚██╔╝██║██║╚════██║
██║  ██║██║  ██║   ██║   ███████╗██║ ╚═╝ ██║██║███████║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝╚══════╝

            EARTH → LEO → NRHO → LUNAR BASE
"""
                ),
                border_style=self.PRIMARY,
                box=box.DOUBLE,
                padding=(1, 4)
            )
        )

    # =====================================================
    # DATASET GENERATION
    # =====================================================

    def render_dataset_generation(self):

        self.console.print(
            Panel(
                Align.center(
                    "[bright_black]Gerando DataSet[/]"
                ),
                border_style=self.PRIMARY,
                box=box.DOUBLE
            )
        )

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
            "LAUNCH",
            "Lançamento, subida e saída da Terra."
        )

        table.add_row(
            "LEO",
            "Órbita Baixa da Terra (Low Earth Orbit) para verificação dos sistemas."
        )

        table.add_row(
            "TRANSLUNAR",
            "Trajetória de transferência da Terra para a Lua."
        )

        table.add_row(
            "NRHO",
            "Órbita Halo Retilínea Próxima (Near Rectilinear Halo Orbit) ao redor da Lua."
        )

        table.add_row(
            "RENDEZVOUS",
            "Acoplamento e transferência de tripulação entre veículos."
        )

        table.add_row(
            "LANDING",
            "Descida controlada e pouso na superfície lunar."
        )

        table.add_row(
            "SURFACE",
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

    # =====================================================
    # ANOMALY DETECTION
    # =====================================================

    def render_anomaly_detection(self):

        self.console.print(

            Panel(

                Align.center(
                    "[bright_black]Detectando Anomalias[/]"
                ),

                border_style=self.PRIMARY,

                box=box.DOUBLE

            )
        )

    # =====================================================
    # ANOMALY VIEWER
    # =====================================================

    def render_anomaly_viewer(
        self,
        anomalies
    ):

        total_anomalies = len(
            anomalies
        )

        if total_anomalies == 0:

            self.console.print(

                Panel(

                    Align.center(
                        "[green]Nenhuma anomalia detectada[/]"
                    ),

                    title="MISSION STATUS",

                    border_style="green",

                    box=box.DOUBLE

                )
            )

            return

        total_pages = (

            total_anomalies
            + self.PAGE_SIZE
            - 1

        ) // self.PAGE_SIZE

        page = 0

        while True:

            self.console.clear()

            self.console.print(

                Panel(

                    Align.center(

                        "[bold white]"
                        "MISSION ANOMALY VIEWER"
                        "[/]"

                    ),

                    border_style=self.PRIMARY,

                    box=box.DOUBLE

                )
            )

            start = (
                page
                * self.PAGE_SIZE
            )

            end = min(

                start
                + self.PAGE_SIZE,

                total_anomalies
            )

            table = Table(

                title=(

                    f"ANOMALIES "
                    f"({start + 1}-{end} "
                    f"de {total_anomalies})"

                ),

                box=box.ROUNDED,

                show_lines=True
            )

            table.add_column(
                "PHASE",
                style="cyan",
                width=12
            )

            table.add_column(
                "INDEX",
                justify="right",
                width=8
            )

            table.add_column(
                "SEVERITY",
                width=12
            )

            table.add_column(
                "ANOMALY",
                style="red",
                width=35
            )

            table.add_column(
                "DESCRIPTION",
                style="white",
                overflow="fold"
            )

            # =====================================================
            # ANOMALY CATALOG
            # =====================================================

            ANOMALY_DESCRIPTIONS = {

                "ALTITUDE_DROP":
                    "Queda inesperada de altitude durante a ascensão.",

                "VELOCITY_DROP":
                    "Redução anormal da velocidade durante o lançamento.",

                "ALTITUDE_STALL":
                    "Altitude deixou de aumentar durante a subida.",

                "VELOCITY_STALL":
                    "Velocidade deixou de aumentar durante a subida.",

                "ORBITAL_DRIFT":
                    "Desvio significativo em relação à trajetória ou órbita nominal.",

                "FUEL_INCREASE":
                    "Aumento inesperado do nível de combustível detectado.",

                "EXCESSIVE_FUEL_CONSUMPTION":
                    "Consumo de combustível acima do perfil previsto.",

                "POWER_OUTLIER":
                    "Potência elétrica fora da faixa operacional esperada.",

                "DISTANCE_INCREASE":
                    "A espaçonave está se afastando do alvo durante o rendezvous.",

                "DOCKING_FAILURE":
                    "O procedimento de acoplamento não foi concluído.",

                "ALTITUDE_RISE":
                    "Aumento inesperado de altitude durante a descida.",

                "SURFACE_NOT_REACHED":
                    "A espaçonave não atingiu a superfície lunar.",

                "LANDING_FAILURE":
                    "Falha detectada durante a sequência de pouso.",

                "POWER_LOSS":
                    "Perda significativa de geração de energia na superfície lunar."
            }

            for anomaly in anomalies[
                start:end
            ]:

                severity = anomaly[
                    "severity"
                ]

                severity_view = (

                    "[bold red]CRITICAL[/]"

                    if severity == "CRITICAL"

                    else

                    "[yellow]WARNING[/]"
                )

                description = (

                    ANOMALY_DESCRIPTIONS.get(

                        anomaly["anomaly"],

                        "Descrição não disponível."

                    )

                )

                table.add_row(

                    anomaly["phase"],

                    str(
                        anomaly["index"]
                    ),

                    severity_view,

                    anomaly["anomaly"],

                    description
                )

            self.console.print(
                table
            )

            self.console.print()

            self.console.print(

                f"[bright_black]"
                f"Página "
                f"{page + 1}"
                f"/"
                f"{total_pages}"
                f"[/]"
            )

            self.console.print()

            self.console.print(

                "[white]"
                "[N] Próxima página    "
                "[P] Página anterior    "
                "[F] Primeira página    "
                "[L] Última página    "
                "[Q] Sair"
                "[/]"
            )

            option = (

                input(
                    "\nOpção: "
                )

                .strip()

                .lower()
            )

            if option == "n":

                if page < total_pages - 1:

                    page += 1

            elif option == "p":

                if page > 0:

                    page -= 1

            elif option == "f":

                page = 0

            elif option == "l":

                page = (
                    total_pages - 1
                )

            elif option == "q":

                break

    # =====================================================
    # RENDER PREDICTION
    # =====================================================

    def render_prediction(self):

        self.console.print(
            Panel(
                Align.center(
                    "[bright_black]Executando Predições[/]"
                ),
                border_style=self.PRIMARY,
                box=box.DOUBLE
            )
        )

    # =====================================================
    # PREDICTION VIEWER
    # =====================================================
    
    def render_predictions_viewer(
        self,
        phase_name,
        predictions,
        phase_score
    ):
        table = Table(
            title=f"{phase_name} Predictions"
        )

        table.add_column("Metric")
        table.add_column("Current")
        table.add_column("Forecast")
        table.add_column("Risk")
        table.add_column("Health")

        for p in predictions:

            color = {
                "LOW": "green",
                "MEDIUM": "yellow",
                "HIGH": "red"
            }[p.risk]

            table.add_row(
                p.metric,
                str(p.current_value),
                str(p.predicted_value),
                f"[{color}]{p.risk}[/{color}]",
                f"{p.health_score}%"
            )

        self.console.print(table)

        self.console.print(
            Panel(
                f"Phase Health Score: "
                f"[cyan]{phase_score}%[/cyan]"
            )
        )