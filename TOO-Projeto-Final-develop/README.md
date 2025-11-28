# Projeto final da disciplina de Tecnologia de Orientação à Objetos
Este projeto implementa um sistema de cinema simples desenvolvido em Python, utilizando os princípios da Orientação a Objetos(abstração, encapsulamento, herança e
polimorfismo). O sistema gerencia e associa classes: filmes, salas de cinema, sessões, ingressos e pagamentos.

## Padrões de Design: Factory, Strategy
### Padrão Factory

O padrão Factory é utilizado para criar diferentes tipos de ingressos no ato da venda (comum, VIP, meia). O objetivo é separar a lógica de criação dos ingressos em uma classe de fábrica, que cria instâncias diferentes de acordo com o tipo de ingresso solicitado.

### Padrão Strategy

O padrão Strategy é usado para definir diferentes métodos de pagamento. Cada estratégia de pagamento implementa o pagamneto de forma distinta, permitindo flexibilidade ao realizá-lo.
