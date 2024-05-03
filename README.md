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



Make Pizzas:

- 厨房点餐：urls
- 厨房制作：views（functions）
- 披萨的味道和材料选择：parameters
- 制作工艺和流程定制：templates（html blueprints）

Template language:

- Variables -> {{blog_title}}
- Tags -> {%if has_title%}
- Filters -> {{blog_title|title}}
- 'APP_DIRS': True : means templates are in app folders
- Templates folder: app/templates/app/index.html

Template Inheritance:

- html的层级使得child可以复用上一层的template。
- skeleon骨架 - 包括block - child的block可以覆盖被继承的template的内容
- 在哪里用？那些不变的地方比如navigator，footer之类的。

Host on Github:

- Settings:host allows * , not good just for fun
- pip install gunicorn，安装web服务器
- pip freeze > requirements.txt
- add ignore file
- push to Github repo


---
React和Django是用于构建Web应用程序的两个不同的技术，一个是前端JavaScript库，另一个是后端Python框架。以下是它们的比较：

**相同点：**

1. **MVC架构支持：** React和Django都支持MVC（Model-View-Controller）或类似的设计模式，这使得在应用程序中实现数据、业务逻辑和用户界面的分离更加容易。

2. **开发社区：** React和Django都拥有庞大的开发社区和生态系统，开发人员可以从中获取插件、库和支持。

3. **组件化：** React和Django都鼓励组件化的开发方式，这使得代码更易于维护和重用。

**不同点：**

1. **前端vs后端：** React是一个用于构建用户界面的JavaScript库，主要用于前端开发。它负责处理应用程序的视图层。而Django是一个后端Python框架，主要用于处理应用程序的业务逻辑和数据层。

2. **语言和技术栈：** React使用JavaScript（通常与JSX一起使用），而Django使用Python。因此，React通常与其他后端框架（如Django）一起使用，形成一个完整的技术栈。

3. **重点和功能：** React的重点是构建交互式的用户界面，它提供了许多用于构建前端组件和处理用户交互的工具。相比之下，Django的重点是提供一个完整的后端开发框架，包括处理URL路由、数据库交互、用户认证等功能。

4. **单页面应用vs多页面应用：** React通常用于构建单页面应用（SPA），其中所有的页面加载一次，然后通过JavaScript动态更新内容。而Django通常用于构建多页面应用（MPA），其中每个页面都是通过服务器渲染的。

总的来说，React和Django分别解决了Web应用程序的前端和后端开发需求，它们通常会一起使用以构建完整的Web应用程序。选择使用哪一个取决于项目的需求、开发人员的技能和偏好，以及团队的技术栈。
