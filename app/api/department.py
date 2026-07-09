from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.core.deps import get_current_user
from app.core.permissions import require_admin

from app.models.user import User

from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse,
)

from app.services.department import (
    create_department_service,
    get_department_service,
    list_department_service,
    update_department_service,
    delete_department_service,
)


router = APIRouter(
    prefix="/departments",
    tags=["Department"],
)


# ==========================
# 创建部门
# 管理员权限
# ==========================
@router.post(
    "",
    response_model=DepartmentResponse,
)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    require_admin(current_user)

    return create_department_service(
        db,
        department,
    )


# ==========================
# 查询单个部门
# 登录用户即可
# ==========================
@router.get(
    "/{department_id}",
    response_model=DepartmentResponse,
)
def get_department(
    department_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_department_service(
        db,
        department_id,
    )


# ==========================
# 查询部门列表
# 登录用户即可
# ==========================
@router.get(
    "",
    response_model=list[DepartmentResponse],
)
def list_departments_api(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return list_department_service(db)



# ==========================
# 更新部门
# 管理员权限
# ==========================
@router.put(
    "/{department_id}",
    response_model=DepartmentResponse,
)
def update_department(
    department_id: int,
    data: DepartmentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    require_admin(current_user)

    return update_department_service(
        db,
        department_id,
        data,
    )


# ==========================
# 删除部门
# 管理员权限
# ==========================
@router.delete(
    "/{department_id}",
    status_code=204,
)
def delete_department_api(
    department_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    require_admin(current_user)

    delete_department_service(
        db,
        department_id,
    )