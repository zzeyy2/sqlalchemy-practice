from sqlalchemy.ext.asyncio import async_sessionmaker
from database.exec_files import engine

AsyncSession = async_sessionmaker(bind=engine)