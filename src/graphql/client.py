import requests

def run_query(query, variables={}):
    body = {'query': query, 'variables': variables}
    response = _make_post_call(body)
    if response.get('data') is not None:
        return response.get('data')
    raise RuntimeError('query failed: ' + str(response))


def _make_post_call(body):
    url = 'https://restaurant-finder.hasura.app/v1/graphql'
    headers = {
        'Content-type': 'application/json',
        'x-hasura-admin-secret': 'X3wUR3snSgKyIXhlHuqYkv4pw1RrW2eOgeL28sfaOS9tQHbsdkNx1MdeWV5GzsI5'
    }
    response = requests.post(url, json=body, headers=headers, timeout=30)
    return response.json()
