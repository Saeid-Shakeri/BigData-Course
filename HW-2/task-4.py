# Chain-of-Thought (CoT) Prompting

from langchain_core.messages import HumanMessage
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="mistral")

prompt = []

user_input = input("Ask your question: ")

prompt.append(HumanMessage(content=user_input))

response = model.invoke(prompt)

print(response)


# input propmt
"""
Question: I have 2 books. If I buy 3 books every year from this year to ten years from now, how many books will I have after ten years?
Answer: I buy 3 books every year, so in ten years it will be: 10 * 3 = 30. And now I have two books, so 30 + 2 = 32

Now answer this question. There were 9 computers in the server room. Every day, five more computers were installed from Monday to Thursday.
How many computers are there in the server room now?

"""

# output 

"""
To find out how many computers are in the server room now, we need to calculate the number of computers that were added each day and then add that to the initial number of computers.

There are 4 days between Monday and Thursday (from Day 1 to Day 5), so during those 4 days, 4 * 5 = 20 more computers were installed. Adding these newly-installed computers to the initial count of 9 computers, we get:

9 + 20 = 29 computers in the server room now.
"""