"""Collection of views to launch pages in my Profile Web Project"""

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.http import JsonResponse
from django.shortcuts import render

# from . import logic
# from . import settings


def render_index_page(request):
    """render home/menu page with all further page choices"""
    page_fill = {}
    return render(request, 'mypage/index.html', page_fill)
