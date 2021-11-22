import requests


def get_api_data(api_url):
    """ Function takes an api url and checks that a successful status code is
        return. If success request, the data is returned as a dictionary
        (JSON format)

    Args:
        api_url (str): api uri to make the GET request to

    Returns:
        dict: Dictionary format of the GET request
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.HTTPError as error:
        raise Exception(f"{error}")
