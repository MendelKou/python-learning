'''
title: 发送邮件功能的封装
time: 2017-07-31
author: KMD
调用实例：
sendemail(
    {
        'smtp_addr' : 'smtp.163.com',
        'from_addr' : 'kmd6174@163.com',
        'password' : 'xxx...'
    },
    ctype='multi',
    to_list = ['xxxx@qq.com','xxx@sohu.com'],
    subject = 'python email 测试',
    content = 'Hello friends, 我在学python',
    attach_list=[
        {
            'path':'2.jpg',
            'type':'image',
            'sub_type':'jpeg',
            'filename':'image-1.jpg'
        }
    ],
    debuglevel=1
)
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr,formataddr
import smtplib
# 格式化编码邮件头信息的辅助函数
def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
def sendemail(smtp_config,ctype,to_list,subject,content,attach_list=[],encoding='utf-8',debuglevel=None):
    if ctype == 'plain' or ctype == 'html':
        msg = MIMEText(content,ctype,encoding)
    elif ctype == 'alternative': #同时支持plain与html 此时content应为提供plain与html内容的字典
        msg = MIMEMultipart('alternative')
        msg.attach(MIMEText(content['plain'],'plain',encoding))
        msg.attach(MIMEText(content['html'],'html',encoding))
    elif ctype == 'multi': #带附件的邮件
        msg = MIMEMultipart()
        msg.attach(MIMEText(content,'plain','utf-8'))
        for index,atch in enumerate(attach_list):
            with open(atch['path'],'rb') as f:
                mime = MIMEBase(atch['type'],atch['sub_type'],filename=atch['filename'])
                mime.add_header('Content-Disposition','attachment',filename=atch['filename'])
                mime.add_header('Content-ID','<'+str(index)+'>')
                mime.add_header('X-Attachment-Id',str(index))
                mime.set_payload(f.read()) #把附件的内容读进来
                encoders.encode_base64(mime)
                msg.attach(mime)
    else:
        raise ValueError('Invalid type:%s' % ctype)
    msg['From'] = _format_addr('<%s>' % smtp_config['from_addr']) #如果不使用_format_addr 则不能包含中文
    msg['To'] = ';'.join([_format_addr('<%s>' % addr) for addr in to_list])
    msg['Subject'] = Header(subject,encoding).encode()

    server = smtplib.SMTP(smtp_config['smtp_addr'],25) #SMTP协议默认端口为25
    if debuglevel != None:
        server.set_debuglevel(debuglevel)
    try:
        server.login(smtp_config['from_addr'],smtp_config['password'])
        server.sendmail(smtp_config['from_addr'],to_list,msg.as_string())
    except Exception as e:
        print(e)
        return -1
    finally:
        server.quit()
    return 1
