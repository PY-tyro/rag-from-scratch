"""
    RAG V0：读取文本文件，按固定长度切分段落，不依赖任何框架。

"""
def load_text(path):
    with open(path, "r",encoding="utf-8") as f:
        return f.read()


# 预测
# 五十个字:本知识库为服装行业通用客服答疑知识，适配RAG检索问答场景，涵盖消费者咨询高频问题，包含尺码选型、面
#len(load_text("data.txt"))为600
# 第五十个字是汉字 是一个词里面的



print(load_text("data.txt")[:50])

# 实际输出：前五十个字: 本知识库为服装行业通用客服答疑知识，适配RAG检索问答场景，涵盖消费者咨询高频问题，包含尺码选型、面
#len(load_text("data.txt"))) 实际630
print(len(load_text("data.txt")))


def split_text(text,size):
    chunks = []
    for i in range(0,len(text),size):
        chunks.append(text[i:i+size])
    return chunks
# 预测
# 切2段
# 每段500字符
# 第二段开头的20个字 "色差、漏发等质量问题，本店承担来回运费，"


chunks = split_text(load_text("data.txt"),500)
print(len(chunks))
for chunk in chunks:
    print(len(chunk))
print(chunks[1][:20])

# 实际
# 切了两段
# 第一段500字符 第二段有130个字符
# 第二段的开头是: "差、漏发等质量问题，本店承担来回运费，可"


# data.txt = 630 字符
# 预测
# size=100  预测段数=_7__  预测每段长度= 前六段都是100 最后一段是30
# size=300  预测段数=_3__  预测每段长度= 前两段都是300 最后一段是30
# size=500  预测段数=_2__  预测每段长度= 第一段500 第二段130
chunks1 = split_text(load_text("data.txt"),100)
print(len(chunks1))
for chunk in chunks1:
    print(len(chunk))

chunks2 = split_text(load_text("data.txt"),300)
print(len(chunks2))
for chunk in chunks2:
    print(len(chunk))

# 实测
# 将代码里的size不要写死,再引用load_text函数
# size=100 的结果 打印出来的结果为 7 100 100 100 100 100 100 30
# size=300 的结果 打印出来的结果为 3 300 300  30
# size=500 昨天已经验证了 打印出来的结果为 500 130 预测全部正确



for chunk in chunks2:
    print(chunk[:20])
    print(chunk[-1])




for chunk in chunks1:
    print(repr(chunk[:20]))
    print(repr(chunk[-1]))


# 9 个切点两侧的两个字符
# size=100 → 面， / 5/ / 气、 / 面洗 / 色差 / 过后
# size=300 → 气、 / 过后
# size=500 → 色差



