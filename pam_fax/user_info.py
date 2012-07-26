import pam_fax.common
from config import PAMFAX_COUNTRY_CODE, PAMFAX_CULTURE, PAMFAX_APIOUTPUTFORMAT, PAMFAX_APIKEY



class UserInfo(pam_fax.common.PamFaxClass):
    """
    Users account management.
    """
    def __init__(
            self,
            name = None,
            username = None,
            password = None,
            hash_function = 'plain',
            email = None,
            street = None,
            zip = None,
            city = None,
            country_code = PAMFAX_COUNTRY_CODE,
            culture = PAMFAX_CULTURE
    ):
        self.name = name
        self.username = username
        self.password = password
        self.hash_function = hash_function
        self.email = email
        self.street = street
        self.zip = zip
        self.city = city
        self.country_code = country_code
        self.culture = culture


    def create_user(self):
        """
        Creates a new PamFax user and logs him in.
        """
        data = {
            'name': self.name,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'culture': self.culture,
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY
        }

        response = pam_fax.common.api_call(method='UserInfo/CreateUser', data=data)
        self.uuid = response['User']['uuid']
        pam_fax.common.usertoken = response['UserToken']['token']


    def delete_user(self):
        """
        Deletes the currently logged in users account.
        """
        data = {
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        pam_fax.common.api_call(method='UserInfo/DeleteUser', data=data)
        pam_fax.common.usertoken = None


    def assign_fax_number(self, areacode_id):
        """
        Assigns a new fax-in number to the current user.
        """
        data = {
            'areacode_id': areacode_id,
            'fullname': self.name,
            'street': self.street,
            'zip': self.zip,
            'city': self.city,
            'country_code': self.country_code,
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        response = pam_fax.common.api_call(method='UserInfo/AssignFaxNumber', data=data)
        self.ext_faxnumber = response['FaxInNumber']['number']


    def set_password(self, new_password, new_hash_function='plain'):
        """
        Set a new login password for the currently logged in user.
        """
        data = {
            'password': new_password,
            'hashFunction': new_hash_function,
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        pam_fax.common.api_call(method='UserInfo/SetPassword', data=data)
        self.password, self.hash_function = new_password, new_hash_function


    def save_user(self, new_name):
        """
        Saves user profile.
        """
        data = {
            'profile[name]': new_name,
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        pam_fax.common.api_call(method='UserInfo/SaveUser', data=data)
        self.name = new_name

