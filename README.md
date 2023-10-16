# gudlift-registration


1. Goal

    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.12

    * Flask

    * Pytest

    * Locust

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * Virtual environment using Windows10 and git bash:

        1. ``` python -m venv env ```

        2. ``` source env/scripts/activate ```

    * Virtual environment using Linux:

        1. ``` python -m venv env ```

        2. ``` source env/bin/activate ```

    * Type ``` pip install -r requirements.txt ``` This will ensure all the packages needed for the program ok.

    * Verification: ``` pip freeze ``` show the list of installed packages in virtual env.

    * I you want to deactivate, type ``` deactivate ```


3. Installation

    * Clone and fork repository from [Repo Github](https://github.com/OpenClassrooms-Student-Center/Python_Testing).

    

    - You should now be ready to test the application. In the directory, type either ``` flask run --debug ```
     or ``` python -m flask run ```. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using.

    We also like to show how well we're testing, so there's a module called 
    [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

