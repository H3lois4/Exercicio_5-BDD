"""Filtro de livros (desenvolvido com TDD no exercício anterior)."""
import unicodedata

from modelos import Livro  # noqa: F401  (reexportado para os testes)


def _normalizar(texto):
    """Remove acentos e diferenças entre maiúsculas e minúsculas."""
    sem_acentos = unicodedata.normalize("NFKD", texto)
    sem_acentos = "".join(c for c in sem_acentos if not unicodedata.combining(c))
    return sem_acentos.casefold().strip()


def _somente_digitos(isbn):
    return "".join(c for c in isbn if c.isalnum()).upper()


def filtrar_livros(livros, *, titulo=None, autor=None, isbn=None,
                   loja=None, apenas_disponiveis=False, preco_maximo=None):
    """Devolve os livros que atendem a TODOS os critérios informados."""
    if preco_maximo is not None and preco_maximo < 0:
        raise ValueError("preco_maximo não pode ser negativo")

    criterios = []

    if titulo:
        termo = _normalizar(titulo)
        criterios.append(lambda l: termo in _normalizar(l.titulo))

    if autor:
        termo_autor = _normalizar(autor)
        criterios.append(lambda l: termo_autor in _normalizar(l.autor))

    if isbn:
        isbn_busca = _somente_digitos(isbn)
        criterios.append(lambda l: _somente_digitos(l.isbn) == isbn_busca)

    if preco_maximo is not None:
        criterios.append(lambda l: l.preco <= preco_maximo)

    if loja:
        criterios.append(lambda l: loja in l.estoque)

    if apenas_disponiveis:
        if loja:
            criterios.append(lambda l: l.estoque.get(loja, 0) > 0)
        else:
            criterios.append(lambda l: any(q > 0 for q in l.estoque.values()))

    return [livro for livro in livros if all(c(livro) for c in criterios)]
