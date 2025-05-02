from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from database import database, engine, metadata # Ensure absolute import
from models import posts # Ensure absolute import
from schemas import Post, PostCreate # Ensure absolute import
import crud # Ensure absolute import

# 创建数据库表 (如果尚不存在)
# 注意: 对于生产环境，通常使用 Alembic 等迁移工具管理数据库模式
metadata.create_all(bind=engine)

app = FastAPI(title="Koko 的技术博客 API")

# 配置 CORS
origins = [
    "http://localhost:5173",  # Vite Vue dev server 默认端口
    "http://127.0.0.1:5173",
    # 如果部署到线上，需要添加你的前端域名
    # "https://like0602.xyz",
    # "https://www.like0602.xyz",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -- 数据库连接事件 --
@app.on_event("startup")
async def startup_db_client():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await database.disconnect()

# -- API 路由 --
@app.post("/posts/", response_model=Post, status_code=201)
async def create_new_post(post: PostCreate):
    created_post = await crud.create_post(db=database, post=post)
    # crud.create_post 现在会尝试返回完整的记录
    if not created_post or created_post.get("created_at") is None: # 简单检查
         raise HTTPException(status_code=500, detail="Failed to create or retrieve post")
    return created_post

@app.get("/posts/", response_model=List[Post])
async def read_posts(skip: int = 0, limit: int = 10):
    db_posts = await crud.get_posts(db=database, skip=skip, limit=limit)
    return db_posts

@app.get("/posts/{post_id}", response_model=Post)
async def read_post(post_id: int):
    db_post = await crud.get_post(db=database, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

# 可以添加 PUT, DELETE 等路由... 