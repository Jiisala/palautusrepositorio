class PlayerStats:

    def __init__(self, reader) -> None:
        self.players = reader.fetch_player_data()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = list(filter(lambda x: x.nationality == nationality, self.players))
        filtered_players.sort(key=lambda x: x.goals + x.assists, reverse=True)
        return filtered_players