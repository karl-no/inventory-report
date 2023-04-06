from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    produto = [{
        "id": 12,
        "nome_do_produto": "Bis",
        "nome_da_empresa": "Lacta",
        "data_de_fabricacao": "2023-04-04",
        "data_de_validade": "2023-10-10",
        "numero_de_serie": "2023100809",
        "instrucoes_de_armazenamento": "local fresco e seco"
    }]

    colored_report_simple = ColoredReport(SimpleReport)
    report_simple = colored_report_simple.generate(produto)

    colored_report_complete = ColoredReport(CompleteReport)
    report_complete = colored_report_complete.generate(produto)

    assert report_simple == (
        "\033[32mData de fabricação mais antiga:\033[0m "
        + "\033[36m2023-04-04\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m "
        + "\033[36m2023-10-10\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m "
        + "\033[31mLacta\033[0m"
    )

    assert report_complete == (
        "\033[32mData de fabricação mais antiga:\033[0m "
        + "\033[36m2023-04-04\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m "
        + "\033[36m2023-10-10\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m "
        + "\033[31mLacta\033[0m\n"
        "Produtos estocados por empresa:\n"
        "- Lacta: 1\n"
    )
