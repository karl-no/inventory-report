from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, products):
        oldest_manufacturing_date = cls.get_oldest_manufacturing_date(products)
        closest_expiring_date = cls.get_closest_expiring_date(products)
        company_with_more_products = cls.get_company_with_more_products(
            products
        )
        products_stocked_by_company = cls.get_products_stocked_by_company(
            products
        )

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiring_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}\n"
            f"Produtos estocados por empresa:\n{products_stocked_by_company}"
        )

    @classmethod
    def get_products_stocked_by_company(cls, products):
        companies = {}
        for product in products:
            if product["nome_da_empresa"] in companies:
                companies[product["nome_da_empresa"]] += 1
            else:
                companies[product["nome_da_empresa"]] = 1
        result = ""
        for item in companies.items():
            result += f"- {item[0]}: {item[1]}\n"
        return result
