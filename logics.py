import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from datetime import datetime
import shutil
from werkzeug.datastructures import FileStorage

LABELS = ['ケモミミ', '制服', 'メイド', '巫女']
TMP = './tmp'
MODEL_FILE = './CharaAttributeCategorizer4cpu.pth'
def save_img(file: FileStorage) -> str:
  """ 
  """
  filename = f"{ datetime.now().strftime('%Y%m%d%H%M%S') }.jpg"
  savepath = os.path.join(TMP, filename)
  file.save(savepath)

  return savepath

def build_model(device: str) -> models.ResNet:
  model = models.resnet18(pretrained=True)

  for param in model.parameters():
    param.requires_grad = False

  infeature_count = model.fc.in_features
  model.fc = nn.Linear(infeature_count, len(LABELS))
  model.to(device)
  model.load_state_dict(torch.load(MODEL_FILE))

  return model

def predict_category(imgpath: str, model: models.ResNet, device: str):
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

  return LABELS[category_idx]
