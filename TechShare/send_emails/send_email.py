# send_email.py
import sys
try:
    import argparse
    import smtplib
    from proxy_smtplib import ProxySMTP
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication
except ImportError:
    print('import error', file=sys.stderr)

def send_proxy(receiver, zip_file):
    email_server = ProxySMTP('smtp.163.com', 25,
                         proxy_addr='跳板机的局域网IP',
                         proxy_port=7891)
    # 需要修改的地方
		file = zip_file
    user_email = 'YOUR_EMAIL@163.com'
    user_pass = 'PASSWD'
    recipient_list = [receiver]

    sendinfo = "注：此邮件由机器自动发出，无人工回复。\n\n" \
               "请查收登录跳板机所需文件，并在登录成功后回复1。" \
               "如何登录服务器请查看wiki。\n\n" \
               "若登录服务器有任何问题，请联系管理员yqykrhf@163.com"
    message = MIMEMultipart()
    #添加正文
    part_text = MIMEText(sendinfo,'plain','utf-8')
    message.attach(part_text)
    # 构建邮件附件
    part_attach1 = MIMEApplication(open(file, 'rb').read())  # 打开附件
    part_attach1.add_header('Content-Disposition', 'attachment', filename=file)  # 为附件命名
    message.attach(part_attach1)  # 添加附件

    message['Subject'] = 'IIPL服务器账户申请结果' 
    #发送方信息
    message['From'] = user_email 
    #接受方信息     
    message['To'] = recipient_list[0]
    try:
        email_server.starttls()
        email_server.login(user_email, user_pass)
        email_server.sendmail(user_email, recipient_list, message.as_string())
        email_server.quit()
        print(f'Send to {recipient_list} successfully')
    except smtplib.SMTPException as e:
        print('send error ', file=sys.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('receiver', type=str, default="xxxxx@163.com", help="Email address")
    parser.add_argument('--file', type=str, help="Email attach")
    config = parser.parse_args()
    send_proxy(config.receiver, config.file)