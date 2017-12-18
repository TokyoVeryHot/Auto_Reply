#coding:utf-8
import re
import time 
import string 
import xlrd
import BuyItem
import User

import os
import xlrd
from xlwt import *
import BuyItem
from xlutils.copy import copy;  

#########################################
# 测试数据
string = '鞋子 4 裤子3 饰品 6.5'
# send_msg = analysis_data(string)
# print (send_msg[1])


# 创建新的工作文本
def creat_new_work_excel( szFileName , szSheetName ):
  w 	= Workbook()
  ws 	= w.add_sheet(szSheetName)
  ws.write(0, 0, label = '微信名称')
  ws.write(0, 1, label = '大区名称')
  ws.write(0, 2, label = '角色名称')
  ws.write(0, 3, label = '商品信息') 
  ws.write(0, 4, label = '上一条微信信息发送的时间') 
  ws.write(0, 5, label = '系统处理时间')
  w.save(szFileName)


# 获取当前日期的字符串
def get_cur_date():
  return str(time.strftime("%Y-%m-%d", time.localtime()))

# 
def write_excel_test():
  # 1. 获取文件名字
  szCurDate 	= get_cur_date()
  szFileName 	= szCurDate + '.xls'
  szSheetName 	= 'Sheet1'

  # 2. 如果目标文件不存在则创建文件
  if not os.path.isfile(szFileName):
  	creat_new_work_excel(szFileName , szSheetName)

  # 2. 打开Excel文件
  bk        = xlrd.open_workbook(szFileName , formatting_info=True)
  shxrange  = range(bk.nsheets)
  try:
   sh       = bk.sheet_by_name(szSheetName)
  except:
   sh 		= bk.add_sheet(szSheetName)
   print ("no sheet in %s named Sheet1" % file)

  # 3. 获取行数和列数
  nrows     = sh.nrows

  # 4. 在新的一行中写入数据
  newWb		= copy(bk)
  newWs		= newWb.get_sheet(0)
  newWs.write(nrows, 0 , label = str('强迫症的潘胖纸'))
  newWs.write(nrows, 1 , label = str('龙门客栈')) 
  newWs.write(nrows, 2 , label = str('西门吹雪')) 
  newWs.write(nrows, 3 , label = str("{'鞋子': 4, '裤子': 3}")) 
  newWs.write(nrows, 4 , label = str('1513304833')) 
  newWs.write(nrows, 5 , label = str('2017-12-15 10:27:16')) 
  newWb.save(szFileName)


# 主函数
def main():
  # 1. 初始化物品文件
  BuyItem.Init()

  # 2. 初始化玩家列表
  User.Init()

  # 测试
  # strAnswer = friend_talk_to_me('11111231231' , '1')
  # print(strAnswer[1])

  for i in range(1, 11500):
  	write_excel_test()


# 有朋友与自己对话
def friend_talk_to_me( strData ):
  strAnswer = User.friend_talk_to_me(strData)
  return strAnswer




  

if __name__=="__main__":
 main()


