from sqlalchemy.orm import Session

from app.models.report import Report
from app.schemas.report import ReportCreate


def create_report(
    db: Session,
    report: ReportCreate,
) -> Report:

    db_report = Report(
        content=report.content,
        user_id=report.user_id,
    )

    db.add(db_report)
    db.commit()
    db.refresh(db_report)

    return db_report


def get_report_by_id(
    db: Session,
    report_id: int,
) -> Report | None:

    return (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )


def list_reports(
    db: Session,
) -> list[Report]:

    return db.query(Report).all()


def delete_report(
    db: Session,
    report: Report,
) -> None:

    db.delete(report)
    db.commit()