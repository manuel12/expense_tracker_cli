from pprint import pprint as p
import util
from input import get_user_input
from expense import create_expense
from expense_counter import ExpenseCounter

expense_file = "expenses.json"

class ExpenseTracker:

  def __init__(self, expense_file):
    self.expenses_file = expense_file
    self.expenses = []
    if util.file_exists(self.expenses_file):
      self.expenses = util.read_from_json(self.expenses_file)

  def track_expense(self):
    expense = create_expense(get_user_input())
    self.expenses.append(expense.serialize())
    util.write_to_json(self.expenses_file, self.expenses)
    self.print_expense_table()

  def get_expenses(self):
  	return self.expenses

  def print_expense_table(self, sorting_key, reverse=False):
    self.expenses = util.read_from_json(self.expenses_file)

    template = "{0:6}|{1:10}|{2:10}|{3:7}"
    print(template.format("AMOUNT", "CONTENT", "SOURCE", "DATE"))

    sorted_expenses = sorted(self.expenses, key=lambda e: e[sorting_key], 
      reverse=reverse)
    for e in sorted_expenses:
      print(template.format(e['amount'], e['content'], e['source'], e['date']))
    print()

    ec = ExpenseCounter(self.get_expenses())

    template = "{0: <23}  {1: >6}"
    print(template.format("DATA", "RESULT"))
    print(template.format("Total expenses:", ec.get_total_amount())) 
    print(template.format("Highest expense:", ec.get_highest_amount()))  
    print(template.format("Lowest expense:", ec.get_lowest_amount())) 
    print(template.format("Average expense amount:", ec.get_average_amount())) 

    print(template.format("Total expenses this week:", ec.get_total_weekly_amount())) 
    print(template.format("Average expense this week:", ec.get_average_weekly_amount())) 


et = ExpenseTracker(expense_file)
ec = ExpenseCounter(et.get_expenses())

print(ec.get_total_weekly_amount())
print(ec.get_average_weekly_amount())


