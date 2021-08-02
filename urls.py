
from django.contrib import admin
from django.urls import path,include
from account.views import home
urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path('acc-',include(('account.urls','account'),namespace='account')),
    path('inc-',include(('income.urls','income'),namespace='income')),
    path('exp-',include(('expense.urls','expense'),namespace='expense')),
]


'''
<a href="{% url 'key:value%}' ">
1)key is mapping for app in project URL
2) value is mapping for function in app URL

3) key is always Match with NameSpace
4) value is always Match with Name Attribut

'''