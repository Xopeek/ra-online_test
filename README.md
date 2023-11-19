# Django Авто-каталог
Это мини-проект, созданный с использованием Django, который предназначен для сбора марок и моделей автомобилей из каталога Auto.ru и их сохранения в базе данных. Проект включает в себя две основные функции:

## 1. Обновление каталога Auto.ru

Путь /update_autoru_catalog отвечает за получение марок и моделей автомобилей из каталога Auto.ru и сохранение их в базе данных. В базе данных присутствуют две модели: Mark и Model, при этом модель Model имеет внешний ключ, ссылающийся на модель Mark. База данных реализована с использованием SQLite.

### Детали реализации:
+ Представление update_autoru_catalog вызывается для обновления каталога.
+ Оно получает марки автомобилей из атрибута name тега mark и модели из атрибута name тега folder (до запятой).
+ Представление удаляет предыдущие данные из базы данных и загружает новые при каждом вызове.

Примечание: Ожидается, что в каталоге Auto.ru будет примерно 350 марок и более 3500 моделей.

## 2. Отображение моделей автомобилей по марке
На главной странице отображается форма, которая позволяет пользователям выбирать марку автомобиля. После отправки формы страница показывает модели, соответствующие выбранной марке.

### Функциональность:
+ Пользователь может выбрать марку автомобиля из выпадающего списка.
+ После отправки формы страница отображает модели, соответствующие выбранной марке.

# Используемые технологии:
+ Django
+ SQLite
+ HTML
+ Bootstrap

# Инструкции по настройке:
1. Клонируйте репозиторий:

```bash
git clone git@github.com:Xopeek/ra-online_test.git
```
2. Перейдите в каталог с проектом:
```bash
cd cars
```
3. Создайте виртуальное окружение:
```bash
python -m venv venv
```
Windows:
```bash
venv\Scripts\activate
```
macOS/Linux:
```bash
source venv/bin/activate
```
4. Установите зависимости:
```bash
pip install -r requirements.txt
```
5. Создайте файл .env в корне проекта и добавьте необходимые переменные окружения (см. следующий раздел)
6. Выполните миграции:
```bash
python manage.py migrate
```
7. Запустите сервер:
```bash
python manage.py runserver
```

# Конфигурация переменных окружения (.env)
В корне проекта создайте файл .env и укажите следующие переменные окружения:
```
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
```
Примечание: SECRET_KEY должен быть уникальным и сложным. Не используйте тот, что указан в примере.

# Использование:
1. Перейдите по адресу http://127.0.0.1:8000/update_autoru_catalog/ для обновления каталога Auto.ru.
2. Посетите главную страницу http://127.0.0.1:8000/ для изучения марок и моделей автомобилей


## Работу выполнил Семляков Игорь