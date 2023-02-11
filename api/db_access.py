import asyncio
from prisma import Prisma

async def find_embeddings() -> None:
    db = Prisma()
    await db.connect()

    documents = await db.execute_raw(
        '''
        SELECT id, content, embedding::text FROM "Documents";
        '''
    )
    print(documents)

    await db.disconnect()
