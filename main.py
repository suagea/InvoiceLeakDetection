# -*- coding: utf-8 -*-
# @Time : 2023/10/14 13:41
# @Author : LiangBoQing
# @File : main
from Config import BM
from Tools.FileIterator import FileIterator
from Tools.path_parser import parse_path_info

# 读取BM
for file in FileIterator(BM, depth=0):
  pinf = parse_path_info(file)
