from fastapi import Request
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.user import User

from app.utils.jwt import verify_token


def get_current_user(
    request: Request,
    db: Session = Depends(get_db)
):

    token = request.cookies.get(
        "access_token"
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )

    payload = verify_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = db.query(User).filter(
        User.id == int(payload["sub"])
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user