
import json

import os

from datetime import date



PERSISTED_DATA_FOLDER_NAME='data'


def get_list_of_vacancies_from_presistenct_source():
	file_names = os.listdir(PERSISTED_DATA_FOLDER_NAME)


	result_list_vacancies=[]

	for file_name in file_names:

		with open(PERSISTED_DATA_FOLDER_NAME+'/'+file_name, 'r') as json_reader:
			json_vacacncies=json_reader.read()

			list_of_vacancies=json_vacacncies.split(";")

			for vacancy_json in list_of_vacancies[:-1]:
					
				vacancy_obj = json.loads(vacancy_json);

				result_list_vacancies.append(vacancy_obj)

	return result_list_vacancies
	

if __name__ == '__main__':
	print(get_list_of_vacancies_from_presistenct_source())
