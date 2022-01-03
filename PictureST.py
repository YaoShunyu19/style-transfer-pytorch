from StyleTransfer import *
from PIL import Image


"""
图像风格迁移
"""


if __name__ == '__main__':
    content_img_path = '../img/cy头像.jpg'
    style_img_path = 'E:/Entertainment/Image/cystyle2.jpg'
    content_img = Image.open(content_img_path)
    style_img = Image.open(style_img_path)
    StyleTransfer(content_img, style_img, save_path='E:\\Entertainment\\image\\', file_name='cy2.jpg')
