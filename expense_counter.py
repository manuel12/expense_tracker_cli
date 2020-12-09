import datetime
import util
from expense_generator import ExpenseListGenerator

class ExpenseCounter:
	
	def __init__(self, expenses):
		self.expenses = expenses

	def get_highest_amount(self):
		highest_expense = sorted(self.expenses, key=lambda l: l["amount"], 
			reverse=True)[0]
		return highest_expense["amount"]

	def get_lowest_amount(self):
		lowest_expense = sorted(self.expenses, key=lambda l: l["amount"], 
			reverse=False)[0]
		lowest_amount = lowest_expense["amount"]
		return lowest_amount

	def get_average_amount(self):
		return round(sum([expense["amount"] for expense in self.expenses]) \
		 / len(self.expenses), 2)

	def get_total_amount(self):
		return sum([expense["amount"] for expense in self.expenses])

	def get_expenses_by_week_num(self, week_num):
		expenses_by_week = []
		for expense in self.expenses:
			date_obj = util.convert_date_str_to_date_obj(expense['date'])
			current_expense_week_num = int(
				util.get_week_num_from_date(date_obj)) + 1
			if current_expense_week_num == week_num:
				expenses_by_week.append(expense)
		return expenses_by_week
