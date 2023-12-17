# -*- coding: utf-8 -*-
from kOS import nact
from datetime import datetime

def main():
    # 获取用户对话消息
    query = nact.k_get_act_query()

    if not query:
        query = nact.k_semantic_confirm_input(query, '记录',  '记录什么？' )

    # 获取当天时间作为文件名
    filename = '/备忘录/' + datetime.now().strftime('%Y-%m-%d') + '.txt'
    # 创建一个文件
    file = nact.k_file_open(filename, nact.FileOpenMode.APPEND, mount_type=nact.FileMountType.MATERIAL)
    # 存储需要记录的内容
    nact.k_file_append(file, query)

main()
