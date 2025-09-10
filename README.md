# Trauma register backend

## Project Overview
This repository contains the source code for the backend component of a data management application designed for the emergency care context. The system is built to manage a structured dataset of patient information, providing a robust foundation for the application's functionality. <br>
This project is part of a graduation thesis to obtain a degree in Systems Engineering from Universidad del Valle

## Key Features
The backend is structured to support several essential functionalities, organized into three main modules:

1. **Patient Management**: Allows users to interact with individual patient data, facilitating operations such as creating, reading, updating, and deleting records. 🧑‍⚕️

2. **Statistical Visualization**: Processes and prepares data for the generation of statistical charts, offering a clear view of various data dimensions. 📊

3. **Bulk Data Upload**: Enables the efficient upload of large volumes of data, which is crucial for integrating new information into the system.📂

## Project Components
This backend repository is complemented by the frontend repository, which handles the user interface. You can find the frontend project [here](https://github.com/Diego2038/trauma_register_frontend).

**Important clarification**: If you want to run this backend repository with the frontend repository mentioned above, you must modify the ***FRONTEND_PORT*** variable in the .env file with the port that the frontend application has been uploaded to, so that the frontend application can receive the CORS properly and thus the communication works normally.

## Technologies Used

This project is built using a robust and modern technology stack to ensure performance, scalability, and ease of maintenance.

* **Python:** The core language for the backend, version 3.10.0.

* **Django:** The high-level Python web framework that provides the foundational structure for the application.

* **PostgreSQL:** The relational database management system used for data storage, it's recommended to use the version 15.

* **Django REST Framework:** A powerful toolkit for building Web APIs.

* **virtualenv:** The tool used to manage the isolated Python virtual environment.

* **NPM:** Used optionally for serving the HTML test coverage report.

## Considerations
A **.env** file must be created to set the pertinent state variables, just as it is in the **.env.example** file, there the specifications for the connection to the database will be defined via Postgres.<br><br>
In Postgres you have to create a database with the same name as defined in the **.env** file for the ***NAME_DATABASE*** variable to establish the connection between Django and the database in Postgres, also with the username, password, host and port.

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

## How to create an user in this application
Currently the only implemented way to create a user in the application is through Django, for this you must execute the following command:
```
python .\manage.py createsuperuser
``` 
After having entered the ***username***, ***email*** and ***password*** data (it is recommended to fill in the username as admin2 and the password as admin2, since this is how it is set in Postman tests, but any allowed value can be inserted), in order to interact with the application it is strictly necessary to confirm the credentials through the ***username*** and ***password*** that you previously created, so that you can use the authentication token (for more information see follow the steps in the module "How to recreate the postman", and execute the request "Login user" with your credentials).

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

6. **First request:**
-  After you have successfully completed all the steps, look for the ***Login user*** request, modifying the respective ***username*** and ***password*** credentials with which you created in the previous step with the "createsuperuser" command.
- Once this step is completed and the response is an HTTP 200 code, you can execute the other requests. 
- It's not necessary to save the token, since the environment variables you created in the previous steps already store it so it can be automatically used in other requests that require it.

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
