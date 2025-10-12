🚀 Space Invaders Pygame Clone
A classic arcade-style shooter built using the Pygame library in Python. Defend the earth against an endless wave of invaders!

🌟 Features
Real-time Movement: Smooth player movement and responsive controls.

Dynamic Invaders: Enemies move back and forth, descending with each boundary hit.

Collision Detection: Accurate hit detection for bullets and invaders.

Scoring System: Track your performance with a live point counter.

Game Over Condition: The game ends if an invader reaches the player's line.

Sound Effects: Background music, shooting sounds, and an explosion effect (requires local sound files).

💻 Requirements
To run this game locally, you need:

Python 3 (version 3.6 or newer recommended).

The Pygame library.

Installation
Install Pygame using pip:

pip install pygame


🛠️ Setup and Running the Game
Clone the Repository (or download the files):

git clone [https://github.com/YOUR_USERNAME/Space-Invaders-Pygame.git](https://github.com/YOUR_USERNAME/Space-Invaders-Pygame.git)
cd Space-Invaders-Pygame


Ensure Assets Are Present:
⚠️ IMPORTANT: The game requires several image and sound files. Make sure the following files are located in the same directory as space_invaders.py:

play@2x.png (Player ship image)

player_shot@2x.png (Bullet image)

inv22@2x.png (Invader image)

ambient_space.wav (Background music - or similar name)

shoot.wav (Bullet sound effect)

explosion.wav (Game over/collision sound effect)

Run the Script:

python space_invaders.py


🕹️ Controls
| Key | Action |
| Left Arrow | Move player ship left |
| Right Arrow | Move player ship right |
| Spacebar | Fire a bullet (only one bullet can be active at a time) |
| ESC / Close Window | Exit the game |
