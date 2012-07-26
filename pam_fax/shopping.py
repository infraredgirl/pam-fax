import pam_fax.common
from config import PAMFAX_COUNTRY_CODE, PAMFAX_STATE, PAMFAX_APIOUTPUTFORMAT, PAMFAX_APIKEY



class Shopping(pam_fax.common.PamFaxClass):
    """
    Functionality for buying and payment.
    """
    def __init__(self, country_code=PAMFAX_COUNTRY_CODE, state=PAMFAX_STATE):
        self.country_code = country_code
        self.state = state


    def list_fax_in_areacodes(self):
        """
        Returns available fax-in area codes in a given country+state.
        """
        data = {
            'country_code': self.country_code,
            'state': self.state,
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        response = pam_fax.common.api_call(method='Shopping/ListFaxInAreacodes', data=data)
        self.areacode_id = response['AreaCodes']['content'][0]['id']

