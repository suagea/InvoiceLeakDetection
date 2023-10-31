# -*- coding: utf-8 -*-
# @Time : 2023/10/14 13:41
# @Author : LiangBoQing
# @File : main
from tqdm import tqdm
from Config import BM, REQ_DOC, INV_CP
from Tools.FileIterator import FileIterator
from Tools.path_parser import parse_path_info
from features import get_bm_info, get_req_info, FileTypeError, NotRecordSheetError, get_inv_info

# 读取BM
bm_list = []
for file in tqdm(list(FileIterator(BM, depth=0))):
  pinf = parse_path_info(file)
  if pinf.extension not in ['.xls', '.xlsx']: continue
  name, price = get_bm_info(pinf.full_path)
  bm_list.append({
    'name': name,
    'price': price,
    'path': pinf.full_path,
    'type': 'BM',
  })

req_list = []
# for file in FileIterator(REQ_DOC):
for file in tqdm(list(FileIterator(REQ_DOC))):
  pinf = parse_path_info(file)
  # print(pinf.full_path)
  if (
      pinf.basename.endswith('写真') or
      pinf.basename.startswith('._') or
      pinf.extension not in ['.xls', '.xlsx']
  ): continue
  try:
    name, price = get_req_info(pinf.full_path)
    req_list.append({
      'name': name,
      'price': price,
      'path': pinf.full_path,
      'type': 'REQ',
    })
  except FileTypeError:
    # print('写真', pinf.full_path)
    pass
  except NotRecordSheetError:
    print('无表', pinf.full_path)
  except Exception as e:
    pass
    # print(e, pinf.full_path)

inv_list = []
for file in tqdm(list(FileIterator(INV_CP))):
  pinf = parse_path_info(file)
  # print(pinf.full_path)
  if (
      pinf.basename.startswith('._') or
      pinf.extension not in ['.xls', '.xlsx']
  ): continue
  try:
    name, price = get_inv_info(pinf.full_path)
    inv_list.append({
      'name': name,
      'price': price,
      'path': pinf.full_path,
      'type': 'INV',
    })
  except Exception as e:
    print(e, pinf.full_path)

# %%
bm_count = len(bm_list)
bm_total_price = sum(_['price'] for _ in bm_list)

req_count = len(req_list)
req_total_price = sum(_['price'] for _ in req_list)

inv_count = len(inv_list)
inv_total_price = sum(_['price'] for _ in inv_list)

print(f'分類: 件数 金額')
print(f'bm : ', bm_count, bm_total_price)
print(f'req: ', req_count, req_total_price)
print(f'b+r: ', bm_count + req_count, bm_total_price + inv_total_price)
print(f'inv: ', inv_count, inv_total_price)


# %%
def sort_list(lis):
  lis.sort(key=lambda x: x['name'])


for _ in [
  bm_list,
  req_list,
  inv_list,
]:
  sort_list(_)

# %%

import pandas as pd

# %%
pd.DataFrame(bm_list).to_excel('out/bm.xlsx')
pd.DataFrame(req_list).to_excel('out/req.xlsx')
pd.DataFrame(inv_list).to_excel('out/inv.xlsx')

# %%
b_r_list = bm_list + req_list

# %%
