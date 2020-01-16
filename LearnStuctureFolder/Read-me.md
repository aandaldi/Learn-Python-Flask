structure:
~~~
|--app.py               #main, called web server is start
|--requirements.txt     #file of pip install statements for your app
|--migrations           #folder created for migrations by calling
|--myproject            #main project folder, sub-components will be in separate folders
|  |  __init__.py
|  |  model.py
|  |  data.sqlite
|  |
|  |--app1
|  |  |  views.py
|  |  |
|  |  |--templates
|  |     |--app1
|  |        |  add_app1.html
|  |
|  |--app2
|  |  |  views.py
|  |  |
|  |  |--templates
|  |  |  |--app2
|  |          add_app2.html
|  |
|  |--static            # where you store your CSS, JS, Image,Fonts, Etc
|  |--templates
|  |  |  index.html
|  |  |  base.html 
~~~


run on CLI:
```flask db init```