from modelos.catalogo.item_catalogo import ItemCatalogo

class Hatch(ItemCatalogo):
    def __init__(self, nome, preco,tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def aplicar_desconto(self):
        self._preco  -= self._preco*0.08 # 8% de desconto

    def __str__(self):
        return f'{self._nome} (Hatch) - {self._preco:.2f}'

