import cv2
import tensorflow as tf
import numpy as np
from moviepy.video.io import ImageSequenceClip
import os

model = tf.keras.models.load_model('U-Net.h5', compile=False)
os.makedir('frames')

def vidGen(vid_path):
    video = cv2.VideoCapture(vid_path)
    success = 1
    fps = video.get(cv2.CAP_PROP_FPS)
    width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    count = 0
    img_files = []
    while success:
        count+=1
        success, image = video.read()
        if success:
            image_shape = image.shape
            image = transform(image)
            img_files.append(segmentFn(image, image_shape, count))

    video.release()
    image_folder = 'frames'
    clip = ImageSequenceClip.ImageSequenceClip(img_files,fps=fps)
    clip.write_videofile('output_video.mp4')



def transform(image):
    image = cv2.resize(image,dsize=(256,256))
    image = image.astype('float32')
    image /= 255.0
    return image

def apply_mask(img_pot, mask_pot):
    img = img_pot*255
    m = mask_pot[:,:,1]
    m = m>=0
    m = m.astype('int32')
    img[:,:,2] = cv2.add(img_pot[:,:,2], mask_pot[:,:,1]*255)
    return img

def segmentFn(image, image_shape, count):
    img_arr = np.array([image])
    mask = model.predict(img_arr)
    seg_img = apply_mask(image, mask[0])
    seg_img = cv2.resize(seg_img, dsize=(image_shape[1],image_shape[0]))
    cv2.imwrite('frames/Frame' + str(count) + '.jpg', seg_img)
    return 'frames/Frame' + str(count) + '.jpg'

if __name__=='__main__':
    vidGen('input_video.mp4')
