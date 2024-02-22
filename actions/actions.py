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
    
class ExplainCreateCavityWaveField(Action):
    def name(self) -> Text:
        return "explain_create_cavity_wavefield"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("To create a Cavity Wave Field, select the cavity geometry from the Geometry Table or view in the 3D window.")
        dispatcher.utter_message("Click the Create Cavity Wavefield Icon in the Toolbar.")
        dispatcher.utter_message("Edit dialog will open to complete definition of Cavity reverberant electromagnetic wavefield")
        dispatcher.utter_message("In 3D Window, Cavity Wavefields displayed with GREEN BORDER on selected Geometry")
        dispatcher.utter_message("In Tree view, Cavity Wavefields are listed in Table view")

        return []
    
class ExplainDefineDielectricVolume(Action):
    def name(self) -> Text:
        return "explain_define_dielectric_volume"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("To EDIT dialog for each Cavity, name the wavefield model, define the Dielectric Gas, and define the cavity Volume")

        return []

class ExplainQFactor(Action):
    def name(self) -> Text:
        return "explain_q_factor"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Multiple different components of Loss Factor may need to be defined to establish the Total Q factor for each Cavity Wavefield.")
        dispatcher.utter_message("These can include Wall Loss, Reflection Loss, and Laminate Loss.")
        dispatcher.utter_message("To add Wall Loss, in the dialog, select ADD “Wall Loss” components, and define Conductive Solid Material and Exposed surface Area")
        dispatcher.utter_message("For Absorption Section, in the dialog, select ADD “Absorption Section” components. Units are an effective area (m2). Multiple Absorption Sections are allowed.")
        dispatcher.utter_message("For Reciever Antenna Loss, in the dialog, select ADD “Receiver” antenna loss components and reference the antenna. Multiple Absorption Sections are allowed.")
        dispatcher.utter_message("To add Reflection Loss, in the dialog, select ADD “User-def Reflection Loss” components. Define Reflection Loss of wall material and Exposed surface Area. Multiple Reflection Loss surfaces are allowed.")
        dispatcher.utter_message("For Laminate Loss, in the dialog, select ADD “Laminate Loss” components. Define the PEC-backed Dielectric Laminate, Exposed surface Area, and Range of EM field incidence. Multiple Laminate surfaces are allowed.")

        return []


