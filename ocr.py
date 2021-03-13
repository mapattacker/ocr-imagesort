import os
import re
from shutil import copyfile

from PIL import Image


def get_image_paths(folder="/home/jake/Desktop/test2/Plant Images"):
    images = []
    for root, _, files in os.walk(folder):
        for i in files:
            i.endswith((".jpg", ".jpeg"))
            images.append(os.path.join(root,i))
    return images


def img_resize(imgpaths, size=0.5):
    """GPU will not have enough memory if not resized"""
    for imgpath in imgpaths:
        im = Image.open(imgpath)
        im = im.resize([int(size * s) for s in im.size])
        im.save(imgpath, "JPEG")


def validation_label(label):
    """check that label lies within a1-f6"""
    match = re.match(r'^[A-F][1-6]$', label)
    if match is not None: 
        match = True
    return match


def validation_results(results, imgpath):
    """validate list of results returned"""
    no_detected = []
    for label in results: 
        if validation_label(label) == True: 
            no_detected.append(1)
        else: 
            no_detected.append(0)
    sum_detected = sum(no_detected)

    if sum_detected == 1:   
        position = no_detected.index(1)
        label = results[position]
    elif sum_detected == 0 or sum_detected > 1 :
        print("no valid label", results)
        image = Image.open(imgpath)
        image.thumbnail([600,800])
        image.show()
        label = input("enter the label: ")
    return label


def copyfiles(img, label, dest_folder, src_folder="/home/jake/Desktop/test2/Plant Images"):
    """copy images to designated folder"""
    dest = os.path.join(dest_folder, label)
    if not os.path.exists(dest):
        os.mkdir(dest)
    src = os.path.join(src_folder, img)
    dest = os.path.join(dest, img)
    copyfile(src, dest)


def check_balance():
    """check all folders have same no. of images after processing"""
    return "something"


def use_easy_ocr(dest_folder):
    """use easyocr: https://github.com/JaidedAI/EasyOCR"""
    import easyocr
    
    reader = easyocr.Reader(['en'], gpu=True)
    
    imgpaths = get_image_paths()
    img_resize(imgpaths, size=0.5)

    for imgpath in imgpaths:
        results = reader.readtext(imgpath, detail=0)
        
        label = validation_results(results, imgpath)
        img = imgpath.split("/")[-1]
        # copy over original rather than resized image folder
        src_folder = imgpath.rsplit("/", 1)[0].replace(" (copy)", "")
        copyfiles(img, label, dest_folder, src_folder)
        print(label, img)


if __name__ == "__main__":
    use_easy_ocr("/home/jake/Desktop/test2/dest")


    
