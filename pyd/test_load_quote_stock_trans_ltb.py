﻿
# -*- coding: utf-8 -*-

# 函数说明
#
# 函数：result = LoadQuote(file_path, file_head, file_code, quote_list, list_info, dict_data)
#
# 功能: 从落地转储文件导入LTB实时逐笔成交行情数据。
#
# 入参：file_path  <- 落地转储文件路径。
#　 　　file_head  <- 落地转储文件头部字节长度。
#　 　　file_code  <- 落地转储文件数据压缩格式，未压缩则置空字符串。
#　 　　quote_list <- 需要筛选的合约列表，英文逗号分隔，为空表示全市场，注意字母大小写。
#
# 返回：result     -> 函数调用执行结果，失败返回：-1，成功返回：>= 0。
#　 　　list_info  -> 函数调用执行信息。
#　 　　dict_data  -> LTB实时逐笔成交行情数据。
#
# 数据："Code", "Name", "Type", "Market", "Index", "Price", "Volume", "Turnover", 
#　 　　"TradeGroupID", "BuyIndex", "SellIndex", "OrderKind", "FunctionCode", 
#　 　　"TransTime", "LocalTime", "LocalIndex"。
#　 　　具体行情数据格式请参考相关业务文档。

import LoadQuoteStockTransLTB

file_head = 32
file_code = "lzma"
file_path = "C:\\Users\\xrd\\Desktop\\20160622.tr.lzma"

list_info = []
dict_data = {}

#result = LoadQuoteStockTransLTB.LoadQuote(file_path, file_head, file_code, "", list_info, dict_data) # 注意内存哦
result = LoadQuoteStockTransLTB.LoadQuote(file_path, file_head, file_code, "600000, 000001", list_info, dict_data)
print(result, len(list_info))
if result >= 0:
    for i in range(result):
        print(dict_data["Code"][i], dict_data["Name"][i], dict_data["Type"][i], dict_data["Market"][i], \
              dict_data["Index"][i], dict_data["Price"][i], dict_data["Volume"][i], dict_data["Turnover"][i], \
              dict_data["TradeGroupID"][i], dict_data["BuyIndex"][i], dict_data["SellIndex"][i], dict_data["OrderKind"][i], dict_data["FunctionCode"][i], \
              dict_data["TransTime"][i], dict_data["LocalTime"][i], dict_data["LocalIndex"][i])
    for i in range(len(list_info)):
        print("成功：", list_info[i])
else:
    for i in range(len(list_info)):
        print("失败：", list_info[i])
