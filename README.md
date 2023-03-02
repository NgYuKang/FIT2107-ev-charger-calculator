# FIT2107_S2_2021 EV Charger Calculator

This is the project I've done with other group members in the unit FIT2107 - Software Quality and Testing.<br />
This project is part of the assignment to implement a simple calculator to calculate fees for charging according to type of charger and time of day.<br/>
This project was focused on the testing part, with the skeleton flask app code provided by the teaching team.<br />
The project was originally on the university's gitlab server, so you will see a gitlab ci/cd file in here.

Below is the original readme provided to setup the project.

## Setting up and running the project via the terminal

### Enabling virtualenv
To use virtualenv, you will need to have pip, the Python package installer, already installed on your machine (by default, it should also be installed when you install Python).

1. Windows
    ```
    python3 -m venv env
    .\env\Scripts\activate
    ```

2. Linux/macOS
    ```
    python3 -m venv env
    source env/bin/activate
    ```

    If you are unable to get virtualenv to run, you might need to run the following command first:
    ```
    sudo apt install python3-venv
    ```

### Installing Required Dependencies/Packages
You will need to install project dependencies for the provided code to work. This only needs to be done once.

```
pip install -r requirements.txt
```

### Exiting Virtualenv
Once you are finished working on the project, you can exit virtualenv by running the following command:

```
deactivate
```
