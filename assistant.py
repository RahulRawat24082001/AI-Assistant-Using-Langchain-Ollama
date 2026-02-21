from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


#we specify the model we want to use, in this case, we are using the llama3 model with 8b parameters.
llm = Ollama(model="llama3:8b")

# This tool will run a web search for free.
search = DuckDuckGoSearchRun()

# This is the Prompt template
prompt = ChatPromptTemplate.from_template("""
Your name is **Uknian**,A helpful AI Assistant from **India**.
Answer all questions of the user in their language (For example hindi,english or any other language they speak).
answer the user questions on the following search results.
If search results are empty or do not contain the answer, Say 'I could not find any information on that topic'.
Search Results: {context}
User Question: {user_question}
""")
# RAG Chain:
chain = ( RunnablePassthrough.assign(
    context = lambda x: search.run(x["user_question"])
)
| prompt| llm
)

# Below is the chain:

"""
Input:
{"question": "..."}
   ↓
RunnablePassthrough.assign
   ↓
{"question": "...", "context": "...search results..."}
   ↓
ChatPromptTemplate
   ↓
Formatted prompt text
   ↓
LLM
   ↓
Final answer
"""


print("🤖 Hello! I'm a Uknian real-time AI assistant. What's new?")
while True: 
    try:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye! See you next time.")
            break
        print("🤖 Thinking...")

        # This one line runs whole process.
        response = chain.invoke({"user_question":user_query})

        print("🤖 Uknian:", response)

    except Exception as e:
        print(f"🚨 Error: {e}")
        continue
