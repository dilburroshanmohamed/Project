from django.db import models

# Create your models here.


class Login(models.Model):
    username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class groups(models.Model):
     groupname = models.CharField(max_length=100)



class groupleaders(models.Model):
      GROUP=models.ForeignKey(groups,on_delete=models.CASCADE,default=1)
      name= models.CharField(max_length=100)
      course= models.CharField(max_length=100)
      email= models.CharField(max_length=100)
      phoneno = models.CharField(max_length=100)
      gender = models.CharField(max_length=100)
      LOGIN= models.ForeignKey(Login,on_delete=models.CASCADE)


class judge(models.Model):
      name= models.CharField(max_length=100)
      place= models.CharField(max_length=100)
      hname= models.CharField(max_length=100)
      proffession= models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      phoneno = models.CharField(max_length=100)
      gender= models.CharField(max_length=100)
      LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)


class program(models.Model):
      programname= models.CharField(max_length=100)
      programtype= models.CharField(max_length=100)
      groupprogram= models.CharField(max_length=100)
      description= models.CharField(max_length=100)



class rulesandregulation(models.Model):
      PROGRAMME= models.ForeignKey(program,on_delete=models.CASCADE)
      rules= models.CharField(max_length=100)

class programschedule(models.Model):
    PROGRAM= models.ForeignKey(program,on_delete=models.CASCADE,default=1)
    date = models.DateField()
    fromtime= models.CharField(max_length=100)
    totime= models.CharField(max_length=100)
    stage= models.CharField(max_length=100)

class programjudgeallocation(models.Model):
      LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
      PROGRAMME = models.ForeignKey(program,on_delete=models.CASCADE)
      JUDGE = models.ForeignKey(judge,on_delete=models.CASCADE,default='')
      PROGRAMESHEDULE= models.ForeignKey(programschedule,on_delete=models.CASCADE,default=1)



class candidate(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    PROGRAM= models.ForeignKey(program,on_delete=models.CASCADE,default="")
    email = models.CharField(max_length=100)
    GROUP = models.ForeignKey(groups, on_delete=models.CASCADE)
    phoneno = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class award(models.Model):
    chessnumber = models.CharField(max_length=100)
    CANDIDATE = models.ForeignKey(candidate, on_delete=models.CASCADE,default='')
    GROUPS = models.ForeignKey(groups, on_delete=models.CASCADE,default='')
    grade = models.CharField(max_length=100)

class candidateresult(models.Model):
    PROGRAMME = models.ForeignKey(program, on_delete=models.CASCADE)
    CANDIDATE = models.ForeignKey(candidate, on_delete=models.CASCADE,default='')
    JUDGE = models.ForeignKey(judge, on_delete=models.CASCADE, default='')
    mark =models.CharField(max_length=10)

class programenrollment(models.Model):
        PROGRAMMESCHEDULE=models.ForeignKey(programschedule,on_delete=models.CASCADE)
        CANDIDATE= models.ForeignKey(candidate,on_delete=models.CASCADE)

class Complaint(models.Model):
    complaint=models.CharField(max_length=100)
    date=models.DateField()
    status=models.CharField(max_length=100)
    replay=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default='')
    type=models.CharField(max_length=100,default='0')

class Feedback(models.Model):
    feedback=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default='')
    type=models.CharField(max_length=100,default='0')


class groupresult(models.Model):
    GROUP = models.ForeignKey(groups, on_delete=models.CASCADE)
    point= models.CharField(max_length=100)


