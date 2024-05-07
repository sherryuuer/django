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
- 创建了class后，进行migration：创建指导，和执行（每次进行class修改后都要执行这两行进行更新操作）每次的更新都和前一次有依存关系，很像是拓扑，然后内部会按照这种顺序进行更新
```bash
python manage.py makemigrations
python manage.py migrate
```
- CRUD 使用python进行数据库操作
```python
Model.objects.all()
Model.objects.get(id=1)
Model.objects.filter(title='ABC')
```
- 使用shell可以进行手动操作
```bash
python manage.py shell # open the shell
>>> from movies.models import MoviePosting
>>> MoviePosting.objects.create(title="铃芽之旅", description="是由新海诚编剧兼执导的日本动画电影，于2022年11月11日在日本国内上映、隔年春季在海外上映。本片为新海诚第8部动画电影[16]，也是他继《你的名字》《天气之子》后，第三部牵涉灾难题材的电影，三片合称作新海诚的“灾难三部曲”。故事讲述少女岩户铃芽、与以关闭灾难之门为使命的“闭门师”宗像草太，为了关闭灾难之门展开一连串的冒险旅程。影片前导标语为“门的那一边，存在着一切的时间——”（扉の向こうには、すべての時間があった——），正式海报标语为“我出发了。”（行ってきます。）", comention="画面很美但是故事尚未达到心理预期，相比较之下还是喜欢你的名字。", rank=6)
>>> MoviePosting.objects.all()
>>> movie = MoviePosting.objects.get(id=1)
>>> movie.rank
>>> movie.rank = 6.5 # update
>>> movie.save()
>>> movie.delete() # delete the data
```
- 可以用一些css样式修饰网页
- can use [tailwindcss](https://tailwindcss.com/)to style page

pip install crispy-tailwind

INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_tailwind",
    ...
)

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

### Admin

- create a admin: `python manage.py createsuperuser`: sally, sally
- rerun the server and login
- register models in admin.py
