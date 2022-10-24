# 仕事スイッチを入れるアプリ
# exeをたたくだけで仕事・作業するための準備をしてくれる

import pyautogui as pag
import os 
import re

def main():
  # main関数
  print("お仕事スイッチON！")
  pag.PAUSE = 0.5
  width, height = pag.size() # 画面のサイズを取得
  # 画角が変わっても多分押せるようにする
  chrome_x = 0.59375
  chrome_y = 0.61
  ym_x = 0.2890625
  ym_y = 0.3518
  print(width)
  print(height)

  shortcut_search('vsc')
  # shortcut_search('chrome')
  # pag.click(x=width*chrome_x, y=height*chrome_y, duration=0.5)
  shortcut_search('youtube music')
  # pag.press('/') # 検索バーを開く
  # pag.write('rock music best', interval=0.5) # 仕事用プレイリスト作りたいな
  # pag.press('enter')
  # pag.click(x=width*ym_x, y=height*ym_y, duration=0.5)
  shortcut_search('gitHub Desktop')
  
  print('頑張れ自分！！')
  
def monitor_length(x):
  # 0 - モニターの長さまでの連続値を取得
  range_lst = []
  for i in range(0, x):
    range_lst.append(i+1)
  return range_lst

def shortcut_search(keyword):
  pag.hotkey('win', 's')
  pag.write(keyword)
  pag.press('enter')

  
if re.compile('__main__').search(__name__):
  main()