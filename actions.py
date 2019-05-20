# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
import twitterAPI as twit

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(
            requests.get("https://api.chucknorris.io/jokes/random").text
        )  # make an api call
        joke = request["value"]  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

class SearchTweet(Action):
    def name(self):
        return "action_search_tweet"

    def run(self, dispatcher, tracker, domain):
        a = ''
        subject = next(tracker.get_latest_entity_values("subject"), None)
        if not subject:
            dispatcher.utter_message("No search found")
            return []

        message = twit.GetTwitter().getTweet(subject)
        dispatcher.utter_message(message)
        return []


class TwitterAction(Action):
    def name(self):
        return "action_twitter"

    def run(self, dispatcher, tracker, domain):
        message = twit.GetTwitter().getTweet("random")
        dispatcher.utter_message(message)
        return []



class SearchCompany(Action):
    def name(self):
        return "action_search_company"

    def run(self, dispatcher, tracker, domain):
        a = ''
        subject = tracker.get_latest_entity_values("ORG")
        if not subject:
            dispatcher.utter_message("No search found")
            return []
        for x in subject:
            message = twit.GetTwitter().getTweet(x)
            dispatcher.utter_message(message)
        return []


class SearchHashtag(Action):
    def name(self):
        return "action_search_hashtag"

    def run(self, dispatcher, tracker, domain):
        a = ''
        subject = next(tracker.get_latest_entity_values("ORG"), None)
        if not subject:
            dispatcher.utter_message("No search found")
            return []

        message = twit.GetTwitter().getTweet(subject)
        dispatcher.utter_message(message)
        return []

    
class SearchUsername(Action):
    def name(self):
        return "action_search_username"

    def run(self, dispatcher, tracker, domain):
        a = ''
        subject = next(tracker.get_latest_entity_values("ORG"), None)
        if not subject:
            dispatcher.utter_message("No search found")
            return []

        message = twit.GetTwitter().getTweet(subject)
        dispatcher.utter_message(message)
        return []
    
'''
next(tracker.get_latest_entity_values(“my_entity_name”), None).
'''
