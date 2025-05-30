import asyncio
import aiosqlite

DB_FILE = "example.db"  # Change if needed

async def async_fetch_users():
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("All users:")
            for row in users:
                print(row)
            return users

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            users = await cursor.fetchall()
            print("Users older than 40:")
            for row in users:
                print(row)
            return users

async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users(),
    )

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())

