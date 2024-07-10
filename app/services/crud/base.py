from typing import Any, List
from pydantic import BaseModel
from sqlalchemy import Column
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.models.base import Base

class CRUDBase[ModelType: Base, CreateSchemaType: BaseModel, UpdateSchemaType: BaseModel]():

    def __init__(self, model: ModelType, pk: Column):
        self.model = model
        self.pk = pk if pk else model.uuid
    
    #TODO: Make pk not any. Match db schema
    def get(self, db: Session, pk: Any) -> ModelType:
        return db.query(self.model).filter(self.pk == pk).first()

    # TODO add filtering and ordering
    def get_multi(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()
    
    def create(self, db: Session, obj: CreateSchemaType) -> ModelType:
        data = self.extract_object_data(jsonable_encoder(obj), self.model)
        obj = self.model(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    
    def update(self, db: Session, pk: Any, obj: UpdateSchemaType) -> ModelType:
        obj = self.get(db=db, pk=pk)
        data = self.extract_object_data(jsonable_encoder(obj), self.model)
        for field in obj:
            if field in data:
                setattr(obj, field, data[field])
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    
    def delete(self, db: Session, pk: Any) -> ModelType:
        obj = self.get(db=db, pk=pk)
        db.delete(obj)
        db.commit()
        return obj

    def extract_object_data(obj_in_data, model):            
        """
        Extract all relevant key value pairs from a dictionary for a model.

        :param obj_in_data: data to extract
        :param model: model class
        """
        obj_cols = [col.name for col in model.__mapper__.columns]
        out_data = {}
        for k, v in obj_in_data.items():
            if k in obj_cols:
                out_data[k] = v
        return out_data