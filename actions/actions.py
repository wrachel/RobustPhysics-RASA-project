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


# math specs 1 | section 12

class ExplainQuantilesDefinition(Action):
    def name(self) -> Text:
        return "utter_quantiles_definition_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Quantiles in the context of electric field levels represent the maximum expected and minimum expected field levels defined by specific probabilities of the field probability density function.")
        return []

class ExplainPDFDescription(Action):
    def name(self) -> Text:
        return "utter_pdf_description_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The probability density function (PDF) for electric field levels describes the likelihood of observing a particular field level at different positions and frequencies within the cavity.")
        return []

class ExplainCumulativeDistributionFunction(Action):
    def name(self) -> Text:
        return "utter_cumulative_distribution_function_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The cumulative distribution function (CDF) for electric field levels gives the probability that the field level is less than or equal to a given value. It is related to the PDF and used to compute quantiles.")
        return []

class ExplainQuantilesComputation(Action):
    def name(self) -> Text:
        return "utter_quantiles_computation_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Quantiles are computed from the inverse function of the cumulative distribution function (CDF) for specific maximum expected or minimum expected probability limits.")
        return []

class ExplainRelativeVarianceSingleCavity(Action):
    def name(self) -> Text:
        return "utter_relative_variance_single_cavity_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The relative variance of reverberant energy for a single cavity is derived based on modal overlap and the exponential integral. It characterizes the variance of the energy of a reverberant wave field within the cavity.")
        return []

class ExplainRelativeVarianceMultipleCavities(Action):
    def name(self) -> Text:
        return "utter_relative_variance_multiple_cavities_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The relative variance of reverberant energy for multiple connected cavities is formulated using a matrix approach provided by Langley & Cotoni. It propagates the relative variance for any network of multiply connected reverberant fields.")
        return []

class ExplainProbabilisticVariancePowerInput(Action):
    def name(self) -> Text:
        return "utter_probabilistic_variance_power_input_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The probabilistic variance formulation for power input involves evaluating the square of the mean power input vector and the square of the effective constraint power, as defined by Langley & Cotoni.")
        return []

class ExplainProbabilisticVarianceApertureCouplingPower(Action):
    def name(self) -> Text:
        return "utter_probabilistic_variance_aperture_coupling_power_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The probabilistic variance formulation for aperture coupling power includes evaluating the square of the element of the power balance matrix and the loading correlation coefficient, as provided by Langley & Cotoni.")
        return []

class ExplainEffectiveModalOverlap(Action):
    def name(self) -> Text:
        return "utter_effective_modal_overlap_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The effective modal overlap for multiple connected cavities is calculated as the ratio of the effective, coupled cavity modal overlap to the effective, coupled cavity loss factor.")
        return []

class ExplainEffectiveTotalLossFactor(Action):
    def name(self) -> Text:
        return "utter_effective_total_loss_factor_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The effective total loss factor for multiple connected cavities is derived from the net power input to the cavity wavefield, using the modal energy solution obtained from the power balance equation.")
        return []

class ExplainStatisticalEnsembleFormulation(Action):
    def name(self) -> Text:
        return "utter_statistical_ensemble_formulation_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The statistical ensemble formulation for the energy of a reverberant wave field is derived for comparison with the statistics of a finite ensemble of sample data. It involves the modal overlap of the cavity wavefield and the finite number of receiver and source positions.")
        return []

class ExplainMaximumMinimumResponseSpectrumLevels(Action):
    def name(self) -> Text:
        return "utter_maximum_minimum_response_spectrum_levels_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The maximum and minimum response spectrum levels are calculated based on the mean and standard deviation of the logarithm of energy, as well as user-defined probabilities.")
        return []

class ExplainMeanElectricField(Action):
    def name(self) -> Text:
        return "utter_mean_electric_field_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The mean electric field in a cavity is proportional to the total field energy and follows a Log Normal probability density function.")
        return []

class ExplainLocalElectricFieldFrequencyStirred(Action):
    def name(self) -> Text:
        return "utter_local_electric_field_frequency_stirred_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The stochastic limits of the frequency-stirred local electric field in a cavity are determined by the unconditional probability density function introduced earlier. It involves the calculation of probability density function parameters and user-defined probabilities.")
        return []

