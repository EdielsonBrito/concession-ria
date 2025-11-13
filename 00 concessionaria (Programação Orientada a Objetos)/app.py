from modelos.concessionaria import Concessionaria
from modelos.catalogo.sedan import Sedan
from modelos.catalogo.hatch import Hatch

# Criando concessionárias
concessionaria_barra = Concessionaria('barra', 'importados','b')
concessionaria_tijuca = Concessionaria('Tijuca', 'sedan', 'a')

# Criando intens do catalogo
renalt_logan = Sedan('Logan', 20.0, 'grande')
honda_civic = Sedan('Civc', 50.0, 'grande')
mini_cooper = Hatch('Cooper',40.0,'pequeno')
onix = Hatch('onix',60.0,'pequeno')

# Adicionando carros às concessionárias
concessionaria_barra.adicionar_no_catalogo(renalt_logan)
concessionaria_barra.adicionar_no_catalogo(mini_cooper)

concessionaria_tijuca.adicionar_no_catalogo(honda_civic)
concessionaria_tijuca.adicionar_no_catalogo(onix)

# Função principal
def main():
    Concessionaria.listar_concessionarias()
     # Exibir catálogo de cada concessionária
    for c in Concessionaria.concessionarias:
        c.exibir_catalogo

if __name__ == '__main__':
    main()

#Criando objetos
#concessionaria_barra = Concessionaria('Barra','importados')
#concessionaria_barra.alternar_estado()
#concessionaria_tijuca = Concessionaria('Tijuca', 'sedan')

#Listando todas
#Concessionaria.listar_concessionarias()