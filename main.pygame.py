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
drawGroup = pygame.sprite.Group()  # Corrigido: era "Goup" (erro de digitação)

imagem = pygame.image.load("img/carafeliz.png").convert_alpha()  # Certifique-se de que esse caminho e o nome do arquivo estão corretos

guy = pygame.sprite.Sprite(drawGroup)
guy.image = pygame.transform.scale(imagem, [100, 100])  # Corrigido: estava usando guy.image antes de definir
guy.rect = guy.image.get_rect()
guy.rect.topleft = (50, 50)

# Loop principal
gameLoop = True
while gameLoop:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        guy.rect.x += 1
        print("Segurando W")
    if keys[pygame.K_a]:
        guy.rect.x += 1
        print("Segurando W")

    # Draw
    display.fill([87, 8, 44])  # Corrigido: 'display' não estava definido antes, agora está
    drawGroup.draw(display)
    pygame.display.update()
