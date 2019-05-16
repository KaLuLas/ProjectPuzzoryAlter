# ProjectPuzztoryNext

### 项目介绍

('/_ ')玩故事接龙的（摸了。



### 项目记录

**TODO:**

- [ ] 主界面Trending & Ranking细化 【 KAL
- [ ] （美化）填充边缘内容让页面不出现白边【KAL
- [ ] 故事展示页进阶 【ALEX
- [ ] 添加片段功能（需要检查各种限制，如是否还能添加，关键词等 【ALEX
- [ ] 成功提交片段通知 【ALEX
- [ ] 故事修改后展示页的刷新 【ALEX
- [ ] 成功提交故事通知 【KAL
- [ ] 提交故事片段数和字数都要大于0【KAL
- [ ] 文字省略显示问题【KAL
- [ ] 用户等级和经验值变更（涉及到几乎每种用户行为【ALEX
- [ ] 故事点赞，片段点赞功能 【ALEX
- [ ] 故事评论，片段评论功能【KAL
- [ ] 故事评论显示，片段评论显示【KAL
- [ ] 故事作者的完结设置功能（不同用户的完结申请结果不同or一般人的故事页没有完结请求按钮【ALEX
- [ ] 普通用户的申请完结功能涉及到通知作者（系统通知【ALEX
- [ ] 针对完结申请和系统通知，是否修改**数据库**【TOGETHER
- [ ] 针对关键词修改**数据库**【TOGETHER
- [ ] 分支添加
- [ ] 分支显示（天啊感觉这是一个超大工程，需要细分出好多要考虑和讨论的
- [ ] （接上一条）比如分支片段点赞，分支完结设置，开启分支的用户身份
- [ ] （不想做）软规则  因为不好检测而且UI不好做（吐舌
- [ ] （进阶）如果要做用户头像，UI需要大改（皱眉
- [ ] （进阶）安全问题的考虑

  

**2019.05.17：**

- [x] 换行在首页和故事展示页的显示问题【ALEX
- [x] 进度条属性中百分比计算 【ALEX



**2019.05.16：**

- [x] 数据库成功大改【TOGETHER
- [x] 故事展示页排版问题【ALEX
- [x] 故事信息能够正常在首页显示【KAL
- [x] README中数据库设计部分补全【TOGETHER



**2019.05.15：**

- [x] 主页故事展示 【KAL
- [x] 解决时区不正确问题 【ALEX
- [x] 故事展示页初步 【ALEX



**2019.05.12 - 13:**

- [x] 新增pythonUser信息中的用户昵称，并且更改欢迎页及用户空间
- [x] 增加已有用户的lastname
- [x] 【新建故事提交UI】新建故事输入框限制
- [x] （故事发布完成）主界面故事展示 & 排行榜 【 ALEX
- [x] 数据库models修改（希望是最后一次
- [x] 主页上面加点margin/padding
- [x] 【用户登录】根据用户登录状态进行正确提示
- [x] 【新建故事提交UI】自定义关键词 / 自定义规则 （行数可变的输入）
- [x] 【新建故事提交UI】字数限制，输入类型限制
- [x] 【故事提交】新建故事提交数据库操作
- [x] 测试数据库是否修改成功



**2019/05/08**

- [x] 数据库models修改【ALEX
- [x] 用户登录状态保存 



**2019/05/04**

- [x] 主界面UI粗略版本完成 【 KAL
- [x] 输入为空时的对应处理【ALEX



**2019/05/03** 

- [x] 登陆界面UI完善 / 功能完善 / 
- [x] 主界面UI完善  LOGO 调整/  【 KAL
- [x] 登陆错误信息弹窗【ALEX



**2019/05/02** 主界面导航条， login.html



**EXTRA：**

- [x] bootstrap3到bootstrap4过渡
- [x] 数据库表单更新



**NOTE：**

 ALTER TABLE fragmentTable MODIFY COLUMN content VARCHAR(500) CHARACTER SET utf8 NOT NULL;

ALTER TABLE storyTable MODIFY COLUMN title VARCHAR(50) CHARACTER SET utf8 NOT NULL;

故事展示页显示问题

部分区域文本缩略问题

