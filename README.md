Required libraries:
import io
import requests
import pandas as pd

api_python (key, report_id, filter_dict, path, _page_size, _page)
Execute report and then export data into dataframe object or save as .csv file

key: api-key of Holistics, need permission to be generated. Get key at Settings -> My Account
report_id: id of report. Collect from URL. 
Ex: https://secure.holistics.io/queries/12345-processing-report
filter_dict (optional): dictionary of filters that would be applied to report
path (optional):
	Set path if want to store .csv file (direction + filename)
	Default value: None
_page_size (optional): set the page size of the response
	Default value: 10000000
_page (optional): set the page number of data to fetch
	Default value: 10000000

