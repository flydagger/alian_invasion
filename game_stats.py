class GameStats:
    """track game statistics"""
    def __init__(self, ai_settings):
        """initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        # don't reset highest score at any case
        self.high_score = 0

    def reset_stats(self):
        """initialize the statistics that may change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

