import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from utils.life_tools import query_liuliang
from utils.linshi import get_token_info
from utils.tools import get_client_ip, get_host_ip


class InfoView(APIView):
    def get(self, *args, **kwargs):
        now_dt = datetime.datetime.now()
        if self.request.query_params.get("token"):
            username = self.request.query_params.get("username")
            passwd = self.request.query_params.get("passwd")
            return Response(get_token_info(username, passwd),
                            content_type="application/json; charset=utf-8")
        data = datetime.datetime.strftime(now_dt, "%Y-%m-%d %H:%M:%S")
        result = {"date": data, "ip": get_client_ip(self.request),
                  "host_ip": get_host_ip()}
        return Response(result)

    def post(self, *args, **kwargs):
        if self.request.query_params.get("token"):
            username = self.request.data.get("username")
            passwd = self.request.data.get("passwd")
            return Response(get_token_info(username, passwd),
                            content_type="application/json; charset=utf-8")

class LifeToolsView(APIView):

    def get(self, *args, **kwargs):
        if self.request.query_params.get("liuliang"):
            return Response(query_liuliang())


class Just200View(View):

    def dispatch(self, request, *args, **kwargs):
        return HttpResponse()

