from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    categoria_id: Optional[float] = None  # Ahora puede ser None
    proveedor_id: Optional[float] = None  # Ahora puede ser None
    usuario_id: Optional[float] = None    # Ahora puede ser None
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