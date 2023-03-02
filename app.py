from flask import Flask, flash
from flask import render_template
from flask import request
from datetime import date, time
from app.calculator import *

from app.calculator_form import *
import os

SECRET_KEY = os.urandom(32)

ev_calculator_app = Flask(__name__)
ev_calculator_app.config['SECRET_KEY'] = SECRET_KEY


@ev_calculator_app.route('/', methods=['GET', 'POST'])
def operation_result():
    # request.form looks for:
    # html tags with matching "name="

    calculator_form = Calculator_Form(request.form)

    # validation of the form
    if request.method == "POST" and calculator_form.validate():
        # if valid, create calculator to calculate the time and cost
        calculator = Calculator()

        # extract information from the form
        battery_capacity = int(request.form['BatteryPackCapacity'])
        initial_charge = int(request.form['InitialCharge'])
        final_charge = int(request.form['FinalCharge'])
        charger_configuration = int(request.form['ChargerConfiguration'])
        start_date_arr = (request.form['StartDate']).split("/")
        start_time_arr = (request.form['StartTime']).split(":")
        postcode = request.form['PostCode']

        start_date = date(day=int(start_date_arr[0]), month=int(start_date_arr[1]), year=int(start_date_arr[2]))
        start_time = time(hour=int(start_time_arr[0]), minute=int(start_time_arr[1]))

        power = calculator.get_configuration(charger_configuration)[0]
        base_cost = calculator.get_configuration(charger_configuration)[1]

        # you may change the logic as your like
        time_charge = calculator.time_calculation(initial_charge, final_charge, battery_capacity, power)
        end_time = calculator.get_end_time(start_date, start_time, time_charge)
        cost = calculator.total_cost_calculation(start_date, start_time, end_time, initial_charge,
                                                 base_cost, power, battery_capacity, postcode, solar_energy=True)
        cost_str = "$%.2f" % cost
        time_str = calculator.get_charging_time_str(time_charge)

        # TODO: Compare Solar energy calculation with cost

        # cost = calculator.cost_calculation(initial_charge, final_charge, battery_capacity, is_peak, is_holiday)

        # you may change the return statement also

        # values of variables can be sent to the template for rendering the webpage that users will see
        return render_template('calculator.html', cost=cost_str, time=time_str,
                               calculation_success=True, form=calculator_form)
        # return render_template('calculator.html', calculation_success=True, form=calculator_form)
    else:
        # battery_capacity = request.form['BatteryPackCapacity']
        # flash(battery_capacity)
        # flash("something went wrong")
        flash_errors(calculator_form)
        return render_template('calculator.html', calculation_success=False, form=calculator_form)


# method to display all errors
def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')


if __name__ == '__main__':
    ev_calculator_app.run()
