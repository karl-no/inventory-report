from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = {
        "id": 12,
        "nome_do_produto": "Bis",
        "nome_da_empresa": "Lacta",
        "data_de_fabricacao": "04/04/2023",
        "data_de_validade": "10/10/2023",
        "numero_de_serie": "2023100809",
        "instrucoes_de_armazenamento": "local fresco e seco"
    }

    produto_mock = Product(
        produto["id"],
        produto["nome_do_produto"],
        produto["nome_da_empresa"],
        produto["data_de_fabricacao"],
        produto["data_de_validade"],
        produto["numero_de_serie"],
        produto["instrucoes_de_armazenamento"]
    )

    assert produto_mock.__repr__() == (
        "O produto Bis fabricado em 04/04/2023"
        " por Lacta com validade até 10/10/2023"
        " precisa ser armazenado local fresco e seco."
    )
