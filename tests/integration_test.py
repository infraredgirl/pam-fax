# -*- coding: utf-8 -*-
import os, sys, datetime
sys.path.append(os.path.split(os.path.split(os.path.abspath(__file__))[0])[0])

from pam_fax.user_info import UserInfo
from pam_fax.session import Session
from pam_fax.shopping import Shopping
from pam_fax.company_info import CompanyInfo
from pam_fax.account import Account



# Instatiate objects
user_info_owner = UserInfo(
    name = 'Company Owner đšžćčĐŠŽĆČ',
    username = 'akrivokapic1@gmail.com',
    password = 'asdfASDF321',
    hash_function = 'plain',
    email = 'akrivokapic1@gmail.com',
    street = 'My Street šđčćžŠĐČĆŽ 123',
    zip = '1000',
    city = 'My City',
    country_code = 'SI',
    culture = 'en-US'
)

user_info_employee = UserInfo(
    name = 'Company Employee đšžćčĐŠŽĆČ',
    username = 'infraredgirl83@yahoo.com',
    password = 'asdfASDF321',
    hash_function = 'plain',
    email = 'infraredgirl83@yahoo.com',
    street = 'My Street šđčćžŠĐČĆŽ 123',
    zip = '1000',
    city = 'My City',
    country_code = 'SI',
    culture = 'en-US'
)

session_owner = Session(
    username = user_info_owner.username,
    password = user_info_owner.password,
)

session_employee = Session(
    username = user_info_employee.username,
    password = user_info_employee.password,
)

shopping = Shopping()

company_info = CompanyInfo(
    companyname = 'My Company',
    owner_name = user_info_owner.name,
    street = user_info_owner.street,
    zip = user_info_owner.zip,
    city = user_info_owner.city,
    country = user_info_owner.country_code,
)

account = Account(
    from_date = datetime.date(2012, 2, 1),
    to_date = datetime.date(2012, 2, 28),
)



# Create company owner
user_info_owner.create_user()
session_owner.verify_user()
session_owner.create_login_identifier()

# Setup fax number
shopping.list_fax_in_areacodes()
#user_info_owner.assign_fax_number(shopping.areacode_id)

# Create company
company_info.save_company()

# Create another employee
user_info_employee.create_user()
session_employee.verify_user()
session_employee.create_login_identifier()

# Login as company owner and invite employee to company
session_owner.verify_from_identifier()
company_info.invite_user(user_info_employee.username)

# Login as employee and accept membership
session_employee.verify_from_identifier()
company_info.accept_membership()

# Login as owner and save employee
session_owner.verify_from_identifier()
company_info.save_employee(user_info_employee.uuid)

# Login as employee and change password and name
session_employee.verify_from_identifier()
user_info_employee.set_password(new_password='MyNewPass321123')
user_info_employee.save_user(new_name='My New Name')

# Delete employee
user_info_employee.delete_user()

# Delete owner
session_owner.verify_from_identifier()
user_info_owner.delete_user()

# Export reseller data
reseller_data = account.export_reseller_data()
for d in reseller_data:
    print d