class ExplainS21OfLocalElectricFieldFrequencyStirred(Action):
    def name(self) -> Text:
        return "utter_s21_of_local_electric_field_frequency_stirred_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The S21 response is proportional to the frequency-stirred stochastic limits of the electric field at any location in the cavity. It is significant in understanding the behavior of the frequency-stirred local electric field.")
        return []


# math specs 1 | section 13

class ExplainDirectFieldCalculation(Action):
    def name(self) -> Text:
        return "utter_direct_field_calculation_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The direct field is calculated as a post-processing operation after the solution of the statistical power balance (SPB) matrix solution. It is the uncorrelated sum of the direct and reverberant fields.")
        return []

class ExplainTotalFieldCalculation(Action):
    def name(self) -> Text:
        return "utter_total_field_calculation_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The total field is calculated by combining the direct and reverberant fields. For a single power source inside a cavity, the direct electric field at a location beyond the near field of the power source is determined.")
        return []

class ExplainNearFieldCorrections(Action):
    def name(self) -> Text:
        return "utter_near_field_corrections_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Near field corrections include field doubling due to coherent reflections at low loss bounding walls and wave scattering about smaller objects within the reverberant field.")
        return []

class ExplainFieldDistribution(Action):
    def name(self) -> Text:
        return "utter_field_distribution_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The total field within the cavity follows a Rice distribution. In a cavity with very low losses, the reverberant field dominates the direct field, resulting in a spatial distribution determined by statistical power balance with a Chi-squared PDF.")
        return []

# math specs 1 | section 14
    
class ExplainGraphInstances(Action):
    def name(self) -> Text:
        return "utter_specific_graph_instances"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Some speciifc graph instances include: Subsystem wavenumber, Subsystem modes in band, Power Inputs ranking chart for any subsystem, and Power input for each source - Mean with Min, Max uncertainty margins")
        return []

# math specs 2 | section 1

class ExplainSimulationToolExplanation(Action):
    def name(self) -> Text:
        return "explain_simulation_tool_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("RobustPhysics' simulation tool simplifies high-frequency cable harness current simulation alongside strong cavity electric fields using stochastic wave mechanics. It couples rigorous physics with statistical modeling, providing a customized solution for NASA's EMC applications. This hybrid approach integrates statistical 3D electric field modeling with deterministic cable harness current modeling. The Phase I STTR validated its efficacy for complex connected cavities, including launch vehicle fairings.")
        return []
    
class ExplainSimulationToolFeatures(Action):
    def name(self) -> Text:
        return "explain_simulation_tool_features"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The main features of RobustPhysics' simulation tool include: 1. Simulation of cavity 3D electric fields using stochastic methods. 2. Deterministic simulation of 5D cable networks. 3. Coupled simulation of cavity-cable networks using stochastic techniques.")
        return []

class ExplainSimulationToolUseCases(Action):
    def name(self) -> Text:
        return "explain_simulation_tool_use_cases"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("RobustPhysics' simulation tool can be applied in various real-world scenarios, including: - Modeling high frequency cable harness currents in the presence of strong cavity electric fields. - Optimizing electromagnetic compatibility (EMC) in NASA's applications. - Simulating complex connected cavities, such as launch vehicle fairings, to ensure efficient power balance.")
        return []

# math specs 2 | section 2

class ExplainCableHarnessModel(Action):
    def name(self) -> Text:
        return "explain_cable_harness_model"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("In the Ph2. STTR Requirements Specification, a cable harness is considered to consist of multiple line segments with uniform section properties.")
        return []

class ExplainSeparableForm(Action):
    def name(self) -> Text:
        return "explain_separable_form"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("For simulating the high frequency currents in each conductor and the radiation loss from each conductor, a key assumption is that the surrounding vector electric field and the surrounding vector magnetic field is a separable product of a propagation function only along the conductor axis and a radiation / scattering function only in the plane transverse to the conductor axis.")
        return []

class ExplainDeterministicTransmissionLineModeling(Action):
    def name(self) -> Text:
        return "explain_deterministic_transmission_line_modeling"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The computational steps of deterministic transmission line modeling involve calculating the per unit length properties of each cable harness segment, calculating transfer matrices for each segment, calculating radiation impedance, assembling end-to-end transfer matrices, defining terminal voltages and currents, solving the transmission line transfer matrix problem, and post-processing the solution for various parameters.")
        return []

