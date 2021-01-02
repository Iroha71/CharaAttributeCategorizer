from icrawler import crawler
from icrawler.builtin import GoogleImageCrawler
import os

ROOTPATH = './images/'
def crawl_img(savedir: str, keyword: str, num: int):
  """ キーワードで画像クローリングを行う

  Args:
    savedir (str): 画像格納ディレクトリ名
    keyword (str): 検索ワード
    num (int): 取得画像数
  """
  crawler = GoogleImageCrawler(storage={ "root_dir": savedir })
  crawler.crawl(keyword=keyword, max_num=num)

def make_savepath(keyword: str, rootpath: str) -> str:
  """ 保存ディレクトリパスを作成する

  Args:
    keyword (str): 検索ワード
    rootpath (str): ルートパス

  Returns:
    str: 画像を保存するフルパス
  """
  return os.path.join(rootpath, keyword)

def get_rootpath() -> str:
  """ ルートパスを取得する

  Returns:
    str: ルートパス
  """
  return ROOTPATH

if __name__ == "__main__":
    print('検索ワードを入力:')
    keyword = input()
    print('取得数を入力:')
    num = input()

    crawl_img(make_savepath(keyword, ROOTPATH), keyword, int(num))