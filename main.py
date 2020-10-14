import requests
import os


def get_token() -> str:
    tenant_id = os.getenv('tenant_id')
    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')
    user_name = os.getenv('user_name')
    pass_word = os.getenv('pass_word')
    url = 'https://login.microsoftonline.com/{0}/oauth2/v2.0/token'.format(
        tenant_id)
    form_data = {
        'grant_type': 'password',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default',
        'userName': user_name,
        'password': pass_word
    }
    return requests.post(url=url, data=form_data).json().get('access_token')


if __name__ == '__main__':
    auth = 'Bearer ' + get_token()
    header = {
        'Authorization': auth
    }
    code = requests.get(
        'https://graph.microsoft.com/v1.0/me/messages', headers=header).status_code
    if code.status_code == 200:
        print('mail success')
    else:
        raise ValueError('mail fail')
    code = requests.get(
        'https://graph.microsoft.com/v1.0/me/drive/root/children', headers=header).status_code
    if code.status_code == 200:
        print('drive success')
    else:
        raise ValueError('drive fail')
