# Web application for determining completed forms.

## Getting Started
The first thing to do is to clone the repository:  
```sh
$ git clone https://github.com/polina-koval/FormWebApp.git
$ cd FormWebApp
```

Create a virtual environment to install dependencies in and activate it:  

```sh
$ virtualenv venv  
$ source venv/bin/activate
```

Then install the dependencies:  

```sh
(venv)$ pip install -r requirements.txt
```
Startup application
```sh
(venv)$ uvicorn main:app --reload 
```
## Main url
- http://127.0.0.1:8000/get_form/ - for post requests.

## Test requests
*  test_main.http if you use PyCharm Professional.
* if you want use command-line:
    ```sh
    (venv)$ python test_requests.py
    ```
## Built with
* [FastAPI](https://fastapi.tiangolo.com/) - The web framework used.
* [TinyDB](https://tinydb.readthedocs.io/en/latest/) - Database.