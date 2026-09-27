"""Entidades do domínio."""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Livro:
    isbn: str
    titulo: str
    autor: str
    preco: float
    estoque: dict = field(default_factory=dict)  # {nome_da_loja: quantidade}


@dataclass(frozen=True)
class Loja:
    nome: str
    endereco: str
    horario: str