class ExplainCanonicalTestCases(Action):
    def name(self) -> Text:
        return "explain_canonical_test_cases"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The Ph2 STTR Test Plan supports validation of transmission line models of specific cable configurations to validate the transmission line computational module.")
        return []
    
# math specs 2 | section 3

class ExplainModelSolutionParameters(Action):
    def name(self) -> Text:
        return "explain_model_solution_parameters_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The model solution parameters include unit systems in SI, such as voltage, current, length, time, and their respective units. It also involves defining the frequency domain, lowest and highest frequencies, and bandwidth parameters.")
        return []

class ExplainFrequencySolutionVector(Action):
    def name(self) -> Text:
        return "explain_frequency_solution_vector_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The frequency solution vector defines the frequency domain for EMC model input parameters. It involves specifying the lowest and highest frequencies.")
        return []

class ExplainConstantBandwidth(Action):
    def name(self) -> Text:
        return "explain_constant_bandwidth_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Constant bandwidth parameters define a frequency range with a uniform bandwidth. The tabular data input format includes model file names, frequency domain type, start frequency, bandwidth, and end frequency.")
        return []

class ExplainLogarithmicBandwidth(Action):
    def name(self) -> Text:
        return "explain_logarithmic_bandwidth_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Logarithmic bandwidth, such as the Third Octave option, is used for frequency band analysis over a wide domain. It involves specifying start and end center frequencies for each frequency band.")
        return []

class ExplainOctaveFrequencies(Action):
    def name(self) -> Text:
        return "explain_octave_frequencies_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Octave frequencies are defined relative to a reference frequency of 1 kHz. The fractional octave frequencies, such as 3rd Octave, 6th Octave, etc., are used to specify lower and upper band frequencies and bandwidth.")
        return []

# math specs 2 | section 4

class ExplainSpectralDataInput(Action):
    def name(self) -> Text:
        return "explain_spectral_data_input_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("There are multiple classes of spectral data, including: relative permittivity, relative permeability, S11, S12, Electric field, conductivity, relative variance, Q factor, loss factor, absorption coefficient, absorption section, reflection loss, power transmission coefficient, transmission section, power, coupling loss factor, voltage source, current source, and impedance. All classes have the same data structure, represented as a table of real valued numbers at frequencies in Hz.")

class ExplainMaterialProperties(Action):
    def name(self) -> Text:
        return "explain_material_properties_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Materials with complex, frequency-dependent properties have properties that vary with frequency. These properties include relative permittivity, relative permeability, conductivity, and others. They require special treatment in modeling due to their frequency dependency.")

# math specs 2 | section 5
        
class ExplainDielectricGasProperties(Action):
    def name(self) -> Text:
        return "explain_dielectric_gas_properties_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Dielectric gas properties include permittivity and permeability.")

class ExplainDielectricSolidProperties(Action):
    def name(self) -> Text:
        return "explain_dielectric_solid_properties_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Dielectric solid properties include permittivity, permeability, conductivity, and mass density.")

class ExplainSolidConductorProperties(Action):
    def name(self) -> Text:
        return "explain_solid_conductor_properties_explanation"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Solid conductor properties include permeability, conductivity, and mass density.")

class ActionBuildAircraftEMCModel(Action):
    def name(self) -> Text:
        return "action_build_aircraft_emc_model"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("To build an aircraft system-level EMC model using Stochastica, follow these steps:\n1. Import simple 3D geometry data using Stochastica's modeling toolbar.\n2. Define area junctions between connected fields and specify field excitation sources.\n3. Solve uncoupled cavity fields and plot output results, including stochastic limits.\n4. Refine the model based on diagnostic plots and adjust sources or transmission paths as necessary.")
        return []

class ActionBuildAutomobileEMCModel(Action):
    def name(self) -> Text:
        return "action_build_automobile_emc_model"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("To build an automobile system-level EMC model using Stochastica, follow these steps:\n1. Import 3D geometry data and define cavity field parameters.\n2. Define area junctions and specify field excitation sources.\n3. Solve cavity fields, plot output results, and analyze stochastic limits.\n4. Create multi-pin connectors, wire conductors, and solve cable harness.\n5. Couple models, identify cable-cavity interactions, and solve coupled model for comprehensive analysis.")
        return []