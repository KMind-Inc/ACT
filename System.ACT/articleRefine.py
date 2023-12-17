# -*- coding: utf-8 -*-
from kOS import nact


def main():
    # 通过LUI，要求用户上传1个文本文件
    file = nact.k_ask_for_file()

    # 数据脱水，将数据降维展开到元空间
    meta_space = nact.k_data_dehydration(file)

    # 评估确认用户输入是否满足要求，若不满足会通过LUI让用户重新按要求输入
    query = nact.k_get_act_query()
    query = nact.k_semantic_confirm_input(query, '修改文章内容', '怎么修改')

    # 语义特征提取：即：标签
    semantic_feature = nact.k_semantic_compute_feature(query)
    # 修改元空间: 关联度计算
    nact.k_meta_space_correlation_compute(meta_space, semantic_feature, file)

    # 搜索 待修改元空间：根据 语义特征 搜索元空间.
    ready_edit_meta_data_list = nact.k_meta_space_search(meta_space, semantic_feature, file)
    # 循环 待修改元空间数据
    for ready_edit_meta_data in ready_edit_meta_data_list:
        # 语义重新理解
        new_content = nact.k_meta_data_semantic_rephrase(ready_edit_meta_data, semantic_feature)
        # 修改元空间
        nact.k_meta_space_update_meta_data(meta_space, ready_edit_meta_data, new_content)

    # 创建结果文件
    new_file = nact.k_file_open(file.file_path+".refined.txt", nact.FileOpenMode.OVERWRITE)

    # 元数据浸泡，将元数据还原为文本数据，并保存在结果文件中
    new_file = nact.k_meta_data_rehydration(meta_space, file, new_file)

    # 通过LUI消息发送结果文件
    nact.k_message_send(new_file)


main()
