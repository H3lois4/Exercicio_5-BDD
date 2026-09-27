# language: pt
Funcionalidade: Consultar estoque do livro na loja
  Como cliente da livraria
  Eu quero consultar se o livro está em estoque na loja
  Para não me deslocar à toa

  Contexto:
    Dado a loja "Paulista" no endereço "Av. Paulista, 1000" com horário "10h às 22h"
    E a loja "Pinheiros" no endereço "Rua dos Pinheiros, 500" com horário "9h às 21h"
    E o livro "Dom Casmurro" de "Machado de Assis" custando R$ 29,90
    E a loja "Paulista" tem 3 exemplares de "Dom Casmurro"
    E a loja "Pinheiros" tem 0 exemplares de "Dom Casmurro"

  Cenário: Livro disponível em uma loja e esgotado em outra
    Quando eu consulto o livro "Dom Casmurro"
    Então devo ver que ele está disponível na loja "Paulista" com 3 exemplares
    E devo ver que ele está indisponível na loja "Pinheiros"

  Cenário: Consulta sem diferenciar maiúsculas e acentos
    Quando eu consulto o livro "dom casmurro"
    Então devo ver que ele está disponível na loja "Paulista" com 3 exemplares

  Cenário: Livro que a livraria não possui
    Quando eu consulto o livro "Harry Potter"
    Então devo ver a mensagem "Nenhum livro encontrado"
