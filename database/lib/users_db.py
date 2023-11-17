from database.models import User
from database.exec_files import AsyncSession
import utils

from typing import Union, NoReturn


async def add_user(user_id: int, username: str, full_name: Union[str, tuple]) -> NoReturn:
    """Добавить пользователя в базу данных

    Args:
        user_id (int): Телеграм айди юзера
        username (str): Телеграм юзернєйм
        full_name (Union[str, tuple]): строка типа "Имя|Фамилия" или же масив (Имя, Фамилия)
    """

    async with AsyncSession() as session:
        session.add(
            User(user_id=user_id, username=username, full_name=utils.format_full_name(full_name))
        )
        await session.commit()
