import datetime
import util

questions = {
	'amount': "Please enter the amount of your expense: ",
	'content': "Please enter the content of your expense: ",
	'source': "Please enter the source of your expense: ",
	'date': """Please enter the date of your expense (format: YYYY-MM-DD HH:MM)
	or just press ENTER to use the current date: """
}



invalid_input_msgs = {
	"amount": "Your input is invalid, please enter a valid number!",
	"content_or_type": "Your input is invalid or empty, please enter a valid input!"
}

def get_user_input():
	input_dict = {}
	for question_key, question in questions.items():
		while True:
			user_input = input(''.join(question))
			validated_input = validate(question, user_input)

			if validated_input:
				input_dict[question_key] = validated_input
				break
	return input_dict

def validate(question, input):
	if "amount" in question:
		input_validated = validate_amount(input)
	elif "date" in question:
		input_validated = validate_date(input)
	else:
		input_validated = validate_content_or_source(input)
	return input_validated

def validate_date(date): 
	date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
	if str(date) == "":
		print("Using current date: %s"  % (date_now))
		return date_now
	else:
		date = util.convert_date_str_to_date_obj(date)
		return date

def validate_amount(amount):
	if util.is_num(amount) == True:
		return util.get_num_from_str(amount)
	print_error_and_fail('amount')

def validate_content_or_source(input):
	if not util.is_empty(input):
		return input.lower()
	print_error_and_fail('content_or_source')

def print_error_and_fail(question_key):
	print(invalid_input_msgs[question_key])
	return False
