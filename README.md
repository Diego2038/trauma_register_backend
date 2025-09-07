
## Considerations
A **.env** file must be created to set the pertinent state variables, just as it is in the **.env.example** file, there the specifications for the connection to the database will be defined via Postgres.<br><br>
In Postgres you have to create a database with the same name as defined in the **.env** file for the ***NAME_DATABASE*** variable to establish the connection between Django and the database in Postgres, also with the username, password, host and port.
The python version used is 3.10.8

## How to execute the code

To create the virtual environment download the "virtualenv" library via pip.

<br>

```
pip install virtualenv 
```

<br> 
Create the virtual environment with named "venv" (in the root folder where the project is)

```
python -m venv venv
```

<br>
To run the virtual environment (from the root folder): <br><br>
In Windows:<br>

```
.\venv\Scripts\activate
```

In Linux distributions or MacOS:<br>

```
source .\venv\bin\activate
```

<br>
Perform the dependency installations (try to have executed the virtual environment):

```
pip install -r requirements.txt
```

<br>
Perform migrations in Django:

```
python manage.py makemigrations
python manage.py migrate
```

<br>
To run the Django server (in development mode):

```
python manage.py runserver
```

<br>
To close the virtual environment:

```
deactivate
``` 

## How to recreate the postman


1. **Open Postman.**

2. **Import the collection:**
- Click on the **Import** button located in the upper left corner.
- Select the **Upload Files** tab.
- Click **Choose Files** and navigate to the **postman_collections** directory within the project.
- Select the file **api_tests.postman_collection.json** and click **Open**.

3. **Import the environment variables:**
- Click on the Environment icon ubicated in the upper left.
- Click on the **Import** button located in the upper left corner.
- Select the **Upload Files** tab.
- Click **Choose Files** and navigate to the **postman_collections** directory within the project.
- Select the file **environment_variables.postman_collection.json** and click **Open**.

4. **Establish the request parameters:**
- Go to "Post data trauma through an excel file"/body/"form-data".
- Select an Excel file containing the trauma data you want to process in the ***"file"*** attribute clicking and select the option "New file from local machine".
- Choose a string value for the ***"user"*** attribute, which will define the user who uploaded the file.
- Select a boolean value for the ***"update_data"*** attribute. If set to true, updates will be allowed for existing records in the Postgres database. If false, no updates will be made.
- Select a boolean value for the ***"only_update"*** attribute. If set to true, only updates will be allowed (no new records will be created). If false, both updates and new record creation will be allowed.

5. **Run the collection:**
- Select the imported collection **api_tests**.
- Click on the **Run** button to execute the requests in the collection.
- You can also run individual requests by selecting them and clicking the **Send** button.

## How to make unit tests


1. **Open the terminal in the project root**

2. **Execute the unit tests established in the tests.py files:**
- Apply the next command to execute all unit tests:
```
python manage.py test
```
- If you want to execute only a specific group of tests according with the app, insert the app name, for example:
```
python manage.py test custom_user
```
3. **Calculate the coverage**
- Execute the next command if you want to know the coverage of the unit tests implemented:
```
coverage run manage.py test
```
4. **Generate a report of the coverage**
- To generate a report in HTML, execute the next command:
```
coverage report
```
- Then, execute the HTML project through a web page visualization tool. Tools like Live Server or the NPM package http-server can be used for this purpose. In this case, the http-server tool will be used (you can find its documentation [here](https://www.npmjs.com/package/http-server)).
Run the following command:

```
http-server htmlcov
```
