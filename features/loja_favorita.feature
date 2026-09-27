# language: pt
Funcionalidade: Escolher loja favorita
  Como cliente da livraria
  Eu quero escolher minha loja favorita
  Para ver sempre o estoque dela primeiro

  Contexto:
    Dado a loja "Paulista" no endereço "Av. Paulista, 1000" com horário "10h às 22h"
    E a loja "Pinheiros" no endereço "Rua dos Pinheiros, 500" com horário "9h às 21h"
    E o livro "A Hora da Estrela" de "Clarice Lispector" custando R$ 39,90
    E a loja "Paulista" tem 1 exemplares de "A Hora da Estrela"
    E a loja "Pinheiros" tem 5 exemplares de "A Hora da Estrela"

  Cenário: Sem loja favorita, as lojas aparecem em ordem alfabética
    Quando eu consulto o livro "A Hora da Estrela"
    Então a primeira loja exibida deve ser "Paulista"

  Cenário: A loja favorita aparece primeiro
    Dado que eu escolhi a loja "Pinheiros" como favorita
    Quando eu consulto o livro "A Hora da Estrela"
    Então a primeira loja exibida deve ser "Pinheiros"

  Cenário: Não é possível favoritar uma loja inexistente
    Quando eu escolho a loja "Centro" como favorita
    Então devo ver a mensagem "Loja não encontrada"
