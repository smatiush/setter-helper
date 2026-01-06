import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables
load_dotenv()

# PostgreSQL connection
DATABASE_URL = os.getenv("DB_HOST")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

logger = logging.getLogger(__name__)


def get_session_local():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
        yield db
    except Exception:
        logger.warning("Database not ready; OHLCV data is still ingesting.")
        raise
    finally:
        db.close()
