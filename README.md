# Вопросы для викторины

В сервисе реализовано REST API, принимающее на вход POST запросы с содержимым вида 
```
{"questions_num": integer}
```
После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.

Полученные ответы сохраняются в базе данных, сохранена следующая информация: 
1. ID вопроса
2. Текст вопроса
3. Текст ответа
4. Дата создания вопроса
В случае, если в БД имеется такой же вопрос, к публичному API с викторинами выполняются дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.

Ответом на POST запрос {"questions_num": integer} является предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

## Настройка и запуск сервиса

1. Клонируйте репозиторий к себе на компьютер с помощью команды:

```
git clone https://github.com/AleksSpace/Questions_for_quiz.git
или
git clone git@github.com:AleksSpace/Questions_for_quiz.git
или
git clone gh repo clone AleksSpace/Questions_for_quiz
```

2. Создайте виртуальное окружение и активируйте его с помощью команды:

```python -m venv venv``` - создаём окружение

```. venv/Scripts/activate``` - ативируем

3. Переходим в папку infra/

```cd infra/```

4. Запускаем сборку докер оброза командой:

```docker-compose up -d --build```

# Всё, сервис работает!!!

# Для его проверки воспользуемя приложением Postman.

Заходим в приложение, и делаем POST запрос по адресу

```http://localhost/api/questions_num```

В теле запроса прописываем:

```
{"questions_num": integer}
```
где integer - это количество вопросов

