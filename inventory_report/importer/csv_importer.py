from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            info_read = csv.DictReader(file)
            listed = list(info_read)
        return listed
