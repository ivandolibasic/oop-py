from player import Player
from game_state_display import GameState

def run():
    player = Player("Pero", 5)
    game = GameState("🟢", "🔴")
    game.display(player.name, max(player.health_points, 6), player.health_points, "gt", "table")

run()