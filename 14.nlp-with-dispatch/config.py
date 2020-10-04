#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "01305c7e-f972-4772-ad8f-7f8d5688c0b5")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "f495ca7f-ca3e-4cb6-98a8-ec2587efba4d")
    # QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://demochatai.cognitiveservices.azure.com/qnamaker")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://demochatai.azurewebsites.net/qnamaker")

    LUIS_APP_ID = os.environ.get("LuisAppId", "fefdce9e-3ac6-444f-93e7-5883652913a9")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "d68868a246ee4552b246d1249ae2273e")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westus.api.cognitive.microsoft.com")






