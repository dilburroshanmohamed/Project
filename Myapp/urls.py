
from django.urls import path

from Myapp import views

urlpatterns = [

    path('login/', views.login),
    path('login_post/', views.login_post),
    path('logout/', views.logout),

    path('admin_change_password/', views.admin_change_password),
    path('achangepassword_post/', views.achangepassword_post),

    path('home/', views.home),

    path('groupleaderadd/', views.groupleaderadd),
    path('groupleaderadd_POST/', views.groupleaderadd_POST),

    path('viewgroupleader/', views.viewgroupleader),
    path('viewgroupleader_post/', views.vieweditgroupleader_post),

    path('editgroupleader/<id>',views.editgroupleader),
    path('editgroupleader_post/',views.editgroupleader_post),

    path('delete_leader/<id>',views.delete_leader),

    path('addjudges/', views.addjudges),
    path('addjudges_post/', views.addjudges_post),

    path('viewjudges/', views.viewjudges),
    path('viewjudges_post/', views.viewjudges_post),

    path('editjudges/<id>', views.editjudges),
    path('editjudges_post/', views.editjudges_post),

    path('delete_judge/<id>',views.delete_judge),

    path('addprogram/', views.addprogram),
    path('addprogram_post/', views.addprogram_post),

    path('viewprogram/', views.viewprogram),
    path('viewprogram_post/', views.viewprogram_post),

    path('editprogram/<id>', views.editprogram),
    path('editprogram_post/', views.editprogram_post),

    path('delate_program/<id>',views.delate_program),

    path('awards/', views.awards),
    path('awards_post/', views.awards_post),

    path('result/<id>', views.result),
    path('result_post/', views.result_post),

    path('rulesregulation/', views.rulesregulation),
    path('rulesregulation_post/', views.rulesregulation_post),

    path('viewrules/', views.viewrules),
    path('viewrules_post/', views.viewrules_post),

    path('editrules/<id>', views.editrules),
    path('editrules_post/', views.editrules_post),

    path('delate_rules/<id>', views.delate_rules),

    path('addprogramshedule/', views.addprogramshedule),
    path('addprogramshedule_post/', views.addprogramshedule_post),

    path('viewprogramshedule/', views.viewprogramshedule),
    path('viewprogramshedule_post/', views.viewprogramshedule_post),

    path('editprogramshedule/<id>', views.editprogramshedule),
    path('editprogramshedule_post/', views.editprogramshedule_post),

    path('delate_shedule/<id>',views.delate_shedule),

    path('programmark/', views.programmark),
    path('programmark_post/', views.programmark_post),

    path('viewfeedback/', views.viewfeedback),
    path('viewfeedback_post/', views.viewfeedback_post),

    path('viewcomplaints/', views.viewcomplaints),
    path('viewcomplaints_post/', views.viewcomplaints_post),

    path('sendreply/<id>', views.sendreply),
    path('sendreply_post/', views.sendreply_post),

    path('prgmjudgeallocation/', views.prgmjudgeallocation),
    path('prgmjudgeallocation_post/', views.prgmjudgeallocation_post),

    path('viewprgmjudgeallocation/', views.viewprgmjudgeallocation),
    path('viewprgmjudgeallocation_post/', views.viewprgmjudgeallocation_post),


    path('view_participants/<id>', views.view_participants),

    path('editprgmjudgeallocation/<id>', views.editprgrmjudgeallocation),
    path('editprgmjudgeallocation_post/', views.editprgrmjudgeallocation_post),

    path('delate_allocation/<id>',views.delate_allocation),

    path('groupadd/', views.groupadd),
    path('groupadd_post/', views.groupadd_post),

    path('groupview/', views.groupview),
    path('groupview_post/', views.groupview_post),

    path('delete_group/<id>',views.delete_group),

    path('editgroup/<id>', views.editgroup),
    path('editgroup_post/', views.editgroup_post),


    path('programs/',views.programs),

    path('viewresult/',views.viewresult),

    path('group_result/',views.group_result),



    ###########leader###########



    path('profilegroupleader/',views.profilegroupleader),
    path('profilegroupleader_post/', views.profilegroupleader_post),

    path('leaderhome/', views.leaderhome),

    path('registercandidate/',views.registercandidate),
    path('registercandidate_post/', views.registercandidate_post),

    path('viewcandidateprogram/', views.viewcandidateprogram),
    path('viewcandidateprogram_Post/', views.viewcandidateprogram_post),

    path('Editcandidateprogram/<id>', views. Editcandidateprogram),
    path('Editcandidateprogram_post/', views.Editcandidateprogram_post),

    path('delete_candiprogram/<id>',views.delete_candiprogram),

    path('tviewprogram/', views.tviewprogram),
    path('tviewprogram_post/', views.tviewprogram_post),

    path('lchangepassword/', views.lchangepassword),
    path('lchangepassword_post/', views.lchangepassword_post),

    path('viewteammember/', views.viewteammember),
    path('viewteammember_post/', views.viewteammember_post),

    path('lviewcomplaint/', views. lviewcomplaint),
    path('lviewcomplaint_post/', views.lviewcomplaint_post),

    path('lSendcomplaint/', views.lSendcomplaint),
    path('lsendcomplaint_post/', views.lsendcomplaint_post),

    path('lSendfeedback/', views. lSendfeedback),
    path('lsendfeedback_post/', views.lsendfeedback_post),

    path('lprograms/',views.lprograms),

    path('viewresult/', views.viewresult),


    path('lresult/<id>', views.lresult),
    path('lresult_post/', views.lresult_post),

    path('lgroup_result/', views.lgroup_result),

    #########judge#########

    path('judgehome/', views.judgehome),

    path('jchangepassword/',views.jChangepassword),
    path('jchangepassword_post/', views.jchangepassword_post),

    path('viewprofile/', views.viewprofile),
    path('viewprofile_Post/', views.viewprofile_post),

    path('viewallocatedprogramcandidate/', views.Viewallocatedprogramcandidate),
    path('viewallocatedprogram&candidate_post/', views.viewallocatedprogramcandidate_post),

    path('jViewprogramshedule/',views. jViewprogramshedule),
    path('jViewprogramshedule_POST/',views.jViewprogramshedule_POST),

    path('jsendfeedback/', views.jsendfeedback),
    path('jsendfeedback_post/', views.jsendfeedback_post),

    path('jsendcomplaint/', views.jsendcomplaint),
    path('jsendcomplaint_post/', views.jsendcomplaint_post),

    path('jviewcomplaint/', views.jviewcomplaint),
    path('jviewcomplaint_post/', views.jviewcomplaint_post),

    path('viewparticipants/<id>',views.viewparticipants),
    path('entermark/',views.entermark),

    path('jprograms/',views.jprograms),

    path('viewresult/', views.viewresult),


    path('jresult/<id>', views.jresult),
    path('jresult_post/', views.jresult_post),

    path('jgroup_result/', views.jgroup_result),


    ######candidate######

   # path('candidatehome/', views.candidatehome),
   # path('Cchangepassword/', views.Cchangepassword),
   # path('Cchangepassword_post/', views.Cchangepassword_post),
   #
   # path('viewprogram/', views.viewprogram),
   # path('viewprogram_post/', views.viewprogram_post),
   #
   # path('Viewcandidateprofile/', views. Viewcandidateprofile),
   # path('Viewcandidateprofile_post/', views.Viewcandidateprofile_post),
   #
   # path('CViewprogramshedule/', views. CViewprogramshedule),
   # path('CViewprogramshedule_post/', views.CViewprogramshedule_post),
   #
   # path('csendfeedback/', views.csendfeedback),
   # path('csendfeedback_post/', views.csendfeedback_post),
   #
   # path('csendcomplaint/', views.csendcomplaint),
   # path('csendcomplaint_post/', views.csendcomplaint_post),
   #
   # path('cviewcomplaint/', views.cviewcomplaint),
   # path('cviewcomplaint_post/', views.cviewcomplaint_post),
   path('cviewonallocation/', views.cviewonallocation),

    #########public############

         path('Viewprogram/', views.Viewprogram),
         path('public_viewprogram_post/', views.public_viewprogram_post),
         path('public_viewprogramshedule/', views.public_viewprogramshedule),
         path('public_viewprogramshedule_post/', views.public_viewprogramshedule_post),
        path('public_home/',views.public_home),

    path('pprograms/', views.pprograms),

    path('viewresult/', views.viewresult),

    path('presult/<id>', views.presult),
    path('presult_post/', views.presult_post),


    path('pgroup_result/', views.pgroup_result),


   #########candidate app##############
    path('candidatelogin/',views.candidatelogin),
    path('candidatehome/', views.candidatehome),
    path('candichangepassword/', views.candichangepassword),

    path('candiviewprogram/', views.candiviewprogram),

    path('candiviewcandidateprofile/', views.candiviewcandidateprofile),

    path('candiviewprogramschedule/', views.candiviewprogramschedule),
    path('candiviewallocation/',views.candiviewallocation),

    path('candisendfeedback/', views.candisendfeedback),

    path('csendcomplaint_post/', views.csendcomplaint_post),

    path('candiviewcomplaint/', views.candiviewcomplaint),
    path('candiviewallocation/', views.cviewonallocation),
    path('cprograms/', views.cprograms),
    path('cresult/', views.cresult),
    # path('cresult_result/', views.cresult_post),
    path('cresult_result/', views.candidate_view_result),
    path('cand_pgroup_result/', views.cand_pgroup_result),


]