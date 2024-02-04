import pygame as pg
import sys
import random as rd

# Initierer pygame
pg.init()

# Poeng font
font = pg.font.SysFont("Arial", 40)
poeng = 0

# Konstanter
WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
FPS = 60

# Farger
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

background_img = pg.image.load("ground.png")
background_img = pg.transform.scale(background_img, (800, 600))

spokelse_img = pg.image.load("spokelse.png")
spokelse_img = pg.transform.scale(spokelse_img, (40, 40))

sau_img = pg.image.load("sau.png")
sau_img = pg.transform.scale(sau_img, (40, 40))

menneske_side_img = pg.image.load("menneske_side.png")
menneske_side_img = pg.transform.scale(menneske_side_img, (100, 600))

sau_side_img = pg.image.load("sau_side.png")
sau_side_img = pg.transform.scale(sau_side_img, (100, 600))

# Lager en overflate
surface = pg.display.set_mode(SIZE)

# Lager klokke
clock = pg.time.Clock()

# Variabel som styrer om spillet skal kjores
run = True


# Klasser

class Spillbrett:
    spokelser = []  
    hindringer = []
    sauer = []

    def leggTilSpillObjekt(self, spillobjekt):
        if isinstance(spillobjekt, Spokelse):
            self.spokelser.append(spillobjekt)
        elif isinstance(spillobjekt, Hindring):
            self.hindringer.append(spillobjekt)
        else:
            self.sauer.append(spillobjekt)

    def fjernSpillObjekt(self, spillobjekt):
        if isinstance(spillobjekt, Spokelse):
            self.spokelser.remove(spillobjekt)
        elif isinstance(spillobjekt, Hindring):
            self.hindringer.remove(spillobjekt)
        else:
            self.sauer.remove(spillobjekt)

    # Funksjon som viser antall poeng
    def antallPoeng(self):
        text_img = font.render(f"Antall sauer: {poeng}", True, WHITE)
        surface.blit(text_img, (30, 30))
    
    
    

class Spillobjekt:
    def __init__(self, xPosisjon, yPosisjon):
        self.xPosisjon = xPosisjon
        self.yPosisjon = yPosisjon

    def settPosisjon(self, x, y):
        self.xPosisjon = x
        self.yPosisjon = y


    def hentPosisjon(self):
        return (self.xPosisjon, self.yPosisjon)
""" 
# Spøkelse klasse
class Spokelse(Spillobjekt):
    def __init__(self):
        super().__init__(rd.randint(100, WIDTH - 140), rd.randint(0, HEIGHT - 40))
        self.vx = 3
        self.vy = 3

    def tegnSpokelse(self):
        surface.blit(spokelse_img,(self.xPosisjon, self.yPosisjon))

    def endreRetning(self):
        self.xPosisjon += self.vx
        self.yPosisjon += self.vy

        if self.xPosisjon <= 100 or self.xPosisjon > WIDTH - 140:
            self.vx *= -1

        if self.yPosisjon > HEIGHT - 40 or self.yPosisjon < 0:
            self.vy *= -1

    def hentRektangel(self):
        return pg.Rect(self.xPosisjon, self.yPosisjon, 40, 40)

    def frys(self):
        self.vx = 0
        self.vy = 0
"""
# Menneske klasse
class Menneske(Spillobjekt):
    
    def __init__(self, fart, poeng, holderSau):
        super().__init__(rd.randint(0, 100 - 40), rd.randint(0, HEIGHT - 40))
        self.fart = fart
        self.poeng = poeng
        self.holderSau = False
        self.sauSomErHoldt = None 

    def hentRektangel(self):
        return pg.Rect(self.xPosisjon, self.yPosisjon, 40, 40)

    #Hindrer at man setter seg fast i hindringer
    def hentNesteRektangel(self, dx, dy):
        return pg.Rect(self.xPosisjon + dx, self.yPosisjon + dy, 40, 40)

    def settHastighet(self, vx,vy):
        self.vx = vx
        self.vy = vy


    def beveg(self, hindringer):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT] and self.xPosisjon > 0:
            if not any(self.hentNesteRektangel(-5,0).colliderect(hindring.hentRektangel()) for hindring in hindringer):
                self.xPosisjon -= self.vx
        if keys[pg.K_RIGHT] and self.xPosisjon < WIDTH - W:
            if not any(self.hentNesteRektangel(5,0).colliderect(hindring.hentRektangel()) for hindring in hindringer):
                self.xPosisjon += self.vx
        if keys[pg.K_DOWN] and self.yPosisjon < HEIGHT - H:
            if not any(self.hentNesteRektangel(0,5).colliderect(hindring.hentRektangel()) for hindring in hindringer):
                self.yPosisjon += self.vy
        if keys[pg.K_UP] and self.yPosisjon > 0:
            if not any(self.hentNesteRektangel(0,-5).colliderect(hindring.hentRektangel()) for hindring in hindringer):
                self.yPosisjon -= self.vy
                
