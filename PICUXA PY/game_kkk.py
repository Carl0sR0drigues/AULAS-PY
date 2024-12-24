# import pygame
# import os
# import random

# TELA_LARGURA = 500
# TELA_ALTURA = 800

# IMAGEM_CANO = pygame.tranfors.scale2x(os.path.join('imgs', 'pipe.png'))
# IMAGEM_CHAO = pygame.tranfors.scale2x(os.path. join('imgs', 'base.png'))
# IMAGEM_BACKGRUD = pygame.tranfors.scale2x(os.path. join('imgs', 'bg.png'))
# IMAGEM_PASAROS = [
#                     pygame.tranfors.scale2x(os.path. join('imgs', 'bird1.png'))
#                     pygame.tranfors.scale2x(os.path. join('imgs', 'bird2.png'))
#                     pygame.tranfors.scale2x(os.path. join('imgs', 'bird3.png'))
#                 ]

# pygame.font.init()
# FONTE_PONTOS = pygame.font.Sysfont('arial', 50)


# class Passaro:
#     IMGS = IMAGEM_PASAROS
#     # animaçôes da rotação
#     ROTACAO_MAXIMA = 25
#     VELOCIDADE_ROTACAO = 20
#     TEMPO_ANIMACAO = 5

#     def __init__(self, x, Y,):
#         self.x = x
#         self.Y = Y
#         self.angulo = 0
#         self.velocidade = 0
#         self.altura = self.Y
#         self.tempo = 0
#         self.contagem_imagem = 0
#         self.imagem = IMGS[0]

#     def pular(self):
#         self.velocidade = -10.5
#         self.tempo = 0
#         self.altura = self.Y

#     def mover(self):
#         # calcular o deslocamento
#         self.temo += 1
#         deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

#     # restringir o deslocamento
#         if deslocamento > 16:
#              deslocamento = 16
#         elif deslocamento < 0:
#             deslocamento -= 2

#         self.y += deslocamento

#     # o angulodo passaro
#     if deslocamento < 0 or self.y < (self.altura + 50):
#         if self.angulo < self.ROTACAO_MAXIMA:
#            self.angulo = self.ROTACAO_MAXIMA
#     else:
#         if self.angulo > -90:
#            self.angulo -= self.VELOCIDADE_ROTACAO

#     def desenhar(self)
#        # definir qual imagem do passaro vai usar
#        self.contagem_imagem += 1

#         if self.contagem_imagem < self.TEMPO_ANIMACAO:
#                 self.imagem = self.IMGS[0]
#         elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
#             self.imagem = self.iIMGS[1]
#         elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
#             self.imagem = self.IMGS[2]
#         elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
#             self.imagem = self.IMGS[1]
#         elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4 + 1:
#             self.imagem = self.IMGS[0]
#             self.contagem_imagem = 0

#         # se  passaro tiver caindo eu não vou bater asa
#         if self.angulo <= -80
#            self.imagem = self.IMGS[1]
#            self.contagem_imagem = self.TEMPO_ANIMACAO*2

#         # desenhar a imagem
#         imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
#         pos_centro_imagem = self.imagem.get_rect(
#             topleft=(self.x, self.y)).center
#         retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
#         tela.blit(imagem_rotacionada, retangulo.topleft)

#     def get_mask(self):
#         return pygame.mask.from_surface(self.imagem)


# class cano:
#     DISTANCIA = 200
#     VELOCIDADE = 5

#     def __init__(self):
#         self.x = x
#         self.altura = 0
#         self.pos_topo = 0
#         self.pos_base
#         self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
#         self.CANO_BASE + IMAGEM_CANO
#         self.passou = False
#         self.definir_altura()

#     def definir_altura(self):
#        self.altura = random.radrange(50, 450)
#        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
#        self.pos_base = self.altura + self.DISTANCIA

#     def mover(self):
#         self.x -= self.VELOCIDADE

#     def desenhar(self, tela):
#          tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
#         tela.blit(self.CANO_TOPO, (self.x, self.pos_base))

