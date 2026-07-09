from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.report import (
    create_report,
    delete_report,
    get_report_by_id,
    list_reports,
)

from app.schemas.report import ReportCreate


def create_report_service(
    db: Session,
    report: ReportCreate,
):
    return create_report(db, report)


def get_report_service(
    db: Session,
    report_id: int,
):
    db_report = get_report_by_id(db, report_id)

    if db_report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    return db_report


def list_reports_service(
    db: Session,
):
    return list_reports(db)


def delete_report_service(
    db: Session,
    report_id: int,
):

    db_report = get_report_by_id(db, report_id)

    if db_report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    delete_report(
        db,
        db_report,
    )