from PIL import Image


def resize(img):
    return img.resize((200, 200))


def crop(img):
    return img.crop((0, 0, 512, 128))  # (left, upper, right, lower)
