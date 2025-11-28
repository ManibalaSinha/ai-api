from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, search

app = FastAPI(title="AI Document Search (RAG)")

# Allow CORS for frontend
origins = ["http://localhost:3000", "http://localhost:5173"]  # React dev URLs
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include routes
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(search.router, prefix="/search", tags=["Search"])

@app.get("/")
def root():
    return {"message": "AI Document Search API Running!"}
