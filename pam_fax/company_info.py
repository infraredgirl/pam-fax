import pam_fax.common
from config import PAMFAX_APIOUTPUTFORMAT, PAMFAX_APIKEY



class CompanyInfo(pam_fax.common.PamFaxClass):
    """
    Functionality to manage Companies.
    """
    def __init__(
            self,
            companyname = None,
            owner_name = None,
            street = None,
            zip = None,
            city = None,
            country = None
    ):
        self.companyname = companyname
        self.owner_name = owner_name
        self.street = street
        self.zip = zip
        self.city = city
        self.country = country


    def save_company(self):
        """
        Creates or updates the company for current user.
        """
        data = {
            'companyname': self.companyname,
            'owner_name': self.owner_name,
            'street': self.street,
            'zip': self.zip,
            'city': self.city,
            'country': self.country,
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        response = pam_fax.common.api_call(method='CompanyInfo/SaveCompany', data=data)
        self.uuid = response['Company']['uuid']


    def invite_user(self, username):
        """
        Invites a pamfax user to company.
        """
        data = {
            'username': username,
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        pam_fax.common.api_call(method='CompanyInfo/InviteUser', data=data)


    def accept_membership(self):
        """
        Accepts a membership for a given company.
        """
        data = {
            'company_uuid': self.uuid,
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        pam_fax.common.api_call(method='CompanyInfo/AcceptMembership', data=data)


    def save_employee(self, user_uuid):
        """
        Saves settings for a company member by his (users) UUID.
        """
        data = {
            'user_uuid': user_uuid,
            'auto_credit': '0',
            'inbox_access': '1',
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        pam_fax.common.api_call(method='CompanyInfo/SaveEmployee', data=data)


