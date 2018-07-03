from holistics import HolisticsAPI
import pandas as pd
import vcr
import requests
import pytest

my_vcr = vcr.VCR(
record_mode='once',
)

api_key_correct = 'api_key_correct'
report_id_correct = 'report_id_correct'
report_id_correct2 = 'report_id_correct2'
job_id_correct = 'job_id_correct'	

api_key_wrong = 'api_key_wrong'
path = 'path'
url = 'secure.holistics.io'
report_id_wrong = 'report_id_wrong'
job_id_wrong = 'job_id_wrong'
path_correct = 'output.csv'
path_wrong = 'C:/&^(@#,ga.tacv'
filters = {'twqdest': 'teqwdst'}

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_submit_export_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.submit_export(report_id_correct, filters)
	assert isinstance(response, str), "Result must be job_id (str)"
	
@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_submit_export_wrong():
	with pytest.raises(requests.exceptions.HTTPError):
		holistics_instance = HolisticsAPI(api_key_correct)
		holistics_instance.submit_export(report_id_wrong, filters)
	
@my_vcr.use_cassette('tests/vcr_cassettes/holistics_wrongapi.yml')
def test_submit_export_wrong2(): #test with wrong API
	with pytest.raises(requests.exceptions.HTTPError):
		holistics_instance = HolisticsAPI(api_key_wrong)
		holistics_instance.submit_export(report_id_correct2, filters)
	
@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_get_export_results_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.get_export_results(job_id_correct, 120, 120)
	assert response==1, "Result must be 1"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_get_export_results_wrong(): #not-exist job_id
	with pytest.raises((requests.exceptions.HTTPError,RuntimeError)):
		holistics_instance = HolisticsAPI(api_key_correct)
		holistics_instance.get_export_results(job_id_wrong, 120, 120)
	
@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_download_results_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.download_results(job_id_correct, path_correct)
	assert isinstance(response, pd.DataFrame), "Result must be DataFrame object"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_download_results_wrong(): #not-exist job_id
	with pytest.raises((requests.exceptions.HTTPError,pd.errors.ParserError)):
		holistics_instance = HolisticsAPI(api_key_correct)
		holistics_instance.download_results(job_id_wrong, path_wrong)
		
@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_export_data_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.export_data(report_id_correct2,filters=filters)
	assert isinstance(response, pd.DataFrame), "Result must be DataFrame object"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_export_data_wrong(): #not-exist report_id
	with pytest.raises((requests.exceptions.HTTPError, RuntimeError, pd.errors.ParserError)):
		holistics_instance = HolisticsAPI(api_key_correct)
		holistics_instance.export_data(report_id_wrong,filters=filters)