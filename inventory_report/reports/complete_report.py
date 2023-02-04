from inventory_report.reports.tools_report import ToolsReport


class CompleteReport:
    def generate(data_list):
        old_date = ToolsReport.oldest_fabric_date(data_list)
        next_date = ToolsReport.closet_valid_date(data_list)
        empresa = ToolsReport.most_products(data_list)
        lista_empresas = ToolsReport.company_stock(data_list)
        return (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {next_date}\n"
            f"Empresa com mais produtos: {empresa}\n"
            f"Produtos estocados por empresa:\n"
            f"{lista_empresas}"
        )
