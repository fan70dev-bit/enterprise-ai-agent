from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
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

router = APIRouter(prefix="/departments", tags=["Department"])


@router.post("", response_model=DepartmentResponse)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
):
    return create_department_service(db, department)

@router.get(
    "/{department_id}",
    response_model=DepartmentResponse,
)
def get_department(
    department_id: int,
    db: Session = Depends(get_db),
):
    return get_department_service(db, department_id)

@router.get(
    "",
    response_model=list[DepartmentResponse],
)
def list_departments_api(
    db: Session = Depends(get_db),
):
    return list_department_service(db)

@router.put(
    "/{department_id}",
    response_model=DepartmentResponse,
)
def update_department(
    department_id: int,
    data: DepartmentUpdate,
    db: Session = Depends(get_db),
):

    return update_department_service(
        db,
        department_id,
        data
    )

@router.delete(
    "/{department_id}",
    status_code=204,
)
def delete_department_api(
    department_id: int,
    db: Session = Depends(get_db),
):
    delete_department_service(db, department_id)