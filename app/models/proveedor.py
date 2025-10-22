from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Proveedor(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    contacto = Column(String)
    telefono = Column(String)
    ciudad = Column(String)

    # Relación 1:N con productos
    productos = relationship("Producto", back_populates="proveedor_relacion")
