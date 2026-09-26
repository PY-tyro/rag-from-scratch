"""
    RAG V0：读取文本文件，按固定长度切分段落，不依赖任何框架。

"""
import os

from dotenv import load_dotenv


load_dotenv() # 必须在os.getenv之前不然会拿到None,header变成"Bearer None" 状态码reps.status_code为401
import requests


def load_text(path):
    with open(path, "r",encoding="utf-8") as f:
        return f.read()


def split_text(text,size):
    chunks = []
    for i in range(0,len(text),size):
        chunks.append(text[i:i+size])
    return chunks

def batch_split(text_list,batch_size):
    """
    把文本按固定长度切成若干段
    :return: 返回一个列表
    """
    batchs = []
    for i in range (0, len(text_list), batch_size):
        batch = text_list[i:i+batch_size]
        batchs.append(batch)
    return batchs


def embed(texts):
    """
    将文本列表转换成向量列表
    """
    DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY") # 没加载 "Bearer None" 报401

    batchs = batch_split(texts, 10)
    # 这里的batch_size设置为10 是因为text-embedding-v4这个模型最多一次性只能处理十条数据,超过10条的数据通过batch_split切分

    all_vecs = []

    for batch in batchs:

        url = "https://dashscope.aliyuncs.com/compatible-mode/v1/embeddings"

        headers = {
            "Authorization": f"Bearer {DASHSCOPE_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "text-embedding-v4", # 单次最多处理十条数据
            "input": batch,
            "dimensions": 1024,
            "encoding_format": "float"
        }
        reps = requests.post(url, headers=headers, json=payload)
        print(reps.status_code)

        for i in range(0, len(reps.json()["data"])):
            all_vecs.append(reps.json()["data"][i]["embedding"])
             # 用append按批顺序,不嵌套,保证all_vecs[i]对应texts[i]

    return all_vecs
# -----------------主程序----------------------------------

text = load_text("data.txt")
chunks = split_text(text,300)
for chunk in chunks:
    print(len(chunks),len(chunk),repr(chunk[:20]))



# 预测
# size=100  预测段数=_7__  预测每段长度= 前六段都是100 最后一段是30
# size=300  预测段数=_3__  预测每段长度= 前两段都是300 最后一段是30
# size=500  预测段数=_2__  预测每段长度= 第一段500 第二段130
# 实测
# size=100 的结果 打印出来的结果为 7 100 100 100 100 100 100 30
# size=300 的结果 打印出来的结果为 3 300 300  30
# size=500 昨天已经验证了 打印出来的结果为 500 130 预测全部正确

# 9 个切点两侧的两个字符
# size=100 → 面， / 5/ / 气、 / 面洗 / 色差 / 过后
# size=300 → 气、 / 过后
# size=500 → 色差

if __name__ == "__main__":
    # 将数据传入到embed,经过text-embedding-v4的处理,返回向量,每次最多处理10条数据,超过10条的数据通过batch_split分批处理,最后通过all_vecs收集每个数据的向量,每个向量的维度都是1024
    texts1 = ("你好", "再见", "hello", "goodbye", "今天天气真好", "我喜欢吃苹果", "我不喜欢唱歌",
                      "这个列表是这样子创建的吗?", "python是这个世界上最好的语言", "我喜欢打游戏", "敲代码让人困扰")

    test1 = embed(texts1)
    print(len(test1))  #总共有多少个数据就有多少个向量
    print(len(test1[0])) #第一个数据的向量维度


    text2 = ("你好","再见","拜拜")
    test2 = embed(text2)
    print(len(test2))
    print(len(test2[0]))

    test3 = embed(()) # 传空列表不报错 生成一个空列表
    print(len(test3)) # 长度为0
