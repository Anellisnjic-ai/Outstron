import pygame
import sys

pygame.init()
pygame.joystick.init()

# --- Screen Setup ---
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Outstron")
clock = pygame.time.Clock()
font_large = pygame.font.SysFont("Arial", 80)
font_medium = pygame.font.SysFont("Arial", 50)
font_small = pygame.font.SysFont("Arial", 30)

# --- Colors ---
BLUE = (0, 120, 255)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
BLACK = (0, 0, 0)

# --- Game States ---
STATE_HOME = "home"
STATE_SINGLEPLAYER = "singleplayer"
STATE_TIME_TRIAL = "time_trial"
STATE_CAR_SELECTION = "car_selection"
STATE_RACE = "race"
STATE_CONTROLLER_DISCONNECT = "controller_disconnect"
game_state = STATE_HOME

# --- Buttons ---
buttons = {}

def draw_button(text, x, y, w, h, color=BLUE):
    pygame.draw.rect(screen, color, (x, y, w, h))
    label = font_medium.render(text, True, WHITE)
    label_rect = label.get_rect(center=(x + w//2, y + h//2))
    screen.blit(label, label_rect)
    return pygame.Rect(x, y, w, h)

# --- Placeholder Assets ---
bahrain_track = pygame.Surface((WIDTH, HEIGHT))
bahrain_track.fill((200, 200, 150))
audi_rs8 = pygame.Surface((200, 100))
audi_rs8.fill((255, 0, 0))

controller_connected = True if pygame.joystick.get_count() > 0 else False

# --- Main Loop ---
while True:
    screen.fill(GRAY)
    mx, my = pygame.mouse.get_pos()
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        elif event.type == pygame.JOYDEVICEREMOVED:
            controller_connected = False
            game_state = STATE_CONTROLLER_DISCONNECT
        elif event.type == pygame.JOYDEVICEADDED:
            controller_connected = True

    # --- Controller Disconnect Screen ---
    if game_state == STATE_CONTROLLER_DISCONNECT:
        screen.fill(BLACK)
        msg = font_large.render("Controller Disconnected", True, WHITE)
        sub = font_small.render("Press any button to continue", True, WHITE)
        screen.blit(msg, msg.get_rect(center=(WIDTH//2, HEIGHT//2 - 50)))
        screen.blit(sub, sub.get_rect(center=(WIDTH//2, HEIGHT//2 + 50)))
        if click or event.type == pygame.KEYDOWN or event.type == pygame.JOYBUTTONDOWN:
            game_state = STATE_HOME
            controller_connected = True

    # --- Home Screen ---
    elif game_state == STATE_HOME:
        title = font_large.render("Outstron", True, BLUE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//4)))

        buttons['singleplayer'] = draw_button("Singleplayer", WIDTH//2-150, HEIGHT//2, 300, 80)
        buttons['multiplayer'] = draw_button("Multiplayer", WIDTH//2-150, HEIGHT//2 - 120, 300, 80, color=GRAY)  # Placeholder

        if click:
            if buttons['singleplayer'].collidepoint(mx, my):
                game_state = STATE_SINGLEPLAYER

    # --- Singleplayer Screen ---
    elif game_state == STATE_SINGLEPLAYER:
        title = font_large.render("Singleplayer", True, BLUE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//4)))

        buttons['time_trial'] = draw_button("Time Trial", WIDTH//2-150, HEIGHT//2, 300, 80)
        if click:
            if buttons['time_trial'].collidepoint(mx, my):
                game_state = STATE_CAR_SELECTION

    # --- Car Selection Screen ---
    elif game_state == STATE_CAR_SELECTION:
        title = font_large.render("Select Your Car", True, BLUE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//4)))

        buttons['audi'] = draw_button("Audi RS8", WIDTH//2-150, HEIGHT//2, 300, 80)
        screen.blit(audi_rs8, (WIDTH//2-100, HEIGHT//2 + 100))

        if click:
            if buttons['audi'].collidepoint(mx, my):
                game_state = STATE_RACE

    # --- Race Screen ---
    elif game_state == STATE_RACE:
        screen.blit(bahrain_track, (0, 0))
        screen.blit(audi_rs8, (WIDTH//2-100, HEIGHT//2+200))
        race_text = font_large.render("Bahrain GPX", True, BLUE)
        screen.blit(race_text, race_text.get_rect(center=(WIDTH//2, 50)))

    pygame.display.flip()
    clock.tick(60)
