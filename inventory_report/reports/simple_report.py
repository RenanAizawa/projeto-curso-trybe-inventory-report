from inventory_report.reports.tool_report import Tools_report


class SimpleReport:
    def __init__(self):
        self.tools_report = Tools_report()

    def generate(self, data_list):
        try
            old_date = self.tools_report.oldest_fabric_date(data_list)
            next_date = self.tools_report.closet_valid_date(data_list)
            empresa = self.tools_report.most_products(data_list)
        else
            pass
        return (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {next_date}\n"
            f"Empresa com mais produtos: {empresa}\n"
        )
