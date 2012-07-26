import urllib, hashlib, logging, json
from config import PAMFAX_API_URL, PAMFAX_SECRET


# Setup logging
logger = logging.getLogger('pam_fax')
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Global variable shared between service calls
usertoken = ''



def api_call(method, data):
    """
    Calls PamFax service and returns response. Raises exception on call fail.
    """
    data = _add_apicheck(data)
    data = urllib.urlencode(data)
    logger.debug('api_call(method=%s, data=%s)' % (method, data))
    response = urllib.urlopen(PAMFAX_API_URL+method, data).read()
    logger.debug('response=%s' % response)

    if method != 'Account/ExportResellerData':
        response = json.loads(response)
        try:
            code = response['result']['code']
        except KeyError:
            raise PamFaxError('PamFax service call %s failed. Response: %s' % (method, response))
        if code != 'success':
            raise PamFaxError('PamFax service call %s failed. Response: %s' % (method, response))

    return response


def _add_apicheck(data):
    """
    Adds checksum to data dictionary.
    """
    data_with_lower_keys = dict((key.lower(), value) for key, value in data.iteritems())
    sorted_keys = sorted(data_with_lower_keys.iterkeys())
    skip_keys = ('page', 'event', 'apikey', 'apicheck', 'usertoken', 'xdebug_profile')
    request_string = ''.join([data_with_lower_keys[key].decode('utf-8') for key in sorted_keys if key not in skip_keys])
    request_string += PAMFAX_SECRET
    request_string = request_string.encode('utf-8')

    apicheck = hashlib.md5()
    apicheck.update(request_string)
    apicheck = apicheck.hexdigest()

    data['apicheck'] = apicheck
    return data



class PamFaxError(Exception):
    pass



class PamFaxClass():
    """
    Super class for all PamFax API classes.
    """
    def __unicode__(self):
        return '\n'.join(
            ['%s: ' % self.__class__.__name__] +
            ['\t%s = %s' % (field, self.__dict__[field]) for field in self.__dict__]
        )


    def __str__(self):
        return self.__unicode__()
