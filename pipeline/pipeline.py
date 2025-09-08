from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimePipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info("Initializing Pipeline")

            vector_build = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            
            retriever = vector_build.load_vectorstore().as_retriever()

            self.recommender = AnimeRecommender(retriever, GROQ_API_KEY, MODEL_NAME)

            logger.info("Pipeline Initialized")

        except Exception as e:
            logger.error(f"Failed to inicialize pipeline {str(e)}")
            raise CustomException("Error during pipeline", e)

    
    def recommend(self, query:str) -> str:
        try:
            logger.info(f"Query: {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated.")
            return recommendation

        except Exception as e:
            logger.error(f"Failed to recommend {str(e)}")
            raise CustomException("Error during recommendation", e)