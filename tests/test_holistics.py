from holistics import HolisticsAPI
import pandas
import vcr
import requests

my_vcr = vcr.VCR(
record_mode='once',
)

api_key_correct = 'Uf6a7qsFkV147Dmkrcqq+msHa4EMLU2xhD17JDF13jM='
api_key_wrong = '123556`41'
path = 'output'
url = 'secure.holistics.io'
report_id_correct = '33874'
report_id_wrong = 'aehnaga'
job_id_correct = '19888412'
job_id_wrong = 'eargaerg'
path_correct = 'output.csv'
path_wrong = 'C:/&^(@#,ga.tacv'
filters = {'twqdest': 'teqwdst'}

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_SubmitReport_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.submit_report(report_id_correct, filters)
	assert type(response) == str, "Response should return string of job_id"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_SubmitReport_wrong():
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.submit_report(report_id_wrong, filters)
	assert type(response) == requests.exceptions.HTTPError, "Response should return HTTPError"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics_wrongapi.yml')
def test_SubmitReport_wrong2(): #test with wrong API
	holistics_instance = HolisticsAPI(api_key_wrong)
	response = holistics_instance.submit_report(report_id_correct, filters)
	assert type(response) == requests.exceptions.HTTPError, "Response should return HTTPError"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_GetExportResults_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.get_export_result(job_id_correct, 120, 120)
	assert response == 1, "Response must be 1"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_GetExportResults_wrong(): #not-exist job_id
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.get_export_result(job_id_wrong, 120, 120)
	assert response != 1, "Response must be != 1 (0 or HTTPError)"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_DownloadResults_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct,path)
	holistics_instance.page['job_id'] = job_id_correct
	response = holistics_instance.download_results()
	assert type(response) != requests.exceptions.HTTPError, "Response should return dataFrame or 1"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_DownloadResults_wrong(): #not-exist job_id
	holistics_instance = HolisticsAPI(api_key_correct,path=path_wrong)
	holistics_instance.page['job_id'] = job_id_wrong
	response = holistics_instance.download_results()
	assert type(response) == requests.exceptions.HTTPError, "Response should return HTTPError"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_ExportData_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.export_data(report_id_correct,filters)
	assert type(response) == int or type(response) == pandas.core.frame.DataFrame, "Response must be != 0"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_ExportData_wrong(): #not-exist report_id
	holistics_instance = HolisticsAPI(api_key_correct,path=path_correct)
	response = holistics_instance.export_data(report_id_wrong,filters)
	assert response == 0, "Response must be 0"

