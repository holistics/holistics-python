Holistics Python API - Export data from QueryReport
=========================
This API is made to help user export data from QueryReport of Holistics.io, save as DataFrame object or .CSV file

How to use:
```
    import holistics_python_api
    
    api = holistics_api()
    result = api.export_data('34hpF2d2cQwu7jdQlzpKuMUGVb+ZkDwhW1kZvX9gsgw=', '12345')
```


Requirements
---------------
- Python version 3
- Libraries:
  - requests: 
  - pandas: 
```
    $ pip install requests
    $ pip install pandas
```


Installing
---------------
holistics_python_api can be installed with pip:
```
    $ pip install holistics_python_api
```
Alternatively, you can grab the latest source code from [GitHub](https://github.com/holistics/holistics-python):
```
    $ git clone git clone git://github.com/holistics/holistics-python.git
    $ python setup.py install
```

Documentation
---------------
**api_python (key, report_id, filter_dict, path, _page_size, _page)**

- **key:** api-key of Holistics, need permission to be generated. Get key at Settings -> My Account
- **report_id:** id of report. Collect from URL. 
    Ex: https://secure.holistics.io/queries/12345-processing-report
- **filter_dict (optional):** dictionary of filters that would be applied to report
- **path (optional):**
  - Set path if want to store .csv file (direction + filename)
  - Default value: None
- **_page_size (optional):** set the page size of the response
  - Default value: 10000000
- **_page (optional):** set the page number of data to fetch
   -Default value: 10000000
