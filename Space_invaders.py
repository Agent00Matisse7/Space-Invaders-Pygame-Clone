import pygame
import math
import random
from pygame import mixer

# --- 1. Initialization ---
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("WELCOME TO SPACE INVADERS")

# --- 2. Assets & Sound Loading ---
# NOTE: The absolute paths in your original code are commented out.
# For others to run this, you MUST put your image and sound files (e.g., play@2x.png, shoot.wav)
# into the same folder as this Python script, and use the simple filenames below.

# Load Images (Using placeholders/simple filenames)
try:
    playerImage = pygame.image.load('play@2x.png')
    bulletImage = pygame.image.load('player_shot@2x.png')
    invader_template_image = pygame.image.load('inv22@2x.png')
except pygame.error as e:
    print(f"Error loading assets. Ensure images are in the same folder as the script: {e}")
    # Create simple placeholder surfaces if assets fail to load
    playerImage = pygame.Surface((64, 64), pygame.SRCALPHA)
    playerImage.fill((0, 255, 0))  # Green placeholder
    bulletImage = pygame.Surface((16, 32), pygame.SRCALPHA)
    bulletImage.fill((255, 255, 0))  # Yellow placeholder
    invader_template_image = pygame.Surface((64, 64), pygame.SRCALPHA)
    invader_template_image.fill((255, 0, 0))  # Red placeholder

# Load Sounds (Move sound loading outside the loop for efficiency)
try:
    # Mixer Music (background)
    mixer.music.load('ambient_space.wav')  # Placeholder name for your background music
    mixer.music.play(-1)

    # Sound effects
    bullet_sound = mixer.Sound('shoot.wav')
    explosion_sound = mixer.Sound('explosion.wav')
except pygame.error as e:
    print(f"Error loading sounds: {e}")
    # Use dummy functions if sound files are missing
    bullet_sound = lambda: None
    explosion_sound = lambda: None


    def dummy_play():
        pass


    bullet_sound.play = dummy_play
    explosion_sound.play = dummy_play

# --- 3. Score and Fonts ---
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)
game_over_font = pygame.font.Font('freesansbold.ttf', 70)


def show_score(x, y):
    score = font.render("POINTS : " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    # Center the text
    text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(game_over_text, text_rect)


# --- 4. Player Setup ---
player_X = 370
player_Y = screen_height - 77
player_Xchange = 0


def player(x, y):
    # Adjusted position slightly based on original logic
    screen.blit(playerImage, (x - 16, y + 10))


# --- 5. Invader Setup ---
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 8

for num in range(no_of_invaders):
    invaderImage.append(invader_template_image)
    invader_X.append(random.randint(64, screen_width - 64))
    invader_Y.append(random.randint(30, 30))
    invader_Xchange.append(1.2)
    invader_Ychange.append(50)


def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))


# --- 6. Bullet Setup ---
bullet_X = 0
bullet_Y = screen_height - 100
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"  # 'rest' means ready to fire, 'fire' means currently moving


def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"


# --- 7. Collision Detection ---
def isCollision(x1, y1, x2, y2):
    # Distance formula for collision detection
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance < 50:
        return True
    else:
        return False


# --- 8. Game Loop ---
running = True
game_active = True

while running:
    # Set background color (RGB)
    screen.fill((0, 0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_Xchange = -1.7
            if event.key == pygame.K_RIGHT:
                player_Xchange = 1.7
            if event.key == pygame.K_SPACE:
                if bullet_state == "rest" and game_active:
                    bullet_X = player_X
                    bullet(bullet_X, bullet_Y)
                    bullet_sound.play()

        if event.type == pygame.KEYUP:
            player_Xchange = 0

    if game_active:
        # Player movement
        player_X += player_Xchange

        # Boundary checks for player
        if player_X <= 16:
            player_X = 16
        elif player_X >= screen_width - 50:
            player_X = screen_width - 50

        # Invader movement and boundaries
        for i in range(no_of_invaders):
            invader_X[i] += invader_Xchange[i]

            # Invader boundary and movement
            if invader_X[i] >= screen_width - 64 or invader_X[i] <= 0:
                invader_Xchange[i] *= -1  # Reverse direction
                invader_Y[i] += invader_Ychange[i]  # Drop down

            # Invader reaches player (Game Over condition)
            if invader_Y[i] >= player_Y - 100:
                # Check for near horizontal collision before triggering game over
                if abs(player_X - invader_X[i]) <= 80:
                    game_active = False
                    for j in range(no_of_invaders):
                        invader_Y[j] = 2000  # Move invaders off-screen
                    explosion_sound.play()
                    break

            # Collision check between bullet and invader
            collision = isCollision(bullet_X, bullet_Y, invader_X[i], invader_Y[i])
            if collision:
                score_val += 1
                bullet_Y = player_Y
                bullet_state = "rest"
                # Reset invader position
                invader_X[i] = random.randint(64, screen_width - 64)
                invader_Y[i] = random.randint(30, 150)
                invader_Xchange[i] *= -1  # Invert direction on reset for variety

            # Draw the invader
            invader(invader_X[i], invader_Y[i], i)

        # Bullet movement
        if bullet_Y <= 0:
            bullet_Y = player_Y
            bullet_state = "rest"
        if bullet_state == "fire":
            bullet(bullet_X, bullet_Y)
            bullet_Y -= bullet_Ychange

        # Draw player and score
        player(player_X, player_Y)
        show_score(scoreX, scoreY)

    else:
        # If game is not active, show game over screen
        game_over()
        # Optionally stop music here
        mixer.music.stop()

    pygame.display.update()
