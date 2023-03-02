from wtforms.validators import ValidationError
from app.calculator_form import Calculator_Form
from flask import Flask, flash
from flask import render_template
from flask import request
from datetime import date, time
from app.calculator import *
from app.calculator_form import *
from unittest.mock import Mock, patch, PropertyMock
import unittest

class TestValidationForm(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['DEBUG'] = False

    def test_capacity_1(self):
        # Test negative capacity
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = "-50"
            with self.assertRaises(ValueError):
                form.validate_BatteryPackCapacity(field)

    def test_capacity_2(self):
        # Test non-numerical input
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = "alda"
            with self.assertRaises(ValueError):
                form.validate_BatteryPackCapacity(field)

    def test_capacity_3(self):
        # test broken input
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = None
            with self.assertRaises(ValidationError):
                form.validate_BatteryPackCapacity(field)

    def test_capacity_4(self):
        # test empty input
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = ''
            with self.assertRaises(ValueError):
                form.validate_BatteryPackCapacity(field)

    def test_initialCharge_1(self):
        # test none input
        with self.app.app_context():
            form = Calculator_Form()
            form.FinalCharge.data = "50"
            field = Mock()
            field.data = None
            with self.assertRaises(ValidationError):
                form.validate_InitialCharge(field)

    def test_initialCharge_2(self):
        # test empty input
        with self.app.app_context():
            form = Calculator_Form()
            form.FinalCharge.data = "50"
            field = Mock()
            field.data = ''
            with self.assertRaises(ValueError):
                form.validate_InitialCharge(field)

    def test_initialCharge_3(self):
        # test non-numerical input
        with self.app.app_context():
            form = Calculator_Form()
            form.FinalCharge.data = "50"
            field = Mock()
            field.data = 'a1'
            with self.assertRaises(ValueError):
                form.validate_InitialCharge(field)

    def test_initialCharge_4(self):
        # test broken final charge inut
        with self.app.app_context():
            form = Calculator_Form()
            form.FinalCharge.data = "a1"
            field = Mock()
            field.data = '40'
            with self.assertRaises(ValueError):
                form.validate_InitialCharge(field)

    def test_initialCharge_5(self):
        # test initial charge > final charge
        with self.app.app_context():
            form = Calculator_Form()
            form.FinalCharge.data = "39"
            field = Mock()
            field.data = '40'
            with self.assertRaises(ValueError):
                form.validate_InitialCharge(field)

    def test_finalCharge_1(self):
        # test None input
        with self.app.app_context():
            form = Calculator_Form()
            form.InitialCharge.data = "20"
            field = Mock()
            field.data = None
            with self.assertRaises(ValidationError):
                form.validate_FinalCharge(field)

    def test_finalCharge_2(self):
        # test empty input
        with self.app.app_context():
            form = Calculator_Form()
            form.InitialCharge.data = "20"
            field = Mock()
            field.data = ''
            with self.assertRaises(ValueError):
                form.validate_FinalCharge(field)

    def test_finalCharge_3(self):
        # test non-numerical final charge
        with self.app.app_context():
            form = Calculator_Form()
            form.InitialCharge.data = "20"
            field = Mock()
            field.data = 'a1'
            with self.assertRaises(ValueError):
                form.validate_FinalCharge(field)

    def test_finalCharge_4(self):
        # test broken initial charge
        with self.app.app_context():
            form = Calculator_Form()
            form.InitialCharge.data = "a1"
            field = Mock()
            field.data = "40"
            with self.assertRaises(ValueError):
                form.validate_FinalCharge(field)


    def test_finalCharge_5(self):
        # test final charge < initial charge
        with self.app.app_context():
            form = Calculator_Form()
            form.InitialCharge.data = "40"
            field = Mock()
            field.data = '20'
            with self.assertRaises(ValueError):
                form.validate_FinalCharge(field)

    def test_finalCharge_6(self):
        # test final charge > 100
        with self.app.app_context():
            form = Calculator_Form()
            form.InitialCharge.data = "40"
            field = Mock()
            field.data = '111'
            with self.assertRaises(ValueError):
                form.validate_FinalCharge(field)

    def test_configuration_tc1(self):
        # Test None input
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = None
            with self.assertRaises(ValueError):
                form.validate_ChargerConfiguration(field)

    def test_configuration_tc2(self):
        # Test empty input
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = ''
            with self.assertRaises(ValueError):
                form.validate_ChargerConfiguration(field)

    def test_configuration_tc3(self):
        # test non numerical input
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = "a1"
            with self.assertRaises(ValueError):
                form.validate_ChargerConfiguration(field)

    def test_configuration_tc4(self):
        # test < 1
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = "0"
            with self.assertRaises(ValueError):
                form.validate_ChargerConfiguration(field)

    def test_configuration_tc5(self):
        # test > 8
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = "9"
            with self.assertRaises(ValueError):
                form.validate_ChargerConfiguration(field)

    def test_postcode_1(self):
        # test none input
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = None
            with self.assertRaises(ValueError):
                form.validate_PostCode(field)

    def test_postcode_2(self):
        # test empty input
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = ''
            with self.assertRaises(ValueError):
                form.validate_PostCode(field)

    def test_postcode_3(self):
        # test non australian postcode (not 4 digit)
        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = "a123"
            with self.assertRaises(ValueError):
                form.validate_PostCode(field)

    @patch('app.calculator.requests.get')
    def test_postcode_4(self, mocked_get):
        # test invalid postcode with 4 digits
        data = []
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 200
        mocked_get.return_value = mocked_response

        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = "0000"
            with self.assertRaises(ValueError):
                form.validate_PostCode(field)

    @patch('app.calculator.requests.get')
    def test_postcode_5(self, mocked_get):
        # test postcode with digits other than 4 digits
        data = [1,2,3]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 400
        mocked_get.return_value = mocked_response

        with self.app.app_context():
            form = Calculator_Form()
            field = Mock()
            field.data = "000"
            with self.assertRaises(ValueError):
                form.validate_PostCode(field)

if __name__ == "__main__":
    # create the test suit from the cases above.
    suit = unittest.TestLoader().loadTestsFromTestCase(TestValidationForm)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)
