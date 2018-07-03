import requests
import io
import json
import pandas as pd
import time

class HolisticsAPI:
    def __init__(self, api_key, url = None):
        self.headers = {
            "Accept":"application/json", 
            "Content-Type":"application/json",
            "X-Holistics-Key": "api_key"}
        self.headers['X-Holistics-Key'] = api_key
        if url is not None:
            self.url = url
        else:
            self.url = 'https://secure.holistics.io'   
        

    def get_url(self, tail_url, params=None):
        res = requests.get(self.url + tail_url, params = params, headers = self.headers)
        res.raise_for_status()
        return res

    def submit_export (self, report_id, filters=None):
        print ("Submitting export request... ", end='')
        tail_url = '/queries/'+str(report_id)+'/submit_export.csv'
        try:
            res = self.get_url(tail_url, filters)
            res = res.json()
            print ("Success")
            return str(res['job_id'])
        except requests.exceptions.HTTPError as err:
            print ("Fail to submit export")
            raise err

    def get_export_results(self, job_id, _page_size = None, _page = None):
        page={
            "job_id": "job_id",
            "_page_size": "10000000",
            "_page": "10000000"}
        print ("Getting export results... ", end='')
        tail_url = '/queries/get_export_results.json'
        page['job_id']=str(job_id)
        if _page_size is not None:
            page['_page_size']=str(_page_size)
        if _page is not None:
            page['_page']=str(_page)
        try:
            res = self.get_url(tail_url, page)
            res = res.json()
            while (res['status'] != 'success'):
                if res['status'] == 'already_existed':
                    page['job_id'] = str(res['job_id'])
                if res['status'] == 'failure':
                    print ("Status: Failure")
                    raise RuntimeError('Status of request is Failure')
                res = self.get_url(tail_url, page).json()
                time.sleep(1)
            print ("Success")
            return 1
        except requests.exceptions.HTTPError as err:
            print ("Fail to get export results")
            raise err
        
    def download_results(self, job_id, path):
        path = str(path)
        job_id = str(job_id)
        print ("Downloading results... ", end='')
        tail_url = '/exports/download?job_id=' + job_id   
        try:
            res = self.get_url(tail_url)
        except requests.exceptions.HTTPError as err:
            print ("Fail to submit download request")
            raise err
        text = str(res.content, 'utf-8', errors='replace')
        try:
            data = pd.read_csv(io.StringIO(text))
        except pd.errors.ParserError as err:
            print ("Fail to parsed result as CSV")
            raise err
        if path == None:
            return data
        else:
            try:
                data.to_csv(path, encoding='utf-8', index=False)
                print ("Export to file successed!")
                return data
            except:
                print ("Can't export file to " + path)    

    def export_data(self,report_id, path=None,filters=None, page_size=None, page=None):
        job_id = self.submit_export(report_id, filters)
        temp = self.get_export_results(job_id,page_size,page)
        res = self.download_results(job_id,path)
        return res