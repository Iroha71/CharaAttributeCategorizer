import os
from typing import List

"""
特定のフォルダ内のファイル名にプレフィックスを付ける
"""
def change_filenames(dir: str, prefix: str):
  files = os.listdir(dir)
  for file in files:
    newname = f"{ prefix }_{ file }"
    newdir = os.path.join(dir, newname)
    olddir = os.path.join(dir, file)
    os.rename(olddir, newdir)
    print(f"{ olddir } to { newdir }")

if __name__ == "__main__":
  print('ファイル名を変更するディレクトリを指定:')
  dir = input()
  print('プレフィックスを入力：')
  prefix = input()
  change_filenames(dir, prefix)
