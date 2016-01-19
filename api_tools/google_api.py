import settings
import api_base
from oauth2client import client

class GoogleAPI(api_base.BaseAPI):
  access_scope = 'https://www.googleapis.com/auth/gmail.readonly'

  def __init__(self):
    super(GoogleAPI, self).__init__()

  def load_keys(self):
    self._client_secrets = settings.GOOGLE_CLIENT_SECRETS

  def get_authorization_url(self, redirect_url):
    flow = client.flow_from_clientsecrets(self._client_secrets, scope=self.access_scope, redirect_uri=redirect_url)
    #flow.params['access_type'] = 'offline'
    return flow.step1_get_authorize_url()
    

