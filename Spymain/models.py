from django.db import models


marital_status_options = (
    ("Single", "Single"),
    ("Married", "Married"),
    ("Divorced", "Divorced"),
    ("Widowed", "Widowed"),
    ("Separated", "Separated"),
    ("Waiting for the one", "Searching"),
)
choice = (('No','No'),('Yes','Yes'))
       

class Models_info(models.Model):
    Username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,null=True, blank=True)
    profile_photo= models.ImageField(upload_to='profilephoto/')
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200,null=True, blank=True)
    city = models.CharField(max_length=200,null=True, blank=True)
    school = models.CharField(max_length=200,null=True, blank=True)
    job = models.CharField(max_length=200,null=True, blank=True)
    hobbies = models.CharField(max_length=200,null=True, blank=True)
    preffered_type_according_to_us=models.TextField(null=True, blank=True)
    secret=models.CharField(max_length=400,null=True, blank=True)
    industry=models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    approx_followers=models.SmallIntegerField(null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    marital_status= models.CharField(
        max_length = 100,
        choices = marital_status_options,
        default = 'Single'
        )
    bust = models.SmallIntegerField(null=True, blank=True)
    waist = models.SmallIntegerField(null=True, blank=True)
    hip = models.SmallIntegerField(null=True, blank=True)
    height_feet=models.SmallIntegerField(null=True, blank=True)
    height_inches=models.SmallIntegerField(null=True, blank=True)
    weight=models.SmallIntegerField(null=True, blank=True)
    Post_view = models.IntegerField(default=0)
    
    def __str__(self):
         return self.Username


class BlogView(Models_info):
    model = Models_info
    def get_object(self):
        obj = super().get_object()
        obj.Post_view += 1
        obj.save()
        return obj
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)

#     votes = models.IntegerField(default=0)
class model_assets(models.Model):
    model = models.ForeignKey(Models_info, on_delete=models.CASCADE) 
    Username = models.CharField(max_length=200) 
    teen = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    milf = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    hot = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    sexy = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    nerdy = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    summer_body = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    fat = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    aunty = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    redhead = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    petite = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    pretty = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    goddess = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    bigboobs = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    bigass = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    classy = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    topper = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    naughty = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    asshole = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    playgirl = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    creep = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    gamer = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    animelover = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    movielover = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    reader = models.CharField(max_length = 100,
        choices = choice,
        default = 'No'
        )
    def __str__(self):
         return self.Username
    