部分区域中文需求问题





### 数据库设计（django



**UserExtension**（User）

| attribute  | type         | null | blank | default | max_length | description           |
| ---------- | ------------ | ---- | ----- | ------- | ---------- | --------------------- |
| id         |              |      |       |         |            | [主键]增序            |
| password   | CharField    |      |       |         | 128        |                       |
| username   | CharField    |      |       |         |            | [Unique]把email存进去 |
| email      | CharField    |      |       |         |            |                       |
| nickname   | CharField    |      | False |         | 20         | 昵称                  |
| level      | IntegerField |      | False | 1       |            | 等级                  |
| experience | IntegerField |      | False | 0       |            | 经验                  |
| avator     | ImageField   |      | True  |         |            | 头像                  |
|            |              |      |       |         |            |                       |


**Story**

| attribute       | type          | null | blank | default      | max_length | description                    |
| --------------- | ------------- | ---- | ----- | ------------ | ---------- | ------------------------------ |
| id              |               |      |       |              |            | [主键]增序                     |
| ffid            | IntegerField  |      | False |              |            | 首个片段                       |
| ffcontent       | CharField     |      | False |              | 500        | 首片内容                       |
| email           | CharField     |      | False |              | 150        | 作者邮箱                       |
| nickname        | CharField     |      | False |              | 20         | 作者昵称                       |
| title           | CharField     |      | False |              | 50         | 题目                           |
| createtime      | DateTimeField |      | False | timezone.now |            | c创建时间                      |
| branch          | BooleanField  |      |       | False        |            | 是否存在分支                   |
| finished        | BooleanField  |      |       | False        |            | 是否完结，true表示完结         |
| lock            | BooleanField  |      |       | False        |            | 是否可编辑，true表示正在被写   |
| modified        | BooleanField  |      |       | True         |            | 是否可编辑，true表示允许修改   |
| likescount      | IntegerField  |      |       | 0            |            | 点赞数                         |
| commentscount   | IntegerField  |      |       | 0            |            | 评论数                         |
| fragscount      | IntegerField  |      |       | 1            |            | 片段数                         |
| fragscountlimit | IntergerField |      |       | -1           |            | 片段数量上限，-1代表无额外限制 |
| fragwordslimit  | IntegerField  |      |       | -1           |            | 片段字数上限，-1代表无额外限制 |


**Fragment**

| attribute     | type          | null | blank | default      | max_length | description |
| ------------- | ------------- | ---- | ----- | ------------ | ---------- | ----------- |
| id            |               |      |       |              |            | [主键]增序  |
| storyid       | IntegerField  |      | False |              |            | 归属故事ID  |
| email         | CharField     |      | False |              | 150        | 作者邮箱    |
| nickname      | CharField     |      | False |              | 20         | 作者昵称    |
| content       | CharField     |      | False |              | 500        | 片段内容    |
| createtime    | DateTimeField |      | False | timezone.now |            | 创建时间    |
| likescount    | IntegerField  |      |       | 0            |            | 点赞数      |
| commentscount | IntegerField  |      |       | 0            |            | 评论数      |
| branchid      | IntegerField  |      | False | 0            |            | 分支ID      |
| branchleft    | IntegerField  | True | True  |              |            | 左分支ID    |
| branchright   | IntegerField  | True | True  |              |            | 右分支ID    |

**Comment**

| attribute  | type          | null | blank | default      | max_length | description             |
| ---------- | ------------- | ---- | ----- | ------------ | ---------- | ----------------------- |
| id         |               |      |       |              |            | [主键]增序              |
| email      | CharField     |      | False |              | 150        | 作者邮箱                |
| nickname   | CharField     |      | False |              | 20         | 作者昵称                |
| sof        | BooleanField  |      | False |              |            | True为故事，False为片段 |
| storyid    | IntegerField  | True | True  |              |            | 归属故事ID              |
| fragid     | IntegerField  | True | True  |              |            | 归属故事ID              |
| content    | CharField     |      | False |              | 150        | 片段内容                |
| createtime | DateTimeField |      | False | timezone.now |            | 创建时间                |
| likescount | IntegerField  |      |       | 0            |            | 点赞数                  |