#     def colidir(self, passaro):
#         passaro_mask = passaro.get_mask()
#         topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
#         base_mask = pygame.mask.from_surface(self.CANO_BASE)

#         distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
#         distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))
#         topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
#         base_ponto = passaro_mask.overlap(base_mask, distancia_base)

#         if base_ponto or topo_ponto:
#             return True
#         else:
#             return False


# class Chao:
#     VELOCIDADE = 20
#     LARGURA = IMAGEM_CHAO.get_width
#     IMAGEM = IMAGEM_CHAO

#     def __init__ (self. y):
#         self.y = y
#         self.x1 = 0
#         self.x2 = self.LARGURA

#     def mover(self):
#         self.x1 -= self.VELOCIDADE
#         self.x2 -= self.VELOCIDADE

#         if self.x1 + self.LARGURA <0:
#             self.x1 = self.x2 + self.LARGURA
#         if self.x2 + self.LARGURA <0:
#             self.x2 = self.x2 + self.LARGURA


#     def desenhar(self, tela):
#         tela.blit(self.IMAGEM, (self.x1, self.y))
#         tela.blit(self.IMAGEM, (self.x2, self.y))

# def desenhar_tela(tela, passaro, canos, chao, pontos):
#     tela.blit(IMAGEM_BACKGRUD,(0, 0))
#     for passaro in passa in passaros:
#         passaro.desenhar(tela)

#     for cano in canos:
#         cano.desenhar(tela)

# texto = FONTE_PONTOS.render(f"pontuação {pontos}", 1, (255, 255, 255))
# tela.blit(texto, ())


# def main:
#     passaros = [Passaro (230, 350)]
#     chao = chao(730
#     canos =  [Cano(700)]
#     tela = pygame.diplay .set_mode((TELA_LARGURA, TELA _ALTURA))
#     pontos = 0
#     relogio = pygame.time.Clock()

#     rodando = True
#     while rodando:
#         relogio.tick(30)

#         for evento in py game.event.get():
#             if evento.key == pygame.K_space:
#                 rodando =False
#                 pygame.quit()
#                 quit()
#             if evento.type == pygame.KEYDOWN:
#                 if evento.key == pygame.K_SPACE:
#                     for passaro in passaros:
#                     passaro.pular


#         #mover as coisas
#         for Passaro in passaros:
#             pssaro.mover()
#         chao.mover()

#         adicionar_cano= False
#         remover_cano = []
#         for cano in canos:
#             for i, Passaro in enumerate(Passaro):
#                 if cano.colidir(passaro):
#                     passaros.pop(i)
#                 if not cano.passou and passaro.x > cano.x:
#                     cano.passou = True
#                     adicionar_cano = True
#             cano.mover()
#             if cano.x + cano.CANO_TOPO.get_width() < 0:
#                remover_canos.append(cano)

#             if adicionar_cano:
#                 pontos += 1
#                 canos.append(Cano(600))
#             for cano if remover_cano:
#                 canos.remover(cano)

#             for i, passaro in enumerate(passaros):
#                 if (passaro.y + passaro.imagem.get_height()) > chao.y


#         desenhar_tela(tela,passaros, canos, chao, pontos)

import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGRUD = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGEM_PASAROS = [
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Passaro:
    IMGS = IMAGEM_PASAROS
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0
            

        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO * 2

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(
            topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))
        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        return bool(topo_ponto or base_ponto)


class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))


def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGRUD, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)
    chao.desenhar(tela)
    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (10, 10))
    pygame.display.update()


def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()
    rodando = True

    while rodando:
        relogio.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()

        for passaro in passaros:
            passaro.mover()
        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)

                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True

            cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
        for cano in remover_canos:
            canos.remove(cano)

        for passaro in passaros:
            if (passaro.y + passaro.imagem.get_height()) > chao.y:
                passaros.remove(passaro)

        desenhar_tela(tela, passaros, canos, chao, pontos)


if __name__ == "__main__":
    main()
