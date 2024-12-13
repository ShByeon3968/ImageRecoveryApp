import cv2
import numpy as np
from ISR.models import RRDN
from deoldify.visualize import get_image_colorizer

def preprocess_image(image_path:str)-> np.ndarray:
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (512,512)) ## 모델 입력 크기에 맞게 조정
    return img

def super_resolve(image):
    model = RRDN(weights='gans')
    sr_img = model.predict(image)
    return sr_img

def colorize_image(image_path):
    colorizer = get_image_colorizer(artistic=True)
    result = colorizer.get_transformed_image(image_path)
    return result