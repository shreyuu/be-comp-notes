from captcha.image import ImageCaptcha

image_info = ImageCaptcha(width=250, height=100)
captcha_text = 'snjb'
source = image_info.generate(captcha_text)
image_info.write(captcha_text, 'abc.png')
