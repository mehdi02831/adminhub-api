from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes.users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AdminHub API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "AdminHub API running"}

@app.get("/stats")
def get_stats(db=None):
    from database import SessionLocal
    from models.user import User
    db = SessionLocal()
    total = db.query(User).count()
    active = db.query(User).filter(User.is_active == True).count()
    admins = db.query(User).filter(User.role == "admin").count()
    db.close()
    return {
        "total_users": total,
        "active_users": active,
        "inactive_users": total - active,
        "admins": admins
    }