#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "aea5e70e-8550-4e71-a984-bdf0422d99e6")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "JqUnA;XCrrbage?{-Rf1LW{g=fAS=b/F")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "01305c7e-f972-4772-ad8f-7f8d5688c0b5")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "f495ca7f-ca3e-4cb6-98a8-ec2587efba4d")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://demochatai.cognitiveservices.azure.com/qnamaker")
