from PIL import Image
i = Image.open('test.jpg')
filter = ImageFilter.GaussianBlur(15.0)
img = i.filter(filter)
img2 = img.convert('L')

img2.save('result.jpg')