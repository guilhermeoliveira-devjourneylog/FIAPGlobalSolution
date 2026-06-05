from rich.table import Table


class MissionTimeline:

    @staticmethod
    def build(phases):

        table = Table(
            title="MISSION TIMELINE",
            show_header=True
        )

        table.add_column("Phase")
        table.add_column("Status")

        for phase in phases:

            table.add_row(
                phase.upper(),
                "[green]● COMPLETE[/green]"
            )

        return table