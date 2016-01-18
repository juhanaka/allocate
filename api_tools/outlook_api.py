import requests
import urllib
import settings
import api_base

class OutlookAPI(api_base.BaseAPI):
  auth_url = settings.MS_AUTH_URL
  access_scope = 'https://outlook.office.com/Mail.Read'

  def __init__(self):
    super(OutlookAPI, self).__init__()

  def load_keys(self):
    with open(settings.MS_APP_ID_FILE) as filep:
      self._app_id = filep.read().strip()
    with open(settings.MS_PASS_FILE) as filep:
      self._pass = filep.read().strip()
    with open(settings.MS_PRIVATE_KEY_FILE) as filep:
      self._private_key = filep.read().strip()

  def get_authorization_url(self, redirect_url):
    params = {'client_id': self._app_id, 'redirect_uri': redirect_url,
              'response_type': 'code', 'scope': self.access_scope}
    return self.auth_url + '?' + urllib.urlencode(params)

