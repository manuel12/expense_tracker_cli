import datetime

class Expense:
	def __init__(self, amount, content, source, date):
		self.amount = amount
		self.content = content
		self.source = source
		self.date = date

	def serialize(self):
		return {
			"amount": self.amount,
			"content": self.content,
			"source": self.source,
			"date": self.date,
		}

def create_expense(data):
	return Expense(
		data["amount"],
		data["content"],
		data["source"],
		data["date"]
	)

