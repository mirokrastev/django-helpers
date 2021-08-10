import os


def relative_url(querystring_key, querystring_value, urlencode=''):
    querystring = f'{querystring_key}={querystring_value}'

    if urlencode:
        querystrings = urlencode.split('&')
        filtered_querystring = []
        new_querystring = True

        for old_querystring in querystrings:
            if old_querystring.split('=')[0] == querystring_key:
                filtered_querystring.append(querystring)
                new_querystring = False
            else:
                filtered_querystring.append(old_querystring)

        encoded_querystring = '&'.join(filtered_querystring)

        action_mapper = {
            True: f'{encoded_querystring}&{querystring}',
            False: f'{encoded_querystring}',
        }

        querystring = action_mapper[new_querystring]

    return f'?{querystring}'


def get_admin_url(scheme, base_url):
    return f"{scheme}://{base_url}/{os.environ.get('ADMIN_PAGE', 'admin/')}"
