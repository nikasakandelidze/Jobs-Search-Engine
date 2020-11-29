
from jobs_filter import get_filtered_list_of_jobs

from jobs_reader import get_list_of_vacancies_from_presistenct_source


def get_links_of_vacancies_as_concated_string(list_of_vacancies):
	result_string=''
	for vacancy in list_of_vacancies:
		result_string+=vacancy['company'] + " : "+vacancy['link']+'\n\n'
	return result_string

def generate_response_depending_on_input(input):
	result_string=''
	if 'front' in input or 'frontend' in input or 'front-end' in input or 'javascript' in input or 'JavaScript' in input or 'Java-Script' in input or 'java-script' in input or 'Java Script' in input or 'java script' in input:
		list_of_vacancies=get_list_of_vacancies_from_presistenct_source()
		result_list = get_filtered_list_of_jobs(['javascript','react','vue','angular','html','markup','css'],list_of_vacancies)	
		result_string=get_links_of_vacancies_as_concated_string(result_list)
	elif 'Java' in input or 'java' in input:
		list_of_vacancies=get_list_of_vacancies_from_presistenct_source()
		result_list = get_filtered_list_of_jobs(['java'],list_of_vacancies)	
		result_string=get_links_of_vacancies_as_concated_string(result_list)
	elif 'Python' in input or 'python' in input:
		list_of_vacancies=get_list_of_vacancies_from_presistenct_source()
		result_list = get_filtered_list_of_jobs(['python'],list_of_vacancies)	
		result_string=get_links_of_vacancies_as_concated_string(result_list)

	return result_string

if __name__=='__main__':
	res = generate_response_depending_on_input('java')
	print(res)