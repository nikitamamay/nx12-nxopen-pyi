# module 'NXOpen.CAE.ResponseSimulation'
#
# Automatically generated 2025-06-09T14:38:44.527382
#

import typing

import NXOpen
import NXOpen.CAE
import NXOpen.GeometricUtilities



class StrengthStressMaterialDefinitionMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StrengthStressMaterialDefinitionMethod():
    """
    Specifies the definition method for material 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UltimateSafety", " - "
       "YieldSafety", " - "
    """
    UltimateSafety = 0  # StrengthStressMaterialDefinitionMethodMemberType
    YieldSafety = 1  # StrengthStressMaterialDefinitionMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SolutionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of response analysis meta solution   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.ResponseSimulation.Manager`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateSolutionBuilder(self, raSolution: Solution) -> SolutionBuilder:
        """
        Creates the builder object of response analysis meta solution  
        
        Signature ``CreateSolutionBuilder(raSolution)`` 
        
        :param raSolution: 
        :type raSolution: :py:class:`NXOpen.CAE.ResponseSimulation.Solution` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.SolutionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CloneSolution(self, oldSolution: Solution, suggestedName: str) -> Solution:
        """
        Clones a response analysis meta solution  
        
        Signature ``CloneSolution(oldSolution, suggestedName)`` 
        
        :param oldSolution:  the :py:class:`CAE.SimSolution` to be cloned  
        :type oldSolution: :py:class:`NXOpen.CAE.ResponseSimulation.Solution` 
        :param suggestedName:  name to use instead of default name (may be NULL)  
        :type suggestedName: str 
        :returns:  the  newly created :py:class:`CAE.ResponseSimulation.Solution`   
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.Solution` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def FindObject(self, solutionName: str) -> Solution:
        """
        Finds a response analysis meta solution with specified solution name  
        
        Signature ``FindObject(solutionName)`` 
        
        :param solutionName: 
        :type solutionName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.Solution` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    ActiveSolution: Solution = ...
    """
    Returns or sets  the active solution 
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveSolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.Solution` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveSolution`` 
    
    :param activeSolution: 
    :type activeSolution: :py:class:`NXOpen.CAE.ResponseSimulation.Solution` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """


class ExcitationComponentMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ExcitationComponent():
    """
    Represents the component type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DistributedLoad", " - "
       "X", " - "
       "Y", " - "
       "Z", " - "
       "Rx", " - "
       "Ry", " - "
       "Rz", " - "
       "UserDefined", " - "
    """
    DistributedLoad = -1  # ExcitationComponentMemberType
    X = 0  # ExcitationComponentMemberType
    Y = 1  # ExcitationComponentMemberType
    Z = 2  # ExcitationComponentMemberType
    Rx = 3  # ExcitationComponentMemberType
    Ry = 4  # ExcitationComponentMemberType
    Rz = 5  # ExcitationComponentMemberType
    UserDefined = 6  # ExcitationComponentMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Excitation(NXOpen.NXObject):
    """
    Represents the abstract class of dynamic excitations   
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    
    class Component():
        """
        Represents the component type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DistributedLoad", " - "
           "X", " - "
           "Y", " - "
           "Z", " - "
           "Rx", " - "
           "Ry", " - "
           "Rz", " - "
           "UserDefined", " - "
        """
        DistributedLoad = -1  # ExcitationComponentMemberType
        X = 0  # ExcitationComponentMemberType
        Y = 1  # ExcitationComponentMemberType
        Z = 2  # ExcitationComponentMemberType
        Rx = 3  # ExcitationComponentMemberType
        Ry = 4  # ExcitationComponentMemberType
        Rz = 5  # ExcitationComponentMemberType
        UserDefined = 6  # ExcitationComponentMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Destroy(self) -> None:
        """
        Deletes a response simulation excitation 
        
        Signature ``Destroy()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    ExcitationName: str = ...
    """
    Returns or sets  the excitation name 
    
    <hr>
    
    Getter Method
    
    Signature ``ExcitationName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ExcitationName`` 
    
    :param excitationName: 
    :type excitationName: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: Excitation = ...  # unknown typename


class NodalFunctionExcitationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodalFunctionExcitationType():
    """
    the subtype of nodal function excitation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NodalForce", " - "
       "EnforcedMotion", " - "
    """
    NodalForce = 0  # NodalFunctionExcitationTypeMemberType
    EnforcedMotion = 1  # NodalFunctionExcitationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NodalFunctionExcitation(Excitation):
    """
    Represents the abstract class of nodal function excitation   
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    
    class Type():
        """
        the subtype of nodal function excitation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NodalForce", " - "
           "EnforcedMotion", " - "
        """
        NodalForce = 0  # NodalFunctionExcitationTypeMemberType
        EnforcedMotion = 1  # NodalFunctionExcitationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Null: NodalFunctionExcitation = ...  # unknown typename


class TranslationalNodalFunctionExcitation(NodalFunctionExcitation):
    """
    Represents a translational nodal function excitation   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: TranslationalNodalFunctionExcitation = ...  # unknown typename


class FrequencyDefinitionInterpolationMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FrequencyDefinitionInterpolationMethod():
    """
    Specifies the method for interpolation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "LogLog", " - "
       "LogLinear", " - "
       "LinearLinear", " - "
    """
    LogLog = 0  # FrequencyDefinitionInterpolationMethodMemberType
    LogLinear = 1  # FrequencyDefinitionInterpolationMethodMemberType
    LinearLinear = 2  # FrequencyDefinitionInterpolationMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FrequencyDefinitionDefinitionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FrequencyDefinitionDefinition():
    """
    Specifies the method to define frequency 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Range", " - "
       "ModalContribution", " - "
    """
    Range = 0  # FrequencyDefinitionDefinitionMemberType
    ModalContribution = 1  # FrequencyDefinitionDefinitionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FrequencyDefinition(NXOpen.TaggedObject):
    """
    Represents the frequency setting to perform FRF evaluation   
    
    .. versionadded:: NX5.0.0
    """
    
    class InterpolationMethod():
        """
        Specifies the method for interpolation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "LogLog", " - "
           "LogLinear", " - "
           "LinearLinear", " - "
        """
        LogLog = 0  # FrequencyDefinitionInterpolationMethodMemberType
        LogLinear = 1  # FrequencyDefinitionInterpolationMethodMemberType
        LinearLinear = 2  # FrequencyDefinitionInterpolationMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Definition():
        """
        Specifies the method to define frequency 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Range", " - "
           "ModalContribution", " - "
        """
        Range = 0  # FrequencyDefinitionDefinitionMemberType
        ModalContribution = 1  # FrequencyDefinitionDefinitionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetFrequencies(self) -> 'list[float]':
        """
        Returns frequency values to perform FRF evaluation.  
        
        Only available when the frequency definition 
        method is :py:class:`CAE.ResponseSimulation.FrequencyDefinitionDefinition.ModalContribution <CAE.ResponseSimulation.FrequencyDefinitionDefinition>`  
        
        Signature ``GetFrequencies()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetFrequencies(self, frequencies: 'list[float]') -> None:
        """
        Sets the frequency values to perform FRF evaluation.  
        
        Only available when the frequency definition 
        method is :py:class:`CAE.ResponseSimulation.FrequencyDefinitionDefinition.ModalContribution <CAE.ResponseSimulation.FrequencyDefinitionDefinition>` 
        
        Signature ``SetFrequencies(frequencies)`` 
        
        :param frequencies: 
        :type frequencies: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    ContributorNumber: int = ...
    """
    Returns or sets  the number of contributors.  
    
    Only available when maximu contributors
    will be generated 
    
    <hr>
    
    Getter Method
    
    Signature ``ContributorNumber`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ContributorNumber`` 
    
    :param contributorNumber: 
    :type contributorNumber: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    EndValue: float = ...
    """
    Returns or sets  the end value of frequency range.  
    
    Only available when the frequency is defined 
    by :py:class:`CAE.ResponseSimulation.FrequencyDefinitionDefinition.Range <CAE.ResponseSimulation.FrequencyDefinitionDefinition>` 
    
    <hr>
    
    Getter Method
    
    Signature ``EndValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``EndValue`` 
    
    :param endValue: 
    :type endValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    EvaluationType: FrequencyDefinitionDefinition = ...
    """
    Returns or sets  the method to define frequency
    
    <hr>
    
    Getter Method
    
    Signature ``EvaluationType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FrequencyDefinitionDefinition` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``EvaluationType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.CAE.ResponseSimulation.FrequencyDefinitionDefinition` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    GenerateMaximumContributors: bool = ...
    """
    Returns or sets  the option for generating maximum contributors or not.  
    
    Only available when
    frequency definition metod is :py:class:`CAE.ResponseSimulation.FrequencyDefinitionDefinition.ModalContribution <CAE.ResponseSimulation.FrequencyDefinitionDefinition>` 
    
    <hr>
    
    Getter Method
    
    Signature ``GenerateMaximumContributors`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``GenerateMaximumContributors`` 
    
    :param generateMaximumContributors: 
    :type generateMaximumContributors: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    InterpolationMethodOption: FrequencyDefinitionInterpolationMethod = ...
    """
    Returns or sets  the interpolation method.  
    
    Only available when the frequency is defined by
    :py:class:`CAE.ResponseSimulation.FrequencyDefinitionDefinition.Range <CAE.ResponseSimulation.FrequencyDefinitionDefinition>` 
    
    <hr>
    
    Getter Method
    
    Signature ``InterpolationMethodOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FrequencyDefinitionInterpolationMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``InterpolationMethodOption`` 
    
    :param interpolationMethod: 
    :type interpolationMethod: :py:class:`NXOpen.CAE.ResponseSimulation.FrequencyDefinitionInterpolationMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    NormalizeResults: bool = ...
    """
    Returns or sets  the option to normalize results.  
    
    Only available when maximu contributors
    will be generated 
    
    <hr>
    
    Getter Method
    
    Signature ``NormalizeResults`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``NormalizeResults`` 
    
    :param normalizeResults: 
    :type normalizeResults: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SpectralLine: int = ...
    """
    Returns or sets  the additional spectral lines.  
    
    Only available when frequency is defined 
    by :py:class:`CAE.ResponseSimulation.FrequencyDefinitionDefinition.Range <CAE.ResponseSimulation.FrequencyDefinitionDefinition>` 
    
    <hr>
    
    Getter Method
    
    Signature ``SpectralLine`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SpectralLine`` 
    
    :param spectralLines: 
    :type spectralLines: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    StartValue: float = ...
    """
    Returns or sets  the start value of frequency range.  
    
    Only available when the frequency is defined
    by :py:class:`CAE.ResponseSimulation.FrequencyDefinitionDefinition.Range <CAE.ResponseSimulation.FrequencyDefinitionDefinition>` 
    
    <hr>
    
    Getter Method
    
    Signature ``StartValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``StartValue`` 
    
    :param startValue: 
    :type startValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: FrequencyDefinition = ...  # unknown typename


class EvaluationSettingManager():
    """
    Represents the manager of all evaluation setting objects.  
    
    Any evaluation setting object must 
    be created through this class 
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.ResponseSimulation.Manager`
    
    .. versionadded:: NX5.0.0
    """
    
    def CreateFrfEvaluationSettingBuilder(self, setting: FrfEvaluationSetting) -> FrfEvaluationSettingBuilder:
        """
        Creates FRF evaluation setting object  
        
        Signature ``CreateFrfEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.FrfEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FrfEvaluationSettingBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateCsdEvaluationSettingBuilder(self, setting: CsdEvaluationSetting) -> CsdEvaluationSettingBuilder:
        """
        Creates CSD evaluation setting object  
        
        Signature ``CreateCsdEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.CsdEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CsdEvaluationSettingBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateTransmissibilityEvaluationSettingBuilder(self, setting: TransmissibilityEvaluationSetting) -> TransmissibilityEvaluationSettingBuilder:
        """
        Creates transmissibility evaluation setting object  
        
        Signature ``CreateTransmissibilityEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateNodalFunctionEvaluationSettingBuilder(self, setting: NodalFunctionEvaluationSetting) -> NodalFunctionEvaluationSettingBuilder:
        """
        Creates nodal function evaluation setting object  
        
        Signature ``CreateNodalFunctionEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSettingBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateElementalFunctionEvaluationSettingBuilder(self, setting: ElementalFunctionEvaluationSetting) -> ElementalFunctionEvaluationSettingBuilder:
        """
        Creates elemental function evaluation setting object  
        
        Signature ``CreateElementalFunctionEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSettingBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateResponseResultsEvaluationSettingBuilder(self, setting: ResponseResultsEvaluationSetting) -> ResponseResultsEvaluationSettingBuilder:
        """
        Creates response results evaluation setting object  
        
        Signature ``CreateResponseResultsEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSettingBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateStrengthResultsEvaluationSettingBuilder(self, setting: StrengthResultsEvaluationSetting) -> StrengthResultsEvaluationSettingBuilder:
        """
        Creates strength results evaluation setting object  
        
        Signature ``CreateStrengthResultsEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSettingBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreatePeakValueEvaluationSettingBuilder(self, setting: PeakValueEvaluationSetting) -> PeakValueEvaluationSettingBuilder:
        """
        Creates peak value evaluation setting object  
        
        Signature ``CreatePeakValueEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSettingBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateRmsResultsEvaluationSettingBuilder(self, setting: RmsResultsEvaluationSetting) -> RmsResultsEvaluationSettingBuilder:
        """
        Creates RMS results evaluation setting object  
        
        Signature ``CreateRmsResultsEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSettingBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateLcrResultsEvaluationSettingBuilder(self, setting: LcrResultsEvaluationSetting) -> LcrResultsEvaluationSettingBuilder:
        """
        Creates LCR results evaluation setting object  
        
        Signature ``CreateLcrResultsEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSettingBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateStrainGageEvaluationSettingBuilder(self, setting: StrainGageEvaluationSetting) -> StrainGageEvaluationSettingBuilder:
        """
        Creates strain gage evaluation setting object  
        
        Signature ``CreateStrainGageEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSettingBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateSensorEvaluationSettingBuilder(self, setting: SensorEvaluationSetting) -> SensorEvaluationSettingBuilder:
        """
        Creates sensor evaluation setting object  
        
        Signature ``CreateSensorEvaluationSettingBuilder(setting)`` 
        
        :param setting: 
        :type setting: :py:class:`NXOpen.CAE.ResponseSimulation.SensorEvaluationSetting` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.SensorEvaluationSettingBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    


class VelocityImpactDirectionDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VelocityImpactDirectionDirectionType():
    """
    the direction options for impact 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NodalComponent", " - "
       "UserDefined", " - "
    """
    NodalComponent = 0  # VelocityImpactDirectionDirectionTypeMemberType
    UserDefined = 1  # VelocityImpactDirectionDirectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class VelocityImpactDirectionNodalComponentTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VelocityImpactDirectionNodalComponentType():
    """
    the types of nodal component 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Dof1", " - "
       "Dof2", " - "
       "Dof3", " - "
    """
    Dof1 = 0  # VelocityImpactDirectionNodalComponentTypeMemberType
    Dof2 = 1  # VelocityImpactDirectionNodalComponentTypeMemberType
    Dof3 = 2  # VelocityImpactDirectionNodalComponentTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class VelocityImpactDirection(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactDirection`
    
    .. versionadded:: NX6.0.0
    """
    
    class DirectionType():
        """
        the direction options for impact 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NodalComponent", " - "
           "UserDefined", " - "
        """
        NodalComponent = 0  # VelocityImpactDirectionDirectionTypeMemberType
        UserDefined = 1  # VelocityImpactDirectionDirectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class NodalComponentType():
        """
        the types of nodal component 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Dof1", " - "
           "Dof2", " - "
           "Dof3", " - "
        """
        Dof1 = 0  # VelocityImpactDirectionNodalComponentTypeMemberType
        Dof2 = 1  # VelocityImpactDirectionNodalComponentTypeMemberType
        Dof3 = 2  # VelocityImpactDirectionNodalComponentTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Validate(self) -> bool:
        """
        Validate whether the inputs to the component are sufficient for 
        commit to be called.  
        
        If the component is not in a state to commit
        then an exception is thrown.  For example, if the component requires
        you to set some property, this method will throw an exception if
        you haven't set it.  This method throws a not-yet-implemented
        NXException for some components.
        
        Signature ``Validate()`` 
        
        :returns:  Was self validation successful  
        :rtype: bool 
        
        .. versionadded:: NX3.0.1
        
        License requirements: None.
        """
        ...
    
    DirectionOption: VelocityImpactDirectionDirectionType = ...
    """
    Returns or sets  the direction option 
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactDirectionDirectionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionOption`` 
    
    :param mDirectionOption: 
    :type mDirectionOption: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactDirectionDirectionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    NodalComponent: VelocityImpactDirectionNodalComponentType = ...
    """
    Returns or sets  the selected nodal component 
    
    <hr>
    
    Getter Method
    
    Signature ``NodalComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactDirectionNodalComponentType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NodalComponent`` 
    
    :param nodalComponent: 
    :type nodalComponent: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactDirectionNodalComponentType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ReverseDirection: bool = ...
    """
    Returns or sets  the option to reverse direction of nodal component or not.  
    
    Only valid when direction option is
    :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactDirectionDirectionType.NodalComponent <NXOpen.CAE.ResponseSimulation.VelocityImpactDirectionDirectionType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseDirection`` 
    
    :param reverseDirection: 
    :type reverseDirection: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    UserDefinedDirection: NXOpen.Direction = ...
    """
    Returns or sets  the user-defined direction
    
    <hr>
    
    Getter Method
    
    Signature ``UserDefinedDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UserDefinedDirection`` 
    
    :param userDefinedDirection: 
    :type userDefinedDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: VelocityImpactDirection = ...  # unknown typename


class BaseBuilder(NXOpen.Builder):
    """
    Represents the abstract builder class for all objects defined in response analysis meta solution   
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    ObjectLabel: ObjectLabel = ...
    """
    Returns  the object label 
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ObjectLabel` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: BaseBuilder = ...  # unknown typename


class RSEventBuilder(BaseBuilder):
    """
    Represents the manager of CAE.  
    
    ResponseSimulation.RSEvent. 
    The object of type :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` can be 
    created or deleted only through this class. 
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.RSEventCollection.CreateEventBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Attributes: RSEventAttributes = ...
    """
    Returns  the attributes setting 
    
    <hr>
    
    Getter Method
    
    Signature ``Attributes`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventAttributes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    EventType: RSEventType = ...
    """
    Returns or sets  the event type 
    
    <hr>
    
    Getter Method
    
    Signature ``EventType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``EventType`` 
    
    :param eventType: 
    :type eventType: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    InitialConditions: InitialConditions = ...
    """
    Returns  the initial condition setting.  
    
    Only available when event type is 
    :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Transient <NXOpen.CAE.ResponseSimulation.RSEventType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``InitialConditions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.InitialConditions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    OutputSetting: RSEventOutputSetting = ...
    """
    Returns  the output setting 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputSetting`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventOutputSetting` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseSimulationSolution: Solution = ...
    """
    Returns  the parent response simulation solution 
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseSimulationSolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.Solution` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: RSEventBuilder = ...  # unknown typename


class CombinationEvaluationOptionsEvaluationMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CombinationEvaluationOptionsEvaluationMethod():
    """
    Specifies the calculation method of combination evaluation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Abs", " - "
       "Srss", " - "
       "Nrl", " - "
       "Cqc", " - "
       "NqcDoubleSum", " - "
    """
    Abs = 0  # CombinationEvaluationOptionsEvaluationMethodMemberType
    Srss = 1  # CombinationEvaluationOptionsEvaluationMethodMemberType
    Nrl = 2  # CombinationEvaluationOptionsEvaluationMethodMemberType
    Cqc = 3  # CombinationEvaluationOptionsEvaluationMethodMemberType
    NqcDoubleSum = 4  # CombinationEvaluationOptionsEvaluationMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CombinationEvaluationOptionsMultipleExcitationCombinationMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CombinationEvaluationOptionsMultipleExcitationCombinationMethod():
    """
    Specifies combination method for multiple excitation combination 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Abs", " - "
       "Srs", " - "
    """
    Abs = 0  # CombinationEvaluationOptionsMultipleExcitationCombinationMethodMemberType
    Srs = 1  # CombinationEvaluationOptionsMultipleExcitationCombinationMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CombinationEvaluationOptions(NXOpen.TaggedObject):
    """
    Represents the setting for combination evaluation.  
    
    .. versionadded:: NX5.0.0
    """
    
    class EvaluationMethod():
        """
        Specifies the calculation method of combination evaluation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Abs", " - "
           "Srss", " - "
           "Nrl", " - "
           "Cqc", " - "
           "NqcDoubleSum", " - "
        """
        Abs = 0  # CombinationEvaluationOptionsEvaluationMethodMemberType
        Srss = 1  # CombinationEvaluationOptionsEvaluationMethodMemberType
        Nrl = 2  # CombinationEvaluationOptionsEvaluationMethodMemberType
        Cqc = 3  # CombinationEvaluationOptionsEvaluationMethodMemberType
        NqcDoubleSum = 4  # CombinationEvaluationOptionsEvaluationMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class MultipleExcitationCombinationMethod():
        """
        Specifies combination method for multiple excitation combination 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Abs", " - "
           "Srs", " - "
        """
        Abs = 0  # CombinationEvaluationOptionsMultipleExcitationCombinationMethodMemberType
        Srs = 1  # CombinationEvaluationOptionsMultipleExcitationCombinationMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    CombinationMethod: CombinationEvaluationOptionsMultipleExcitationCombinationMethod = ...
    """
    Returns or sets  the combination method for multiple excitation combination 
    
    <hr>
    
    Getter Method
    
    Signature ``CombinationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptionsMultipleExcitationCombinationMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``CombinationMethod`` 
    
    :param combinationMethod: 
    :type combinationMethod: :py:class:`NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptionsMultipleExcitationCombinationMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    EvaluationMethodOption: CombinationEvaluationOptionsEvaluationMethod = ...
    """
    Returns or sets  the calculation method 
    
    <hr>
    
    Getter Method
    
    Signature ``EvaluationMethodOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptionsEvaluationMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``EvaluationMethodOption`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptionsEvaluationMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    NeighboringFactor: float = ...
    """
    Returns or sets  the neighboring factor.  
    
    Must be specified when calculation method is 
    :py:class:` CAE.ResponseSimulation.CombinationEvaluationOptionsEvaluationMethod.Nrl < CAE.ResponseSimulation.CombinationEvaluationOptionsEvaluationMethod>` 
    
    <hr>
    
    Getter Method
    
    Signature ``NeighboringFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``NeighboringFactor`` 
    
    :param neighboringFactor: 
    :type neighboringFactor: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    TimeDuration: float = ...
    """
    Returns or sets  the time duration in second.  
    
    Must be specified when calculation method is 
    :py:class:`CAE.ResponseSimulation.CombinationEvaluationOptionsEvaluationMethod.NqcDoubleSum <CAE.ResponseSimulation.CombinationEvaluationOptionsEvaluationMethod>` 
    
    <hr>
    
    Getter Method
    
    Signature ``TimeDuration`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``TimeDuration`` 
    
    :param timeDuration: 
    :type timeDuration: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: CombinationEvaluationOptions = ...  # unknown typename


class SensorTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SensorType():
    """
    Specifies the type of Sensor 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Component", " - "
       "Direction", " - "
       "Normal", " - "
    """
    Component = 0  # SensorTypeMemberType
    Direction = 1  # SensorTypeMemberType
    Normal = 2  # SensorTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DynamicResultEvaluationSettingBuilder(NXOpen.Builder):
    """
    Represents the abstract builder class of evaluation setting for all dynamic results evaluations.  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    
    def GetDescriptionString(self) -> 'list[str]':
        """
        Returns the description.  
        
        Signature ``GetDescriptionString()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetDescriptionString(self, description: 'list[str]') -> None:
        """
        Sets the description 
        
        Signature ``SetDescriptionString(description)`` 
        
        :param description: 
        :type description: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    Null: DynamicResultEvaluationSettingBuilder = ...  # unknown typename


