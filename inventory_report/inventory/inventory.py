import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        with open(path, encoding="utf-8") as file:
            report_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            report = []
            for info in report_reader:
                report.append(info)
        if type == "simples":
            return SimpleReport.generate()
        if type == "completo":
            return CompleteReport.generate()
