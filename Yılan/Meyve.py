import random

import pygame

class Meyve(pygame.Rect):
    def __init__(self,renk, kenar, ekran_kenar_sayisi):
        super().__init__(0,0 ,kenar,kenar)
        self.renk = renk
        self.kenar = kenar
        self.ekran_kenar_sayisi=ekran_kenar_sayisi
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.ekran_kenar_sayisi-1) * self.kenar
        self.y = random.randint(0, self.ekran_kenar_sayisi-1) * self.kenar

    def cizdir(self, ekran):
        pygame.draw.rect(ekran, self.renk, self)