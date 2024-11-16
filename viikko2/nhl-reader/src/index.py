import requests
from player import Player


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


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    # Näytä tietyn maan pelaajat
    country_code = input(
        "Enter the country code (e.g., 'FIN') to display players: ").strip()
    players = stats.top_scorers_by_nationality(country_code)

    if not players:
        print(f"No players found from {country_code.upper()}.")
    else:
        print(f"\nPlayers from {country_code.upper()}\n")
        for player in players:
            print(player)


if __name__ == "__main__":
    main()
