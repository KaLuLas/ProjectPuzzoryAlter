# 数据库设计

## UserExtension（User）

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

## Story

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

## Fragment

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

## Comment

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

## Announcement

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