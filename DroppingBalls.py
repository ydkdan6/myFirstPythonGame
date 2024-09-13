import pygame, random, sys

pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player = pygame.Rect(200, 500, 30, 30)
player_speed = 5

# Enemy settings
enemy = pygame.Rect(random.randint(0, 370), -50, 30, 30)
enemy_speed = 5

score = 0

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < 400:
        player.x += player_speed

    # Move enemy
    enemy.y += enemy_speed
    if enemy.top > 600:
        enemy.x, enemy.y = random.randint(0, 370), -50
        score += 1
        enemy_speed += 1  # Gradually increase speed for difficulty

    # Collision detection
    if player.colliderect(enemy):
        pygame.quit()
        sys.exit()

    # Drawing player and enemy
    pygame.draw.rect(screen, BLACK, player)
    pygame.draw.rect(screen, RED, enemy)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (70, 10))

    pygame.display.update()
    clock.tick(60)
