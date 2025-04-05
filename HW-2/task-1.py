# Design a conversational customer support chatbot

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="mistral")

system_prompt = SystemMessage(content="تو یک چت بات پشتیبانی مشتری هستی و برای ما کار میکنی. "
                          "حوزه کاری ما فروش دوره ها و فیلم های اموزشی دانشگاهی است."
                          " روند کار این گونه است که پس از پرداخت هزینه دوره توسط مشتری پس از ۲ ساعت آن دوره به پروفایل کاربر اضافه میشود"
                          "اگر اطلاعات کافی نداری، مشتری را به اپراتور انسانی ارجاع بده.")

chat_history = [system_prompt]

print(" برای خروج بنویس خروج.")

while True:
    user_input = input("سوال خود را بپرسید: ")
    if user_input.strip() == "خروج":
        print(" گفتگو پایان یافت.")
        break

    chat_history.append(HumanMessage(content=user_input))

    response = model.invoke(chat_history)

    print("پشتیبان:", response)

    chat_history.append(AIMessage(content=response))
