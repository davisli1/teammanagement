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
* Django: Backend Python framework 

### How to run app on VSCode:
1. Close repository from Github: gh repo clone davisli1/teammanagement
2. Open terminal and use following command to create virtual environment named .venv to run Django 
```
py -3 -m venv .venv
.venv\scripts\activate
```
3. In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:
![command-palette](https://user-images.githubusercontent.com/74220806/181405631-6d41a13a-717b-445a-a976-a27637d157dd.png)

4. From the list, select the virtual environment in your project folder that starts with ./.venv or .\.venv:
![select-virtual-environment](https://user-images.githubusercontent.com/74220806/181405644-e08afd03-f595-44be-a44d-9be8eec2db59.png)
![environment-in-status-bar](https://user-images.githubusercontent.com/74220806/181405692-4b8e255f-0ca0-44ec-b501-eb2f742981a4.png)

5. Install new version of pip and django
```
python -m pip install --upgrade pip
```
```
python -m pip install django
```
6. Run this line of code to set up demo at: http://127.0.0.1:5000/
```
python manage.py runserver 5000
```
7. Enjoy!

### Possible Extensions
* Google authentication: where those deemed admin can actually have the power to delete members
* Unified Search: where you can search for employees on the team

### License
Distributed under the MIT License.
