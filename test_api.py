import requests

# API URL under test
url = ("https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?"
       "catalogue=false")


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


def test_verify_name():
    """ Test Checks the Name field from the api data is as expected

    Returns:
        None
    """
    print(f"Test verifies name returned is expected name")
    expected_name = "Carbon credits"
    api_data = get_api_data(url)
    name_returned = api_data.get("Name")

    print(f"Expected name: {expected_name}, name returned "
          f"from api: {name_returned}")
    assert name_returned == expected_name

