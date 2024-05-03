[documantation tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)

```bash
python -m venv env
source env/bin/activate
pip install django

django-admin startproject config .

python manage.py runserver
```

- create multi apps for functions

```bash
python manage.py startapp my_app
```

- add my_app to config/settings.py
- add my_app/views 
- add config/urls
- Url:view is paired, Path will match from top to buttom



### like Make Pizzas:

- 厨房点餐：urls
- 厨房制作：views（functions）
- 披萨的味道和材料选择：parameters
- 制作工艺和流程定制：templates（html blueprints）

### Template language:

- Variables -> {{blog_title}}
- Tags -> {%if has_title%}
- Filters -> {{blog_title|title}}
- 'APP_DIRS': True : means templates are in app folders
- Templates folder: app/templates/app/index.html

Template Inheritance:

- html的层级使得child可以复用上一层的template。
- skeleon骨架 - 包括block - child的block可以覆盖被继承的template的内容
- 在哪里用？那些不变的地方比如navigator，footer之类的。

### Push to Github:

- Settings:host allows * , not good just for fun
- pip install gunicorn，安装web服务器
- pip freeze > requirements.txt
- add ignore file
- push to Github repo

要在服务器上正常host图片等静态文件需要安装一些库比如whitenoise。

- pip install whitenoise
- add middleware in settings.py file
- add static files setting to settings.py file
```python
STATIC_URL = 'static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```
- create a bash file like build.sh for render to run at the beginning
- Host web use [render.com](https://render.com/)
  - build command: ./build.sh
  - start commnad: gunicorn config.wsgi

---

Whitenoise 是一个 Python 库，用于在 Web 应用程序中处理静态文件。

- 将静态文件（例如 HTML、CSS 和 JavaScript 文件）存储在您的 Web 应用程序中。
- 为您的静态文件提供缓存和压缩。
- 处理未找到的页面和其他错误。
- Whitenoise 通常与 WSGI 框架（例如 Django 和 Flask）一起使用。

这样网页就像很多静态网站那样可以host在网上了，但是接下来才到models重头戏。

### Models

- 每个 model 都是一个Python Class 代表一个 database table，每个 class 的 attribute 是一个 table 的 field
- 和数据库表格联动
