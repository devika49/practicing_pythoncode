from rembg import remove
from PIL import Image

input_path = 'image1.jpg'
output_path = 'outputimg.png'

inp = Image.open(input_path)
output = remove(inp)

output.save(output_path)
Image.open("outputimg.png")