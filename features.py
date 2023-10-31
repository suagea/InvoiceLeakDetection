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


def get_bm_info(file_path):
  work_book = open_workbook(file_path)
  sheet = work_book.sheet_by_name('業者様　見積書(入力用)')
  name = get_cell_value_by_coordinate(sheet, 'C11')
  price = int(round(float(get_cell_value_by_coordinate(sheet, 'C15')), 0))
  return name, price


class FileTypeError(Exception):
  pass


class NotRecordSheetError(Exception):
  pass


def get_req_info(file_path):
  work_book = open_workbook(file_path)

  # 显示所有表(sheet)名
  all_sheet_names = work_book.sheet_names()
  # print("所有的表(sheet)名：")
  # for sheet_name in all_sheet_names:
  #   print(sheet_name)
  if 'BPS用請求書' in all_sheet_names:
    sheet = work_book.sheet_by_name('BPS用請求書')
    name = get_cell_value_by_coordinate(sheet, 'C11')
    price = int(round(float(get_cell_value_by_coordinate(sheet, 'C14')), 0))

  elif 'ＢＰＳ　見積書-10%' in all_sheet_names:
    sheet = work_book.sheet_by_name('ＢＰＳ　見積書-10%')
    name = get_cell_value_by_coordinate(sheet, 'C11')
    price = int(round(float(get_cell_value_by_coordinate(sheet, 'C15')), 0))

  elif '業者様　見積書(入力用)' in all_sheet_names:
    sheet = work_book.sheet_by_name('業者様　見積書(入力用)')
    name = get_cell_value_by_coordinate(sheet, 'C11')
    price = int(round(float(get_cell_value_by_coordinate(sheet, 'C15')), 0))

  elif '見積書' in all_sheet_names:
    sheet = work_book.sheet_by_name('業者様　見積書(入力用)')
    name = get_cell_value_by_coordinate(sheet, 'C6')
    price = int(round(float(get_cell_value_by_coordinate(sheet, 'D15')), 0))

  else:
    sheet = work_book.sheet_by_name(all_sheet_names[0])
    _ = get_cell_value_by_coordinate(sheet, 'A1')
    if '報告' in _:
      raise FileTypeError()
    else:
      raise NotRecordSheetError()

  return name, price


def get_inv_info(file_path):
  work_book = open_workbook(file_path)
  sheet = work_book.sheet_by_name('請求書(縦)')
  name = get_cell_value_by_coordinate(sheet, 'C11')
  price = int(round(float(get_cell_value_by_coordinate(sheet, 'C10')), 0))
  return name, price


if __name__ == '__main__':
  test_file = r'D:\GitHome\InvoiceLeakDetection\test_data\管球交換請求書\2017.1月管球交換SR請求書\白金コンド.xls'
  print(get_req_info(test_file))
  pass
