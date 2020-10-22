# OFFICE365 E5 激活

![auto subscription](https://github.com/lizhaode/office365-subscription/workflows/auto%20subscription/badge.svg)

保持反复调用 office 365 的接口可以续订 E5

我的帐号已经两次续期成功了

### 用法

fork 这个项目，然后在配置中的 `Secrects` 下创建这几个

`tenant_id` `client_id` `client_secret` `user_name` `pass_word`

等待收到续订成功的邮件

### 关于安全
我自己的账户下边，一共给这个程序开了这些权限

email
Files.Read
Files.Read.All
Files.Read.Selected
Mail.Read
Mail.Read.Shared
Mail.ReadBasic
Mail.ReadBasic.All
Mail.ReadWrite
User.Read
User.Read.All

理论上你自己填写你自己的密钥等信息

直接用 Github Actions 运行

应该是比较安全的

##### 这个程序干了啥
每6个小时重复执行一次

获取 accessToken

调用 https://graph.microsoft.com/v1.0/me/messages 获取邮件列表

调用 https://graph.microsoft.com/v1.0/me/drive/root/children 获取 OneDrive 文件列表