class PrlResultsEvaluationSettingBuilder(DynamicResultEvaluationSettingBuilder):
    """
    Represents the abstract builder class of evaluation setting for peak value, RMS results
    and LCR results.  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    
    def GetOutputNodes(self) -> 'list[NXOpen.CAE.FENode]':
        """
        Returns the destination nodes.  
        
        Only available when result type is 
        :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.Displacement <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`,
        :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.Acceleration <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`,
        :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.ElementForce <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`
        
        Signature ``GetOutputNodes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetOutputNodes(self, destinationNodes: 'list[NXOpen.CAE.FENode]') -> None:
        """
        Sets the destination nodes 
        
        Signature ``SetOutputNodes(destinationNodes)`` 
        
        :param destinationNodes: 
        :type destinationNodes: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetOutputElements(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Returns the destination elements.  
        
        Only available when the result type is 
        :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.Stress <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`,
        :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.ShellResultant <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`
        
        Signature ``GetOutputElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetOutputElements(self, destinationElements: 'list[NXOpen.CAE.FEElement]') -> None:
        """
        Sets the destination elements 
        
        Signature ``SetOutputElements(destinationElements)`` 
        
        :param destinationElements: 
        :type destinationElements: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetDataComponents(self) -> 'list[DirectionDataComponent]':
        """
        Returns the direction data components.  
        
        The condidate choices will be changed according to 
        :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType` setting
        
        Signature ``GetDataComponents()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetDataComponents(self, dataComponent: 'list[DirectionDataComponent]') -> None:
        """
        Sets the direction data components.  
        
        The condidate choices will be changed according to 
        :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType` setting
        
        Signature ``SetDataComponents(dataComponent)`` 
        
        :param dataComponent: 
        :type dataComponent: list of :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    CoordinateSystem: CoordinateSystem = ...
    """
    Returns or sets  the coordinate system.  
    
    Only available when the result type is 
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.Stress <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`,
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.ShellResultant <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``CoordinateSystem`` 
    
    :param coordinateSystem: 
    :type coordinateSystem: :py:class:`NXOpen.CAE.ResponseSimulation.CoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ObservationNode: NXOpen.CAE.FENode = ...
    """
    Returns or sets  the relative node.  
    
    Only available when result type is 
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.Displacement <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`,
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.Acceleration <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`,
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.ElementForce <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`
    
    <hr>
    
    Getter Method
    
    Signature ``ObservationNode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ObservationNode`` 
    
    :param relativeNode: 
    :type relativeNode: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Relative: bool = ...
    """
    Returns or sets  the option of using the observation node in evaluation
    
    <hr>
    
    Getter Method
    
    Signature ``Relative`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Relative`` 
    
    :param relative: 
    :type relative: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResultType: EvaluationResultType = ...
    """
    Returns or sets  the result type 
    
    <hr>
    
    Getter Method
    
    Signature ``ResultType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResultType`` 
    
    :param resultType: 
    :type resultType: :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: PrlResultsEvaluationSettingBuilder = ...  # unknown typename


class PeakValueEvaluationSettingBuilder(PrlResultsEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSetting` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreatePeakValueEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    CombinationOptions: CombinationEvaluationOptions = ...
    """
    Returns  the setting of combination evaluation.  
    
    Only available when event type is
    :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Random <NXOpen.CAE.ResponseSimulation.RSEventType>` or
    :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.ResponseSpectrum <NXOpen.CAE.ResponseSimulation.RSEventType>`
    
    <hr>
    
    Getter Method
    
    Signature ``CombinationOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: PeakValueEvaluationSettingBuilder = ...  # unknown typename


class StrainGagePlacementTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StrainGagePlacementType():
    """
    Specifies the placement type of Strain Gage 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Node", " - "
       "ElementFaceCenter", " - "
    """
    Node = 0  # StrainGagePlacementTypeMemberType
    ElementFaceCenter = 1  # StrainGagePlacementTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NodalFunctionEvalBeamLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodalFunctionEvalBeamLocation():
    """
    Specifies beam element evaluation locations for nodal function evaluation 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "C", "Stress Recovery point C on a beam cross section"
       "D", "Stress Recovery point D on a beam cross section"
       "E", "Stress Recovery point E on a beam cross section"
       "F", "Stress Recovery point F on a beam cross section"
       "All", "All four Stress Recovery points on a beam cross section"
    """
    C = 0  # NodalFunctionEvalBeamLocationMemberType
    D = 1  # NodalFunctionEvalBeamLocationMemberType
    E = 2  # NodalFunctionEvalBeamLocationMemberType
    F = 3  # NodalFunctionEvalBeamLocationMemberType
    All = 4  # NodalFunctionEvalBeamLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StaticLoadExcitation(Excitation):
    """
    Represents an excitation of static load type   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.StaticLoadExcitationBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: StaticLoadExcitation = ...  # unknown typename


