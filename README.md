# mail-sender

一个简单的邮件发送工具，支持附件。

使用前需要先配置 `mail.conf` 文件，示例见 `mail.conf.example`

使用示例

`python sender.py --config mail.conf --recipient recipient@example.com --cc cc@example.com --subject "Hello" --body "Body" --attachment attachment.txt`