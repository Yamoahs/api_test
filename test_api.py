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
    print("Test verifies name returned is expected name")
    expected_name = "Carbon credits"
    api_data = get_api_data(url)
    name_returned = api_data.get("Name")

    print(f"Expected name: {expected_name}, name returned "
          f"from api: {name_returned}")
    assert name_returned == expected_name


def test_verify_can_relist():
    """ Test checks the canRelist field from the api data is as expected

    Returns:
        None
    """
    print("Test verifies canRelist field returned is as expected")
    expected_can_relist = True
    api_data = get_api_data(url)
    can_relist_returned = api_data.get("CanRelist")

    print(f"Expected canRelist: {expected_can_relist}, returned status "
          f"from api: {can_relist_returned}")
    assert can_relist_returned == expected_can_relist


def test_verify_promotions_description():
    """ Test checks Promotions element description returned contains the
        expected description

    Returns:
        None
    """
    print("Test verifies Promotions element description returned contains the "
          "expected description")
    expected_element_name = "Gallery"
    expected_description = "Good position in category"
    api_data = get_api_data(url)
    promotions = api_data.get("Promotions", [])

    # Parse promotions list to find specific element to test
    for promotion in promotions:
        if promotion.get("Name") == expected_element_name:
            print("Verifying Promotion element description contains expected "
                  f"string: '{expected_description}', returned description: "
                  f"'{promotion.get('Description')}'")
            assert expected_description in promotion.get("Description")
            break
    else:
        assert False, ("No Promotion with Name element: "
                       f"{expected_element_name}")
