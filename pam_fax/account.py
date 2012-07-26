import csv
import pam_fax.common
from config import PAMFAX_APIOUTPUTFORMAT, PAMFAX_APIKEY



class Account(pam_fax.common.PamFaxClass):
    """
    API to manage the PamFax partner's API account.
    """
    def __init__(self, from_date=None, to_date=None):
        self.from_date = from_date
        self.to_date = to_date


    def export_reseller_data(self):
        """
        Exports all reseller data for a given datetime range to CSV.
        """
        method = 'Account/ExportResellerData'
        data = {
            'from': str(self.from_date),
            'to': str(self.to_date),
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY
        }

        rawdata = pam_fax.common.api_call(method, data)
        reader = csv.reader(rawdata.splitlines(), delimiter=';')
        return [line for line in reader]
