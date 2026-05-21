from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def display_stats(hero):
    # Create a nice table
    table = Table(title=f"{hero.name}'s Stats", show_header=True, header_style="bold magenta")
    
    table.add_column("Stat", style="dim", width=12)
    table.add_column("Total", justify="center")
    table.add_column("Breakdown", justify="center")

    for stat in ["health", "strength", "agility", "intelligence", "defence", "speed"]:
        core = hero.core_stats[stat]
        bonus = hero.bonus_stats[stat]
        total = core + bonus
        
        # We can even color the bonus if it's positive!
        bonus_color = "green" if bonus > 0 else "white"
        table.add_row(
            stat.capitalize(), 
            f"[bold cyan]{total}[/bold cyan]", 
            f"({core} + [{bonus_color}]{bonus}[/{bonus_color}])"
        )

    # Put the table inside a nice border (Panel)
    console.print(Panel(table, expand=False, border_style="blue"))

# If you called display_stats(hero), it would look like a 
# professionally designed UI in your terminal!