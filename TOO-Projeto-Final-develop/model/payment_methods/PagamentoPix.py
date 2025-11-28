from .MetodoPagamento import MetodoPagamento

class PagamentoPix(MetodoPagamento):

    def pagar(self, valor: float):
        print(f"PIX: Pagamento confirmado no valor de R$ {valor:.2f}.")
