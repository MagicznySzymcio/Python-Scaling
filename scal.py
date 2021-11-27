from PIL import Image
import os
import argparse


def parser_config():
    parser = argparse.ArgumentParser(description='Python command line program for scalling all images in folder to specific size.')
    parser.add_argument('path', type=str, help='Path to image folder')
    parser.add_argument('--size', type=int, default=512, help='Target size of image (default: 512)')
    args = parser.parse_args()

    return args.path, args.size


def resize(img_url, size):
    img = Image.open(img_url)

    if (img.size[0] != size) or (img.size[1] != size):
        if img.size[0] > img.size[1]:
            ratio = (size / float(img.size[0]))
            height = int((float(img.size[1]) * float(ratio)))
            img = img.resize((size, height), Image.ANTIALIAS)
        else:
            ratio = (size / float(img.size[1]))
            width = int((float(img.size[0]) * float(ratio)))
            img = img.resize((width, size), Image.ANTIALIAS)

    img.save(img_url)


def file_loop(path, size):
    files = os.listdir(path)

    for file in files:
        f_name = file.format()
        if f_name.lower().endswith('.jpg') or f_name.lower().endswith('.png'):
            f_path = (path + '\\' + f_name).replace("\\", "/")
            resize(f_path, size)


if __name__ == '__main__':
    path, size = parser_config()
    file_loop(path, size)
