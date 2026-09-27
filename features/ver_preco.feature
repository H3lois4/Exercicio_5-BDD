# language: pt
Funcionalidade: Ver o preço praticado na loja
  Como cliente da livraria
  Eu quero ver o preço praticado na loja
  Para não ter surpresa no caixa

  Contexto:
    Dado a loja "Paulista" no endereço "Av. Paulista, 1000" com horário "10h às 22h"
    E o livro "Grande Sertão: Veredas" de "João Guimarães Rosa" custando R$ 1.089,00
    E a loja "Paulista" tem 2 exemplares de "Grande Sertão: Veredas"

  Cenário: Preço exibido junto com a consulta
    Quando eu consulto o livro "Grande Sertão"
    Então devo ver o preço "R$ 1.089,00" na loja "Paulista"
