<h1 align="center"><a target="_blank">Telegram Bot</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Demo Telegram bot</h3>

- Run the app.py
- ...
- PROFIT

Файлы:
- app.py
        точка входа
- config.py
        токен бота
- handlers.py
        хранятся все хендлеры бота
- keyboards.py
        хранятся клавиатуры бота
- loader.py
        подгрузка переменных бота


Главное меню:
- Посчитать предметы:
        Переводит в меню выбора обьекта и загрузки изображения
- Помощь:
        Переводит в меню помощи

Посчитать предметы:
- Содержит кнопки выбора объекта и назад
- Кнопка выбора объекта открывает WebApp выбора. Пользователь выбирает объект, WebApp закрывается, а его выбор сохраняется в переменную. После необходимо загрузить изображение. Бот вернет заблюреное(обработаное) изображение, так же оно сохраняется в папке static, а в терминал выведется ключ изображения, как заглушка. Если пользователь загружает изображение до выбора WebApp объекта, вылетает ошибка.

Меню выбора бъекта - это вынужденная мера, так как ответ можно получить только от клавиатурных кнопок

