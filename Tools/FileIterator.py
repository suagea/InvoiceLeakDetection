# -*- coding: utf-8 -*-
# @Time : 2023/10/14 13:53
# @Author : LiangBoQing
# @File : FileIterator
import os


class FileIterator:
  def __init__(self, start_directory, depth=-1):
    self.start_directory = start_directory
    self.depth = depth

  def __iter__(self):
    return self._iterate_directory(self.start_directory, 0)

  def _iterate_directory(self, dirpath, current_depth):
    if self.depth != -1 and current_depth > self.depth:
      return
    for root, dirs, files in os.walk(dirpath):
      # 当前深度的文件
      for filename in files:
        yield os.path.join(root, filename)

      # 遍历子目录
      for subdir in dirs:
        subdir_path = os.path.join(root, subdir)
        yield from self._iterate_directory(subdir_path, current_depth + 1)
      # 在这里退出，以防止os.walk()继续遍历子目录
      break

    # 使用示例:


if __name__ == '__main__':
  start_directory = r'D:\\'
  for filepath in FileIterator(start_directory, depth=2):
    print(filepath)
