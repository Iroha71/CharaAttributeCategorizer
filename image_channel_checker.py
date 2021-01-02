import torch, torchvision
from torchvision import transforms
from PIL import Image
import os

"""
学習データに使う画像の色チャンネルがRGBか確認する
"""
def get_img_channel(imgpath: str) -> int:
  transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, ), (0.5, ))
  ])
  img = Image.open(imgpath)
  img = transform(img)

  return img.shape[0]

def get_img_tensor(imgpath: str):
  transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, ), (0.5, ))
  ])
  img = Image.open(imgpath)
  print(transform(img).shape)

if __name__ == "__main__":
  print('チェックするディレクトリを入力')
  dir = input()
  if not os.path.splitext(dir)[1] == '':
    get_img_tensor(dir)
  else:
    imgs = os.listdir(dir)
    for img in imgs:
      color_channel: int = get_img_channel(os.path.join(dir, img))
      if color_channel == 4:
        print(f"{ img } : rgba")
      elif not color_channel == 3:
        print(f"{ img } : color channel is { color_channel }")