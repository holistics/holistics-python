from holistics import HolisticsAPI
import pandas as pd
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
def test_submit_export_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.submit_export(report_id_correct, filters)
	assert response == 1, "Response should return string of job_id"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_submit_export_wrong():
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.submit_export(report_id_wrong, filters)
	assert isinstance(response, requests.exceptions.HTTPError), "Response should return HTTPError"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics_wrongapi.yml')
def test_submit_export_wrong2(): #test with wrong API
	holistics_instance = HolisticsAPI(api_key_wrong)
	response = holistics_instance.submit_export(report_id_correct, filters)
	assert isinstance(response, requests.exceptions.HTTPError), "Response should return HTTPError"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_get_export_results_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.get_export_results(job_id_correct, 120, 120)
	assert response == 1, "Response must be 1"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_get_export_results_wrong(): #not-exist job_id
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.get_export_results(job_id_wrong, 120, 120)
	assert isinstance(response, (requests.exceptions.HTTPError, ValueError)), "Response must be != 1 (0 or HTTPError)"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_download_results_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	holistics_instance.page['job_id'] = job_id_correct
	response = holistics_instance.download_results(path_correct)
	assert isinstance(response, pd.DataFrame), "Response should return dataFrame or 1"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_download_results_wrong(): #not-exist job_id
	holistics_instance = HolisticsAPI(api_key_correct)
	holistics_instance.page['job_id'] = job_id_wrong
	response = holistics_instance.download_results(path_wrong)
	assert isinstance(response, (requests.exceptions.HTTPError, pd.errors.ParserError)), "Response should return HTTPError"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_export_data_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.export_data(report_id_correct,filters)
	assert isinstance(response, pd.DataFrame), "Response must be != 0"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_export_data_wrong(): #not-exist report_id
	holistics_instance = HolisticsAPI(api_key_correct)
	print (holistics_instance.page)
	response = holistics_instance.export_data(report_id_wrong,filters)
	assert response == 0, "Response must be 0"

