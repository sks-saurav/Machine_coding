from entity import BowlingAlley, Player


players = []
for id, name in [(1, 'Saurav'), (2, 'Khushi'), (3, 'Aish')]:
    player = Player(id, name)
    players.append(player)

bowling_alley = BowlingAlley(players)
bowling_alley.simulate_game()

for player in bowling_alley.players:
    print(f"{player.name}'s Scoreboard:\n{player.scoreboard}")

bowling_alley.print_winner()