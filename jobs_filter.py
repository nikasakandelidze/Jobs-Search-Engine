

def is_vacancy_valid_according_to_filter_word(filter_words, vacancy):
	for filter_word in filter_words:
		if filter_word in vacancy['description'].lower() or filter_word in vacancy['company'].lower() or filter_word in vacancy['startDate'].lower() or filter_word in vacancy['endDate'].lower() or filter_word in vacancy['link'].lower():
			return True
	return False

def get_filtered_list_of_jobs(filter_words, list_of_vacancies):
	result_list = []
	for vacancy in list_of_vacancies:
		if is_vacancy_valid_according_to_filter_word(filter_words, vacancy):
			result_list.append(vacancy)
	return result_list

if __name__ == "__main__":
	isValid = is_vacancy_valid_according_to_filter_word(['a'],{'link':'a', 'description':'w','company':'w','startDate':'s','endDate':'ss'})	
	
