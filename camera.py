from re import ASCII
from cv2 import VideoCapture, resize, flip
from PIL import Image, ImageEnhance
import pygame, colorsys

ASCII_CHARS = list("$@B%8&WM#*oahkbdpqwmZOXLzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ASCII_CHARS = ASCII_CHARS[::-1]
# ASCII_CHARS = list(".:-=+*#%@")
# ASCII_CHARS = list("█▓▒░ ")[::-1]

cam = VideoCapture(0)
cam.set(3, 180)
cam.set(4, 240)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1150, 750], pygame.RESIZABLE)
#base_font = pygame.font.Font(None, 12)
base_font = pygame.font.SysFont("FreeMono, Monospace", 5)


def asciify(image):
    screen.fill((0, 0, 0))

    img = Image.fromarray(image)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
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
    #print(image_list)
    lines = len(image_list)
    for x in range(lines):
        #text = base_font.render(image_list[x], False, (tuple(x * 255 for x in colorsys.hsv_to_rgb(x/lines, 1, 1))))
        text = base_font.render(image_list[x], False, (255, 0, 255))
        screen.blit(text, (0, 5*x))
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
    cam.release()