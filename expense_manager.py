import datetime

class ExpenseManager:
	
	def __init__(self, expenses):
		self.expenses = expenses

	def print_dates(self):
		for expense in self.expenses:
			print(expense["date"])

	def modify_date_format(self):
		for expense in self.expenses:
			date = datetime.datetime.strptime(expense["date"], "%Y-%m-%d %H:%M:%S.%f")			
			modified_date = date.strftime("%Y-%m-%d %H:%M")
			expense["date"] = modified_date
		return self.expenses

	def replace_type_with_source(self):
		sources = []
		for expense in self.expenses:
			expense["source"] = expense["type"]
			del expense["type"]
		return self.expenses