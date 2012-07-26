import pam_fax.common
from config import PAMFAX_APIOUTPUTFORMAT, PAMFAX_APIKEY



class Session(pam_fax.common.PamFaxClass):
    """
    Manage users sessions.
    """
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password


    def verify_user(self):
        """
        Verifies a user via username/password.
        """
        data = {
            'username': self.username,
            'password': self.password,
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        response = pam_fax.common.api_call(method='Session/VerifyUser', data=data)
        pam_fax.common.usertoken = response['UserToken']['token']


    def verify_from_identifier(self):
        """
        Verifies a user from a login identifier.
        """
        data = {
            'identifier': self.identifier,
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        response = pam_fax.common.api_call(method='Session/VerifyFromIdentifier', data=data)
        pam_fax.common.usertoken = response['UserToken']['token']


    def create_login_identifier(self):
        """
        Creates an identifier for the current user.
        """
        data = {
            'timetolifeminutes': '-1',
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        response = pam_fax.common.api_call(method='Session/CreateLoginIdentifier', data=data)
        self.identifier = response['UserIdentifier']['identifier']


    def logout(self):
        """
        Terminates the current session.
        """
        data = {
            'apioutputformat': PAMFAX_APIOUTPUTFORMAT,
            'apikey': PAMFAX_APIKEY,
            'usertoken': pam_fax.common.usertoken
        }

        pam_fax.common.api_call(method='Session/Logout', data=data)


