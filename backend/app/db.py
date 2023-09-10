import logging

import databases
import sqlalchemy
from app.settings import settings

logger = logging.getLogger("__name__")
database = databases.Database(settings.POSTGRES_URL)
engine = sqlalchemy.create_engine(settings.POSTGRES_URL)
metadata = sqlalchemy.MetaData()


async def connect():
    try:
        await database.connect()
        logger.info("Successfully connected to database.")
    except sqlalchemy.exc.SQLAlchemyError as sa_err:
        logger.error(f"SQLAlchemy Error: {sa_err}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred while connecting to database: {e}")
        raise


async def disconnect():
    try:
        await database.disconnect()
        logger.info("Successfully disconnected from database.")
    except sqlalchemy.exc.SQLAlchemyError as sa_err:
        logger.error(f"SQLAlchemy Error: {sa_err}")
        raise
    except Exception as e:
        logger.error(
            f"An unexpected error occurred while disconnecting from database: {e}"
        )
        raise
