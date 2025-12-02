from .TipoSala import TipoSala

class Sala:
    def __init__(self, numero, capacidade, tipo = TipoSala.SALA_COMUM):
        self.numero = numero
        self.capacidade = capacidade
        self.tipo = tipo

    # Número

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("O número deve ser inteiro positivo.")
        self.__numero = numero

    # Capacidade

    @property
    def capacidade(self):
        return self.__capacidade
    @capacidade.setter
    def capacidade(self, capacidade):
        if not isinstance(capacidade, int) or capacidade <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")
        self.__capacidade = capacidade

    # Altera Tipo de Sala

    def alterar_tipo(self, novo_tipo: TipoSala):
        if not isinstance(novo_tipo, TipoSala):
            raise TypeError("Tipo inválido.")
        self.tipo = novo_tipo

    # Representação

    def __str__(self):
        return f"Sala {self.numero} ({self.capacidade}) - {self.tipo.value}\n"
    
    # Exibe dados

    def exibir_dados(self):
        return (
            f"SALA CADASTRADA:\n"
            f" Número: {self.numero}\n"
            f" Capacidade: {self.capacidade}\n"
            f" Tipo: {self.tipo.value}\n"
        )