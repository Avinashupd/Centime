import requests
from ratelimit import limits, sleep_and_retry
import openpyxl
import pytest

api_key = "6DMD92PP423TYRE3"
url = "https://www.alphavantage.co/query?"
min_time = 60
day_time = 86400


@sleep_and_retry
@limits(calls=5, period=min_time)
def test_get_record():
    wb = openpyxl.load_workbook("centime/testcase.xlsx")
    sheet = wb.active
    response_dict = {}
    for r in sheet.iter_rows(min_row=3, min_col=2, max_col=7, values_only=True):
        response_dict = {
            "function": r[1],
            "symbol": r[2],
            "outputsize": r[3],
            "datatype": r[4],
            "apikey": r[5]
        }

        getRecord = requests.get(url, params=response_dict)
        print(getRecord)
        getRecord_response = getRecord.json()
        # print(getRecord_response)
        if getRecord.status_code != 200:
            raise Exception('API response: {}'.format(getRecord.status_code))
        print(getRecord_response)
    return getRecord_response
