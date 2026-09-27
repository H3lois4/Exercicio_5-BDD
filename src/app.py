"""Nível mais alto do sistema: os casos de uso do MVP.

Desenvolvido top-down: esta camada foi escrita primeiro e define o que
as camadas de baixo (repositorios, busca, modelos) precisam oferecer.
"""
from dataclasses import dataclass, field

from busca import filtrar_livros


class LojaNaoEncontrada(Exception):
    def __init__(self):
        super().__init__("Loja não encontrada")


@dataclass(frozen=True)
class ItemConsulta:
    titulo: str
    autor: str
    loja: str
    quantidade: int
    preco: float

    @property
    def disponivel(self):
        return self.quantidade > 0


@dataclass
class ResultadoConsulta:
    itens: list = field(default_factory=list)
    mensagem: str | None = None


def formatar_preco(valor):
    """Formata 1089.0 como 'R$ 1.089,00'."""
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


class AppLivraria:
    def __init__(self, repo_livros, repo_lojas):
        self._livros = repo_livros
        self._lojas = repo_lojas
        self._loja_favorita = None

    # História: consultar estoque + ver preço
    def consultar(self, termo):
        livros = filtrar_livros(self._livros.listar(), titulo=termo)
        if not livros:
            return ResultadoConsulta(mensagem="Nenhum livro encontrado")

        itens = [
            ItemConsulta(livro.titulo, livro.autor, loja, livro.estoque[loja], livro.preco)
            for livro in livros
            for loja in self._ordenar_lojas(livro.estoque)
        ]
        return ResultadoConsulta(itens=itens)

    # História: ver horário e endereço
    def informacoes_loja(self, nome):
        loja = self._lojas.buscar(nome)
        if loja is None:
            raise LojaNaoEncontrada()
        return loja

    # História: loja favorita
    def definir_loja_favorita(self, nome):
        self._loja_favorita = self.informacoes_loja(nome).nome

    def _ordenar_lojas(self, nomes):
        """Loja favorita primeiro; as demais em ordem alfabética."""
        return sorted(nomes, key=lambda nome: (nome != self._loja_favorita, nome))
