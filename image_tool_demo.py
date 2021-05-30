import sys
from PIL import Image, ImageFilter


'''圖片縮放'''
def resizeImg(imgName):
    try:
        img = Image.open(imgName)
        print("Current size (width, height)", img.size) # size 取得圖檔高度與寬度
        newWidth = int(input("new width:")) # 輸入新的高
        ratio = float(newWidth) / img.size[0] # 取得縮放倍率
        newHight = int(img.size[1] * ratio)  # 將高度乘上縮放倍率
        resizeImg = img.resize((newWidth, newHight), Image.BICUBIC) # 第二傳參為演算法 BICUBIC(二立方體演算法)效果較漂亮
        print("new image size: ", resizeImg.size)
        dotIndex = imgName.index(".") # index(索引值) = (".")所在位置
        newImgName = imgName[:dotIndex] + "_resized" + imgName[dotIndex:] # 新檔名
        resizeImg.save(newImgName)
        print("Resized img is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print("File Not Found Error!")


'''圖片旋轉'''
def rotateImg(imgName):
    try:
        img = Image.open(imgName)
        print("旋轉選項: )")
        print("1: 左右翻轉")
        print("2: 上下翻轉")
        print("3: 旋轉 90 度")
        print("4: 旋轉 180 度")
        print("5: 旋轉 270 度")
        print("6: other")
        op1 = input("您要進行的動作:")
        if op1 == "1":
            newIm = img.transpose(Image.FLIP_LEFT_RIGHT)
            str1 = "_flip_LR"
        elif op1 == "2":
            newIm = img.transpose(Image.FLIP_TOP_BOTTOM)
            str1 = "_flip_TB"
        elif op1 == "3":
            newIm = img.transpose(Image.ROTATE_90)
            str1 = "_rotate_90"
        elif op1 == "4":
            newIm = img.transpose(Image.ROTATE_180)
            str1 = "_rotate_180"
        elif op1 == "5":
            newIm = img.transpose(Image.ROTATE_270)
            str1 = "_rotate_270"
        elif op1 == "6":
            rotateDegree = float(input("Rotate degree: "))
            newIm = img.rotate(rotateDegree)
            str1 = "_rotate_{}".format(rotateDegree)
        
        dotIndex = imgName.index(".") # index(索引值) = (".")所在位置
        newImgName = imgName[:dotIndex] + str1 + imgName[dotIndex:] # 新檔名
        newIm.save(newImgName)
        print("Thumbnail img is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print("File Not Found Error!")


'''圖片縮圖'''
def genThumbnail(imgName):
    try:
        img = Image.open(imgName)
        print("Current size (width, height)", img.size) # size 取得圖檔高度與寬度
        newWidth, newHight = map(int, input("請輸入縮圖尺寸: ").split())
        img.thumbnail((newWidth, newHight)) # thumbnail(寬, 高) 改變為指定尺寸
        dotIndex = imgName.index(".") # index(索引值) = (".")所在位置
        newImgName = imgName[:dotIndex] + "_thumbnail" + imgName[dotIndex:] # 新檔名
        img.save(newImgName)
        print("Rotate img is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print("File Not Found Error!")


'''套用濾鏡'''
def applyFilter(imgName):
    try:
        img = Image.open(imgName)

        print("濾鏡選項: ")
        print("1: 模糊 (BLUR)")
        print("2: 輪廓 (CONTOUR)")
        print("3: 細節增強 (DETAIL)")
        print("4: 邊緣增強 (EDGE_ENHANCE)")
        print("5: 深度邊緣增強 (EDGE_ENHANCE_MORE)")
        print("6: 浮雕效果 (EMBOSS)")
        print("7: 邊緣訊息 (FIND_EDGES)")
        print("8: 平滑效果 (SMOOTH)")
        print("9: 深度平滑效果 (SMOOTH_MORE)")
        print("A: 銳利化效果 (SHARPEN)")
        op1 = input("請選擇要套用的濾鏡: ")

        if op1 == "1":
            newImg = img.filter(ImageFilter.BLUR)
            str1 = "_BLUR"
        elif op1 == "2":
            newImg = img.filter(ImageFilter.CONTOUR)
            str1 = "_CONTOUR"
        elif op1 == "3":
            newImg = img.filter(ImageFilter.DETAIL)
            str1 = "_DETAIL"
        elif op1 == "4":
            newImg = img.filter(ImageFilter.EDGE_ENHANCE)
            str1 = "_EDGE_ENHANCE"
        elif op1 == "5":
            newImg = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            str1 = "_EDGE_ENHANCE_MORE"
        elif op1 == "6":
            newImg = img.filter(ImageFilter.EMBOSS)
            str1 = "_EMBOSS"
        elif op1 == "7":
            newImg = img.filter(ImageFilter.FIND_EDGES)
            str1 = "_FIND_EDGES"
        elif op1 == "8":
            newImg = img.filter(ImageFilter.SMOOTH)
            str1 = "_SMOOTH"
        elif op1 == "9":
            newImg = img.filter(ImageFilter.SMOOTH_MORE)
            str1 = "_SMOOTH_MORE"
        elif op1 == "A":
            newImg = img.filter(ImageFilter.SHARPEN)
            str1 = "_SHARPEN"

        dotIndex = imgName.index(".") # index(索引值) = (".")所在位置
        newImgName = imgName[:dotIndex] + str1 + imgName[dotIndex:] # 新檔名
        newImg.save(newImgName)
        print("Filter img is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print("File Not Found Error!")



def showMenu():
    print("========================")
    print("1: 等比例縮放")
    print("2: 圖片旋轉")
    print("3: 產生縮圖")
    print("4: 套用濾鏡")
    print("0: 結束")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        showMenu()
        op = input("選擇功能: ")
        while True:
            if op == "1":
                resizeImg(sys.argv[1])
            elif op == "2":
                rotateImg(sys.argv[1])
            elif op == "3":
                genThumbnail(sys.argv[1])    
            elif op == "4":
                applyFilter(sys.argv[1])
            elif op == "0":
                print("Thank you for using! Bye~")
                break
            
    else:
        print("Argument error!")