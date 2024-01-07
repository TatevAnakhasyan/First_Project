from django.db import models
from django.utils.safestring import mark_safe



class Blog(models.Model):
    img = models.ImageField('Image', upload_to='media')
    title = models.CharField('Title', max_length=255)
    text = models.TextField('Text', max_length=255)
    date = models.DateField('Date')



    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'


class HomeBG(models.Model):
    image1 = models.ImageField('First Background Images', upload_to="media", null=True)
    image2 = models.ImageField('Second Background Images', upload_to="media", null=True)
    image3 = models.ImageField('Third Background Images', upload_to="media", null=True)
    image4 = models.ImageField('Forth Background Images', upload_to="media", null=True)


    def __str__(self) -> str:
        return 'Images'
    

    class Meta:
        verbose_name = 'Home Background Image'
        verbose_name_plural = 'Home Background Images'


class OurService(models.Model):
    text1 = models.TextField('First Text', max_length=255, null=True)
    text2 = models.TextField('Second Text', max_length=255, null=True)


    def __str__(self) -> str:
       return f"Our Service"
    

    class Meta:
        verbose_name = 'Our Services '
        verbose_name_plural = 'Our Services'


class ServiceIcons(models.Model):
    icon = models.CharField('Icon', max_length=100)
    text = models.TextField('Text', max_length= 255)

    def __str__(self) -> str:
        return f"Icon"
    
    class Meta:
        verbose_name = 'Icon'
        verbose_name_plural = 'Icons'


class OurGallery(models.Model):
    title = models.CharField('Title', max_length=50, null=True)
    subtitle = models.CharField('Subtitle',max_length=50, null=True)
    img = models.ImageField('Small Image', upload_to='media', null=True)
    img_large = models.ImageField('Large Image', upload_to='media', null=True)

    def __str__(self) -> str:
        return self.title
    
    def img_preview(self):
        return mark_safe(f'<img src = "{self.img.url}"  width = "60"/>')
    
    class Meta:
        verbose_name = 'Our Gallery'
        verbose_name_plural = 'Our Galleries'


class AboutUs(models.Model):
    text1 = models.TextField('First Text', max_length=255)
    text2 = models.TextField('Second Text', max_length=255)
    text3 = models.TextField('Third Text', max_length=255)


    def __str__(self) -> str:
        return 'About Us'
    

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Uses'


class ContactTxt(models.Model):
    text = models.TextField('Text', max_length=255)

    def __str__(self) -> str:
        return f"About of contact"
    
    class Meta:
        verbose_name = 'Contact Text'
        verbose_name_plural = 'Contact Texts'


class ContactUs(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    message = models.TextField('Message')

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'





