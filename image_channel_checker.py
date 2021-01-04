from typing import Any, List
import torch, torchvision
from torchvision import transforms
from PIL import Image
import os
import cv2
import numpy as np

"""
学習データに使う画像の色チャンネルがRGBか確認する
"""
def get_img_tensor(imgpath: str):
  transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, ), (0.5, ))
  ])
  img = Image.open(imgpath)
  print(transform(img).shape)

def convert_rgba2rgb(imgpaths: List[str]):
  """ RGBA画像をRGBに変換する

  Args:
    imgpaths (List[str]): RGBA画像パスのリスト
  """
  for imgpath in imgpaths:
    img = Image.open(imgpath)
    newimg = img.convert("RGB")
    newimg.save(imgpath)
    print(f"{ imgpath } saved.")

def convert_rgb2rgb_wb(imgpath: str):
  """ RGBに変換する際にホワイトバックで保存する

  Args:
    imgpath (str): RGB変換対象の画像パス
  """
  img = cv2.imread(imgpath, cv2.IMREAD_UNCHANGED)
  savedir = os.path.splitext(imgpath)
  for y in range(img.shape[0]):
    for x in range(img.shape[1]):
      if img.shape[2] <= 3:
        return
      if img[y, x, 3] == 0:
        img[y, x] = [255, 255, 255, 255]
  cv2.imwrite(savedir[0] + '.jpg', img)
  print(savedir[0] + '.jpg')
  # todo: png画像を削除する

def show_rgbafiles(dir: str, imgpaths: List[str]) -> List[str]:
  """ RGBA画像のファイル名を表示する

  Args:
    dir (str): 画像が格納されているディレクトリ
    imgpaths (List[str]): 画像ファイル名リスト
  
  Returns:
    List[str]: RGBA画像パスのリスト
  """
  rgbaimgs = []
  print('-- RGBA files --')
  for imgpath in imgpaths:
    imgpath = os.path.join(dir, imgpath)
    img = Image.open(imgpath)
    if img.mode == 'RGBA':
      print(imgpath)
      rgbaimgs.append(imgpath)

  return rgbaimgs

if __name__ == "__main__":
  print('チェックするディレクトリを入力')
  dir = input()
  if os.path.splitext(dir)[1] != '':
    get_img_tensor(dir)
  else:
    imgs = os.listdir(dir)
    rgbaimgs: List[str] = show_rgbafiles(dir, imgs)
    if len(rgbaimgs) > 0:
      print('RGBA画像をRGBに変換しますか? (y/n)')
      cmd = input()
      if cmd == 'y':
        convert_rgba2rgb(rgbaimgs)
      