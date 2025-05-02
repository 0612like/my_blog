from sqlalchemy.future import select
from sqlalchemy import insert, update, delete
from databases import Database
from models import posts # Changed back to absolute
from schemas import PostCreate # Changed back to absolute
from typing import List, Optional

async def get_post(db: Database, post_id: int) -> Optional[dict]:
    query = select(posts).where(posts.c.id == post_id)
    result = await db.fetch_one(query)
    return result._asdict() if result else None

async def get_posts(db: Database, skip: int = 0, limit: int = 100) -> List[dict]:
    query = select(posts).offset(skip).limit(limit).order_by(posts.c.created_at.desc())
    results = await db.fetch_all(query)
    return [result._asdict() for result in results]

async def create_post(db: Database, post: PostCreate) -> dict:
    query = insert(posts).values(title=post.title, content=post.content)
    last_record_id = await db.execute(query)
    # Return a dictionary structure that can be validated by Post schema later
    # Fetching the full record after creation is safer for complex models
    created_post = await get_post(db, last_record_id)
    if created_post:
        return created_post
    else:
        # Fallback or raise error
        return {"id": last_record_id, **post.dict(), "created_at": None, "updated_at": None} # Adjust as needed 