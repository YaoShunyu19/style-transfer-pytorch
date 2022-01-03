import cv2 as cv
import os
from StyleTransfer import *
from PIL import Image


"""
将视频拆分成图像进行风格迁移，再合并成视频
"""

videos_path = 'E:/Entertainment/Video/buywatermelon.mp4'  # 原始视频路径
frames_origin_path = 'E:/Entertainment/Image/Origin/'  # 原始拆分图像路径

frames_processed_dir = 'E:/Entertainment/Image/Processed/'  # 帧存放路径
result_video_path = 'E:/Entertainment/Video/result.mp4'  # 合成视频存放的路径


def video2frame(videos_path, frames_save_path, time_interval):
    """
    将视频拆分成图像
    :param videos_path: 视频的存放路径
    :param frames_save_path: 视频切分成帧之后图片的保存路径
    :param time_interval: 保存间隔
    :return: 无
    """
    video = cv.VideoCapture(videos_path)
    success, image = video.read()
    count = 0
    index = 0
    while success:
        success, image = video.read()
        count += 1
        if count % time_interval == 0:
            index += 1
            cv.imwrite(frames_save_path + '/%d.jpg' % index, image)
            print(frames_save_path + '/%d.jpg' % index)
    print('Finished.')


def frame2video(frames_processed_dir, result_video_path, fps):
    """
    将图像合并成视频
    :param frames_processed_dir: 图像保存路径
    :param result_video_path: 视频保存路径
    :param fps: 合成视频帧率
    :return: 无
    """
    im_list = os.listdir(frames_processed_dir)
    im_list.sort(key=lambda x: int(x.split('.')[0]))
    img = Image.open(os.path.join(frames_processed_dir, im_list[0]))
    img_size = img.size  # 获得图片分辨率，frames_processed_dir文件夹下的图片分辨率需要一致

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    videoWriter = cv.VideoWriter(result_video_path, fourcc, fps, img_size)
    # count = 1
    for i in im_list:
        im_name = os.path.join(frames_processed_dir + i)
        print(im_name + '.jpg')
        frame = cv.imdecode(np.fromfile(im_name, dtype=np.uint8), -1)
        videoWriter.write(frame)
    videoWriter.release()
    print('Finished.')


def main():
    time_interval = 2  # 拆分帧间隔
    video2frame(videos_path, frames_origin_path, time_interval)

    style_img_path = '../img/style_星月夜.jpg'
    style_img = Image.open(style_img_path)  # 风格图像

    num_jpg = len(os.listdir(frames_origin_path))  # 原始图像的个数

    for i in range(num_jpg):
        content_img_path = frames_origin_path + str(i + 1) + '.jpg'
        print(str(i + 1) + '.jpg')
        content_img = Image.open(content_img_path)
        StyleTransfer(content_img, style_img, save_path=frames_processed_dir, file_name=str(i + 1) + '.jpg', epochs_num=300)


if __name__ == '__main__':
    main()
    frame2video(frames_processed_dir, result_video_path, 10.8)
