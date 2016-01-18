
class BaseAPI(object):
  def __init__(self):
    self.load_keys()

  def load_keys(self):
    raise NotImplementedError

  def get_authorization_url(self, redirect_url):
    raise NotImplementedError
