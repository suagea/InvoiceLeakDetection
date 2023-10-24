# -*- coding: utf-8 -*-
# @Time : 2023/10/14 14:05
# @Author : LiangBoQing
# @File : path_parser
import os
import enum
from typing import Optional, Union


# 使用枚举定义文件类型
class FileType(enum.Enum):
  FILE = "文件"
  DIRECTORY = "文件夹"


# 定义一个类来存储解析出的路径信息
class PathInfo:
  def __init__(
      self,
      path_type: Optional[FileType],
      directory: Optional[str],
      name: Optional[str],
      full_path: str,
      extension: str,
      valid: bool,
      size: int) -> None:
    self.path_type = path_type
    self.directory = directory
    self.name = name
    self.full_path = full_path
    self.extension = extension
    self.valid = valid
    self.size = size

  def __repr__(self) -> str:
    return \
      f'path_type:{self.path_type}\n' \
      f'directory:{self.directory}\n' \
      f'name:{self.name}\n' \
      f'full_path:{self.full_path}\n' \
      f'extension:{self.extension}\n' \
      f'valid:{self.valid}\n' \
      f'size:{self.size}\n' \
      f'{"*" * 55}'


def parse_path_info(path: str) -> PathInfo:
  # 获取文件/文件夹的名字
  directory, name = os.path.split(path)
  # 初始化默认值
  path_type = FileType.DIRECTORY
  size = -1
  valid = True

  # 获取文件扩展名，如果没有扩展名则认为它是一个目录
  extension = os.path.splitext(name)[1]
  if extension:
    path_type = FileType.FILE

  # 如果路径存在，更新 path_type 和 size
  if os.path.exists(path):
    if os.path.isfile(path):
      path_type = FileType.FILE
      size = os.path.getsize(path)
    elif os.path.isdir(path):
      path_type = FileType.DIRECTORY
  else:
    valid = False

  return PathInfo(path_type, directory, name, path, extension, valid, size)


if __name__ == '__main__':
  print(parse_path_info(
    r"D:\GitHome\InvoiceLeakDetection\test_data\BM見積り\駒込スクエア　日常清掃月2回.xlsx"
  ))

  # print(parse_path_info(
  #   r"D:\GitHome\InvoiceLeakDetection\test_data\BM見積り\啊记否.a"
  # ))
