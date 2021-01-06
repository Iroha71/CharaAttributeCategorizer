from flask import Flask, request, render_template
import torch
from models import FileManager, AttributeCategorizer as AC

app = Flask(__name__, static_folder='tmp')
global model, resource

"""
画像を受け取り、フォルダに格納後に属性推論を行う
"""
@app.route("/", methods=["POST"])
def upload_img():
  file_manager = FileManager()
  imgpath: str = file_manager.save_img(request.files['img'])
  
  ac = AC()
  attribute_name: str = ac.predict(imgpath, model, resource)

  return render_template('result.html', attribute=attribute_name, imgpath=imgpath)

"""
トップページを表示する
"""
@app.route('/', methods=["GET"])
def index():
  return render_template('index.html')

if __name__ == "__main__":
    resource = 'cpu'
    model = AC.build_model(resource)
    app.run(host='0.0.0.0', port=5500, debug=True)
