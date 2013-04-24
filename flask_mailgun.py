import requests

class Mailgun(object):
    mailgun_api = None

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.mailgun_api = MailgunApi(app.config['MAILGUN_DOMAIN'],
                app.config['MAILGUN_API_KEY'])

    def send_email(self, **kwargs):
        if not self.mailgun_api:
            raise ValueError('A valid app instance has not been provided')

        return self.mailgun_api.send_email(**kwargs)

class MailgunApi(object):
    def __init__(self, domain, api_key):
        self.domain = domain
        self.api_key = api_key

    def send_email(self, **kwargs):
        response = requests.post(self.endpoint, data=kwargs, auth=self.auth)
        response.raise_for_status()
        return response

    @property
    def endpoint(self):
        return 'https://api.mailgun.net/v2/{}/messages'.format(self.domain)

    @property
    def auth(self):
        return ('api', self.api_key)