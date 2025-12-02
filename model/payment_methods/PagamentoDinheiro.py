from .MetodoPagamento import MetodoPagamento

class PagamentoDinheiro(MetodoPagamento):

    def pagar(self, valor: float):
        print(f"DINHEIRO: Recebido R$ {valor:.2f}. Troco calculado se necessário.")
