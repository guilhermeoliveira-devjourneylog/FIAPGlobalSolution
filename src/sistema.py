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

from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.rule import Rule
from rich.text import Text
from rich.columns import Columns
from rich import box

# =========================================================
# PALETA MONOCROMÁTICA
# =========================================================

PRIMARY = "white"
SECONDARY = "bright_black"

# =========================================================
# CONSOLE
# =========================================================

console = Console()

# =========================================================
# CABEÇALHO
# =========================================================

titulo = Text(
    "ARTEMIS MISSION CONTROL SYSTEM",
    style=f"bold {PRIMARY}",
    justify="center"
)

subtitulo = Text(
    "Exploração Lunar • Orion • SLS • Moon Base",
    style=SECONDARY,
    justify="center"
)

console.print()

console.print(
    Panel(
        Align.center(titulo),
        border_style=PRIMARY,
        box=box.DOUBLE,
        padding=(1, 4)
    )
)

console.print(subtitulo)

console.print(
    Rule(
        characters="─",
        style=SECONDARY
    )
)

# =========================================================
# MISSÃO ESTRATÉGICA
# =========================================================

estrategia = """
Estabelecer presença humana permanente na Lua
como preparação para futuras missões tripuladas a Marte.

Objetivos Estratégicos:

• Exploração Científica
• Autonomia Operacional
• Utilização de Recursos Locais (ISRU)
• Desenvolvimento Tecnológico
• Expansão da Presença Humana no Espaço
"""

console.print(
    Panel(
        estrategia.strip(),
        title="[bold white]MISSÃO ESTRATÉGICA[/]",
        border_style=SECONDARY,
        box=box.ROUNDED,
        padding=(1, 2)
    )
)

console.print()

# =========================================================
# ARTEMIS ROADMAP
# =========================================================

roadmap = """
[bold white]✓ Artemis I[/]
Teste não tripulado da cápsula Orion

[bold white]✓ Artemis II[/]
Missão tripulada circumlunar

[white]► Artemis III[/]
Validação do Human Landing System

[white]► Artemis IV[/]
Retorno à superfície lunar

[white]► Artemis V[/]
Expansão das operações lunares

[bold white]► Artemis VI+[/]
Construção da Moon Base
"""

console.print(
    Panel(
        roadmap.strip(),
        title="[bold white]ARTEMIS ROADMAP[/]",
        border_style=SECONDARY,
        box=box.ROUNDED,
        padding=(1, 2)
    )
)

console.print()

# =========================================================
# SEQUÊNCIA OPERACIONAL
# =========================================================

pipeline = Group(

    Panel(
        (
            "[bold white]🚀 LANÇAMENTO SLS[/]\n\n"
            "• Motores RS-25\n"
            "• Boosters sólidos\n"
            "• Core Stage\n"
            "• Telemetria crítica\n"
            "• Janela de lançamento\n\n"
            "Objetivo:\n"
            "Inserção segura da cápsula Orion."
        ),
        border_style=SECONDARY,
        box=box.ROUNDED
    ),

    Panel(
        (
            "[bold white]🌍 ÓRBITA TERRESTRE[/]\n\n"
            "• Validação dos sistemas\n"
            "• Navegação orbital\n"
            "• Comunicação com a Terra\n"
            "• Preparação para TLI\n\n"
            "Objetivo:\n"
            "Preparar a transferência translunar."
        ),
        border_style=SECONDARY,
        box=box.ROUNDED
    ),

    Panel(
        (
            "[bold white]🌙 TRANSFERÊNCIA CISLUNAR[/]\n\n"
            "• Correções de trajetória\n"
            "• Consumo de propelente\n"
            "• Controle de atitude\n"
            "• Monitoramento da Orion\n\n"
            "Objetivo:\n"
            "Alcançar órbita lunar."
        ),
        border_style=SECONDARY,
        box=box.ROUNDED
    ),

    Panel(
        (
            "[bold white]🛰 RENDEZVOUS HLS[/]\n\n"
            "• Acoplamento orbital\n"
            "• Transferência de tripulação\n"
            "• Verificação dos sistemas\n"
            "• Preparação para descida\n\n"
            "Objetivo:\n"
            "Garantir segurança operacional."
        ),
        border_style=SECONDARY,
        box=box.ROUNDED
    ),

    Panel(
        (
            "[bold white]🛬 POUSO LUNAR[/]\n\n"
            "• Navegação terminal\n"
            "• Sensores de terreno\n"
            "• Controle de descida\n"
            "• Touchdown seguro\n\n"
            "Objetivo:\n"
            "Alcançar a superfície lunar."
        ),
        border_style=SECONDARY,
        box=box.ROUNDED
    ),

    Panel(
        (
            "[bold white]🏗 OPERAÇÕES DE SUPERFÍCIE[/]\n\n"
            "• Produção de energia\n"
            "• Habitats\n"
            "• Mobilidade lunar\n"
            "• Experimentos científicos\n"
            "• ISRU\n\n"
            "Objetivo:\n"
            "Garantir permanência sustentável."
        ),
        border_style=SECONDARY,
        box=box.ROUNDED
    ),

    Panel(
        (
            "[bold white]🌎 RETORNO À TERRA[/]\n\n"
            "• Decolagem lunar\n"
            "• Acoplamento Orion\n"
            "• Reentrada atmosférica\n"
            "• Recuperação da cápsula\n\n"
            "Objetivo:\n"
            "Retorno seguro da tripulação."
        ),
        border_style=SECONDARY,
        box=box.ROUNDED
    )
)

