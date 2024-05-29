# Логирование
Для работы приложения треубется:
1. Запустить user_service
```
uvicorn user_service:app
```
2. Запустить publisher и subscriber
```
python subscriber.py
python publisher.py 
```
Все приложения запускайте в разных терминалах, для корректной работы программы!
