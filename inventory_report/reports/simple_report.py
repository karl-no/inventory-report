from datetime import datetime
from collections import Counter


class SimpleReport:

    @classmethod
    def generate(cls, products):
        oldest_manufacturing_date = cls.get_oldest_manufacturing_date(products)
        closest_expiring_date = cls.get_closest_expiring_date(products)
        company_with_more_products = cls.get_company_with_more_products(
            products
        )
        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiring_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )

    @classmethod
    def get_oldest_manufacturing_date(cls, products):
        return min(item["data_de_fabricacao"] for item in products)

    @classmethod
    def get_closest_expiring_date(cls, products):
        return min([
            item["data_de_validade"] for item in products
            if datetime.strptime(
                item["data_de_validade"], "%Y-%m-%d"
            ) > datetime.today()
        ])

    @classmethod
    def get_company_with_more_products(cls, products):
        return Counter(
            item["nome_da_empresa"] for item in products
        ).most_common(1)[0][0]
