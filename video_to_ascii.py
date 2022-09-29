import cv2
from PIL import Image

ASCII_CHARS = list("█$@B%8&WMX▓KDS#*oahkbdpqwmZO0QLCJ▒UYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,░\"^`'. ")
ASCII_CHARS = ASCII_CHARS[::-1]

def asciify(image):
    
    img = Image.fromarray(image)
    width, height = img.size
    image = img.convert("L")
    pixels = image.load()

    resultant_image = ""

    for x in range(height):
        resultant_image += "\n"
        for y in range(width):
            resultant_image += (f"{ASCII_CHARS[pixels[y, x]//3 ]}")
    #os.system("clear")
    # print() : 
    # print(resultant_image)
    return resultant_image

if __name__ == "__main__":
    count = 0
    vidcap = cv2.VideoCapture('sample.mp4')
    success, img = vidcap.read()
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
        img = cv2.flip(cv2.resize(img, (240, 87)), 1)
        print(asciify(img))
        success, image = vidcap.read()
        count += 1
    input()