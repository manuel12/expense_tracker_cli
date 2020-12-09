import os
import json
import datetime

def is_num(input):
  try:
    input = int(input)
    return True
  except ValueError:
    try:
      input = float(input)
      return True
    except ValueError:
      return False

def get_num_from_str(str):
  try:
    num = int(str)
    return num
  except ValueError:
    try:
      num = float(str)
      return num
    except ValueError:
      return False

def is_empty(input):
  return str(input).isspace()

def file_exists(file):
  if os.path.exists(file):
      return True
  else:
      return False

def read_from_json(file):
  try:
    with open(file, 'r') as f:
      data = json.load(f)
      return data
  except IOError as e:
    print(e)
    write_to_file(file, '[]')
    return False

def write_to_json(file, data):
  try:
    with open(file, 'w+') as f:
      json.dump(data, f, sort_keys=True, indent=4)
  except IOError as e:
    print(e)
    return False

def check_json_file_contains_data(data, file):
  data_from_file = read_from_json(file)
  if data in data_from_file:
    print("Data found as: %s" % (data))
    return True
  else:
    return False 

def sort_obj_list_by_key(list_, key, rev=False):
  return sorted(list_, key=lambda l: l[key], reverse=rev)

def convert_date_str_to_date_obj(string, format='%Y-%m-%d %H:%M'):
  try:
    date_obj = datetime.datetime.strptime(string, format)
    return date_obj
  except Exception as e:
    print(e)
    return False

def get_week_num_from_date(date):
  return date.strftime("%U")

def get_expenses_by_week(expense_list, week_num):
  week_expenses = []
  for expense in expense_list:
    date = convert_date_str_to_date_obj(expense['date'])
    expense_week = int(get_week_num_from_date(date))
    if(expense_week == week_num):
      week_expenses.append(expense)
  return week_expenses

def get_total_amount_of_expenses(expense_list):
  total_expenses = 0
  for expense in expense_list:
    total_expenses += int(expense['amount'])
  return  total_expenses

def get_highest_expense_amount(expense_list):
  amounts = []
  for expense in expense_list:
    amounts.append(int(expense['amount']))
  return max(amounts)

def update_obj_keys_from_list(list_, key, func):
  for item in list_:
    item[key] = func(item[key])
  return list_


