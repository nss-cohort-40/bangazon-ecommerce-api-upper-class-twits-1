<img src="./images/Bangazon.png" width="100" height="100">
# Bangazon Django REST API
***
A Team Project Built using Python, Django, and the Django REST Framework that ties to our [client-side application](https://github.com/nss-cohort-40/bangazon-ecommerce-client-upperclasstwits).
#####ERD
<img src="./images/ERD.png" width="100" height="100">

---

## Launching the Bangazon API

1. Create a new directory in your terminal of choice
1. Clone down the repository by clicking the "Clone or Download" button
1. In your terminal write: `git clone sshKeyGoesHere`
   conversion tool for writers.

---

Now, set up your virtual environment:

1. `python -m venv bangazonEnv`
1. Activate virtual environment:
   **Mac**
   `source ./bangazonEnv/bin/activate`
   **Windows**
   `source ./bangazonenv/Scripts/activate`
1. Install dependencies:
   `pip install -r requirements.txt`
1. Run migrations:
   `python manage.py migrate`
1. Create a superuser for your local version of the app:
   `python manage.py createsuperuser`
1. **Fixtures??????????**
1. Now Run that Server!
   `python manage.py runserver`
