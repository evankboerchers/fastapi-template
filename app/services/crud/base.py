from typing import Any, List, Optional
from pydantic import BaseModel
from sqlalchemy import Column
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.models.base import Base

class CRUDBase[ModelType: Base, CreateSchemaType: BaseModel, UpdateSchemaType: BaseModel]():

    def __init__(self, model: ModelType, pk: Optional[Column] = None ):
        self.model = model
        self.pk = pk if pk else model.uuid
    
    #TODO: Make pk not any. Match db schema
    def get(self, db: Session, pk: Any) -> ModelType:
        return db.query(self.model).filter(self.pk == pk).first()

    # TODO add filtering and ordering
    def get_multi(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()
    
    def create(self, db: Session, obj: CreateSchemaType) -> ModelType:
        data = jsonable_encoder(obj)
        # TODO: how to create associations
        data = self.extract_model_data(data)
        db_obj = self.model(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(self, db: Session, pk: Any, obj: UpdateSchemaType) -> ModelType:
        data = jsonable_encoder(obj, exclude_unset=True)
        data = self.extract_model_data(data)
        # TODO: How to avoid reseting fields via non explicit none.
        db_obj = self.get(db=db, pk=pk)
        for field in data:
            if field in db_obj.__dict__:
                setattr(db_obj, field, data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def delete(self, db: Session, pk: Any) -> ModelType:
        obj = self.get(db=db, pk=pk)
        db.delete(obj)
        db.commit()
        return obj

    def extract_model_data(self, data: BaseModel):            
        """
        Extract all relevant key value pairs from a dictionary for a model.

        :param obj_in_data: data to extract
        :param model: model class
        """
        obj_cols = [col.name for col in self.model.__mapper__.columns]
        out_data = {}
        for k, v in data.items():
            if k in obj_cols:
                out_data[k] = v
        return out_data