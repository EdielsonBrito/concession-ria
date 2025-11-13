from modelos.catalogo.item_catalogo import ItemCatalogo

class Sedan(ItemCatalogo):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self.descricao = descricao

    def aplicar_desconto(self):
        self._preco -= self._preco *0.10 # 10% de desconto

    def __str__(self):
        return f'{self._nome} (Sedan) - {self._preco:.2f}'
    