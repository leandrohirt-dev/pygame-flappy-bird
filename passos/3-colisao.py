import pygame
import random

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
emoji = pygame.font.SysFont("segoeuiemoji", 36)
passaro = emoji.render("\U0001F424", 1, "white")
passaro = pygame.transform.flip(passaro, True, False)
y = 200
vel = 0
canos = []
quadro = 0

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                vel = -9

    vel += 0.8
    y += vel
    corpo = pygame.Rect(100, y, 40, 34)

    quadro += 1
    if quadro % 45 == 0:
        buraco = random.randint(60, 250)
        canos.append(pygame.Rect(600, 0, 60, buraco))
        baixo = buraco + 140
        canos.append(pygame.Rect(600, baixo, 60, 400))
    for cano in canos:
        cano.x -= 4
    canos = [c for c in canos if c.right > 0]

    fora = corpo.top < 0 or corpo.bottom > 400
    if fora or corpo.collidelist(canos) >= 0:
        y, vel = 200, 0
        canos.clear()

    tela.fill("skyblue")
    for cano in canos:
        pygame.draw.rect(tela, "forestgreen", cano)
        pygame.draw.rect(tela, "darkgreen", cano, 4)
    pos = passaro.get_rect(center=corpo.center)
    tela.blit(passaro, pos)
    pygame.display.flip()
    relogio.tick(30)

pygame.quit()
