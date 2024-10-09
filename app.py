from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_bk = Restaurante('Burguer King','Fast Food')

bebida_suco = Bebida('OJ classic',5,'Big')
prato_sushi = Prato('temaki',30,'Temaki bruto chama no madame japo')
mega_stacker = Prato('Mega Stacker',50,'50% de chance de ter cancer')

bebida_suco.aplicar_desconto()
prato_sushi.aplicar_desconto()
mega_stacker.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_sushi)
restaurante_bk.adicionar_no_cardapio(mega_stacker)


def main():
    restaurante_praca.exibir_cardapio
    restaurante_bk.exibir_cardapio
    

if __name__ == '__main__':
    main()