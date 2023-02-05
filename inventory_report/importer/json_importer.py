from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        if ".json" not in path:
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            info_read = file.read()
        return list(json.loads(info_read))
