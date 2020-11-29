from jobs_ge_parser import get_parsed_vacanies

import json

from datetime import date

PERSISTED_DATA_FOLDER_NAME='data'

def persist_parsed_jobs_into_local_file():
	
	vacancies = get_parsed_vacanies()

	with open(PERSISTED_DATA_FOLDER_NAME+'/'+str(date.today())+'.txt', 'w') as outfile:
		
		for vacancy in vacancies:
			
			json_value_of_vacancy=json.dumps(vacancy.__dict__);
			outfile.write(json_value_of_vacancy+';')


			
### Main part
if __name__ == "__main__":
		
	persist_parsed_jobs_into_local_file();
	
