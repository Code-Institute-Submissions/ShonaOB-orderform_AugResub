import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('order-form')


def get_school_name():
    """
    Get the name of the school this order is for from the user
    """
    print("Please enter the school name")
    print("The name of the school should start with the County")
    print("for example: Dublin St. Mary's NS \n")

    school_name_str = input("Enter your school name here:\n")
    print(f"The school name you have provided is {school_name_str}")


get_school_name()