from dataclasses import dataclass, field
from typing import Optional
from unicodedata import decimal

@dataclass
class CategoriaEntity:
    id: Optional[int]
    nome: Optional[str] = None

@dataclass
class ProdutoEntity:
    id: Optional[int]
    codigo: Optional[int] = None
    nome: str = None
    categoria: Optional[CategoriaEntity] = None
    preco: Optional[decimal] = 0.0

@dataclass
class NotafiscalEntity:
    id: Optional[int]
    numero: Optional[int] = None
    produto: ProdutoEntity = None
    qnt: Optional[float] = None

@dataclass
class ImpostoEntity:
    nome: str
    valor: decimal = 0.0
