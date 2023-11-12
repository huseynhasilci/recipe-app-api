# recipe-app-api
docker-compose run --rm app sh -c "flake8" flake8 çalıştırma kodu

docker-compose run --rm app sh -c "django-admin startproject app ." bununlar docker üzerinden projeyi başlattık

docker-compose up ile projeyi ayağa kaldırdık.

docker-compose --rm app sh -c "python manage.py makemigrations" -- migrationları yaptık

docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate" -- database için migrate yaptık ancak bunu çalıştırınca docker volumeler ile karşılaşabiliriz bunun çözümü de şu şekilde

docker volume rm recipe-app-api_dev-db-data
Error response from daemon: remove recipe-app-api_dev-db-data: volume is in use - [be9c83c7105ae6bc8e11d7ff325561577f011ffbc26a11361df5e4fd30d78204] bu hatayı atacak biz de 

docker-compose down yapacağız ardından 

docker volume rm recipe-app-api_dev-db-data bunu çalıştıracağız

docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate" bunu çalıştırıp migration yaptık 