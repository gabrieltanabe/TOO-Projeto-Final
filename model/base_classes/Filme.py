from datetime import datetime
from .StatusFilme import StatusFilme
from .ClassindFilme import ClassindFilme

class Filme:
    def __init__(self, titulo, duracao, classificacao = ClassindFilme.LIVRE, descricao = None, status = StatusFilme.EM_CARTAZ, data_estreia = None):
        self.titulo = titulo
        self.__duracao = duracao
        self.classificacao = classificacao
        self.__descricao = descricao
        self.status = status
        self.__data_estreia = None
        if data_estreia:
            self.data_estreia = data_estreia

    # Titulo

    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo.title()

    # Duração

    @property
    def duracao(self):
        return self.__duracao
    @duracao.setter
    def duracao(self, minutos):
        if minutos <= 0:
            raise ValueError("A duração deve ser maior que zero.")
        self.__duracao = minutos

    # Descrição

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, texto):
        self.__descricao = texto

    # Data estreia

    @property
    def data_estreia(self):
        return self.__data_estreia
    @data_estreia.setter
    def data_estreia(self, data):
        self.__data_estreia = None
        if data is not None:
            if isinstance(data, str):
                try:
                    self.__data_estreia = datetime.strptime(data, "%d-%m-%Y")
                except ValueError:
                    print("Data inválida. Use o formato DD-MM-YYYY.")
            elif isinstance(data, datetime):
                self.__data_estreia = data
            else:
                print("Data inválida.")

    # Altera Status

    def alterar_status(self, novo_status: StatusFilme):
        if not isinstance(novo_status, StatusFilme):
            raise TypeError("Status inválido.")
        self.status = novo_status

    # Altera Classificação Indicativa

    def alterar_classificacao(self, nova_classind: ClassindFilme):
        if not isinstance(nova_classind, ClassindFilme):
            raise TypeError("Classificação inválida.")
        self.classificacao = nova_classind

    # Representação

    def __str__(self):
        return f"{self.titulo} ({self.status.value}) - {self.duracao} min\n"
    
    # Exibe dados
    
    def exibir_dados(self):
        descricao = f" Descrição: {self.descricao}\n" if self.descricao else ""
        data = f" Data de Estreia: {self.data_estreia.strftime('%d-%m-%Y')}\n" if self.data_estreia else ""

        return (
            f"FILME CADASTRADO:\n"
            f" Título: {self.titulo}\n"
            f" Status: {self.status.value}\n"
            f" Duração: {self.duracao} minutos\n"
            f" Classificação: {self.classificacao.value}\n"
            f"{descricao}"
            f"{data}"
        )