import yagmail

email = "xxxxxx"
name = "기쁨"
subject = f'{name}님 수료를 축하해요!'
body = f'{name}님 본문'

yag = yagmail.SMTP(
    user="xxxxxx",
    password="xxxxxx"
)
yag.send(
    to=email,
    subject=subject,
    contents=body,
)
