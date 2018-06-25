import requests
import io
import json
import pandas as pd
import time

class api:
    path = None
    url = 'https://secure.holistics.io/'
    headers = {
            "Accept":"application/json", 
            "Content-Type":"application/json",
            "X-Holistics-Key": ''}
    page={
            'job_id': '',
            '_page_size': '10000000',
            '_page': '10000000'}

    def __init__(self, api_key, path = None, url = None):
        self.headers['X-Holistics-Key'] = api_key
        if url is not None:
            self.url = url
        if path is not None:
            self.path = path

    def get_url(self, tail_url, params=None):
        res = requests.get(self.url + tail_url, params = params, headers = self.headers)
        if res.status_code != 200:
            print ("Error " + str(r.status_code))
            return 0
        else:
            return res

    def submit_export(self, report_id, filters=None):
        print ("Submitting export request... ", end='')
        tail_url = 'queries/'+report_id+'/submit_export.csv'
        res = self.get_url(tail_url, filters).json()
        if res!=0:
            print ("Success")
            self.page['job_id'] = str(res['job_id'])

    def get_export_results(self, job_id, _page_size = None, _page = None):
        print ("Getting export results... ", end='')
        tail_url = '/queries/get_export_results.json'
        self.page['job_id']=job_id
        if _page_size is not None:
            self.page['_page_size']=_page_size
        if _page is not None:
            self.page['_page']=_page
        res = self.get_url(tail_url, self.page).json()
        if res!=0:
            if res['status'] == 'already_existed':
                self.page['job_id'] = str(res['job_id'])
            if res['status'] == 'failure':
                print ("Status: Failure")				
                return 0
            while (res['status'] != 'success'):
                res = self.get_url(tail_url, self.page).json()
                time.sleep(1)	
        print ("Success")
        
    def download_results(self):
        print ("Downloading results... ", end='')
        tail_url = 'exports/download?job_id=' + self.page['job_id']
        res = self.get_url(tail_url)
        if res!=0:
            text = str(res.content, 'utf-8', errors='replace')
            data = pd.read_csv(io.StringIO(text))
            print ("Success")
            if self.path == None:
                return data
            else:
                try:
                    data.to_csv(path, encoding='utf-8', index=False)
                    return "Export to file successed!"
                except:
                    return "Can't export file to " + self.path
        

    def export_data(self,report_id,filters=None,_page_size=None,_page=None):
        self.submit_export(report_id, filters)
        self.get_export_results(self.page['job_id'],_page_size,_page)
        return self.download_results()
