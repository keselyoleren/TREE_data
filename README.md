# Tree Data

# Instalasi
```
$ git clone https://github.com/keselyoleren/TREE_data.git
$ cd TREE_data

$ configure .env file

# generate database
$ paython src/manage.py makemigrations
$ paython src/manage.py migrate

# create super user
$ paython src/manage.py createsuperuser

# runserver
$ paython src/manage.py runserver

```


# Api URl
```
# http//:localhost:8000/api/orang/ method [GET, CREATE, UPDATE, DELETE]
```

# visualisasi data
```
# http://localhost:8000/
```
![vis data tree](https://github.com/keselyoleren/TREE_data/blob/master/vis_tree.png)



# struktur folder
```
├── dump.rdb
├── media
├── src
│   ├── app
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── admin.cpython-36.pyc
│   │   │   ├── apps.cpython-36.pyc
│   │   │   ├── models.cpython-36.pyc
│   │   │   ├── router.cpython-36.pyc
│   │   │   └── views.cpython-36.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-36.pyc
│   │   │       └── __init__.cpython-36.pyc
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── serializers
│   │   │   ├── __pycache__
│   │   │   │   ├── comment.cpython-36.pyc
│   │   │   │   ├── replies.cpython-36.pyc
│   │   │   │   └── user.cpython-36.pyc
│   │   │   ├── comment.py
│   │   │   ├── replies.py
│   │   │   └── user.py
│   │   ├── tests.py
│   │   └── views
│   │       ├── __pycache__
│   │       │   ├── comment.cpython-36.pyc
│   │       │   └── replies.cpython-36.pyc
│   │       ├── comment.py
│   │       └── replies.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── settings.cpython-36.pyc
│   │   │   ├── urls.cpython-36.pyc
│   │   │   └── wsgi.cpython-36.pyc
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── helper
│   │   ├── __pycache__
│   │   │   └── pagination.cpython-36.pyc
│   │   └── pagination.py
│   ├── manage.py
│   └── middleware
│       ├── __pycache__
│       │   └── middleware_response.cpython-36.pyc
│       └── middleware_response.py
├── static
└── templates
└── .env

```

## keterangan
### ** ```src``` smua app dimasukkan ke dalam folder ini
### ** ```helper``` berisi smua file pembantu
### ** ```middleware``` berisi file untuk mnyamakan format reponse api
### ** ```.env``` file untuk enviroment agar lebih mudah di gunakan oleh beberapa dev

## format api yang biasa saya gunakan
```

  [1] success 
      {
        "data": {
          "results": [
          ],
          "meta": {
            "current_page": 1,
            "next_page": null,
            "previous_page": null,
            "count": 1
          }
        },
        "message": "Success",
        "status": 200,
        "success": true
      }

  [2] failed
      {
        "data":{
           "status": 400,
           "success": false,
           "message": "The failed message",
           "result": {}
        }        
      }
```


## Query untuk mendapatkan anak Budi
```
# Queryset
Orang.objects.all()

# SQL Query
SELECT `app_orang`.`id`, `app_orang`.`parent_id`, `app_orang`.`nama`, `app_orang`.`jenis_kelamin` FROM `app_orang`
```


## Query untuk mendapatkan cucu Budi
```
  #get parent 
  for x in Orange.objects.filter(parent__nama="budi"):
      #get semua cucu budi
    cucu  = Orang.objects.filter(parent__id=x.id)
```

## Query untuk mendapatkan cucu perempuan dari Budi
```
  #get parent 
  for x in Orange.objects.filter(parent__nama="budi"):
      #get semua cucu budi
    cucu  = Orang.objects.filter(parent__id=x.id, jenis_kelamin="Perempuan")
```

## Buat query untuk mendapatkan bibi dari Farah
``` 
  for x in Orange.objects.filter(parent__nama="budi", jenis_kelamin="perempuan"):
    print(x.nama)   
```

## Buat query untuk mendapatkan sepupu laki-laki dari Hani
```
for x in Orange.objects.filter(parent__nama="budi"):
    cucu  = Orang.objects.filter(parent__id=x.id, jenis_kelamin="Laki - Laki")

```

