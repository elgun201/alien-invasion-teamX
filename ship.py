"""Oyunçunun kosmik gəmisini və hərəkət məntiqini idarə edən modul."""

from pathlib import Path
import pygame


class Ship:
    """Kosmik gəminin təsvirini, mövqeyini və hərəkətini idarə edən sinif."""

    def __init__(self, ai_settings, screen) -> None:
        """Gəmini işə salır və ekranın alt mərkəzində yerləşdirir."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Gəmi şəklini yükləyir və ölçüləndirir (assets/ və ya images/ qovluğundan)
        ship_image_path = self._resolve_ship_image()
        if ship_image_path is not None:
            loaded_image = pygame.image.load(str(ship_image_path))
            self.image = pygame.transform.scale(loaded_image, (60, 48))
        else:
            # Şəkil faylı hələ əlavə olunmayıbsa, ehtiyat qrafik səth yaradır
            self.image = pygame.Surface((60, 48), pygame.SRCALPHA)
            pygame.draw.polygon(
                self.image,
                (100, 200, 255),
                [(30, 0), (58, 46), (30, 36), (2, 46)],
            )

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Hər yeni gəmini ekranın alt mərkəzində yerləşdirir
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Gəminin mərkəz koordinatını kəsr ədəd (float) kimi saxlayır
        self.center = float(self.rect.centerx)

        # Hərəkət bayraqları
        self.moving_right = False
        self.moving_left = False

    @staticmethod
    def _resolve_ship_image() -> Path | None:
        """Mümkün qovluqlarda gəmi şəkil faylını (.png / .bmp) axtarır."""
        candidate_paths = [
            Path("assets/ship.png"),
            Path("assets/ship.bmp"),
            Path("images/ship.png"),
            Path("images/ship.bmp"),
        ]
        for path in candidate_paths:
            if path.exists():
                return path
        return None

    def update(self) -> None:
        """Hərəkət bayraqlarına əsasən gəminin mövqeyini və sərhədləri yeniləyir."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Kəsr dəyəri (float) tam ədəd kimi rect.centerx-ə mənimsədir
        self.rect.centerx = self.center

    def blitme(self) -> None:
        """Gəmini cari mövqeyində ekranda çəkir."""
        self.screen.blit(self.image, self.rect)


if __name__ == "__main__":
    # Digər modullar hazır olmadan ship.py faylını təkbaşına test etmək üçün
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Ship Modulu Testi")
    clock = pygame.time.Clock()

    class MockSettings:
        ship_speed_factor = 4.5
        bg_color = (25, 30, 48)

    ai_settings = MockSettings()
    ship = Ship(ai_settings, screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_q:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

        ship.update()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
