from random import random

from django.db.models import Count, Q
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from Myapp.models import *


def login(request):
    return render(request,"ADMINISTRATION 1/login 1.html")

def login_post(request):
    Username = request.POST['textfield']
    Password = request.POST['textfield2']

    res=Login.objects.filter(username=Username,Password=Password)
    if res.exists():
        res1 = Login.objects.get(username=Username, Password=Password)
        request.session['lid']=res1.id
        if res1.type == 'admin':
            return HttpResponse('''<script>alert('Login Successfully');window.location="/Myapp/home/"</script>''')

        elif res1.type == 'groupleaders':
            return HttpResponse('''<script>alert('Login Successfully');window.location="/Myapp/leaderhome/"</script>''')
        elif res1.type == 'judge':
            return HttpResponse('''<script>alert('Login Successfully');window.location="/Myapp/judgehome/"</script>''')
        elif res1.type == 'candidate':
            return HttpResponse('''<script>alert('Login Successfully');window.location="/Myapp/candidatehome/"</script>''')

        else:
            return HttpResponse('''<script>alert('User Not Found');window.location="/Myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid');window.location="/Myapp/login/"</script>''')

def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')


def home(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"adminhomeindex.html")

def admin_change_password(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"ADMINISTRATION 1/change password 2.html")

def achangepassword_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    currentpassword=request.POST['textfield']
    Newpassword=request.POST['textfield2']
    Confirmpassword=request.POST['textfield3']
    res = Login.objects.filter(Password=currentpassword,id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(Password=currentpassword,id=request.session['lid'])
        if Newpassword==Confirmpassword:
            res = Login.objects.filter(Password=currentpassword, id=request.session['lid']).update(Password=Confirmpassword)
            return HttpResponse('''<script>alert('Changing Successfully');window.location="/Myapp/login/"</script>''')
        else:
            return HttpResponse('''<script>alert('Password Mismatch');window.location="/Myapp/achangepassword/"</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid');window.location="/Myapp/achangepassword/"</script>''')

def groupadd(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"ADMINISTRATION 1/group add 24.html")

def groupadd_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    Groupname= request.POST['textfield']

    gobj=groups()
    gobj.groupname=Groupname
    gobj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/home/"</script>''')


def groupview(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = groups.objects.all()
    return render(request,"ADMINISTRATION 1/group view 25.html",{'data':res})

def groupview_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    search = request.POST['textfield']
    res = groups.objects.filter(groupname__icontains=search)

    return render(request,"ADMINISTRATION 1/group view 25.html",{'data':res})


def editgroup(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=groups.objects.get(id=id)
    return render(request,"ADMINISTRATION 1/edit group 26.html",{'data':var})

def editgroup_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    id=request.POST['id']
    Groupname= request.POST['textfield']
    obj=groups.objects.get(id=id)
    obj.groupname=Groupname
    obj.save()
    return HttpResponse('''<script>alert('Successfully edited');window.location="/Myapp/groupview/"</script>''')

def delete_group(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    obj=groups.objects.get(id=id).delete()
    return redirect('/Myapp/groupview/',)




def groupleaderadd(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=groups.objects.all()
    return render(request,"ADMINISTRATION 1/group leader add 3.html",{'data1':var})


def groupleaderadd_POST(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    Name=request.POST['textfield']
    gender=request.POST['RadioGroup1']
    Course=request.POST['textfield2']
    Email=request.POST['textfield3']
    phonenumber=request.POST['textfield4']
    group = request.POST['select2']

    lobj = Login()
    lobj.username = Email
    lobj.Password = phonenumber
    lobj.type = "groupleaders"
    lobj.save()

    globj=groupleaders()
    globj.name = Name
    globj.gender = gender
    globj.course = Course
    globj.email = Email
    globj.phoneno= phonenumber
    globj.GROUP_id = group
    globj.LOGIN=lobj
    globj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/groupleaderadd/"</script>''')


def viewgroupleader(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = groupleaders.objects.all()
    return render(request,"ADMINISTRATION 1/view group leader 4.html",{'data':res})

def vieweditgroupleader_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    search=request.POST['textfield']
    return HttpResponse("OK")

def editgroupleader(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=groupleaders.objects.get(id=id)
    var1=groups.objects.all()
    return render(request,"ADMINISTRATION 1/edit group leader 5.html",{'data':var,'data2':var1})

def editgroupleader_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    id=request.POST['id']
    name=request.POST['textfield']
    gender=request.POST['RadioGroup1']
    course=request.POST['textfield2']
    email=request.POST['textfield3']
    phonenumber=request.POST['textfield4']
    groups=request.POST['select2']

    obj=groupleaders.objects.get(id=id)
    obj.name=name
    obj.course = course
    obj.email = email
    obj.phoneno = phonenumber
    obj.gender = gender
    obj.GROUP_id = groups
    obj.save()
    return HttpResponse('''<script>alert(' Edited Successfully ');window.location="/Myapp/viewgroupleader/"</script>''')

def delete_leader(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    obj=groupleaders.objects.get(id=id).delete()
    return redirect('/Myapp/viewgroupleader/',)


def addjudges (request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"ADMINISTRATION 1/add judges 6.html")

def addjudges_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    Name=request.POST['textfield']
    Gender=request.POST['RadioGroup1']
    housename=request.POST['textfield3']
    Place=request.POST['textfield2']
    profession=request.POST['textfield6']
    Email=request.POST['textfield7']
    Phonenumber=request.POST['textfield8']

    lobj=Login()
    lobj.username=Email
    lobj.Password=Phonenumber
    lobj.type="judge"
    lobj.save()

    gjobj = judge()
    gjobj.name = Name
    gjobj.gender = Gender
    gjobj.place = Place
    gjobj.email = Email
    gjobj.phoneno = Phonenumber
    gjobj.hname = housename
    gjobj.proffession = profession
    gjobj.LOGIN=lobj
    gjobj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/home/"</script>''')

def viewjudges(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res=judge.objects.all()
    return render(request,"ADMINISTRATION 1/view judges 7.html",{'data':res})

def viewjudges_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    search=request.POST['textfield']
    res=judge.objects.filter(name__icontains=search)
    return render(request,"ADMINISTRATION 1/view judges 7.html",{'data':res})



def editjudges(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = judge.objects.get(id=id)
    return render(request,"ADMINISTRATION 1/edit judges 8.html",{'data':res})

def editjudges_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    id=request.POST['id']
    Name=request.POST['textfield']
    Gender=request.POST['RadioGroup1']
    housename=request.POST['textfield5']
    Place=request.POST['textfield2']
    profession=request.POST['textfield6']
    Email=request.POST['textfield7']
    Phonenumber=request.POST['textfield8']

    gjobj = judge.objects.get(id=id)
    gjobj.name = Name
    gjobj.gender = Gender
    gjobj.place = Place
    gjobj.email = Email
    gjobj.phoneno = Phonenumber
    gjobj.hname = housename
    gjobj.proffession = profession
    gjobj.save()
    return HttpResponse('''<script>alert('edit Successfully ');window.location="/Myapp/viewjudges/"</script>''')

def delete_judge(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    obj=judge.objects.get(id=id).delete()
    return redirect('/Myapp/viewjudges/',)


def addprogram(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"ADMINISTRATION 1/add program 9.html")

def addprogram_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    programname=request.POST['textfield']
    programtype = request.POST['textfield2']
    isgroupitem=request.POST['textfield3']
    Description=request.POST['textarea']

    gpobj = program()
    gpobj.programname = programname
    gpobj.programtype = programtype
    gpobj.groupprogram = isgroupitem
    gpobj.description = Description
    gpobj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/home/"</script>''')


def viewprogram(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = program.objects.all()
    return render(request,"ADMINISTRATION 1/view program 10.html",{'data':res})

def viewprogram_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    search=request.POST['textfield']
    return HttpResponse("OK")

def editprogram(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=program.objects.get(id=id)
    return render(request,"ADMINISTRATION 1/edit program 11.html",{'data':var})

def editprogram_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    id=request.POST['id']
    programname = request.POST['textfield']
    programtype = request.POST['textfield2']
    isgroupitem = request.POST['textfield3']
    Description = request.POST['textarea']

    gjobj = program.objects.get(id=id)
    gjobj.programname = programname
    gjobj.programtype = programtype
    gjobj.groupprogram = isgroupitem
    gjobj.description = Description
    gjobj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/viewprogram/"</script>''')

def delate_program(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    obj=program.objects.get(id=id).delete()
    return redirect('/Myapp/viewprogram',)

def awards(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=program.objects.all()
    var1=candidate.objects.all()
    return render(request,"ADMINISTRATION 1/awards 12.html",{'data':var,'data1':var1})

def awards_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    groups=request.POST['select2']
    position=request.POST['textfield2']
    Program=request.POST['select3']
    year=request.POST['textfield5']

    gaobj = award()
    gaobj.groupname = groups
    gaobj.PROGRAMME_id = Program
    gaobj.awardtype = position
    gaobj.year=year
    gaobj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/home/"</script>''')



def result(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    cc=candidate.objects.filter(PROGRAM__id=id)
    l=[]
    for i in cc:
        res = candidateresult.objects.filter(CANDIDATE__id=i.id)
        mark=int(0)
        for j in res:
            mark+=int(j.mark)
        l.append({'id':i.id,"GROUP":i.GROUP.groupname,'s':i.name, 'mark':mark})

    for i in range(0,len(l)):
        for j in range(0,len(l)):
            if l[i]['mark'] > l[j]['mark'] :
                temp= l[i]
                l[i]= l[j]
                l[j]= temp
    return render(request, "ADMINISTRATION 1/result  13.html", {'data': l})

    # print(total_sum_of_marks)
    # l=[]
    # for i in res:
    #     l.append({'id':i.id,'cname':i.CANDIDATE.name,'cid':i.CANDIDATE.id,'gname':i.CANDIDATE.GROUP.groupname})

    #     # ss=candidate.objects.filter(id=i.CANDIDATE.id)
    #     ss=candidate.objects.filter(PROGRAMME__id=id).annotate(Count('id=i.CANDIDATE.id'), distinct=True)
    #     l.append({'i'})
    #     print(ss,"hii")
    # return render(request,"ADMINISTRATION 1/result  13.html",{'data':l,'mark':total_sum_of_marks})


def result_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    search=request.POST['textfield']
    res = award.objects.filter(PROGRAMME__programname=search)
    return render(request,"ADMINISTRATION 1/result  13.html",{'data':res})

# def groupresult(request):
#     if  request.session['lid']=='':
#         return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
#     return render(request,"ADMINISTRATION 1/group result.html")


def rulesregulation(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=program.objects.all()
    return render(request,"ADMINISTRATION 1/rules&regulation 14.html",{'data1':var})

def rulesregulation_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    program=request.POST['select2']
    rules=request.POST['textarea']

    gjobj = rulesandregulation()
    gjobj.PROGRAMME_id = program
    gjobj.rules = rules
    gjobj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/home/"</script>''')


def viewrules(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = rulesandregulation.objects.all()
    return render(request,"ADMINISTRATION 1/view rules 15.html",{'data':res})

def viewrules_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    search=request.POST['textfield']
    var=rulesandregulation.objects.filter(PROGRAMME__programname=search)
    return render(request,"ADMINISTRATION 1/view rules 15.html",{'data':var})

def editrules(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var2=program.objects.all()
    var=rulesandregulation.objects.get(id=id)
    return render(request,"ADMINISTRATION 1/edit rules 16.html",{'data':var,'data2':var2})

def editrules_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    id=request.POST['id']
    program = request.POST['select2']
    rules = request.POST['textarea']
    bobj=rulesandregulation.objects.get(id=id)
    bobj.PROGRAMME_id=program
    bobj.rules=rules
    bobj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/viewrules/"</script>''')

def delate_rules(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    obj=rulesandregulation.objects.get(id=id).delete()
    return redirect('/Myapp/viewrules',)



def addprogramshedule(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"ADMINISTRATION 1/addprogramshedule.html")

def addprogramshedule_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    program = request.POST['textfield5']
    date= request.POST['textfield']
    fromd= request.POST['textfield2']
    to = request.POST['textfield3']
    stage = request.POST['textfield4']

    gjobj = programschedule()
    gjobj.Program = program
    gjobj.date = date
    gjobj.fromtime = fromd
    gjobj.totime = to
    gjobj.stage = stage
    gjobj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/home/"</script>''')


def viewprogramshedule(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = programschedule.objects.all()
    return render(request,"ADMINISTRATION 1/viewprogramshedule.html",{'data':res})

def viewprogramshedule_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    Searchprogram = request.POST['textfield']
    Fromd= request.POST['textfield']
    To= request.POST['textfield2']


    return HttpResponse("OK")

def editprogramshedule(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res=programschedule.objects.get(id=id)
    return render(request,"ADMINISTRATION 1/editprogramshedule.html",{'data':res})

def editprogramshedule_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    id=request.POST['id']
    Program= request.POST['textfield5']
    Date= request.POST['textfield']
    Fromd= request.POST['textfield2']
    To= request.POST['textfield3']
    Stage= request.POST['textfield4']

    bobj = programschedule.objects.get(id=id)
    bobj.PROGRAMME_id=program
    bobj.date = Date
    bobj.fromtime = Fromd
    bobj.totime = To
    bobj.stage = Stage
    bobj.save()
    return HttpResponse('''<script>alert('edit Successfully ');window.location="/Myapp/viewprogramshedule/"</script>''')

def delate_shedule(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    obj=programschedule.objects.get(id=id).delete()
    return redirect('/Myapp/viewprogramshedule',)


def programmark(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"ADMINISTRATION 1/program mark 17.html")

def programmark_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    Assignedprograms= request.POST['textfield2']
    Mark= request.POST['textfield3']
    return HttpResponse("OK")

def viewfeedback (request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=Feedback.objects.all()
    l = []
    for i in var:
        if i.type =='judge':
            JJ=judge.objects.get(LOGIN__id=i.LOGIN.id)
            l.append({"feedback":i.feedback,"date":i.date,"uname":JJ.name})
        elif i.type == 'candidate':
            cc=candidate.objects.get(LOGIN__id=i.LOGIN.id)
            l.append({"feedback": i.feedback, "date": i.date, "uname": cc.name})
        elif i.type == 'groupleaders':
            gl = groupleaders.objects.get(LOGIN__id=i.LOGIN.id)
            l.append({"feedback": i.feedback, "date": i.date, "uname": gl.name})
    return render(request,"ADMINISTRATION 1/view feedback 18.html",{"data":l})



def viewfeedback_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    FromDate = request.POST['textfield']
    ToDate = request.POST['textfield2']
    var=Feedback.objects.filtet(date__range=[FromDate,ToDate])
    return render(request,"ADMINISTRATION 1/view feedback 18.html",{'data':var})


def viewcomplaints(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var = Complaint.objects.all()
    l = []
    for i in var:
        if i.type == 'judge':
            JJ = judge.objects.get(LOGIN__id=i.LOGIN.id)
            l.append({"complaint": i.complaint, "date": i.date, "uname": JJ.name,"status":i.status,"replay":i.replay,"id":i.id})
        elif i.type == 'candidate':
            cc = candidate.objects.get(LOGIN__id=i.LOGIN.id)
            l.append({"complaint": i.complaint, "date": i.date, "uname": cc.name,"status":i.status,"replay":i.replay,"id":i.id})
        elif i.type == 'groupleaders':
            gl = groupleaders.objects.get(LOGIN__id=i.LOGIN.id)
            l.append({"complaint": i.complaint, "date": i.date, "uname": gl.name,"status":i.status,"replay":i.replay,"id":i.id})
    return render(request,"ADMINISTRATION 1/view complaints 19.html", {"data": l})


def viewcomplaints_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return HttpResponse("OK")

def sendreply(request, id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"ADMINISTRATION 1/send reply 20.html",{'id':id})

def sendreply_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    replay = request.POST['textarea']
    cid=request.POST['cid']
    var=Complaint.objects.get(id=cid)
    var.replay=replay
    var.status='replied'
    var.save()
    return HttpResponse('''<script>alert('send replay ');window.location="/Myapp/viewcomplaints/"</script>''')

def prgmjudgeallocation(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=program.objects.all()
    var1=judge.objects.all()
    return render(request,"ADMINISTRATION 1/prgm judge allocation 21.html",{'data':var,'data1':var1})

def prgmjudgeallocation_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    program= request.POST['select']
    judges= request.POST['select2']

    gaobj = programjudgeallocation()
    gaobj.PROGRAMME_id= program
    gaobj.JUDGE_id= judges

    gaobj.LOGIN=Login.objects.get(id=request.session['lid'])
    gaobj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/home/"</script>''')


def viewprgmjudgeallocation(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=programjudgeallocation.objects.all()
    return render(request,"ADMINISTRATION 1/view prgm judge allocation 22.html",{'data':var})

def viewprgmjudgeallocation_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    search=request.POST['textfield']
    res=programjudgeallocation.objects.filter(PROGRAMME__programname=search)
    return render(request,"ADMINISTRATION 1/view prgm judge allocation 22.html",{'data':res})


def editprgrmjudgeallocation(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = programjudgeallocation.objects.get(id=id)
    var1=program.objects.all()
    var=judge.objects.all()
    return render(request,"ADMINISTRATION 1/edit prgm judge allocation 23.html",{'data':res,'data1':var1,'data2':var})

def editprgrmjudgeallocation_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    id=request.POST['id']
    program= request.POST['select']
    judges= request.POST['select2']
    gaobj = programjudgeallocation.objects.get(id=id)
    gaobj.PROGRAMME_id = program
    gaobj.JUDGE_id = judges

    gaobj.LOGIN = Login.objects.get(id=request.session['lid'])
    gaobj.save()

    return HttpResponse('''<script>alert(' Edited Successfully ');window.location="/Myapp/viewprgmjudgeallocation/"</script>''')

def delate_allocation(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    obj=programjudgeallocation.objects.get(id=id).delete()
    return redirect('/Myapp/viewprgmjudgeallocation',)


def view_participants(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res=candidate.objects.filter(PROGRAM_id=id)
    return render(request,"ADMINISTRATION 1/participants.html",{"data":res})


def programs(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = program.objects.all()
    return render(request, "ADMINISTRATION 1/programs.html", {'data': res})




def group_result(request):
    from django.db.models import Sum
    all_groups = groups.objects.all()
    l=[]


    allgroupsobjs= groups.objects.all()
    wholegroupids=[]
    wholegroupscores=[]
    for i in allgroupsobjs:
        wholegroupids.append(i.id)
        wholegroupscores.append(0)

    pgm=program.objects.all()
    for  ii in pgm:

        print("inside progrma")
        group_candidates = candidate.objects.filter(PROGRAM=ii)
        grp=[]
        mark=[]
        for i in group_candidates:


            # total_marks = candidateresult.objects.filter(Q(CANDIDATE=i)   Q(CANDIDATE__PROGRAM=ii)).aggregate(total_marks=Sum('mark'))['total_marks']
            total_marks=0
            cc= candidateresult.objects.filter(CANDIDATE=i)

            for imm in cc:

                if imm.PROGRAMME==ii:

                    total_marks= total_marks+ float(imm.mark)












            print(total_marks,"lik", type(total_marks))
            if total_marks >0 :
                grp.append(i.GROUP.id)
                mark.append(float(total_marks))


        for m in range(0,len(mark)):

            for n in range(0,len(mark)):

                if mark[m]> mark[n]:

                    temp= mark[m]
                    mark[m]= mark[n]
                    mark[n]= temp

                    temp = grp[m]
                    grp[m] = grp[n]
                    grp[n] = temp

        if  len(grp)>0:

            for  ii in range(0,len(wholegroupids)):

                if grp[0] == wholegroupids[ii]:

                    wholegroupscores[ii]= wholegroupscores[ii]+ 5

        if len(grp) > 1:

            for ii in range(0, len(wholegroupids)):

                if grp[1] == wholegroupids[ii]:
                    wholegroupscores[ii] = wholegroupscores[ii] + 3

        if len(grp) > 2:

            for ii in range(0, len(wholegroupids)):

                if grp[2] == wholegroupids[ii]:
                    wholegroupscores[ii] = wholegroupscores[ii] + 1


    for i in range(0,len(wholegroupids)):
        for j in range(0,len(wholegroupids)):

            if wholegroupscores[i]> wholegroupscores[j]:

                temp= wholegroupscores[i]
                wholegroupscores[i]= wholegroupscores[j]
                wholegroupscores[j]= temp

                temp= wholegroupids[i]
                wholegroupids[i]= wholegroupids[j]
                wholegroupids[j]= temp



    s=[]

    for i in range(0,len(wholegroupids)):

        gname= groups.objects.get(id= wholegroupids[i])

        s.append(
            {

             'g':gname,
             'score':wholegroupscores[i],
            }
        )




    return render(request, "ADMINISTRATION 1/group result.html",{"data":s})









############################grpup









#
# def group_result(request):
#     from django.db.models import Sum
#     all_groups = groups.objects.all()
#     group_results = {}
#     l=[]
#     c=[]
#     for group_obj in all_groups:
#         group_candidates = candidate.objects.filter(GROUP=group_obj)
#         total_marks = candidateresult.objects.filter(CANDIDATE__in=group_candidates).aggregate(total_marks=Sum('mark'))['total_marks']
#         if total_marks is None:
#             total_marks = 0
#         points = total_marks
#         group_results[group_obj.groupname] = points
#     for group_name, points in group_results.items():
#         l.append({"group":group_name,"point":str(points)})
#
#
#     return render(request, "ADMINISTRATION 1/group result.html",{"data":l})
#













def leaderhome(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return render(request, "TEAM LEADER 2/leader index.html")



def profilegroupleader(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    vars=groupleaders.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"TEAM LEADER 2/profile group leader 1.html",{'data':vars})

def profilegroupleader_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return HttpResponse("OK")

def registercandidate(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    var=program.objects.all()
    vars=groups.objects.all()
    return render(request,"TEAM LEADER 2/register candidate to program 2.html",{'data':vars,'data1':var})

def registercandidate_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    Name = request.POST['textfield']
    gender = request.POST['RadioGroup1']
    Course = request.POST['textfield2']
    Email = request.POST['textfield3']
    phonenumber = request.POST['textfield4']
    program = request.POST['select3']
    print(program,"hlooo")
    group = request.POST['select2']

    lobj = Login()
    lobj.username = Email
    lobj.Password = phonenumber
    lobj.type = "candidate"
    lobj.save()

    globj = candidate()
    globj.name = Name
    globj.gender = gender
    globj.course = Course
    globj.email = Email
    globj.phoneno = phonenumber
    globj.PROGRAM_id= program
    globj.GROUP_id = group
    globj.LOGIN = lobj
    globj.save()
    return HttpResponse('''<script>alert('Successfully Added');window.location="/Myapp/registercandidate/"</script>''')


def viewcandidateprogram(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    res = candidate.objects.all()
    return render(request,"TEAM LEADER 2/view candidate to program 3.html",{'data':res})

def viewcandidateprogram_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    search = request.POST['textfield']
    return HttpResponse("OK")

def Editcandidateprogram(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    var = candidate.objects.get(id=id)
    var1 = groups.objects.all()
    var2=program.objects.all()
    return render(request,"TEAM LEADER 2/Edit candidate program 4.html",{'data': var, 'data2': var1,'data3':var2})

def Editcandidateprogram_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    id = request.POST['id']
    name = request.POST['textfield5']
    gender = request.POST['RadioGroup1']
    course = request.POST['textfield2']
    email = request.POST['textfield3']
    phonenumber = request.POST['textfield4']
    program = request.POST['select3']
    groups = request.POST['select2']

    obj = candidate.objects.get(id=id)
    obj.name = name
    obj.course = course
    obj.email = email
    obj.phoneno = phonenumber
    obj.gender = gender
    obj.GROUP_id = groups
    obj.PROGRAM_id = program
    obj.save()
    return HttpResponse('''<script>alert(' Edited Successfully ');window.location="/Myapp/viewcandidateprogram/"</script>''')


def delete_candiprogram(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    obj=candidate.objects.get(id=id).delete()
    return redirect('/Myapp/viewcandidateprogram',)

def tviewprogram(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    obj=program.objects.all()
    print(obj,"hai")
    return render(request,"TEAM LEADER 2/View program 5.html",{"data":obj})

def tviewprogram_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return HttpResponse("OK")

def lchangepassword(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return render(request,"TEAM LEADER 2/change password  6.html")

def lchangepassword_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    currentpassword = request.POST['textfield']
    Newpassword = request.POST['textfield2']
    Confirmpassword = request.POST['textfield3']
    res = Login.objects.filter(Password=currentpassword, id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(Password=currentpassword, id=request.session['lid'])
        if Newpassword == Confirmpassword:
            res = Login.objects.filter(Password=currentpassword, id=request.session['lid']).update(
                Password=Confirmpassword)
            return HttpResponse('''<script>alert('Changing Successfully');window.location="/Myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert('Password Mismatch');window.location="/Myapp/lchangepassword/"</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid');window.location="/Myapp/lchangepassword/"</script>''')

def viewteammember(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return render(request,"TEAM LEADER 2/view team member 7.html")

def viewteammember_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return HttpResponse("OK")


def lviewcomplaint(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    # l=groupleaders.objects.get(LOGIN=request.session['lid'])


    var = Complaint.objects.filter(LOGIN=request.session['lid'])
    return render(request, "TEAM LEADER 2/view complaint 8.html", {"data": var})


def lviewcomplaint_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return HttpResponse("OK")

def lSendcomplaint(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return render(request,"TEAM LEADER 2/Send complaints 9.html")

def lsendcomplaint_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    complaints = request.POST['textarea']
    var1 = Complaint()
    var1.complaint = complaints
    import datetime
    var1.date = datetime.date.today()
    var1.LOGIN_id = request.session['lid']
    var1.type = 'groupleaders'
    var1.replay='pending'
    var1.status='pending'
    var1.save()
    return HttpResponse("OK")

def lSendfeedback(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return render(request,"TEAM LEADER 2/Send feedback 10.html")

def lsendfeedback_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    cFeedback = request.POST['textarea']
    var1=Feedback()
    var1.feedback=cFeedback
    import datetime
    var1.date=datetime.date.today()
    var1.LOGIN_id=request.session['lid']
    var1.type='groupleaders'
    var1.save()
    return HttpResponse("OK")


def lprograms(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = program.objects.all()
    return render(request, "TEAM LEADER 2/lprograms.html", {'data': res})

def lresult(request, id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    cc = candidate.objects.filter(PROGRAM__id=id)
    l = []
    for i in cc:
            res = candidateresult.objects.filter(CANDIDATE__id=i.id)
            mark = int(0)
            for j in res:
                mark += int(j.mark)
            l.append({'id': i.id, "GROUP": i.GROUP.groupname, 's': i.name, 'mark': mark})

    for i in range(0, len(l)):
        for j in range(0, len(l)):

                if l[i]['mark'] > l[j]['mark']:
                    temp = l[i]
                    l[i] = l[j]
                    l[j] = temp

    return render(request, "TEAM LEADER 2/lresult.html", {'data': l})

        # print(total_sum_of_marks)
        # l=[]
        # for i in res:
        #     l.append({'id':i.id,'cname':i.CANDIDATE.name,'cid':i.CANDIDATE.id,'gname':i.CANDIDATE.GROUP.groupname})

        #     # ss=candidate.objects.filter(id=i.CANDIDATE.id)
        #     ss=candidate.objects.filter(PROGRAMME__id=id).annotate(Count('id=i.CANDIDATE.id'), distinct=True)
        #     l.append({'i'})
        #     print(ss,"hii")
        # return render(request,"ADMINISTRATION 1/result  13.html",{'data':l,'mark':total_sum_of_marks})

def lresult_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
        search = request.POST['textfield']
        res = award.objects.filter(PROGRAMME__programname=search)
        return render(request, "TEAM LEADER 2/lresult.html", {'data': res})


def lgroup_result(request):
            from django.db.models import Sum
            all_groups = groups.objects.all()
            l = []

            allgroupsobjs = groups.objects.all()
            wholegroupids = []
            wholegroupscores = []
            for i in allgroupsobjs:
                wholegroupids.append(i.id)
                wholegroupscores.append(0)

            pgm = program.objects.all()
            for ii in pgm:

                print("inside progrma")
                group_candidates = candidate.objects.filter(PROGRAM=ii)
                grp = []
                mark = []
                for i in group_candidates:

                    # total_marks = candidateresult.objects.filter(Q(CANDIDATE=i)   Q(CANDIDATE__PROGRAM=ii)).aggregate(total_marks=Sum('mark'))['total_marks']
                    total_marks = 0
                    cc = candidateresult.objects.filter(CANDIDATE=i)

                    for imm in cc:

                        if imm.PROGRAMME == ii:
                            total_marks = total_marks + float(imm.mark)

                    print(total_marks, "lik", type(total_marks))
                    if total_marks > 0:
                        grp.append(i.GROUP.id)
                        mark.append(float(total_marks))

                for m in range(0, len(mark)):

                    for n in range(0, len(mark)):

                        if mark[m] > mark[n]:
                            temp = mark[m]
                            mark[m] = mark[n]
                            mark[n] = temp

                            temp = grp[m]
                            grp[m] = grp[n]
                            grp[n] = temp

                if len(grp) > 0:

                    for ii in range(0, len(wholegroupids)):

                        if grp[0] == wholegroupids[ii]:
                            wholegroupscores[ii] = wholegroupscores[ii] + 5

                if len(grp) > 1:

                    for ii in range(0, len(wholegroupids)):

                        if grp[1] == wholegroupids[ii]:
                            wholegroupscores[ii] = wholegroupscores[ii] + 3

                if len(grp) > 2:

                    for ii in range(0, len(wholegroupids)):

                        if grp[2] == wholegroupids[ii]:
                            wholegroupscores[ii] = wholegroupscores[ii] + 1

            for i in range(0, len(wholegroupids)):
                for j in range(0, len(wholegroupids)):

                    if wholegroupscores[i] > wholegroupscores[j]:
                        temp = wholegroupscores[i]
                        wholegroupscores[i] = wholegroupscores[j]
                        wholegroupscores[j] = temp

                        temp = wholegroupids[i]
                        wholegroupids[i] = wholegroupids[j]
                        wholegroupids[j] = temp

            s = []

            for i in range(0, len(wholegroupids)):
                gname = groups.objects.get(id=wholegroupids[i])

                s.append(
                    {

                        'g': gname,
                        'score': wholegroupscores[i],
                    }
                )

            return render(request, "TEAM LEADER 2/lgresult.html", {"data": s})



        ###########judgde############


def judgehome(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request, "JUDGES 3/judgeindex.html")


def jChangepassword(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"JUDGES 3/change password 1.html")

def jchangepassword_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    currentpassword = request.POST['textfield']
    Newpassword = request.POST['textfield2']
    Confirmpassword = request.POST['textfield3']
    res = Login.objects.filter(Password=currentpassword, id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(Password=currentpassword, id=request.session['lid'])
        if Newpassword == Confirmpassword:
            res = Login.objects.filter(Password=currentpassword, id=request.session['lid']).update(
                Password=Confirmpassword)
            return HttpResponse('''<script>alert('Changing Successfully');window.location="/Myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert('Password Mismatch');window.location="/Myapp/jchangepassword/"</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid');window.location="/Myapp/jchangepassword/"</script>''')


def viewprofile(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    vars=judge.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"JUDGES 3/view profile 2.html",{'data':vars})


def viewprofile_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return HttpResponse("OK")

def Viewallocatedprogramcandidate(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=programjudgeallocation.objects.filter(JUDGE__LOGIN_id=request.session['lid'])
    return render(request,"JUDGES 3/View allocated program&candidates 3.html",{'data':var})

def viewallocatedprogramcandidate_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return HttpResponse("OK")

def jViewprogramshedule(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=programschedule.objects.all
    return render(request,"JUDGES 3/view program shedule 4.html",{'data':var})

def jViewprogramshedule_POST(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return HttpResponse("OK")

def jsendfeedback(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return render(request,"JUDGES 3/Send feedback 5.html")

def jsendfeedback_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    cFeedback = request.POST['textarea']
    var1=Feedback()
    var1.feedback=cFeedback
    import datetime
    var1.date=datetime.date.today()
    var1.LOGIN_id=request.session['lid']
    var1.type='judge'
    var1.save()
    return HttpResponse('''<script>alert('send');window.location="/Myapp/jsendfeedback/"</script>''')

def jsendcomplaint(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"JUDGES 3/send complaint.html")

def jsendcomplaint_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    complaints = request.POST['textarea']
    var1 = Complaint()
    var1.complaint = complaints
    import datetime
    var1.date = datetime.date.today()
    var1.LOGIN_id = request.session['lid']
    var1.type = 'candidate'
    var1.replay='pending'
    var1.status='pending'
    var1.save()
    return HttpResponse('''<script>alert('send');window.location="/Myapp/jsendcomplaint/"</script>''')

def jviewcomplaint(request):
        if request.session['lid'] == '':
            return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

        # l=groupleaders.objects.get(LOGIN=request.session['lid'])


        var = Complaint.objects.filter(LOGIN=request.session['lid'])
        return render(request, "JUDGES 3/view complaint 6.html", {"data": var})

def jviewcomplaint_post(request):
        if request.session['lid'] == '':
            return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')



def viewparticipants(request,id):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    ress=candidate.objects.filter(PROGRAM_id=id)
    return render(request,"JUDGES 3/view participans.html",{"data":ress,"pid":id})

def entermark(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    mark=request.POST['textfield']
    pid=request.POST['pid']
    cid=request.POST['cid']
    gid=request.POST['gid']
    res=candidateresult.objects.filter(PROGRAMME_id=pid ,CANDIDATE_id=cid,CANDIDATE__GROUP_id=gid,JUDGE__LOGIN_id=request.session['lid'])
    if res.exists():
        print(res)
        return HttpResponse('''<script>alert('already added');window.location="/Myapp/judgehome/"</script>''')
    else:
        rr = candidateresult()
        rr.PROGRAMME_id = pid
        rr.CANDIDATE_id = cid
        rr.JUDGE = judge.objects.get(LOGIN_id=request.session['lid'])
        rr.mark = mark
        rr.save()
        return HttpResponse('''<script>alert('Successfull');window.location="/Myapp/judgehome/"</script>''')


from django.db.models import Avg
#
# def viewresult(request):
#     candidateresult_objects = candidateresult.objects.all()
#     data = []
#     for result in candidateresult_objects:
#         data.append({
#             'name': result.CANDIDATE.name,
#             'program': result.PROGRAMME.programname,
#             'mark': result.mark
#         })
#     return render(request, "ADMINISTRATION 1/viewresult.html", {'data': data})
#
#

from django.db.models import Avg

def assign_grade(average_mark):
    if average_mark >= 90:
        return 'A'
    elif 80 <= average_mark < 90:
        return 'B'
    elif 70 <= average_mark < 80:
        return 'C'
    elif 60 <= average_mark < 70:
        return 'D'
    else:
        return 'F'

def viewresult(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    candidateresult_objects = candidateresult.objects.all()
    data = []

    for result in candidateresult_objects:
        # Calculate the average mark for each candidate
        average_mark = candidateresult.objects.filter(CANDIDATE=result.CANDIDATE).aggregate(Avg('mark'))['mark__avg']

        # Assign grade based on the average mark
        grade = assign_grade(average_mark)

        # Append the candidate's name, average mark, and grade to the data list
        data.append({
            'name': result.CANDIDATE.name,
            'average_mark': average_mark if average_mark is not None else 0,  # Handle case when no marks are present
            'grade': grade
        })

    return render(request, "ADMINISTRATION 1/viewresult.html", {'data': data})

#
# def viewresult(request):
#     candidateresult_objects = candidateresult.objects.all()
#     data = []
#
#     for result in candidateresult_objects:
#         # Calculate the average mark for each candidate
#         average_mark = candidateresult.objects.filter(CANDIDATE=result.CANDIDATE).aggregate(Avg('mark'))['mark__avg']
#
#         # Append the candidate's name and average mark to the data list
#         data.append({
#             'name': result.CANDIDATE.name,
#             'average_mark': average_mark if average_mark is not None else 0  # Handle case when no marks are present
#         })
#
#     return render(request, "ADMINISTRATION 1/viewresult.html", {'data': data})
#

def jprograms(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = program.objects.all()
    return render(request, "JUDGES 3/jprograms.html", {'data': res})

def jresult(request, id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    cc = candidate.objects.filter(PROGRAM__id=id)
    l = []
    for i in cc:
            res = candidateresult.objects.filter(CANDIDATE__id=i.id)
            mark = int(0)
            for j in res:
                mark += int(j.mark)
            l.append({'id': i.id, "GROUP": i.GROUP.groupname, 's': i.name, 'mark': mark})

    for i in range(0, len(l)):
        for j in range(0, len(l)):

                if l[i]['mark'] > l[j]['mark']:
                    temp = l[i]
                    l[i] = l[j]
                    l[j] = temp

    return render(request, "JUDGES 3/jresult.html", {'data': l})

        # print(total_sum_of_marks)
        # l=[]
        # for i in res:
        #     l.append({'id':i.id,'cname':i.CANDIDATE.name,'cid':i.CANDIDATE.id,'gname':i.CANDIDATE.GROUP.groupname})

        #     # ss=candidate.objects.filter(id=i.CANDIDATE.id)
        #     ss=candidate.objects.filter(PROGRAMME__id=id).annotate(Count('id=i.CANDIDATE.id'), distinct=True)
        #     l.append({'i'})
        #     print(ss,"hii")
        # return render(request,"ADMINISTRATION 1/result  13.html",{'data':l,'mark':total_sum_of_marks})

def jresult_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
        search = request.POST['textfield']
        res = award.objects.filter(PROGRAMME__programname=search)
        return render(request, "JUDGES 3/jresult.html", {'data': res})

def jgroup_result(request):
            from django.db.models import Sum
            all_groups = groups.objects.all()
            l = []

            allgroupsobjs = groups.objects.all()
            wholegroupids = []
            wholegroupscores = []
            for i in allgroupsobjs:
                wholegroupids.append(i.id)
                wholegroupscores.append(0)

            pgm = program.objects.all()
            for ii in pgm:

                print("inside progrma")
                group_candidates = candidate.objects.filter(PROGRAM=ii)
                grp = []
                mark = []
                for i in group_candidates:

                    # total_marks = candidateresult.objects.filter(Q(CANDIDATE=i)   Q(CANDIDATE__PROGRAM=ii)).aggregate(total_marks=Sum('mark'))['total_marks']
                    total_marks = 0
                    cc = candidateresult.objects.filter(CANDIDATE=i)

                    for imm in cc:

                        if imm.PROGRAMME == ii:
                            total_marks = total_marks + float(imm.mark)

                    print(total_marks, "lik", type(total_marks))
                    if total_marks > 0:
                        grp.append(i.GROUP.id)
                        mark.append(float(total_marks))

                for m in range(0, len(mark)):

                    for n in range(0, len(mark)):

                        if mark[m] > mark[n]:
                            temp = mark[m]
                            mark[m] = mark[n]
                            mark[n] = temp

                            temp = grp[m]
                            grp[m] = grp[n]
                            grp[n] = temp

                if len(grp) > 0:

                    for ii in range(0, len(wholegroupids)):

                        if grp[0] == wholegroupids[ii]:
                            wholegroupscores[ii] = wholegroupscores[ii] + 5

                if len(grp) > 1:

                    for ii in range(0, len(wholegroupids)):

                        if grp[1] == wholegroupids[ii]:
                            wholegroupscores[ii] = wholegroupscores[ii] + 3

                if len(grp) > 2:

                    for ii in range(0, len(wholegroupids)):

                        if grp[2] == wholegroupids[ii]:
                            wholegroupscores[ii] = wholegroupscores[ii] + 1

            for i in range(0, len(wholegroupids)):
                for j in range(0, len(wholegroupids)):

                    if wholegroupscores[i] > wholegroupscores[j]:
                        temp = wholegroupscores[i]
                        wholegroupscores[i] = wholegroupscores[j]
                        wholegroupscores[j] = temp

                        temp = wholegroupids[i]
                        wholegroupids[i] = wholegroupids[j]
                        wholegroupids[j] = temp

            s = []

            for i in range(0, len(wholegroupids)):
                gname = groups.objects.get(id=wholegroupids[i])

                s.append(
                    {

                        'g': gname,
                        'score': wholegroupscores[i],
                    }
                )

            return render(request, "JUDGES 3/jgresult.html", {"data": s})




    #########candidate#######

def candidatehome(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request, "CANDIDATE 4/candidate index.html")

def Cchangepassword(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"CANDIDATE 4/change password 1.html")

def Cchangepassword_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    currentpassword = request.POST['textfield']
    Newpassword = request.POST['textfield2']
    Confirmpassword = request.POST['textfield3']
    res = Login.objects.filter(Password=currentpassword, id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(Password=currentpassword, id=request.session['lid'])
        if Newpassword == Confirmpassword:
            res = Login.objects.filter(Password=currentpassword, id=request.session['lid']).update(
                Password=Confirmpassword)
            return HttpResponse('''<script>alert('Changing Successfully');window.location="/Myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert('Password Mismatch');window.location="/Myapp/Cchangepassword/"</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid');window.location="/Myapp/Cchangepassword/"</script>''')

def cviewprogram(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"CANDIDATE 4/View program 2.html")

def cviewprogram_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return HttpResponse("OK")

def Viewcandidateprofile(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    var=candidate.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"CANDIDATE 4/view candidate profile 4.html",{'data':var})

def Viewcandidateprofile_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return HttpResponse("OK")

def CViewprogramshedule(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    var=programschedule.objects.all
    return render(request,"CANDIDATE 4/view program shedule 3.html",{'data':var})

def CViewprogramshedule_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return HttpResponse("OK")

def csendfeedback(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return render(request,"CANDIDATE 4/send feedback.html")

def csendfeedback_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    cFeedback = request.POST['textarea']
    var1=Feedback()
    var1.feedback=cFeedback
    import datetime
    var1.date=datetime.date.today()
    var1.LOGIN_id=request.session['lid']
    var1.type='candidate'
    var1.save()
    return HttpResponse('''<script>alert('send');window.location="/Myapp/csendfeedback/"</script>''')

def csendcomplaint(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    return render(request,"CANDIDATE 4/send complaint.html")


def cviewcomplaint(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    # l=groupleaders.objects.get(LOGIN=request.session['lid'])


    var = Complaint.objects.filter(LOGIN=request.session['lid'])
    return render(request, "CANDIDATE 4/view complaint.html", {"data": var})


def cviewcomplaint_post(request):
    if  request.session['lid']=='':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    fromd=request.POST['fdate']
    tod=request.POST['tdate']
    var = Complaint.objects.filter(LOGIN=request.session['lid'],date__range=[fromd,tod])
    return render(request, "CANDIDATE 4/view complaint.html", {"data": var})



def cviewonallocation(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res=programenrollment.objects.filter(CANDIDATE__LOGIN_id=request.session['lid'])
    return render(request,"CANDIDATE 4/view allocation.html",{'data':res})


#############public##############



def Viewprogram(request):
    res=program.objects.all()
    return render(request,"PUBLIC 5/View program 1.html",{'data':res})

def public_viewprogram_post(request):
    return HttpResponse("OK")

def public_viewprogramshedule(request):
    res = programschedule.objects.all()
    return render(request,"PUBLIC 5/view program shedule 2.html",{'data':res})

def public_viewprogramshedule_post(request):
    Searchprogram = request.POST['textfield']
    Fromd= request.POST['textfield']
    To= request.POST['textfield2']


    return HttpResponse("OK")


def public_home(request):
    # if request.session == '':
    #     return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')

    return render(request,"PUBLIC 5/publicindex.html")


def pprograms(request):
    res = program.objects.all()
    return render(request, "PUBLIC 5/pprograms.html", {'data': res})

def presult(request, id):

        cc = candidate.objects.filter(PROGRAM__id=id)
        l = []
        for i in cc:
            res = candidateresult.objects.filter(CANDIDATE__id=i.id)
            mark = int(0)
            for j in res:
                mark += int(j.mark)
            l.append({'id': i.id, "GROUP": i.GROUP.groupname, 's': i.name, 'mark': mark})

        for i in range(0, len(l)):
            for j in range(0, len(l)):

                if l[i]['mark'] > l[j]['mark']:
                    temp = l[i]
                    l[i] = l[j]
                    l[j] = temp

        return render(request, "PUBLIC 5/presult.html", {'data': l})

        # print(total_sum_of_marks)
        # l=[]
        # for i in res:
        #     l.append({'id':i.id,'cname':i.CANDIDATE.name,'cid':i.CANDIDATE.id,'gname':i.CANDIDATE.GROUP.groupname})

        #     # ss=candidate.objects.filter(id=i.CANDIDATE.id)
        #     ss=candidate.objects.filter(PROGRAMME__id=id).annotate(Count('id=i.CANDIDATE.id'), distinct=True)
        #     l.append({'i'})
        #     print(ss,"hii")
        # return render(request,"ADMINISTRATION 1/result  13.html",{'data':l,'mark':total_sum_of_marks})









def presult_post(request):
        search = request.POST['textfield']
        res = award.objects.filter(PROGRAMME__programname=search)
        return render(request, "PUBLIC 5/presult.html", {'data': res})

def pgroup_result(request):
            from django.db.models import Sum
            all_groups = groups.objects.all()
            l = []

            allgroupsobjs = groups.objects.all()
            wholegroupids = []
            wholegroupscores = []
            for i in allgroupsobjs:
                wholegroupids.append(i.id)
                wholegroupscores.append(0)

            pgm = program.objects.all()
            for ii in pgm:

                print("inside progrma")
                group_candidates = candidate.objects.filter(PROGRAM=ii)
                grp = []
                mark = []
                for i in group_candidates:

                    # total_marks = candidateresult.objects.filter(Q(CANDIDATE=i)   Q(CANDIDATE__PROGRAM=ii)).aggregate(total_marks=Sum('mark'))['total_marks']
                    total_marks = 0
                    cc = candidateresult.objects.filter(CANDIDATE=i)

                    for imm in cc:

                        if imm.PROGRAMME == ii:
                            total_marks = total_marks + float(imm.mark)

                    print(total_marks, "lik", type(total_marks))
                    if total_marks > 0:
                        grp.append(i.GROUP.id)
                        mark.append(float(total_marks))

                for m in range(0, len(mark)):

                    for n in range(0, len(mark)):

                        if mark[m] > mark[n]:
                            temp = mark[m]
                            mark[m] = mark[n]
                            mark[n] = temp

                            temp = grp[m]
                            grp[m] = grp[n]
                            grp[n] = temp

                if len(grp) > 0:

                    for ii in range(0, len(wholegroupids)):

                        if grp[0] == wholegroupids[ii]:
                            wholegroupscores[ii] = wholegroupscores[ii] + 5

                if len(grp) > 1:

                    for ii in range(0, len(wholegroupids)):

                        if grp[1] == wholegroupids[ii]:
                            wholegroupscores[ii] = wholegroupscores[ii] + 3

                if len(grp) > 2:

                    for ii in range(0, len(wholegroupids)):

                        if grp[2] == wholegroupids[ii]:
                            wholegroupscores[ii] = wholegroupscores[ii] + 1

            for i in range(0, len(wholegroupids)):
                for j in range(0, len(wholegroupids)):

                    if wholegroupscores[i] > wholegroupscores[j]:
                        temp = wholegroupscores[i]
                        wholegroupscores[i] = wholegroupscores[j]
                        wholegroupscores[j] = temp

                        temp = wholegroupids[i]
                        wholegroupids[i] = wholegroupids[j]
                        wholegroupids[j] = temp

            s = []
            for i in range(0, len(wholegroupids)):
                gname = groups.objects.get(id=wholegroupids[i])

                s.append(
                    {

                        'g': gname,
                        'score': wholegroupscores[i],
                    }
                )

            return render(request, "PUBLIC 5/pgresult.html", {"data": s})








def candidatelogin(request):
    username=request.POST['username']
    password=request.POST['password']
    log=Login.objects.filter(username=username,Password=password)
    if log.exists():
        log1 = Login.objects.get(username=username, Password=password)
        lid=log1.id
        if log1.type=='candidate':
            return JsonResponse({'status':'ok','lid':str(lid),'type':log1.type})
        else:
            return JsonResponse({'status':'No'})
    else:
        return JsonResponse({'status': 'No'})



def candichangepassword(request):
    lid=request.POST['lid']
    Currentpassword=request.POST['Currentpassword']
    Newpassword=request.POST['Newpassword']
    Confirmpassword=request.POST['Confirmpassword']
    log=Login.objects.filter(Password=Currentpassword,id=lid)
    if log.exists():
        log1 = Login.objects.get(Password=Currentpassword,id=lid)
        if Newpassword==Confirmpassword:
            log1 = Login.objects.filter(Password=Currentpassword, id=lid).update(Password=Newpassword)
            return JsonResponse({'status':'ok'})

        else:
            return JsonResponse({'status':'No'})
    else:
        return JsonResponse({'status':'No'})

def candisendcomplaint(request):
    lid=request.POST['lid']
    complaint=request.POST['']
    cobj=Complaint()
    cobj.complaint=complaint
    import datetime
    cobj.date = datetime.date.today()
    cobj.LOGIN_id = lid
    cobj.type = 'candidate'
    cobj.replay = 'pending'
    cobj.status = 'pending'
    cobj.save()
    return JsonResponse({'status':'ok'})


def candisendfeedback(request):
    lid = request.POST['lid']
    fdbk=request.POST['feedback']

    var1=Feedback()
    var1.feedback=fdbk
    import datetime
    var1.date=datetime.date.today()
    var1.LOGIN_id=lid
    var1.type='candidate'
    var1.save()
    return JsonResponse({'status': 'ok'})


# def candiviewallocation(request):
#     lid = request.POST['lid']
#     obj=programschedule.objects.get(LOGIN_id=lid)
#     l=[]
#     for i in obj:
#         l.append(
#             {'id': i.id, 'programme': i.PROGRAM.programname, 'date': i.date, 'fromtime': i.fromtime, 'totime': i.totime,
#              'stage': i.stage})
#         return JsonResponse({'status': 'ok','data':l})





def candiviewallocation(request):
    lid = request.POST['lid']
    obj=programenrollment.objects.filter(CANDIDATE__LOGIN_id=lid)
    l=[]
    for i in obj:
        l.append(
            {'id': i.PROGRAMMESCHEDULE.PROGRAM.id, 'programme': i.PROGRAMMESCHEDULE.PROGRAM.programname,
             'date': i.PROGRAMMESCHEDULE.date,
             'fromtime': i.PROGRAMMESCHEDULE.fromtime, 'totime': i.PROGRAMMESCHEDULE.totime,
             'stage': i.PROGRAMMESCHEDULE.stage})
    print(l,"lllllllllllll")
    return JsonResponse({'status': 'ok','data':l})


def candiviewcandidateprofile(request):
    lid=request.POST['lid']
    obj=candidate.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','id':obj.id,
                         'name':obj.name,'gender':obj.gender,'course':obj.course,
                         'program':obj.PROGRAM.programname,'email':obj.email,'group':obj.GROUP.groupname,
                         'phoneno':obj.phoneno})

def candiviewcomplaint(request):
    lid = request.POST['lid']
    var=Complaint.objects.filter(LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'complaint':i.complaint,'date':i.date,'status':i.status,'replay':i.replay,'type':i.type})
    return JsonResponse({'status':'ok','data':l})

def candiviewprogramschedule(request):
    # lid =request.POST['lid']
    var=programschedule.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'programname':i.PROGRAM.programname,'date':i.date,'fromtime':i.fromtime,'totime':i.totime,'stage':i.stage})
    return JsonResponse({'status':'ok','data':l})

def candiviewprogram(request):
    # lid=request.POST['lid']
    var=program.objects.all()
    l=[]
    for i in var:
        l.append(
            {'id': i.id, 'programname': i.programname, 'programtype': i.programtype,
             'groupprogram': i.groupprogram, 'description': i.description,})
    return JsonResponse({'status': 'ok','data':l})







def csendcomplaint_post(request):


    id = request.POST['lid']
    complaints = request.POST['comp']
    var1 = Complaint()
    var1.complaint = complaints
    import datetime
    var1.date = datetime.date.today()
    var1.LOGIN =Login.objects.get(id=id)
    var1.type = 'candidate'
    var1.replay='pending'
    var1.status='pending'
    var1.save()
    return JsonResponse({'status':'ok'})



def cprograms(request):
    # if  request.session['lid']=='':
    #     return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    res = program.objects.all()
    l=[]
    for i in res:
        l.append({'id':i.id, "program": i.programname})
    return JsonResponse({'status': 'ok','data':l})

def cresult(request):
    pid=request.POST['pid']
    res = award.objects.filter(GROUPS_id=pid)
    l = []
    for i in res:
     l.append({'id': i.id,'chessnumber':i.ichessnumber, "CANDIDATE": i.CANDIDATE.name, 'GROUPS': i.programname, 'grade': i.grade})
    return JsonResponse({'status': 'ok', 'data': l})
    # if request.session['lid'] == '':
    #     return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
    #
    #     cc = candidate.objects.filter(PROGRAM__id=id)
    #     l = []
    #     for i in cc:
    #         res = candidateresult.objects.filter(CANDIDATE__id=i.id)
    #         mark = int(0)
    #         for j in res:
    #             mark += int(j.mark)
    #         l.append({'id': i.id, "GROUP": i.GROUP.groupname, 's': i.name, 'mark': mark})
    #
    #     for i in range(0, len(l)):
    #         for j in range(0, len(l)):
    #
    #             if l[i]['mark'] > l[j]['mark']:
    #                 temp = l[i]
    #                 l[i] = l[j]
    #                 l[j] = temp

        # return JsonResponse({'status': 'ok', 'data': l})

        # print(total_sum_of_marks)
        # l=[]
        # for i in res:
        #     l.append({'id':i.id,'cname':i.CANDIDATE.name,'cid':i.CANDIDATE.id,'gname':i.CANDIDATE.GROUP.groupname})

        #     # ss=candidate.objects.filter(id=i.CANDIDATE.id)
        #     ss=candidate.objects.filter(PROGRAMME__id=id).annotate(Count('id=i.CANDIDATE.id'), distinct=True)
        #     l.append({'i'})
        #     print(ss,"hii")
        # return render(request,"ADMINISTRATION 1/result  13.html",{'data':l,'mark':total_sum_of_marks})
#
# def cresult_post(request):
#     if request.session['lid'] == '':
#         return HttpResponse('''<script>alert('logout');window.location="/Myapp/login/"</script>''')
#         search = request.POST['textfield']
#         res = award.objects.filter(PROGRAMME__programname=sear)
#         return JsonResponse({'status': 'ok', 'data': l})




def candidate_view_result(request):
    lid=request.POST['lid']
    pid=request.POST['pid']
    cc = candidate.objects.filter(PROGRAM__id=pid)
    l = []
    for i in cc:
        res = candidateresult.objects.filter(CANDIDATE__id=i.id)
        mark = int(0)
        for j in res:
            mark += int(j.mark)
        l.append({'id': i.id, "GROUP": i.GROUP.groupname, 's': i.name, 'mark': mark,"grade":"A"})

    for i in range(0, len(l)):
        for j in range(0, len(l)):

            if l[i]['mark'] > l[j]['mark']:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp


                ############
    # a=[]
    # for k in l:
    #     a.append({"s":k.s,"GROUP":k.GROUP,"mark":k.mark,"grade":k.grade})
    #     print(a)
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})


def cand_pgroup_result(request):
    from django.db.models import Sum
    all_groups = groups.objects.all()
    l = []

    allgroupsobjs = groups.objects.all()
    wholegroupids = []
    wholegroupscores = []
    for i in allgroupsobjs:
        wholegroupids.append(i.id)
        wholegroupscores.append(0)

    pgm = program.objects.all()
    for ii in pgm:

        print("inside progrma")
        group_candidates = candidate.objects.filter(PROGRAM=ii)
        grp = []
        mark = []
        for i in group_candidates:

            # total_marks = candidateresult.objects.filter(Q(CANDIDATE=i)   Q(CANDIDATE__PROGRAM=ii)).aggregate(total_marks=Sum('mark'))['total_marks']
            total_marks = 0
            cc = candidateresult.objects.filter(CANDIDATE=i)

            for imm in cc:

                if imm.PROGRAMME == ii:
                    total_marks = total_marks + float(imm.mark)

            print(total_marks, "lik", type(total_marks))
            if total_marks > 0:
                grp.append(i.GROUP.id)
                mark.append(float(total_marks))

        for m in range(0, len(mark)):

            for n in range(0, len(mark)):

                if mark[m] > mark[n]:
                    temp = mark[m]
                    mark[m] = mark[n]
                    mark[n] = temp

                    temp = grp[m]
                    grp[m] = grp[n]
                    grp[n] = temp

        if len(grp) > 0:

            for ii in range(0, len(wholegroupids)):

                if grp[0] == wholegroupids[ii]:
                    wholegroupscores[ii] = wholegroupscores[ii] + 5

        if len(grp) > 1:

            for ii in range(0, len(wholegroupids)):

                if grp[1] == wholegroupids[ii]:
                    wholegroupscores[ii] = wholegroupscores[ii] + 3

        if len(grp) > 2:

            for ii in range(0, len(wholegroupids)):

                if grp[2] == wholegroupids[ii]:
                    wholegroupscores[ii] = wholegroupscores[ii] + 1

    for i in range(0, len(wholegroupids)):
        for j in range(0, len(wholegroupids)):

            if wholegroupscores[i] > wholegroupscores[j]:
                temp = wholegroupscores[i]
                wholegroupscores[i] = wholegroupscores[j]
                wholegroupscores[j] = temp

                temp = wholegroupids[i]
                wholegroupids[i] = wholegroupids[j]
                wholegroupids[j] = temp

    s = []
    for i in range(0, len(wholegroupids)):
        gname = groups.objects.get(id=wholegroupids[i])

        s.append(
            {

                'g': gname.groupname,
                'score': wholegroupscores[i],
            }
        )

    return JsonResponse({'status':'ok',"data": s})
