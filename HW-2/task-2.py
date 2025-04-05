# Create an English-to-Persian translator with a specific style

from langchain_core.messages import HumanMessage
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="mistral")

prompt = []

user_input = input("لغت مورد نظر را وارد کنید: ")

prompt.append(HumanMessage(content=user_input))

response = model.invoke(prompt)

print(response)

# input prompt

"""
من هر کلمه ای که برای ترجمه به تو میدهم را در این فرمت برایم ترجمه کن: کلمه: ترجمه
و بعد در مورد ان کلمه توضیح بده و یک جمله دیگر مثال بزن که آن کلمه در آن استفاده شده باشد
بعنوان مثال :‌ Prominent: برجسته - مشهور ممتاز . توضیح: این کلمه بعنوان یک صفت برای افراد یا وقایع بکار برده میشود 
جمله مثالی : Napoleon is a prominent figure in the history of France. 

"""