# language: pt
Funcionalidade: Ver horário e endereço da loja
  Como cliente da livraria
  Eu quero ver o horário de funcionamento e o endereço da loja
  Para planejar minha visita

  Contexto:
    Dado a loja "Paulista" no endereço "Av. Paulista, 1000" com horário "10h às 22h"

  Cenário: Consultar informações de uma loja existente
    Quando eu vejo as informações da loja "Paulista"
    Então devo ver o endereço "Av. Paulista, 1000"
    E devo ver o horário "10h às 22h"

  Cenário: Consultar uma loja que não existe
    Quando eu vejo as informações da loja "Centro"
    Então devo ver a mensagem "Loja não encontrada"
