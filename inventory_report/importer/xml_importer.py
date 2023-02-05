from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            info_read = xmltodict.parse(file.read())["dataset"]["record"]
        return info_read