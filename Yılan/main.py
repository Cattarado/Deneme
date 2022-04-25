import pygame, sys
from Meyve import Meyve
from Yilan import Yilan

pygame.init()
saat = pygame.time.Clock()
ekran_gen,ekran_yuk  = 400, 400
ekran = pygame.display.set_mode((ekran_gen,ekran_yuk))
kenar = 20
ekran_kenar_sayisi = ekran_gen/kenar

yilan = Yilan("red","white" , kenar,ekran_kenar_sayisi)
meyve = Meyve("white", kenar, ekran_kenar_sayisi)

def restart():
    yilan.reset()
    meyve.reset()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        yilan.hizlari_guncelle(event)

    yilan.konum_guncelle()
    if yilan.carpisma_kontrol(): # Yılan gövdesine çarptıysa veya ekran sınırlarını aştıysa
        restart() # oyun yeniden başlasın
    if yilan.yeme_kontrol(meyve): #Yılan meyveyi yediyse
        meyve.reset() # Meyve rastgele başka bir noktada çıksın

    #ÇİZDİRME
    ekran.fill("green")
    yilan.cizdir(ekran)
    meyve.cizdir(ekran)
    pygame.display.flip()
    saat.tick(6)