import requests
import io
import json
import pandas as pd
import time

class HolisticsAPI:
    data = False
    path = None
    url = 'https://secure.holistics.io'
    headers = {
            "Accept":"application/json", 
            "Content-Type":"application/json",
            "X-Holistics-Key": None}
    page={
            'job_id': None,
            '_page_size': '10000000',
            '_page': '10000000'}

    def __init__(self, api_key, path = None, url = None):
        self.headers['X-Holistics-Key'] = api_key
        if url is not None:
            self.url = url
        if path is not None:
            self.path = path

    def info(self):
        return {'api_key': self.headers['X-Holistics-Key'], 'path': self.path, 'url': self.url, }

    def get_url(self, tail_url, params=None):
        res = requests.get(self.url + tail_url, params = params, headers = self.headers)
        res.raise_for_status()
        return res

    def submit_report (self, report_id, filters=None):
        print ("Submitting export request... ", end='')
        tail_url = '/queries/'+str(report_id)+'/submit_export.csv'
        try:
            res = self.get_url(tail_url, filters)
            res = res.json()
            print ("Success")
            return str(res['job_id'])
        except requests.exceptions.HTTPError as err:
            return err

    def get_export_result(self, job_id, _page_size = None, _page = None):
        print ("Getting export results... ", end='')
        tail_url = '/queries/get_export_results.json'
        self.page['job_id']=job_id
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
                    return 0
                res = self.get_url(tail_url, self.page).json()
                time.sleep(1)
            print ("Success")
            return 1
        except requests.exceptions.HTTPError as err:
            return err
        
    def download_results(self):
        print ("Downloading results... ", end='')
        tail_url = '/exports/download?job_id=' + self.page['job_id']
        try:
            res = self.get_url(tail_url)
            text = str(res.content, 'utf-8', errors='replace')
            data = pd.read_csv(io.StringIO(text))
            self.data = True
            print ("Success")
            if self.path == None:
                return data
            else:
                try:
                    data.to_csv(self.path, encoding='utf-8', index=False)
                    print ("Export to file successed!")
                    return 1
                except:
                    print ("Can't export file to " + self.path)
        except requests.exceptions.HTTPError as err:
            return err
        

    def export_data(self,report_id,filters=None, page_size=None, page=None):
        res = self.submit_report(report_id, filters)
        if type(res) == requests.exceptions.HTTPError:
            print ("Fail to submit report")
            return 0
        res = self.get_export_result(res,page_size,page)
        if res != 1:
            print ("Fail to get export results")
            return 0
        res = self.download_results()
        if type(res) == requests.exceptions.HTTPError:
            print ("Fail to download Results")
            return 0
        else:
            return res
