class Player:
    def __init__(self, player_data):
        """
        Initializes a Player object with data from a dictionary.

        :param player_data: Dictionary containing player information
        """
        self.name = player_data.get('name', 'Unknown')
        self.team = player_data.get('team', 'Unknown')
        self.goals = player_data.get('goals', 0)
        self.assists = player_data.get('assists', 0)
        self.total_points = self.goals + self.assists
        self.nationality = player_data.get('nationality', 'Unknown')

    def __str__(self):
        """
        Returns a formatted string representation of the player's information.

        :return: String with player details
        """
        return f"{self.name:20} {self.team:3}  {self.goals} + {self.assists} = {self.total_points}"
