import pygame
import sys
import math

pygame.init()

# --- Screen Setup ---
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Outstron - Singleplayer")
clock = pygame.time.Clock()

# --- Fonts ---
font_large = pygame.font.SysFont("Arial", 80)
font_medium = pygame.font.SysFont("Arial", 50)
font_small = pygame.font.SysFont("Arial", 30)

# --- Colors ---
BLUE = (0, 120, 255)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)

# --- Game States ---
STATE_HOME = "home"
STATE_TRACK_SELECT = "track_select"
STATE_CAR_SELECT = "car_select"
STATE_RACE = "race"

game_state = STATE_HOME

# --- Buttons ---
buttons = {}
def draw_button(text, x, y, w, h, color=BLUE):
    pygame.draw.rect(screen, color, (x, y, w, h))
    label = font_medium.render(text, True, WHITE)
    screen.blit(label, label.get_rect(center=(x + w//2, y + h//2)))
    return pygame.Rect(x, y, w, h)

# --- Track ---
bahrain_track = pygame.Surface((WIDTH, HEIGHT))
bahrain_track.fill((34, 139, 34))  # green grass

# --- Car Physics ---
class Car:
    def __init__(self):
        self.image = pygame.Surface((60, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, RED, [(0,0),(60,15),(0,30)])  # simple shape
        self.orig_image = self.image
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.angle = 0
        self.speed = 0
        self.max_speed = 320 / 3.6  # convert km/h to m/s for game scale
        self.acceleration = 0.3
        self.brake_deceleration = 0.5
        self.turn_speed = 3

    def update(self, keys):
        # Acceleration
        if keys[pygame.K_w]:
            self.speed += self.acceleration
        elif keys[pygame.K_s]:
            self.speed -= self.brake_deceleration
        else:
            # natural friction
            self.speed *= 0.98

        # Clamp speed
        if self.speed > self.max_speed/20:  # scale down for Pygame units
            self.speed = self.max_speed/20
        if self.speed < -self.max_speed/40:  # reverse slower
            self.speed = -self.max_speed/40

        # Turning
        if keys[pygame.K_a]:
            self.angle += self.turn_speed * (self.speed/2)
        if keys[pygame.K_d]:
            self.angle -= self.turn_speed * (self.speed/2)

        # Move car
        rad = math.radians(self.angle)
        self.x += math.cos(rad) * self.speed
        self.y -= math.sin(rad) * self.speed  # y-axis inverted in Pygame

    def draw(self, surface):
        rotated = pygame.transform.rotate(self.orig_image, self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect)

car = Car()

# --- Main Loop ---
while True:
    screen.fill(GRAY)
    mx, my = pygame.mouse.get_pos()
    click = False

    for event in pygameevent.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click = True

    keys = pygame.key.get_pressed()

    # --- Home Screen ---
    if game_state == STATE_HOME:
        title = font_large.render("Outstron", True, BLUE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//4)))

        buttons['singleplayer'] = draw_button("Singleplayer", WIDTH//2-150, HEIGHT//2, 300, 80)
        if click and buttons['singleplayer'].collidepoint(mx, my):
            game_state = STATE_TRACK_SELECT

    # --- Track Selection ---
    elif game_state == STATE_TRACK_SELECT:
        title = font_large.render("Select Track", True, BLUE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//4)))

        buttons['bahrain'] = draw_button("Bahrain GPX", WIDTH//2-150, HEIGHT//2, 300, 80)
        if click and buttons['bahrain'].collidepoint(mx, my):
            game_state = STATE_CAR_SELECT

    # --- Car Selection ---
    elif game_state == STATE_CAR_SELECT:
        title = font_large.render("Select Car", True, BLUE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//4)))

        buttons['audi'] = draw_button("Audi RS8", WIDTH//2-150, HEIGHT//2, 300, 80)
        if click and buttons['audi'].collidepoint(mx, my):
            game_state = STATE_RACE

    # --- Race ---
    elif game_state == STATE_RACE:
        screen.blit(bahrain_track, (0,0))
        car.update(keys)
        car.draw(screen)

        race_text = font_large.render("Bahrain GPX - Audi RS8", True, BLUE)
        screen.blit(race_text, race_text.get_rect(center=(WIDTH//2, 50)))

        # Speed display
        speed_kmh = round(car.speed * 20 * 3.6, 1)  # scale back to km/h for display
        speed_text = font_small.render(f"Speed: {speed_kmh} km/h", True, WHITE)
        screen.blit(speed_text, (10, HEIGHT-40))

    pygamedisplay.flip()
    clock.tick(60)
class Car:
    def __init__(self):
        self.image = pygame.Surface((60,30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (255,0,0), [(0,0),(60,15),(0,30)])
        self.orig_image = self.image
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.angle = 0
        self.speed = 0
        self.max_speed = 320 / 3.6  # realistic 320 km/h scaled
        self.acceleration = 0.3
        self.brake_deceleration = 0.5
        self.turn_speed = 3

    def update(self, keys):
        if keys[pygame.K_w]:
            self.speed += self.acceleration
        elif keys[pygame.K_s]:
            self.speed -= self.brake_deceleration
        else:
            self.speed *= 0.98  # friction

        if self.speed > self.max_speed/20:
            self.speed = self.max_speed/20
        if self.speed < -self.max_speed/40:
            self.speed = -self.max_speed/40

        if keys[pygame.K_a]:
            self.angle += self.turn_speed * (self.speed/2)
        if keys[pygame.K_d]:
            self.angle -= self.turn_speed * (self.speed/2)

        rad = math.radians(self.angle)
        self.x += math.cos(rad) * self.speed
        self.y -= math.sin(rad) * self.speed

    def draw(self, surface):
        rotated = pygame.transform.rotate(self.orig_image, self.angle)
        rect = rotated.get_rect(center=(self.x,self.y))
        surface.blit(rotated, rect)
