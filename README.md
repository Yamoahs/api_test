# API test with pytest
This project is a small piece of python code that is used to automate testing 
of 3 given requirements using pytest.
The repo consists of three main files:
* environment_setup.sh - is an easy setup script used to configure the
 test environmnet
* packages.txt - contains the necessary python modlues that are required to
 run the test
* test_api.py - python file with the three testcases pytest will execute


### Setting up the python 3 Virtual Environment
NOTE: The setup script has only been tested on Unbuntu 18.04 and Unbuntu 20.04 
OS, any other versions of Linux/Unix has not been tests so may not work. 
The setup script will not work on wndows. In order to run the test correctly, 
the `environment_setup.sh` script will need to be executed prior to running 
the test(s). In this script, it will install (if not already present on the 
system) `python3.8, python3.8-venv and python3-pip` (User password will be 
required as sudo is used) then create and activate a python virtual environment 
to install the required packages from the `packages.txt` using pip.
To run the setup script from the project directory, use the command:

`source environment_setup.sh`

If the script fails to setup and configure the virtual enrivonment, it can be
 run manually with the commands below:
 ```
# Install Python3.8, dev tools and pip
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt install python3.8 python3.8-venv
sudo apt install python3-pip

# Create and activate virtural Environment with packages installed from
 packages.txt
python3.8 -m venv test_venv
source test_venv/bin/activate
pip install -r pacckages.txt
```
Once setup correctly the shell environment will look similar to this:

`(test_venv) user@pc_name:~/api_test$ `

### Begin Test Execution
The tests makes use of pytest to run the tests. Test 1 (test_verify_name) 
checks the name field from the API data is "Carbon credits". 
Test 2 (test_verify_can_relist) verifies the CanRelist field is set to "true".
Test 3 (test_verify_promotions_description) verifies that the Promotions 
element with Name "Gallery" has a Description that contains "Good position in
 category".

To run all the tests, use the command:

`pytest test_api.py -s` (-s will display print messages to stdout)

To run a single test, use the command:

`pytest test_api.py::<test_module_name> -s`

To close the virtual environment, use the command:

`deactivate`
