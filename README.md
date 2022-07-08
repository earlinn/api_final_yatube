# API YATUBE

## _API социальной сети Yatube_

### Описание проекта API Yatube:

API, позволяющее аутентифицированным пользователям создавать, редактировать 
и удалять записи в социальной сети Yatube, а также просматривать и 
комментировать записи других пользователей и подписываться на других авторов.
Анонимным пользователям доступно чтение чужих записей и комментариев.

Стек: Python 3, Django, Django REST Framework, Simple-JWT, SQLite3.

### Запуск проекта на локальном компьютере:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:earlinn/api_final_yatube.git
cd yatube_api
```

Создать в корневой папке проекта файл с названием ".env" и следующим 
содержанием:

```
SECRET_KEY = <придумайте и впишите секретный ключ>
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env

# для Linux
source env/bin/activate

# для Windows
env\Scripts\activate
# в случае с терминалом bash эта команда может не сработать, тогда следует 
перейти в папку Scripts командой
cd env/Scripts/
# и активировать виртуальное окружение, поставив впереди точку:
. activate

# деактивировать виртуальное окружение можно командой
deactivate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Создать суперпользователя с правами администратора:

```
python3 manage.py createsuperuser
```

Локально запустить проект из папки api_final_yatube/yatube_api/:

```
python3 manage.py runserver
```

Выйти из проекта: Ctrl + C.

### Документация в формате Redoc и пример запроса к API Yatube:

http://127.0.0.1:8000/redoc/

*POST-запрос на публикацию записи*  

{  
&nbsp;&nbsp;&nbsp;&nbsp;"text": "Текст поста",  
&nbsp;&nbsp;&nbsp;&nbsp;"image": "картинка",  
&nbsp;&nbsp;&nbsp;&nbsp;"group": 1  
}  

*Ответ API в случае успешной публикации записи*  

{  
&nbsp;&nbsp;&nbsp;&nbsp;"id": 1,  
&nbsp;&nbsp;&nbsp;&nbsp;"author": "Я",  
&nbsp;&nbsp;&nbsp;&nbsp;"text": "Текст поста",  
&nbsp;&nbsp;&nbsp;&nbsp;"pub_date": "2019-08-24T14:15:22Z",  
&nbsp;&nbsp;&nbsp;&nbsp;"image": "картинка",  
&nbsp;&nbsp;&nbsp;&nbsp;"group": 1  
}  

### Авторы

[Галина Волкова](https://github.com/earlinn/) и Яндекс.Практикум
