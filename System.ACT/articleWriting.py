# -*- coding: utf-8 -*-
from kOS import nact

def main():
    # 获取用户对话消息
    query = nact.k_get_act_query()

    if not query:
        query = nact.k_semantic_confirm_input(query, '写文章', '文章主题是？')

    prompt = '''
你的角色是一名专业的作家，你的任务是写出内容真实、逻辑准确、文字优美的文章。
请生成一篇文章。

要求：
1.只能来源于以下提供的信息进行写作：%s
2.反思你生成的内容，确保逻辑准确
3.按照下面的步骤进行思考，但请注意这只是你的思考过程，请不要体现在文章的结构上，
4.整理文字排版，在适当的位置加上换行符

限制：
1.字数在350至400个汉字之间。
2.不要在文章中出现“子主题1”“子主题2”等等表述
3.你的回复必须是中文，如果回复内容不是中文，则需要将其翻译为中文
''' % (query)

    result = nact.k_semantic_chat(prompt)
    # 发送结果
    nact.k_message_send(result)
    
main()
