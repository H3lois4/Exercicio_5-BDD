# Livraria MVP – BDD e desenvolvimento top-down

MVP do aplicativo da livraria: o cliente descobre, antes de sair de casa,
se vale a pena ir à loja.

## Histórias implementadas

| História | Arquivo de comportamento |
|---|---|
| Consultar se o livro está em estoque na loja | `features/consultar_estoque.feature` |
| Ver o preço praticado na loja | `features/ver_preco.feature` |
| Ver horário de funcionamento e endereço | `features/informacoes_loja.feature` |
| Escolher loja favorita | `features/loja_favorita.feature` |

## Como foi desenvolvido

**BDD:** o comportamento de cada história foi escrito primeiro em Gherkin
(português), com cenários Dado / Quando / Então. Os passos em
`tests/bdd/conftest.py` transformam esses cenários em testes automáticos.

**Top-down:** o código foi escrito do nível mais alto para o mais baixo:

1. `features/` – comportamento esperado
2. `tests/bdd/` – passos que exercitam o sistema
3. `src/app.py` – casos de uso (camada mais alta)
4. `src/modelos.py` e `src/repositorios.py` – entidades e armazenamento
5. `src/busca.py` – filtro de livros (base, testado com TDD em `tests/unit/`)

## Estrutura

```
features/          cenários BDD em Gherkin
src/               código do sistema
tests/bdd/         passos dos cenários BDD
tests/unit/        testes unitários (TDD)
```

## Como rodar

```bash
pip install -r requirements.txt
pytest -v
```