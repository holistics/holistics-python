Holistics module: export data easier
=========================
This module is made to help python user export data from QueryReport of Holistics.io, save as DataFrame object or .CSV file

A simple way to use Holistics API

```
from holistics import HolisticsAPI

result = HolisticsAPI(api_key='Uf6aeraergFkV147Dmkrergga4EMLU2xhD17JDF13jM=')
result.ExportData(report_id='3123574', path='C:/output.csv')
```

# Requirement
- Python's version: >= 3

# Installation
Module can be installed with pip:
```
$ pip install holistics
```
Alternatively, you can grab the latest source code from [GitHub](https://github.com/holistics/holistics-python):
```
$ git clone git clone git://github.com/holistics/holistics-python.git
$ python setup.py install
```

# Documentation
## **1. Import module**
```
from holistics import HolisticsAPI
```  

## **2. Initalize HolisticsAPI class:**  
**HolisticsAPI(api_key, url)**
```
obj = HolisticsAPI(api_key = 'aerg454hoiaKJGlgku', url = 'demo.holistics.io')
```
- **api-key (str):** API-key of your Holistics's user. 
    - [How to get API-key](https://docs.holistics.io/api/)
- **url (str) (optional):** Chang to other Holistics domain if you aren't using https://secure.holistics.io.  
    - Ex: https://demo.holistics.io   

## **3. Export data:**
**ExportData (report_id, filter_dict, _page_size, _page)**  
```
    my_dataframe = obj.ExportData(report_id='331235', filter_dict={'date': '2017-04-28'}, 
                                  path = 'C:/output.csv', _page_size = 12, _page = 5)
```  
    
- **report_id (str):** id of report. Collect from URL.  
    - Ex: https://secure.holistics.io/queries/12345-processing-report (12345)
- **filter_dict (dict) (optional):** dictionary of filters that would be applied to report.  
    - Ex: {
            'tenant': 'holistics',
            'date': '2017-04-28'
        }
- **path (str) (optional):** If you want to store export data to file, set path variable.  
    - Ex: D:/Data/output.csv
- **_page_size (int) (optional):** Set the page size of the response.  
    - Default value: 10000000
- **_page (int) (optional):** Set the page number of data to fetch.  
    - Default value: 10000000
