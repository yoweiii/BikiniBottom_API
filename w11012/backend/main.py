from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="簡單貼文 API")

# ✅ 允許跨域 (解決前端無法連線問題)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 測試時允許所有來源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 模擬資料庫
posts = {
    1: {"content": "派大星：晚餐要吃什麼？🍔", "likes": 0, "comments": []},
    2: {"content": "章魚哥：安靜一點好嗎…🎶", "likes": 0, "comments": []},
    3: {"content": "蟹老闆：錢才是最重要的 💰", "likes": 0, "comments": []},
    4: {"content": "海綿寶寶：拉拉拉~ 🪼", "likes": 0, "comments": []},
}

# 留言模型
class Comment(BaseModel):
    text: str

# 取得所有貼文
@app.get("/posts")
def get_posts():
    return posts

# 貼文按讚
@app.post("/posts/{post_id}/like")
def like_post(post_id: int):
    if post_id in posts:
        posts[post_id]["likes"] += 1
        return {"message": "成功按讚！", "data": posts[post_id]}
    return {"error": "找不到貼文"}

# 新增留言
@app.post("/posts/{post_id}/comment")
def comment_post(post_id: int, comment: Comment):
    if post_id in posts:
        posts[post_id]["comments"].append(comment.text)
        return {"message": "留言成功！", "data": posts[post_id]}
    return {"error": "找不到貼文"}

