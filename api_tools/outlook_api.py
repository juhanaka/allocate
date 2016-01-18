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
    self._app_id = settings.MS_APP_ID

  def get_authorization_url(self, redirect_url):
    params = {'client_id': self._app_id, 'redirect_uri': redirect_url,
              'response_type': 'code', 'scope': self.access_scope}
    return self.auth_url + '?' + urllib.urlencode(params)

