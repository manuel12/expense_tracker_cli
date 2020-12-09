from datetime import datetime, timedelta
import random

class ExpenseListGenerator:
	"""Generates a list of random expenses."""

	def _generate_amount(self):
		return random.randint(1, 20)
		
	def _generate_contents(self):
		contents = [
		'meat', 'eggs', 'fruits', 'beer', 'bananas', 'cigarretes',
		'books', 'shoes', 'chicken', 'rice', 'clothes']
		num_contents = random.randint(1, 20)
		contents_to_return = set()
		for content in range(num_contents):
			contents_to_return.add(contents[random.randint(0, 10)])
		return contents_to_return

	def _generate_date(self):
		days_ago = random.randint(1, 14)
		date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d %H:%M')
		return date

	def _generate_source(self):
		sources = ['lidl', 'carrefour', 'decathlon', 'bar', 'restaurant']
		source = sources[random.randint(0, 4)]
		return source

	def generate(self, num_expenses):
		expense_list = []
		while len(expense_list) < num_expenses:
			expense = {
				"amount":self. _generate_amount(),
				"content": self._generate_contents(),	
				"date": self._generate_date(),
				"source": self._generate_source(),
			}
			expense_list.append(expense)
		return expense_list
			



elg = ExpenseListGenerator()
elg.generate(10)