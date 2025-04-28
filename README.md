<h2>Parser</h2>


<b>Parser</b> - проект, написанный на языке Python c использованием библиотеки Scrapy.<br>

<div>
Приложение ставит перед собой задачу парсинга необходимой URL страницы по её HTML документу и<br>
сохранение информации в удобоваримом формате:
<ul>
    <li>JSON</li>
    <li>CSV</li>
    <li>XML</li>
</ul>
</div>
Страницы необходимые к парсингу сохранены отдельной константой в классе-парсере. 
<br>
<hr>
<div>
<h3>Локальное развёртывание проекта на ОС Windows</h3>

```cmd
    git clone https://github.com/735Andrew/parser 
    cd parser 
    python -m venv venv 
    venv\Scripts\activate
    (venv) pip install -r requirements.txt
    
    (venv) scrapy crawl goods -O result.json   # Создание результурующего файла в формате JSON 
    (venv) scrapy crawl goods -O result.csv    # Создание результурующего файла в формате CSV
    (venv) scrapy crawl goods -O result.xml    # Создание результурующего файла в формате xml
    
    # Файлы с данными будут сохранены в корневой директории проекта
```
</div>
<hr>

