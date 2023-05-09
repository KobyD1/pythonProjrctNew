import os
import shutil
import time

import PIL
from matplotlib import image
from selenium import webdriver
from PIL import Image, ImageChops

# to install package Pillow  and matplotlib before
class ImagesUtils():

    def __init__(self,driver,is_learning):
        self.driver = driver
        self.is_learning = is_learning


    def get_screen_capture(self,path):
        print ('get screen capture at ',path)
        self.driver.save_screenshot(path)



    def crop_image(self,rectangle,path_save,path_under_test):
        im = Image.open(path_under_test)
        cropped = im.crop(rectangle)
        cropped.save(path_save)

    #     basic method to compare between 2 images

    def compare_images(self ,path_file_under_test,path_ref,path_res):
        im1 = Image.open(path_file_under_test)
        im2 = Image.open(path_ref)
        assert im1.size == im2.size , 'Mismatch found into image files sizes '
        translucent = Image.new("RGBA", im1.size, (255, 0, 0, 127))
        mask = ImageChops.difference(im1, im2).convert("L")
        is_equals = open(path_file_under_test, "rb").read() == open(path_ref,"rb").read()

        im2.paste(translucent, (0, 0), mask)
        im2.save(path_res)
        return is_equals


    def compare_image_rectangle (self, path_file_ref, rectangle, name):

        properties = self.prapare(name,path_file_ref)
        Image.open(properties.get('path_res'))
        box=(rectangle['x'],rectangle['y'],rectangle['x+width'],rectangle['y+highet'])
        self.get_screen_capture(properties.get('path_screenshot'))
        shutil.copyfile(properties.get('path_screenshot'),properties.get('path_res'))
        self.crop_image(box, properties.get('path_crop'), properties.get('path_screenshot'))
        if (self.is_learning):
            path_learning = properties.get('path_root')+'_Learning//_Learning_name.png'
            self.crop_image(box, path_learning, properties.get('path_screenshot'))

        is_equals = self.compare_images(properties.get('path_crop'),path_file_ref,properties.get('path_res'))
        return is_equals

    def compare_image_coardinations (self, path_file_ref, coardinations, name):
        im = Image.open(path_file_ref)
        width = im.size[0]
        highet = im.size[1]
        rectangle = {
            'x' : coardinations ['x'],
            'y' : coardinations['y'],
            'x+width': coardinations ['x'] + width,
            'y+highet': coardinations['y'] + highet

            }

        is_equals = self.compare_image_rectangle(path_file_ref,rectangle,name)
        return is_equals

    def prapare(self,prefix,path_file_ref):
        ms = str(round(time.time() * 1000.0))
        ms = ms[6:]
        path_dir = "..//Images//Results//" + prefix + ms
        os.makedirs(path_dir, exist_ok=True)
        assert os.path.exists(path_file_ref), 'Ref. file not found as expected at '+path_file_ref

        properties = {
            'path_root' :  "..//Images//Results//" + prefix + ms,
            'path_crop' : path_dir+"//cropped.png",
            'path_res': path_dir + "//result.png",
            'path_screenshot' : path_dir+"//screenshot.png"
        }
        self.get_screen_capture(properties.get('path_res'))
        shutil.copyfile(path_file_ref, path_dir+"//ref.png")

        return properties

    def close_file(self,path):
        try:
            file = open(path, "r+")
        finally:
            file.close()