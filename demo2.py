'''
繪圖。
'''
from PIL import Image, ImageDraw

# 新增一個物件(畫布) Image.new("模式", (尺寸, ), "#RGB色號")
newImg = Image.new("RGBA", (1000, 1000), "#000000")
drawObj = ImageDraw.Draw(newImg) # 繪畫物件(可在newImg繪製)
color_list = ["White", "Red", "Yellow", "Green", "Blue", "Purple"]
color_count = 0
for i in range(200, 801, 5):
    for j in range(200, 801, 5):
        if color_count > len(color_list) - 1:
            color_count = 0
        color = color_list[color_count]
        drawObj.point([i, j], fill = color) # 畫點
        color_count += 1

drawObj.line ([(198, 198), (802, 198), (802, 802), (198, 802), (198, 198)], "White") # 畫線 內框
drawObj.line ([(10, 10), (990, 10), (990, 990), (10, 990), (10, 10)], "Purple") # 畫線 外框

# 上左
for x in range(500, 0, -20):
    drawObj.line([(x, 0), (0, 500 - x)], "Red")
# 上右
for x in range(500, 1000, 20):
    drawObj.line([(x, 0), (1000, x - 500)], "Yellow")
# 下左
for y in range(500, 1000, 20):
    drawObj.line([(0, y), (y - 500, 1000)], "Purple")
# 下右
decreaseValue = 500
for y in range(500, 0, -20):
    drawObj.line([(1000 , 1000 - y), (y + 500, 1000)], "Green")
newImg.save("newImg.png")