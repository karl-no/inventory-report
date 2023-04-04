from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "caneta",
        "Pentel",
        "2023-01-14",
        "2033-01-14",
        "110002055",
        "em local fresco e longe do sol",
    )

    assert produto.__repr__() == (
            "O produto caneta"
            " fabricado em 2023-01-14"
            " por Pentel com validade"
            " até 2033-01-14"
            " precisa ser armazenado em local fresco e longe do sol."
    )
