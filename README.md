# email-sender

一个简单的邮件发送工具，支持附件。

## 配置

可以通过命令行参数或配置文件来设置电子邮件的相关参数。

### 命令行参数

使用以下命令行参数来设置电子邮件的相关参数：

- `--config`: 配置文件的路径。默认为 `mail.conf`。
- `--sender`: 发件人的电子邮件地址。
- `--sender_name`: 发件人的显示名称。
- `--password`: 发件人的电子邮件密码。
- `--server`: 邮件服务器的地址。
- `--port`: 邮件服务器的端口号。
- `--connection`: 邮件服务器的连接类型。可以是 `ssl`、`tls` 或 `plain`。
- `--recipient`: 收件人的电子邮件地址。多个收件人之间用逗号分隔。
- `--cc`: 抄送人的电子邮件地址。多个抄送人之间用逗号分隔。
- `--subject`: 电子邮件主题。
- `--body`: 电子邮件正文。
- `--attachment`: 附件文件的路径。

### 配置文件

使用配置文件来设置电子邮件的相关参数。配置文件包含以下部分和字段：

```conf
[email]
sender = 发件人的电子邮件地址
sender_name = 发件人的显示名称
password = 发件人的电子邮件密码
server = 邮件服务器的地址
port = 邮件服务器的端口号
connection = 邮件服务器的连接类型

[config]
recipient = 收件人的电子邮件地址
cc = 抄送人的电子邮件地址
subject = 电子邮件主题
body = 电子邮件正文
attachment = 附件文件的路径
```

如果同时提供了命令行参数和配置文件，则命令行参数将覆盖配置文件中的相应设置。

## 发送电子邮件

要使用此代码发送电子邮件，可以在命令行中运行以下命令：

`python sender.py [options]`

其中 [options] 是您希望设置的命令行参数。例如，要使用配置文件 myconfig.conf 发送一封带有附件 attachment.pdf 的电子邮件，可以运行以下命令：

`python sender.py --config myconfig.conf --attachment attachment.pdf`