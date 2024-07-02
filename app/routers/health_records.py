from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models, database
from app.utills import get_current_user

router = APIRouter(
    prefix="/health_records",
    tags=["health_records"],
)

@router.post("/", response_model=schemas.HealthRecord)
def create_health_record(health_record: schemas.HealthRecordCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_health_record = models.HealthRecord(**health_record.dict(), owner_id=current_user.id)
    db.add(db_health_record)
    db.commit()
    db.refresh(db_health_record)
    return db_health_record

@router.get("/", response_model=List[schemas.HealthRecord])
def read_health_records(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    health_records = db.query(models.HealthRecord).filter(models.HealthRecord.owner_id == current_user.id).offset(skip).limit(limit).all()
    return health_records

@router.get("/{health_record_id}", response_model=schemas.HealthRecord)
def read_health_record(health_record_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    health_record = db.query(models.HealthRecord).filter(models.HealthRecord.id == health_record_id, models.HealthRecord.owner_id == current_user.id).first()
    if health_record is None:
        raise HTTPException(status_code=404, detail="Health record not found")
    return health_record

@router.delete("/{health_record_id}")
def delete_health_record(health_record_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    health_record = db.query(models.HealthRecord).filter(models.HealthRecord.id == health_record_id, models.HealthRecord.owner_id == current_user.id).first()
    if health_record is None:
        raise HTTPException(status_code=404, detail="Health record not found")
    db.delete(health_record)
    db.commit()
    return {"message": "Health record deleted successfully"}
