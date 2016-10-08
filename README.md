# django-capitxula

This project generate captchas based on image figures. Initial idea is make question like:

```
What figures on this square is fruits?
```

And user click on fruits to system accept captcha.

## What install to contribute with this project?

Clone this project:

```
$ git clone git@github.com:rafaelhenrique/django-capitxula.git
```

Create an virtualenv (i prefer [virtualenv-wrapper](https://virtualenvwrapper.readthedocs.org/en/latest/ "virtualenv-wrapper")):

```
$ mkvirtualenv django-capitxula
```

Install requirements:

```
$ pip install -r requirements.txt
```

Run example project to simulate capitxula in action:

```
$ cd example
$ python manage.py runserver
```

Access [http://localhost:8000](http://localhost:8000) on your browser to see capitxula in action!

## Why django-capitxula is called django-capitxula?

1. Because integrate with Django;
2. On song [Pelados em Santos](https://www.youtube.com/watch?v=rmMj8UC5Mig) the band `Mamonas Assassinas` mention `my dear` as `my pitxula`;
3. The sound of word `Captcha` remember `Pitxula`.

... and is a tribute to `Mamonas Assassinas` band and Brazilian culture! 

That's all folks!
