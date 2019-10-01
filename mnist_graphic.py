import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import model_from_json
import logging

logging.getLogger('tensorflow').disabled = True

pygame.init()

FPS = 70
fpsClock = pygame.time.Clock()

resolution = 28
width = 700
height = 700
sw = width / resolution
sh = height / resolution

DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('A ver que pasa')
font = pygame.font.Font('freesansbold.ttf', 60)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Cell:
    def __init__(self, i, j):
        self.idx = i + j * resolution
        self.x = i * sw
        self.y = j * sh
        self.color = BLACK

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.color, (int(self.x), int(self.y), int(sw), int(sh)))
        pygame.draw.rect(DISPLAYSURF, WHITE, (int(self.x), int(self.y), int(sw), int(sh)), 1)

    def clicked(self):
        if pygame.mouse.get_pressed()[0]:
            coords = pygame.mouse.get_pos()
            if self.x < coords[0] < self.x + sw:
                if self.y < coords[1] < self.y + sh:
                    self.color = WHITE
                    if number[self.idx + 1].color != WHITE:
                        number[self.idx + 1].color = (50, 50, 50)
                    if number[self.idx + resolution].color != WHITE:
                        number[self.idx + resolution].color = (50, 50, 50)
                    if number[self.idx - 1].color != WHITE:
                        number[self.idx - 1].color = (50, 50, 50)
                    if number[self.idx - resolution].color != WHITE:
                        number[self.idx - resolution].color = (50, 50, 50)


number = []
for i in range(resolution):
    for j in range(resolution):
        number.append(Cell(j, i))
array = []


def predictor(array):
    num_mio = np.array(array)
    num_mio = num_mio.reshape((1, 28 * 28))
    num_mio = num_mio.astype('float32') / 255

    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")

    predictions = loaded_model.predict(num_mio[:1])
    # print("\n\nPrediccion: ", np.argmax(predictions[0]))
    return np.argmax(predictions[0])


text = font.render('', True, WHITE)
drawing = True

while True:
    DISPLAYSURF.fill(BLACK)

    for cell in number:
        cell.draw()
        cell.clicked()

    if pygame.key.get_pressed()[K_SPACE]:
        array = []
        for cell in number:
            array.append(int(np.average(cell.color)))
        text = font.render("Creo que es un: " + str(predictor(array)), True, WHITE)
        drawing = False

    if not drawing:
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(text, (320 - text.get_width() // 2, 240 - text.get_height()))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
