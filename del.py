# -*- coding: utf-8 -*-
# @Time : 2023/10/29 12:21
# @Author : LiangBoQing
# @File : del
import os

files = r"""
D:\GitHome\InvoiceLeakDetection\test_data\管球交換請求書\2016.8管球交換ＳＲ請求書\BA20160090 グローバリュービューテラスⅣ (バージョン 1) (自動保存済み).xls
D:\GitHome\InvoiceLeakDetection\test_data\管球交換請求書\2021.11　管球交換SR請求書\アークガーデン亀戸　高圧洗浄 報告書.xlsx
D:\GitHome\InvoiceLeakDetection\test_data\管球交換請求書\2023.2　管球交換SR請求書\ベルエクラ阿佐ヶ谷　102給湯器修理写真（編集版）.xlsx
D:\GitHome\InvoiceLeakDetection\test_data\管球交換請求書\2023.2　管球交換SR請求書\ライオンズマンション西新宿第7　602インターフォン交換写真 .xlsx
D:\GitHome\InvoiceLeakDetection\test_data\管球交換請求書\2023.5　管球交換SR請求書\スピカ小岩ビル　害虫駆除作業（5月時）.xlsx
D:\GitHome\InvoiceLeakDetection\test_data\管球交換請求書\2023.7　管球交換SR請求書\【井上Works】クレア南千住　敷地内ゴミ回収作業.xlsx
""".strip()

for file in files.split('\n'):
  os.remove(file)
