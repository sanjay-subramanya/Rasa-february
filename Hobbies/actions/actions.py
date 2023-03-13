from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk import Action, Tracker

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

        
# class ActionSayFood(Action):

    # def name(self) -> Text:
        # return "action_say_player"

    # def run(self, dispatcher: CollectingDispatcher,
            # tracker: Tracker,
            # domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # sport = tracker.get_slot("sport")
        
        # if sport == None:
            # dispatcher.utter_message(text=f"And who is your favourite player in that sport? !Q@W#D My favourite player is Virat Kohli")
        # else:
            # dispatcher.utter_message(text=f"And who is your favourite player in {sport}? !Q@W#D My favourite player is Virat Kohli")
        # return [AllSlotsReset()]

   