# Spøkelse klasse
class Spokelse(Spillobjekt):
    def __init__(self):
        super().__init__(rd.randint(100, WIDTH - 140), rd.randint(0, HEIGHT - 40))
        self.vx = 3
        self.vy = 3

    def tegnSpokelse(self):
        surface.blit(spokelse_img,(self.xPosisjon, self.yPosisjon))

    def endreRetning(self):
        self.xPosisjon += self.vx
        self.yPosisjon += self.vy

        if self.xPosisjon <= 100 or self.xPosisjon > WIDTH - 140:
            self.vx *= -1

        if self.yPosisjon > HEIGHT - 40 or self.yPosisjon < 0:
            self.vy *= -1

    def hentRektangel(self):
        return pg.Rect(self.xPosisjon, self.yPosisjon, 40, 40)

    def frys(self):
        self.vx = 0
        self.vy = 0
                
# Hindring klasse
class Hindring(Spillobjekt):
    def __init__(self):
        super().__init__(rd.randint(100, WIDTH - 180), rd.randint(0, HEIGHT - 80))
        self.bredde = rd.randint(10, 80)
        self.hoyde = rd.randint(10, 80)

    def tegnHindring(self):
        pg.draw.rect(surface, BLACK, [self.xPosisjon, self.yPosisjon, self.bredde, self.hoyde])

    def hentRektangel(self):
        return pg.Rect(self.xPosisjon, self.yPosisjon, self.bredde, self.hoyde)
        
# Saue klasse
class Sau(Spillobjekt):
    def __init__(self):
        super().__init__(rd.randint(WIDTH - 100, WIDTH - 40), rd.randint(0, HEIGHT - 40))

    def tegnSau(self):
        surface.blit(sau_img, (self.xPosisjon, self.yPosisjon))

    def hentRektangel(self):
        return pg.Rect(self.xPosisjon, self.yPosisjon, 40, 40)

    def sauKollisjon(self):
        while len(spillbrett.sauer) < 3:
            nySau = Sau()
            ok = True

            for sau in spillbrett.sauer:
                if nySau.hentRektangel().colliderect(sau.hentRektangel()):
                    ok = False
                    print("prøver igjen")
                    break

            if ok:
                spillbrett.leggTilSpillObjekt(nySau)
        


# Oppretter menneskeobjektet
menneske = Menneske(0, 0, False)
menneske.settHastighet(5,5)

W = 40
H = 40

spillbrett = Spillbrett()

# Lager 3 sauer som skal være der fra start
for i in range(0,3):
    hindring = Hindring()
    spillbrett.leggTilSpillObjekt(hindring)
    sau = Sau()
    spillbrett.leggTilSpillObjekt(sau)

spokelse = Spokelse()
spillbrett.leggTilSpillObjekt(spokelse)


# Spill-lokken
while run:
    # Sorger for at lokken kjores i korrekt hastighet
    clock.tick(FPS)

    # Gar gjennom hendelser (events)
    for event in pg.event.get():
        # Sjekker om vi onsker a lukke vinduet
        if event.type == pg.QUIT:
            run = False  # Spillet skal avsluttes

    # Kaller menneske bevegmetoden
    menneske.beveg(spillbrett.hindringer)

    if any(menneske.hentRektangel().colliderect(hindring.hentRektangel()) for hindring in spillbrett.hindringer):
        print("Kollisjon mellom menneske og hindring")
        
    if any(menneske.hentRektangel().colliderect(spokelse.hentRektangel()) for spokelse in spillbrett.spokelser):
        for spokelse in spillbrett.spokelser:
            spokelse.frys()
            
        menneske.settHastighet(0,0)

   
    for sau in spillbrett.sauer:
        if not menneske.holderSau:
            if menneske.hentRektangel().colliderect(sau.hentRektangel()):
                menneske.holderSau = True
                menneske.sauSomErHoldt = sau
                menneske.settHastighet(3, 3)

    if menneske.holderSau and menneske.sauSomErHoldt.hentPosisjon()[0] < 100:
        menneske.sauSomErHoldt.settPosisjon(0,0)
        spillbrett.leggTilSpillObjekt(Sau())
        spillbrett.leggTilSpillObjekt(Spokelse())
        spillbrett.leggTilSpillObjekt(Hindring())
        poeng += 1
        menneske.settHastighet(5, 5)
        menneske.sauSomErHoldt = None
        menneske.holderSau = False

    for sau in spillbrett.sauer:
        if menneske.holderSau and sau is menneske.sauSomErHoldt:
            sau.settPosisjon(menneske.hentPosisjon()[0]+5, menneske.hentPosisjon()[1])
        sau.tegnSau()


    # Fyller skjermen med en farge
    surface.blit(background_img, (100, 0))
    surface.blit(menneske_side_img, (0, 0))
    surface.blit(sau_side_img, (900, 0))

    # Tegner Menneske
    pg.draw.rect(surface, RED, [menneske.xPosisjon, menneske.yPosisjon, W, H])

    # Tegner spillobjektene
    for spokelse in spillbrett.spokelser:
        spokelse.tegnSpokelse()
        spokelse.endreRetning()

    for hindring in spillbrett.hindringer:
        hindring.tegnHindring()

    for sau in spillbrett.sauer:
        sau.sauKollisjon()
        sau.tegnSau()
        
    spillbrett.antallPoeng()   
      


    # "Flipper" displayet for a vise hva vi har tegnet
    pg.display.flip()

# Avslutter pygame
pg.quit()
sys.exit()