from inventory_report.inventory.inventory import Inventory
import sys


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    path = sys.argv[1]
    type_report = sys.argv[2]

    report = Inventory.import_data(path, type_report)
    sys.stdout.write(report)
