import sys

from .auth import get_current_user
sys.path.append("..")
from starlette import status
from starlette.responses import RedirectResponse

from fastapi import Depends, Form, HTTPException, Request, APIRouter
import sys

from .auth import get_current_user
sys.path.append("..")
from starlette import status
from starlette.responses import RedirectResponse

from fastapi import Depends, Form, HTTPException, Request, APIRouter
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not Found"}}
)

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory='templates')

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class ChangePassword(BaseModel):
    username: str
    password: str
    new_password: str

@router.get("/change-password", response_class=HTMLResponse)
async def change_password_page(request: Request):
    user = await  get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse("change-password.html", {"request": request, "user": user})
       
@router.post("/change-password", response_class=HTMLResponse)
async def change_password(request: Request, username: str = Form(...), password: str = Form(...), new_password: str = Form(...), db: Session = Depends(get_db)):
    user = await  get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)
    user_data = db.query(models.Users).filter(models.Users.username == username).first()
    msg = 'Invalid username or password'
    
    if user_data is not None:
        if username == user_data.username and bcrypt_context.verify(password, user_data.hashed_password):
            user_data.hashed_password = bcrypt_context.hash(new_password)
            db.add(user_data)
            db.commit()
            msg='Password Updated'
    return templates.TemplateResponse('change-password.html', {"request": request, "user":user, "msg": msg})
