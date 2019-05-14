# -* - coding: UTF-8 -* -
from PIL import Image
import tesserocr, requests
import random
import uuid
import os

img_url = 'https://ebao.sinosig.com/travel/page/welcome/AuthCode?times='
img_path = '/Users/duhao/tmp/img/'

#图片下载
def img_download():
    url = img_url + str(random.uniform(1, 10))
    response = requests.get(url)
    path = img_path + str(uuid.uuid4())+".jpg"
    with open(path, 'wb') as f:
        f.write(response.content)

#查询图片
def img_query(path):
    img = Image.open(path)
    return img

#图片转灰度处理
def img_grayscale_deal(image):
    image = image.convert('L')
    return image

#图片二值化处理
def img_thresholding(image):
    threshold = 160
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    return image

#图片识别
def img_tesserocr_crack(image):
    result = tesserocr.image_to_text(image)
    return result

#初始化调用
if __name__ == '__main__':
    #下载图片
    '''
    for i in range(0,10):
        img_download()
    '''
    #获得图片路径
    for file in os.listdir(img_path):
        if file.find('.jpg') >= 0:
            file_path = os.path.join(img_path, file)
            image = img_query(file_path)
            img1 = img_grayscale_deal(image)
            img2 = img_thresholding(img1)
            data = img_tesserocr_crack(img2)
            print(file, data)