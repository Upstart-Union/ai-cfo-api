from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.parser.csv_parser import parse_csv
from app.services.finance.financial_engine import calculate_metrics

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".csv"):
            raise HTTPException(
                status_code=400,
                detail="Only CSV files are currently supported."
            )

        dataframe = parse_csv(file.file)

        metrics = calculate_metrics(dataframe)

        return {
            "success": True,
            "filename": file.filename,
            "dashboard": metrics
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )