# Интернет-магазин "Online Shop"

Добро пожаловать в репозиторий интернет-магазина "Online Shop". Этот проект создан в рамках моей дипломной работы и представляет собой полноценное веб-приложение для электронной коммерции.

## Описание проекта

"Online Shop" - это современный интернет-магазин, разработанный с использованием фреймворка Django на языке программирования Python. Проект включает в себя все необходимые компоненты для успешного функционирования электронного бизнеса.

## Основные функциональности

- **Управление каталогом товаров:** Добавление, редактирование и удаление товаров в удобной административной панели.

- **Оформление заказов:** Простой и интуитивно понятный процесс заказа с возможностью выбора количества товара.

- **Аутентификация и авторизация:** Личный кабинет для пользователей, отслеживание истории заказов.

## Технологии и инструменты

- **Django:** Использован для быстрой разработки и создания мощных веб-приложений.

- **SQLite:** Компактная база данных, выбранная для удобства разработки и тестирования.

- **HTML, CSS, JavaScript:** Фронтенд разработан с использованием стандартных веб-технологий.

## Установка и запуск

1. Клонируйте репозиторий на свой компьютер:

```git clone git@github.com:Fananad/shop_django.git```

2. Установка виртуальной среды

```python3 -m venv venv```

3. Установка зависимостей

```pip install -r requirements.txt```

4. Проведение миграций 

```python3 manage.py makemigrations && python3 manage.py migrate```

5. Заполни .env токенном который использует приложение (шаблон файла приведен в корне)

6. Запуск приложения

```python3 manage.py runserver```


