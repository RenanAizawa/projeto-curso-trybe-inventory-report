from inventory_report.reports.tool_report import Tools_report

class SimpleReport:
    def __init__(self):
        self.tools_report = Tools_report()


    def generate(self, data_list):
        return (
            f"Data de fabricação mais antiga: {self.tools_report.oldest_fabric_date(data_list)}\n"
            f"Data de validade mais próxima: {data_val_mais_proxiself.tools_report.closet_valid_date(data_list)}\n"
            f"Empresa com mais produtos: {self.tools_report.most_products(data_list)}\n"
        )
        