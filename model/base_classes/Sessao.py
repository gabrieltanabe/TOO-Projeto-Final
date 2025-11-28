from datetime import datetime
from .Filme import Filme
from .Sala import Sala

class Sessao:
    def __init__(self, numero, filme: Filme, sala: Sala, horario, preco_base: float):
        self.numero = numero
        self.filme = filme
        self.sala = sala
        self.horario = horario
        self.preco_base = preco_base
        
    # Número

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("O número deve ser inteiro positivo.")
        self.__numero = numero

    # Filme

    @property
    def filme(self):
        return self.__filme
    @filme.setter
    def filme(self, filme_obj):
        if not isinstance(filme_obj, Filme):
            raise TypeError("O atributo 'filme' deve ser uma instância de Filme.")
        self.__filme = filme_obj

    # Sala

    @property
    def sala(self):
        return self.__sala
    @sala.setter
    def sala(self, sala_obj):
        if not isinstance(sala_obj, Sala):
            raise TypeError("O atributo 'sala' deve ser uma instância de Sala.")

        self.__sala = sala_obj

        self.__assentos_ocupados = set()
        self.__assentos_livres = set(range(1, sala_obj.capacidade + 1))

    # Horário

    @property
    def horario(self):
        return self.__horario
    @horario.setter
    def horario(self, h):
        if isinstance(h, str):
            try:
                self.__horario = datetime.strptime(h, "%d-%m-%Y %H:%M")
            except ValueError:
                raise ValueError("Horário inválido. Use o formato DD-MM-YYYY HH:MM.\n")
        elif isinstance(h, datetime):
            self.__horario = h
        else:
            raise TypeError("Horário deve ser string no formato correto ou datetime.\n")

    # Preço base

    @property
    def preco_base(self):
        return self.__preco_base
    @preco_base.setter
    def preco_base(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("O preço base deve ser um número.")
        if valor <= 0:
            raise ValueError("O preço base deve ser maior que zero.")
        self.__preco_base = float(valor)

    # Assentos

    def reservar_assento(self, numero_assento: int):
        try:
            if not isinstance(numero_assento, int):
                raise TypeError("O número do assento deve ser inteiro.")

            if numero_assento not in self.__assentos_livres:
                if numero_assento in self.__assentos_ocupados:
                    raise ValueError(
                        f"O assento {numero_assento} já está reservado.\n"
                        f"Assentos livres: {sorted(self.__assentos_livres)}\n"
                    )
                else:
                    raise ValueError(
                        f"Assento {numero_assento} não existe na Sala {self.sala.numero}. "
                        f"Escolha entre 1 e {self.sala.capacidade}.\n"
                    )

            # Reserva o assento
            self.__assentos_livres.remove(numero_assento)
            self.__assentos_ocupados.add(numero_assento)

            print(f"Assento {numero_assento} reservado com sucesso!\n")

        except (TypeError, ValueError) as e:
            print(f"Erro ao reservar o assento: {e}")

    def liberar_assento(self, numero_assento: int):
        if numero_assento in self.__assentos_ocupados:
            self.__assentos_ocupados.remove(numero_assento)
            self.__assentos_livres.add(numero_assento)
            print(f"Assento {numero_assento} agora está livre.\n")
        else:
            print(f"O assento {numero_assento} já está livre.\n")

    def assentos_disponiveis(self):
        return len(self.__assentos_livres)
    
    # Representação

    def __str__(self):
        return f"Sessão {self.numero} - {self.filme.titulo}\nSala {self.sala.numero} - {self.sala.tipo.value}"

    # Exibe dados 
    
    def exibir_dados(self): 
        data_hora = self.horario.strftime("%d-%m-%Y %H:%M") 
        ocupados = (
            ", ".join(map(str, sorted(self.__assentos_ocupados))) 
            if self.__assentos_ocupados else "Nenhum" 
        ) 
        return ( 
            "SESSÃO ATIVA:\n" 
            f" Filme: {self.filme.titulo}\n" 
            f" Sala: {self.sala.numero} ({self.sala.tipo.value})\n" 
            f" Horário: {data_hora}\n" 
            f" Capacidade: {self.sala.capacidade}\n" 
            f" Assentos disponíveis: {self.assentos_disponiveis()}\n" 
            f" Assentos ocupados: {ocupados}\n" 
        )
    
    # Exibe assentos disponíveis

    def exibir_assentos(self):
        return f"Assentos livres: {sorted(self.__assentos_livres)}\n" 