#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "3b89930e-eef9-41af-9643-1db7fedb0817")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "346fd1977b174cfea0a707e571e77d55")

    LUIS_APP_ID = os.environ.get("LuisAppId", "3b89930e-eef9-41af-9643-1db7fedb0817")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "346fd1977b174cfea0a707e571e77d55")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westus.api.cognitive.microsoft.com")

