import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            with open(path, encoding="utf-8") as file:
                report_reader = xmltodict.parse(file.read())
            return list(report_reader["dataset"]["record"])
        else:
            raise ValueError("Formato do arquivo inválido!")
