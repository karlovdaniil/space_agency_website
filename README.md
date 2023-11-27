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