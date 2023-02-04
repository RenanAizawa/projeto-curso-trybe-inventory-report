from datetime import datetime


class ToolsReport:
    @staticmethod
    def most_products(data_list: list):
        company_count = {}
        for company in data_list:
            company_name = company["nome_da_empresa"]
            if company_name not in company_count.keys():
                company_count[f"{company_name}"] = 1
            else:
                company_count[f"{company_name}"] += 1
        return sorted(company_count.items(), key=lambda t: t[1])[-1][0]

    @staticmethod
    def closet_valid_date(data_list: list):
        today = datetime.now()
        datas_validas = []
        for product in data_list:
            data_validade = datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d")
            if data_validade > today:
                datas_validas.append(data_validade)
        return min(datas_validas).date()

    @staticmethod
    def oldest_fabric_date(data_list: list):
        oldest_date = datetime.now()
        for product in data_list:
            fabric_date = datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d")
            if fabric_date < oldest_date:
                oldest_date = fabric_date
        return oldest_date.date()

    @staticmethod
    def company_stock(self, data_list: list):
        stock_dict = self.calculate_stock_company(data_list)
        return "".join(stock_dict)

    def calculate_stock_company(data_list: list):
        pass
