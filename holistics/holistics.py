import requests
import io
import json
import pandas as pd
import time

class HolisticsAPI:
    def __init__(self, api_key, url = None):
        self.url = 'https://secure.holistics.io'   
        self.headers = {
            "Accept":"application/json", 
            "Content-Type":"application/json",
            "X-Holistics-Key": 'api_key'}
        self.page={
            'job_id': 'job_id',
            '_page_size': '10000000',
            '_page': '10000000'}
        self.headers['X-Holistics-Key'] = api_key
        if url is not None:
            self.url = url
        

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
            self.page['job_id'] = str(res['job_id'])
            print (str(res['job_id']))
            return 1
        except requests.exceptions.HTTPError as err:
            print ("Fail to submit export")
            return err

    def get_export_results(self, job_id, _page_size = None, _page = None):
        print ("Getting export results... ", end='')
        tail_url = '/queries/get_export_results.json'
        self.page['job_id']=str(job_id)
        if _page_size is not None:
            self.page['_page_size']=_page_size
        if _page is not None:
            self.page['_page']=_page
        try:
            res = self.get_url(tail_url, self.page)
            res = res.json()
            while (res['status'] != 'success'):
                if res['status'] == 'already_existed':
                    self.page['job_id'] = str(res['job_id'])
                if res['status'] == 'failure':
                    print ("Status: Failure")
                    raise ValueError('Can\'t get export results')
                res = self.get_url(tail_url, self.page).json()
                time.sleep(1)
            print ("Success")
            return 1
        except requests.exceptions.HTTPError as err:
            print ("Fail to get export results")
            return err
        
    def download_results(self, path):
        path = str(path)
        try:
            print ("Downloading results... ", end='')
            tail_url = '/exports/download?job_id=' + self.page['job_id']        
            res = self.get_url(tail_url)
            text = str(res.content, 'utf-8', errors='replace')
            data = pd.read_csv(io.StringIO(text))
            if path == None:
                return data
            else:
                try:
                    data.to_csv(path, encoding='utf-8', index=False)
                    print ("Export to file successed!")
                    return data
                except:
                    print ("Can't export file to " + path)
        except (requests.exceptions.HTTPError,pd.errors.ParserError) as err:
            print ("Fail to download results")
            return err
        

    def export_data(self,report_id, path=None,filters=None, page_size=None, page=None):
        try:
            res = self.submit_export(report_id, filters)
            res = self.get_export_results(self.page['job_id'],page_size,page)
            res = self.download_results(path)
            if isinstance(res, ((requests.exceptions.HTTPError, pd.errors.ParserError, ValueError))):
                raise ValueError
        except Exception:
            print ("Fail to export data")
            return 0
        else:
            return res