from django.urls import path

from company import views
urlpatterns=[
    path("employee/add",views.employeeadd,name="employeeadd"),
    path("employee/view",views.employeeview,name="employeeview"),
    path("employee/details/<int:id>",views.employeedetails,name="employeedetails"),
    path("employee/details/remove/<int:id>",views.employeeremove,name="removeemp"),
path("employee/details/change/<int:id>",views.employeechange,name="changeemp"),
]