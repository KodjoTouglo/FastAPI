from fastapi import FastAPI, HTTPException
from typing import  List
from pydantic import BaseModel


app = FastAPI(title="News", version="2.0")

class Post(BaseModel):
    titre: str
    texte: str
    categorie: str

post = []
print(post)


@app.get("/")
async def home():
    return "Bienvenu sur votre site d'information"

@app.get("/article/", response_model=List[Post])
async def articles():
    return post

@app.get("/post/{id}")
async def posts(id: int):
    try:
        return post[id]
    except:
        raise HTTPException(status_code=404, detail="Aucun article trouvé")


@app.post("/post/ajouter/")
async def cree_post(posts: Post):
    post.append(posts)
    return post

@app.put("/post/modifier/{id}")
async def modifier(id: int, new_posts: Post):
    try:
        post[id] = new_posts
        return new_posts[id]
    except:
        raise HTTPException(status_code=404, detail="Aucun article trouvé")


@app.delete("/post/supprimer/{id}")
async def supprimer(id: int):
    try:
        article = post[id]
        post.pop(id)
        return article
    except:
        raise HTTPException(status_code=404, detail="Aucun article trouvé")


