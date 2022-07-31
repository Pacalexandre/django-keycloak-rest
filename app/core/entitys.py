from dataclasses import dataclass
from typing import Optional
from unicodedata import decimal

@dataclass
class CategoriaEntity:
    id: Optional[int] = None
    nome: Optional[str] = None

@dataclass
class ProdutoEntity:
    id: Optional[int] = None
    codigo: Optional[int] = None
    nome: str = None
    categoria: Optional[CategoriaEntity] = None
    preco: Optional[decimal] = 0.0

@dataclass
class NotafiscalEntity:
    id: Optional[int] = None
    numero: Optional[int] = None
    produto: Optional[ProdutoEntity] = None
    qnt: Optional[float] = None

@dataclass
class ImpostoEntity:
    nome: str
    valor: decimal = 0.0
