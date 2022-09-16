from typing import Dict, Text, Any, List
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher

class ActionValidateTime(Action):
    def name(self) ->Text:
        return 'action_candidate_time_slot'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        var = tracker.get_slot("time")
        from datetime import datetime as dt
        if type(var) != type(dict()):
            time_object = dt.strptime(var, "%Y-%m-%dT%H:%M:%S.%f%z")
            time_object = time_object.strftime("%m/%d/%Y, %H:%M:%S")
            msg = f"Sounds Good ! Your Interview will scheduled on {time_object}. More details will be shared through e-mail.\nHave a great day !!"
        else:
            time_from = dt.strptime(var["from"], "%Y-%m-%dT%H:%M:%S.%f%z")
            time_from = time_from.strftime("%m/%d/%Y, %H:%M:%S")
            time_to = dt.strptime(var["to"], "%Y-%m-%dT%H:%M:%S.%f%z")
            time_to = time_to.strftime("%m/%d/%Y, %H:%M:%S")
            msg = f"Sounds Good ! Your Interview will scheduled between {time_from} and {time_to}. More details will be shared through e-mail.\nHave a great day !!"
        dispatcher.utter_message(text=msg)
        return []