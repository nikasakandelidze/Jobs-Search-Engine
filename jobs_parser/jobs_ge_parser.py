from bs4 import BeautifulSoup
import requests
'''
	This file at the moment parses only one arbitrary web page of vacancies
'''

WEB_PAGE_LINK="https://jobs.ge/?page=1&q=&cid=6&lid=&jid="

WEB_PAGE_DOMAIN_NAME="jobs.ge"

# Actual Vacany class, it's object are entites of actual active vacancies
class Vacancy:
    def __init__(self,description,company,startDate,endDate,link):
        self.description = description
        self.company = company
        self.startDate=startDate
        self.endDate=endDate
        self.link=link


'''
	initialise BeautifulSoup Object
'''
def initialise_beautiful_soup_for_current_webpage(link):
    web_page_result = requests.get(link)
    return BeautifulSoup(web_page_result.content, "html.parser")

#this function takes table row as an input parameter and returns container of useful texts from vacancy
def get_current_vacancy_as_list_of_its_fields(tr) :
    container = []
    for td in tr.findAll('td'):
        vacancyInfoText= td.text.replace("\n", "").replace("\t", "")
        if vacancyInfoText : container.append(vacancyInfoText)
    return container

'''
Get list of full vacancies links
'''
def get_links_of_vacancies(document_of_jobs_on_webpage):

    result_links = []
    
    links_of_anchor_tag_nodes = document_of_jobs_on_webpage.findAll('a',class_="vip",href=True)
    
    for anchor_node in links_of_anchor_tag_nodes:

        if anchor_node: result_links.append( WEB_PAGE_DOMAIN_NAME + anchor_node['href'] )

    return result_links

'''
	Parse jobs results into list
'''
def parse_job_reuslts_from_document(document_of_jobs_on_webpage):

    job_results = []
    
    links = get_links_of_vacancies(document_of_jobs_on_webpage)
    
    current_link_index=0
    
    for tr in document_of_jobs_on_webpage.findAll('tr'):
    
        current_job_as_list_of_fields=get_current_vacancy_as_list_of_its_fields(tr)
    
        if current_job_as_list_of_fields :
    
            job_results.append(Vacancy(current_job_as_list_of_fields[0],
            	current_job_as_list_of_fields[1],
            	current_job_as_list_of_fields[2],
            	current_job_as_list_of_fields[3],
            	str(links[current_link_index])))
    
            current_link_index+=1
    
    return job_results


def get_parsed_vacanies():
	document_of_webpage = initialise_beautiful_soup_for_current_webpage(WEB_PAGE_LINK)

	#in find(...) method parameters are hardcoded by exploring html src code of jobs.ge 
	document_of_jobs_on_webpage = document_of_webpage.find("table", {"id": "job_list_table"})

	return parse_job_reuslts_from_document(document_of_jobs_on_webpage)

### Main part
if __name__ == "__main__":
	list_of_parsed_vacancies = get_parsed_vacanies()
    
       
	