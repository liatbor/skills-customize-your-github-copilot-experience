from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI(title="FastAPI — Notes API Starter")

class NoteCreate(BaseModel):
    title: str
    content: Optional[str] = ""

class Note(NoteCreate):
    id: str

# In-memory store
notes = []

@app.get("/items/", response_model=List[Note])
def list_items():
    return notes

@app.get("/items/{item_id}", response_model=Note)
def get_item(item_id: str):
    for n in notes:
        if n["id"] == item_id:
            return n
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/", response_model=Note, status_code=201)
def create_item(payload: NoteCreate):
    new = {"id": str(uuid4()), "title": payload.title, "content": payload.content}
    notes.append(new)
    return new

@app.put("/items/{item_id}", response_model=Note)
def update_item(item_id: str, payload: NoteCreate):
    for n in notes:
        if n["id"] == item_id:
            n["title"] = payload.title
            n["content"] = payload.content
            return n
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: str):
    global notes
    for n in notes:
        if n["id"] == item_id:
            notes = [x for x in notes if x["id"] != item_id]
            return
    raise HTTPException(status_code=404, detail="Item not found")
