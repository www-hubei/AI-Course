import os
from openai import OpenAI

# 1. 初始化客户端（此处以火山引擎接入 DeepSeek 为例）
# 请将 YOUR_API_KEY 替换为你实际申请的 Key
client = OpenAI(
    api_key = "YOUR_API_KEY", 
    base_url = "https://ark.cn-beijing.volces.com/api/v3"
)

def start_chat():
    print("DeepSeek Chatbot 已启动（输入 'quit' 退出）")
    while True:
        prompt = input("用户: ")
        if prompt.lower() == 'quit':
            break
        
        # 2. 调用模型发送文本问题
        completion = client.chat.completions.create(
            model = "这里填写你的推理点ID", # 从云平台获取的 Endpoint ID
            messages = [{"role": "user", "content": prompt}]
        )
        
        # 3. 获取并打印回复
        print(f"Chatbot: {completion.choices[0].message.content}\n")

if __name__ == "__main__":
    start_chat()
