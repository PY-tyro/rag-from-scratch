
def load_text(path):
    with open(path, "r",encoding="utf-8") as f:
        return f.read()


print(load_text("data.txt")[:50])
# 预测
# 五十个字:本知识库为服装行业通用客服答疑知识，适配RAG检索问答场景，涵盖消费者咨询高频问题，包含尺码选型、面
# len()等于50
# 第五十个字是汉字

# 实际输出：本知识库为服装行业通用客服答疑知识，适配RAG检索问答场景，涵盖消费者咨询高频问题，包含尺码选型、面