import requests
from player import Player
from rich.console import Console
from rich.table import Table


class PlayerReader:
    def __init__(self, url):
        """
        Initializes a PlayerReader object to fetch players from a given URL.

        :param url: URL to fetch player data from
        """
        self.url = url

    def get_players(self):
        """
        Fetches player data from the URL and creates Player objects.

        :return: List of Player objects
        """
        response = requests.get(self.url).json()
        return [Player(player_dict) for player_dict in response]


class PlayerStats:
    def __init__(self, reader):
        """
        Initializes a PlayerStats object to create statistics for players.

        :param reader: PlayerReader object
        """
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        """
        Filters players by nationality and sorts them by points in descending order.

        :param nationality: The nationality code to filter players by
        :return: List of Player objects
        """
        filtered_players = [
            player for player in self.players if player.nationality == nationality.upper()]
        return sorted(filtered_players, key=lambda p: p.total_points, reverse=True)


def display_players_with_rich(players, country_code):
    """
    Displays player data in a formatted table using Rich.

    :param players: List of Player objects
    :param country_code: Country code to display
    """
    console = Console()
    table = Table(title=f"Players from {country_code.upper()}")

    table.add_column("Name", justify="left")
    table.add_column("Team", justify="center")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Total Points", justify="right")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals),
                      str(player.assists), str(player.total_points))

    console.print(table)


def main():
    season = input("Enter the season (e.g., '2023-24'): ").strip()
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    # Näytä tietyn maan pelaajat
    country_code = input(
        "Enter the country code (e.g., 'FIN') to display players: ").strip()
    players = stats.top_scorers_by_nationality(country_code)

    if not players:
        print(f"No players found from {
            country_code.upper()} in season {season}.")
    else:
        display_players_with_rich(players, country_code)
        # print(f"\nPlayers from {country_code.upper()}\n")
        # for player in players:
        #    print(player)


if __name__ == "__main__":
    main()
