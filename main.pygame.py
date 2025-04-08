import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura = 640
altura = 480
display = pygame.display.set_mode((largura, altura))  # Corrigido: nome da variável era 'tela', mas você usa 'display'

# Mudar o nome da janela 
pygame.display.set_caption("Jogo dos D")

# Carregar imagem e sprite
drawGroup = pygame.sprite.Group() 

imagem = pygame.image.load("img/carafeliz.png").convert_alpha()  # trasparencia convert_alpha

guy = pygame.sprite.Sprite(drawGroup)
guy.image = pygame.transform.scale(imagem, [100, 100]) 
guy.rect = guy.image.get_rect()
guy.rect.topleft = (50, 50)

# music
pygame.mixer.music.load("audio/blues.mp3")
pygame.mixer.music.play(-1)

# Sounds
complete = pygame.mixer.Sound("audi/completetask_0.mp3")

# Loop principal
gameLoop = True
while gameLoop:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                complete.play()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        guy.rect.x += 1
        print("Segurando W")
    if keys[pygame.K_a]:
        guy.rect.x += 1
        print("Segurando W")

    # Draw
    display.fill([87, 8, 44])  
    drawGroup.draw(display)
    pygame.display.update()

    