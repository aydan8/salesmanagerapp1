from collections import defaultdict
from datetime import datetime

class SalesManager:
    def __init__(self):
        self.sales_data = {}
        self.salesperson_data = {}
        self.sales_history = defaultdict(list)

    def add_sale(self, salesperson, product, amount):
        now = datetime.now()
        month_year = now.strftime("%B %Y")

        if product in self.sales_data:
            self.sales_data[product] += amount
        else:
            self.sales_data[product] = amount

        if salesperson in self.salesperson_data:
            if product in self.salesperson_data[salesperson]:
                self.salesperson_data[salesperson][product] += amount
            else:
                self.salesperson_data[salesperson][product] = amount
        else:
            self.salesperson_data[salesperson] = {product: amount}

        self.sales_history[month_year].append((salesperson, product, amount))

    def total_sales(self):
        return sum(self.sales_data.values())

    def sales_report(self):
        print("Sales Report:")
        for product, amount in self.sales_data.items():
            print(f"{product}: {amount}")

    def salesperson_report(self):
        print("Salesperson Report:")
        for salesperson, sales_data in self.salesperson_data.items():
            print(f"{salesperson}:")
            for product, amount in sales_data.items():
                print(f"\t{product}: {amount}")

    def trend_analysis(self):
        print("Trend Analysis:")
        for month_year, sales_data in self.sales_history.items():
            total_sales_month = sum([amount for _, _, amount in sales_data])
            print(f"{month_year}: Total Sales - {total_sales_month}")

# Example Usage:
manager = SalesManager()
manager.add_sale("Brett", "H-4 Mahomes II", 8.10)
manager.add_sale("Joshua", "SS-26 DeVonta Smith", 0.22)
# Adding more sales for Product A

print("Total Sales:", manager.total_sales())
manager.sales_report()
manager.salesperson_report()
manager.trend_analysis()