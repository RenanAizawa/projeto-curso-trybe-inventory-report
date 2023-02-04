from datetime import date

from inventory_report.inventory.product import Product


def test_cria_produto():
    mock_product = Product(
        id=0,
        nome_do_produto="manga hype",
        nome_da_empresa="Aizawa S.A",
        data_de_fabricacao=date(2023, 1, 1),
        data_de_validade=date(2023, 1, 31),
        numero_de_serie="123456789",
        instrucoes_de_armazenamento="no gelo",
    )
    assert mock_product.id == 0
    assert mock_product.nome_do_produto == "manga hype"
    assert mock_product.nome_da_empresa == "Aizawa S.A"
    assert mock_product.data_de_fabricacao == "2023-01-01"
    assert mock_product.data_de_validade == "2023-01-31"
    assert mock_product.numero_de_serie == "123456789"
    assert mock_product.instrucoes_de_armazenamento == "no gelo"
