import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# 보내는 사람 정보
me = "kdxz1993@gmail.com"
my_password = "1234"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
email_list = ["rmafud93@naver.com", "rmafud93@naver.com"]

for you in email_list:
    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "다중으로 보내기"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "성공"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 메일 보내기
    s.sendmail(me, you, msg.as_string())

# 다 끝나고 닫기
s.quit()

