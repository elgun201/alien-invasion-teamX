"""Oyunun ümumi konfiqurasiya parametrlərini saxlayan modul."""


class Settings:
    """Alien Invasion oyunu üçün bütün tənzimləmələri saxlayan sinif."""

    def __init__(self) -> None:
        """Oyunun ilkin parametrlərini işə salır."""
        # Ekran parametrləri
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25, 30, 48)

        # Kosmik gəmi parametrləri
        self.ship_speed_factor = 1.5

        # Güllə (mərmi) parametrləri
        self.bullet_speed_factor = 3.0
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 90, 90)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Oyun vəziyyəti və bitiş mesajı parametrləri
        self.game_active = True
        self.end_message = ""
        self.win_color = (80, 255, 140)
        self.lose_color = (255, 90, 90)
```[cite: 7]

