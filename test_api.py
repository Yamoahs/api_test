import requests


def get_api_data(url):
    """ Function takes an api url and checks that a successful status code is
        return. If success request, the data is returned as a dictionary
        (JSON format)

    Args:
        url (str): api uri to make the GET request to

    Returns:
        dict: Dictionary format of the GET request
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.HTTPError as error:
        print(f"Get Request failed: {error}")
