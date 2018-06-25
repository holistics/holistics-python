from __future__ import print_function
import requests
import io
import json
import pandas as pd
import time

class api:
    def __init__(self, api_key):
        self.headers = {
            "Accept":"application/json", 
            "Content-Type":"application/json",
            "X-Holistics-Key": api_key}
    
    def export_data(self, report_id, filter_dict=dict(), path=None, _page_size=10000000, _page=10000000): 
        print ("Executing report...")
        r = requests.get('https://secure.holistics.io/queries/'+report_id+'/submit_export.csv', params = filter_dict, headers = self.headers)
        if r.status_code != 200:
            return "Error " + str(r.status_code)
        print ("Success")
        job_id = str(r.json()['job_id'])
        page={
            'job_id': job_id,
            '_page_size': _page_size,
            '_page': _page}
        print ("Getting export results...")
        r = requests.get('https://secure.holistics.io/queries/get_export_results.json', params = page,headers = self.headers)
        if r.status_code != 200:
            return "Error " + str(r.status_code)
        print ("Success")
        res = r.json()
        while (res['status'] != 'success'):
            r = requests.get('https://secure.holistics.io/queries/get_export_results.json', params = page,headers = self.headers)
            res = r.json()
            time.sleep(1)
        print ("Downloading export results...")
        r = requests.get('https://secure.holistics.io/exports/download?job_id=' + job_id,headers = self.headers)
        if r.status_code != 200:
            return "Error " + str(r.status_code)
        text = str(r.content, 'utf-8', errors='replace')    
        data = pd.read_csv(io.StringIO(text))
        if path == None:
            return data
        else:
            try:
                data.to_csv(path, encoding='utf-8', index=False)
                return "Export to file successed!"
            except:
                return "Path not found"
