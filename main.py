import pygame
from random import randint
from time import sleep

pygame.init()

pedra = pygame.image.load("download.png")
imgpedra = pygame.transform.scale(pedra, (100, 100))

papel = pygame.image.load("papel.png")
imgpapel = pygame.transform.scale(papel, (100, 100))

tesoura = pygame.image.load("tesoura.png")
imgtesoura = pygame.transform.scale(tesoura, (100, 100))

txt = "Jokenpo"
pygame.font.init()
fonte = pygame.font.get_default_font()
fontesys = pygame.font.SysFont(fonte, 60)
txttela = fontesys.render(txt, 1, (255,255,255))

def win_result(ganhador, tela):
    text_vc = "Você"
    text_cp = "Computador"
    pygame.font.init()
    fonte = pygame.font.get_default_font()
    fontesys = pygame.font.SysFont(fonte, 60)
    txt_tela = fontesys.render(text_vc, 1, (255, 255, 255))
    tela.blit(txt_tela, (50, 104))
    txt_pc = fontesys.render(text_cp, 1, (255, 255, 255))
    tela.blit(txt_pc, (250, 104))
    fontewin = pygame.font.SysFont(fonte, 50)
    txt_winer = fontewin.render(ganhador, 1, (255, 255, 255))
    tela.blit(txt_winer, (100, 300))

def main():
    tela_largura = 500
    tela_altura = 500
    tela = pygame.display.set_mode((tela_largura, tela_altura))
    pygame.display.set_caption('JOKENPO')

    tela.blit(imgpapel, (50, 300))
    tela.blit(imgtesoura, (200, 300))
    tela.blit(imgpedra, (350, 300))
    tela.blit(txttela, (150, 150))
    pygame.display.update()

    winer = False
    while not winer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                cp = randint(0, 2)
                if pos[0] <= 150 and pos[1] <= 400:
                    if cp == 0:
                        tela.fill((255, 0, 0))
                        tela.blit(imgpapel, (50, 140))
                        tela.blit(imgpapel, (350, 140))
                        ganhador = "Empate"
                        win_result(ganhador, tela)
                        pygame.display.update()
                        winer = True
                    elif cp == 1:
                        tela.fill((255, 0, 0))
                        tela.blit(imgpapel, (50, 140))
                        tela.blit(imgtesoura, (350, 140))
                        ganhador = "Computador Ganhou"
                        win_result(ganhador, tela)
                        pygame.display.update()
                        winer = True
                    else:
                        tela.fill((255, 0, 0))
                        tela.blit(imgpapel, (50, 140))
                        tela.blit(imgpedra, (350, 140))
                        ganhador = "Você ganhou"
                        win_result(ganhador, tela)
                        pygame.display.update()
                        winer = True
                elif pos[0] <= 300 and pos[1] <= 400 and pos[0] >= 150:
                        if cp == 0:
                            tela.fill((255, 0, 0))
                            tela.blit(imgtesoura, (50, 140))
                            tela.blit(imgpapel, (350, 140))
                            ganhador = "Você Ganhou"
                            win_result(ganhador, tela)
                            pygame.display.update()
                            winer = True
                        elif cp == 1:
                            tela.fill((255, 0, 0))
                            tela.blit(imgtesoura, (50, 140))
                            tela.blit(imgtesoura, (350, 140))
                            ganhador = "Empate"
                            win_result(ganhador, tela)
                            pygame.display.update()
                            winer = True
                        else:
                            tela.fill((255, 0, 0))
                            tela.blit(imgtesoura, (50, 140))
                            tela.blit(imgpedra, (350, 140))
                            ganhador = "Computador Ganhou"
                            win_result(ganhador, tela)
                            pygame.display.update()
                            winer = True
                elif pos [0] <= 450 and pos[1] <= 400 and pos[0] >= 300:
                    if cp == 0:
                        tela.fill((255, 0, 0))
                        tela.blit(imgpedra, (50, 140))
                        tela.blit(imgpapel, (350, 140))
                        ganhador = "Computador Ganhou"
                        win_result(ganhador, tela)
                        pygame.display.update()
                        winer = True
                    elif cp == 1:
                        tela.fill((255, 0, 0))
                        tela.blit(imgpedra, (50, 140))
                        tela.blit(imgtesoura, (350, 140))
                        ganhador = "Você Ganhou"
                        win_result(ganhador, tela)
                        pygame.display.update()
                        winer = True
                    else:
                        tela.fill((255, 0, 0))
                        tela.blit(imgpedra, (50, 140))
                        tela.blit(imgpedra, (350, 140))
                        ganhador = "Empate"
                        win_result(ganhador, tela)
                        pygame.display.update()
                        winer = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

main()
