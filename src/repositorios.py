"""Armazenamento em memória. Pode ser trocado por um banco de dados
sem alterar o app, desde que mantenha os mesmos métodos."""


class RepositorioLojas:
    def __init__(self):
        self._lojas = {}

    def adicionar(self, loja):
        self._lojas[loja.nome] = loja

    def buscar(self, nome):
        return self._lojas.get(nome)

    def listar(self):
        return list(self._lojas.values())


class RepositorioLivros:
    def __init__(self):
        self._livros = []

    def adicionar(self, livro):
        self._livros.append(livro)

    def listar(self):
        return list(self._livros)

    def definir_estoque(self, titulo, loja, quantidade):
        if quantidade < 0:
            raise ValueError("quantidade não pode ser negativa")
        for livro in self._livros:
            if livro.titulo == titulo:
                livro.estoque[loja] = quantidade
                return
        raise KeyError(f"Livro não cadastrado: {titulo}")
