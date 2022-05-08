from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name="index"),
    path('courses' , views.courses , name="courses"),
    path('admin_panel' , views.notifications , name='notifications'),
    path('register',  views.register , name="register"),
    path('t-register',  views.t_register , name="t-register"),
    path('log_in' , views.login_view , name="log-in"),
    path('log_out' , views.logout_view , name="log-out" ),
    path('confirm_author/<str:con_id>' , views.confirm_author , name="confirm_author"),
    path('decline_author/<str:con_id>' , views.decline_author , name="decline_author"),
    path('std_by_num' , views.std_by_num , name="std_by_num"),
    path('std_dash' , views.std_dash , name="std_dash"),
    path('profile' , views.profile , name="profile"),
    path('program_detail/<int:program_id>' , views.detail, name="detail" ),

]
