

def is_vacancy_valid_according_to_filter_word(filter_word, vacancy):
	return  filter_word in vacancy['description'].lower() or filter_word in vacancy['company'].lower() or filter_word in vacancy['startDate'].lower() or filter_word in vacancy['endDate'].lower() or filter_word in vacancy['link'].lower()

def get_filtered_list_of_jobs(filter_word, list_of_vacancies):
	result_list = []
	for vacancy in list_of_vacancies:
		if is_vacancy_valid_according_to_filter_word(filter_word, vacancy):
			result_list.append(vacany)
	return result_list

if __name__ == "__main__":
	isValid = is_vacancy_valid_according_to_filter_word('a',{'link':'a', 'description':'w','company':'w','startDate':'s','endDate':'ss'})	
	
