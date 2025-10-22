from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    categoria_id: float
    proveedor_id: float
    usuario_id: float
    precio: float
    ciudad: str
    fuente: str

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    pass

class Config:
    orm_mode = True