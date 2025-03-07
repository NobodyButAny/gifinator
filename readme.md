Это простой игрушечный скриптик для наложения текста поверх гифок с помощью ffmpeg. (**Windows**)  

## Структура проекта:
1) **ffmpeg.template.j2**   
Jinja-шаблон команды для ffmpeg. Сердце всего мероприятия, на данный момент там ничего интересного, но работоспособность скриптика зависит от него.

3) **generate.py**  
Python-скрипт просто вставляющий данные в шаблон. Кроме прочего, для удобства, если имеется папка resources, предлагает выбрать картинку оттуда, в ином случае обрабатывает in.gif в корне проекта.

2) **filterconfig.txt**  
Конфигурация с фильтрами, котороая вставляется в шаблон. Вынесена в отдельный файл для удобства. Содержит настройки шрифта, для замены шрифта идти сюда.

3) **text.txt**  
Сам текст, вставляющийся на картинку. Просто строка. Указывается параметром textfile в конфиге фильтра drawtext, а не шаблонизируется в команду - в ином случае не поддерживается unicode и кириллица соответственно (при условии, что шрифт поддерживает unicode).

4) **out.gif**  
Результат исполнения.

## Как запустить?

1) Удостоверьтесь, что у вас установлен ffmpeg и он есть в PATH.  
> **Терминал**  
>  ` >  ffmpeg `  
> ` ffmpeg version 6.1.1 ...`
2) Установите шрифт, подходящий под ваши нужды. Скачайте его (например с Google Fonts) и поместите где-то в папке проекта, после чего укажите путь до него в filterconfig.  
> Например сейчас в **filterconfig.txt** (путь указан от корневой папки)  
> `fontfile=Roboto/Roboto-Regular.ttf`   

3) Положите в корень файл `in.gif` или создайте папку `resources` и поместите туда ваши гифки под любым названием. Напишите желаемый текст в text.txt 

4) Запустите скрипт generate.py (необходим jinja2)