from database import users_db
import asyncio

async def test():
    await users_db.add_user(
        12312, '@fafsa', ('Igor', 'Lambadov')
    )
    await users_db.add_user(
        5345, '@vxsd', 'Ivan|Nosov'
    )
    
    
asyncio.run(test())