class Venda:
    def __init__(self, ingresso, metodo_pagamento):
        self.ingresso = ingresso
        self.metodo_pagamento = metodo_pagamento

    def finalizar(self):
        valor = self.ingresso.calcular_preco()

        print("\nPROCESSANDO VENDA")
        print(self.ingresso.exibir_dados())

        self.metodo_pagamento.pagar(valor)

        print("Venda concluída com sucesso!\n")