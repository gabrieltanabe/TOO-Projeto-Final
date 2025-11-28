from abc import ABC, abstractmethod

class MetodoPagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass