# from django.contrib import admin
# from django.urls import path
# from app.views import employeeListView, employeeDetailView, userListView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/employee/', employeeListView),
#     path('api/employee/<int:pk>', employeeDetailView),
#     path('api/user/', userListView),
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls'))
]