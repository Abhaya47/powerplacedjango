from django.db import models

class powerPlaces(models.Model):
    title=models.TextField()
    description=models.TextField()
    imagePath= models.ImageField(upload_to='uploads/', default="i.jpg")

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title=models.TextField()
    description=models.TextField()
    pubDate = models.DateTimeField("date published", auto_now_add=True)
    imagePath= models.ImageField(upload_to='uploads/', default="i.jpg")

    def __str__(self):
        return self.title

class Package(models.Model):
    packageID=models.AutoField(primary_key=True, editable=False)
    packageTitle=models.CharField(max_length=255, unique=True)
    description=models.TextField()
    image_path= models.ImageField(upload_to='uploads/', default="i.jpg")
    duration=models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.packageTitle

class User(models.Model):
    userID=models.AutoField(primary_key=True,editable=False)
    name=models.TextField()
    email=models.EmailField(unique=True)
    phone=models.BigIntegerField(unique=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    bookingID=models.AutoField(primary_key=True,editable=False)
    userID=models.ForeignKey(User,on_delete=models.CASCADE)    
    packageID=models.ForeignKey(Package, on_delete=models.CASCADE)
    startDate=models.DateField()
    endDate=models.DateField()

