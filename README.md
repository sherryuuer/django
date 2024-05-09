Check the project by:
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

---
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

### Auth

Django的内置的Auth方法。需要在config层级，也就是项目层级进行templates的设置。所有的urls和views都在env中可以找到。其实它和一般的app的构造是一样的，区别只是，它是Django内置的。

这里要注意项目层级的templates文件夹和config是同一个层级。而不是在config内部，这里的项目是指django这个最外层文件夹项目。

django
  - config
  - templates/registration/login.html
  - apps

### Django REST Framework

App很多情况下不仅仅是在浏览器中，它需要在website，mobile，store display screen上都可用。

使用一个menu应用来尝试这个框架。

使用JsonResponse也可以得到很好的效果，见menu.views。

安装框架：

```bash
pip install djangorestframework
```
Add to setting app list.

menu/serializers.py

通过它专有的序列化工具，response库，装饰器，可以迅速构架一个api界面，或json格式。

序列化数据：

Serialization（序列化）是指将对象或数据结构转换为可存储或传输的格式的过程，通常是将其转换为字节流或文本流的形式。序列化的主要目的是允许对象在不同系统之间或不同时间点之间进行传输、存储和重建，同时保持其结构和状态的完整性。

在计算机科学中，序列化常见于以下几个方面：

1. **对象序列化（Object Serialization）**：将对象转换为字节流的过程，使得对象可以被存储到文件中、通过网络进行传输，或在内存中保存以供后续使用。Java 中的序列化机制（Serializable 接口）、Python 中的 Pickle 库以及.NET Framework 中的 BinaryFormatter 都提供了对象序列化的实现。

2. **数据序列化（Data Serialization）**：将数据结构（如数组、列表、字典等）转换为字节流或文本流的过程，以便进行存储、传输或持久化。JSON、XML 和 Protocol Buffers 等数据序列化格式都被广泛应用于数据交换和存储。

3. **数据库序列化（Database Serialization）**：将对象或数据结构转换为数据库中的存储格式，以便在数据库中进行持久化存储和检索。ORM（对象关系映射）工具通常会将对象转换为数据库中的行，或将数据库查询结果转换为对象。

4. **内存序列化（Memory Serialization）**：将对象或数据结构转换为内存中的表示形式，以便在内存中进行传递、复制或持久化。这在分布式系统中很常见，如通过消息传递在不同节点之间传递对象。

总的来说，序列化允许将对象或数据结构转换为一种通用的格式，以便在不同的环境中进行传输、存储和处理，是实现数据交换和持久化的重要机制之一。
