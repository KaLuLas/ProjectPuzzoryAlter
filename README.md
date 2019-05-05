# ProjectPuzztoryNext


**2019/05/04**

- [x] 主界面UI粗略版本完成 【 KAL

**TODO:**

- [x] 数据库内容检索
- [x] 登陆错误信息弹窗
- [x] 输入为空时的对应处理
- [x] 登陆/注册界面UI完善 【 ALEX
- [ ] 用户登录状态保存 
- [ ] 数据库models修改【ALEX
- [ ] 主界面列表图表 & 故事框图片添加

**APPEND：**

- [x] bootstrap3到bootstrap4过渡
- [ ] 数据库表单更新



**2019/05/03** 

- [x] 登陆界面UI完善 / 功能完善 / 
- [x] 主界面UI完善  LOGO 调整/  【 KAL
- [ ] 发布故事UI 【 KAL



**2019/05/02** 主界面导航条， login.html



**Usertable**

| 属性名     |      | 注释     |
| ---------- | ---- | -------- |
| useremail  |      | 用户邮箱 |
| username   |      | 用户昵称 |
| password   |      | 密码     |
| level      |      | 等级     |
| experience |      | 经验值   |

**Storytable**

| 属性名           |      | 注释                       |
| ---------------- | ---- | -------------------------- |
|                  |      |                            |
| username         |      | 创建人昵称                 |
| useremail        |      | 创建人邮箱                 |
| title            |      | 标题                       |
| likescount       |      | 获得的赞数                 |
| fragmentcapacity |      | 最多允许片段数（由作者决定 |
| fragmentscount   |      | 当前片段个数               |
| branch           |      | 是否允许分支               |
| wordslimit       |      | 是否限制片段字数           |
| finished         |      | 是否完结                   |
| modified         |      | 是否允许修改               |
| createtime       |      | 故事创建日期               |
| beginning        |      | 故事开头片段id             |

**Fragmenttable**

| 属性名        |      | 注释       |
| ------------- | ---- | ---------- |
|               |      |            |
| username      |      | 创建人昵称 |
| useremail     |      | 创建人邮箱 |
| content       |      | 片段文本   |
| createtime    |      | 创建时间   |
| commentscount |      | 评论数     |
| likescount    |      | 获得的赞数 |
| storyid       |      | 故事ID     |
| branchid      |      | 所处分支ID |
| branchleft    |      | 左分支ID   |
| branchright   |      | 右分支ID   |

**Commenttable**

| 属性名     |      | 注释     |
| ---------- | ---- | -------- |
| commentid  |      | 评论ID   |
| storyid    |      | 故事ID   |
| fragmentid |      | 片段ID   |
| content    |      | 评论文本 |
| username   |      | 用户昵称 |
| useremail  |      | 用户邮箱 |
| createtime |      | 创建时间 |
| likescount |      | 点赞数   |

