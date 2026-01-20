from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="qooba/bielik-4.5b-v3.0-instruct:Q8_0")

template = """
Jesteś ekspertem w firmie w sprawie pisaniu maili do klinetów.
Nie używaj markdown oraz nie dodawaj stopek do maili.
Nie dodawaj również tematu wiadomości.
Tutaj jest kilka przykładowych wiadomości mail: {Odp}
Tutaj są przykładowe zapytania od klientów : {Pytanie}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

while True:
    question = input("Zadaj pytanie: (q żeby zakończyć) \n")
    if question == "q":
        break
    else:
        email = retriever.invoke(question)  # tu użyj 'question'
        result = chain.invoke({"Pytanie": question, "Odp": email})  # i tu
        print(result)