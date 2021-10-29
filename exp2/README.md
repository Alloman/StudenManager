## 实验二



### 开发环境

> Python == 3.9
>
> Django==3.2.3
>
> django-bootstrap4==3.0.1
>
> PyMySQL==1.0.2

### 文件目录

>├─exp2                                 项目配置文件
>├─static								静态文件
>│  ├─css
>│  ├─images
>│  └─js
>├─system_apps					主项目文件（包含各功能的应用）
>│  ├─course							课程功能实现
>│  │  ├─migrations
>│  │  └─templates
>│  ├─login								登录功能实现
>│  │  ├─migrations
>│  │  └─templates
>│  ├─student							学生相关功能实现
>│  │  ├─migrations
>│  │  └─templates
>│  ├─system_admin				管理员相关功能实现
>│  │  ├─migrations
>│  │  └─templates
>│  └─teacher							教师相关功能实现
>│      ├─migrations
>│      └─templates
>└─templates							主页模板

### 应用内文件介绍

> │  admin.py 								Django管理功能
> │  apps.py									Django应用功能
> │  models.py								定义该应用的实体类
> │  tests.py
> │  urls.py									应用内路由文件
> │  views.py								功能逻辑实现
> │
> ├─migrations							Django数据库迁移
> │
> └─templates								应用页面
>        student_base.html				基础页面
>        student_find.html				查找功能页面
>        student_index_base.html	应用主页
>        student_select.html			选课功能页面



### 使用



#### 1. 数据迁移

依次执行：

``` bash
python manage.py makemigrations 
python manage.py migrate
```

#### 2. 启动项目

``` bash
python manage.py runserver 
```

访问http://127.0.0.1:8000/