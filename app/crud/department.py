from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import DepartmentCreate
from app.schemas.department import DepartmentUpdate


def create_department(db: Session, department: DepartmentCreate) -> Department:
    db_department = Department(
        name=department.name,
        description=department.description,
    )

    db.add(db_department)
    db.commit()
    db.refresh(db_department)

    return db_department


def get_department_by_id(db: Session, department_id: int) -> Department | None:
    return (
        db.query(Department)
        .filter(Department.id == department_id)
        .first()
    )


def get_department_by_name(db: Session, name: str) -> Department | None:
    return (
        db.query(Department)
        .filter(Department.name == name)
        .first()
    )


def list_departments(db: Session) -> list[Department]:
    return db.query(Department).all()


def delete_department(db: Session, department: Department) -> None:
    db.delete(department)
    db.commit()

def update_department(
    db: Session,
    department: Department,
    data: DepartmentUpdate,
):

    department.name = data.name
    department.description = data.description

    db.commit()
    db.refresh(department)

    return department