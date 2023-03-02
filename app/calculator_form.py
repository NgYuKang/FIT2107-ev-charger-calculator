from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField
from wtforms.validators import DataRequired, ValidationError, Optional
from datetime import date, time
import requests


# validation for form inputs
class Calculator_Form(FlaskForm):
    # this variable name needs to match with the input attribute name in the html file
    # you are NOT ALLOWED to change the field type, however, you can add more built-in validators and custom messages
    BatteryPackCapacity = StringField("Battery Pack Capacity", [DataRequired()])
    InitialCharge = StringField("Initial Charge", [DataRequired()])
    FinalCharge = StringField("Final Charge", [DataRequired()])
    StartDate = DateField("Start Date", [DataRequired("Data is missing or format is incorrect")], format='%d/%m/%Y')
    StartTime = TimeField("Start Time", [DataRequired("Data is missing or format is incorrect")], format='%H:%M')
    ChargerConfiguration = StringField("Charger Configuration", [DataRequired()])
    PostCode = StringField("Post Code", [DataRequired()])

    # use validate_ + field_name to activate the flask-wtforms built-in validator
    # this is an example for you
    def validate_BatteryPackCapacity(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("cannot fetch data")
        try:
            batteryCapacity = float(field.data)
        except ValueError:
            raise ValueError("Battery capacity is not numerical")
        if batteryCapacity <= 0:
            raise ValueError("Battery capacity cannot be 0 or negative")

    # validate initial charge here
    def validate_InitialCharge(self, field):
        # another example of how to compare initial charge with final charge
        # you may modify this part of the code
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("cannot fetch data")
        try:
            initialCharge = float(field.data)
        except ValueError:
            raise ValueError("Initial charge is not an integer")
        try:
            finalCharge = float(self.FinalCharge.data)
        except ValueError:
            raise ValueError("Final charge is not an integer")

        if initialCharge > finalCharge:
            raise ValueError("Initial charge is bigger than final charge")

    # validate final charge here
    def validate_FinalCharge(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("cannot fetch data")
        try:
            initialCharge = float(self.InitialCharge.data)
        except ValueError:
            raise ValueError("Initial charge is not an integer")
        try:
            finalCharge = float(field.data)
        except ValueError:
            raise ValueError("Final charge is not an integer")
        if initialCharge > finalCharge:
            raise ValueError("Final charge is smaller than initial charge")
        if finalCharge > 100:
            raise ValueError("Final charge is bigger than 100")

    # validate start date here
    def validate_StartDate(self, field):
        # print("Type: %s, data: %s" %(type(field.data), field.data))
        # conversion and checking is automatically done already....
        pass

    # validate start time here
    def validate_StartTime(self, field):
        # conversion and checking is automatically done already....
        pass

    # validate charger configuration here
    def validate_ChargerConfiguration(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("cannot fetch data")
        try:
            config = int(field.data)
        except ValueError:
            raise ValueError("Configuration is not in a numerical form")
        if config < 1 or config > 8:
            raise ValueError("Configuration is not between 1 and 8 inclusive")

    # validate postcode here
    def validate_PostCode(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("cannot fetch data")

        try:
            postCode = int(field.data)
        except ValueError:
            raise ValueError("Postcode is not numerical")
        # if 0 > postCode or postCode > 9999:
        #     raise ValueError("Postcode is invalid Australian Postcode")
        locationURL = "http://118.138.246.158/api/v1/location?postcode="
        requestLocationURL = locationURL + field.data
        resLocation = requests.get(url=requestLocationURL)
        if resLocation.status_code != 200:
            raise ValueError("Invalid postcode")
        if len(resLocation.json()) == 0:
            raise ValueError("Invalid postcode")
