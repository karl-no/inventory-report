from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter


class Inventory:
    @staticmethod
    def import_data(path, type):
        if path.endswith(".csv"):
            info = CsvImporter.import_data(path)
        if path.endswith(".json"):
            info = JsonImporter.import_data(path)

        if type == "simples":
            return SimpleReport.generate(info)
        if type == "completo":
            return CompleteReport.generate(info)
