# Project Setup

To start your Project on your local system :

  * create python virtual environment `python -m venv name_env`
  * Activate environment mac `source name_env/bin/activat`
  * Activate environment window `.\name_env\Scripts\activate`
  * Install dependencies `pip install -r requirements.txt`
  * Collect static files `python manage.py collectstatic`
  * Use the following function to generate secret key for your project
  * `django.core.management.utils.get_random_secret_key()`
  * create .env file in your project directory and add your secret keys like this
```
    SECRET_KEY=<"YourSecretKey">
    OPEN_WEATHER_API_KEY=<"Yourapikey">>
```



To run project on your local system : `python manage.py runserver`

## Run Project On Docker
Make sure docker is installed on your local system. Run the command
`docker compose up`