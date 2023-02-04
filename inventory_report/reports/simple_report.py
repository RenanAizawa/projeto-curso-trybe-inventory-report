from inventory_report.reports.tools_report import ToolsReport


class SimpleReport:
    # def __init__(self):
    #     self.tools_report = ToolsReport()

    def generate(data_list):
        try:
            old_date = ToolsReport.oldest_fabric_date(data_list)
            next_date = ToolsReport.closet_valid_date(data_list)
            empresa = ToolsReport.most_products(data_list)
        finally:
            pass
        return (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {next_date}\n"
            f"Empresa com mais produtos: {empresa}"
        )
