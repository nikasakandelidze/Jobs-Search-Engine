
from jobs_filter import get_filtered_list_of_jobs

from jobs_reader import get_list_of_vacancies_from_presistenct_source


def get_links_of_vacancies_as_concated_string(list_of_vacancies):
	result_string=''
	for vacancy in list_of_vacancies:
		result_string+=vacancy['company'] + " : "+vacancy['link']+'\n'
	return result_string

def generate_response_depending_on_input(input):
	result_string=''
	if 'Java' in input or 'java' in input:
		list_of_vacancies=get_list_of_vacancies_from_presistenct_source()
		result_list = get_filtered_list_of_jobs(['java','Java'],list_of_vacancies)	
		result_string=get_links_of_vacancies_as_concated_string(result_list)
	elif 'Python' in input or 'python' in input:
		list_of_vacancies=get_list_of_vacancies_from_presistenct_source()
		result_list = get_filtered_list_of_jobs(['python','Python'],list_of_vacancies)	
		result_string=get_links_of_vacancies_as_concated_string(result_list)
	
	return result_string

if __name__=='__main__':
	res = generate_response_depending_on_input('java')
	print(res)