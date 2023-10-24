# -*- coding: utf-8 -*-
# @Time : 2023/10/14 13:36
# @Author : LiangBoQing
# @File : features

from xlrd import open_workbook
from xlrd.sheet import Sheet


def excel_coordinates_to_indices(coordinate: str):
  """将Excel坐标（如"C11"）转换为行和列的索引"""

  # 分离字母和数字
  col_str = ''.join(filter(str.isalpha, coordinate))
  row_str = ''.join(filter(str.isdigit, coordinate))

  # 将列字母转换为列索引
  col_index = 0
  for char in col_str:
    col_index = col_index * 26 + (ord(char.upper()) - ord('A')) + 1
  col_index -= 1  # 转换为0-based索引

  # 转换行号为0-based索引
  row_index = int(row_str) - 1

  return row_index, col_index


def get_cell_value_by_coordinate(sheet: Sheet, coordinate: str) -> str:
  row, col = excel_coordinates_to_indices(coordinate)
  return sheet.cell_value(row, col)


def get_bm_name_and_price(file_path):
  work_book = open_workbook(file_path)
  sheet = work_book.sheet_by_name('業者様　見積書(入力用)')
  name = get_cell_value_by_coordinate(sheet, 'C11')
  print(name)


if __name__ == '__main__':
  test_file = r'D:\GitHome\InvoiceLeakDetection\test_data\BM見積り\adatto西新小岩　日常清掃月2回消防点検.xlsx'
  get_bm_name_and_price(test_file)
  pass
