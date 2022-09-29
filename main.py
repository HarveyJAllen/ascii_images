from PIL import Image

def asciify(image):
    image = image.load()

ASCII_CHARS = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
for x in range(len(ASCII_CHARS)):
    ASCII_CHARS[x] = ASCII_CHARS[x]*2
ASCII_CHARS = ASCII_CHARS[::-1]
image = Image.open("images/quandale.jpg")
image = image.resize((300, 250))
width, height = image.size
image = image.convert("L")
pixels = image.load()

resultant_image = ""

for x in range(height):
    resultant_image += "\n"
    for y in range(width):
        resultant_image += (f"{ASCII_CHARS[pixels[y, x]//4  ]}")

with open("ascii_img.txt", "w+") as file:
    file.write(resultant_image)

