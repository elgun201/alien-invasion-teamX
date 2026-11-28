import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Kosmik gəmidən atılan güllələri idarə edən sinif."""

    def __init__(self, ai_settings, screen, ship) -> None:
        """Gəminin cari mövqeyində yeni güllə obyekti yaradır."""
        super().__init__()
        self.screen = screen

        # (0, 0) koordinatında düzbucaqlı güllə yaradır və düzgün mövqeyə gətirir
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Güllənin mövqeyini kəsr ədəd (float) kimi saxlayır
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self) -> None:
        """Gülləni ekran boyunca yuxarı doğru hərəkət etdirir."""
        # Güllənin kəsr mövqeyini yeniləyir
        self.y -= self.speed_factor
        # Düzbucaqlının (rect) mövqeyini yeniləyir
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Gülləni ekranda çəkir."""
        pygame.draw.rect(self.screen, self.color, self.rect)


if __name__ == "__main__":
    # Digər komanda yoldaşlarının faylları olmadan təkbaşına test etmək üçün
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bullet Modulu Testi")
    clock = pygame.time.Clock()

    class MockSettings:
        bullet_width = 4
        bullet_height = 15
        bullet_color = (255, 80, 80)
        bullet_speed_factor = 5.0

    class MockShip:
        def __init__(self, screen_rect):
            self.rect = pygame.Rect(0, 0, 50, 40)
            self.rect.centerx = screen_rect.centerx
            self.rect.bottom = screen_rect.bottom - 10

    mock_settings = MockSettings()
    mock_ship = MockShip(screen.get_rect())
    bullets = pygame.sprite.Group()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.add(Bullet(mock_settings, screen, mock_ship))

        screen.fill((20, 24, 38))
        pygame.draw.rect(screen, (70, 180, 255), mock_ship.rect)

        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            bullet.draw_bullet()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
