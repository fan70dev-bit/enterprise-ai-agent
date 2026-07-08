from sqlalchemy.orm import Session

from app.crud.department import (
    create_department,
    get_department_by_name,
)
from app.schemas.department import DepartmentCreate


def create_department_service(
    db: Session,
    department: DepartmentCreate,
):
    existing = get_department_by_name(db, department.name)

    if existing:
        raise ValueError("Department already exists")

    return create_department(db, department)