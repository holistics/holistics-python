from holistics import HolisticsAPI
import pandas as pd
import vcr
import requests
import pytest

my_vcr = vcr.VCR(
record_mode='once',
)

api_key_correct = '+msHa4EMLU2xhD17JDF13jM='
api_key_wrong = '123556`41'
path = 'output'
url = 'secure.holistics.io'
report_id_correct = '33874'
report_id_correct2 = '34412'
report_id_wrong = 'aehnaga'
job_id_correct = '19888412'	
job_id_wrong = 'eargaerg'
path_correct = 'output.csv'
path_wrong = 'C:/&^(@#,ga.tacv'
filters = {'twqdest': 'teqwdst'}

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_submit_export_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	holistics_instance.submit_export(report_id_correct, filters)
	
@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_submit_export_wrong():
	with pytest.raises(requests.exceptions.HTTPError):
		holistics_instance = HolisticsAPI(api_key_correct)
		holistics_instance.submit_export(report_id_wrong, filters)
	
@my_vcr.use_cassette('tests/vcr_cassettes/holistics_wrongapi.yml')
def test_submit_export_wrong2(): #test with wrong API
	with pytest.raises(requests.exceptions.HTTPError):
		holistics_instance = HolisticsAPI(api_key_wrong)
		holistics_instance.submit_export(report_id_correct, filters)
	
@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_get_export_results_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	holistics_instance.get_export_results(job_id_correct, 120, 120)
	
@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_get_export_results_wrong(): #not-exist job_id
	with pytest.raises((requests.exceptions.HTTPError,RuntimeError)):
		holistics_instance = HolisticsAPI(api_key_correct)
		holistics_instance.get_export_results(job_id_wrong, 120, 120)
	
@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_download_results_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	holistics_instance.page['job_id'] = job_id_correct
	holistics_instance.download_results(path_correct)
	
@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_download_results_wrong(): #not-exist job_id
	with pytest.raises((requests.exceptions.HTTPError,pd.errors.ParserError)):
		holistics_instance = HolisticsAPI(api_key_correct)
		holistics_instance.page['job_id'] = job_id_wrong
		holistics_instance.download_results(path_wrong)
		
@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_export_data_correct(): #all correct
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.export_data(report_id_correct2,filters=filters)
	assert isinstance(response, pd.DataFrame), "Result must be DataFrame obj"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_export_data_wrong(): #not-exist report_id
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.export_data(report_id_wrong,filters=filters)
	assert response == 0, "Wrong input must return 0"