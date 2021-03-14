# Algo-Phantom-Backend

<img src="https://i.ibb.co/CvN6XxK/backend-final.png" alt="backend final.png" align="center" width="1080" />

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![Maintenance](https://img.shields.io/maintenance/yes/2021) 
  
![GitHub Repo stars](https://img.shields.io/github/stars/Algo-Phantoms/Algo-Phantoms-Backend?style=social) 
![GitHub forks](https://img.shields.io/github/forks/Algo-Phantoms/Algo-Phantoms-Backend?style=social)

#### 💻 Algo-Phantoms-Backend is an Application that provides pathways and quizzes along with a code editor to help you towards your DSA journey.📰🔥 This repository contains the REST APIs of the application.✨

## 🔥 Features
📰 Write and edit your code in our application.

✨ Play quizzes to improve your DSA fundamentals.

🚀 Give your DSA journey a proper guide using pathways in our application.

## 🛠 Tech Used

<img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img alt="Django" src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/> <img alt="Django Rest Framework" src="https://img.shields.io/badge/django rest framework%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/>

## 💫 Quick Start

- Fork and Clone the repository using-
```
git clone https://github.com/Algo-Phantoms/Algo-Phantoms-Backend.git
```
- Create a Branch- 
```
git checkout -b <branch_name>
```
- Create virtual environment-
```
python -m venv env
env\Scripts\activate
```
- Install dependencies using-
```
pip install -r requirements.txt
```
*If you have python2 and python3 installed you need to specify python3 by using command:*
```
python3 -m pip install -r requirements.txt
```

- Headover to Project Directory- 
```
cd AlgoPhantomBackend
```
- Make migrations using-
```
python manage.py makemigrations
```
*If you have python2 and python3 installed you need to specify python3 by using command:*
```
python3 manage.py makemigrations
```

- Migrate Database-
```
python manage.py migrate
```
- Create a superuser-
```
python manage.py createsuperuser
```
- Run server using-
```
python manage.py runserver
```
- Push Changes-
```
git add .
git commit -m "<your commit message>"
git push --set-upstream origin <branch_name>
```
## Project Architecture
```
ALGO-PHANTOMS-BACKEND                             # Project Name
|
├───AlgoPhantomBackend                            # Project Directory
|   |
|   └──__pychache__                               # Cache Folder            [Default]
|   ├──__init__.py                                #                         [Default]
|   ├──asgi.py                                    #                         [Default]
|   ├──settings.py                                #                         [Default]
|   ├──urls.py                                    #                         [Default]
|   └──wsgi.py                                    #                         [Default]
|
├───core                                          # Core App Directory
|   |
|   └──migrations                                 # Migrations                   
|   ├──_init__.py              
|   ├──admin.py                                   #                         [Default]
|   ├──apps.py                                    # Define App name         [Default]
|   ├──models.py                                  # Create models           [Default]
|   ├──serializers.py                                                       [Created]
|   ├──signals.py                                                           [Created]
|   ├──tests.py                                   # Test                    [Default]
|   ├──tokens.py                                  #                         [Created]
|   ├──urls.py                                    #                         [Created]
|   ├──utils.py                                   #                         [Created]
|   └──views.py                                   #                         [Default]
|
├───quiz                                          # Quiz App Directory
|   |
|   └──migrations                                 #                         [Default]
|   ├──_init__.py                                 #                         [Default]
|   ├──admin.py                                   #                         [Default]
|   ├──apps.py                                    #                         [Default]
|   ├──models.py                                  #                         [Default]
|   ├──serializers.py                             #                         [Created]
|   ├──tests.py                                   #                         [Default]
|   ├──urls.py                                    #                         [Created]
|   └──views.py                                   #                         [Default]
|
├──manage.py                                      #                         [Default]
└──requirements.txt                               #                         [Created]


```

## ⚙️ Contribution Guidelines 

* Make sure you do not copy codes from external sources because that work will not be considered. Plagiarism is strictly not allowed.
* You can only work on issues that you have been assigned to you.
* If you want to contribute, we prefer that you create an issue before making a PR and link your PR to that issue.
* If you have modified/added code work, make sure the code compiles before submitting.
* Do not update the **[README.md](https://github.com/Algo-Phantoms/Algo-Phantoms-Backend/blob/main/README.md).**

## 📖 Code Of Conduct:

You can find our Code of Conduct [here](https://github.com/Algo-Phantoms/Algo-Phantoms-Backend/blob/main/CODE_OF_CONDUCT.md).

## 📝 License  

This project follows the [MIT License](https://choosealicense.com/licenses/mit/).

## 😇 Maintainers 
<table>
  <tbody><tr>
    <td align="center"><a href="https://github.com/diyajaiswal11"><img alt="" src="https://avatars.githubusercontent.com/diyajaiswal11" width="100px;"><br><sub><b> Diya Jaiswal</b></sub></a><br><a href="https://github.com/Algo-Phantoms/Algo-Tree/commits?author=diyajaiswal11" title="Code">💻 </a></td> </a>
  </td>
  
 <td align="center"><a href="https://github.com/prajul007"><img alt="" src="https://avatars.githubusercontent.com/prajul007" width="100px;"><br><sub><b> Prajul Gupta </b></sub></a><br><a href="https://github.com/Algo-Phantoms/Algo-Tree/commits?author=prajul007" title="Code">💻 </a></td></a></td>
 
 <td align="center"><a href="https://github.com/hmangukia"><img alt="" src="https://avatars.githubusercontent.com/hmangukia" width="100px;"><br><sub><b> Hetal Mangukia</b></sub></a><br><a href="https://github.com/Algo-Phantoms/Algo-Tree/commits?author=hmangukia" title="Code">💻 </a></td> </a>
  </td>
  
  <td align="center"><a href="https://github.com/harsh-9in"><img alt="" src="https://avatars.githubusercontent.com/harsh-9in" width="100px;"><br><sub><b> Harsh Kumar</b></sub></a><br><a href="https://github.com/Algo-Phantoms/Algo-Tree/commits?author=harsh-9in" title="Code">💻 </a></td> </a>
  </td>
 
  </tr>
</tbody></table>


## If you liked the project don't forget to star 🌟 and fork 🍽 the project.

<h2 align="center">Made with ❤ by Algo Phantoms</h2>


[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)