console.print(
    Panel(
        pipeline,
        title="[bold white]SEQUÊNCIA OPERACIONAL[/]",
        border_style=PRIMARY,
        box=box.DOUBLE_EDGE,
        padding=(1, 2)
    )
)

console.print()

# =========================================================
# SUBSISTEMAS
# =========================================================

energia = Panel(
    (
        "[bold white]⚡ ENERGIA[/]\n\n"
        "Painéis Solares\n"
        "Baterias\n"
        "Reatores Nucleares\n"
        "Distribuição Elétrica"
    ),
    border_style=SECONDARY,
    box=box.ROUNDED
)

navegacao = Panel(
    (
        "[bold white]🧭 NAVEGAÇÃO[/]\n\n"
        "GN&C\n"
        "Posicionamento Orbital\n"
        "Controle de Atitude\n"
        "Delta-V"
    ),
    border_style=SECONDARY,
    box=box.ROUNDED
)

comunicacao = Panel(
    (
        "[bold white]📡 COMUNICAÇÕES[/]\n\n"
        "Deep Space Network\n"
        "Telemetria\n"
        "Links Terra-Lua\n"
        "Gateway"
    ),
    border_style=SECONDARY,
    box=box.ROUNDED
)

vida = Panel(
    (
        "[bold white]🧪 LIFE SUPPORT[/]\n\n"
        "Oxigênio\n"
        "Água\n"
        "Temperatura\n"
        "Pressurização"
    ),
    border_style=SECONDARY,
    box=box.ROUNDED
)

superficie = Panel(
    (
        "[bold white]🌕 SURFACE OPS[/]\n\n"
        "Rovers\n"
        "Habitats\n"
        "ISRU\n"
        "Logística"
    ),
    border_style=SECONDARY,
    box=box.ROUNDED
)

seguranca = Panel(
    (
        "[bold white]🛡 SAFETY[/]\n\n"
        "Radiação\n"
        "Micrometeoritos\n"
        "Alertas\n"
        "Emergências"
    ),
    border_style=SECONDARY,
    box=box.ROUNDED
)

console.print(
    Panel(
        Columns(
            [
                energia,
                navegacao,
                comunicacao,
                vida,
                superficie,
                seguranca
            ],
            equal=True,
            expand=True
        ),
        title="[bold white]SUBSISTEMAS MONITORADOS[/]",
        border_style=PRIMARY,
        box=box.DOUBLE_EDGE
    )
)

console.print()

# =========================================================
# RODAPÉ
# =========================================================

console.print(
    Rule(
        characters="─",
        style=SECONDARY
    )
)

