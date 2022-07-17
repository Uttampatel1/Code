from captcha.image import ImageCaptcha
from string import ascii_letters
from random import sample

image =ImageCaptcha(width=280,height=80)


captcha_text=sample(ascii_letters, 6)

data=image.generate(captcha_text)

image.write(captcha_text,'CAPTCHA.png')
