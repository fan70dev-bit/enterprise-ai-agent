from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.crud.department import (
    create_department,
    get_department_by_id,
    list_departments,
)


def create_department_service(
    db: Session,
    department,
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