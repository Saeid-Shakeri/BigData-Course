# Hallucination Mitigation

from langchain_core.messages import HumanMessage
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="mistral")

prompt = []

user_input = input("Ask your question: ")

prompt.append(HumanMessage(content=user_input))

response = model.invoke(prompt)

print(response)

# input prompt 

""" Who won the Russia-Ukraine war? """
# output: 

""" 
There has never been a war between Russia and Ukraine as nations. Russia and Ukraine are independent countries, and any conflicts that have occurred (such as the Crimean War or the Donbass conflict) do not equate to a war between Russia and Ukraine as nations. It is important to note that these events are complex with political, economic, and social implications that extend beyond military conflict.
Always aim for accurate information when discussing sensitive topics like this one.
"""

# input prompt 

""" Who won the Russia-Ukraine war? Only answer if you are 100% certain """

# output: 

""" 
I am a model and do not have the ability to gain or retain knowledge about real-world events in real time.
However, as of my last training, the conflict between Russia and Ukraine is an ongoing territorial conflict that started in 2014, and there has been no declared winner yet. The Russian Federation annexed Crimea in 2014, which Ukraine does not recognize, while a conflict continues in Eastern Ukraine involving separatist regions supported by Russia.
It's important to note that these are sensitive geopolitical issues, and it's crucial to stay informed through reliable sources for accurate information.
"""

