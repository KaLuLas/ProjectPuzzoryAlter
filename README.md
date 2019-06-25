ProjectPuzztoryNext

### 项目介绍

('/_ ')玩故事接龙的（摸了。

把大量的TODO都放在了project记录里面

上锁功能的测试备忘记录放在了Issues里面



### 项目记录

**05.23之后的记录将在Projects中更新，不再添加README记录**


**2019.05.23：**

- [x] 敲除片段（简易版）
- [x] 敲除片段后回到之前在浏览的那一页
- [x] 如果敲除掉当前页唯一的片段会到前一页
- [x] threading.timer 释放锁



**2019.05.22：**

- [x] 当用户为故事作者时可以对modified=False的文章进行修改 【ALEX
- [x] 片段个数超过7时故事开始分页 【ALEX
- [x] 故事页分页功能 【ALEX
- [x] 片段锁的处理 【TOGETHER



**2019.05.21：**

- [x] 文字省略显示问题【KAL
- [x] 空格检测jquery实现 【KAL
- [x] 主界面翻页设计 【KAL
- [x] 经验的一次小尝试【KAL



**2019.05.20：**

- [x] 欲提交片段时检查用户登录状态【KAL
- [x] 新增片段按钮的条件限制disabled【KAL
- [x] 首页Trending & Ranking跳转 【KAL
- [x] 主界面Trending & Ranking细化 【KAL
- [x] 提交故事片段数和字数都要大于0【KAL
- [x] 去除空格偷懒做法【KAL
- [x] 添加空格检测，不允许全是空格的片段和标题【ALEX



**2019.05.19：**

- [x] 添加片段功能基本完成【ALEX
- [x] 添加片段之前检查各种限制 【ALEX
- [x] 故事展示页布局修改 【ALEX
- [x] 故事修改后展示页的刷新 【ALEX



**2019.05.18：**

- [x] 为故事新增片段简易UI 【ALEX



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

| attribute   | type         | null | blank | default | max_length | description           |
| ----------- | ------------ | ---- | ----- | ------- | ---------- | --------------------- |
| id          |              |      |       |         |            | [主键]增序            |
| password    | CharField    |      |       |         | 128        |                       |
| username    | CharField    |      |       |         |            | [Unique]把email存进去 |
| email       | CharField    |      |       |         |            |                       |
| nickname    | CharField    |      | False |         | 20         | 昵称                  |
| level       | IntegerField |      | False | 1       |            | 等级                  |
| experience  | IntegerField |      | False | 0       |            | 经验                  |
| avator      | ImageField   |      | True  |         |            | 头像                  |
| description | CharField    | True | True  |         | 150        | 用户个人签名          |


**Story**

| attribute       | type          | null | blank | default      | max_length | description                    |
| --------------- | ------------- | ---- | ----- | ------------ | ---------- | ------------------------------ |
| id              |               |      |       |              |            | [主键]增序                     |
| ffid            | IntegerField  |      | False |              |            | 首个片段                       |
| ffcontent       | CharField     |      | False |              | 500        | 首片内容                       |
| email           | CharField     |      | False |              | 150        | 作者邮箱                       |
| nickname        | CharField     |      | False |              | 20         | 作者昵称                       |
| **editor**      | CharField     |      | False |              | 150        | 修改者邮箱                     |
| title           | CharField     |      | False |              | 50         | 题目                           |
| createtime      | DateTimeField |      | False | timezone.now |            | 创建时间                       |
| **updatetime**  | DataTimeField |      | False | timezone.now |            | 修改时间                       |
| **remains**     | IntegerField  |      | False | 0            |            | 剩余修改时间                   |
| branch          | BooleanField  |      |       | False        |            | 是否存在分支                   |
| finished        | BooleanField  |      |       | False        |            | 是否完结，true表示完结         |
| lock            | BooleanField  |      |       | False        |            | 是否可编辑，true表示正在被写   |
| modified        | BooleanField  |      |       | True         |            | 是否可编辑，true表示允许修改   |
| likescount      | IntegerField  |      |       | 0            |            | 点赞数                         |
| commentscount   | IntegerField  |      |       | 0            |            | 评论数                         |
| fragscount      | IntegerField  |      |       | 1            |            | 片段数                         |
| fragscountlimit | IntergerField |      |       | -1           |            | 片段数量上限，-1代表无额外限制 |
| fragwordslimit  | IntegerField  |      |       | -1           |            | 片段字数上限，-1代表无额外限制 |
| tags            | CharField     | True | True  |              | 110        |                                |
| keywords        | CharField     | True | True  |              | 110        |                                |
| rules           | CharField     | True | True  |              | 310        |                                |


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

**Announcement**

| attribute    | type          | null | blank | default      | max_length | description  |
| ------------ | ------------- | ---- | ----- | ------------ | ---------- | ------------ |
| id           |               |      |       |              |            | [主键]增序   |
| optype       | CharField     |      | False |              | 20         |              |
| targetid     | IntegerField  |      | False |              |            | 对象id       |
| fromuser     |               |      | False |              |            | 发起者用户id |
| fromnickname |               |      | False |              |            | 发起者用户名 |
| touser       |               |      | False |              |            | 目标用户id   |
| createtime   | DataTimeField |      | False | timezone.now |            | 发起时间     |
| content      | CharField     | True | True  |              |            | 评论         |
| read         | BooleanField  |      | False | False        |            | 是否被浏览   |

新增片段 / 故事点赞 / 片段点赞 / 故事评论 / 片段评论 / 评论评论
