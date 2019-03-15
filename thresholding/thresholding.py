import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import os



class Thresholding:
    def __init__(self):
       
        
        return
    def abs_sobel_thresh(self, img, orient='x', thresh_min=0, thresh_max=255):
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Apply x or y gradient with the OpenCV Sobel() function
        # and take the absolute value
        if orient == 'x':
            abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 1, 0))
        if orient == 'y':
            abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 0, 1))
        # Rescale back to 8 bit integer
        scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))
        # Create a copy and apply the threshold
        binary_output = np.zeros_like(scaled_sobel)
        # Here I'm using inclusive (>=, <=) thresholds, but exclusive is ok too
        binary_output[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 1
    
        # Return the result
        return binary_output
    

    def run(self):
        # Load our image
        img = cv2.imread('../test_images/test1.jpg')
        binary_output = self.abs_sobel_thresh(img, 'x', 140, 255)
        cv2.imwrite('../test_images/test1_binary.jpg', binary_output)
       
  

        plt.imshow(binary_output, cmap="gray")
        plt.show()
        
        return
    
  

    
if __name__ == "__main__":   
    obj= Thresholding()
    obj.run()