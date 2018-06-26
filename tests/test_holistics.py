from holistics import HolisticsAPI
import pandas as pd
from pytest import fixture
import vcr

my_vcr = vcr.VCR(
record_mode='once',
)
api_key_correct = 'Uf6a7qsFkV147Dmkrcqq+msHa4EMLU2xhD17JDF13jM='
api_key_wrong = '123556`41'
path = 'output'
url = 'secure.holistics.io'
report_id_correct = '34412'
report_id_wrong = 'aehnaga'
job_id_correct = '19763907'
job_id_wrong = 'eargaerg'
path_correct = 'output.csv'
path_wrong = 'C:/&^(@#,ga.tacv'
filters = {'twqdest': 'teqwdst'}

def test_holistics_info():
	holistics_instance = HolisticsAPI(api_key_correct,path,url)
	response = holistics_instance.info()
	assert isinstance(response, dict)
	assert response['api_key'] == api_key_correct, "The api_key should be in the response"
	assert response['path'] == path, "The path should be in the response"
	assert response['url'] == url, "The url should be in the response"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_GetURL_correct(): #correct, exist url
	tail_url = '/queries/'+str(report_id_correct)+'/submit_export.csv'
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.GetURL(tail_url)
	assert response.status_code == 200, "Status code should be 200"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_GetURL_wrong(): #wrong, non-exist url (wrong report_id)
	tail_url = '/queries/'+str(report_id_wrong)+'/submit_export.csv'
	holistics_instance = HolisticsAPI(api_key_wrong)
	response = holistics_instance.GetURL(tail_url, filters)
	assert response == 0, "Response must be error (return 0)"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_SubmitReport_correct():
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.SubmitReport(report_id_correct, filters)
	assert response == 1, "job_id must be generated"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_SubmitReport_wrong():
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.SubmitReport(report_id_wrong, filters)
	assert response == 0, "Response must be error"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_GetExportResults_correct():
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.GetExportResults(job_id_correct, 120, 120)
	assert response == 1, "Response must be 1"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_GetExportResults_wrong():
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.GetExportResults(job_id_wrong, 120, 120)
	assert response == 0, "Response must be 0"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_DownloadResults_correct():
	holistics_instance = HolisticsAPI(api_key_correct,path)
	holistics_instance.page['job_id'] = '19763834'
	response = holistics_instance.DownloadResults()
	assert holistics_instance.data == True, "Response must be 1 or DataFrame object"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_DownloadResults_wrong():
	holistics_instance = HolisticsAPI(api_key_correct,path=path_wrong)
	holistics_instance.page['job_id'] = 'iaujhlfawef'
	response = holistics_instance.DownloadResults()
	assert response is None or response == 0, "Response must be 0"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_ExportData_correct():
	holistics_instance = HolisticsAPI(api_key_correct)
	response = holistics_instance.ExportData(report_id_correct,filters)
	assert holistics_instance.data == True, "Response must be 1 or DataFrame object"

@my_vcr.use_cassette('tests/vcr_cassettes/holistics.yml')
def test_ExportData_wrong():
	holistics_instance = HolisticsAPI(api_key_correct,path=path_correct)
	response = holistics_instance.ExportData(report_id_wrong,filters)
	assert response is None or response == 0, "Response must be 0"

