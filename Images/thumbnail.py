from PIL import Image, ImageFilter, ImageOps

img = Image.open(r'astro.jpg')
img.show()
print(img.size)
new_img = img.resize((400,400))
new_img.save('thumbnail_astro.jpg')
# to keep the aspect ratio
thumbnail_astro = Image.open('astro.jpg')
thumbnail_astro.thumbnail((400,400))
thumbnail_astro.save('thumbnail2_astro.jpg')
print(thumbnail_astro.size)

