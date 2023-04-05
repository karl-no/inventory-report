import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".json"):
            with open(path) as file:
                report_reader = json.load(file)
                return report_reader
        else:
            raise ValueError("Formato do arquivo inválido!")
