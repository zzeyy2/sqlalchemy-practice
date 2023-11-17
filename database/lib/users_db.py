from database.models import User
from database.exec_files import AsyncSession
from typing import Union


async def add_user(user_id: int, username: str, full_name: Union[str, tuple]):
    """Добавить пользователя в базу данных

    Args:
        user_id (int): Телеграм айди юзера
        username (str): Телеграм юзернєйм
        full_name (Union[str, tuple]): строка типа "Имя|Фамилия" или же масив (Имя, Фамилия)
    """

    if isinstance(full_name, tuple):
        full_name = f"{full_name[0]}|{full_name[1]}"
    async with AsyncSession() as session:
        session.add(
            User(user_id=user_id, username=username, full_name=full_name)
        )
        await session.commit()
