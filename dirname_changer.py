import os
from image_crawler import get_rootpath
from typing import List

"""
特定のディレクトリ配下のフォルダ名を連番に変更する
"""
def rename_dirname():
  dirs = os.listdir(get_rootpath())
  for idx, dir in enumerate(dirs):
    origindir = os.path.join(get_rootpath(), dir)
    newdir = os.path.join(get_rootpath(), str(idx))
    os.rename(origindir, newdir)
    print(f"{ dir } to { idx }")
    print(get_progress(dirs, idx + 1))

def get_progress(dirs: List[str], cur_idx: int) -> float:
  return (float(cur_idx) / len(dirs)) * 100.0

if __name__ == "__main__":
  rename_dirname()
