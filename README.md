Holistics module: export data more easier
=========================
This Module is made to help python user export data from QueryReport of Holistics.io, save as DataFrame object or .CSV file

A simple way to use Holistics API

```
from holistics import HolisticsAPI

api_key = 'Uf6aeraergFkV147Dmkrergga4EMLU2xhD17JDF13jM='
path = 'C:/output.csv'
report_id = '3123574'

result = HolisticsAPI('Uf6aeraergFkV147Dmkrergga4EMLU2xhD17JDF13jM=',path='C:/output.csv')
result.ExportData('3123574')
    
#Each user's account has one unique API key. 
#API key is generated at Setting -> My Account, require permission of administators.
```

Requirement
---------------
- Python's version: >= 3

Installation
---------------
Module can be installed with pip:
```
$ pip install holistics
```
Alternatively, you can grab the latest source code from [GitHub](https://github.com/holistics/holistics-python):
```
$ git clone git clone git://github.com/holistics/holistics-python.git
$ python setup.py install
```

Documentation
---------------

**export_data (report_id, filter_dict, path, _page_size, _page)**
- **report_id (str):** id of report. Collect from URL. 
    Ex: https://secure.holistics.io/queries/**12345**-processing-report
- **filter_dict (dict) (optional):** dictionary of filters that would be applied to report
- **path (str) (optional):**
  - Set path if want to store .csv file (direction + filename)
  - Default value: None
- **_page_size (int) (optional):** set the page size of the response
  - Default value: 10000000
- **_page (int) (optional):** set the page number of data to fetch
   -Default value: 10000000
