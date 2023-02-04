from datetime import datetime


class Tools_report:
    format_date = "%y-%m-%d"

    def most_products(data_list: list):
        company_count = {}
        for company in data_list:
            company_name = company["nome_da_empresa"]
            if company_name not in company_count.keys():
                company_count[f"{company_name}"] = 1
            else:
                company_count[f"{company_name}"] += 1
        return max(company_count)

    def closet_valid_date(data_list: list, format_date):
        today = datetime.now()
        datas_validas = []
        for product in data_list:
            data_validade = datetime.strptime(
                product["data_de_validade"], format_date)
            if data_validade > today:
                datas_validas.append(data_validade)
        return min(datas_validas).date()

    def oldest_fabric_date(data_list: list, format_date):
        oldest_date = datetime.now()
        for product in data_list:
            fabric_date = datetime.strptime(
                product["data_de_fabricacao"], format_date)
            if fabric_date < oldest_date:
                oldest_date = fabric_date
        return oldest_date.date()

    def company_stock(self, data_list: list):
        stock_dict = self.calculate_stock_company(data_list)
        return "".join(stock_dict)

    def calculate_stock_company(data_list: list):
        pass
