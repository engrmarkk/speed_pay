# Speed_Pay

<!-- Back to Top Navigation Anchor -->

<a name="readme-top"></a>


<!-- https://user-images.githubusercontent.com/100721103/200149633-373db975-c47f-43a7-9288-f6cbd16e0410.mp4 -->

<br><br>
<!-- Project Shields -->
<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Twitter][twitter-shield]][twitter-url]

[//]: # ([![Twitter][twitter-shield2]][twitter-url2])

</div>

<br />

<div>
  <p align="center">
    <a href="https://github.com/engrmarkk/Scissor API#readme"><strong>Explore the docs »</strong></a>
    <br />
    ·
    <a href="https://github.com/engrmarkk/Scissor API/issues">Report Bug</a>
    ·
    <a href="https://github.com/engrmarkk/Scissor API/issues">Request Feature</a>
  </p>
</div>

---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-Scissor API">About the project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#features">Features</a></li>
      </ul>
     <!-- <li><a href="#demo">Demo</a></li> -->
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
         <li><a href="#endpoints">Endpoints</a></li>
      </ul>
    <!-- <li><a href="#shots">Shots</a></li> -->
    <li><a href="#contact">Contact</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the api -->

## About The Project

The API is a secure and efficient financial transaction service built with Django Rest Framework. The platform enables users to conduct seamless and reliable fund transfers, and balance inquiries. With the API, managing your finances becomes effortless, ensuring a smooth experience for individuals.

### Features
- Secure Authentication: SpeedPay offers robust user authentication, ensuring that your financial information remains safe and accessible only to you.

- Automatic Account Generation: When you create an account, a unique 10-digit account number is automatically generated for you, simplifying transactions and enhancing security.

- Convenient Fund Transfers: Send funds to other users' accounts effortlessly with our user-friendly transfer endpoint. Whether it's a friend, or family member, transferring money is quick and hassle-free.

- Real-time Balance Inquiries: Keep track of your account balance in real-time. The API allows you to check your available balance at any moment, ensuring you have full control over your finances.

<p align="right"><a href="#readme-top">back to top</a></p>



### Built With:

![Python][python]
![Django][django]
![DjangoRest][djangorest]

[//]: # (<p align="right"><a href="#readme-top">back to top</a></p>)

[//]: # (---)

[//]: # (## Demo)

[//]: # ()
[//]: # (https://user-images.githubusercontent.com/100721103/225929529-95040462-f36d-4880-854c-c89b4bac6d33.mp4)

[//]: # ()
[//]: # (<br><p align="right"><a href="#readme-top">back to top</a></p>)

---
<!-- Lessons from the Project -->

[//]: # (## Exposure)

[//]: # ()
[//]: # (Creating this project got me more exposed to:)

[//]: # ()
[//]: # (- Debugging)

[//]: # (- Restful API)

[//]: # (- Thorough research)

[//]: # (- Database Management)

[//]: # (- Authentication)

[//]: # (- Authorization)

[//]: # (- Endpoint restriction)

[//]: # (- Testing with unittest)

[//]: # (- Swagger UI)

[//]: # (- API Documentation)

[//]: # (- Integration with React)

<p align="right"><a href="#readme-top">back to top</a></p>

[//]: # (---)

<!-- GETTING STARTED -->

## Usage

To get a local copy up and running, follow the steps below.

### Prerequisites

Python3: [Get Python](https://www.python.org/downloads/)

### Installation

1. Clone this repo
   ```sh
   git clone https://github.com/engrmarkk/speed_pay.git
   ```
2. Navigate into the directory
   ```sh
   cd speed_pay
   ```
3. Create a virtual environment
   ```sh
   python -m venv your_venv_name
   ```
4. Activate the virtual environment on powershell or cmd
   ```sh
   your_venv_name\Scripts\activate.bat
   ```
   On Bash ('Scripts' for windows, 'bin' for linux)
   ```sh
   source your_venv_name/Scripts/activate.csh
   ```
5. Install project dependencies
   ```sh
   pip install -r requirements.txt
   ```
6. Create SQLite database
   ```sh
   python manage.py makemigrations speedpay
   python manage.py migrate
   ```

8. Run App
   ```sh
    python manage.py runserver
   ```
9. Use the link generated on the terminal to access the endpoints
    ```sh
   http://127.0.0.1:8000
   ```
   To use swagger-ui, use the link below
   ```sh
    http://127.0.0.1:8000/
   ```
   <br>
### Project structure
   ```
   .
   ├── README.md
   ├── .gitignore
   ├── LICENSE
   ├── speed_app
   │   ├── __init__.py
   │   ├── endpoints
   │   │   ├── __init__.py
   │   │   ├── auth.py
   │   │   └── users.py
   │   ├── models
   │   ├── apps.py
   │   ├── managers.py
   │   ├── serializers
   │   ├── tests.py
   │   └── urls.pyy
   ├── speed_proj
   │   ├── __init__.py
   │   ├── asgi.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── your_venv_name
   ├── manage.py
   ├── Your_sqlite_database
   └── requirements.txt
   ```  


### Endpoints
<br>
POST (Register) http://127.0.0.1:8000/api/register

REQUEST
```json
{
  "firstname": "string",
  "password1": "string",
  "password2": "string",
  "email": "string@string.com",
  "username": "string",
  "lastname": "string",
}
```

[//]: # (RESPONSE)

[//]: # (```json)

[//]: # ({)

[//]: # (    "id": 1,)

[//]: # (    "first_name": "string",)

[//]: # (    "password": "string",)

[//]: # (    "email": "string@string.com",)

[//]: # (    "last_name": "string")

[//]: # (})

[//]: # (```)
POST (Login) http://127.0.0.1:8000/api/login

REQUEST
```json
{
  "email": "user@example.com", 
        'or'
  "username": "string",
  "password": "string"
}
```
RESPONSE
```json
  {
    "key": "eyJhbGciOiJIUzIEyM...................",
  }
```

POST (Send fund) http://127.0.0.1:8000/api/send-fund <br/>
@login_required

REQUEST
```json
{
  "transaction_amount": 0,
  "transact_user_account": 0
}
```
RESPONSE
```json
  {
  "message": "Funds transferred successfully"
}
```

POST (Deposit) http://127.0.0.1:8000/api/deposit <br/>

REQUEST
```json
{
  "transaction_amount": 1000
}
```
RESPONSE
```json
  {
  "message": "Funds deposited successfully"
}
```

GET (Check Balance) http://127.0.0.1:8000/api/check-balance <br>
@login_required

RESPONSE
```json
{
  "message": "Your balance is $1000"
}
```

GET (Get all users) http://127.0.0.1:8000/api/users <br>
@admin_required

RESPONSE
```json
  [
  {
    "id": 1,
    "firstname": "string",
    "lastname": "string",
    "username": "string",
    "email": "user@example.com",
    "phone": "091.....",
    "account_number": 91900000,
    "balance": 1200
  },
  {
    "id": 2,
    "firstname": "string",
    "lastname": "string",
    "username": "string1",
    "email": "user1@example.com",
    "phone": "091.....",
    "account_number": 31320000,
    "balance": 2000
  },
  {
    "id": 3,
    "firstname": "string",
    "lastname": "string",
    "username": "speedpay",
    "email": "user1@speedpay.com",
    "phone": "081.....",
    "account_number": 7180000,
    "balance": 1000
  }
]
```

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Sample Screenshot -->

<!-- ## Shots -->

<!-- <br /> -->
<!-- <p>Light Mode</p> -->

<!-- [![My Blog Project Screenshot][Quiz_Api-screenshot]](https://github.com/engrmarkk/Quiz_Api/blob/main/static/images/screen-light.png) -->

<!-- <br/> -->
<!-- <p>Dark Mode</p> -->

<!-- [![My Blog Project Screenshot][Quiz_Api-screenshot2]](https://github.com/engrmarkk/Quiz_Api/blob/main/static/images/screen-dark.png) -->

[//]: # (<br/>)

[//]: # (<p align="right"><a href="#readme-top">back to top</a></p>)


<!-- Contact -->

## Contact

Adeniyi Olanrewaju - [@iamengrmark](https://twitter.com/iamengrmark) - adeniyiboladale@yahoo.com <br>

[//]: # (Gabriel Kalango - [@GabrielKalango]&#40;https://twitter.com/GabrielKalango&#41; - kallythegreat11@gmail.com)

Project Link: [SpeedPay Test Api](https://github.com/engrmarkk/speed_pay) <br>

Live Link: [Cut Live](https://cut-ox14.onrender.com/)

<p align="right"><a href="#readme-top">back to top</a></p>

---


<!-- Markdown Links & Images -->

[contributors-shield]: https://img.shields.io/github/contributors/engrmarkk/Academia-API.svg?style=for-the-badge
[contributors-url]: https://github.com/engrmarkk/Academia-API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/engrmarkk/Academia-API.svg?style=for-the-badge
[forks-url]: https://github.com/engrmarkk/Academia-API/network/members
[stars-shield]: https://img.shields.io/github/stars/engrmarkk/Academia-API.svg?style=for-the-badge
[stars-url]: https://github.com/engrmarkk/Academia_API/stargazers
[issues-shield]: https://img.shields.io/github/issues/engrmarkk/Academia-API.svg?style=for-the-badge
[issues-url]: https://github.com/engrmarkk/Academia-APIissues
[license-shield]: https://img.shields.io/github/license/engrmarkk/Academia-API.svg?style=for-the-badge
[license-url]: https://github.com/engrmarkk/Academia-API/blob/main/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/-@iamengrmark-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/iamengrmark
[twitter-shield2]: https://img.shields.io/badge/-@GabrielKalango-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/GabrielKalango
[twitter-url]: https://twitter.com/iamengrmark
[postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[twitter-url2]: https://twitter.com/GabrielKalango
[Quiz_Api-screenshot]: static/images/screen-light.png
[Quiz_Api-screenshot2]: static/images/screen-dark.png
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[djangorest]: https://img.shields.io/badge/django_rest_framework-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[jinja]: https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black
[html5]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[css3]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[javascript]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[bootstrap]: https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white
