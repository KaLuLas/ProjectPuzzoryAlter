# ProjectPuzztoryNext

### 项目介绍

('/_ ')玩故事接龙的（摸了。



### 项目记录

**2019.05.15：**

- [x] 主页故事展示 【KAL
- [x] 解决时区不正确问题 【ALEX
- [x] 故事展示页初步 【ALEX



**TODO:**

- [ ] 主界面列表图标 & 故事框图片添加 【 KAL
- [ ] 添加片段功能 【 ALEX
- [ ] 故事展示页进阶 【ALEX
- [ ] 成功提交故事通知 【KAL
- [ ] 片段数和字数都要大于0【KAL
- [ ] 要能显示“无片段数限制” 【KAL



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
| lock            | BooleanField  |      |       | False        |            | 是否可编辑，true表示不可修改   |
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

