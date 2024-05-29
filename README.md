# Логирование
### Перед запуском требуется установить:
#### 1. uvicorn
```
 pip install uvicorn
```
#### 2. requests
```
pip install requests
```
#### 3. paho-mqtt
```
pip install paho-mqtt==1.5.1
```

### Для работы приложения треубется:
#### 1. Запустить user_service
```
uvicorn user_service:app
```
![image](https://github.com/Kirilligu/Logging1/assets/149255706/f6cb8076-5827-4969-accf-556d98839dc7)

#### 2. Запустить publisher и subscriber
```
python subscriber.py
python publisher.py 
```
![image](https://github.com/Kirilligu/Logging1/assets/149255706/1feb3cdf-fff0-4a37-b2c9-670898350bc8)
![image](https://github.com/Kirilligu/Logging1/assets/149255706/7dda57f4-7394-43ba-ba36-4ac441be6233)

## Все приложения запускайте в разных терминалах, для корректной работы программы!

### После запуска приложений у вас автоматически создатутся файлы с логами
Для проверки логов на корректность восользуйтесь кодом checkLoogs
- Запустите в отедльном окне checkLogs
```
python checkLogs.py  
```
если логи впорядке, то он выведет True
![image](https://github.com/Kirilligu/Logging1/assets/149255706/d41945f7-1358-4a54-88a0-68012ff42954)

### Пример содержание файлов
- user_service
  ![image](https://github.com/Kirilligu/Logging1/assets/149255706/a0c40346-ae5c-42d7-a04e-fd29a7995172)
- publisher
  ![image](https://github.com/Kirilligu/Logging1/assets/149255706/4f887b1d-3bca-48b2-a9dd-d9f6e494ae9d)
- subscriber
  ![image](https://github.com/Kirilligu/Logging1/assets/149255706/773ddacd-76a9-4daf-9133-b4d35f893db0)
- общий файл со всеми логами (common.log)
  ![image](https://github.com/Kirilligu/Logging1/assets/149255706/f59471e3-38ab-40cb-a6b0-b7c3afb9153e)



