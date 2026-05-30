from fastapi import Depends
from fastapi import HTTPException

from app.core.dependencies import (
    get_current_user
)


def admin_required(
    current_user=Depends(
        get_current_user
    )
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admins only"
        )

    return current_user