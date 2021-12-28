import numpy as np
import cv2

def whoAmI(name: str):
    print(f'My Self : {name}')
    return f"Hi {name}, starting learning Python"

def createwhiteimage():
    # Lets use two methods
    # 1. Using np.full()
    array_created_using_full = np.full((500,500,3), 255, dtype=np.uint8)
    cv2.imshow("Using np.full", array_created_using_full)
    
    # 2. Using np.zeroes
    array_created_using_zeroes = np.zeros([500, 500,3], dtype=np.uint8)
    array_created_using_zeroes[:,:] = [255, 255, 255]
    cv2.imshow("Using np.zeroes", array_created_using_full)
    cv2.waitKey()
