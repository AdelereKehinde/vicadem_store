from sqlalchemy.orm import Session

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from app.schemas.user import UserCreate
from app.schemas.user import UserLogin

from app.models.user import User

from app.core.database import get_db

from app.core.security import hash_password
from app.core.security import verify_password

from app.utils.jwt import create_access_token
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/health")
def auth_health():
    return {
        "message": "Auth working"
    }

@router.post("/register")
def register(
    payload: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == payload.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user = User(
        fullname=payload.fullname,
        email=payload.email,
        hashed_password=hash_password(
            payload.password
        )
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return {
        "message": "Registration successful"
    }

@router.post("/login")
def login(
    payload: UserLogin,
    response: Response,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == payload.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        payload.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": str(user.id),
            "role": user.role
        }
    )

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax"
    )

    return {
        "message": "Login successful"
    }   

@router.get("/me")
def me(
    current_user=Depends(
        get_current_user
    )
):
    return current_user

@router.post("/logout")
def logout(
    response: Response
):

    response.delete_cookie(
        "access_token"
    )

    return {
        "message": "Logged out"
    } 