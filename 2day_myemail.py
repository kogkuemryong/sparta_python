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
you = "rmafud93@naver.com"

# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "이것이 제목이다."
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "오늘은 2일차다"
part2 = MIMEText(content, 'plain')
msg.attach(part2)

# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()

# 2단계 인증 해제 - https://myaccount.google.com/signinoptions/two-step-verification
# 보안 수준이 낮은 앱 해제하기 - https://myaccount.google.com/lesssecureapps