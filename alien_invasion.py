"""Alien Invasion oyununun əsas işəsalma modulu."""

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game() -> None:
    """Oyunu işə salır və əsas dövrəni idarə edir."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Səs sistemini hazırlayır (assets/ qovluğunda fayllar varsa yüklənir)
    pygame.mixer.init()

    # Gəmi, aktiv güllə qrupu və yadplanetli donanma qrupunu yaradır
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Başlanğıc yadplanetli donanmasını yaradır
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 60 FPS sürətini saxlamaq üçün saat obyekti
    clock = pygame.time.Clock()

    # Oyunun əsas dövrəsi
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        clock.tick(60)


if __name__ == "__main__":
    run_game()
