# teammanagement
Web app for team management
Built by Davis Li for Instawork

### About the Project:
During the interview process for Instawork, I was asked to create a full-stack team management web-app using Django. This took me about 2 days of time while working a full-time job

### Features
1. Users should be able to view all employees with total count at top
2. Users should be able to add new employee with information fields
3. Users should be able to edit employees

### How I approached it:
Right off the bat I realized I needed to create a database that stores the fields of the employee (first name, last name, email, phone.etc), so I started with models and built out that class. I decided to use class-based views because of its ability to inherit another class and that I don't have to repeat code. After that I went ahead to create the employee list page 

### Built With
* Django: Backend framework to develop database

### Future Features
* Google authentication: where those deemed admin can actually have the power to delete members
* Unified Search: where you can search for employees on the team