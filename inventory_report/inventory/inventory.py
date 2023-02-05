from inventory_report.inventory.worked_data import WorkedData
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def relatorio_type(data_list: list, type: str):
        if type == "simples":
            return SimpleReport.generate(data_list)
        elif type == "completo":
            return CompleteReport.generate(data_list)

    def import_data(path: str, type: str):
        if '.csv' in path:
            resposta = WorkedData.clean_csv(path)
            return Inventory.relatorio_type(resposta, type)
        elif '.json' in path:
            resposta = WorkedData.clean_json(path)
            return Inventory.relatorio_type(resposta, type)
        elif '.xml' in path:
            resposta = WorkedData.clean_xml(path)
            return Inventory.relatorio_type(resposta, type)
