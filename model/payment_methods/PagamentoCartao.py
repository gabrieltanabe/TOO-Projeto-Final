from .MetodoPagamento import MetodoPagamento

class PagamentoCartao(MetodoPagamento):

    def pagar(self, valor: float):
        print(f"CARTÃO: Pagamento autorizado no valor de R$ {valor:.2f}.")
