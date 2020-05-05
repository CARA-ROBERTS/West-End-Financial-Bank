'''
Credit Crunch
Author: Andrew McKinney
Creation Date: 2020-04-28
'''



### Field Lists used in packing and unpacking of data
field_list = ['CHK_ACCT', 'DURATION', 'HISTORY', 'NEW_CAR', 'USED_CAR', 'FURNITURE', 'RADIO_TV', 'EDUCATION', 'RETRAINING',
'AMOUNT', 'SAV_ACCT', 'EMPLOYMENT', 'INSTALL_RATE', 'MALE_DIV', 'MALE_SINGLE', 'MALE_MAR_or_WID', 'CO_APPLICANT', 'GUARANTOR', 
'PRESENT_RESIDENT', 'REAL_ESTATE', 'PROP_UNKN_NONE', 'AGE', 'OTHER_INSTALL', 'RENT', 'OWN_RES', 'NUM_CREDITS', 'JOB', 
'NUM_DEPENDENTS', 'TELEPHONE', 'FOREIGN']

general_field_list = ['CHK_ACCT', 'DURATION', 'HISTORY', 'AMOUNT', 'SAV_ACCT', 'EMPLOYMENT', 'INSTALL_RATE', 
'CO_APPLICANT', 'GUARANTOR', 'PRESENT_RESIDENT', 'AGE', 'OTHER_INSTALL', 'NUM_CREDITS', 'JOB', 
'NUM_DEPENDENTS', 'TELEPHONE', 'FOREIGN']

packed_field_list = {'PURPOSE':['NEW_CAR', 'USED_CAR', 'FURNITURE', 'RADIO_TV', 'EDUCATION', 'RETRAINING'], 
'SEX_REL':['MALE_DIV', 'MALE_SINGLE', 'MALE_MAR_or_WID'], 
'RES_STAT':['RENT', 'OWN_RES'], 
'REAL_STAT':['REAL_ESTATE', 'PROP_UNKN_NONE']}

# basic model list (UNSORTED)
basic_model_field_list = ['CHK_ACCT', 'DURATION', 'HISTORY', 'AMOUNT', 'SAV_ACCT', 'EMPLOYMENT', 'INSTALL_RATE', 'PRESENT_RESIDENT', 
'AGE', 'JOB']







def form_dict(field_list):
# collecting items from form and making data dictionary

    from flask import request

    form_data = {}

    # looping through passed field list
    for field in field_list:

        field_value = request.form[field]

        # adding to data dictionary if user selection made
        if field_value != "":
            form_data[field] = field_value

    return form_data



def unpacking(packed_data, packed_field_list):
# unpacking packed data inside of packed fields from input form

    unpacked_data = {}

    # creating lists of fields and values in packed data
    packed_data_fields = [item for item in packed_data]
    packed_data_values = [packed_data[item] for item in packed_data]

    # looping through packed fata fields and retrieving unpacked data fields from field list
    for packed_field in packed_data_fields:
        unpacked_fields = packed_field_list[packed_field]

        # looping through unpacked fields and checking if present in the packed values to determine binary status
        for field in unpacked_fields:
            if field in packed_data_values:
                unpacked_data[field] = 1
            else:
                unpacked_data[field] = 0


    return unpacked_data



def merge_dict(field_list, form_data_1, form_data_2):
# merging dictionary datas to sorted field list, returning as dictionary data package

    data_package = {}
    
    # looping through sorted field list to acquire field value
    for field in field_list:

        # checking for field data in form_data dictionaries
        try:
            field_value = form_data_1[field]
        except:
            try:
                field_value = form_data_2[field]
            except:
                continue
        
        # appending integer value of field data to data_package
        data_package[field] = int(field_value)

    return data_package
