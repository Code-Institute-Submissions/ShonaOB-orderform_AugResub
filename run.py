import gspread
from google.oauth2.service_account import Credentials
import datetime


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
    print(f"The school name you have provided is {school_name_str}\n")
    return school_name_str


def get_delivery_date():
    """
    Get the date of the delivery from the user
    """
    print("Please enter the required delivery date for this order")
    print("The date should be in the format DD/MM/YYYY")
    print("for example: 01/04/2022 \n")

    global delivery_date
    delivery_date = input("Enter your required delivery date:\n")
    print(f"You have requested a delivery on the {delivery_date}\n")
    return delivery_date


def date_format(delivery_date):
    """
    Convert the date string into datetime format
    """
    try: 
        date = datetime.datetime.strptime(delivery_date, "%d %B, %Y")
    except ValueError:
        date = None
    return date
    print(f" the date you have chosen is: {date}")


def update_worksheet(data):
    """
    update worksheet with school name and date
    """
    print("Adding school name to order worksheet....")
    order_worksheet = SHEET.worksheet("orders")
    order_worksheet.append_row(data)
    print("School name added successfully...\n")


def main ():
    data = [get_school_name(), get_delivery_date()]
    school = get_school_name()
    del_date = get_delivery_date()
    date_for_sheet = date_format(delivery_date)
    update_worksheet(data)


main()
