import pygame
import sys

print("Pygame foi importado com sucesso!")

# Inicializa o Pygame
pygame.init()

# Configurações da tela
tela = pygame.display.set_mode((800, 600))  # Define a largura e altura da tela
pygame.display.set_caption("Meu Primeiro Jogo")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha o jogo se clicar no "X"
            pygame.quit()
            sys.exit()

    # Preenche a tela com a cor branca
    tela.fill(branco)

    # Atualiza a tela
    pygame.display.flip()
