# ProjectPuzztoryNext

('/_ ')玩故事接龙的一个站点，承载了许多回忆的课程作业。

后端使用django开发，数据库选用mysql。前端使用经典jquery。

## Features

* 为故事接续片段
* 为接续故事限定关键词，限定接续长度
* 点赞：故事点赞 / 片段点赞 / 评论点赞
* 评论：故事评论 / 片段评论 / 回复评论

## Layout

```
.
│  database-design.md # 数据库设计
│  manage.py
│  README.md
│
├─PuzzModel # django侧数据库声明
│
├─puzztory
│      settings.py # 配置项
│      urls.py # url路由
│      user.py # 用户相关
│      view.py # 核心交互逻辑
|      ...
│
├─static # 站点静态资源
│
└─templates # 网页模板html
```



## Prerequisites for deployment

下面列出的是开发环境使用的版本，仅供参考，低于此版本应该也没有问题

* **python** 3.6.8
  * django 3.2
  * pymysql 1.0.2
  * pillow 8.3.1
* **mysql** Ver 8.0.32 for Linux on x86_64 (MySQL Community Server - GPL)(**Red Hat Enterprise Linux 7 / Oracle Linux 7 (Architecture Independent), RPM Package** -> mysql80-community-release-el6-7.noarch.rpm)

## Deployment

1. 手动在新设备上使用mysql建库，或者在新设备上执行下述命令重新建库均可

	```sh
	python manage.py migrate
	```

2. 使用django自带脚本进行后端的简易部署

	```
	python manage.py runserver [ip]:[port]
	```


3. You are good to go!