console.print()

console.print(
    Panel(
        Align.center(
            "[bold white]SIMULAR MISSÃO[/]\n\n"
            "[bright_black]Aguardando autorização para início das operações espaciais.[/]"
        ),
        border_style=PRIMARY,
        box=box.DOUBLE,
        padding=(1, 4)
    )
)

console.print()

console.print(
    Panel(
        Align.center(
            r"""
[bright_black]

 █████╗ ██████╗ ████████╗███████╗███╗   ███╗██╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗ ████║██║██╔════╝
███████║██████╔╝   ██║   █████╗  ██╔████╔██║██║███████╗
██╔══██║██╔══██╗   ██║   ██╔══╝  ██║╚██╔╝██║██║╚════██║
██║  ██║██║  ██║   ██║   ███████╗██║ ╚═╝ ██║██║███████║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝╚══════╝

            ╔══════════════════════════╗
            ║  MISSION CONTROL  SYSTEM ║
            ╚══════════════════════════╝

    🚀 EARTH > 🛰️ LEO > 🌙 NRHO > 🏕️ LUNAR BASE   
[/]
"""
        ),
        border_style=PRIMARY,
        box=box.DOUBLE,
        padding=(1, 4),
    )
)

console.print(
    Panel(
        Align.center(
            "[bright_black]Gerando DataSet[/]"
        ),
        border_style=PRIMARY,
        box=box.DOUBLE,
        padding=(1, 4)
    )
)

console.print()

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

print(mission.head())
print(mission.tail())

viewer = MissionConsole()

viewer.render_mission(
    mission
)

console.print(
    Panel(
        Align.center(
            "[bright_black]Detectando Anomalias[/]"
        ),
        border_style=PRIMARY,
        box=box.DOUBLE,
        padding=(1, 4)
    )
)

console.print()

all_anomalies = []

for phase_name in mission["phase"].unique():

    phase_df = mission[
        mission["phase"] == phase_name
    ]

    anomalies = (
        MissionAnomalyDetector
        .detect(phase_df)
    )

    all_anomalies.extend(
        anomalies
    )

# =========================================================
# ANOMALY VIEWER
# =========================================================

PAGE_SIZE = 25

total_anomalies = len(
    all_anomalies
)

if total_anomalies == 0:

    console.print(
        Panel(
            Align.center(
                "[green]Nenhuma anomalia detectada[/]"
            ),
            title="MISSION STATUS",
            border_style="green",
            box=box.DOUBLE
        )
    )

else:

    total_pages = (

        total_anomalies
        + PAGE_SIZE
        - 1

    ) // PAGE_SIZE

    page = 0

    while True:

        console.clear()

        console.print(
            Panel(
                Align.center(
                    "[bold white]MISSION ANOMALY VIEWER[/]"
                ),
                border_style=PRIMARY,
                box=box.DOUBLE
            )
        )

        start = page * PAGE_SIZE

        end = min(
            start + PAGE_SIZE,
            total_anomalies
        )

        table = Table(

            title=(
                f"ANOMALIES "
                f"({start+1}-{end} "
                f"de {total_anomalies})"
            ),

            box=box.ROUNDED,

            show_lines=True
        )

        table.add_column(
            "PHASE",
            style="cyan"
        )

        table.add_column(
            "INDEX",
            justify="right"
        )

        table.add_column(
            "SEVERITY"
        )

        table.add_column(
            "ANOMALY",
            style="red"
        )

        for anomaly in all_anomalies[
            start:end
        ]:

            severity = (
                anomaly["severity"]
            )

            if severity == "CRITICAL":

                severity_view = (
                    "[bold red]CRITICAL[/]"
                )

            else:

                severity_view = (
                    "[yellow]WARNING[/]"
                )

            table.add_row(

                anomaly["phase"],

                str(
                    anomaly["index"]
                ),

                severity_view,

                anomaly["anomaly"]
            )

        console.print(table)

        console.print()

        console.print(
            f"[bright_black]"
            f"Página {page+1}/{total_pages}"
            f"[/]"
        )

        console.print()

        console.print(
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