"""
    Copyright (C) 2023. ExodusEnt Corp. All rights reserved.
    You must have prior written permission to read this file.

    Author: Yoo Jisung <yoojisung@myloveidol.com>
"""

# built-in
import json
from pprint import pformat

# rich
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.console import Console

# django
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class ApiLoggingMiddleware(MiddlewareMixin):
    console = Console()

    def process_request(self, request):
        endpoint = request.path

        method = request.method
        user_agent = request.META.get("HTTP_USER_AGENT", "unknown")

        body = request.body.decode("utf-8")

        info = Text()
        info.append("Endpoint: ", style="bold light_sea_green")
        info.append(f"{method} {endpoint}\n")
        info.append("User Agent: ", style="bold light_sea_green")
        info.append(f"{user_agent}")
        if request.GET:
            info.append("\nUrlParams: ", style="bold light_sea_green")
            info.append(json.dumps(request.GET, indent=4))
        if request.POST:
            info.append("\nFormParams: ", style="bold light_sea_green")
            info.append(json.dumps(request.POST, indent=4))

        if body:
            info.append("\nBody: ", style="bold light_sea_green")
            info.append(pformat(body))

        panel = Panel(info, title="Request", border_style="khaki1")
        self.console.print(panel)

    def process_response(self, request, response):
        info = Text()
        info.append("Status Code: ", style="bold light_sea_green")
        info.append(f"{response.status_code}\n")

        content = response.content.decode("utf-8")

        try:
            content = json.loads(content)
            info.append(pformat(content))
        #     gcode = content.get("gcode")
        #     success = content.get("success")
        #     message = content.get("message")

        #     info.append(f"GCODE: ", style="bold light_sea_green")
        #     info.append(f"{gcode}\n")

        #     info.append(f"SUCCESS: ", style="bold light_sea_green")
        #     info.append(f"{success}")

        #     if message:
        #         info.append(f"\nMESSAGE: ", style="bold light_sea_green")
        #         info.append(f"{message}")
        except:
            info.append(pformat(content))
        
        panel = Panel(info, title="Response", border_style="green")
        self.console.print(panel)

        return response