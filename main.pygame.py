import pygame
import sys

pygame.init()

# Tela
WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animação 4 Direções + Inimigo")

fonte = pygame.font.SysFont("Arial", 28)

# Carrega imagem do fundo
background_img = pygame.image.load("./img/fundo.png").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Frames por direção
right_frames = [pygame.transform.scale(pygame.image.load(f"./img/pixil-frame-{i}.png").convert_alpha(), (64, 64)) for i in range(4)]
left_frames = [pygame.transform.flip(f, True, False) for f in right_frames]
up_frames = [pygame.transform.scale(pygame.image.load(f"./img/cima.png").convert_alpha(), (64, 64)) for i in range(4)]
down_frames = [pygame.transform.scale(pygame.image.load(f"./img/baixo.png").convert_alpha(), (64, 64)) for i in range(4)]

# Carrega imagem do inimigo
enemy_img = pygame.image.load("./img/enemy.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
enemy_x, enemy_y = 100, 150
enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)

# Variáveis
x, y = WIDTH // 2, HEIGHT // 2
velocidade = 5
frame_index = 0
frame_delay = 10
frame_counter = 0
direction = "down"
moving = False
mostrar_mensagem = False

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    # Desenha o fundo
    window.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_a]:
        x -= velocidade
        direction = "left"
        moving = True
    elif keys[pygame.K_d]:
        x += velocidade
        direction = "right"
        moving = True
    elif keys[pygame.K_w]:
        y -= velocidade
        direction = "up"
        moving = True
    elif keys[pygame.K_s]:
        y += velocidade
        direction = "down"
        moving = True

    # Animação
    if moving:
        frame_counter += 1
        if frame_counter >= frame_delay:
            frame_counter = 0
            frame_index = (frame_index + 1) % 4
    else:
        frame_index = 0

    # Escolhe o frame
    if direction == "right":
        personagem_frame = right_frames[frame_index]
    elif direction == "left":
        personagem_frame = left_frames[frame_index]
    elif direction == "up":
        personagem_frame = up_frames[frame_index]
    elif direction == "down":
        personagem_frame = down_frames[frame_index]
    else:
        personagem_frame = down_frames[0]

    personagem_rect = pygame.Rect(x, y, 64, 64)

    # Interação com o inimigo ao apertar "E"
    if personagem_rect.colliderect(enemy_rect) and keys[pygame.K_e]:
        mostrar_mensagem = True
    elif not keys[pygame.K_e]:
        mostrar_mensagem = False

    # Desenha o inimigo
    window.blit(enemy_img, (enemy_x, enemy_y))

    # Desenha personagem
    window.blit(personagem_frame, (x, y))

    # Mensagem
    if mostrar_mensagem:
        texto = fonte.render("Olá!", True, (255, 255, 255))
        window.blit(texto, (WIDTH // 2 - texto.get_width() // 2, 30))

    pygame.display.flip()

pygame.quit()
sys.exit()
