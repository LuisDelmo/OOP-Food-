from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('OJ classic',5,'Big')
prato_sushi = Prato('temaki',30,'Temaki bruto chama no madame japo')

restaurante_praca.adicionar_bebida_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_sushi)

def main():
    print(bebida_suco)
    print(prato_sushi)

if __name__ == '__main__':
    main()