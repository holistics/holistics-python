Holistics package: export data easier
=========================
This package is made to help Python user export report data from Holistics.io, save as DataFrame object or .CSV file without manually log in.

# Requirement
- Python's version: >= 3

# Installation
Package can be installed with pip:
```
$ pip install holistics
```
Alternatively, you can grab the latest source code from [GitHub](https://github.com/holistics/holistics-python):
```
$ git clone git clone git://github.com/holistics/holistics-python.git
$ python setup.py install
```

# Documentation
## **1. Import package**
```
from holistics import HolisticsAPI
```  

## **2. Create an object of HolisticsAPI class:**  
**HolisticsAPI(api_key, url)**
```
obj = HolisticsAPI(api_key = 'aerg454hoiaKJGlgku', url = 'demo.holistics.io')
```
- **api-key (str):** API-key of your Holistic acount. 
    - [How to get API-key](https://docs.holistics.io/api/)
- **url (str) (optional):** Chang to other Holistics domain if you aren't using https://secure.holistics.io.  
    - Ex: https://demo.holistics.io   

## **3. Export data:**
**export_data (report_id, path, filter_dict, _page_size, _page)**  
```
    my_dataframe = obj.export_data(report_id='123456', path='C:/output.csv', 
                                filter_dict={'date': '2017-04-28', 'vat': 1.1}, _page_size = 12, _page = 5)
```  
    
- **report_id (str):** id of report. Collect from URL.  
    - Ex: https://secure.holistics.io/queries/12345-processing-report (12345)
- **path (str) (optional):** If you want to store export data to file, set path variable.  
    - Default value: None
    - Ex: D:/Data/output.csv
- **filter_dict (dict) (optional):** dictionary of filters that would be applied to report.  
    - Default value: None
    - Ex: {
            'tenant': 'holistics',
            'date': '2017-04-28'
        }
- **_page_size (int) (optional):** Set the page size of the response.  
    - Default value: 10000000
- **_page (int) (optional):** Set the page number of data to fetch.  
    - Default value: 10000000
