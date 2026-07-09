from typing import List

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.user import User

from app.core.deps import get_current_user
from app.core.permissions import require_admin

from app.schemas.report import (
    ReportCreate,
    ReportResponse,
)

from app.services.report import (
    create_report_service,
    get_report_service,
    list_reports_service,
    delete_report_service,
)

router = APIRouter(
    prefix="/reports",
    tags=["Report"],
)


@router.post(
    "",
    response_model=ReportResponse,
)
def create_report(
    report: ReportCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return create_report_service(
        db,
        report,
    )


@router.get(
    "",
    response_model=List[ReportResponse],
)
def list_reports(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_reports_service(db)


@router.get(
    "/{report_id}",
    response_model=ReportResponse,
)
def get_report(
    report_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_report_service(
        db,
        report_id,
    )


@router.delete(
    "/{report_id}",
    status_code=204,
)
def delete_report(
    report_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    delete_report_service(
        db,
        report_id,
    )

    return Response(status_code=204)