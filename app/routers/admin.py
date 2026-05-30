from fastapi import APIRouter
from fastapi import Depends

from app.core.admin import (
    admin_required
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/dashboard")
def dashboard(
    admin=Depends(admin_required)
):
    return {
        "message": "Welcome Admin"
    }