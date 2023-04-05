from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def define_path(path):
    if path.endswith(".csv"):
        info = CsvImporter.import_data(path)
    elif path.endswith(".json"):
        info = JsonImporter.import_data(path)
    elif path.endswith(".xml"):
        info = XmlImporter.import_data(path)
    return info


class Inventory:

    def import_data(path, type):
        info = define_path(path)
        if type == "simples":
            return SimpleReport.generate(info)
        elif type == "completo":
            return CompleteReport.generate(info)
