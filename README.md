# Space_agency_website
Лендинг сайта космического агентства
https://www.figma.com/file/csU67B0SQVZO1AkwvMZa3D/Тестовое-задание-N2?type=design&node-id=602-278&mode=design&t=ls2U31IYBsaP6RWh-0

## Стек: python 3.9, Django 4.1, MySQL 8, bootstrap 5

---

### Запуск контейнера MySQL
```bash
cd MySQL
docker compose up -d --build
```

### Применение миграций (из корня проекта)
```bash
python manage.py migrate
```

### Запуск Django приложения
```bash
python manage.py runserver
```

### Функциональные особенности

- для сборки клиентской части страницы использован bootstrap 5.
- на странице применен слайдер slick slider http://kenwheeler.github.io/slick/ (см. Slider Syncing).
- по клику на большую фотографию на слайдере фотографии открываются на весь экран и листаются галереей.
- slider заполнялся через админку django. Настроен визуально понятный admin.py, выводится картинка и название в списке записей элементов слайдера.
- для картинок модели слайдера необходимо использован пакет django-filer и через него загружаются картинки в слайдер.
- записи слайдера в админке сортируются при помощи drag&drop (использовать пакет django-admin-sortable2).
- все зависимости для запуска проекта находятся в файле req.pip в корне проекта.
