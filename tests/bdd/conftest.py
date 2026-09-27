"""Definição dos passos (steps) usados nos cenários BDD."""
import pytest
from pytest_bdd import given, parsers, then, when

from app import AppLivraria, LojaNaoEncontrada, formatar_preco
from modelos import Livro, Loja
from repositorios import RepositorioLivros, RepositorioLojas


def converter_preco(texto):
    """Converte '1.089,00' em 1089.0."""
    return float(texto.replace(".", "").replace(",", "."))


@pytest.fixture
def repo_livros():
    return RepositorioLivros()


@pytest.fixture
def repo_lojas():
    return RepositorioLojas()


@pytest.fixture
def app(repo_livros, repo_lojas):
    return AppLivraria(repo_livros, repo_lojas)


@pytest.fixture
def contexto():
    """Guarda o que aconteceu no 'Quando' para ser verificado no 'Então'."""
    return {}


# ---------- Dado ----------

@given(parsers.parse('a loja "{nome}" no endereço "{endereco}" com horário "{horario}"'))
def cadastrar_loja(repo_lojas, nome, endereco, horario):
    repo_lojas.adicionar(Loja(nome, endereco, horario))


@given(parsers.parse('o livro "{titulo}" de "{autor}" custando R$ {preco}'))
def cadastrar_livro(repo_livros, titulo, autor, preco):
    isbn = f"ISBN-{len(repo_livros.listar()) + 1}"
    repo_livros.adicionar(Livro(isbn, titulo, autor, converter_preco(preco)))


@given(parsers.parse('a loja "{loja}" tem {quantidade:d} exemplares de "{titulo}"'))
def definir_estoque(repo_livros, loja, quantidade, titulo):
    repo_livros.definir_estoque(titulo, loja, quantidade)


@given(parsers.parse('que eu escolhi a loja "{nome}" como favorita'))
def ja_escolhi_favorita(app, nome):
    app.definir_loja_favorita(nome)


# ---------- Quando ----------

@when(parsers.parse('eu consulto o livro "{termo}"'))
def consultar_livro(app, contexto, termo):
    resultado = app.consultar(termo)
    contexto["resultado"] = resultado
    contexto["mensagem"] = resultado.mensagem


@when(parsers.parse('eu vejo as informações da loja "{nome}"'))
def ver_informacoes_loja(app, contexto, nome):
    try:
        contexto["loja"] = app.informacoes_loja(nome)
    except LojaNaoEncontrada as erro:
        contexto["mensagem"] = str(erro)


@when(parsers.parse('eu escolho a loja "{nome}" como favorita'))
def escolher_favorita(app, contexto, nome):
    try:
        app.definir_loja_favorita(nome)
    except LojaNaoEncontrada as erro:
        contexto["mensagem"] = str(erro)


# ---------- Então ----------

def item_da_loja(contexto, loja):
    itens = [i for i in contexto["resultado"].itens if i.loja == loja]
    assert itens, f"A loja {loja} não apareceu no resultado"
    return itens[0]


@then(parsers.parse('devo ver que ele está disponível na loja "{loja}" com {quantidade:d} exemplares'))
def verificar_disponivel(contexto, loja, quantidade):
    item = item_da_loja(contexto, loja)
    assert item.disponivel
    assert item.quantidade == quantidade


@then(parsers.parse('devo ver que ele está indisponível na loja "{loja}"'))
def verificar_indisponivel(contexto, loja):
    assert not item_da_loja(contexto, loja).disponivel


@then(parsers.parse('devo ver o preço "{preco}" na loja "{loja}"'))
def verificar_preco(contexto, preco, loja):
    assert formatar_preco(item_da_loja(contexto, loja).preco) == preco


@then(parsers.parse('devo ver o endereço "{endereco}"'))
def verificar_endereco(contexto, endereco):
    assert contexto["loja"].endereco == endereco


@then(parsers.parse('devo ver o horário "{horario}"'))
def verificar_horario(contexto, horario):
    assert contexto["loja"].horario == horario


@then(parsers.parse('a primeira loja exibida deve ser "{loja}"'))
def verificar_primeira_loja(contexto, loja):
    assert contexto["resultado"].itens[0].loja == loja


@then(parsers.parse('devo ver a mensagem "{mensagem}"'))
def verificar_mensagem(contexto, mensagem):
    assert contexto.get("mensagem") == mensagem
