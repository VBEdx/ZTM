from PIL import Image, ImageFilter

img = Image.open(r'.\Pokedex\pikachu.jpg')
print(img.format, img.size, img.mode)
print(dir(img))

filteredImg = img.filter(ImageFilter.BLUR)
filteredImg.save(r'.\Pokedex\pikachu_blur.png', 'png')
greyImg = img.convert('L')
greyImg.save(r'.\Pokedex\pikachu_grey.png', 'png')
greyImg.show()
amended_img = greyImg.rotate(90)
amended_img.resize((1024,1024))
amended_img.show()

cropped_img = greyImg.crop((100,100,400, 400))
cropped_img.show()