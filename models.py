import os
from datetime import date, datetime
from werkzeug.datastructures import FileStorage
import torch, torchvision
from torchvision import models, transforms
import torch.nn as nn
from PIL import Image

class FileManager():
  def save_img(self, imgfile: FileStorage) -> str:
    """ 画像を一時ファイルに保存する

    Args:
      imgfile (FileStorage): 保存する画像

    Returns:
      str: 保存した画像のフルパス
    """
    TMP = './tmp'
    filename = f"{ datetime.now().strftime('%Y%m%d%H%M%S') }.jpg"
    savepath = os.path.join(TMP, filename)
    imgfile.save(savepath)

    return savepath

class AttributeCategorizer():
  MODEL_FILE = './CharaAttributeCategorizer4cpu.pth'
  LABELS = ['ケモミミ', '制服', 'メイド', '巫女']

  @classmethod
  def build_model(cls, device: str) -> models.ResNet:
    """ 推論モデルを構築する

    Args:
      device (str): 推論に利用するリソース名

    Returns:
      models.ResNet: 構築済みモデル
    """
    model = models.resnet18(pretrained=True)

    for param in model.parameters():
      param.requires_grad = False

    infeature_count = model.fc.in_features
    model.fc = nn.Linear(infeature_count, len(cls.LABELS))
    model.to(device)
    model.load_state_dict(torch.load(cls.MODEL_FILE))

    return model

  def predict(self, imgpath: str, model: models.ResNet, device: str) -> str:
    """ イラストの属性を推論する

    Args:
      imgpath (str): 推論対象画像パス
      model (models.ResNet): 推論モデル
      device (str): 推論に利用するリソース名

    Returns:
      str: 属性名
    """
    model.eval()
    tsfm = transforms.Compose([
      transforms.Resize((224, 224)),
      transforms.ToTensor(),
      transforms.Normalize((0.5, ), (0.5, ))
    ])
    img = Image.open(imgpath)
    img = tsfm(img)
    img = img.unsqueeze(0)
    results = model(img.to(device))
    category_idx = results.argmax().numpy()

    return self.LABELS[category_idx]
