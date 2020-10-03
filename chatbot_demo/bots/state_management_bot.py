# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import time
from datetime import datetime

from botbuilder.core import ActivityHandler, ConversationState, TurnContext, UserState
from botbuilder.schema import ChannelAccount

from data_models import ConversationData, UserProfile, Operation, Case


class StateManagementBot(ActivityHandler):
    def __init__(self, conversation_state: ConversationState, user_state: UserState):
        if conversation_state is None:
            raise TypeError(
                "[StateManagementBot]: Missing parameter. conversation_state is required but None was given"
            )
        if user_state is None:
            raise TypeError(
                "[StateManagementBot]: Missing parameter. user_state is required but None was given"
            )

        self.conversation_state = conversation_state
        self.user_state = user_state

        self.conversation_data_accessor = self.conversation_state.create_property(
            "ConversationData"
        )
        self.user_profile_accessor = self.user_state.create_property("UserProfile")

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)

        await self.conversation_state.save_changes(turn_context)
        await self.user_state.save_changes(turn_context)

    async def on_members_added_activity(
            self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "Welcome to MicrosoftDemo Bot Sample. \nHi"
                )

    async def on_message_activity(self, turn_context: TurnContext):
        # Get the state properties from the turn context.
        user_profile = await self.user_profile_accessor.get(turn_context, UserProfile)
        conversation_data = await self.conversation_data_accessor.get(
            turn_context, ConversationData
        )
        user_input = turn_context.activity.text.strip()
        if user_profile.name is None:
            # First time around this is undefined, so we will prompt user for name.
            if conversation_data.prompted_for_user_name:
                # Set the name to what the user provided.
                user_profile.name = user_input

                # Acknowledge that we got their name.
                await turn_context.send_activity(
                    f"Thanks {user_profile.name}. How can we help you?"
                )

                # Reset the flag to allow the bot to go though the cycle again.
                conversation_data.prompted_for_user_name = False
            else:
                # Prompt the user for their name.
                await turn_context.send_activity("What is your name?")

                # Set the flag to true, so we don't prompt in the next turn.
                conversation_data.prompted_for_user_name = True
        elif 'new' in user_input or conversation_data.last_operation_asked == Operation.NEW:
            await self._fill_out_new_case(conversation_data, user_profile, turn_context)
        elif 'track' in user_input or conversation_data.last_operation_asked == Operation.TRACK:
            await self._fill_out_track_case(conversation_data, user_profile, turn_context)
        elif not conversation_data.prompted_for_survey:
            await turn_context.send_activity(
                f"{user_profile.name} would you like to participate on survey?"
            )
        else:
            await turn_context.send_activity(
                f"{user_profile.name}. How can we help you?"
            )

    async def _fill_out_new_case(
            self, flow: ConversationData, profile: UserProfile, turn_context: TurnContext
    ):
        user_input = turn_context.activity.text.strip()

        # ask for issue name
        if flow.last_operation_asked == Operation.NONE:
            await turn_context.send_activity(
                "Let's get started. what is your issue?"
            )
            flow.last_operation_asked = Operation.NEW
            flow.last_case_asked = Case.TITLE

        # ask for issue description
        elif flow.last_case_asked == Case.TITLE and flow.last_operation_asked == Operation.NEW:
            profile.submitted_cases.append([user_input])
            flow.last_case_asked = Case.DESCRIPTION
            await turn_context.send_activity("Please describe your issue?"
                                             )

        # update base and generate id
        elif flow.last_case_asked == Case.DESCRIPTION and flow.last_operation_asked == Operation.NEW:
            profile.submitted_cases[-1].append(user_input)
            flow.last_case_asked = Case.NONE
            flow.last_operation_asked = Operation.NONE
            await turn_context.send_activity("Your issue have been submitted and you can track it by id: 346246"
                                             )

    async def _fill_out_track_case(
            self, flow: ConversationData, profile: UserProfile, turn_context: TurnContext
    ):
        flow.last_operation_asked = Operation.TRACK
        if len(profile.submitted_cases) > 0:
            user_input = turn_context.activity.text.strip()
            if flow.last_case_asked == Case.NONE:
                flow.last_case_asked = Case.ID
                await turn_context.send_activity("You have cases, please send case id,"
                                                 " or send all to view all submitted cases"
                                                 )
            elif 'all' in user_input:
                cases = profile.submitted_cases
                await turn_context.send_activity(str(cases))
            elif user_input in ['12', '13']:
                await turn_context.send_activity("Case state in progress")
            else:
                await turn_context.send_activity("No case wiht the submitted id")
        else:
            await turn_context.send_activity("You dont have any open cases"
                                             )
            flow.last_operation_asked = Operation.NONE
