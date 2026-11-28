# alien-invasion-teamX

A 2D arcade space-shooter built with Python and Pygame as a collaborative team project (`elgun201/alien-invasion-teamX`). Players pilot a starship along the bottom of the screen to defend against descending rows of an alien fleet.

---

## Features

* **Smooth Ship Movement:** Responsive left-and-right ship navigation bounded within the game window.
* **Projectile Firing:** Spacebar firing with active on-screen bullet limits and automatic off-screen cleanup.
* **Dynamic Alien Fleet:** Multi-row alien formation that patrols horizontally, drops down upon reaching screen edges, and reverses direction.
* **Collision Detection:** Real-time sprite group collision handling between player bullets and alien ships.
* **60 FPS Game Loop:** Frame-rate capped loop with sound mixer initialization support.

---

## Project Structure

```text
alien-invasion-teamX/
├── alien_invasion.py     # Main entry point and 60 FPS game loop
├── settings.py           # Screen dimensions, colors, speeds, and fleet settings
├── ship.py               # Player Ship sprite class, movement, and rendering
├── bullet.py             # Bullet sprite class and upward projectile logic
├── alien.py              # Alien sprite class, edge detection, and horizontal movement
├── game_functions.py     # Event handling, fleet generation, updates, and screen drawing
├── images/               # Ship and alien sprite assets (e.g., ship.png, alien.png)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
