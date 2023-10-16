# gudlift-registration


1. Goal

    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.12

    * Flask

    * Pytest

    * Locust


3. Installation

    * Clone and fork repository from [Repo Github](https://github.com/OpenClassrooms-Student-Center/Python_Testing).

    * Unzip the repo and enter "Python_Testing-main".

    * Rename the new folder that appears "Python_Testing-main"   Python_Testing.

    * Enter Python_Testing and:

    * Create virtual environment using Windows10 and git bash:

        1. ``` python -m venv env ```

        2. ``` source env/scripts/activate ```

    * Or virtual environment using Linux:

        1. ``` python -m venv env ```

        2. ``` source env/bin/activate ```

    * Type ``` pip install -r requirements.txt ``` This will ensure all the packages needed for the program ok.

    * Verification: ``` pip freeze ``` show the list of installed packages in virtual env.

    * Particulary this should install Flask which allows us to add only what we need. Contrarily Django is an ORM
        and install himself all is needed for SGBDR. 

    * I you have to deactivate this env, type ``` deactivate ```    

    * You should now be ready to run the application. In the directory, type either ``` flask run --debug ```
     or ``` python -m flask run ```. The app should respond with an address you should be able to go to using your browser and go to (http://127.0.0.1:5000).

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    * For coverage tests run : ``` pytest --cov=. ```

    * For performance tests with Locust:

        1. ``` cd tests/performance_tests ``` 
        2. ``` locust ```
        3. fill out:
            1. Number of users: 1
            2. Spawn rate: 1
            3. Host: localhost:8089 or 0.0.0.0:8089
    

    We also like to show how well we're testing, so there's a module called 
    [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

