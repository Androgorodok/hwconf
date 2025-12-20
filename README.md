# Домашняя работа

## Вариант 6

Разработан инструмент командной строки для учебного конфигурационного языка. Этот инструмент преобразует текст из входного формата в выходной. Синтаксические ошибки выявляются с выдачей сообщений


Входной текст на учебном конфигурационном языке принимается из стандартного ввода. Выходной текст на языке toml попадает в файл, путь к которому задан ключом командной строки

<img width="622" height="683" alt="image" src="https://github.com/user-attachments/assets/6143e7df-523f-4792-9282-a1ea9dc5682f" />

Для подготовки к запуску нужно следовать следующим инструкциям

```
git clone https://github.com/Androgorodok/hwconf.git
```


```
cd hwconf
```


```
python -m venv .venv
```

```
source .venv/Scripts/activate
```

```
pip install -r requirements.txt
```

Для запуска можно использовать эту команду. Входом является стандартный ввод, а выходом — файл toml

```
python cli.py -o result/config.toml << 'EOF'
port is 8080
number is |port|
host is @"/User"
endpoints is { @"/api", @"/health" }
EOF
```

После запуска в файл config.toml (находится в папке result) запишется результат

<img width="346" height="237" alt="image" src="https://github.com/user-attachments/assets/2af48a3f-3f6f-41f4-875d-9306e8d8b079" />

Дполнительно реализован вход в качестве файла config.conf (находится в папке examples)

```
python cli.py -o result/config.toml < examples/config.conf
```

Входной файл

<img width="492" height="193" alt="image" src="https://github.com/user-attachments/assets/996c80e3-ad03-4fb0-a84c-86ffb84c4571" />

В итоге в файл config.toml запишется результат

<img width="343" height="261" alt="image" src="https://github.com/user-attachments/assets/11ca8e42-dc0e-4d0d-83c6-d3ab3619a4da" />

Для запуска тестов
```
pytest tests/test_basic.py -v
```

<img width="717" height="352" alt="image" src="https://github.com/user-attachments/assets/c46a7211-0ce2-4bbd-a026-b459ee716b94" />

parser.py — разбирает текст (синтаксический анализ)

transformer.py — преобразует дерево в данные (семантический анализ)

cli.py — интерфейс командной строки (чтение ввода/запись вывода)

lark — парсер (строит дерево из текста)

tomli-w — запись TOML (сериализация результата)

argparse — обработка аргументов командной строки

pytest — тестирование (запуск и проверка тестов)
