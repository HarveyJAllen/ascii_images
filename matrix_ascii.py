from re import ASCII
from cv2 import VideoCapture, resize, flip
from PIL import Image, ImageEnhance
import pygame
import random

ASCII_CHARS = list("$@B%8&WM#*oahkbdpqwmZOXLzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ASCII_CHARS = ASCII_CHARS[::-1]
# ASCII_CHARS = list(".:-=+*#%@")
# ASCII_CHARS = list("█▓▒░ ")[::-1]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
#base_font = pygame.font.Font(None, 12)
base_font = pygame.font.SysFont("FreeMono, Monospace", 5)

cam = VideoCapture(0)
cam.set(3, 180)
cam.set(4, 240)

PREV_GRN_PX = []
COUNT = 0

def asciify(image):
    screen.fill((0, 0, 0))

    img = Image.fromarray(image)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)
    width, height = img.size
    image = img.convert("L")
    pixels = image.load()

    resultant_image = ""

    for x in range(height):
        resultant_image += "\n"
        for y in range(width):
            resultant_image += (f"{ASCII_CHARS[pixels[y, x]//4 ]}")
    #os.system("clear")
    image_list = resultant_image.split("\n")
    image_list.remove(image_list[0])
    #print(image_list)
    lines = len(image_list)
    for x in range(lines):
        cols = len(image_list[x])
        for y in range(cols):
            color = random.choices([(255, 255, 255), (0, 255, 0)], weights=(50, 50), k=1)
            if color[0] == (0, 255, 0):
                PREV_GRN_PX.append(y)
            text = base_font.render(image_list[x][y], False, color[0])
            screen.blit(text, (3*y, 5*x))
    pygame.display.flip()
    clock.tick(60)

def get_frame():
    s, img = cam.read()
    if s:
        img = flip(resize(img, (380, 150)), 1)
        #img = flip(resize(img, (380//2, 150//2)), 1)
        #img = flip(resize(img, (240, 180)), 1)
        asciify(img)

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        get_frame()
        COUNT += 1
    cam.release()