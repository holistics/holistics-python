# Python Library for Holistics API

Our package ([**Holistics Package for Python**](https://github.com/holistics/holistics-python)) allow Python's user export report's data by inputting:
- Your API-key
- Report's ID
- Dictionary of filters applied to that report
<br>

# **Installation**
Package can be installed with `pip`:
```
pip install holistics
```
Alternatively, you can grab the latest source code from GitHub:
```
git clone git clone git://github.com/holistics/holistics-python.git
python setup.py install
```
<br>

# **How to export data**
Beginning by import holistics package
```
from holistics import HolisticsAPI
```  
<br>

Next, creating an object of HolisticsAPI class with your API-key and Holistics server's url
```
obj = HolisticsAPI(api_key = 'aerg454hoiaKJGlgku', url = 'demo.holistics.io')
```
**Args:**
- `api_key` **(str): **Your account's API-key. 
    - [How to generate API-key](https://docs.holistics.io/api/)
- `url` **(str) (optional):** URL of your Holistics server 
    - Default value: 'https://secure.holistics.io'
    
<br>

Finally, call export_data function with specific syntax:
<br>&emsp; &emsp; **export_data (report_id, path, filter_dict, _page_size, _page)**  
```
my_dataframe = obj.export_data(report_id='123456', path='C:/output.csv', 
                              filter_dict={'date': '2017-04-28', 'vat': 1.1}, 
                              _page_size = 12, _page = 5)
```  
**Args:**
- `report_id` **(str):** ID of report. Get from URL.  
    - Ex: https://secure.holistics.io/queries/12345-processing-report (12345)
- `path` **(str) (optional):** If you want to store export data to local path, set path variable.  
    - Default value: None
    - Ex: 'D:/Data/output.csv'
- `filter_dict` **(dict) (optional):** dictionary of filters that would be applied to report.  
    - Default value: None
    - Ex: {'tenant': 'holistics', 'date': '2017-04-28'}
- `_page_size` **(int) (optional):** Set the page size of the response.  
    - Default value: 10000000
- `_page` **(int) (optional):** Set the page number of data to fetch.  
    - Default value: 10000000

## **Return:**
A DataFrame object. If `path` is not None, save object as .csv file at that path.

## **Raises:**
- `HTTPError`: If the program can't connect to target site and get data. 
   - You should check your API-key, url of holistics and internect connection.
- `RuntimeError`: If return status is Failure. 
   - It could be caused by wrong SQL of your QueryReport.
- `ParserError`: If program can't parse downloaded data as DataFrame object. 
   - It could be caused when downloaded data is None.
