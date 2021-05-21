'''
嘗試將車牌變清晰。
'''
from PIL import Image
from PIL import ImageFilter

img1 = Image.open("car.jpeg")
img2 = img1.filter(ImageFilter.DETAIL)
img2 = img2.filter(ImageFilter.SHARPEN)
img2 = img2.filter(ImageFilter.DETAIL)
img2 = img2.filter(ImageFilter.SHARPEN)
img2 = img2.filter(ImageFilter.DETAIL)
img3 = img2.filter(ImageFilter.EMBOSS)
img2.save("car2.png")
img3.save("car3_浮雕.png")
