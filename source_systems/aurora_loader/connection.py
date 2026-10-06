from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    f"postgresql+psycopg2://"
    f"{os.getenv('AURORA_USER')}:"
    f"{os.getenv('AURORA_PASSWORD')}@"
    f"{os.getenv('AURORA_HOST')}:"
    f"{os.getenv('AURORA_PORT')}/"
    f"{os.getenv('AURORA_DB')}"
)