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


def split_text(text,size=500):
    chunks = []
    for i in range(0,len(text),size):
        chunks.append(text[i:i+size])
    return chunks
# 预测
# 切2段
# 每段500字符
# 第二段开头的20个字 "色差、漏发等质量问题，本店承担来回运费，"


chunks = split_text(load_text("data.txt"))
print(len(chunks))
for chunk in chunks:
    print(len(chunk))
print(chunks[1][:20])

# 实际
# 切了两段
# 第一段500字符 第二段有130个字符
# 第二段的开头是: "差、漏发等质量问题，本店承担来回运费，可"