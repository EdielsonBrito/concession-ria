# Importação
from modelos.avaliacao import Avaliacao
from modelos.catalogo.item_catalogo import ItemCatalogo

# Definição da classe
class Concessionaria:

# Atributo de classe
    concessionarias = []

# Método construtor (__init__)
    def __init__(self, nome, categoria,plataforma):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._plataforma = plataforma.title ()
        self._ativo = False
        self._avaliacao = []
        self._catalogo = []
        Concessionaria.concessionarias.append(self)
    
# Representação textual
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._plataforma}'
    
# Método de classe
    @classmethod
    def listar_concessionarias(cls):
        ordenadas = sorted(cls.concessionarias, key=lambda c: c._plataforma)
        print(f"{'Nome da concessionária'.ljust(25)} | {'Categoria'.ljust(25)} | {'Plataforma'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'} ")
        for concessionaria in cls.concessionarias:
            print(f"{concessionaria._nome.ljust(25)} | {concessionaria._categoria.ljust(25)} | {concessionaria._plataforma.ljust(25)} |{concessionaria._avaliacao.ljust(25)} | {concessionaria.ativo}")

# Propriedade ativo
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
# Alternar estado
    def alternar_estado(self):
        self._ativo = not self._ativo

# Receber as avaliação
    def receber_avaliacao(self,cliente,nota):
        if 0 < nota <= 10:
            avaliacao = Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)

# Média das avaliações
    def media_avaliacao(self):
        if not self._avaliacao:
            return'_'
        soma_das_notas = sum (avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas,1)
        return media

# Adicionar item ao catálogo
    def adicionar_no_catalogo(self, item):
        if isinstance(item, ItemCatalogo):
            self._catalogo.append(item)

# Exibir catálogo
    @property
    def exibir_catalogo(self):
        print(f'\nCatálogo da concessionária {self._nome}\n')
        for i, item in enumerate(self._catalogo, start=1):
            if hasattr(item, 'descricao'):
                print(f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item.descricao}')
            elif hasattr(item, 'tamanho'):
                print(f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item.tamanho}')



