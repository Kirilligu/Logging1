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
### После запуска приложений у вас автоматически создатутся файлы с логами
Для проверки логов на корректность восользуйтесь кодом checkLoogs
- Запустите в отедльном окне checkLogs
```
python checkLogs.py  
```
если логи впорядке, то он выведет True
![image](https://github.com/Kirilligu/Logging1/assets/149255706/d41945f7-1358-4a54-88a0-68012ff42954)
