import random
from datetime import datetime
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


def get_county_name():
    """
    Get the county of the school this order is for from the user
    """
    global county

    print("Please enter the County where the school is located.")
    print("Please note! Delivery is currently")
    print("only available in Dublin and Offaly.")
    county_str = input("Enter your COUNTY here:\n").capitalize()
    if len(county_str) == 0:
        print("Oh no! You have not entered a county. Please try again.")
        main()

    client_counties = ["Offaly", "Dublin"]
    if any(county in county_str for county in client_counties):
        print(f"Great! We deliver to that county! {county_str}\n")
    else:
        print("Oops! You did not enter a county")
        print("or you entered a county that we do not deliver to!\n")
        print("Try again...\n")
        main()


def get_school_name():
    """
    Get the name of the school this order is for from the user
    """

    global school_name_str
    print(".............................................................")
    print("Please enter the school name")
    print("The name of the school must be longer than 5 characters.\n")
    school_name_str = input("Enter your school name here:\n").capitalize()
    if len(school_name_str) == 0:
        print("Oops! You did not enter a valid school name!\n")
        print("You will need to start again! \n")
        main()
    elif school_name_str == " ":
        print("Oops! You did not enter a valid school name!\n")
        print("You will need to start again! \n")
        main()
    elif school_name_str == "  ":
        print("Oops! You did not enter a valid school name!\n")
        print("You will need to start again! \n")
        main()
    elif school_name_str == "   ":
        print("Oops! You did not enter a valid school name!\n")
        print("You will need to start again! \n")
        main()
    elif " " not in school_name_str:
        print("Oops! You did not fill in the school name correctly.")
        print("Please try again.\n")
        main()
    else:
        print("checking...")
    if len(school_name_str) < 5:
        print("Oops! You did not enter a valid school name! Try again...\n")
        get_school_name()
    else:
        print(f"School Name: {school_name_str}")


def production_run():
    """
    Assigns a random number and the letter P to create a production run
    """
    random_no = random.randint(0, 200)
    prun = "P" + str(random_no)
    return prun


def get_delivery_date():
    """
    Get the date of the delivery from the user and validate it also
    """
    print(".............................................................")
    print("Please enter the required delivery date for this order")
    print("The date should be in the format DD/MM/YYYY")
    print("for example: 01/04/2022 \n")

    global delivery_date
    delivery_date = input("Enter your required delivery date:\n")
    # CREDIT: this code to validate the date was taken from tutsmake.com
    # see README for details
    if len(delivery_date) == 0:
        print("You have not entered a date. Please try again \n")
        get_delivery_date()
    if "/" not in delivery_date:
        print("You have not entered a vaild date format. Please try again \n")
        get_delivery_date()
    if len(delivery_date) < 10:
        print("You have not entered a valid date format.")
        print("Remember to use format dd/mm/yyyy Please try again \n")
        get_delivery_date()
    dd, mm, yy = delivery_date.split('/')
    dd = int(dd)
    mm = int(mm)
    yy = int(yy)
    if(mm == 1 or mm == 3 or
       mm == 5 or mm == 7 or
       mm == 8 or mm == 10 or
       mm == 12):
        max1 = 31
    elif(mm == 4 or mm == 6 or mm == 9 or mm == 11):
        max1 = 30
    elif(yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0):
        max1 = 29
    else:
        max1 = 28
    if(mm < 1 or mm > 12):
        print("Date is invalid.")
        get_delivery_date()
    elif(dd < 1 or dd > max1):
        print("Date is invalid.")
        get_delivery_date()
    elif(dd == max1 and mm != 12):
        dd = 1
        mm = mm + 1
        print("The date is: ", dd, mm, yy)
    elif(dd == 31 and mm == 12):
        dd = 1
        mm = 1
        yy = yy + 1
    else:
        dd = dd
        print("The delivery date is: ", dd, mm, yy)
    date_format = "%d/%m/%Y"
    start = datetime.strptime(delivery_date, date_format)
    now = datetime.now()
    if start < now:
        print("Oops! You must pick a date in the future\n")
        get_delivery_date()
    else:
        return delivery_date


def get_order_detail():
    """
    Get the order for the school from the user
    """
    print(".............................................................")
    print("Please enter the order detail")

    order_detail_str = input("Enter your order detail here:\n")
    if len(order_detail_str) == 0 or len(order_detail_str) < 10:
        print("You must enter more order details....\n")
        get_order_detail()
    print(f"The order you have placed is {order_detail_str}\n")
    return order_detail_str


def update_worksheet(data):
    """
    update worksheet with school name and date and order
    """
    print("Adding order to order worksheet....")
    order_worksheet = SHEET.worksheet("orders")
    order_worksheet.append_row(data)
    print("Order added successfully!\n")
    main()


def main():
    """
    Runs the main program
    """
    print("Welcome to the Order Form App!\n")
    print("................................................\n")
    data = [
        get_county_name(),
        get_school_name(),
        get_delivery_date(),
        get_order_detail(),
        production_run(), ]
    update_worksheet(data)
    print("DONE")


main()
