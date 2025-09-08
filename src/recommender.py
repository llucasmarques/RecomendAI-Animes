from langchain.chains import RetrivalQA
from langchain_groq import ChatGroq
from src.prompt import anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key:str, model_name:str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = anime_prompt()

        self.qa_chain = RetrivalQA.from_chain_type(
            llm = self.llm,
            chain_type = "stuff",
            retriever = retriever,
            return_source_documents = True,
            chain_type_kwargs = {"prompt": self.prompt}
        )

    def get_recommendation(self, query:str):
        result = self.qa_chain({"query": query})
        return result['results']