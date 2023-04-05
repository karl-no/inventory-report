import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as file:
                report_reader = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                return list(report_reader)
        else:
            raise ValueError("Arquivo inválido")
