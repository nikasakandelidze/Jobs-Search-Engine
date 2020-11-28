from jobs_ge_parser import get_parsed_vacanies

import json

from datetime import date

vacancies = get_parsed_vacanies()

def persist_parsed_jobs_into_local_file():
	
	with open(str(date.today())+'.txt', 'w') as outfile:
		for vacancy in vacancies:
			
			vacancy_json = json.dumps(vacancy.__dict__)
			
			outfile.write(vacancy_json)
		

### Main part
if __name__ == "__main__":
		
	persist_parsed_jobs_into_local_file();
	
