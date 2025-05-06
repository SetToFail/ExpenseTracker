# Expense Tracker

## Описание

Это простое приложение для отслеживания расходов.  Оно позволяет пользователям добавлять расходы, категоризировать их и просматривать отчеты.

## Функциональность

*   Добавление расходов с указанием суммы, категории и описания.
*   Просмотр списка всех расходов.
*   Генерация ежедневных, еженедельных и месячных отчетов.

## Установка

1.  Установите Python 3.
2.  Установите Flask: `pip install flask`
3.  Клонируйте репозиторий: `git clone https://github.com/SetToFail/ExpenseTracker`
4.  Перейдите в директорию проекта: `cd expense_tracker`
5.  Запустите приложение: `python app.py`

## Запуск

Откройте браузер и перейдите по адресу `http://127.0.0.1:5000/`.

## Скриншоты

![image](https://github.com/user-attachments/assets/b283f2e2-98f3-427a-9285-6c1edc902cff)
![image](https://github.com/user-attachments/assets/706b726b-5938-4507-853f-97e5954b475a)
![image](https://github.com/user-attachments/assets/b92559aa-a7d9-4dbf-87dc-999781df4f81)
![image](https://github.com/user-attachments/assets/0478e790-6b76-4a74-9ad0-198f86a97f50)





## Использованные технологии

*   HTML5
*   Python
*   Flask
*   SQLite
*   Bootstrap (CDN)

## Архитектура

Приложение использует следующую архитектуру:

*   UI (Flask)
*   ExpenseController
*   ExpenseService
*   ExpenseRepository
*   Data Storage (SQLite)

## Паттерны проектирования

*   **Repository:**  Абстрагирует доступ к данным, позволяя легко заменять источник данных.
*   **Factory Method:**  Используется для создания различных типов генераторов отчетов.
*   **Dependency Injection:** Контроллер получает зависимости через конструктор.
