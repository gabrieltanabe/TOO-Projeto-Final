from model.base_classes.Filme import Filme
from model.base_classes.ClassindFilme import ClassindFilme
from model.base_classes.StatusFilme import StatusFilme
from model.base_classes.Sala import Sala
from model.base_classes.TipoSala import TipoSala
from model.base_classes.Sessao import Sessao
from model.base_classes.Ingresso import IngressoFactory
from model.payment_methods.PagamentoDinheiro import PagamentoDinheiro
from model.payment_methods.PagamentoPix import PagamentoPix
from model.payment_methods.PagamentoCartao import PagamentoCartao
from model.payment_methods.Venda import Venda

# Instâncias de Filme e alterações:

f1 = Filme("Truque de Mestre: O 3° Ato", 112, descricao=None, data_estreia=None)
print("\nMétodo Representação:\n", f1)
print(f1.exibir_dados())
f1.alterar_classificacao(ClassindFilme.DOZE_ANOS)
print("Alterando Classificação: ")
print(f1.exibir_dados())

f2 = Filme("Avatar: Fogo e Cinzas", 192, classificacao=ClassindFilme.QUATORZE_ANOS, descricao=None, status=StatusFilme.EM_BREVE, data_estreia="18-12-2025")
print(f2.exibir_dados())
f2.alterar_status(StatusFilme.ESTREIA)
print("Alterando Status:")
print(f2.exibir_dados())

# Instâncias de Sala e alterações:

s1 = Sala(101, 15, tipo=TipoSala.SALA_3D)
print("Método Representação:\n", s1)
print(s1.exibir_dados())
s1.alterar_tipo(TipoSala.SALA_COMUM)
print("Alterando Tipo:")
print(s1.exibir_dados())

# Instâncias de Sessao, suas funções e instâncias Ingresso:

sessao1 = Sessao(1001, filme=f1, sala=s1, horario="30-11-2025 20:00", preco_base=30.0)
print(sessao1.exibir_dados())
sessao1.reservar_assento(1)
sessao1.reservar_assento(2)
sessao1.reservar_assento(2)
print(sessao1.exibir_dados())

ing1 = IngressoFactory.criar("comum", sessao1, 4)
print(ing1)
ing2 = IngressoFactory.criar("meia", sessao1, 5)
print(ing2)
ing3 = IngressoFactory.criar("vip", sessao1, 6)
print(ing3)

print(ing3.exibir_dados())
print(sessao1.exibir_dados())
print(sessao1.exibir_assentos())

# Instâncias de Venda, suas funções e strategies de MetodoPagamento

print("PAGAMENTO DINHEIRO")
venda_dinheiro = Venda(ing1, PagamentoDinheiro())
venda_dinheiro.finalizar()

print("PAGAMENTO CARTÃO")
venda_cartao = Venda(ing2, PagamentoCartao())
venda_cartao.finalizar()

print("PAGAMENTO PIX")
venda_pix = Venda(ing3, PagamentoPix())
venda_pix.finalizar()