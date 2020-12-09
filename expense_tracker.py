from pprint import pprint as p
import util
from input import get_user_input
from expense import create_expense
from expense_counter import ExpenseCounter

expense_file = "expenses.json"

class ExpenseTracker:

	def __init__(self, expense_file):
		self.expenses_file = expense_file
		self.local_expenses = []
		if util.file_exists(self.expenses_file):
			self.local_expenses = util.read_from_json(self.expenses_file)

	def track_expense(self):
		expense = create_expense(get_user_input())
		self.local_expenses.append(expense.serialize())
		util.write_to_json(self.expenses_file, self.local_expenses)
		self.print_expense_table()

	def print_expense_table(self, sorting_key, reverse=False):
		self.local_expenses = util.read_from_json(self.expenses_file)
		
		template = "{0:6}|{1:10}|{2:10}|{3:7}"
		print(template.format("AMOUNT", "CONTENT", "SOURCE", "DATE"))

		sorted_expenses = sorted(self.local_expenses, key=lambda e: e[sorting_key], 
			reverse=reverse)
		for e in sorted_expenses:
		  print(template.format(e['amount'], e['content'], e['source'], e['date']))
		print()

		ec = ExpenseCounter(self.local_expenses)
		template = "{0: <23}  {1: >6}"
		print(template.format("DATA", "RESULT"))
		print(template.format("Total expenses:", ec.get_total_amount())) 
		print(template.format("Highest expense:", ec.get_highest_amount())) 
		print(template.format("Lowest expense:", ec.get_lowest_amount())) 
		print(template.format("Average expense amount:", ec.get_average_amount())) 


et = ExpenseTracker(expense_file)
et.print_expense_table('amount')


