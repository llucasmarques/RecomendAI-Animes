from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger()

def main():
    try:
        logger.info("Starting build the pipeline")

        loader = AnimeDataLoader("data/Animes.csv", "data/Animes_updated.csv")
        updated_csv = loader.process_data()

        logger.info("Data loaded and processed")

        vector_builder = VectorStoreBuilder(updated_csv)
        vector_builder.build_vectostore()

        logger.info("Vector Built")

    except Exception as e:
        logger.error(f"Failed to create Vector {str(e)}")
        raise CustomException("Error during vector build", e)