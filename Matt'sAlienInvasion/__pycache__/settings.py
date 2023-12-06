
class Settings:
        """ A class to store all settings for Alien Invasion"""
        def __init__(self):
                """ Initialize the game's settings"""
# Screen settings
                self.screen_width = 1200
                self.screen_height = 800
                self.bg_color = (50, 20, 70)
# Ship settings
                self.ship_speed = 1.5
                self.ship_limit = 3
# Bullet settings - dark grey bullets that a re 3 pixels wide and 15 pixels high. Bullets travel slower than the ship.

                self.bullet_speed = 3.0
                self.bullet_width = 30000
                self.bullet_height = 15
                self.bullet_color = (60, 60, 60)
                self.bullets_allowed = 5
# alien settings
                self.alien_speed = 1.0
                self.fleet_drop_speed = 10
# fleet direction of 1 represents right; -1 represents left.
                self.fleet_direction = 1

                self.score_scale = 1.5

                self.initialize_dynamic_settings()
                self.speedup_scale = 1.1

        def initialize_dynamic_settings(self):
                self.ship_limit = 1.5
                self.bullet_speed = 3.0
                self.alien_speed = 1.0
                self.fleet_direction = 1
                self.alien_points = 10.0

        def increase_speed(self):
                self.ship_speed *= self.speedup_scale
                self.bullet_speed *= self.speedup_scale
                self.alien_speed *= self.speedup_scale

                self.alien_points = int(self.alien_points * self.score_scale)