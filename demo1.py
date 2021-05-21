'''
ImageFilter(): 濾鏡
'''

from PIL import Image
from PIL import ImageFilter # 濾鏡(在影像上做處理)

img1 = Image.open("SA.jpeg")
img2 = img1.filter(ImageFilter.BLUR) # 模糊化
img2.save("模糊化.png") # 輸出
img3 = img1.filter(ImageFilter.CONTOUR) # 輪廓(素描)
img3.save("輪廓(素描).png") 
img4 = img1.filter(ImageFilter.DETAIL) # 細節增強(清晰化)
img4.save("細節增強(清晰化).png")
img5 = img1.filter(ImageFilter.EDGE_ENHANCE) # 邊緣增強(顆粒化)
img5.save("邊緣增強(顆粒化).png")
img6 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE) # 邊緣大幅增強(顆粒化)
img6.save("邊緣大幅增強(顆粒化).png")
img7 = img1.filter(ImageFilter.EMBOSS) # 浮雕(石板感)
img7.save("浮雕(石板感).png")
img8 = img1.filter(ImageFilter.FIND_EDGES) # 尋找邊緣(黑底白線:適用電子瑕疵之良率偵測)
img8.save("尋找邊緣(黑底白線:適用電子瑕疵之良率偵測).png")
img9 = img1.filter(ImageFilter.SMOOTH) # 平滑
img9.save("平滑.png")
img10 = img1.filter(ImageFilter.SMOOTH_MORE) # 平滑(增強)
img10.save("平滑(增強).png")
img11 = img1.filter(ImageFilter.SHARPEN) # 銳利化(增強線條明暗對比度)
img11.save("銳利化(增強線條明暗對比度).png")