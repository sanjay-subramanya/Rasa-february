from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk import Action, Tracker

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset


# class ActionSayPlace(Action):

    # def name(self) -> Text:
        # return "action_say_place"

    # def run(self, dispatcher: CollectingDispatcher,
            # tracker: Tracker,
            # domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        # place = tracker.get_slot("place")
        
        # if place == None:
            # dispatcher.utter_message(text=f"What are your favourite places there? !Q@W#D My favourite places are the beaches and museums")
        # else:
            # dispatcher.utter_message(text=f"What are your favourite places in {place} !Q@W#D My favourite places are the beaches and museums")
        # return []

        
# class ActionSayFood(Action):

    # def name(self) -> Text:
        # return "action_say_food"

    # def run(self, dispatcher: CollectingDispatcher,
            # tracker: Tracker,
            # domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # place = tracker.get_slot("place")
        
        # if place == None:
            # dispatcher.utter_message(text=f"Are there any famous dishes I can try when I come there? !Q@W#D Yes, you can try biryani and idli. Both are very famous")
        # else:
            # dispatcher.utter_message(text=f"Are there any famous dishes I can try when I come to {place}? !Q@W#D Yes, you can try the biryani and idli. Both are very famous")
        # return [AllSlotsReset()]

   
# class ActionSayBye(Action):

     # def name(self) -> Text:
            # return "action_say_bye"

     # def run(self, dispatcher: CollectingDispatcher,
             # tracker: Tracker,
             # domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        # dispatcher.utter_message(text=f"It was great talking to you. Thank you for your time, goodbye!")
        # return [AllSlotsReset()]
         
