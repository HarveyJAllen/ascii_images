from cv2 import VideoCapture, resize, flip
from PIL import Image, ImageEnhance
import pygame, colorsys

#------------------------------------------------------------------------------------#

"""Choose the character set for the image"""
ASCII_CHARS = list("$@B%8&WM#*oahkbdpqwmZOXLzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")[::-1]
#ASCII_CHARS = list(".:-=+*#%@")
#ASCII_CHARS = list("█▓▒░ ")[::-1]

"""Choose the height and width for the frame"""
w_height = 700
w_width = w_height*1.7

"""Choose the character size"""
font_size = 10

"""Choose if you want an RGB image"""
RGB = False

#------------------------------------------------------------------------------------#

divisor = int(256/len(ASCII_CHARS))+1

#Set up pygame window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1150, 750], pygame.RESIZABLE)
base_font = pygame.font.SysFont("Consolas", font_size)

#Set up camera
cam = VideoCapture(0)
cam.set(3, 180)
cam.set(4, 240)

#turn image into an ascii string and print that to the pygame window
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
            resultant_image += (f"{ASCII_CHARS[pixels[y, x]//divisor]}")
    image_list = resultant_image.split("\n")
    lines = len(image_list)
    for x in range(lines):
        if RGB:
            text = base_font.render(image_list[x], False, (tuple(x * 255 for x in colorsys.hsv_to_rgb(x/lines, 1, 1))))
        else:
            text = base_font.render(image_list[x], True, (255, 255, 255))
        screen.blit(text, (0, font_size*x))
    pygame.display.flip()
    clock.tick(60)

def get_frame():
    success, img = cam.read()
    if success:
        img = flip(resize(img, (int(1.7*w_width//font_size), int(1.2*w_height//font_size))), 1)
        asciify(img)

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        get_frame()
    cam.release()