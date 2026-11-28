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
