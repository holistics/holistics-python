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

    def GetURL(self, tail_url, params=None):
        try:
            res = requests.get(self.url + tail_url, params = params, headers = self.headers)
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print (err)
            return 0
        return res
        

    def SubmitReport (self, report_id, filters=None):
        print ("Submitting export request... ", end='')
        tail_url = '/queries/'+str(report_id)+'/submit_export.csv'
        res = self.GetURL(tail_url, filters)
        if res!=0:
            res = res.json()
            print ("Success")
            self.page['job_id'] = str(res['job_id'])
            return 1
        else:
            return 0

    def GetExportResults(self, job_id, _page_size = None, _page = None):
        print ("Getting export results... ", end='')
        tail_url = '/queries/get_export_results.json'
        self.page['job_id']=job_id
        if _page_size is not None:
            self.page['_page_size']=_page_size
        if _page is not None:
            self.page['_page']=_page
        res = self.GetURL(tail_url, self.page)
        if res!=0:
            res = res.json()
            while (res['status'] != 'success'):
                if res['status'] == 'already_existed':
                    self.page['job_id'] = str(res['job_id'])
                    break
                if res['status'] == 'failure':
                    print ("Status: Failure")
                    return 0
                res = self.GetURL(tail_url, self.page).json()
                time.sleep(1)
            print ("Success")
            return 1
        else:
            return 0
        
    def DownloadResults(self):
        print ("Downloading results... ", end='')
        tail_url = '/exports/download?job_id=' + self.page['job_id']
        res = self.GetURL(tail_url)
        if res!=0:
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
                except:
                    print ("Can't export file to " + self.path)
        

    def ExportData(self,report_id,filters=None, page_size=None, page=None):
        self.SubmitReport(report_id, filters)
        self.GetExportResults(self.page['job_id'],page_size,page)
        return self.DownloadResults()
