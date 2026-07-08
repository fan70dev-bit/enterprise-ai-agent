from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
)
from app.crud.department import (
    create_department,
    get_department_by_id,
    list_departments,
    update_department,
    delete_department,
)


def create_department_service(
    db: Session,
    department: DepartmentCreate,
):
    return create_department(
        db,
        department
    )


def get_department_service(
    db: Session,
    department_id: int,
):

    department = get_department_by_id(
        db,
        department_id
    )

    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )

    return department

def list_department_service(
    db: Session,
):
    return list_departments(db)

def update_department_service(
    db: Session,
    department_id: int,
    data: DepartmentUpdate,
):

    department = get_department_by_id(
        db,
        department_id
    )

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return update_department(
        db,
        department,
        data
    )

def delete_department_service(
    db: Session,
    department_id: int,
):
    department = get_department_by_id(db, department_id)

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    delete_department(db, department)