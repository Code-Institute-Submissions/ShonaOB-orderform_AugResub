![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

https://stackoverflow.com/questions/6531482/how-to-check-if-a-string-contains-an-element-from-a-list-in-python

date validation: 
https://www.tutsmake.com/python-program-to-check-the-given-date-is-valid-or-not/
dd,mm,yy=delivery_date.split('/')
    dd=int(dd)
    mm=int(mm)
    yy=int(yy)
    if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
        max1=31
    elif(mm==4 or mm==6 or mm==9 or mm==11):
        max1=30
    elif(yy%4==0 and yy%100!=0 or yy%400==0):
        max1=29
    else:
        max1=28
    if(mm<1 or mm>12):
        print("Date is invalid.")
    elif(dd<1 or dd>max1):
        print("Date is invalid.")
    elif(dd==max1 and mm!=12):
        dd=1
        mm=mm+1
        print("The date is: ",dd,mm,yy)
    elif(dd==31 and mm==12):
        dd=1
        mm=1
        yy=yy+1
        print("The date is: ",dd,mm,yy)

Welcome ShonaOB,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!