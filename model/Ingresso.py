from abc import ABC, abstractmethod
from model.Sessao import Sessao

class Ingresso(ABC):
    def __init__(self, sessao: Sessao, assento: int):
        if not isinstance(sessao, Sessao):
            raise TypeError("Deve ser uma instância de Sessao.")
        if not isinstance(assento, int):
            raise TypeError("O assento deve ser um número inteiro.")

        self.sessao = sessao
        self.assento = assento

    @abstractmethod
    def calcular_preco(self):
        pass

    @abstractmethod
    def tipo(self):
        pass

    def exibir_dados(self):
        horario = self.sessao.horario.strftime("%d/%m/%Y %H:%M")
        return (
            f"DADOS DO INGRESSO:\n"
            f" Tipo: {self.tipo()}\n"
            f" Filme: {self.sessao.filme.titulo}\n"
            f" Sala: {self.sessao.sala.numero}\n"
            f" Horário: {horario}\n"
            f" Assento: {self.assento}\n"
            f" Preço: R$ {self.calcular_preco():.2f}\n"
        )

    def __str__(self):
        horario = self.sessao.horario.strftime("%d/%m %H:%M")
        return (
            f"- {self.tipo()}\n"
            f" - Filme: {self.sessao.filme.titulo}\n"
            f" - Sala {self.sessao.sala.numero} - {horario} Assento {self.assento}\n"
            f" -  Preço: R$ {self.calcular_preco():.2f}\n"
        )


# Tipos Ingresso

class IngressoComum(Ingresso):
    def calcular_preco(self):
        return self.sessao.preco_base

    def tipo(self):
        return "Ingresso Comum"


class IngressoMeia(Ingresso):
    def calcular_preco(self):
        return self.sessao.preco_base * 0.5

    def tipo(self):
        return "Ingresso Meia-Entrada"


class IngressoVip(Ingresso):
    def calcular_preco(self):
        return self.sessao.preco_base * 1.15

    def tipo(self):
        return "Ingresso VIP"

class IngressoFactory:
    @staticmethod
    def criar(tipo, sessao, assento):
        tipo = tipo.lower().strip()

        sessao.reservar_assento(assento)

        if tipo == "comum":
            return IngressoComum(sessao, assento)
        elif tipo == "meia":
            return IngressoMeia(sessao, assento)
        elif tipo == "vip":
            return IngressoVip(sessao, assento)
        else:
            raise ValueError(
                f"Tipo de ingresso inválido: {tipo}. Opções: comum, meia, vip."
            )