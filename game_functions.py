"""Module managing game events, bullets, alien fleet, and screen updates."""

import sys
import pygame

from alien import Alien
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE and ai_settings.game_active:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    bullets_allowed = getattr(ai_settings, "bullets_allowed", 3)
    if len(bullets) < bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, bullets, aliens):
    """Update bullet positions, remove collisions, and check win condition."""
    bullets.update()

    # Ekranın üstünden çıkan mermileri temizler
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Çarpışan mermi ve kareleri siler
    pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Ekranda hiç kare kalmadıysa oyunu kazanma ekranıyla bitirir
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.game_active = False
        ai_settings.end_message = "YOU WIN"


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (
        ai_settings.screen_height - (3 * alien_height) - ship_height
    )
    return int(available_space_y / (2 * alien_height))


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height
    )

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, screen, aliens):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ai_settings.game_active = False
            ai_settings.end_message = "GAME OVER"
            break


def update_aliens(ai_settings, screen, aliens):
    """Check edges/bottom, then update all alien positions."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    check_aliens_bottom(ai_settings, screen, aliens)


def draw_end_message(ai_settings, screen):
    """Draw YOU WIN or GAME OVER text at the center of the screen."""
    if not ai_settings.end_message:
        return

    font = pygame.font.SysFont(None, 96)
    color = (
        ai_settings.win_color
        if ai_settings.end_message == "YOU WIN"
        else ai_settings.lose_color
    )
    text_surface = font.render(ai_settings.end_message, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = screen.get_rect().center
    screen.blit(text_surface, text_rect)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)

    if ai_settings.game_active:
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
    else:
        draw_end_message(ai_settings, screen)

    pygame.display.flip()
```[cite: 1, 2, 4, 7, 9]

