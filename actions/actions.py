# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# # from typing import Any, Text, Dict, List
# #
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# #
# #
# # class ActionHelloWorld(Action):
# #
# #     def name(self) -> Text:
# #         return "action_hello_world"
# #
# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #         dispatcher.utter_message(text="Hello World!")
# #
# #         return []

# # actions.py

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ExplainFrequencyVectorAction(Action):
#     def name(self) -> Text:
#         return "explain_frequency_vector"

#     async def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("To create a frequency vector, go under the Tree solution domain node and add the frequency vector.")
#         return []

# class ExplainFrequencySampleAction(Action):
#     def name(self) -> Text:
#         return "explain_frequency_sample"

#     async def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("Set the frequency sample for solving the model in the window below the Tree solution domain node.")
#         return []

# class ExplainInputSpectralDataAction(Action):
#     def name(self) -> Text:
#         return "explain_input_spectral_data"

#     async def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("To input spectral data, store frequency-dependent input data like Permittivity and Conductivity in the model database called 'Spectral Data'.")
#         dispatcher.utter_message("All frequency-dependent input data for the simulation is stored in 'Spectral Data', including Permittivity, Permeability, and Conductivity used in Materials.")
#         dispatcher.utter_message("Q factor, Absorption Coefficient, Reflection Loss, and Absorption Section are used to define Cavity Wavefield Losses.")
#         dispatcher.utter_message("Coupling Loss Factor, Transmission Section, and Power Transmission Coefficient are used to define junctions between cavity wavefields.")
#         dispatcher.utter_message("To add spectral data, right-click and select 'add' to open a dialog box for entering the necessary information.")
#         return []
    
# class add(Action):
#     def name(self) -> Text:
#         return "explain_add_spectral_data_dialog"

# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ExplainFrequencyVectorAction(Action):
    def name(self) -> Text:
        return "explain_frequency_vector"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("To create a frequency vector, go under the Tree solution domain node and add the frequency vector.")
        return []

class ExplainFrequencySampleAction(Action):
    def name(self) -> Text:
        return "explain_frequency_sample"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Set the frequency sample for solving the model in the window below the Tree solution domain node.")
        return []

class ExplainInputSpectralDataAction(Action):
    def name(self) -> Text:
        return "explain_input_spectral_data"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("To input spectral data, store frequency-dependent input data like Permittivity and Conductivity in the model database called 'Spectral Data'.")
        dispatcher.utter_message("All frequency-dependent input data for the simulation is stored in 'Spectral Data', including Permittivity, Permeability, and Conductivity used in Materials.")
        dispatcher.utter_message("Q factor, Absorption Coefficient, Reflection Loss, and Absorption Section are used to define Cavity Wavefield Losses.")
        dispatcher.utter_message("Coupling Loss Factor, Transmission Section, and Power Transmission Coefficient are used to define junctions between cavity wavefields.")
        dispatcher.utter_message("To add spectral data, right-click and select 'add' to open a dialog box for entering the necessary information.")
        return []

class ExplainAddSpectralDataDialogAction(Action):
    def name(self) -> Text:
        return "explain_add_spectral_data_dialog"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Explain adding spectral data using the dialog box.")
        return []

