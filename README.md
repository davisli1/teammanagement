# Team Member Management Application

### About the Project:
A simple team-member management application built using Django that allows the user to view, edit, add, and delete team members. View video demo below:
Built for the interview process for Instawork, approximate time taken = 2 days

![Video_thumbnail](https://user-images.githubusercontent.com/74220806/181405393-094ba0e6-a0b5-4da3-8e93-dfe9b1161b35.png)

### Project Demo
https://user-images.githubusercontent.com/74220806/181405328-9fed535f-d7d9-416f-a0f4-2454dfc55b6d.mp4

### Features
* Users should be able to view all employees with total count at top
* Users should be able to add new employee with information fields
* Users should be able to edit employees

### Built with:
* Django: Backend framework to develop database
* HTML: For frontend

### How to run app on VSCode:
1. Close repository from Github: gh repo clone davisli1/teammanagement
2. Open terminal and use following command to create virtual environment named .venv to run Django 
```
py -3 -m venv .venv
.venv\scripts\activate
```
3. In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:
4. From the list, select the virtual environment in your project folder that starts with ./.venv or .\.venv:
5. Install new version of pip and django
```
python -m pip install --upgrade pip
```
```
python -m pip install django
```
6. Run this line of code to set up demo at: http://127.0.0.1:8000/
```
python manage.py runserver 5000
```
8. Enjoy!