class ExcitationLocationDefinition(NXOpen.TaggedObject):
    """
    Represents the manager to :py:class:`CAE.ResponseSimulation.DistributedLoadExcitation`.  
    
    The object of type :py:class:`CAE.ResponseSimulation.DistributedLoadExcitation`
    can only be created or edited through this class.
    
    .. versionadded:: NX5.0.0
    """
    ExcitationLocation: NXOpen.SelectObject = ...
    """
    Returns  the excitation location on which the excitation will be applied.  
    
    The excitation location
    type could be force location, enforced motion location or dynamic load defined in response 
    dynamic solution 
    
    <hr>
    
    Getter Method
    
    Signature ``ExcitationLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectObject` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ExcitationLocationId: int = ...
    """
    Returns or sets  the ID of excitation location on which the excitation will be applied.  
    
    The excitation location ID
    could be node label or load set label 
    
    <hr>
    
    Getter Method
    
    Signature ``ExcitationLocationId`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ExcitationLocationId`` 
    
    :param excitaitonLocationId: 
    :type excitaitonLocationId: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ExcitationLocationType: ExcitationBuilderExcitationLocationType = ...
    """
    Returns or sets  the type of excitaion location 
    
    <hr>
    
    Getter Method
    
    Signature ``ExcitationLocationType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationBuilderExcitationLocationType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ExcitationLocationType`` 
    
    :param excitationLocationType: 
    :type excitationLocationType: :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationBuilderExcitationLocationType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: ExcitationLocationDefinition = ...  # unknown typename


class DDAMExcitationShipTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DDAMExcitationShipType():
    """
    Specifies the ship type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Surface", " - "
       "Submarine", " - "
    """
    Surface = 0  # DDAMExcitationShipTypeMemberType
    Submarine = 1  # DDAMExcitationShipTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DDAMExcitationMountingTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DDAMExcitationMountingType():
    """
    Specifies the mounting type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Hull", " - "
       "Duck", " - "
       "ShellPlating", " - "
    """
    Hull = 0  # DDAMExcitationMountingTypeMemberType
    Duck = 1  # DDAMExcitationMountingTypeMemberType
    ShellPlating = 2  # DDAMExcitationMountingTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DDAMExcitationResponseTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DDAMExcitationResponseType():
    """
    Specifies the response type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Elastic", " - "
       "ElasticPlastic", " - "
    """
    Elastic = 0  # DDAMExcitationResponseTypeMemberType
    ElasticPlastic = 1  # DDAMExcitationResponseTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DDAMExcitationLoadingTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DDAMExcitationLoadingType():
    """
    Specifies the loading type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Vertical", " - "
       "Athwartship", " - "
       "ForeAndAft", " - "
    """
    Vertical = 0  # DDAMExcitationLoadingTypeMemberType
    Athwartship = 1  # DDAMExcitationLoadingTypeMemberType
    ForeAndAft = 2  # DDAMExcitationLoadingTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DDAMExcitationCoefficientDefinitionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DDAMExcitationCoefficientDefinitionType():
    """
    the choices of define DDAM coefficients. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ByFile", "Get the DDAM coefficients from a DDAM coefficient file"
       "InputManually", "Input the DDAM coefficient manually"
    """
    ByFile = 0  # DDAMExcitationCoefficientDefinitionTypeMemberType
    InputManually = 1  # DDAMExcitationCoefficientDefinitionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DDAMExcitation(Excitation):
    """
    Represents an DDAM excitation.  
    
    DDAM excitation could only be used by DDAM event. 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class ShipType():
        """
        Specifies the ship type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Surface", " - "
           "Submarine", " - "
        """
        Surface = 0  # DDAMExcitationShipTypeMemberType
        Submarine = 1  # DDAMExcitationShipTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class MountingType():
        """
        Specifies the mounting type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Hull", " - "
           "Duck", " - "
           "ShellPlating", " - "
        """
        Hull = 0  # DDAMExcitationMountingTypeMemberType
        Duck = 1  # DDAMExcitationMountingTypeMemberType
        ShellPlating = 2  # DDAMExcitationMountingTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ResponseType():
        """
        Specifies the response type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Elastic", " - "
           "ElasticPlastic", " - "
        """
        Elastic = 0  # DDAMExcitationResponseTypeMemberType
        ElasticPlastic = 1  # DDAMExcitationResponseTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LoadingType():
        """
        Specifies the loading type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Vertical", " - "
           "Athwartship", " - "
           "ForeAndAft", " - "
        """
        Vertical = 0  # DDAMExcitationLoadingTypeMemberType
        Athwartship = 1  # DDAMExcitationLoadingTypeMemberType
        ForeAndAft = 2  # DDAMExcitationLoadingTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CoefficientDefinitionType():
        """
        the choices of define DDAM coefficients. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ByFile", "Get the DDAM coefficients from a DDAM coefficient file"
           "InputManually", "Input the DDAM coefficient manually"
        """
        ByFile = 0  # DDAMExcitationCoefficientDefinitionTypeMemberType
        InputManually = 1  # DDAMExcitationCoefficientDefinitionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Null: DDAMExcitation = ...  # unknown typename


class TranslationalDDAMExcitation(DDAMExcitation):
    """
    Represents an DDAM excitation.  
    
    DDAM excitation could only be used by DDAM event. 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.TranslationalDDAMExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: TranslationalDDAMExcitation = ...  # unknown typename


class StrainGageResultMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StrainGageResult():
    """
    Specifies the result type of Strain Gage 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Strain", " - "
       "Stress", " - "
    """
    Strain = 0  # StrainGageResultMemberType
    Stress = 1  # StrainGageResultMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StrainGageCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of response analysis strain gage   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.ResponseSimulation.Manager`
    
    .. versionadded:: NX6.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateStrainGageBuilder(self, strainGage: StrainGage) -> StrainGageBuilder:
        """
        Creates a strain gage buider  
        
        Signature ``CreateStrainGageBuilder(strainGage)`` 
        
        :param strainGage: 
        :type strainGage: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGage` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def FindObject(self, name: str) -> StrainGage:
        """
        Finds an strain gage with specified gage name  
        
        Signature ``FindObject(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGage` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    


class RotationalDDAMExcitation(DDAMExcitation):
    """
    Represents an DDAM excitation.  
    
    DDAM excitation could only be used by DDAM event. 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.RotationalDDAMExcitationBuilder`
    """
    Null: RotationalDDAMExcitation = ...  # unknown typename


class NodalFunctionEvalShellLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodalFunctionEvalShellLocation():
    """
    Specifies shell element evaluation locations for nodal function evaluation 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Top", "Top layer"
       "Middle", "Middle layer"
       "Bottom", "Bottom layer"
       "All", "All three layers"
    """
    Top = 0  # NodalFunctionEvalShellLocationMemberType
    Middle = 1  # NodalFunctionEvalShellLocationMemberType
    Bottom = 2  # NodalFunctionEvalShellLocationMemberType
    All = 3  # NodalFunctionEvalShellLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EvaluationSetting(NXOpen.NXObject):
    """
    Represents the abstract class of all evaluation setting classes.  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    
    def Destroy(self) -> None:
        """
        Destroies the evaluation setting object after evaluation.  
        
        Signature ``Destroy()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    Null: EvaluationSetting = ...  # unknown typename


class DynamicResultEvaluationSetting(EvaluationSetting):
    """
    Represents the abstract class of evaluation setting for all dynamic results evaluations.  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    Null: DynamicResultEvaluationSetting = ...  # unknown typename


class PrlResultsEvaluationSetting(DynamicResultEvaluationSetting):
    """
    Represents the abstract class of evaluation setting for peak value, RMS results
    and LCR results.  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    Null: PrlResultsEvaluationSetting = ...  # unknown typename


class RmsResultsEvaluationSetting(PrlResultsEvaluationSetting):
    """
    Represents the parameters setting for RMS results evaluation in response analysis.  
    
    Only
    available when event type is :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Random <NXOpen.CAE.ResponseSimulation.RSEventType>` 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: RmsResultsEvaluationSetting = ...  # unknown typename


class Solution(NXOpen.NXObject):
    """
    Represents a meta solution providing response analysis functionalities in the .  
    
    sim file  
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.SolutionBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def GetSolutionName(self) -> str:
        """
        Returns the response simulation solution name  
        
        Signature ``GetSolutionName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetSolutionName(self, solutionName: str, renameResultFile: bool) -> None:
        """
        Sets the response simulation solution name 
        
        Signature ``SetSolutionName(solutionName, renameResultFile)`` 
        
        :param solutionName: 
        :type solutionName: str 
        :param renameResultFile:  if there are result files associated with the solution, rename the files or not 
        :type renameResultFile: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def Destroy(self, deleteResultFile: bool) -> None:
        """
        Deletes a response simulation solution, including all events and excitations
        under it 
        
        Signature ``Destroy(deleteResultFile)`` 
        
        :param deleteResultFile:  delete the result files associated with the solution or not  
        :type deleteResultFile: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetModalProperties(self) -> ModalProperties:
        """
        Returns the modal properties of Response Analysis Meta solution 
        
        Signature ``GetModalProperties()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ModalProperties` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetEvaluationParameters(self) -> EvaluationParameters:
        """
        Returns the evaluation parameters of Response Analysis Meta solution 
        
        Signature ``GetEvaluationParameters()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationParameters` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetEvents(self) -> 'list[RSEvent]':
        """
        Returns all the events of the solution 
        
        Signature ``GetEvents()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def ImportEvent(self, eventDefinitionFile: str, suggestedName: str) -> RSEvent:
        """
        Imports an event to the solution  
        
        Signature ``ImportEvent(eventDefinitionFile, suggestedName)`` 
        
        :param eventDefinitionFile: 
        :type eventDefinitionFile: str 
        :param suggestedName: 
        :type suggestedName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CloneEvent(self, sourceEvent: RSEvent, suggestedName: str) -> RSEvent:
        """
        Clones an event to the solution  
        
        Signature ``CloneEvent(sourceEvent, suggestedName)`` 
        
        :param sourceEvent: 
        :type sourceEvent: :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` 
        :param suggestedName: 
        :type suggestedName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetResultFileName(self) -> str:
        """
        Returns the result file name of solution  
        
        Signature ``GetResultFileName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateFrf(self, evaluationSetting: FrfEvaluationSetting) -> None:
        """
        Performs evaluation for FRF.  
        
        The evaluation results will be stored in an AFU file,
        which name could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.Solution.GetResultFileName` 
        
        Signature ``EvaluateFrf(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.FrfEvaluationSetting` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateTransmissibility(self, evaluationSetting: TransmissibilityEvaluationSetting) -> None:
        """
        Performs evaluation for transimissibility.  
        
        The evaluation results will be stored in an AFU file,
        which name could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.Solution.GetResultFileName` 
        
        Signature ``EvaluateTransmissibility(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSetting` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CloneSensor(self, sourceSensor: Sensor, suggestedName: str) -> Sensor:
        """
        Clones a sensor to the solution  
        
        Signature ``CloneSensor(sourceSensor, suggestedName)`` 
        
        :param sourceSensor: 
        :type sourceSensor: :py:class:`NXOpen.CAE.ResponseSimulation.Sensor` 
        :param suggestedName: 
        :type suggestedName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.Sensor` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CloneStrainGage(self, sourceGage: StrainGage, suggestedName: str) -> StrainGage:
        """
        Clones a strain gage to the solution  
        
        Signature ``CloneStrainGage(sourceGage, suggestedName)`` 
        
        :param sourceGage: 
        :type sourceGage: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGage` 
        :param suggestedName: 
        :type suggestedName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGage` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CheckObsoleteStatus(self) -> None:
        """
        Checks status and updates solution properties for the solution which became obsolete because
        referenced modal shape file was changed.  
        
        The solution will be reactivated as normal state after status checking. 
        
        Signature ``CheckObsoleteStatus()`` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    ActiveEvent: RSEvent = ...
    """
    Returns or sets  the active event 
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveEvent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveEvent`` 
    
    :param activeEvent: 
    :type activeEvent: :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: Solution = ...  # unknown typename


class SensorCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of response analysis sensor   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.ResponseSimulation.Manager`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateSensorBuilder(self, rsSensor: Sensor) -> SensorBuilder:
        """
        Creates a sensor buider  
        
        Signature ``CreateSensorBuilder(rsSensor)`` 
        
        :param rsSensor: 
        :type rsSensor: :py:class:`NXOpen.CAE.ResponseSimulation.Sensor` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.SensorBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def DeleteSensor(self, rsSensor: Sensor) -> None:
        """
        Deletes an sensor 
        
        Signature ``DeleteSensor(rsSensor)`` 
        
        :param rsSensor: 
        :type rsSensor: :py:class:`NXOpen.CAE.ResponseSimulation.Sensor` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def FindObject(self, name: str) -> Sensor:
        """
        Finds an sensor with specified event name  
        
        Signature ``FindObject(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.Sensor` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    


class SensorCoordinateTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SensorCoordinateType():
    """
    Specifies the coordinate type of Sensor 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NodalCs", " - "
       "GlobalCs", " - "
    """
    NodalCs = 0  # SensorCoordinateTypeMemberType
    GlobalCs = 1  # SensorCoordinateTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FunctionEvaluationSettingBuilder(NXOpen.Builder):
    """
    Represents the abstract builder class of evaluation setting for function response evaluation
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    OutputSettings: FunctionEvaluationOutputSettings = ...
    """
    Returns  the output setting.  
    
    <hr>
    
    Getter Method
    
    Signature ``OutputSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FunctionEvaluationOutputSettings` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResultType: EvaluationResultType = ...
    """
    Returns or sets  the result type 
    
    <hr>
    
    Getter Method
    
    Signature ``ResultType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResultType`` 
    
    :param resultType: 
    :type resultType: :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: FunctionEvaluationSettingBuilder = ...  # unknown typename


class FunctionEvaluationOutputSettings(NXOpen.TaggedObject):
    """
    Represents the output setting for function response evaluation  
    
    .. versionadded:: NX5.0.0
    """
    RecordPrefix: str = ...
    """
    Returns or sets  the prefix of evaluation results record name 
    
    <hr>
    
    Getter Method
    
    Signature ``RecordPrefix`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``RecordPrefix`` 
    
    :param recordPrefix: 
    :type recordPrefix: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ShowPlot: bool = ...
    """
    Returns or sets  the option of show plot.  
    
    If true, the evaluation results will be displayed on screen 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowPlot`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowPlot`` 
    
    :param showPlot: 
    :type showPlot: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    StoreOption: bool = ...
    """
    Returns or sets  the store option.  
    
    If true, the evaluation results will be stored on disk 
    
    <hr>
    
    Getter Method
    
    Signature ``StoreOption`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``StoreOption`` 
    
    :param storeOption: 
    :type storeOption: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: FunctionEvaluationOutputSettings = ...  # unknown typename


class FunctionEvaluationSetting(EvaluationSetting):
    """
    Represents the abstract class of evaluation setting for function response evaluation
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    Null: FunctionEvaluationSetting = ...  # unknown typename


class ElementalFunctionEvaluationSetting(FunctionEvaluationSetting):
    """
    Represents the parameters setting for elemental function evaluation.  
    
    Only available to
    :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Transient <NXOpen.CAE.ResponseSimulation.RSEventType>`,
    :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Frequency <NXOpen.CAE.ResponseSimulation.RSEventType>`,
    :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Random <NXOpen.CAE.ResponseSimulation.RSEventType>`
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: ElementalFunctionEvaluationSetting = ...  # unknown typename


class ModalResultsEvaluationSetting(FunctionEvaluationSetting):
    """
    Represents the abstract class of evaluation setting for FRF and transmissibility   
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    Null: ModalResultsEvaluationSetting = ...  # unknown typename


class ObjectLabel(NXOpen.TaggedObject):
    """
    Represents the setting to label an object.  
    
    Includes name and description 
    
    .. versionadded:: NX5.0.0
    """
    
    def GetDescriptions(self) -> 'list[str]':
        """
        Returns the description for the object  
        
        Signature ``GetDescriptions()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetDescriptions(self, description: 'list[str]') -> None:
        """
        Sets the description for the object 
        
        Signature ``SetDescriptions(description)`` 
        
        :param description: 
        :type description: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    Name: str = ...
    """
    Returns or sets  the object name 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: ObjectLabel = ...  # unknown typename


class VelocityImpactExcitation(Excitation):
    """
    Represents a velocity impact excitation   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: VelocityImpactExcitation = ...  # unknown typename


class NodalFunctionEvalRequestMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodalFunctionEvalRequest():
    """
    Specifies response request for nodal function evaluation 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UserDefinedDirection", " - "
       "DataComponent", " - "
    """
    UserDefinedDirection = 0  # NodalFunctionEvalRequestMemberType
    DataComponent = 1  # NodalFunctionEvalRequestMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SolutionAttributes(NXOpen.TaggedObject):
    """
    Represents attributes setting of response analysis meta solution   
    
    .. versionadded:: NX6.0.0
    """
    RigidBodyToleranceExp: NXOpen.Expression = ...
    """
    Returns  the tolerance expression 
    
    <hr>
    
    Getter Method
    
    Signature ``RigidBodyToleranceExp`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: SolutionAttributes = ...  # unknown typename


class RSEventSolverParametersDdamCoefficientTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RSEventSolverParametersDdamCoefficientType():
    """
    Represents DDAM coefficient type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Af", " - "
       "Vf", " - "
       "Aa", " - "
       "Ab", " - "
       "Ac", " - "
       "Ad", " - "
       "Va", " - "
       "Vb", " - "
       "Vc", " - "
    """
    Af = 0  # RSEventSolverParametersDdamCoefficientTypeMemberType
    Vf = 1  # RSEventSolverParametersDdamCoefficientTypeMemberType
    Aa = 2  # RSEventSolverParametersDdamCoefficientTypeMemberType
    Ab = 3  # RSEventSolverParametersDdamCoefficientTypeMemberType
    Ac = 4  # RSEventSolverParametersDdamCoefficientTypeMemberType
    Ad = 5  # RSEventSolverParametersDdamCoefficientTypeMemberType
    Va = 6  # RSEventSolverParametersDdamCoefficientTypeMemberType
    Vb = 7  # RSEventSolverParametersDdamCoefficientTypeMemberType
    Vc = 8  # RSEventSolverParametersDdamCoefficientTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RSEventSolverParameters(NXOpen.TaggedObject):
    """
    Represents a response analysis event   
    
    .. versionadded:: NX5.0.0
    """
    
    class DdamCoefficientType():
        """
        Represents DDAM coefficient type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Af", " - "
           "Vf", " - "
           "Aa", " - "
           "Ab", " - "
           "Ac", " - "
           "Ad", " - "
           "Va", " - "
           "Vb", " - "
           "Vc", " - "
        """
        Af = 0  # RSEventSolverParametersDdamCoefficientTypeMemberType
        Vf = 1  # RSEventSolverParametersDdamCoefficientTypeMemberType
        Aa = 2  # RSEventSolverParametersDdamCoefficientTypeMemberType
        Ab = 3  # RSEventSolverParametersDdamCoefficientTypeMemberType
        Ac = 4  # RSEventSolverParametersDdamCoefficientTypeMemberType
        Ad = 5  # RSEventSolverParametersDdamCoefficientTypeMemberType
        Va = 6  # RSEventSolverParametersDdamCoefficientTypeMemberType
        Vb = 7  # RSEventSolverParametersDdamCoefficientTypeMemberType
        Vc = 8  # RSEventSolverParametersDdamCoefficientTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetDdamCoefficient(self, coefficientType: RSEventSolverParametersDdamCoefficientType) -> float:
        """
        Returns DDAM coefficient value of the specified type  
        
        Signature ``GetDdamCoefficient(coefficientType)`` 
        
        :param coefficientType: 
        :type coefficientType: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventSolverParametersDdamCoefficientType` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def SetDdamCoefficient(self, coefficientType: RSEventSolverParametersDdamCoefficientType, coefficient: float) -> None:
        """
        Sets the DDAM coefficient value of the specified type 
        
        Signature ``SetDdamCoefficient(coefficientType, coefficient)`` 
        
        :param coefficientType: 
        :type coefficientType: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventSolverParametersDdamCoefficientType` 
        :param coefficient: 
        :type coefficient: float 
        
        .. versionadded:: NX7.5.2
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    DdamCoefficientA: float = ...
    """
    Returns or sets  the DDAM A coefficient 
    
    <hr>
    
    Getter Method
    
    Signature ``DdamCoefficientA`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``DdamCoefficientA`` 
    
    :param coefficientA: 
    :type coefficientA: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    DdamCoefficientV: float = ...
    """
    Returns or sets  the DDAM V coefficient 
    
    <hr>
    
    Getter Method
    
    Signature ``DdamCoefficientV`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``DdamCoefficientV`` 
    
    :param coefficientV: 
    :type coefficientV: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: RSEventSolverParameters = ...  # unknown typename


class RmsLcrEvaluationMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RmsLcrEvaluationMethod():
    """
    Specifies the evaluation method for RMS or LCR calculation 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SmallNumberItems", "Small number of evaluation items"
       "LargeNumberItems", "Large number of evaluation items"
       "AutomaticSelection", "Automatic selection"
    """
    SmallNumberItems = 0  # RmsLcrEvaluationMethodMemberType
    LargeNumberItems = 1  # RmsLcrEvaluationMethodMemberType
    AutomaticSelection = 2  # RmsLcrEvaluationMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StrengthStressCriteriaMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StrengthStressCriteria():
    """
    Specifies strength stress criteria 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "VonMises", " - "
       "MaxPrinciple", " - "
       "MinPrinciple", " - "
    """
    VonMises = 0  # StrengthStressCriteriaMemberType
    MaxPrinciple = 1  # StrengthStressCriteriaMemberType
    MinPrinciple = 2  # StrengthStressCriteriaMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ShellElementEvaluationLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ShellElementEvaluationLocation():
    """
    Specifies shell element evaluation locations 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Top", " - "
       "Middle", " - "
       "Bottom", " - "
    """
    Top = 0  # ShellElementEvaluationLocationMemberType
    Middle = 1  # ShellElementEvaluationLocationMemberType
    Bottom = 2  # ShellElementEvaluationLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RmsResultsEvaluationSettingBuilder(PrlResultsEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSetting` can be
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateRmsResultsEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    EvaluationMethod: RmsLcrEvaluationMethod = ...
    """
    Returns or sets  the evaluation method for RMS 
    
    <hr>
    
    Getter Method
    
    Signature ``EvaluationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RmsLcrEvaluationMethod` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``EvaluationMethod`` 
    
    :param evaluationMethod: 
    :type evaluationMethod: :py:class:`NXOpen.CAE.ResponseSimulation.RmsLcrEvaluationMethod` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    UserDefinedDirection: NXOpen.Direction = ...
    """
    Returns or sets   the user defined direction 
    
    <hr>
    
    Getter Method
    
    Signature ``UserDefinedDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX8.5.0
       This method is not used any more and there is no replacement for it.
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``UserDefinedDirection`` 
    
    :param userDefinedDirection: 
    :type userDefinedDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX8.5.0
       This method is not used any more and there is no replacement for it.
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    UsingUserDefinedDirection: bool = ...
    """
    Returns or sets  the option of using user defined direction 
    
    <hr>
    
    Getter Method
    
    Signature ``UsingUserDefinedDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX8.5.0
       This method is not used any more and there is no replacement for it.
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``UsingUserDefinedDirection`` 
    
    :param usingUserDefinedDirection: 
    :type usingUserDefinedDirection: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX8.5.0
       This method is not used any more and there is no replacement for it.
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: RmsResultsEvaluationSettingBuilder = ...  # unknown typename


class ModalProperties(NXOpen.NXObject):
    """
    Represents the modal presentation of a response analysis meta solution   
    
    .. versionadded:: NX5.0.0
    """
    
    def GetNormalModeCount(self) -> int:
        """
        Returns the count of normal modes  
        
        Signature ``GetNormalModeCount()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetConstrainModeCount(self) -> int:
        """
        Returns the count of constrain modes  
        
        Signature ``GetConstrainModeCount()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetAttachmentModeCount(self) -> int:
        """
        Returns the count of attachment modes  
        
        Signature ``GetAttachmentModeCount()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetNormalModeById(self, modeId: int) -> NormalMode:
        """
        Returns normal mode with specified node ID  
        
        Signature ``GetNormalModeById(modeId)`` 
        
        :param modeId: 
        :type modeId: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.NormalMode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetNormalModes(self) -> 'list[NormalMode]':
        """
        Returns all normal modes  
        
        Signature ``GetNormalModes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.ResponseSimulation.NormalMode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def Activate(self, activate: bool) -> None:
        """
        Sets activate or deactivate status for all normal modes 
        
        Signature ``Activate(activate)`` 
        
        :param activate: 
        :type activate: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetDampingFactors(self, viscousDamping: float, hystereticDamping: float) -> None:
        """
        Set damping factors for all normal modes 
        
        Signature ``SetDampingFactors(viscousDamping, hystereticDamping)`` 
        
        :param viscousDamping: 
        :type viscousDamping: float 
        :param hystereticDamping: 
        :type hystereticDamping: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetRayleighDamping(self, alphaFactor: float, beltaFactor: float) -> None:
        """
        Set rayleigh's damping for all normal modes 
        
        Signature ``SetRayleighDamping(alphaFactor, beltaFactor)`` 
        
        :param alphaFactor: 
        :type alphaFactor: float 
        :param beltaFactor: 
        :type beltaFactor: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetPhysicalDampingSettings(self) -> PhysicalDampingSettings:
        """
        Returns the physical damping setting object  
        
        Signature ``GetPhysicalDampingSettings()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.PhysicalDampingSettings` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    Null: ModalProperties = ...  # unknown typename


class PeakValueEvaluationSetting(PrlResultsEvaluationSetting):
    """
    Represents the parameters setting of peak value evaluation.  
    
    Only NOT available when
    event type is :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Random <NXOpen.CAE.ResponseSimulation.RSEventType>`. For more information,
    see the Response Dynamics section of the Gateway Help 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: PeakValueEvaluationSetting = ...  # unknown typename


class StrainGageTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StrainGageType():
    """
    Specifies the type of Strain Gage 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UniAxial", " - "
       "BiAxial", " - "
       "Rosette45DegreeIncrement", "Rosette 0-45-90"
       "Rosette60DegreeIncrement", "Rosette 0-60-120"
    """
    UniAxial = 0  # StrainGageTypeMemberType
    BiAxial = 1  # StrainGageTypeMemberType
    Rosette45DegreeIncrement = 2  # StrainGageTypeMemberType
    Rosette60DegreeIncrement = 3  # StrainGageTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ExcitationBuilderExcitationLocationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ExcitationBuilderExcitationLocationType():
    """
    the type of excitation location 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "StaticLoad", " - "
       "DistributedLoad", " - "
       "NodalForce", " - "
       "EnforcedMotion", " - "
    """
    StaticLoad = -2  # ExcitationBuilderExcitationLocationTypeMemberType
    DistributedLoad = -1  # ExcitationBuilderExcitationLocationTypeMemberType
    NodalForce = 0  # ExcitationBuilderExcitationLocationTypeMemberType
    EnforcedMotion = 1  # ExcitationBuilderExcitationLocationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ExcitationBuilder(BaseBuilder):
    """
    Represents the abstract excitation builder class.  
    
    Any of real excitation builder
    must inherit from this class.
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    
    class ExcitationLocationType():
        """
        the type of excitation location 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "StaticLoad", " - "
           "DistributedLoad", " - "
           "NodalForce", " - "
           "EnforcedMotion", " - "
        """
        StaticLoad = -2  # ExcitationBuilderExcitationLocationTypeMemberType
        DistributedLoad = -1  # ExcitationBuilderExcitationLocationTypeMemberType
        NodalForce = 0  # ExcitationBuilderExcitationLocationTypeMemberType
        EnforcedMotion = 1  # ExcitationBuilderExcitationLocationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    DynamicEvent: RSEvent = ...
    """
    Returns  the parent dynamic event object 
    
    <hr>
    
    Getter Method
    
    Signature ``DynamicEvent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ExcitationLocationDefinition: ExcitationLocationDefinition = ...
    """
    Returns  the excitation location definition 
    
    <hr>
    
    Getter Method
    
    Signature ``ExcitationLocationDefinition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationLocationDefinition` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: ExcitationBuilder = ...  # unknown typename


class NodalFunctionExcitationBuilder(ExcitationBuilder):
    """
    Represents the manager to :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionExcitation`.  
    
    The objects of :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionExcitation` 
    can be created or edited on through this class 
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    Null: NodalFunctionExcitationBuilder = ...  # unknown typename


class TranslationalNodalFunctionExcitationBuilderRotationAxisTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TranslationalNodalFunctionExcitationBuilderRotationAxisType():
    """
    Represents the rotation axis type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", " - "
       "Y", " - "
       "Z", " - "
    """
    X = 0  # TranslationalNodalFunctionExcitationBuilderRotationAxisTypeMemberType
    Y = 1  # TranslationalNodalFunctionExcitationBuilderRotationAxisTypeMemberType
    Z = 2  # TranslationalNodalFunctionExcitationBuilderRotationAxisTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TranslationalNodalFunctionExcitationBuilder(NodalFunctionExcitationBuilder):
    """
    Represents the manager to :py:class:`NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitation`.  
    
    The objects of :py:class:`NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitation` 
    can be created or edited on through this class 
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.ExcitationCollection.CreateTranslationalNodalFunctionExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class RotationAxisType():
        """
        Represents the rotation axis type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "X", " - "
           "Y", " - "
           "Z", " - "
        """
        X = 0  # TranslationalNodalFunctionExcitationBuilderRotationAxisTypeMemberType
        Y = 1  # TranslationalNodalFunctionExcitationBuilderRotationAxisTypeMemberType
        Z = 2  # TranslationalNodalFunctionExcitationBuilderRotationAxisTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    EnableUserDefinedDirection: bool = ...
    """
    Returns or sets  the excitation function definition method 
    
    <hr>
    
    Getter Method
    
    Signature ``EnableUserDefinedDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``EnableUserDefinedDirection`` 
    
    :param enableUserDefinedDirection: 
    :type enableUserDefinedDirection: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    EnableUserDefinedRotation: bool = ...
    """
    Returns or sets  the excitation function definition method 
    
    <hr>
    
    Getter Method
    
    Signature ``EnableUserDefinedRotation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``EnableUserDefinedRotation`` 
    
    :param enableUserDefinedRotation: 
    :type enableUserDefinedRotation: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    FunctionComponentX: FunctionComponentData = ...
    """
    Returns  the function component of X direction  
    
    <hr>
    
    Getter Method
    
    Signature ``FunctionComponentX`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FunctionComponentData` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    FunctionComponentY: FunctionComponentData = ...
    """
    Returns  the function component of Y direction 
    
    <hr>
    
    Getter Method
    
    Signature ``FunctionComponentY`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FunctionComponentData` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    FunctionComponentZ: FunctionComponentData = ...
    """
    Returns  the function component of Z direction 
    
    <hr>
    
    Getter Method
    
    Signature ``FunctionComponentZ`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FunctionComponentData` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    RotationAxis: TranslationalNodalFunctionExcitationBuilderRotationAxisType = ...
    """
    Returns or sets  the rotation axis 
    
    <hr>
    
    Getter Method
    
    Signature ``RotationAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilderRotationAxisType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``RotationAxis`` 
    
    :param rotationAxis: 
    :type rotationAxis: :py:class:`NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilderRotationAxisType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    UserDefinedDirection: NXOpen.Direction = ...
    """
    Returns or sets  the magnitude direction 
    
    <hr>
    
    Getter Method
    
    Signature ``UserDefinedDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``UserDefinedDirection`` 
    
    :param magnitudeDirection: 
    :type magnitudeDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    UserDefinedFunction: FunctionComponentData = ...
    """
    Returns  the magnitude function 
    
    <hr>
    
    Getter Method
    
    Signature ``UserDefinedFunction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FunctionComponentData` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: TranslationalNodalFunctionExcitationBuilder = ...  # unknown typename


class SensorBuilder(BaseBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ResponseSimulation.SensorBuilder`
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.SensorCollection.CreateSensorBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def GetSelectedNodes(self) -> 'list[NXOpen.CAE.FENode]':
        """
        Returns the destination nodes  
        
        Signature ``GetSelectedNodes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetSelectedNodes(self, destinationNodes: 'list[NXOpen.CAE.FENode]') -> None:
        """
        Sets the destination nodes 
        
        Signature ``SetSelectedNodes(destinationNodes)`` 
        
        :param destinationNodes: 
        :type destinationNodes: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    ReverseNormalDirection: bool = ...
    """
    Returns or sets  the option for reverse the normal direction.  
    
    Only available when the sensor type is
    :py:class:`CAE.ResponseSimulationSensorType.Normal <CAE.ResponseSimulationSensorType>`  
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseNormalDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseNormalDirection`` 
    
    :param normalDirection: 
    :type normalDirection: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SensorCoordinateType: SensorCoordinateType = ...
    """
    Returns or sets  the sensor's coordinate type 
    
    <hr>
    
    Getter Method
    
    Signature ``SensorCoordinateType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.SensorCoordinateType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SensorCoordinateType`` 
    
    :param coordinateType: 
    :type coordinateType: :py:class:`NXOpen.CAE.ResponseSimulation.SensorCoordinateType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SensorDirectionX: bool = ...
    """
    Returns or sets  the setting for x direction compontent of sensor.  
    
    If true, the response on direction x will be calculated.
    Only available when the sensor type is
    :py:class:`CAE.ResponseSimulationSensorType.Component <CAE.ResponseSimulationSensorType>`  
    
    <hr>
    
    Getter Method
    
    Signature ``SensorDirectionX`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SensorDirectionX`` 
    
    :param directionX: 
    :type directionX: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SensorDirectionY: bool = ...
    """
    Returns or sets  the setting for y direction compontent of sensor.  
    
    If true, the response on direction y will be calculated.
    Only available when the sensor type is
    :py:class:`CAE.ResponseSimulationSensorType.Component <CAE.ResponseSimulationSensorType>`  
    
    <hr>
    
    Getter Method
    
    Signature ``SensorDirectionY`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SensorDirectionY`` 
    
    :param directionY: 
    :type directionY: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SensorDirectionZ: bool = ...
    """
    Returns or sets  the setting for z direction compontent of sensor.  
    
    If true, the response on direction z will be calculated.
    Only available when the sensor type is
    :py:class:`CAE.ResponseSimulationSensorType.Component <CAE.ResponseSimulationSensorType>`  
    
    <hr>
    
    Getter Method
    
    Signature ``SensorDirectionZ`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SensorDirectionZ`` 
    
    :param directionZ: 
    :type directionZ: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SensorResultType: SensorResultType = ...
    """
    Returns or sets  the sensor's result type 
    
    <hr>
    
    Getter Method
    
    Signature ``SensorResultType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.SensorResultType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SensorResultType`` 
    
    :param resultType: 
    :type resultType: :py:class:`NXOpen.CAE.ResponseSimulation.SensorResultType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SensorRotationX: bool = ...
    """
    Returns or sets  the setting for x rotation compontent of sensor.  
    
    If true, the response on rotation x will be calculated.
    Only available when the sensor type is
    :py:class:`CAE.ResponseSimulationSensorType.Component <CAE.ResponseSimulationSensorType>`  
    
    <hr>
    
    Getter Method
    
    Signature ``SensorRotationX`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SensorRotationX`` 
    
    :param rotationX: 
    :type rotationX: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SensorRotationY: bool = ...
    """
    Returns or sets  the setting for y rotation compontent of sensor.  
    
    If true, the response on rotation y will be calculated.
    Only available when the sensor type is
    :py:class:`CAE.ResponseSimulationSensorType.Component <CAE.ResponseSimulationSensorType>`  
    
    <hr>
    
    Getter Method
    
    Signature ``SensorRotationY`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SensorRotationY`` 
    
    :param rotationY: 
    :type rotationY: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SensorRotationZ: bool = ...
    """
    Returns or sets  the setting for z rotation compontent of sensor.  
    
    If true, the response on rotation z will be calculated.
    Only available when the sensor type is
    :py:class:`CAE.ResponseSimulationSensorType.Component <CAE.ResponseSimulationSensorType>`  
    
    <hr>
    
    Getter Method
    
    Signature ``SensorRotationZ`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SensorRotationZ`` 
    
    :param rotationZ: 
    :type rotationZ: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SensorType: SensorType = ...
    """
    Returns or sets  the sensor's type 
    
    <hr>
    
    Getter Method
    
    Signature ``SensorType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.SensorType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SensorType`` 
    
    :param sensorType: 
    :type sensorType: :py:class:`NXOpen.CAE.ResponseSimulation.SensorType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SensorVector: NXOpen.Direction = ...
    """
    Returns or sets  the user defined direction.  
    
    Only available when the sensor type is
    :py:class:`CAE.ResponseSimulationSensorType.Direction <CAE.ResponseSimulationSensorType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``SensorVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SensorVector`` 
    
    :param sensorVector: 
    :type sensorVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: SensorBuilder = ...  # unknown typename


class TransmissibilityEvaluationSetting(ModalResultsEvaluationSetting):
    """
    Represents parameters setting for transmissibility evaluation   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: TransmissibilityEvaluationSetting = ...  # unknown typename


class RotationalNodalFunctionExcitation(NodalFunctionExcitation):
    """
    Represents a rotational nodal function excitation   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: RotationalNodalFunctionExcitation = ...  # unknown typename


class CSDExcitationBuilder(ExcitationBuilder):
    """
    Represents the manager to :py:class:`NXOpen.CAE.ResponseSimulation.CSDExcitation`.  
    
    The object of type :py:class:`NXOpen.CAE.ResponseSimulation.CSDExcitation`
    can only be created or edited through this class.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.ExcitationCollection.CreateCsdExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def GetFromFunction(self) -> tuple:
        """
        Returns the from function  
        
        Signature ``GetFromFunction()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (fromExcitation, componentType). fromExcitation is a :py:class:`NXOpen.CAE.ResponseSimulation.Excitation`. componentType is a :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationComponent`. 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetFromFunction(self, fromExcitation: Excitation, componentType: ExcitationComponent) -> None:
        """
        Sets the from function 
        
        Signature ``SetFromFunction(fromExcitation, componentType)`` 
        
        :param fromExcitation: 
        :type fromExcitation: :py:class:`NXOpen.CAE.ResponseSimulation.Excitation` 
        :param componentType: 
        :type componentType: :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationComponent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetToFunction(self) -> tuple:
        """
        Returns the to function  
        
        Signature ``GetToFunction()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (toExcitation, componentType). toExcitation is a :py:class:`NXOpen.CAE.ResponseSimulation.Excitation`. componentType is a :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationComponent`. 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetToFunction(self, toExcitation: Excitation, componentType: ExcitationComponent) -> None:
        """
        Sets the to function 
        
        Signature ``SetToFunction(toExcitation, componentType)`` 
        
        :param toExcitation: 
        :type toExcitation: :py:class:`NXOpen.CAE.ResponseSimulation.Excitation` 
        :param componentType: 
        :type componentType: :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationComponent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    CorrelationType: CSDExcitationCorrelationType = ...
    """
    Returns or sets  the correlation type 
    
    <hr>
    
    Getter Method
    
    Signature ``CorrelationType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CSDExcitationCorrelationType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``CorrelationType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.CAE.ResponseSimulation.CSDExcitationCorrelationType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    CorrelationValue: float = ...
    """
    Returns or sets  the correlation type 
    
    <hr>
    
    Getter Method
    
    Signature ``CorrelationValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``CorrelationValue`` 
    
    :param correlationValue: 
    :type correlationValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: CSDExcitationBuilder = ...  # unknown typename


class CsdEvaluationSettingBuilder(FunctionEvaluationSettingBuilder):
    """
    Represents the CSD build   
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateCsdEvaluationSettingBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    def GetResponseNodes(self) -> 'list[NXOpen.CAE.FENode]':
        """
        Get the response nodes.  
        
        Available if the result type is 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Displacement <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Velocity <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Acceleration <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.ReactionForce <CAE.ResponseSimulationEvaluationResultType>` 
        
        Signature ``GetResponseNodes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetResponseNodes(self, responseNode: 'list[NXOpen.CAE.FENode]') -> None:
        """
        Set the response nodes.  
        
        Available if the result type is 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Displacement <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Velocity <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Acceleration <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.ReactionForce <CAE.ResponseSimulationEvaluationResultType>` 
        
        Signature ``SetResponseNodes(responseNode)`` 
        
        :param responseNode: 
        :type responseNode: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetResponseElements(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Get the response elments.  
        
        Available if the result type is 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Stress <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Strain <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.ShellStressResultant <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.ElementForce <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.BeamElementForce <CAE.ResponseSimulationEvaluationResultType>` 
        
        Signature ``GetResponseElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetResponseElements(self, responseElements: 'list[NXOpen.CAE.FEElement]') -> None:
        """
        Set the response elments.  
        
        Available if the result type is 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Stress <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Strain <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.ShellStressResultant <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.ElementForce <CAE.ResponseSimulationEvaluationResultType>` 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.BeamElementForce <CAE.ResponseSimulationEvaluationResultType>` 
        
        Signature ``SetResponseElements(responseElements)`` 
        
        :param responseElements: 
        :type responseElements: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    ReferenceCoordinateSystem: CoordinateSystem = ...
    """
    Returns or sets  the coordinate system of reference element.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Stress <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Strain <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ShellStressResultant <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ElementForce <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.BeamElementForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceCoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CoordinateSystem` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceCoordinateSystem`` 
    
    :param referenceCoordinateSystem: 
    :type referenceCoordinateSystem: :py:class:`NXOpen.CAE.ResponseSimulation.CoordinateSystem` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ReferenceDataLocation: DataLocation = ...
    """
    Returns  the reference element location of reference element.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Stress <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Strain <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceDataLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DataLocation` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ReferenceElement: NXOpen.CAE.FEElement = ...
    """
    Returns or sets  the reference element.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Stress <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Strain <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ShellStressResultant <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ElementForce <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.BeamElementForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceElement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.FEElement` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceElement`` 
    
    :param referenceElement: 
    :type referenceElement: :py:class:`NXOpen.CAE.FEElement` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ReferenceElementDataComponent: DirectionDataComponent = ...
    """
    Returns or sets  the direction data component of reference element.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Stress <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Strain <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ShellStressResultant <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ElementForce <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.BeamElementForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceElementDataComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceElementDataComponent`` 
    
    :param referenceElementDataComponent: 
    :type referenceElementDataComponent: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ReferenceNode: NXOpen.CAE.FENode = ...
    """
    Returns or sets  the reference node.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Displacement <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Velocity <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Acceleration <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ReactionForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceNode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceNode`` 
    
    :param referenceNode: 
    :type referenceNode: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ReferenceNodeDataComponent: DirectionDataComponent = ...
    """
    Returns or sets  the direction data component of reference node.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Displacement <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Velocity <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Acceleration <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ReactionForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceNodeDataComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceNodeDataComponent`` 
    
    :param referenceNodeDataComponent: 
    :type referenceNodeDataComponent: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ReferenceUserDefinedDirection: NXOpen.Direction = ...
    """
    Returns or sets   the user defined direction of reference node.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Displacement <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Velocity <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Acceleration <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ReactionForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceUserDefinedDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceUserDefinedDirection`` 
    
    :param referenceUserDefinedDirection: 
    :type referenceUserDefinedDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ReferenceUsingUserDefinedDirection: NodalFunctionEvalRequest = ...
    """
    Returns or sets  the option of using user defined direction of the reference node.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Displacement <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Velocity <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Acceleration <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ReactionForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceUsingUserDefinedDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceUsingUserDefinedDirection`` 
    
    :param referenceUsingUserDefinedDirection: 
    :type referenceUsingUserDefinedDirection: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseCoordinateSystem: CoordinateSystem = ...
    """
    Returns or sets  the coordinate system of response elements.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Stress <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Strain <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ShellStressResultant <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ElementForce <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.BeamElementForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseCoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CoordinateSystem` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResponseCoordinateSystem`` 
    
    :param responseCoordinateSystem: 
    :type responseCoordinateSystem: :py:class:`NXOpen.CAE.ResponseSimulation.CoordinateSystem` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseDataLocation: DataLocation = ...
    """
    Returns  the response element location.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Stress <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Strain <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseDataLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DataLocation` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseElementDataComponent: DirectionDataComponent = ...
    """
    Returns or sets  the direction data component of response elements.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Stress <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Strain <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ShellStressResultant <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ElementForce <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.BeamElementForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseElementDataComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResponseElementDataComponent`` 
    
    :param responseElementDataComponent: 
    :type responseElementDataComponent: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseNodeDataComponent: DirectionDataComponent = ...
    """
    Returns or sets  the direction data component of response node.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Displacement <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Velocity <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Acceleration <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ReactionForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseNodeDataComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResponseNodeDataComponent`` 
    
    :param responseNodeDataComponent: 
    :type responseNodeDataComponent: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseUserDefinedDirection: NXOpen.Direction = ...
    """
    Returns or sets   the user defined direction of response nodes.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Displacement <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Velocity <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Acceleration <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ReactionForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseUserDefinedDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResponseUserDefinedDirection`` 
    
    :param responseUserDefinedDirection: 
    :type responseUserDefinedDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseUsingUserDefinedDirection: NodalFunctionEvalRequest = ...
    """
    Returns or sets  the option of using user defined direction of response nodes.  
    
    Available if the result type is 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Displacement <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Velocity <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.Acceleration <CAE.ResponseSimulationEvaluationResultType>` 
    :py:class:`CAE.ResponseSimulationEvaluationResultType.ReactionForce <CAE.ResponseSimulationEvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseUsingUserDefinedDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResponseUsingUserDefinedDirection`` 
    
    :param responseUsingUserDefinedDirection: 
    :type responseUsingUserDefinedDirection: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: CsdEvaluationSettingBuilder = ...  # unknown typename


class StrengthResultsEvaluationSettingBuilder(DynamicResultEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSetting` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateStrengthResultsEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def GetDestinationElements(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Returns the destination elements  
        
        Signature ``GetDestinationElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetDestinationElements(self, destinationElement: 'list[NXOpen.CAE.FEElement]') -> None:
        """
        Sets the destination elements 
        
        Signature ``SetDestinationElements(destinationElement)`` 
        
        :param destinationElement: 
        :type destinationElement: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    CombinationOptionsBuilder: CombinationEvaluationOptions = ...
    """
    Returns  the setting of combination evaluation 
    
    <hr>
    
    Getter Method
    
    Signature ``CombinationOptionsBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    DataLocation: DataLocation = ...
    """
    Returns  the setting of combination evaluation 
    
    <hr>
    
    Getter Method
    
    Signature ``DataLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DataLocation` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    MaterialDefinitionType: StrengthStressMaterialDefinitionMethod = ...
    """
    Returns or sets  the definition method of material 
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialDefinitionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrengthStressMaterialDefinitionMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialDefinitionType`` 
    
    :param materialProperty: 
    :type materialProperty: :py:class:`NXOpen.CAE.ResponseSimulation.StrengthStressMaterialDefinitionMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    MaterialOverrideOption: bool = ...
    """
    Returns or sets  the choice of override material property or not.  
    
    If false, the material safty factor will be read 
    from destination element selected, else a customized value will be used 
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialOverrideOption`` 
    
    :returns:  NRC_Double_Sum Time Duration 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialOverrideOption`` 
    
    :param overrideMaterialProperty: 
    :type overrideMaterialProperty: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    MaterialSafetyFactor: float = ...
    """
    Returns or sets  the customized material safety factor 
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialSafetyFactor`` 
    
    :returns:  NRC_Double_Sum Time Duration 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialSafetyFactor`` 
    
    :param safetyFactor: 
    :type safetyFactor: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    StandardDeviation: float = ...
    """
    Returns or sets  the customized standard deviation for random event 
    
    <hr>
    
    Getter Method
    
    Signature ``StandardDeviation`` 
    
    :returns:  Random Event Standard Deviation  
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``StandardDeviation`` 
    
    :param standardDeviation: 
    :type standardDeviation: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    StressCriteriaType: StrengthStressCriteria = ...
    """
    Returns or sets  the stress criteria type 
    
    <hr>
    
    Getter Method
    
    Signature ``StressCriteriaType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrengthStressCriteria` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``StressCriteriaType`` 
    
    :param stressCriteria: 
    :type stressCriteria: :py:class:`NXOpen.CAE.ResponseSimulation.StrengthStressCriteria` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    StressOptionType: StrengthStressOption = ...
    """
    Returns or sets  the stress option type 
    
    <hr>
    
    Getter Method
    
    Signature ``StressOptionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrengthStressOption` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``StressOptionType`` 
    
    :param stressOption: 
    :type stressOption: :py:class:`NXOpen.CAE.ResponseSimulation.StrengthStressOption` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: StrengthResultsEvaluationSettingBuilder = ...  # unknown typename


class ResponseResultsEvaluationSettingBuilder(DynamicResultEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSetting` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateResponseResultsEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def GetDestinationNodes(self) -> 'list[NXOpen.CAE.FENode]':
        """
        Returns the destination nodes  
        
        Signature ``GetDestinationNodes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetDestinationNodes(self, destinationNodes: 'list[NXOpen.CAE.FENode]') -> None:
        """
        Sets the destination nodes 
        
        Signature ``SetDestinationNodes(destinationNodes)`` 
        
        :param destinationNodes: 
        :type destinationNodes: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetDestinationElements(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Returns the destination elements  
        
        Signature ``GetDestinationElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetDestinationElements(self, destinationElement: 'list[NXOpen.CAE.FEElement]') -> None:
        """
        Sets the destination elements 
        
        Signature ``SetDestinationElements(destinationElement)`` 
        
        :param destinationElement: 
        :type destinationElement: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetOutputOptions(self) -> 'list[EvaluationResultType]':
        """
        Returns the output options  
        
        Signature ``GetOutputOptions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetOutputOptions(self, outputOptions: 'list[EvaluationResultType]') -> None:
        """
        Sets the output options 
        
        Signature ``SetOutputOptions(outputOptions)`` 
        
        :param outputOptions: 
        :type outputOptions: list of :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetPointsValueList(self) -> 'list[float]':
        """
        Returns the points value list  
        
        Signature ``GetPointsValueList()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetPointsValueList(self, pointsValueList: 'list[float]') -> None:
        """
        Sets the points value list 
        
        Signature ``SetPointsValueList(pointsValueList)`` 
        
        :param pointsValueList: 
        :type pointsValueList: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    DecimationOrder: int = ...
    """
    Returns or sets  the decimation order of domain setting.  
    
    Only available when response domain is
    :py:class:`CAE.ResponseSimulationResponseDomainDefinitionMethod.StartEndPoint <CAE.ResponseSimulationResponseDomainDefinitionMethod>` 
    
    <hr>
    
    Getter Method
    
    Signature ``DecimationOrder`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``DecimationOrder`` 
    
    :param decimationOrder: 
    :type decimationOrder: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    EndPoint: float = ...
    """
    Returns or sets  the end value of domain setting.  
    
    Only available when response domain is 
    :py:class:`CAE.ResponseSimulationResponseDomainDefinitionMethod.StartEndPoint <CAE.ResponseSimulationResponseDomainDefinitionMethod>` 
    
    <hr>
    
    Getter Method
    
    Signature ``EndPoint`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``EndPoint`` 
    
    :param endPoint: 
    :type endPoint: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    PointValue: float = ...
    """
    Returns or sets  the method choosed to define select point value.  
    
    Only available when response domain is 
    :py:class:`CAE.ResponseSimulationResponseDomainDefinitionMethod.KeyIn <CAE.ResponseSimulationResponseDomainDefinitionMethod>` 
    
    <hr>
    
    Getter Method
    
    Signature ``PointValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``PointValue`` 
    
    :param pointValue: 
    :type pointValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseDomainDefinitionOption: ResponseDomainDefinitionMethod = ...
    """
    Returns or sets  the method choosed to define response domain 
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseDomainDefinitionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ResponseDomainDefinitionMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResponseDomainDefinitionOption`` 
    
    :param definitionMethod: 
    :type definitionMethod: :py:class:`NXOpen.CAE.ResponseSimulation.ResponseDomainDefinitionMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    StartPoint: float = ...
    """
    Returns or sets  the start value of domain setting.  
    
    Only available when response domain is 
    :py:class:`CAE.ResponseSimulationResponseDomainDefinitionMethod.StartEndPoint <CAE.ResponseSimulationResponseDomainDefinitionMethod>` 
    
    <hr>
    
    Getter Method
    
    Signature ``StartPoint`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``StartPoint`` 
    
    :param startPoint: 
    :type startPoint: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: ResponseResultsEvaluationSettingBuilder = ...  # unknown typename


class StrainGageBuilder(BaseBuilder):
    """
    Represents a StrainGageBuilder
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.StrainGageCollection.CreateStrainGageBuilder`
    
    Default values.
    
    ====================  ==========================================
    Property              Value
    ====================  ==========================================
    GageType              UniAxial 
    --------------------  ------------------------------------------
    Placement             Node 
    --------------------  ------------------------------------------
    Plane                 FacePlane 
    --------------------  ------------------------------------------
    ResultType            Strain 
    --------------------  ------------------------------------------
    RotationAngle.Value   0.0 (millimeters part), 0.0 (inches part) 
    --------------------  ------------------------------------------
    ShellElementFace      Top 
    ====================  ==========================================
    
    .. versionadded:: NX6.0.0
    """
    Csys: NXOpen.SmartObject = ...
    """
    Returns or sets  the orientation direction, Only available when the strain gage's orientation plane type is
    :py:class:`CAE.ResponseSimulationStrainGageOrientationPlane.Csys <CAE.ResponseSimulationStrainGageOrientationPlane>`
    
    <hr>
    
    Getter Method
    
    Signature ``Csys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SmartObject` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Csys`` 
    
    :param orientationCoordSystem: 
    :type orientationCoordSystem: :py:class:`NXOpen.SmartObject` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    GageType: StrainGageType = ...
    """
    Returns or sets  the type of strain gage
    
    <hr>
    
    Getter Method
    
    Signature ``GageType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``GageType`` 
    
    :param gageType: 
    :type gageType: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Placement: StrainGagePlacementType = ...
    """
    Returns or sets  the placement type of strain gage
    
    <hr>
    
    Getter Method
    
    Signature ``Placement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGagePlacementType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Placement`` 
    
    :param gagePlacement: 
    :type gagePlacement: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGagePlacementType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Plane: StrainGageOrientationPlane = ...
    """
    Returns or sets  the orientation plane type of strain gage
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageOrientationPlane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageOrientationPlane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResultType: StrainGageResult = ...
    """
    Returns or sets  the result type of strain gage
    
    <hr>
    
    Getter Method
    
    Signature ``ResultType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageResult` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResultType`` 
    
    :param resultType: 
    :type resultType: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageResult` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    RotationAngle: NXOpen.Expression = ...
    """
    Returns  the rotation angle, Only available when the strain gage's orientation plane type is
    :py:class:`CAE.ResponseSimulationStrainGageOrientationPlane.Csys <CAE.ResponseSimulationStrainGageOrientationPlane>` 
    
    <hr>
    
    Getter Method
    
    Signature ``RotationAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SelectedElementFaces: NXOpen.CAE.SelectFEElemFaceList = ...
    """
    Returns   the selected element face.  
    
    Only available when the strain gage's placement type is
    :py:class:`CAE.ResponseSimulationStrainGagePlacementType.ElementFaceCenter <CAE.ResponseSimulationStrainGagePlacementType>`  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedElementFaces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SelectFEElemFaceList` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SelectedNode: NXOpen.CAE.SelectFENodeList = ...
    """
    Returns  the destination nodes, Only available when the strain gage's placement type is
    :py:class:`CAE.ResponseSimulationStrainGagePlacementType.Node <CAE.ResponseSimulationStrainGagePlacementType>`  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedNode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SelectFENodeList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ShellElementFace: StrainGageShellElementFaceType = ...
    """
    Returns or sets  the shell element face location type of strain gage 
    
    <hr>
    
    Getter Method
    
    Signature ``ShellElementFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageShellElementFaceType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ShellElementFace`` 
    
    :param shellElementFace: 
    :type shellElementFace: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageShellElementFaceType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: StrainGageBuilder = ...  # unknown typename


class SensorEvaluationSettingBuilder(FunctionEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.SensorEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.SensorEvaluationSetting` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateSensorEvaluationSettingBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Sensor: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the destination sensor 
    
    <hr>
    
    Getter Method
    
    Signature ``Sensor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: SensorEvaluationSettingBuilder = ...  # unknown typename


class InterpolationMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class InterpolationMethod():
    """
    This enum defines interpolation method 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "LogLog", " - "
       "LinearLinear", " - "
       "LinearLog", " - "
       "LogLinear", " - "
    """
    LogLog = 0  # InterpolationMethodMemberType
    LinearLinear = 1  # InterpolationMethodMemberType
    LinearLog = 2  # InterpolationMethodMemberType
    LogLinear = 3  # InterpolationMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PhysicalDampingSettings(NXOpen.TaggedObject):
    """
    Represents the physical damping settings for a response simulation meta solution   
    
    .. versionadded:: NX6.0.0
    """
    PhysicalHystereticScalingFactor: float = ...
    """
    Returns or sets  the scaling factor for physical hysteretic damping 
    
    <hr>
    
    Getter Method
    
    Signature ``PhysicalHystereticScalingFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``PhysicalHystereticScalingFactor`` 
    
    :param scalingFactor: 
    :type scalingFactor: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    PhysicalViscousScalingFactor: float = ...
    """
    Returns or sets  the scaling factor for physical viscous damping 
    
    <hr>
    
    Getter Method
    
    Signature ``PhysicalViscousScalingFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``PhysicalViscousScalingFactor`` 
    
    :param scalingFactor: 
    :type scalingFactor: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    UsingPhysicalHysteretic: bool = ...
    """
    Returns or sets  the usage setting for physical hysteretic damping 
    
    <hr>
    
    Getter Method
    
    Signature ``UsingPhysicalHysteretic`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``UsingPhysicalHysteretic`` 
    
    :param usingPhysicalHysteretic: 
    :type usingPhysicalHysteretic: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    UsingPhysicalViscous: bool = ...
    """
    Returns or sets  the usage setting for physical viscous damping 
    
    <hr>
    
    Getter Method
    
    Signature ``UsingPhysicalViscous`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``UsingPhysicalViscous`` 
    
    :param usingPhysicalViscous: 
    :type usingPhysicalViscous: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: PhysicalDampingSettings = ...  # unknown typename


class ModalResultsEvaluationSettingBuilder(FunctionEvaluationSettingBuilder):
    """
    Represents the abstract builder class of evaluation setting for FRF and transmissibility   
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    
    def GetOutputNodes(self) -> 'list[NXOpen.CAE.FENode]':
        """
        Returns destination nodes.  
        
        Only available when result type is 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Displacement <CAE.ResponseSimulationEvaluationResultType>`,
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Velocity <CAE.ResponseSimulationEvaluationResultType>`,
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Acceleration <CAE.ResponseSimulationEvaluationResultType>`,
        :py:class:`CAE.ResponseSimulationEvaluationResultType.ReactionForce <CAE.ResponseSimulationEvaluationResultType>`  
        
        Signature ``GetOutputNodes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetOutputNodes(self, destinationNode: 'list[NXOpen.CAE.FENode]') -> None:
        """
        Sets destination nodes 
        
        Signature ``SetOutputNodes(destinationNode)`` 
        
        :param destinationNode: 
        :type destinationNode: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetOutputElements(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Returns destination nodes.  
        
        Only available when result type is 
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Stress <CAE.ResponseSimulationEvaluationResultType>`,
        :py:class:`CAE.ResponseSimulationEvaluationResultType.Strain <CAE.ResponseSimulationEvaluationResultType>`,
        :py:class:`CAE.ResponseSimulationEvaluationResultType.ShellStressResultant <CAE.ResponseSimulationEvaluationResultType>`  
        
        Signature ``GetOutputElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetOutputElements(self, destinationElements: 'list[NXOpen.CAE.FEElement]') -> None:
        """
        Sets destination nodes 
        
        Signature ``SetOutputElements(destinationElements)`` 
        
        :param destinationElements: 
        :type destinationElements: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    DataLocation: DataLocation = ...
    """
    Returns  the frequency setting 
    
    <hr>
    
    Getter Method
    
    Signature ``DataLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DataLocation` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    EvaluationProperty: FrequencyDefinition = ...
    """
    Returns  the frequency setting 
    
    <hr>
    
    Getter Method
    
    Signature ``EvaluationProperty`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FrequencyDefinition` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    InputDirection: DirectionDataComponent = ...
    """
    Returns or sets  the source direction data component 
    
    <hr>
    
    Getter Method
    
    Signature ``InputDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``InputDirection`` 
    
    :param dataComponent: 
    :type dataComponent: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    InputNode: NXOpen.CAE.FENode = ...
    """
    Returns or sets  the source node.  
    
    <hr>
    
    Getter Method
    
    Signature ``InputNode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``InputNode`` 
    
    :param sourceNode: 
    :type sourceNode: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ObservationNode: NXOpen.CAE.FENode = ...
    """
    Returns or sets  the observation nodes.  
    
    <hr>
    
    Getter Method
    
    Signature ``ObservationNode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ObservationNode`` 
    
    :param observationNode: 
    :type observationNode: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    OutputRequest: DirectionDataComponent = ...
    """
    Returns or sets  the destination direction data component 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputRequest`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``OutputRequest`` 
    
    :param dataComponent: 
    :type dataComponent: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: ModalResultsEvaluationSettingBuilder = ...  # unknown typename


class TransmissibilityEvaluationSettingBuilderMotionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransmissibilityEvaluationSettingBuilderMotionType():
    """
    This enum defines input motion type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Displacement", " - "
       "Velocity", " - "
       "Acceleration", " - "
    """
    Displacement = 0  # TransmissibilityEvaluationSettingBuilderMotionTypeMemberType
    Velocity = 1  # TransmissibilityEvaluationSettingBuilderMotionTypeMemberType
    Acceleration = 2  # TransmissibilityEvaluationSettingBuilderMotionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TransmissibilityEvaluationSettingBuilder(ModalResultsEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSetting` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateTransmissibilityEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class MotionType():
        """
        This enum defines input motion type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Displacement", " - "
           "Velocity", " - "
           "Acceleration", " - "
        """
        Displacement = 0  # TransmissibilityEvaluationSettingBuilderMotionTypeMemberType
        Velocity = 1  # TransmissibilityEvaluationSettingBuilderMotionTypeMemberType
        Acceleration = 2  # TransmissibilityEvaluationSettingBuilderMotionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    InputMotionType: TransmissibilityEvaluationSettingBuilderMotionType = ...
    """
    Returns or sets  the input motion type 
    
    <hr>
    
    Getter Method
    
    Signature ``InputMotionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilderMotionType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``InputMotionType`` 
    
    :param motionType: 
    :type motionType: :py:class:`NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilderMotionType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: TransmissibilityEvaluationSettingBuilder = ...  # unknown typename


class RSEventCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of response analysis event   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.ResponseSimulation.Manager`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateEventBuilder(self, raEvent: RSEvent) -> RSEventBuilder:
        """
        Creates a event buider  
        
        Signature ``CreateEventBuilder(raEvent)`` 
        
        :param raEvent: 
        :type raEvent: :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def DeleteEvent(self, raEvent: RSEvent) -> None:
        """
        Deletes an event 
        
        Signature ``DeleteEvent(raEvent)`` 
        
        :param raEvent: 
        :type raEvent: :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def FindObject(self, name: str) -> RSEvent:
        """
        Finds an event with specified event name  
        
        Signature ``FindObject(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEvent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    


class EvaluationSettingBuilder(NXOpen.Builder):
    """
    Represents the abstract builder class of all evaluation setting classes.  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX5.0.0
    """
    Null: EvaluationSettingBuilder = ...  # unknown typename


class VelocityImpactExcitationBuilderImpactMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VelocityImpactExcitationBuilderImpactMethodType():
    """
    the impact definiton methods 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ConstantVelocity", "the users will only be able to specify the velocity for the impact"
       "DropImpact", "the users will be able to specify the drop height or the desired velocity at the impact"
    """
    ConstantVelocity = 0  # VelocityImpactExcitationBuilderImpactMethodTypeMemberType
    DropImpact = 1  # VelocityImpactExcitationBuilderImpactMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class VelocityImpactExcitationBuilder(ExcitationBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder`
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.ExcitationCollection.CreateVelocityImpactExcitationBuilder`
    
    Default values.
    
    =====================================  ==========================================
    Property                               Value
    =====================================  ==========================================
    ImpactDirection.DirectionOption        NodalComponent 
    -------------------------------------  ------------------------------------------
    ImpactDirection.NodalComponent         Dof1 
    -------------------------------------  ------------------------------------------
    ImpactMethod                           ConstantVelocity 
    -------------------------------------  ------------------------------------------
    ImpactParameters.DropHeight.Value      1.0 (millimeters part), 1.0 (inches part) 
    -------------------------------------  ------------------------------------------
    ImpactParameters.PulseDuration.Value   1.0 (millimeters part), 1.0 (inches part) 
    -------------------------------------  ------------------------------------------
    ImpactParameters.StartPosition         AtDrop 
    -------------------------------------  ------------------------------------------
    ImpactParameters.TimeStep.Value        1.0 (millimeters part), 1.0 (inches part) 
    -------------------------------------  ------------------------------------------
    ImpactParameters.Velocity.Value        1.0 (millimeters part), 1.0 (inches part) 
    =====================================  ==========================================
    
    .. versionadded:: NX6.0.0
    """
    
    class ImpactMethodType():
        """
        the impact definiton methods 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ConstantVelocity", "the users will only be able to specify the velocity for the impact"
           "DropImpact", "the users will be able to specify the drop height or the desired velocity at the impact"
        """
        ConstantVelocity = 0  # VelocityImpactExcitationBuilderImpactMethodTypeMemberType
        DropImpact = 1  # VelocityImpactExcitationBuilderImpactMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    ImpactDirection: VelocityImpactDirection = ...
    """
    Returns  the impact direction setting
    
    <hr>
    
    Getter Method
    
    Signature ``ImpactDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactDirection` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ImpactMethod: VelocityImpactExcitationBuilderImpactMethodType = ...
    """
    Returns or sets  the impact method 
    
    <hr>
    
    Getter Method
    
    Signature ``ImpactMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilderImpactMethodType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImpactMethod`` 
    
    :param impactMethod: 
    :type impactMethod: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilderImpactMethodType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ImpactParameters: VelocityImpactParameters = ...
    """
    Returns  the impact parameters setting
    
    <hr>
    
    Getter Method
    
    Signature ``ImpactParameters`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactParameters` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: VelocityImpactExcitationBuilder = ...  # unknown typename


class NodalAveragingOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodalAveragingOption():
    """
    Specifies nodal averaging options 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Shells", " - "
       "Solids", " - "
    """
    Shells = 0  # NodalAveragingOptionMemberType
    Solids = 1  # NodalAveragingOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class InitialConditionsTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class InitialConditionsType():
    """
    Specifies the method to define initial condition 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "QuasiStatic", " - "
       "Zero", " - "
       "UserDefined", " - "
    """
    QuasiStatic = 0  # InitialConditionsTypeMemberType
    Zero = 1  # InitialConditionsTypeMemberType
    UserDefined = 2  # InitialConditionsTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class InitialConditionsEntryMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class InitialConditionsEntryMethod():
    """
    Specifies how to define initial condition for the user customization 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ManualData", " - "
       "FromEef", " - "
    """
    ManualData = 0  # InitialConditionsEntryMethodMemberType
    FromEef = 1  # InitialConditionsEntryMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class InitialConditions(NXOpen.NXObject):
    """
    Represents the initial condition setting of transient event   
    
    .. versionadded:: NX5.0.0
    """
    
    class Type():
        """
        Specifies the method to define initial condition 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "QuasiStatic", " - "
           "Zero", " - "
           "UserDefined", " - "
        """
        QuasiStatic = 0  # InitialConditionsTypeMemberType
        Zero = 1  # InitialConditionsTypeMemberType
        UserDefined = 2  # InitialConditionsTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class EntryMethod():
        """
        Specifies how to define initial condition for the user customization 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ManualData", " - "
           "FromEef", " - "
        """
        ManualData = 0  # InitialConditionsEntryMethodMemberType
        FromEef = 1  # InitialConditionsEntryMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetCustomizedInitialDataById(self, modeId: int) -> ModeInitialData:
        """
        Returns customized initial data of normal mode by mode id.  
        
        Only available when initial condition
        type is :py:class:`CAE.ResponseSimulation.InitialConditionsType.UserDefined <CAE.ResponseSimulation.InitialConditionsType>`  
        
        Signature ``GetCustomizedInitialDataById(modeId)`` 
        
        :param modeId: 
        :type modeId: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ModeInitialData` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetAllCustomizedInitialData(self) -> 'list[ModeInitialData]':
        """
        Returns customized initial data of all normal modes.  
        
        Only available when initial condition type is 
        :py:class:`CAE.ResponseSimulation.InitialConditionsType.UserDefined <CAE.ResponseSimulation.InitialConditionsType>`  
        
        Signature ``GetAllCustomizedInitialData()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.ResponseSimulation.ModeInitialData` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    EntryMethodOption: InitialConditionsEntryMethod = ...
    """
    Returns or sets  the entry method of user customization 
    
    <hr>
    
    Getter Method
    
    Signature ``EntryMethodOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.InitialConditionsEntryMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``EntryMethodOption`` 
    
    :param entryMethod: 
    :type entryMethod: :py:class:`NXOpen.CAE.ResponseSimulation.InitialConditionsEntryMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ExistingEefFile: str = ...
    """
    Returns or sets  an existing EEF file containing initial condition.  
    
    Only available when the 
    initial condition type is :py:class:`CAE.ResponseSimulation.InitialConditionsType.UserDefined <CAE.ResponseSimulation.InitialConditionsType>`
    and the entry method is :py:class:`CAE.ResponseSimulation.InitialConditionsEntryMethod.FromEef <CAE.ResponseSimulation.InitialConditionsEntryMethod>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ExistingEefFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ExistingEefFile`` 
    
    :param eefFile: 
    :type eefFile: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    InitialConditionType: InitialConditionsType = ...
    """
    Returns or sets  the definition method 
    
    <hr>
    
    Getter Method
    
    Signature ``InitialConditionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.InitialConditionsType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``InitialConditionType`` 
    
    :param initialConditionType: 
    :type initialConditionType: :py:class:`NXOpen.CAE.ResponseSimulation.InitialConditionsType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: InitialConditions = ...  # unknown typename


class RSEventTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RSEventType():
    """
    the type of reponse analysis event 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Transient", " - "
       "Frequency", " - "
       "Random", " - "
       "ResponseSpectrum", " - "
       "Ddam", " - "
       "Static", " - "
    """
    Transient = 0  # RSEventTypeMemberType
    Frequency = 1  # RSEventTypeMemberType
    Random = 2  # RSEventTypeMemberType
    ResponseSpectrum = 3  # RSEventTypeMemberType
    Ddam = 4  # RSEventTypeMemberType
    Static = 5  # RSEventTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RSEventAnalysisTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RSEventAnalysisType():
    """
    the analysis type of response analysis event. Only available for
    :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Transient <NXOpen.CAE.ResponseSimulation.RSEventType>` and 
    :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Frequency <NXOpen.CAE.ResponseSimulation.RSEventType>` 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ModeAcceleration", " - "
       "ModeDisplacement", " - "
    """
    ModeAcceleration = 0  # RSEventAnalysisTypeMemberType
    ModeDisplacement = 1  # RSEventAnalysisTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RSEventResultFileTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RSEventResultFileType():
    """
    the result file type of event. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ModalResponse", "Result file to be used as Restart File, which extension is ".eef" or ".sef""
       "FunctionResponse", "Result file to contain function response evaluation results, which extenstion is ".afu""
       "DynamicResponse", "Result file to contain dynamic response evaluation results, which extension is ".rs2""
    """
    ModalResponse = 0  # RSEventResultFileTypeMemberType
    FunctionResponse = 1  # RSEventResultFileTypeMemberType
    DynamicResponse = 2  # RSEventResultFileTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RSEventSpacingTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RSEventSpacingType():
    """
    the spacing type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Even", " - "
       "Uneven", " - "
    """
    Even = 0  # RSEventSpacingTypeMemberType
    Uneven = 1  # RSEventSpacingTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RSEventDdamFormulationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RSEventDdamFormulationType():
    """
    Represents the fromulation type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Standard", " - "
       "UserDefined", " - "
    """
    Standard = 0  # RSEventDdamFormulationTypeMemberType
    UserDefined = 1  # RSEventDdamFormulationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RSEventDurationOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RSEventDurationOption():
    """
    the duration option 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ExcitationFunction", " - "
       "UserDefined", " - "
    """
    ExcitationFunction = 0  # RSEventDurationOptionMemberType
    UserDefined = 1  # RSEventDurationOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RSEvent(NXOpen.NXObject):
    """
    Represents a response analysis event   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.RSEventBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class Type():
        """
        the type of reponse analysis event 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Transient", " - "
           "Frequency", " - "
           "Random", " - "
           "ResponseSpectrum", " - "
           "Ddam", " - "
           "Static", " - "
        """
        Transient = 0  # RSEventTypeMemberType
        Frequency = 1  # RSEventTypeMemberType
        Random = 2  # RSEventTypeMemberType
        ResponseSpectrum = 3  # RSEventTypeMemberType
        Ddam = 4  # RSEventTypeMemberType
        Static = 5  # RSEventTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class AnalysisType():
        """
        the analysis type of response analysis event. Only available for
        :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Transient <NXOpen.CAE.ResponseSimulation.RSEventType>` and 
        :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Frequency <NXOpen.CAE.ResponseSimulation.RSEventType>` 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ModeAcceleration", " - "
           "ModeDisplacement", " - "
        """
        ModeAcceleration = 0  # RSEventAnalysisTypeMemberType
        ModeDisplacement = 1  # RSEventAnalysisTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ResultFileType():
        """
        the result file type of event. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ModalResponse", "Result file to be used as Restart File, which extension is ".eef" or ".sef""
           "FunctionResponse", "Result file to contain function response evaluation results, which extenstion is ".afu""
           "DynamicResponse", "Result file to contain dynamic response evaluation results, which extension is ".rs2""
        """
        ModalResponse = 0  # RSEventResultFileTypeMemberType
        FunctionResponse = 1  # RSEventResultFileTypeMemberType
        DynamicResponse = 2  # RSEventResultFileTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SpacingType():
        """
        the spacing type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Even", " - "
           "Uneven", " - "
        """
        Even = 0  # RSEventSpacingTypeMemberType
        Uneven = 1  # RSEventSpacingTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DdamFormulationType():
        """
        Represents the fromulation type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Standard", " - "
           "UserDefined", " - "
        """
        Standard = 0  # RSEventDdamFormulationTypeMemberType
        UserDefined = 1  # RSEventDdamFormulationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DurationOption():
        """
        the duration option 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ExcitationFunction", " - "
           "UserDefined", " - "
        """
        ExcitationFunction = 0  # RSEventDurationOptionMemberType
        UserDefined = 1  # RSEventDurationOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetSolverParameters(self) -> RSEventSolverParameters:
        """
        Returns the solver parameters  
        
        Signature ``GetSolverParameters()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventSolverParameters` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetCalculateStaticOffset(self) -> bool:
        """
        Returns the option setting for calculating static offset result.  
        
        The staic offset calculation is only available to transient event  
        
        Signature ``GetCalculateStaticOffset()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetCalculateStaticOffset(self, calculateStaticOffset: bool) -> None:
        """
        Set the option setting for calculating static offset result.  
        
        The static offset calculation is
        only available to transient event 
        
        Signature ``SetCalculateStaticOffset(calculateStaticOffset)`` 
        
        :param calculateStaticOffset: 
        :type calculateStaticOffset: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetEventName(self) -> str:
        """
        Returns the event name  
        
        Signature ``GetEventName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetEventName(self, eventName: str, renameResultFile: bool) -> None:
        """
        Sets the event name 
        
        Signature ``SetEventName(eventName, renameResultFile)`` 
        
        :param eventName: 
        :type eventName: str 
        :param renameResultFile:  if there are result files associated with the event, rename them or not 
        :type renameResultFile: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def Destroy(self, deleteResultFile: bool) -> None:
        """
        Deletes a response simulation dynamic event, including all excitations
        under it 
        
        Signature ``Destroy(deleteResultFile)`` 
        
        :param deleteResultFile:  delete the result files associated with the solution or not  
        :type deleteResultFile: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetExcitations(self) -> 'list[Excitation]':
        """
        Returns all excitations of an event  
        
        Signature ``GetExcitations()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.ResponseSimulation.Excitation` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetResultFileName(self, resultFileType: RSEventResultFileType) -> str:
        """
        Returns result file name of specified type  
        
        Signature ``GetResultFileName(resultFileType)`` 
        
        :param resultFileType: 
        :type resultFileType: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventResultFileType` 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def Export(self, eventDefinitionFile: str) -> None:
        """
        Exports event definition to a XML file 
        
        Signature ``Export(eventDefinitionFile)`` 
        
        :param eventDefinitionFile: 
        :type eventDefinitionFile: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateModalFunctionResponse(self) -> None:
        """
        Performs evaluation for modal function response.  
        
        The results is stored in an AFU file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName` 
        
        Signature ``EvaluateModalFunctionResponse()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateNodalFunctionResponse(self, evaluationSetting: NodalFunctionEvaluationSetting) -> None:
        """
        Performs evaluation for nodal function response.  
        
        The results is stored in an AFU file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName` 
        
        Signature ``EvaluateNodalFunctionResponse(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSetting` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateElementalFunctionResponse(self, evaluationSetting: ElementalFunctionEvaluationSetting) -> None:
        """
        Performs evaluation for elemental function response.  
        
        The results is stored in an AFU file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName` 
        
        Signature ``EvaluateElementalFunctionResponse(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSetting` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateCsd(self, evaluationSetting: CsdEvaluationSetting) -> None:
        """
        Performs evaluation for CSD.  
        
        The evaluation results will be stored in an AFU file, 
        which name could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName` 
        
        Signature ``EvaluateCsd(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.CsdEvaluationSetting` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateModalResponse(self) -> None:
        """
        Performs evaluation for modal response.  
        
        The results is getting eef file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName` 
        
        Signature ``EvaluateModalResponse()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateResponseResults(self, evaluationSetting: ResponseResultsEvaluationSetting) -> None:
        """
        Performs evaluation for response results.  
        
        The results is stored in an RS2 file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName`.  
        
        Signature ``EvaluateResponseResults(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSetting` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateStrengthResults(self, evaluationSetting: StrengthResultsEvaluationSetting) -> None:
        """
        Performs evaluation for strength results.  
        
        The results is stored in an RS2 file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName`.  
        
        Signature ``EvaluateStrengthResults(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSetting` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluatePeakValueResults(self, evaluationSetting: PeakValueEvaluationSetting) -> None:
        """
        Performs evaluation for peak value results.  
        
        The results is stored in an RS2 file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName`.  
        
        Signature ``EvaluatePeakValueResults(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSetting` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateRmsResults(self, evaluationSetting: RmsResultsEvaluationSetting) -> None:
        """
        Perfroms evaluation for RMS results.  
        
        The results is stored in an RS2 file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName`. 
        
        Signature ``EvaluateRmsResults(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSetting` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateLcrResults(self, evaluationSetting: LcrResultsEvaluationSetting) -> None:
        """
        Performs evaluation for LCR results.  
        
        The results is stored in an RS2 file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName` 
        
        Signature ``EvaluateLcrResults(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSetting` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    @typing.overload
    def EvaluateSensorResponse(self) -> None:
        """
        Performs evaluation for sensor response. The results is stored in an AFU file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName` 
        
        Signature ``EvaluateSensorResponse()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    @typing.overload
    def EvaluateSensorResponse(self, evaluationSetting: SensorEvaluationSetting) -> None:
        """
        Performs evaluation for sensor response. The results is stored in an AFU file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName` 
        
        Signature ``EvaluateSensorResponse(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.SensorEvaluationSetting` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def EvaluateStrainGageResponse(self, evaluationSetting: StrainGageEvaluationSetting) -> None:
        """
        Performs evaluation for strain gage response.  
        
        The results is stored in an AFU file, which file name
        could be returned by :py:meth:`NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName` 
        
        Signature ``EvaluateStrainGageResponse(evaluationSetting)`` 
        
        :param evaluationSetting: 
        :type evaluationSetting: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSetting` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    Null: RSEvent = ...  # unknown typename


class DDAMExcitationBuilder(ExcitationBuilder):
    """
    Represents the manager to :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitation`.  
    
    The object of type :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitation` can only
    be created or edited through this class. 
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.ExcitationCollection.CreateDdamExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def SetComponentStatus(self, component: ExcitationComponent, enable: bool) -> None:
        """
        Sets the status for a direction component
        
        Signature ``SetComponentStatus(component, enable)`` 
        
        :param component: 
        :type component: :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationComponent` 
        :param enable: 
        :type enable: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetComponentStatus(self, component: ExcitationComponent) -> bool:
        """
        Returns the status of a dierction component  
        
        Signature ``GetComponentStatus(component)`` 
        
        :param component: 
        :type component: :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationComponent` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    LoadingType: DDAMExcitationLoadingType = ...
    """
    Returns or sets  the loading type
    
    <hr>
    
    Getter Method
    
    Signature ``LoadingType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationLoadingType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``LoadingType`` 
    
    :param loadingType: 
    :type loadingType: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationLoadingType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseType: DDAMExcitationResponseType = ...
    """
    Returns or sets  the response type
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationResponseType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResponseType`` 
    
    :param responseType: 
    :type responseType: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationResponseType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: DDAMExcitationBuilder = ...  # unknown typename


class ElementLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElementLocation():
    """
    Specifies element locations 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Both", " - "
       "Centroid", " - "
       "Corners", " - "
    """
    Both = 0  # ElementLocationMemberType
    Centroid = 1  # ElementLocationMemberType
    Corners = 2  # ElementLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SensorEvaluationSetting(DynamicResultEvaluationSetting):
    """
    Represents the parameters setting for sensor evaluation.  
    
    For more information, see the 
    Response Dynamics section of the Gateway Help 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.SensorEvaluationSettingBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: SensorEvaluationSetting = ...  # unknown typename


class StrainGageEvaluationSetting(DynamicResultEvaluationSetting):
    """
    Represents the parameters setting for strain gage evaluation.  
    
    For more information, see the 
    Response Dynamics section of the Gateway Help 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSettingBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: StrainGageEvaluationSetting = ...  # unknown typename


class ModeInitialData(NXOpen.NXObject):
    """
    Represents the initial setting for a normal mode   
    
    .. versionadded:: NX5.0.0
    """
    
    def GetModeId(self) -> int:
        """
        Returns normal mode ID  
        
        Signature ``GetModeId()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    InitialDisplacement: float = ...
    """
    Returns or sets  the initial diaplacement 
    
    <hr>
    
    Getter Method
    
    Signature ``InitialDisplacement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``InitialDisplacement`` 
    
    :param initialDisplacement: 
    :type initialDisplacement: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    InitialVelocity: float = ...
    """
    Returns or sets  the initial velocity 
    
    <hr>
    
    Getter Method
    
    Signature ``InitialVelocity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``InitialVelocity`` 
    
    :param initialVelocity: 
    :type initialVelocity: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: ModeInitialData = ...  # unknown typename


class StrainGage(NXOpen.DisplayableObject):
    """
    Represents a :py:class:`NXOpen.CAE.ResponseSimulation.StrainGage`
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    def GetDisplayAttribute(self) -> RSDisplayObject:
        """
        Get display attribute of gage  
        
        Signature ``GetDisplayAttribute()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSDisplayObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    Null: StrainGage = ...  # unknown typename


class DDAMComponentDataResponseTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DDAMComponentDataResponseType():
    """
    Specifies the response type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Elastic", " - "
       "ElasticPlastic", " - "
    """
    Elastic = 0  # DDAMComponentDataResponseTypeMemberType
    ElasticPlastic = 1  # DDAMComponentDataResponseTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DDAMComponentDataLoadingTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DDAMComponentDataLoadingType():
    """
    Specifies the loading type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Vertical", " - "
       "Athwartship", " - "
       "ForeAndAft", " - "
    """
    Vertical = 0  # DDAMComponentDataLoadingTypeMemberType
    Athwartship = 1  # DDAMComponentDataLoadingTypeMemberType
    ForeAndAft = 2  # DDAMComponentDataLoadingTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DDAMComponentData(NXOpen.TaggedObject):
    """
    Represents an excitation on one specified direction.  
    
    .. versionadded:: NX5.0.0
    """
    
    class ResponseType():
        """
        Specifies the response type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Elastic", " - "
           "ElasticPlastic", " - "
        """
        Elastic = 0  # DDAMComponentDataResponseTypeMemberType
        ElasticPlastic = 1  # DDAMComponentDataResponseTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LoadingType():
        """
        Specifies the loading type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Vertical", " - "
           "Athwartship", " - "
           "ForeAndAft", " - "
        """
        Vertical = 0  # DDAMComponentDataLoadingTypeMemberType
        Athwartship = 1  # DDAMComponentDataLoadingTypeMemberType
        ForeAndAft = 2  # DDAMComponentDataLoadingTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetComponentType(self) -> ExcitationComponent:
        """
        Returns the component type  
        
        Signature ``GetComponentType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationComponent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetEnable(self) -> bool:
        """
        Returns the enable option  
        
        Signature ``GetEnable()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    LoadingTypeOption: DDAMComponentDataLoadingType = ...
    """
    Returns or sets  the option of loading type 
    
    <hr>
    
    Getter Method
    
    Signature ``LoadingTypeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMComponentDataLoadingType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``LoadingTypeOption`` 
    
    :param loadingType: 
    :type loadingType: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMComponentDataLoadingType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseTypeOption: DDAMComponentDataResponseType = ...
    """
    Returns or sets  the option of response type 
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseTypeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMComponentDataResponseType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ResponseTypeOption`` 
    
    :param responseType: 
    :type responseType: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMComponentDataResponseType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: DDAMComponentData = ...  # unknown typename


class NodalFunctionEvaluationSettingBuilder(FunctionEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSetting` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateNodalFunctionEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def GetDestinationNodes(self) -> 'list[NXOpen.CAE.FENode]':
        """
        Returns the destination nodes  
        
        Signature ``GetDestinationNodes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetDestinationNodes(self, destinationNodes: 'list[NXOpen.CAE.FENode]') -> None:
        """
        Sets the destination nodes 
        
        Signature ``SetDestinationNodes(destinationNodes)`` 
        
        :param destinationNodes: 
        :type destinationNodes: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    BeamDataLocation: NodalFunctionEvalBeamLocation = ...
    """
    Returns or sets  the evaluation location of beam element, which is available when 
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType` is 
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.Stress <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`, or
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.Strain <NXOpen.CAE.ResponseSimulation.EvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``BeamDataLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvalBeamLocation` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``BeamDataLocation`` 
    
    :param beamLocation: 
    :type beamLocation: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvalBeamLocation` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    CoordinateSystem: CoordinateSystem = ...
    """
    Returns or sets  the coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``CoordinateSystem`` 
    
    :param coordinateSystem: 
    :type coordinateSystem: :py:class:`NXOpen.CAE.ResponseSimulation.CoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    DataComponent: DirectionDataComponent = ...
    """
    Returns or sets  the direction data component 
    
    <hr>
    
    Getter Method
    
    Signature ``DataComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``DataComponent`` 
    
    :param dataComponent: 
    :type dataComponent: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    RelativeNode: NXOpen.CAE.FENode = ...
    """
    Returns or sets  the relative node  
    
    <hr>
    
    Getter Method
    
    Signature ``RelativeNode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``RelativeNode`` 
    
    :param relativeNode: 
    :type relativeNode: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ShellDataLocation: NodalFunctionEvalShellLocation = ...
    """
    Returns or sets  the evaluation location of shell element, which is available when 
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType` is 
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.Stress <NXOpen.CAE.ResponseSimulation.EvaluationResultType>`, or
    :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationResultType.Strain <NXOpen.CAE.ResponseSimulation.EvaluationResultType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ShellDataLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvalShellLocation` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ShellDataLocation`` 
    
    :param shellLocation: 
    :type shellLocation: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvalShellLocation` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    UserDefinedDirection: NXOpen.Direction = ...
    """
    Returns or sets   the user defined direction 
    
    <hr>
    
    Getter Method
    
    Signature ``UserDefinedDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``UserDefinedDirection`` 
    
    :param userDefinedDirection: 
    :type userDefinedDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    UsingUserDefinedDirection: NodalFunctionEvalRequest = ...
    """
    Returns or sets  the option of using user defined direction 
    
    <hr>
    
    Getter Method
    
    Signature ``UsingUserDefinedDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``UsingUserDefinedDirection`` 
    
    :param usingUserDefinedDirection: 
    :type usingUserDefinedDirection: :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: NodalFunctionEvaluationSettingBuilder = ...  # unknown typename


class EvaluationResultTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EvaluationResultType():
    """
    Specifies the evaluation result type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Receptance", " - "
       "Mobility", " - "
       "Inertance", " - "
       "Displacement", " - "
       "Velocity", " - "
       "Acceleration", " - "
       "Stress", " - "
       "Strain", " - "
       "StrainEnergy", " - "
       "ShellResultant", " - "
       "ElementForce", " - "
       "BeamElementForce", " - "
       "ShellStressResultant", " - "
       "ReactionForce", " - "
    """
    Receptance = 0  # EvaluationResultTypeMemberType
    Mobility = 1  # EvaluationResultTypeMemberType
    Inertance = 2  # EvaluationResultTypeMemberType
    Displacement = 3  # EvaluationResultTypeMemberType
    Velocity = 4  # EvaluationResultTypeMemberType
    Acceleration = 5  # EvaluationResultTypeMemberType
    Stress = 6  # EvaluationResultTypeMemberType
    Strain = 7  # EvaluationResultTypeMemberType
    StrainEnergy = 8  # EvaluationResultTypeMemberType
    ShellResultant = 9  # EvaluationResultTypeMemberType
    ElementForce = 10  # EvaluationResultTypeMemberType
    BeamElementForce = 11  # EvaluationResultTypeMemberType
    ShellStressResultant = 12  # EvaluationResultTypeMemberType
    ReactionForce = 13  # EvaluationResultTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StrainGageShellElementFaceTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StrainGageShellElementFaceType():
    """
    Specifies the shell element location type of Strain Gage 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Top", " - "
       "Botton", " - "
    """
    Top = 0  # StrainGageShellElementFaceTypeMemberType
    Botton = 1  # StrainGageShellElementFaceTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ExcitationCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of excitation objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.ResponseSimulation.Manager`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateTranslationalNodalFunctionExcitationBuilder(self, excitation: TranslationalNodalFunctionExcitation) -> TranslationalNodalFunctionExcitationBuilder:
        """
        Creates the builder object of :py:class:`NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitation`  
        
        Signature ``CreateTranslationalNodalFunctionExcitationBuilder(excitation)`` 
        
        :param excitation: 
        :type excitation: :py:class:`NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitation` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateRotationalNodalFunctionExcitationBuilder(self, excitation: RotationalNodalFunctionExcitation) -> RotationalNodalFunctionExcitationBuilder:
        """
        Creates the builder object of :py:class:`NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitation`  
        
        Signature ``CreateRotationalNodalFunctionExcitationBuilder(excitation)`` 
        
        :param excitation: 
        :type excitation: :py:class:`NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitation` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateDistributedLoadExcitationBuilder(self, excitation: DistributedLoadExcitation) -> DistributedLoadExcitationBuilder:
        """
        Creates the builder object of :py:class:`NXOpen.CAE.ResponseSimulation.DistributedLoadExcitation` 
        
        Signature ``CreateDistributedLoadExcitationBuilder(excitation)`` 
        
        :param excitation: 
        :type excitation: :py:class:`NXOpen.CAE.ResponseSimulation.DistributedLoadExcitation` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DistributedLoadExcitationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateDdamExcitationBuilder(self, excitation: DDAMExcitation) -> DDAMExcitationBuilder:
        """
        Creates the builder object of :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitation`  
        
        Signature ``CreateDdamExcitationBuilder(excitation)`` 
        
        :param excitation: 
        :type excitation: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitation` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateTranslationalDdamExcitationBuilder(self, excitation: DDAMExcitation) -> DDAMExcitationBuilder:
        """
        Creates the builder object of :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitation`  
        
        Signature ``CreateTranslationalDdamExcitationBuilder(excitation)`` 
        
        :param excitation: 
        :type excitation: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitation` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateRotationalDdamExcitationBuilder(self, excitation: DDAMExcitation) -> DDAMExcitationBuilder:
        """
        Creates the builder object of :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitation`  
        
        Signature ``CreateRotationalDdamExcitationBuilder(excitation)`` 
        
        :param excitation: 
        :type excitation: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitation` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateCsdExcitationBuilder(self, excitation: CSDExcitation) -> CSDExcitationBuilder:
        """
        Creates the builder object of :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitation`  
        
        Signature ``CreateCsdExcitationBuilder(excitation)`` 
        
        :param excitation: 
        :type excitation: :py:class:`NXOpen.CAE.ResponseSimulation.CSDExcitation` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CSDExcitationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateVelocityImpactExcitationBuilder(self, excitation: VelocityImpactExcitation) -> VelocityImpactExcitationBuilder:
        """
        Creates the builder object of :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactExcitation`  
        
        Signature ``CreateVelocityImpactExcitationBuilder(excitation)`` 
        
        :param excitation: 
        :type excitation: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactExcitation` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def CreateStaticLoadExcitationBuilder(self, excitation: StaticLoadExcitation) -> StaticLoadExcitationBuilder:
        """
        Creates the builder object of :py:class:`NXOpen.CAE.ResponseSimulation.StaticLoadExcitation` 
        
        Signature ``CreateStaticLoadExcitationBuilder(excitation)`` 
        
        :param excitation: 
        :type excitation: :py:class:`NXOpen.CAE.ResponseSimulation.StaticLoadExcitation` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StaticLoadExcitationBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def DeleteExcitation(self, excitation: Excitation) -> None:
        """
        Deletes an excitation 
        
        Signature ``DeleteExcitation(excitation)`` 
        
        :param excitation: 
        :type excitation: :py:class:`NXOpen.CAE.ResponseSimulation.Excitation` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def FindObject(self, name: str) -> Excitation:
        """
        Finds an excitation with specified excitation name  
        
        Signature ``FindObject(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.Excitation` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    


class ResponseDomainDefinitionMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ResponseDomainDefinitionMethod():
    """
    Specifies response result evaluation options
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "StartEndPoint", " - "
       "KeyIn", " - "
       "NaturalFrequency", " - "
    """
    StartEndPoint = 0  # ResponseDomainDefinitionMethodMemberType
    KeyIn = 1  # ResponseDomainDefinitionMethodMemberType
    NaturalFrequency = 2  # ResponseDomainDefinitionMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NormalMode(NXOpen.NXObject):
    """
    Represents the properties of one normal mode   
    
    .. versionadded:: NX5.0.0
    """
    
    def GetModeId(self) -> int:
        """
        Returns mode ID  
        
        Signature ``GetModeId()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetFrequency(self) -> float:
        """
        Returns the natrual frequency of the normal mode  
        
        Signature ``GetFrequency()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetStiffeness(self) -> float:
        """
        Returns the stiffeness of the normal mode  
        
        Signature ``GetStiffeness()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetMass(self) -> float:
        """
        Returns the mass of the normal mode  
        
        Signature ``GetMass()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetXMass(self) -> float:
        """
        Returns the percent mass of X direction component  
        
        Signature ``GetXMass()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetYMass(self) -> float:
        """
        Returns the percent mass of Y direction component  
        
        Signature ``GetYMass()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetZMass(self) -> float:
        """
        Returns the percent mass of Z direction component  
        
        Signature ``GetZMass()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetRxMass(self) -> float:
        """
        Returns the percent mass of Rx direction component  
        
        Signature ``GetRxMass()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetRyMass(self) -> float:
        """
        Returns the percent mass of Ry direction component  
        
        Signature ``GetRyMass()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetRzMass(self) -> float:
        """
        Returns the percent mass of Rz direction component  
        
        Signature ``GetRzMass()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetPhysicalViscous(self) -> float:
        """
        Returns the physical viscous factor  
        
        Signature ``GetPhysicalViscous()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def GetPhysicalHysteretic(self) -> float:
        """
        Returns the physical hysteretic factor  
        
        Signature ``GetPhysicalHysteretic()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    Active: bool = ...
    """
    Returns or sets  the activate status 
    
    <hr>
    
    Getter Method
    
    Signature ``Active`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Active`` 
    
    :param active: 
    :type active: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Hysteretic: float = ...
    """
    Returns or sets  the hysteretic factor 
    
    <hr>
    
    Getter Method
    
    Signature ``Hysteretic`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Hysteretic`` 
    
    :param hysteretic: 
    :type hysteretic: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Viscous: float = ...
    """
    Returns or sets  the viscous factor 
    
    <hr>
    
    Getter Method
    
    Signature ``Viscous`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Viscous`` 
    
    :param viscous: 
    :type viscous: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: NormalMode = ...  # unknown typename


class LcrResultsEvaluationSetting(RmsResultsEvaluationSetting):
    """
    Represents the parameters setting of LCR results evaluation.  
    
    Only available when
    event type is :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Random <NXOpen.CAE.ResponseSimulation.RSEventType>`. For more information,
    see the Response Dynamics Section of the Gateway Help 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: LcrResultsEvaluationSetting = ...  # unknown typename


class StrengthStressOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StrengthStressOption():
    """
    The options of stress 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ElementMaximum", " - "
       "NodeOnElement", " - "
    """
    ElementMaximum = 0  # StrengthStressOptionMemberType
    NodeOnElement = 1  # StrengthStressOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StrengthResultsEvaluationSetting(DynamicResultEvaluationSetting):
    """
    Represents parameters setting for strength results evaluation.  
    
    Available to all kinds of 
    event type 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: StrengthResultsEvaluationSetting = ...  # unknown typename


class ResponseResultsEvaluationSetting(DynamicResultEvaluationSetting):
    """
    Represents the parameters setting for response results evaluation.  
    
    Only available when 
    event type are :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Transient <NXOpen.CAE.ResponseSimulation.RSEventType>` and 
    :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Frequency <NXOpen.CAE.ResponseSimulation.RSEventType>`. For more information, see the 
    Response Dynamics section of the Gateway Help 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: ResponseResultsEvaluationSetting = ...  # unknown typename


class ElementalFunctionEvalBeamLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElementalFunctionEvalBeamLocation():
    """
    Specifies beam element evaluation locations 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "C", " - "
       "D", " - "
       "E", " - "
       "F", " - "
    """
    C = 0  # ElementalFunctionEvalBeamLocationMemberType
    D = 1  # ElementalFunctionEvalBeamLocationMemberType
    E = 2  # ElementalFunctionEvalBeamLocationMemberType
    F = 3  # ElementalFunctionEvalBeamLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DistributedLoadExcitation(Excitation):
    """
    Represents an excitation of distributed-load type   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.DistributedLoadExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: DistributedLoadExcitation = ...  # unknown typename


class SolutionBuilder(BaseBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.Solution` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.Solution` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.SolutionCollection.CreateSolutionBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Attributes: SolutionAttributes = ...
    """
    Returns  the attributes setting 
    
    <hr>
    
    Getter Method
    
    Signature ``Attributes`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.SolutionAttributes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ImportedEefFile: str = ...
    """
    Returns or sets  the EEF file imported to create an imported response analysis meta solution.  
    
    There is 
    event definition containing in the EEF file. An event will be created with the solution.
    To the imported solution and event, the users can only perform evaluation and not able to
    create new events and excitations
    
    <hr>
    
    Getter Method
    
    Signature ``ImportedEefFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ImportedEefFile`` 
    
    :param importedEefFile: 
    :type importedEefFile: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ReferencedSolution: NXOpen.CAE.SimSolution = ...
    """
    Returns or sets  the referenced solution which must be a SEMODES *103 solution with modal results solved 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferencedSolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SimSolution` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferencedSolution`` 
    
    :param referencedSolution:  This parameter may not be None. 
    :type referencedSolution: :py:class:`NXOpen.CAE.SimSolution` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: SolutionBuilder = ...  # unknown typename


class DirectionDataComponentMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DirectionDataComponent():
    """
    Specifies the direction data components 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", " - "
       "Y", " - "
       "Z", " - "
       "Rx", " - "
       "Ry", " - "
       "Rz", " - "
       "Xx", " - "
       "Yy", " - "
       "Zz", " - "
       "Xy", " - "
       "Xz", " - "
       "Yz", " - "
       "Ax", " - "
       "Sy", " - "
       "Sz", " - "
       "Tx", " - "
       "Byy", " - "
       "Bz", " - "
       "Fxx", " - "
       "Fyy", " - "
       "Fzz", " - "
       "Fxy", " - "
       "Mx", " - "
       "My", " - "
       "Mz", " - "
       "Mxy", " - "
       "Mxz", " - "
       "Myz", " - "
       "Vx", " - "
       "Vy", " - "
       "TranslationalMagnitude", " - "
       "Vonmises", " - "
       "MaxPrincipal", " - "
       "MinPrincipal", " - "
       "MaxShear", " - "
       "AllNormals", " - "
       "AllTranslational", " - "
       "AllForces", " - "
       "AllDirections", " - "
       "AllDataComponents", " - "
       "All", " - "
       "AllXyPlane", " - "
       "Leg1", " - "
       "Leg2", " - "
       "Leg3", " - "
       "AllLegs", " - "
    """
    X = 0  # DirectionDataComponentMemberType
    Y = 1  # DirectionDataComponentMemberType
    Z = 2  # DirectionDataComponentMemberType
    Rx = 3  # DirectionDataComponentMemberType
    Ry = 4  # DirectionDataComponentMemberType
    Rz = 5  # DirectionDataComponentMemberType
    Xx = 6  # DirectionDataComponentMemberType
    Yy = 7  # DirectionDataComponentMemberType
    Zz = 8  # DirectionDataComponentMemberType
    Xy = 9  # DirectionDataComponentMemberType
    Xz = 10  # DirectionDataComponentMemberType
    Yz = 11  # DirectionDataComponentMemberType
    Ax = 12  # DirectionDataComponentMemberType
    Sy = 13  # DirectionDataComponentMemberType
    Sz = 14  # DirectionDataComponentMemberType
    Tx = 15  # DirectionDataComponentMemberType
    Byy = 16  # DirectionDataComponentMemberType
    Bz = 17  # DirectionDataComponentMemberType
    Fxx = 18  # DirectionDataComponentMemberType
    Fyy = 19  # DirectionDataComponentMemberType
    Fzz = 20  # DirectionDataComponentMemberType
    Fxy = 21  # DirectionDataComponentMemberType
    Mx = 22  # DirectionDataComponentMemberType
    My = 23  # DirectionDataComponentMemberType
    Mz = 24  # DirectionDataComponentMemberType
    Mxy = 25  # DirectionDataComponentMemberType
    Mxz = 26  # DirectionDataComponentMemberType
    Myz = 27  # DirectionDataComponentMemberType
    Vx = 28  # DirectionDataComponentMemberType
    Vy = 29  # DirectionDataComponentMemberType
    TranslationalMagnitude = 30  # DirectionDataComponentMemberType
    Vonmises = 31  # DirectionDataComponentMemberType
    MaxPrincipal = 32  # DirectionDataComponentMemberType
    MinPrincipal = 33  # DirectionDataComponentMemberType
    MaxShear = 34  # DirectionDataComponentMemberType
    AllNormals = 35  # DirectionDataComponentMemberType
    AllTranslational = 36  # DirectionDataComponentMemberType
    AllForces = 37  # DirectionDataComponentMemberType
    AllDirections = 38  # DirectionDataComponentMemberType
    AllDataComponents = 39  # DirectionDataComponentMemberType
    All = 40  # DirectionDataComponentMemberType
    AllXyPlane = 41  # DirectionDataComponentMemberType
    Leg1 = 42  # DirectionDataComponentMemberType
    Leg2 = 43  # DirectionDataComponentMemberType
    Leg3 = 44  # DirectionDataComponentMemberType
    AllLegs = 45  # DirectionDataComponentMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TranslationalDDAMExcitationBuilder(DDAMExcitationBuilder):
    """
    Represents the manager to :py:class:`CAE.ResponseSimulation.DDAMExcitation`.  
    
    The object of type :py:class:`CAE.ResponseSimulation.DDAMExcitation` can only
    be created or edited through this class. 
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.ExcitationCollection.CreateTranslationalDdamExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: TranslationalDDAMExcitationBuilder = ...  # unknown typename


class CoordinateSystemMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CoordinateSystem():
    """
    Specifies the coordinate system 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Nodal", " - "
       "Global", " - "
       "Elemental", " - "
       "Material", " - "
    """
    Nodal = 0  # CoordinateSystemMemberType
    Global = 1  # CoordinateSystemMemberType
    Elemental = 2  # CoordinateSystemMemberType
    Material = 3  # CoordinateSystemMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RSEventAttributes(NXOpen.TaggedObject):
    """
    Represents all possible attributes setting for response analysis event   
    
    .. versionadded:: NX5.0.0
    """
    AnalysisType: RSEventAnalysisType = ...
    """
    Returns or sets  the analysis type.  
    
    Only available for transient event and frequency event 
    
    <hr>
    
    Getter Method
    
    Signature ``AnalysisType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventAnalysisType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``AnalysisType`` 
    
    :param analysisType: 
    :type analysisType: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventAnalysisType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    CoefficientDefinitionMethod: DDAMExcitationCoefficientDefinitionType = ...
    """
    Returns or sets  the DDAM coefficient definition method 
    
    <hr>
    
    Getter Method
    
    Signature ``CoefficientDefinitionMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationCoefficientDefinitionType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``CoefficientDefinitionMethod`` 
    
    :param definitionMethod: 
    :type definitionMethod: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationCoefficientDefinitionType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    CoefficientFile: str = ...
    """
    Returns or sets  the DDAM coefficients definition file.  
    
    Only available when event type is
    :py:class:`CAE.ResponseSimulation.DDAMExcitationCoefficientDefinitionType.ByFile <CAE.ResponseSimulation.DDAMExcitationCoefficientDefinitionType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``CoefficientFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``CoefficientFile`` 
    
    :param coefficientFile: 
    :type coefficientFile: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Duration: float = ...
    """
    Returns or sets  the time duration in second for transient event 
    
    <hr>
    
    Getter Method
    
    Signature ``Duration`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Duration`` 
    
    :param duration: 
    :type duration: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    DurationOption: RSEventDurationOption = ...
    """
    Returns or sets  the time duration optionin option for transient event 
    
    <hr>
    
    Getter Method
    
    Signature ``DurationOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventDurationOption` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DurationOption`` 
    
    :param durationOption: 
    :type durationOption: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventDurationOption` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    FastRmsMethod: bool = ...
    """
    Returns or sets  the Use Fast RMS Method.  
    
    Only available when event type is
    :py:class:`CAE.ResponseSimulation.RSEventType.Random <CAE.ResponseSimulation.RSEventType>`>,
    
    <hr>
    
    Getter Method
    
    Signature ``FastRmsMethod`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``FastRmsMethod`` 
    
    :param fastRmsMethod: 
    :type fastRmsMethod: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Formulation: RSEventDdamFormulationType = ...
    """
    Returns or sets  the DDAM formulation type
    
    <hr>
    
    Getter Method
    
    Signature ``Formulation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventDdamFormulationType` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Formulation`` 
    
    :param formulation: 
    :type formulation: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventDdamFormulationType` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    InterpolationMethod: InterpolationMethod = ...
    """
    Returns or sets  the interpolation method.  
    
    only available when event type is
    :py:class:`CAE.ResponseSimulation.RSEventType.Frequency <CAE.ResponseSimulation.RSEventType>`,
    :py:class:`CAE.ResponseSimulation.RSEventType.Random <CAE.ResponseSimulation.RSEventType>`, 
    :py:class:`CAE.ResponseSimulation.RSEventType.ResponseSpectrum <CAE.ResponseSimulation.RSEventType>`,
    
    <hr>
    
    Getter Method
    
    Signature ``InterpolationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.InterpolationMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``InterpolationMethod`` 
    
    :param interpolationMethod: 
    :type interpolationMethod: :py:class:`NXOpen.CAE.ResponseSimulation.InterpolationMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    MinimumGValue: float = ...
    """
    Returns or sets  the Minimum G value 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumGValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumGValue`` 
    
    :param minimumG: 
    :type minimumG: float 
    
    .. versionadded:: NX7.5.2
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    MountingType: DDAMExcitationMountingType = ...
    """
    Returns or sets  the ship type
    
    <hr>
    
    Getter Method
    
    Signature ``MountingType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationMountingType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``MountingType`` 
    
    :param mountingType: 
    :type mountingType: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationMountingType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ResponseType: DDAMExcitationResponseType = ...
    """
    Returns or sets  the DDAM response type
    
    <hr>
    
    Getter Method
    
    Signature ``ResponseType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationResponseType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ResponseType`` 
    
    :param responseType: 
    :type responseType: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationResponseType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ShipType: DDAMExcitationShipType = ...
    """
    Returns or sets  the ship type
    
    <hr>
    
    Getter Method
    
    Signature ``ShipType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationShipType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ShipType`` 
    
    :param shipType: 
    :type shipType: :py:class:`NXOpen.CAE.ResponseSimulation.DDAMExcitationShipType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Spacing: RSEventSpacingType = ...
    """
    Returns or sets  the spacing type
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventSpacingType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Spacing`` 
    
    :param spacing: 
    :type spacing: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventSpacingType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    SpectralLines: int = ...
    """
    Returns or sets  the spectral lines setting.  
    
    Only available when event type is
    :py:class:`CAE.ResponseSimulation.RSEventType.Frequency <CAE.ResponseSimulation.RSEventType>`,
    :py:class:`CAE.ResponseSimulation.RSEventType.Random <CAE.ResponseSimulation.RSEventType>`,
    :py:class:`CAE.ResponseSimulation.RSEventType.ResponseSpectrum <CAE.ResponseSimulation.RSEventType>`,
    
    <hr>
    
    Getter Method
    
    Signature ``SpectralLines`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``SpectralLines`` 
    
    :param spectralLine: 
    :type spectralLine: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: RSEventAttributes = ...  # unknown typename


class FrfEvaluationSettingBuilder(ModalResultsEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.FrfEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.FrfEvaluationSetting` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateFrfEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: FrfEvaluationSettingBuilder = ...  # unknown typename


class StrainGageOrientationPlaneMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StrainGageOrientationPlane():
    """
    Specifies the orientation plane type of Strain Gage 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FacePlane", " - "
       "Csys", " - "
    """
    FacePlane = 0  # StrainGageOrientationPlaneMemberType
    Csys = 1  # StrainGageOrientationPlaneMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FunctionComponentData(NXOpen.TaggedObject):
    """
    Represents a function component setting of 
    :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionExcitation` on one direction   
    
    .. versionadded:: NX5.0.0
    """
    
    def GetComponentType(self) -> ExcitationComponent:
        """
        Returns the component type  
        
        Signature ``GetComponentType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationComponent` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    Enable: bool = ...
    """
    Returns or sets  the option to enable the function component to be used while evaluating 
    
    <hr>
    
    Getter Method
    
    Signature ``Enable`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Enable`` 
    
    :param enableOption: 
    :type enableOption: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Function: NXOpen.CAE.Function = ...
    """
    Returns or sets  the function to be applied 
    
    <hr>
    
    Getter Method
    
    Signature ``Function`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Function` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``Function`` 
    
    :param excitationFunction: 
    :type excitationFunction: :py:class:`NXOpen.CAE.Function` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    PhaseAngle: float = ...
    """
    Returns or sets  the phase angle.  
    
    Only available when the onwer event is 
    :py:class:`NXOpen.CAE.ResponseSimulation.RSEventType.Transient <NXOpen.CAE.ResponseSimulation.RSEventType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``PhaseAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``PhaseAngle`` 
    
    :param phaseAngle: 
    :type phaseAngle: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ScalarFactor: float = ...
    """
    Returns or sets  the scalar factor 
    
    <hr>
    
    Getter Method
    
    Signature ``ScalarFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ScalarFactor`` 
    
    :param scalarFactor: 
    :type scalarFactor: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: FunctionComponentData = ...  # unknown typename


class EvaluationParametersAnalysisIntegrationMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EvaluationParametersAnalysisIntegrationMethod():
    """
    the integration method used for transient analysis 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DuhameldIntegral", " - "
       "NewmarkBeta", " - "
    """
    DuhameldIntegral = 0  # EvaluationParametersAnalysisIntegrationMethodMemberType
    NewmarkBeta = 1  # EvaluationParametersAnalysisIntegrationMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EvaluationParameters(NXOpen.TaggedObject):
    """
    Represents the evaluation parameters for a response simulation meta solution   
    
    Not support KF.
    
    .. versionadded:: NX6.0.0
    """
    
    class AnalysisIntegrationMethod():
        """
        the integration method used for transient analysis 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DuhameldIntegral", " - "
           "NewmarkBeta", " - "
        """
        DuhameldIntegral = 0  # EvaluationParametersAnalysisIntegrationMethodMemberType
        NewmarkBeta = 1  # EvaluationParametersAnalysisIntegrationMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    HypermatrixBufferSize: int = ...
    """
    Returns or sets  the buffer allocated for Hypermatrix files 
    
    <hr>
    
    Getter Method
    
    Signature ``HypermatrixBufferSize`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``HypermatrixBufferSize`` 
    
    :param bufferSize: 
    :type bufferSize: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    IntegrationMethod: EvaluationParametersAnalysisIntegrationMethod = ...
    """
    Returns or sets  the integration method used for transient analysis 
    
    <hr>
    
    Getter Method
    
    Signature ``IntegrationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationParametersAnalysisIntegrationMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``IntegrationMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationParametersAnalysisIntegrationMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    MaxArraySize: int = ...
    """
    Returns or sets  the dynamic storage array size allocated for RS evaluations 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxArraySize`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``MaxArraySize`` 
    
    :param maxArraySize: 
    :type maxArraySize: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    MinDampingStatus: bool = ...
    """
    Returns or sets  the minimum damping ratio status 
    
    <hr>
    
    Getter Method
    
    Signature ``MinDampingStatus`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``MinDampingStatus`` 
    
    :param dampingStatus: 
    :type dampingStatus: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ZeroMeanCorrection: bool = ...
    """
    Returns or sets  the time-domain integration of acceleration excitations,
    used in evaluating time responses to acceleration loads.  
    
    false: no correction, meaning that "rigid drifting" shows in the
    displacement response when an acceleration excitation is applied;
    true:  the software corrects for drifting by assuming a zero mean. Rigid drifting is filtered
    out based on a numerical integration that does not assume an initial condition.
    
    <hr>
    
    Getter Method
    
    Signature ``ZeroMeanCorrection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ZeroMeanCorrection`` 
    
    :param correctionValue: 
    :type correctionValue: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: EvaluationParameters = ...  # unknown typename


class Manager():
    """
    Represents the Response Dynamics manager to contain all Response Dynamics objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.SimSimulation`
    
    .. versionadded:: NX5.0.0
    """
    Solutions: SolutionCollection = ...
    """
    Returns the Response Dynamics solution collection belonging to this sim part 
    
    Signature ``Solutions`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.SolutionCollection`
    """
    Events: RSEventCollection = ...
    """
    Returns the Response Dynamics event collection belonging to this sim part 
    
    Signature ``Events`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSEventCollection`
    """
    Excitations: ExcitationCollection = ...
    """
    Returns the Response Dynamics excitation collection belonging to this sim part 
    
    Signature ``Excitations`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ExcitationCollection`
    """
    EvaluationSettingManager: EvaluationSettingManager = ...
    """
    Returns the Response Dynamics evaluation data manager belonging to this sim part 
    
    Signature ``EvaluationSettingManager`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager`
    """
    Sensors: SensorCollection = ...
    """
    Returns the Response Dynamics sensor collection belonging to this sim part 
    
    Signature ``Sensors`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.SensorCollection`
    """
    StrainGages: StrainGageCollection = ...
    """
    Returns the Response Dynamics strain gage collection belonging to this sim part 
    
    Signature ``StrainGages`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageCollection`
    """


class DistributedLoadExcitationBuilder(ExcitationBuilder):
    """
    Represents the manager to :py:class:`NXOpen.CAE.ResponseSimulation.DistributedLoadExcitation`.  
    
    The object of type :py:class:`NXOpen.CAE.ResponseSimulation.DistributedLoadExcitation`
    can only be created or edited through this class.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.ExcitationCollection.CreateDistributedLoadExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    ExcitationFunction: FunctionComponentData = ...
    """
    Returns  the magnitude function 
    
    <hr>
    
    Getter Method
    
    Signature ``ExcitationFunction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FunctionComponentData` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: DistributedLoadExcitationBuilder = ...  # unknown typename


class SensorResultTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SensorResultType():
    """
    Specifies the result type of Sensor 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Displacement", " - "
       "Velocity", " - "
       "Acceleration", " - "
       "ReactionForce", " - "
    """
    Displacement = 0  # SensorResultTypeMemberType
    Velocity = 1  # SensorResultTypeMemberType
    Acceleration = 2  # SensorResultTypeMemberType
    ReactionForce = 3  # SensorResultTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LcrResultsEvaluationSettingBuilder(RmsResultsEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSetting` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateLcrResultsEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    CrossingLevel: float = ...
    """
    Returns or sets  the crossing level 
    
    <hr>
    
    Getter Method
    
    Signature ``CrossingLevel`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX8.5.0
       Use :py:meth:`CrossingLevelExpression`` instead.
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``CrossingLevel`` 
    
    :param crossingLevel: 
    :type crossingLevel: float 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX8.5.0
       Use :py:meth:`CrossingLevelExpression`` instead.
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    CrossingLevelExpression: NXOpen.Expression = ...
    """
    Returns  the crossing level expression
    
    <hr>
    
    Getter Method
    
    Signature ``CrossingLevelExpression`` 
    
    :returns:  crossing level expression  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: LcrResultsEvaluationSettingBuilder = ...  # unknown typename


class NodalFunctionEvaluationSetting(FunctionEvaluationSetting):
    """
    Represents the parameters setting of nodal function response evaluation.  
    
    Available to all
    kinds of event type 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: NodalFunctionEvaluationSetting = ...  # unknown typename


class DataLocationBeamMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DataLocationBeam():
    """
    Specifies the location for beam 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "C", " - "
       "D", " - "
       "E", " - "
       "F", " - "
    """
    C = 0  # DataLocationBeamMemberType
    D = 1  # DataLocationBeamMemberType
    E = 2  # DataLocationBeamMemberType
    F = 3  # DataLocationBeamMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DataLocationShellMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DataLocationShell():
    """
    Specifies the location for shell 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Top", " - "
       "Bottom", " - "
       "Middle", " - "
    """
    Top = 0  # DataLocationShellMemberType
    Bottom = 1  # DataLocationShellMemberType
    Middle = 2  # DataLocationShellMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DataLocationElementMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DataLocationElement():
    """
    Specifies the element location for element 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Both", " - "
       "Centroid", " - "
       "Corners", " - "
    """
    Both = 0  # DataLocationElementMemberType
    Centroid = 1  # DataLocationElementMemberType
    Corners = 2  # DataLocationElementMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DataLocation(NXOpen.TaggedObject):
    """
    Represents the data location to perform evaluation   
    
    .. versionadded:: NX5.0.0
    """
    
    class Beam():
        """
        Specifies the location for beam 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "C", " - "
           "D", " - "
           "E", " - "
           "F", " - "
        """
        C = 0  # DataLocationBeamMemberType
        D = 1  # DataLocationBeamMemberType
        E = 2  # DataLocationBeamMemberType
        F = 3  # DataLocationBeamMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Shell():
        """
        Specifies the location for shell 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Top", " - "
           "Bottom", " - "
           "Middle", " - "
        """
        Top = 0  # DataLocationShellMemberType
        Bottom = 1  # DataLocationShellMemberType
        Middle = 2  # DataLocationShellMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Element():
        """
        Specifies the element location for element 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Both", " - "
           "Centroid", " - "
           "Corners", " - "
        """
        Both = 0  # DataLocationElementMemberType
        Centroid = 1  # DataLocationElementMemberType
        Corners = 2  # DataLocationElementMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    BeamLocation: DataLocationBeam = ...
    """
    Returns or sets  the method to define frequency
    
    <hr>
    
    Getter Method
    
    Signature ``BeamLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DataLocationBeam` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``BeamLocation`` 
    
    :param beamLocation: 
    :type beamLocation: :py:class:`NXOpen.CAE.ResponseSimulation.DataLocationBeam` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ElementLocation: DataLocationElement = ...
    """
    Returns or sets  the element location.  
    
    Only available when stress and strain is defined
    by :py:class:`CAE.ResponseSimulation.FrequencyDefinitionDefinition.Range <CAE.ResponseSimulation.FrequencyDefinitionDefinition>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ElementLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DataLocationElement` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ElementLocation`` 
    
    :param elementLocation: 
    :type elementLocation: :py:class:`NXOpen.CAE.ResponseSimulation.DataLocationElement` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    LayerSelection: int = ...
    """
    Returns or sets  the end value of frequency range.  
    
    Only available when the frequency is defined 
    by :py:class:`CAE.ResponseSimulation.FrequencyDefinitionDefinition.Range <CAE.ResponseSimulation.FrequencyDefinitionDefinition>` 
    
    <hr>
    
    Getter Method
    
    Signature ``LayerSelection`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``LayerSelection`` 
    
    :param layerNumber: 
    :type layerNumber: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ShellLocation: DataLocationShell = ...
    """
    Returns or sets  the start value of frequency range.  
    
    Only available when the frequency is defined
    by :py:class:`CAE.ResponseSimulation.FrequencyDefinitionDefinition.Range <CAE.ResponseSimulation.FrequencyDefinitionDefinition>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ShellLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DataLocationShell` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ShellLocation`` 
    
    :param shellLocation: 
    :type shellLocation: :py:class:`NXOpen.CAE.ResponseSimulation.DataLocationShell` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: DataLocation = ...  # unknown typename


class StrainGageEvaluationSettingBuilder(FunctionEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSetting` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateStrainGageEvaluationSettingBuilder`
    
    Default values.
    
    ==============  ===========
    Property        Value
    ==============  ===========
    DataComponent   AllXyPlane 
    ==============  ===========
    
    .. versionadded:: NX6.0.0
    """
    DataComponent: DirectionDataComponent = ...
    """
    Returns or sets  the data component of strain gage evaluation results
    
    <hr>
    
    Getter Method
    
    Signature ``DataComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``DataComponent`` 
    
    :param dataComponent: 
    :type dataComponent: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    StrainGage: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the destination strain Gages 
    
    <hr>
    
    Getter Method
    
    Signature ``StrainGage`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: StrainGageEvaluationSettingBuilder = ...  # unknown typename


class CSDExcitationCorrelationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CSDExcitationCorrelationType():
    """
    Represents the correlation type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PhaseAngle", " - "
       "TimeDelay", " - "
    """
    PhaseAngle = 0  # CSDExcitationCorrelationTypeMemberType
    TimeDelay = 1  # CSDExcitationCorrelationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CSDExcitation(Excitation):
    """
    Represents an CSD excitation.  
    
    CSD excitation could only be used by CSD event. 
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.CSDExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class CorrelationType():
        """
        Represents the correlation type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PhaseAngle", " - "
           "TimeDelay", " - "
        """
        PhaseAngle = 0  # CSDExcitationCorrelationTypeMemberType
        TimeDelay = 1  # CSDExcitationCorrelationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Null: CSDExcitation = ...  # unknown typename


class CsdEvaluationSetting(FunctionEvaluationSetting):
    """
    Represents the class of evaluation setting for CSD   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.CsdEvaluationSettingBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: CsdEvaluationSetting = ...  # unknown typename


class RotationalNodalFunctionExcitationBuilder(NodalFunctionExcitationBuilder):
    """
    Represents the manager to :py:class:`NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitation`.  
    
    The objects of :py:class:`NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitation` 
    can be created or edited on through this class 
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.ExcitationCollection.CreateRotationalNodalFunctionExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    FunctionComponentRx: FunctionComponentData = ...
    """
    Returns  the function component of Rx direction  
    
    <hr>
    
    Getter Method
    
    Signature ``FunctionComponentRx`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FunctionComponentData` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    FunctionComponentRy: FunctionComponentData = ...
    """
    Returns  the function component of Ry direction 
    
    <hr>
    
    Getter Method
    
    Signature ``FunctionComponentRy`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FunctionComponentData` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    FunctionComponentRz: FunctionComponentData = ...
    """
    Returns  the function component of Rz direction 
    
    <hr>
    
    Getter Method
    
    Signature ``FunctionComponentRz`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FunctionComponentData` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: RotationalNodalFunctionExcitationBuilder = ...  # unknown typename


class VelocityImpactParametersStartPositionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VelocityImpactParametersStartPositionType():
    """
    the calculation start position for impact 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AtDrop", "Calculation starts from the drop time"
       "BeforeImpact", "Calculation ends at the impact time"
       "AtImpact", "Calculation starts from the impact time"
    """
    AtDrop = 0  # VelocityImpactParametersStartPositionTypeMemberType
    BeforeImpact = 1  # VelocityImpactParametersStartPositionTypeMemberType
    AtImpact = 2  # VelocityImpactParametersStartPositionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class VelocityImpactParameters(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactParameters`
    
    .. versionadded:: NX6.0.0
    """
    
    class StartPositionType():
        """
        the calculation start position for impact 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AtDrop", "Calculation starts from the drop time"
           "BeforeImpact", "Calculation ends at the impact time"
           "AtImpact", "Calculation starts from the impact time"
        """
        AtDrop = 0  # VelocityImpactParametersStartPositionTypeMemberType
        BeforeImpact = 1  # VelocityImpactParametersStartPositionTypeMemberType
        AtImpact = 2  # VelocityImpactParametersStartPositionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Validate(self) -> bool:
        """
        Validate whether the inputs to the component are sufficient for 
        commit to be called.  
        
        If the component is not in a state to commit
        then an exception is thrown.  For example, if the component requires
        you to set some property, this method will throw an exception if
        you haven't set it.  This method throws a not-yet-implemented
        NXException for some components.
        
        Signature ``Validate()`` 
        
        :returns:  Was self validation successful  
        :rtype: bool 
        
        .. versionadded:: NX3.0.1
        
        License requirements: None.
        """
        ...
    
    DropHeight: NXOpen.Expression = ...
    """
    Returns  the drop height.  
    
    Not available if the impact excitation is of type :py:class:` 
    CAE.ResponseSimulation.VelocityImpactExcitationBuilderImpactMethodType.ConstantVelocity
    < 
    CAE.ResponseSimulation.VelocityImpactExcitationBuilderImpactMethodType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``DropHeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    PulseDuration: NXOpen.Expression = ...
    """
    Returns  the impact pulse duration 
    
    <hr>
    
    Getter Method
    
    Signature ``PulseDuration`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    StartPosition: VelocityImpactParametersStartPositionType = ...
    """
    Returns or sets  the start position 
    
    <hr>
    
    Getter Method
    
    Signature ``StartPosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactParametersStartPositionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StartPosition`` 
    
    :param mStartPosition: 
    :type mStartPosition: :py:class:`NXOpen.CAE.ResponseSimulation.VelocityImpactParametersStartPositionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    TimeStep: NXOpen.Expression = ...
    """
    Returns  the time step.  
    
    The value must be larger than 1/20 of the impact pulse duration 
    
    <hr>
    
    Getter Method
    
    Signature ``TimeStep`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Velocity: NXOpen.Expression = ...
    """
    Returns  the velocity 
    
    <hr>
    
    Getter Method
    
    Signature ``Velocity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: VelocityImpactParameters = ...  # unknown typename


class RSDisplayObject(NXOpen.NXObject):
    """
    Represents a BC display attributes 
    
    .. versionadded:: NX6.0.0
    """
    DisplayName: bool = ...
    """
    Returns or sets  the true/false flag based on whether the name of the BC is
    displayed in the graphics window 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayName`` 
    
    :returns:  true when the name is displayed, false otherwise  
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayName`` 
    
    :param nameFlag:  true when the name should be displayed, false otherwise  
    :type nameFlag: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Scale: NXOpen.Expression = ...
    """
    Returns  the RS display scaling factor
    this option specifies the scale of the graphic symbol relative to the size of the bounding box of the RS OBject.  
    
    scale -> 0 
    
    <hr>
    
    Getter Method
    
    Signature ``Scale`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: RSDisplayObject = ...  # unknown typename


class FrfEvaluationSetting(ModalResultsEvaluationSetting):
    """
    Represents the parameters setting for FRF results evaluation   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.FrfEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: FrfEvaluationSetting = ...  # unknown typename


class ElementalFunctionEvaluationSettingBuilder(FunctionEvaluationSettingBuilder):
    """
    This is a manager to the :py:class:`NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSetting` class.  
    
    Object of type :py:class:`NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSetting` can be 
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.EvaluationSettingManager.CreateElementalFunctionEvaluationSettingBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def GetDestinationElements(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Returns the destination elements  
        
        Signature ``GetDestinationElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    
    def SetDestinationElements(self, destinationElement: 'list[NXOpen.CAE.FEElement]') -> None:
        """
        Sets the destination elements 
        
        Signature ``SetDestinationElements(destinationElement)`` 
        
        :param destinationElement: 
        :type destinationElement: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    BeamDataLocation: ElementalFunctionEvalBeamLocation = ...
    """
    Returns or sets  the data location of beam element.  
    
    For more information about beam data location,
    see the Response Simulatin section of the Gateway help 
    
    <hr>
    
    Getter Method
    
    Signature ``BeamDataLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ElementalFunctionEvalBeamLocation` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``BeamDataLocation`` 
    
    :param beamLocation: 
    :type beamLocation: :py:class:`NXOpen.CAE.ResponseSimulation.ElementalFunctionEvalBeamLocation` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    CoordinateSystem: CoordinateSystem = ...
    """
    Returns or sets  the coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.CoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``CoordinateSystem`` 
    
    :param coordinateSystem: 
    :type coordinateSystem: :py:class:`NXOpen.CAE.ResponseSimulation.CoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    DataComponent: DirectionDataComponent = ...
    """
    Returns or sets  the data component of direction 
    
    <hr>
    
    Getter Method
    
    Signature ``DataComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``DataComponent`` 
    
    :param dataComponent: 
    :type dataComponent: :py:class:`NXOpen.CAE.ResponseSimulation.DirectionDataComponent` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ElementLocation: ElementLocation = ...
    """
    Returns or sets  the evaluation location of element.  
    
    <hr>
    
    Getter Method
    
    Signature ``ElementLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ElementLocation` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ElementLocation`` 
    
    :param elementLocation: 
    :type elementLocation: :py:class:`NXOpen.CAE.ResponseSimulation.ElementLocation` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    ShellEvaluationLocation: ShellElementEvaluationLocation = ...
    """
    Returns or sets  the evaluation location of shell element.  
    
    <hr>
    
    Getter Method
    
    Signature ``ShellEvaluationLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.ShellElementEvaluationLocation` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``ShellEvaluationLocation`` 
    
    :param shellLocation: 
    :type shellLocation: :py:class:`NXOpen.CAE.ResponseSimulation.ShellElementEvaluationLocation` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: ElementalFunctionEvaluationSettingBuilder = ...  # unknown typename


class DynamicEvaluationOutputSettings(NXOpen.TaggedObject):
    """
    Represents the output setting for dynamic response evaluation  
    
    .. versionadded:: NX5.0.0
    """
    PreviewOption: bool = ...
    """
    Returns or sets  the preview option.  
    
    If true, the evaluation results will be previewed by plot and not saved to disk until
    you confirm to save them 
    
    <hr>
    
    Getter Method
    
    Signature ``PreviewOption`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``PreviewOption`` 
    
    :param previewOption: 
    :type previewOption: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    RecordPrefix: str = ...
    """
    Returns or sets  the prefix of evaluation results record name 
    
    <hr>
    
    Getter Method
    
    Signature ``RecordPrefix`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``RecordPrefix`` 
    
    :param recordPrefix: 
    :type recordPrefix: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: DynamicEvaluationOutputSettings = ...  # unknown typename


class Sensor(NXOpen.DisplayableObject):
    """
    Represents a :py:class:`NXOpen.CAE.ResponseSimulation.Sensor`
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.ResponseSimulation.SensorBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def GetDisplayAttribute(self) -> RSDisplayObject:
        """
        Get display attribute of sensor  
        
        Signature ``GetDisplayAttribute()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.RSDisplayObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_response_anlys ("NX Response Analysis")
        """
        ...
    
    Null: Sensor = ...  # unknown typename


class RotationalDDAMExcitationBuilder(DDAMExcitationBuilder):
    """
    Represents the manager to :py:class:`CAE.ResponseSimulation.DDAMExcitation`.  
    
    The object of type :py:class:`CAE.ResponseSimulation.DDAMExcitation` can only
    be created or edited through this class. 
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.ExcitationCollection.CreateRotationalDdamExcitationBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: RotationalDDAMExcitationBuilder = ...  # unknown typename


class StaticLoadExcitationBuilder(ExcitationBuilder):
    """
    Represents the manager to :py:class:`NXOpen.CAE.ResponseSimulation.StaticLoadExcitation`.  
    
    The object of type :py:class:`NXOpen.CAE.ResponseSimulation.StaticLoadExcitation`
    can only be created or edited through this class.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ResponseSimulation.ExcitationCollection.CreateStaticLoadExcitationBuilder`
    
    .. versionadded:: NX6.0.0
    """
    ExcitationFunction: FunctionComponentData = ...
    """
    Returns  the magnitude function 
    
    <hr>
    
    Getter Method
    
    Signature ``ExcitationFunction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResponseSimulation.FunctionComponentData` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: StaticLoadExcitationBuilder = ...  # unknown typename


class RSEventOutputSetting(NXOpen.TaggedObject):
    """
    Reprensents the output setting for an event   
    
    .. versionadded:: NX5.0.0
    """
    FemGeometrySaveOption: bool = ...
    """
    Returns or sets  the option to save FEM information with evaluation results.  
    
    The option could not be
    changed after the event is created. 
    
    <hr>
    
    Getter Method
    
    Signature ``FemGeometrySaveOption`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    
    <hr>
    
    Setter Method
    
    Signature ``FemGeometrySaveOption`` 
    
    :param saveFemGeometry: 
    :type saveFemGeometry: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_response_anlys ("NX Response Analysis")
    """
    Null: RSEventOutputSetting = ...  # unknown typename


