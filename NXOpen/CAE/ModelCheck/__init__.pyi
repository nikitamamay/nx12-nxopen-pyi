# module 'NXOpen.CAE.ModelCheck'
#
# Automatically generated 2025-06-09T14:38:44.527382
#

import typing

import NXOpen
import NXOpen.CAE



class ElementTestResult(NXOpen.TransientObject):
    """
    Represents quality checking result for an element.  
    
    To obtain an instance of this class use CAE.ModelCheck.ElementQualityCheckResults.GetElementTestResults
    
    .. versionadded:: NX8.5.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTestResults(self) -> 'list[TestResult]':
        """
        Returns the quality test results of this element  
        
        Signature ``GetTestResults()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.ModelCheck.TestResult` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    OverallResult: TestValueTypesResult = ...
    """
    Returns  the overrall result of this element.  
    
    <hr>
    
    Getter Method
    
    Signature ``OverallResult`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesResult` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """


class FaceClearanceCheckBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.FaceClearanceCheckBuilder` to perform polygon face
    interference or clearance check.  
    
    You can do the check by :py:meth:`Builder.Commit` or 
    :py:meth:`NXOpen.CAE.ModelCheck.FaceClearanceCheckBuilder.DoCheck`. :py:meth:`Builder.Commit`
    performs the check and displays the failed faces in graphics window. :py:meth:`NXOpen.CAE.ModelCheck.FaceClearanceCheckBuilder.DoCheck`
    performs the check and if faces are detected violating the check, returns the output group containing the failed faces.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateFaceClearanceCheckBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    def DoCheck(self) -> NXOpen.CAE.CaeGroup:
        """
        Perform the clearance check.  
        
        All polygon faces on the current display are considered for
        the check. If polygon faces are detected as intersecting or violating the given clearance, they
        are placed in a group, which would be returned  
        
        Signature ``DoCheck()`` 
        
        :returns:  the group contains the failed faces  
        :rtype: :py:class:`NXOpen.CAE.CaeGroup` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Clearance: NXOpen.Expression = ...
    """
    Returns  the clearance.  
    
    If the clearance value is zero, an intersection check between faces will be
    performed. If the clearance value is non-zero, a clearance check will be performed. If a negative
    non-zero clearance is set, the absolute value will be used 
    
    <hr>
    
    Getter Method
    
    Signature ``Clearance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: FaceClearanceCheckBuilder = ...  # unknown typename


class AlignShellElementNormalBuilderConnectedElementScopeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AlignShellElementNormalBuilderConnectedElementScope():
    """
    the options to define the connection scope to the seed element for model checking 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SeedMesh", "Limits check to only those shell elements in the mesh that contains the Seed Element"
       "AllVisible", "Limits check to only those shell elements which are connected to the Seed Element and are currently visible"
       "UserSpecified", "Limits check to only those shell elements specified in :py:meth:`NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.UserSpecifiedConnectElements`"
    """
    SeedMesh = 0  # AlignShellElementNormalBuilderConnectedElementScopeMemberType
    AllVisible = 1  # AlignShellElementNormalBuilderConnectedElementScopeMemberType
    UserSpecified = 2  # AlignShellElementNormalBuilderConnectedElementScopeMemberType
    
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
    


class AlignShellElementNormalBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder` builder used to align the normals of
    connected shell elements with a seed shell element.  
    
    You can align the normals by executing either 
    :py:meth:`Builder.Commit` or :py:meth:`NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.AlignNormals`.
    The difference between these two methods is :py:meth:`Builder.Commit` aligns the normals
    and updates normal display, but it does not return the elements that have changed normals.
    :py:meth:`NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.AlignNormals` aligns the normals
    and returns the elements that have changed normals. Both of the methods are only available in fem context.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateAlignShellElementNormalBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class ConnectedElementScope():
        """
        the options to define the connection scope to the seed element for model checking 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SeedMesh", "Limits check to only those shell elements in the mesh that contains the Seed Element"
           "AllVisible", "Limits check to only those shell elements which are connected to the Seed Element and are currently visible"
           "UserSpecified", "Limits check to only those shell elements specified in :py:meth:`NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.UserSpecifiedConnectElements`"
        """
        SeedMesh = 0  # AlignShellElementNormalBuilderConnectedElementScopeMemberType
        AllVisible = 1  # AlignShellElementNormalBuilderConnectedElementScopeMemberType
        UserSpecified = 2  # AlignShellElementNormalBuilderConnectedElementScopeMemberType
        
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
        
    
    
    def FindAllVisibleConnectedElements(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Finds all visible elements connected with the seed element  
        
        Signature ``FindAllVisibleConnectedElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayNormals(self) -> None:
        """
        Display element normals for connected elements, which are to be aligned with seed element normal 
        
        Signature ``DisplayNormals()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def AlignNormals(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Aligns the normals of elements connected to the seed element.  
        
        Returns the elements
        that have had the normals successfully reversed. This method will only reverse
        the normals for shell elements in the current work fem part.
        
        Signature ``AlignNormals()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    ElementConnectScope: AlignShellElementNormalBuilderConnectedElementScope = ...
    """
    Returns or sets  the option to indicate how to define connected elements for checking 
    
    <hr>
    
    Getter Method
    
    Signature ``ElementConnectScope`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilderConnectedElementScope` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ElementConnectScope`` 
    
    :param connectScope: 
    :type connectScope: :py:class:`NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilderConnectedElementScope` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ReverseSeedNormal: bool = ...
    """
    Returns or sets  the option indicating whether to reverse element normals so that they are aligned with the seed element 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseSeedNormal`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseSeedNormal`` 
    
    :param seedNormalToBeReversed: 
    :type seedNormalToBeReversed: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    SeedElement: NXOpen.CAE.FEElement = ...
    """
    Returns or sets  the seed element 
    
    <hr>
    
    Getter Method
    
    Signature ``SeedElement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.FEElement` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeedElement`` 
    
    :param seedElement: 
    :type seedElement: :py:class:`NXOpen.CAE.FEElement` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    UserSpecifiedConnectElements: NXOpen.CAE.SelectElementsBuilder = ...
    """
    Returns  the user specified connected elements to be aligned with seed element 
    
    <hr>
    
    Getter Method
    
    Signature ``UserSpecifiedConnectElements`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SelectElementsBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: AlignShellElementNormalBuilder = ...  # unknown typename


class ISelectionBuilder():
    """
    Represents the model check selection builder  
    
    This is an interface, and cannot be instantiated.
    
    .. versionadded:: NX11.0.1
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class DuplicateNodesCheckBuilderDisplaySettings_Struct():
    """
    Represents the display settings data .  
    
    Constructor: 
    NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.DisplaySettings()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    ShowDuplicateNodes: bool = ...
    """
    Whether to show duplicate nodes 
    <hr>
    
    Field Value
    Type:bool
    """
    ShowMergedNodeLabels: bool = ...
    """
    Whether to show merged node labels 
    <hr>
    
    Field Value
    Type:bool
    """
    ShowRetainedNodeLabels: bool = ...
    """
    Whether to show retained node labels 
    <hr>
    
    Field Value
    Type:bool
    """
    KeepNodesColor: NXOpen.NXColor = ...
    """
    The kept nodes display color 
    <hr>
    
    Field Value
    Type:Id
    """
    MergeNodesColor: NXOpen.NXColor = ...
    """
    The merged nodes display color 
    <hr>
    
    Field Value
    Type:Id
    """
    UnableToMergeNodesColor: NXOpen.NXColor = ...
    """
    Field Value
    Type:Id
    """


class ITestValue():
    """
    Represents the quality check criteria value settings  
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX8.5.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ElementSpecificTestValue(NXOpen.NXObject, ITestValue):
    """
    Represents the quality setting for a specfied element reference  
    
    Not to support KF
    
    .. versionadded:: NX8.5.0
    """
    
    def GetTestType(self) -> TestValueTypesTestType:
        """
        Returns the test type  
        
        Signature ``GetTestType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesTestType` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetValidator(self) -> TestValueTypesValidator:
        """
        Returns the validator type  
        
        Signature ``GetValidator()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesValidator` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def HasCriteriaValue(self) -> bool:
        """
        Tells whether there is criteria value associated with this test  
        
        Signature ``HasCriteriaValue()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCriteriaValue(self, criteriaType: TestValueTypesCriteriaType) -> tuple:
        """
        Returns the criteria value.  
        
        An exception will be thrown if there is no criteria value associated with this test  
        
        Signature ``GetCriteriaValue(criteriaType)`` 
        
        :param criteriaType: 
        :type criteriaType: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesCriteriaType` 
        :returns: a tuple 
        :rtype: A tuple consisting of (unit, criteriaValue). unit is a :py:class:`NXOpen.Unit`. criteriaValue is a float. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetCriteriaValue(self, criteriaType: TestValueTypesCriteriaType, criteriaValue: float, unit: NXOpen.Unit) -> None:
        """
        Sets the criteria value. An exception will be thrown if there is no criteria value associated with this test 
        
        Signature ``SetCriteriaValue(criteriaType, criteriaValue, unit)`` 
        
        :param criteriaType: 
        :type criteriaType: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesCriteriaType` 
        :param criteriaValue: 
        :type criteriaValue: float 
        :param unit: 
        :type unit: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetCriteriaValue(self, criteriaType: TestValueTypesCriteriaType, criteriaValue: str, unit: NXOpen.Unit) -> None:
        """
        Sets the criteria value. An exception will be thrown if there is no criteria value associated with this test 
        
        Signature ``SetCriteriaValue(criteriaType, criteriaValue, unit)`` 
        
        :param criteriaType: 
        :type criteriaType: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesCriteriaType` 
        :param criteriaValue: 
        :type criteriaValue: str 
        :param unit: 
        :type unit: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetIsSolverSpecificTest(self) -> tuple:
        """
        To know whether this quality test is a solver specific test and a system test  
        
        Signature ``GetIsSolverSpecificTest()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (isSolverSpecificTest, isSystemTest). isSolverSpecificTest is a bool. isSystemTest is a bool. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetElementReferences(self) -> 'list[TestValueTypesElementReference_Struct]':
        """
        Returns the element reference definitions associated with this test  
        
        Signature ``GetElementReferences()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesElementReference_Struct` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetToCustomerDefault(self) -> None:
        """
        Reset as customer default setting 
        
        Signature ``ResetToCustomerDefault()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    DoTest: bool = ...
    """
    Returns or sets  an option value indicating whether to do element quality check for this test  
    
    <hr>
    
    Getter Method
    
    Signature ``DoTest`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DoTest`` 
    
    :param doTest: 
    :type doTest: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: ElementSpecificTestValue = ...  # unknown typename


class ElementQualityCheckBuilderReportFormatMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElementQualityCheckBuilderReportFormat():
    """
    indicates how to generate report 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Does not generate report"
       "Failed", "Only lists check results for elements with error results in the report"
       "Warning", "Only lists check results for elements with warning results in the report"
       "FailedAndWarning", "Lists check results for elements with both error and warning results in the report"
       "All", "Lists check results for all elements"
    """
    NotSet = 0  # ElementQualityCheckBuilderReportFormatMemberType
    Failed = 1  # ElementQualityCheckBuilderReportFormatMemberType
    Warning = 2  # ElementQualityCheckBuilderReportFormatMemberType
    FailedAndWarning = 3  # ElementQualityCheckBuilderReportFormatMemberType
    All = 4  # ElementQualityCheckBuilderReportFormatMemberType
    
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
    


class ElementQualityCheckBuilderOutputElementsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElementQualityCheckBuilderOutputElements():
    """
    indicates how to create output group 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Output nothing"
       "Failed", "Creates OUTPUT group with failed elements"
       "Warning", "Creates OUTPUT group with warning elements"
       "FailedAndWarning", "Creates OUTPUT group with both warning and failed elements"
    """
    NotSet = 0  # ElementQualityCheckBuilderOutputElementsMemberType
    Failed = 1  # ElementQualityCheckBuilderOutputElementsMemberType
    Warning = 2  # ElementQualityCheckBuilderOutputElementsMemberType
    FailedAndWarning = 3  # ElementQualityCheckBuilderOutputElementsMemberType
    
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
    


class ElementQualityCheckBuilder(NXOpen.Builder, ISelectionBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder` to
    perform quality checking on the candidate elements.  
    
    Set the properties of the 
    :py:class:`NXOpen.CAE.ModelCheck.ElementQualitySetting` instance for the
    current solver language in the CAE part to define the specific quality checks to perform. 
    
    Those elements with failed quality check results will be displayed according to the display setting
    :py:meth:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ShowFailedElementsLabel`` and 
    :py:meth:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.FailedElementsColor``.
    
    The report will be generated according to :py:meth:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ElementReportFormat``
    
    You can do element quality check by :py:meth:`Builder.Commit` and 
    :py:meth:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ExecuteCheck`. 
    :py:meth:`Builder.Commit` performs the check, displays the failed elements and generates the report 
    in a listing window. But :py:meth:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder` just performs the check and
    returns the check result :py:class:`NXOpen.CAE.ModelCheck.ElementQualityCheckResults`
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateElementQualityCheckBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class ReportFormat():
        """
        indicates how to generate report 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Does not generate report"
           "Failed", "Only lists check results for elements with error results in the report"
           "Warning", "Only lists check results for elements with warning results in the report"
           "FailedAndWarning", "Lists check results for elements with both error and warning results in the report"
           "All", "Lists check results for all elements"
        """
        NotSet = 0  # ElementQualityCheckBuilderReportFormatMemberType
        Failed = 1  # ElementQualityCheckBuilderReportFormatMemberType
        Warning = 2  # ElementQualityCheckBuilderReportFormatMemberType
        FailedAndWarning = 3  # ElementQualityCheckBuilderReportFormatMemberType
        All = 4  # ElementQualityCheckBuilderReportFormatMemberType
        
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
        
    
    
    class OutputElements():
        """
        indicates how to create output group 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Output nothing"
           "Failed", "Creates OUTPUT group with failed elements"
           "Warning", "Creates OUTPUT group with warning elements"
           "FailedAndWarning", "Creates OUTPUT group with both warning and failed elements"
        """
        NotSet = 0  # ElementQualityCheckBuilderOutputElementsMemberType
        Failed = 1  # ElementQualityCheckBuilderOutputElementsMemberType
        Warning = 2  # ElementQualityCheckBuilderOutputElementsMemberType
        FailedAndWarning = 3  # ElementQualityCheckBuilderOutputElementsMemberType
        
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
        
    
    
    def ExecuteCheck(self) -> ElementQualityCheckResults:
        """
        Execute element quality checking for :py:meth:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.SelectionList`
        and returns the check results.  
        
        You could also use :py:meth:`Builder.Commit` to do
        the checking. :py:meth:`Builder.Commit` only executes the checking, displaying failed elements and
        generating report, but does not return the results
        
        Signature ``ExecuteCheck()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementQualityCheckResults` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    ElementReportFormat: ElementQualityCheckBuilderReportFormat = ...
    """
    Returns or sets  the report style 
    
    <hr>
    
    Getter Method
    
    Signature ``ElementReportFormat`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilderReportFormat` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ElementReportFormat`` 
    
    :param reportElements: 
    :type reportElements: :py:class:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilderReportFormat` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ElementsOutputOption: ElementQualityCheckBuilderOutputElements = ...
    """
    Returns or sets  the element output options 
    
    <hr>
    
    Getter Method
    
    Signature ``ElementsOutputOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilderOutputElements` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ElementsOutputOption`` 
    
    :param outputElements: 
    :type outputElements: :py:class:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilderOutputElements` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    FailedElementsColor: NXOpen.NXColor = ...
    """
    Returns or sets  the display color of failed elements 
    
    <hr>
    
    Getter Method
    
    Signature ``FailedElementsColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FailedElementsColor`` 
    
    :param color: 
    :type color: Id 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    NumberFormat: NXOpen.CAE.NumberFormat = ...
    """
    Returns  the number format option 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberFormat`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.NumberFormat` 
    
    .. versionadded:: NX11.0.2
    
    License requirements: None.
    """
    SelectionList: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects to be checked.  
    
    The objects must be :py:class:`NXOpen.CAE.Mesh` or
    :py:class:`NXOpen.CAE.FEElement` 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowFailedElementsLabel: bool = ...
    """
    Returns or sets  the value indicating whether to show label for those failed elements 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFailedElementsLabel`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFailedElementsLabel`` 
    
    :param showFailedElementsLabel: 
    :type showFailedElementsLabel: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    WarningElementsColor: NXOpen.NXColor = ...
    """
    Returns or sets  the display color of warning elements 
    
    <hr>
    
    Getter Method
    
    Signature ``WarningElementsColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WarningElementsColor`` 
    
    :param color: 
    :type color: Id 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    CheckScopeOption: CheckScope = ...
    """
    Returns or sets  the check scope setting 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckScopeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckScopeOption`` 
    
    :param scope: 
    :type scope: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: ElementQualityCheckBuilder = ...  # unknown typename


class CheckScopeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CheckScope():
    """
    the option indicates the check scope for a model check command 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Displayed", "check all displayed elements or nodes"
       "Selected", "check selected elements or nodes"
    """
    Displayed = 0  # CheckScopeMemberType
    Selected = 1  # CheckScopeMemberType
    
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
    


class ElementQualityCheckResultsTestSummary_Struct():
    """
    Reprents the summary data of a specified quality checking test type .  
    
    Constructor: 
    NXOpen.CAE.ModelCheck.ElementQualityCheckResults.TestSummary()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    TestType: TestValueTypesTestType = ...
    """
    the test type
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.CAE.ModelCheck.TestValueTypesTestType`
    """
    WorstTestValue: float = ...
    """
    the worst test value of the specified test within all checked elements.  
    
    which is only availabe for the test has a test value 
    <hr>
    
    Field Value
    Type:float
    """
    HasTestValue: bool = ...
    """
    indicates whether the test has a test value.  
    
    If false, there is no test value associcated
    with this test 
    <hr>
    
    Field Value
    Type:bool
    """
    TestCount: int = ...
    """
    indicates the total number of elements tested for this test 
    <hr>
    
    Field Value
    Type:int
    """
    ErrorCount: int = ...
    """
    the count of elements with error results 
    <hr>
    
    Field Value
    Type:int
    """
    WarnedCount: int = ...
    """
    the count of elements with warning results.  
    
    For those tests without a test value, it is always zero 
    <hr>
    
    Field Value
    Type:int
    """


class ElementQualityCheckResults(NXOpen.TransientObject):
    """
    Represents the element quality checking result of :py:class:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder`
    
    To obtain an instance of this class use CAE.ModelCheck.ElementQualityCheckBuilder
    
    .. versionadded:: NX8.5.0
    """
    
    class TestSummary():
        """
        Reprents the summary data of a specified quality checking test type .  
        
        Constructor: 
        NXOpen.CAE.ModelCheck.ElementQualityCheckResults.TestSummary()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        TestType: TestValueTypesTestType = ...
        """
        the test type
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.CAE.ModelCheck.TestValueTypesTestType`
        """
        WorstTestValue: float = ...
        """
        the worst test value of the specified test within all checked elements.  
        
        which is only availabe for the test has a test value 
        <hr>
        
        Field Value
        Type:float
        """
        HasTestValue: bool = ...
        """
        indicates whether the test has a test value.  
        
        If false, there is no test value associcated
        with this test 
        <hr>
        
        Field Value
        Type:bool
        """
        TestCount: int = ...
        """
        indicates the total number of elements tested for this test 
        <hr>
        
        Field Value
        Type:int
        """
        ErrorCount: int = ...
        """
        the count of elements with error results 
        <hr>
        
        Field Value
        Type:int
        """
        WarnedCount: int = ...
        """
        the count of elements with warning results.  
        
        For those tests without a test value, it is always zero 
        <hr>
        
        Field Value
        Type:int
        """
    
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTestSummary(self) -> 'list[ElementQualityCheckResultsTestSummary_Struct]':
        """
        Returns summary data of tests executed by :py:class:`NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder` 
        
        Signature ``GetTestSummary()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.ModelCheck.ElementQualityCheckResultsTestSummary_Struct` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetElementTestResultByIndex(self, index: int) -> ElementTestResult:
        """
        Returns test results of each element  
        
        Signature ``GetElementTestResultByIndex(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementTestResult` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    ElementTestCount: int = ...
    """
    Returns  the total number of element tested during a test session 
    
    <hr>
    
    Getter Method
    
    Signature ``ElementTestCount`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """


class SolidElementFaceNormalBuilder(NXOpen.Builder, ISelectionBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.SolidElementFaceNormalBuilder` used to reorient normals
    for left handed solid elements.  
    
    Both of the methods are only available in fem context.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateSolidElementFaceNormalBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def DisplayNormals(self) -> None:
        """
        Display normals of :py:meth:`NXOpen.CAE.ModelCheck.SolidElementFaceNormalBuilder.DisplayNormals` 
        
        Signature ``DisplayNormals()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def ReorientLeftHandedElements(self) -> None:
        """
        Reorient normals specified in :py:meth:`NXOpen.CAE.ModelCheck.SolidElementFaceNormalBuilder.ReorientLeftHandedElements`
        which normal is left handed and returns those elements whose normals were reoriented successfully.  
        
        This method will only reorient
        the normals for solid left handed elements in the current work fem part.
        
        Signature ``ReorientLeftHandedElements()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def CreateGroupOfLeftHandedElements(self) -> None:
        """
        Create group for the left handed elements in
        :py:meth:`NXOpen.CAE.ModelCheck.SolidElementFaceNormalBuilder.CreateGroupOfLeftHandedElements`
        and returns those elements which were grouped successfully.  
        
        This method will only group left handed solid elements
        in the current work fem part.
        
        Signature ``CreateGroupOfLeftHandedElements()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    NegativeFaceColor: int = ...
    """
    Returns or sets  the negative face color 
    
    <hr>
    
    Getter Method
    
    Signature ``NegativeFaceColor`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NegativeFaceColor`` 
    
    :param negativeFaceColor: 
    :type negativeFaceColor: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    PositiveFaceColor: int = ...
    """
    Returns or sets  the positive face color 
    
    <hr>
    
    Getter Method
    
    Signature ``PositiveFaceColor`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PositiveFaceColor`` 
    
    :param positiveFaceColor: 
    :type positiveFaceColor: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    SelectionList: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects to be checked.  
    
    The objects must be :py:class:`NXOpen.CAE.Mesh` or
    :py:class:`NXOpen.CAE.FEElement` 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    CheckScopeOption: CheckScope = ...
    """
    Returns or sets  the check scope setting 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckScopeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckScopeOption`` 
    
    :param scope: 
    :type scope: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: SolidElementFaceNormalBuilder = ...  # unknown typename


class TestValueTypesElementReference_Struct():
    """
    represents an element reference definition associated with this test .  
    
    Constructor: 
    NXOpen.CAE.ModelCheck.TestValueTypes.ElementReference()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    ElementTypeName: str = ...
    """
    the element type name, which is defined in solver specific item 
    <hr>
    
    Field Value
    Type:str
    """
    ElementPropertyName: str = ...
    """
    a specified integer element property name 
    <hr>
    
    Field Value
    Type:str
    """
    ElementPropertyValue: int = ...
    """
    the control value of integer element property, only valid when property name is not NULL 
    <hr>
    
    Field Value
    Type:int
    """


class DuplicateElementsCheckBuilderDeletePreferenceMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DuplicateElementsCheckBuilderDeletePreference():
    """
    Represents the duplicate elements deleting preference 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "KeepHighLabel", "Keep the elements with higher labels"
       "KeepLowLabel", "Keep the elements with lower labels"
       "KeepSelected", "Keep the elements specified in the element list :py:meth:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.PreferenceElements`"
       "RemoveSelected", "Delete the elements specified in the element list :py:meth:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.PreferenceElements`"
    """
    KeepHighLabel = 0  # DuplicateElementsCheckBuilderDeletePreferenceMemberType
    KeepLowLabel = 1  # DuplicateElementsCheckBuilderDeletePreferenceMemberType
    KeepSelected = 2  # DuplicateElementsCheckBuilderDeletePreferenceMemberType
    RemoveSelected = 3  # DuplicateElementsCheckBuilderDeletePreferenceMemberType
    
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
    


class DuplicateElementsCheckBuilderDisplaySettings_Struct():
    """
    Represents the display settings of duplicated elements detected .  
    
    Constructor: 
    NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DisplaySettings()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    ShowDuplicateElements: bool = ...
    """
    Whether to show duplicate elements 
    <hr>
    
    Field Value
    Type:bool
    """
    ShowElementLabels: bool = ...
    """
    Whether to show labels of duplicate elements 
    <hr>
    
    Field Value
    Type:bool
    """
    ElementsColor: NXOpen.NXColor = ...
    """
    The display color of duplicate elements 
    <hr>
    
    Field Value
    Type:Id
    """
    ElementsWidth: NXOpen.DisplayableObjectObjectWidth = ...
    """
    The display line width of duplicate elements 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.DisplayableObjectObjectWidth`
    """


class DuplicateElementsCheckBuilder(NXOpen.Builder, ISelectionBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder`
    to check for duplicate elements within the candidate elements.  
    
    Duplicate elements are elements which share the same corner nodes,but do not include
    the middle nodes.
    
    The general workflow is:
    
      #.  Set the candidate elements 
      #.  Set the display settings data 
      #.  Identify the duplicate elements 
      #.  Set the preference option 
      #.  Delete the duplicate elements 
    
    You can delete duplicate elements through :py:meth:`Builder.Commit` or
    :py:meth:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DeleteDuplicateElements`.
    Commits the builder to delete duplicate elements.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateDuplicateElementsCheckBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class DeletePreference():
        """
        Represents the duplicate elements deleting preference 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "KeepHighLabel", "Keep the elements with higher labels"
           "KeepLowLabel", "Keep the elements with lower labels"
           "KeepSelected", "Keep the elements specified in the element list :py:meth:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.PreferenceElements`"
           "RemoveSelected", "Delete the elements specified in the element list :py:meth:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.PreferenceElements`"
        """
        KeepHighLabel = 0  # DuplicateElementsCheckBuilderDeletePreferenceMemberType
        KeepLowLabel = 1  # DuplicateElementsCheckBuilderDeletePreferenceMemberType
        KeepSelected = 2  # DuplicateElementsCheckBuilderDeletePreferenceMemberType
        RemoveSelected = 3  # DuplicateElementsCheckBuilderDeletePreferenceMemberType
        
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
        
    
    
    class DisplaySettings():
        """
        Represents the display settings of duplicated elements detected .  
        
        Constructor: 
        NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DisplaySettings()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        ShowDuplicateElements: bool = ...
        """
        Whether to show duplicate elements 
        <hr>
        
        Field Value
        Type:bool
        """
        ShowElementLabels: bool = ...
        """
        Whether to show labels of duplicate elements 
        <hr>
        
        Field Value
        Type:bool
        """
        ElementsColor: NXOpen.NXColor = ...
        """
        The display color of duplicate elements 
        <hr>
        
        Field Value
        Type:Id
        """
        ElementsWidth: NXOpen.DisplayableObjectObjectWidth = ...
        """
        The display line width of duplicate elements 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.DisplayableObjectObjectWidth`
        """
    
    
    def IdentifyDuplicateElements(self) -> None:
        """
        Calculates to find the duplicate elements and display them in the
        :py:class:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilderDisplaySettings_Struct`.  
        
        The detected duplicate elements are cached, to access the cached calculation result, you could use
        :py:meth:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DuplicateElementGroupsCount` and
        :py:meth:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.GetDuplicateElements`. The previous
        cached data will be cleaned automatically when you start a new identification. 
        
        Signature ``IdentifyDuplicateElements()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetDuplicateElements(self, groupIndex: int) -> 'list[NXOpen.CAE.FEElement]':
        """
        Returns the duplicate elements of specified group index  
        
        Signature ``GetDuplicateElements(groupIndex)`` 
        
        :param groupIndex: 
        :type groupIndex: int 
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def DeleteDuplicateElements(self) -> None:
        """
        Deletes the duplicate elements and clear all cached duplicate elements in this builder.  
        
        The method :py:meth:`Builder.Commit` will also do the same thing. Duplicate elements
        can only be deleted when the context part of this builder is a :py:class:`NXOpen.CAE.BaseFemPart` 
        
        Signature ``DeleteDuplicateElements()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    DisplaySettingsData: DuplicateElementsCheckBuilderDisplaySettings_Struct = ...
    """
    Returns or sets  the display settings for duplicate elements 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplaySettingsData`` 
    
    :returns:  Display settings data  
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilderDisplaySettings_Struct` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplaySettingsData`` 
    
    :param displaySettings:  Display settings data  
    :type displaySettings: :py:class:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilderDisplaySettings_Struct` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    DuplicateElementGroupsCount: int = ...
    """
    Returns  the duplicate elements group count, each group contains elements that are
    duplicates of each other and each group contains at least two duplicate elements 
    
    <hr>
    
    Getter Method
    
    Signature ``DuplicateElementGroupsCount`` 
    
    :returns:  Duplicate element groups count  
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Preference: DuplicateElementsCheckBuilderDeletePreference = ...
    """
    Returns or sets  the duplicate elements deleting preference 
    
    <hr>
    
    Getter Method
    
    Signature ``Preference`` 
    
    :returns:  Delete elements preference  
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilderDeletePreference` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Preference`` 
    
    :param deletePreference:  Delete elements preference  
    :type deletePreference: :py:class:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilderDeletePreference` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    PreferenceElements: NXOpen.CAE.SelectElementsBuilder = ...
    """
    Returns  the preference elements for keep selected and remove selected options 
    
    <hr>
    
    Getter Method
    
    Signature ``PreferenceElements`` 
    
    :returns:  Preference elements  
    :rtype: :py:class:`NXOpen.CAE.SelectElementsBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SelectionList: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects to be checked.  
    
    The objects must be :py:class:`NXOpen.CAE.Mesh` or
    :py:class:`NXOpen.CAE.FEElement` 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CheckScopeOption: CheckScope = ...
    """
    Returns or sets  the check scope setting 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckScopeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckScopeOption`` 
    
    :param scope: 
    :type scope: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: DuplicateElementsCheckBuilder = ...  # unknown typename


class ElementQualitySettingLimitValueMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElementQualitySettingLimitValue():
    """
    indicates how criteria value is defined 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "WarningAndErrorLimit", "Both warning and error criteria value could be defined"
       "ErrorLimitOnly", "Only error criteria value could be defined"
    """
    WarningAndErrorLimit = 0  # ElementQualitySettingLimitValueMemberType
    ErrorLimitOnly = 1  # ElementQualitySettingLimitValueMemberType
    
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
    


class ElementQualitySetting(NXOpen.NXObject):
    """
    Represents element quality check settings of a specified solver language. Each solve language has a
    :py:class:`NXOpen.CAE.ModelCheck.ElementQualitySetting`.
    
    To get a quality check criteria value of a specfied quality test for one element, you can call
    :py:meth:`NXOpen.CAE.ModelCheck.ElementQualitySetting.LocateTestDescriptorName` to get the test
    criteria value name, then call :py:meth:`NXOpen.CAE.ModelCheck.ElementQualitySetting.GetQualityValue` to
    get the criteria value object.
    
    Not to support KF
    
    .. versionadded:: NX8.5.0
    """
    
    class LimitValue():
        """
        indicates how criteria value is defined 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "WarningAndErrorLimit", "Both warning and error criteria value could be defined"
           "ErrorLimitOnly", "Only error criteria value could be defined"
        """
        WarningAndErrorLimit = 0  # ElementQualitySettingLimitValueMemberType
        ErrorLimitOnly = 1  # ElementQualitySettingLimitValueMemberType
        
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
        
    
    
    def GetTestValueByIndex(self, index: int) -> QualityTestValue:
        """
        Returns the :py:class:`NXOpen.CAE.ModelCheck.QualityTestValue` at the specified index in the setting   
        
        Signature ``GetTestValueByIndex(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.QualityTestValue` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTestValueByType(self, testType: TestValueTypesTestType) -> QualityTestValue:
        """
        Returns the :py:class:`NXOpen.CAE.ModelCheck.QualityTestValue` of a specified :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesTestType`  
        
        Signature ``GetTestValueByType(testType)`` 
        
        :param testType: 
        :type testType: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesTestType` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.QualityTestValue` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetQualityValue(self, descriptorName: str) -> ITestValue:
        """
        Returns the test quality value with the specified descriptor name  
        
        Signature ``GetQualityValue(descriptorName)`` 
        
        :param descriptorName: 
        :type descriptorName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.ITestValue` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def LocateTestDescriptorName(self, element: NXOpen.CAE.FEElement, testType: TestValueTypesTestType, useElemSpecific: bool) -> str:
        """
        Returns the name of a quality test value, which is associated with
        an element for a specified test type  
        
        Signature ``LocateTestDescriptorName(element, testType, useElemSpecific)`` 
        
        :param element: 
        :type element: :py:class:`NXOpen.CAE.FEElement` 
        :param testType: 
        :type testType: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesTestType` 
        :param useElemSpecific: 
        :type useElemSpecific: bool 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def ResetToCustomerDefault(self) -> None:
        """
        Reset the quality check setting as customer default 
        
        Signature ``ResetToCustomerDefault()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    LimitValueOption: ElementQualitySettingLimitValue = ...
    """
    Returns or sets  the limit value option 
    
    <hr>
    
    Getter Method
    
    Signature ``LimitValueOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementQualitySettingLimitValue` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LimitValueOption`` 
    
    :param limitValueOption: 
    :type limitValueOption: :py:class:`NXOpen.CAE.ModelCheck.ElementQualitySettingLimitValue` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    TestValueCount: int = ...
    """
    Returns  the count of :py:class:`NXOpen.CAE.ModelCheck.QualityTestValue` in the setting 
    
    <hr>
    
    Getter Method
    
    Signature ``TestValueCount`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    UseElementSpecificValue: bool = ...
    """
    Returns or sets  an option indicating whether to use element specific quality value for testing 
    
    <hr>
    
    Getter Method
    
    Signature ``UseElementSpecificValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseElementSpecificValue`` 
    
    :param useElementSpecificValue: 
    :type useElementSpecificValue: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Null: ElementQualitySetting = ...  # unknown typename


class ElementQualitySettingCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.CAE.ModelCheck.ElementQualitySetting` in a cae part.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.CaePart`
    
    .. versionadded:: NX8.5.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def GetElementQualitySetting(self, solverName: str) -> ElementQualitySetting:
        """
        Retuns the :py:class:`NXOpen.CAE.ModelCheck.ElementQualitySetting` of a specified solver.  
        
        Signature ``GetElementQualitySetting(solverName)`` 
        
        :param solverName: 
        :type solverName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementQualitySetting` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> ElementQualitySetting:
        """
        Finds the :py:class:`NXOpen.CAE.ModelCheck.ElementQualitySetting` with the given identifier as
        recorded in a journal.  
        
        An exception will be thrown if no object can be found with the given
        journal identifier 
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier: 
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementQualitySetting` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    


class ElementEdgeCheckBuilderEdgeDisplayStyle_Struct():
    """
    the display style of the edges detected .  
    
    Constructor: 
    NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    Font: NXOpen.DisplayableObjectObjectFont = ...
    """
    line font 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.DisplayableObjectObjectFont`
    """
    Width: NXOpen.DisplayableObjectObjectWidth = ...
    """
    line width 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.DisplayableObjectObjectWidth`
    """
    Color: NXOpen.NXColor = ...
    """
    line color 
    <hr>
    
    Field Value
    Type:Id
    """


class ReverseBeamElementDirectionBuilder(NXOpen.Builder, ISelectionBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder` used to reverse directions
    for specified beam elements.  
    
    You can reverse beam element directions by using either :py:meth:`Builder.Commit`
    or :py:meth:`NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder.ReverseDirections`.
    The difference between these two methods is :py:meth:`Builder.Commit` reverses the directions
    and updates direction display, but it does not return the beam elements which were reversed
    successfully. :py:meth:`NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder.ReverseDirections` 
    reverses directions and returns the beam elements which were reversed successfully.
    Both of the methods are only available in fem context.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateReverseBeamElementDirectionBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    def DisplayDirections(self) -> None:
        """
        Display directions of :py:meth:`NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder.SelectionList` 
        
        Signature ``DisplayDirections()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def ReverseDirections(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Reverses directions specified in :py:meth:`NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder.SelectionList`
        and returns those elements whose directions were reversed successfully.  
        
        This method will only reverse
        the directions for beam elements in the current work fem part.
        
        Signature ``ReverseDirections()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    SelectionList: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects to be checked.  
    
    The objects must be :py:class:`NXOpen.CAE.Mesh` or
    :py:class:`NXOpen.CAE.FEElement` 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CheckScopeOption: CheckScope = ...
    """
    Returns or sets  the check scope setting 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckScopeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckScopeOption`` 
    
    :param scope: 
    :type scope: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: ReverseBeamElementDirectionBuilder = ...  # unknown typename


class AlignBeamElementDirectionBuilderConnectedElementScopeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AlignBeamElementDirectionBuilderConnectedElementScope():
    """
    the options to define the connection scope to the seed element for model checking 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SeedMesh", "Limits check to only those beam elements in the mesh that contains the Seed Element"
       "AllVisible", "Limits check to only those beam elements which are connected to the Seed Element and are currently visible"
       "UserSpecified", "Limits check to only those beam elements specified in :py:meth:`NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.UserSpecifiedConnectElements`"
    """
    SeedMesh = 0  # AlignBeamElementDirectionBuilderConnectedElementScopeMemberType
    AllVisible = 1  # AlignBeamElementDirectionBuilderConnectedElementScopeMemberType
    UserSpecified = 2  # AlignBeamElementDirectionBuilderConnectedElementScopeMemberType
    
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
    


class AlignBeamElementDirectionBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder` builder used to align the Directions of
    connected beam elements with a seed beam element.  
    
    You can align the directions by executing either 
    :py:meth:`Builder.Commit` or :py:meth:`NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.AlignDirections`.
    The difference between these two methods is :py:meth:`Builder.Commit` aligns the directions
    and updates direction display, but it does not return the elements that have changed directions.
    :py:meth:`NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.AlignDirections` aligns the directions
    and returns the elements that have changed directions. Both of the methods are only available in fem context.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateAlignBeamElementDirectionBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class ConnectedElementScope():
        """
        the options to define the connection scope to the seed element for model checking 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SeedMesh", "Limits check to only those beam elements in the mesh that contains the Seed Element"
           "AllVisible", "Limits check to only those beam elements which are connected to the Seed Element and are currently visible"
           "UserSpecified", "Limits check to only those beam elements specified in :py:meth:`NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.UserSpecifiedConnectElements`"
        """
        SeedMesh = 0  # AlignBeamElementDirectionBuilderConnectedElementScopeMemberType
        AllVisible = 1  # AlignBeamElementDirectionBuilderConnectedElementScopeMemberType
        UserSpecified = 2  # AlignBeamElementDirectionBuilderConnectedElementScopeMemberType
        
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
        
    
    
    def FindAllVisibleConnectedElements(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Finds all visible elements connected with the seed element  
        
        Signature ``FindAllVisibleConnectedElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayDirections(self) -> None:
        """
        Display element directions for connected elements, which are to be aligned with seed element direction 
        
        Signature ``DisplayDirections()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def AlignDirections(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Aligns the directions of elements connected to the seed element.  
        
        Returns the elements
        that have had the directions successfully reversed. This method will only reverse
        the directions for beam elements in the current work fem part.
        
        Signature ``AlignDirections()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    ElementConnectScope: AlignBeamElementDirectionBuilderConnectedElementScope = ...
    """
    Returns or sets  the option to indicate how to define connected elements for checking 
    
    <hr>
    
    Getter Method
    
    Signature ``ElementConnectScope`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilderConnectedElementScope` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ElementConnectScope`` 
    
    :param connectScope: 
    :type connectScope: :py:class:`NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilderConnectedElementScope` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ReverseSeedDirection: bool = ...
    """
    Returns or sets  the option indicating whether to reverse element directions so that they are aligned with the seed element 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseSeedDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseSeedDirection`` 
    
    :param seedDirectionToBeReversed: 
    :type seedDirectionToBeReversed: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    SeedElement: NXOpen.CAE.FEElement = ...
    """
    Returns or sets  the seed element 
    
    <hr>
    
    Getter Method
    
    Signature ``SeedElement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.FEElement` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeedElement`` 
    
    :param seedElement: 
    :type seedElement: :py:class:`NXOpen.CAE.FEElement` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    UserSpecifiedConnectElements: NXOpen.CAE.SelectElementsBuilder = ...
    """
    Returns  the user specified connected elements to be aligned with seed element 
    
    <hr>
    
    Getter Method
    
    Signature ``UserSpecifiedConnectElements`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SelectElementsBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: AlignBeamElementDirectionBuilder = ...  # unknown typename


class TestValueTypesTestTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TestValueTypesTestType():
    """
    the test types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "JacobianZero", " - "
       "JacobianRatio", " - "
       "JacobianSign", " - "
       "Volume", " - "
       "AxisymmetricY", "When elements are modeled in XZ plane, check consistent Y. When elements are modeled in XY plane, check consistent Z."
       "AxisymmetricX", "When elements are modeled in XZ plane, check X >= 0.0. When elements are modeled in XY plane, check Y >= 0.0."
       "AspectRatio", " - "
       "SkewAngle", " - "
       "InteriorAngleMinimum", " - "
       "InteriorAngleMaximum", " - "
       "Taper", " - "
       "WarpFactor", " - "
       "FaceWarpCoefficient", " - "
       "EdgePointLengthRatio", " - "
       "EdgePointIncludedAngle", " - "
       "LengthRatioOffset", " - "
       "ParallelDeviation", " - "
       "ShapeFactor", " - "
       "Twist", " - "
       "LengthMinimum", " - "
       "LengthMaximum", " - "
       "TetCollapse", " - "
       "WarpageAngle", " - "
       "CohesiveElement", " - "
       "LaminateTaperRatio", "Ratio of longest edge to shortest edge in stacking direction for the elements that reference PCOMPS entries only."
       "LaminateThicknessRatio", "Ratio of the difference between thickness in stacking direction as defined by grids and thickness as defined by ply thickness specification to the thickness in the stacking direction as defined by grids for the elements that reference PCOMPS entries only."
       "Area", " - "
    """
    JacobianZero = 0  # TestValueTypesTestTypeMemberType
    JacobianRatio = 1  # TestValueTypesTestTypeMemberType
    JacobianSign = 2  # TestValueTypesTestTypeMemberType
    Volume = 3  # TestValueTypesTestTypeMemberType
    AxisymmetricY = 4  # TestValueTypesTestTypeMemberType
    AxisymmetricX = 5  # TestValueTypesTestTypeMemberType
    AspectRatio = 6  # TestValueTypesTestTypeMemberType
    SkewAngle = 7  # TestValueTypesTestTypeMemberType
    InteriorAngleMinimum = 8  # TestValueTypesTestTypeMemberType
    InteriorAngleMaximum = 9  # TestValueTypesTestTypeMemberType
    Taper = 10  # TestValueTypesTestTypeMemberType
    WarpFactor = 11  # TestValueTypesTestTypeMemberType
    FaceWarpCoefficient = 12  # TestValueTypesTestTypeMemberType
    EdgePointLengthRatio = 13  # TestValueTypesTestTypeMemberType
    EdgePointIncludedAngle = 14  # TestValueTypesTestTypeMemberType
    LengthRatioOffset = 15  # TestValueTypesTestTypeMemberType
    ParallelDeviation = 16  # TestValueTypesTestTypeMemberType
    ShapeFactor = 17  # TestValueTypesTestTypeMemberType
    Twist = 18  # TestValueTypesTestTypeMemberType
    LengthMinimum = 19  # TestValueTypesTestTypeMemberType
    LengthMaximum = 20  # TestValueTypesTestTypeMemberType
    TetCollapse = 21  # TestValueTypesTestTypeMemberType
    WarpageAngle = 22  # TestValueTypesTestTypeMemberType
    CohesiveElement = 23  # TestValueTypesTestTypeMemberType
    LaminateTaperRatio = 24  # TestValueTypesTestTypeMemberType
    LaminateThicknessRatio = 25  # TestValueTypesTestTypeMemberType
    Area = 26  # TestValueTypesTestTypeMemberType
    
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
    


class TestValueTypesValidatorMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TestValueTypesValidator():
    """
    indicates how to compare the check result with the criteria value 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "indicates no criteria value defined, not necessary to compare the check result with criteria value"
       "GreatThan", "the check passes if the check result is great than the criteria value"
       "GreatThanOrEqual", "the check passes if the check result is equal or great than the criteria value"
       "SmallThan", "the check passes if the check result is small than the criteria value"
       "SmallThanOrEqual", "the check passes if the check result is equal or small than the criteria value"
    """
    NotSet = 0  # TestValueTypesValidatorMemberType
    GreatThan = 1  # TestValueTypesValidatorMemberType
    GreatThanOrEqual = 2  # TestValueTypesValidatorMemberType
    SmallThan = 3  # TestValueTypesValidatorMemberType
    SmallThanOrEqual = 4  # TestValueTypesValidatorMemberType
    
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
    


class TestValueTypesCriteriaTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TestValueTypesCriteriaType():
    """
    the alert level of a criteria value 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Warning", "reports as warning if the check result failed with the criteria value"
       "Error", "reports as error if the check result failed with the criteria value"
    """
    Warning = 0  # TestValueTypesCriteriaTypeMemberType
    Error = 1  # TestValueTypesCriteriaTypeMemberType
    
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
    


class TestValueTypesResultMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TestValueTypesResult():
    """
    the checking result 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Passed", "indicates the test value does not violate the criteria values"
       "Failed", "indicates the test value violates the error criteria value"
       "Exception", "indicates there is an exception thrown during the checking"
       "NotApply", "indicates the test is not available or not done for an element"
       "Warned", "indicates the test value violates the warning criteria value"
    """
    Passed = 0  # TestValueTypesResultMemberType
    Failed = 1  # TestValueTypesResultMemberType
    Exception = 2  # TestValueTypesResultMemberType
    NotApply = 3  # TestValueTypesResultMemberType
    Warned = 4  # TestValueTypesResultMemberType
    
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
    


class TestValueTypes():
    """
    Represents the quality check criteria value settings  
    
    No Creator this holds an enum  shared by other classes
    
    .. versionadded:: NX8.5.0
    """
    
    class TestType():
        """
        the test types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "JacobianZero", " - "
           "JacobianRatio", " - "
           "JacobianSign", " - "
           "Volume", " - "
           "AxisymmetricY", "When elements are modeled in XZ plane, check consistent Y. When elements are modeled in XY plane, check consistent Z."
           "AxisymmetricX", "When elements are modeled in XZ plane, check X >= 0.0. When elements are modeled in XY plane, check Y >= 0.0."
           "AspectRatio", " - "
           "SkewAngle", " - "
           "InteriorAngleMinimum", " - "
           "InteriorAngleMaximum", " - "
           "Taper", " - "
           "WarpFactor", " - "
           "FaceWarpCoefficient", " - "
           "EdgePointLengthRatio", " - "
           "EdgePointIncludedAngle", " - "
           "LengthRatioOffset", " - "
           "ParallelDeviation", " - "
           "ShapeFactor", " - "
           "Twist", " - "
           "LengthMinimum", " - "
           "LengthMaximum", " - "
           "TetCollapse", " - "
           "WarpageAngle", " - "
           "CohesiveElement", " - "
           "LaminateTaperRatio", "Ratio of longest edge to shortest edge in stacking direction for the elements that reference PCOMPS entries only."
           "LaminateThicknessRatio", "Ratio of the difference between thickness in stacking direction as defined by grids and thickness as defined by ply thickness specification to the thickness in the stacking direction as defined by grids for the elements that reference PCOMPS entries only."
           "Area", " - "
        """
        JacobianZero = 0  # TestValueTypesTestTypeMemberType
        JacobianRatio = 1  # TestValueTypesTestTypeMemberType
        JacobianSign = 2  # TestValueTypesTestTypeMemberType
        Volume = 3  # TestValueTypesTestTypeMemberType
        AxisymmetricY = 4  # TestValueTypesTestTypeMemberType
        AxisymmetricX = 5  # TestValueTypesTestTypeMemberType
        AspectRatio = 6  # TestValueTypesTestTypeMemberType
        SkewAngle = 7  # TestValueTypesTestTypeMemberType
        InteriorAngleMinimum = 8  # TestValueTypesTestTypeMemberType
        InteriorAngleMaximum = 9  # TestValueTypesTestTypeMemberType
        Taper = 10  # TestValueTypesTestTypeMemberType
        WarpFactor = 11  # TestValueTypesTestTypeMemberType
        FaceWarpCoefficient = 12  # TestValueTypesTestTypeMemberType
        EdgePointLengthRatio = 13  # TestValueTypesTestTypeMemberType
        EdgePointIncludedAngle = 14  # TestValueTypesTestTypeMemberType
        LengthRatioOffset = 15  # TestValueTypesTestTypeMemberType
        ParallelDeviation = 16  # TestValueTypesTestTypeMemberType
        ShapeFactor = 17  # TestValueTypesTestTypeMemberType
        Twist = 18  # TestValueTypesTestTypeMemberType
        LengthMinimum = 19  # TestValueTypesTestTypeMemberType
        LengthMaximum = 20  # TestValueTypesTestTypeMemberType
        TetCollapse = 21  # TestValueTypesTestTypeMemberType
        WarpageAngle = 22  # TestValueTypesTestTypeMemberType
        CohesiveElement = 23  # TestValueTypesTestTypeMemberType
        LaminateTaperRatio = 24  # TestValueTypesTestTypeMemberType
        LaminateThicknessRatio = 25  # TestValueTypesTestTypeMemberType
        Area = 26  # TestValueTypesTestTypeMemberType
        
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
        
    
    
    class Validator():
        """
        indicates how to compare the check result with the criteria value 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "indicates no criteria value defined, not necessary to compare the check result with criteria value"
           "GreatThan", "the check passes if the check result is great than the criteria value"
           "GreatThanOrEqual", "the check passes if the check result is equal or great than the criteria value"
           "SmallThan", "the check passes if the check result is small than the criteria value"
           "SmallThanOrEqual", "the check passes if the check result is equal or small than the criteria value"
        """
        NotSet = 0  # TestValueTypesValidatorMemberType
        GreatThan = 1  # TestValueTypesValidatorMemberType
        GreatThanOrEqual = 2  # TestValueTypesValidatorMemberType
        SmallThan = 3  # TestValueTypesValidatorMemberType
        SmallThanOrEqual = 4  # TestValueTypesValidatorMemberType
        
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
        
    
    
    class CriteriaType():
        """
        the alert level of a criteria value 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Warning", "reports as warning if the check result failed with the criteria value"
           "Error", "reports as error if the check result failed with the criteria value"
        """
        Warning = 0  # TestValueTypesCriteriaTypeMemberType
        Error = 1  # TestValueTypesCriteriaTypeMemberType
        
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
        
    
    
    class Result():
        """
        the checking result 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Passed", "indicates the test value does not violate the criteria values"
           "Failed", "indicates the test value violates the error criteria value"
           "Exception", "indicates there is an exception thrown during the checking"
           "NotApply", "indicates the test is not available or not done for an element"
           "Warned", "indicates the test value violates the warning criteria value"
        """
        Passed = 0  # TestValueTypesResultMemberType
        Failed = 1  # TestValueTypesResultMemberType
        Exception = 2  # TestValueTypesResultMemberType
        NotApply = 3  # TestValueTypesResultMemberType
        Warned = 4  # TestValueTypesResultMemberType
        
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
        
    
    
    class ElementReference():
        """
        represents an element reference definition associated with this test .  
        
        Constructor: 
        NXOpen.CAE.ModelCheck.TestValueTypes.ElementReference()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        ElementTypeName: str = ...
        """
        the element type name, which is defined in solver specific item 
        <hr>
        
        Field Value
        Type:str
        """
        ElementPropertyName: str = ...
        """
        a specified integer element property name 
        <hr>
        
        Field Value
        Type:str
        """
        ElementPropertyValue: int = ...
        """
        the control value of integer element property, only valid when property name is not NULL 
        <hr>
        
        Field Value
        Type:int
        """
    


class QualityTestValue(NXOpen.NXObject, ITestValue):
    """
    Represents quality test settings of a specified test type  
    
    Not to support KF
    
    .. versionadded:: NX8.5.0
    """
    
    def GetElementSpecificTestByIndex(self, index: int) -> ElementSpecificTestValue:
        """
        Returns :py:class:`NXOpen.CAE.ModelCheck.ElementSpecificTestValue` of specified index in this test setting  
        
        Signature ``GetElementSpecificTestByIndex(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementSpecificTestValue` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTestType(self) -> TestValueTypesTestType:
        """
        Returns the test type  
        
        Signature ``GetTestType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesTestType` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetValidator(self) -> TestValueTypesValidator:
        """
        Returns the validator type  
        
        Signature ``GetValidator()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesValidator` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def HasCriteriaValue(self) -> bool:
        """
        Tells whether there is criteria value associated with this test  
        
        Signature ``HasCriteriaValue()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCriteriaValue(self, criteriaType: TestValueTypesCriteriaType) -> tuple:
        """
        Returns the criteria value.  
        
        An exception will be thrown if there is no criteria value associated with this test  
        
        Signature ``GetCriteriaValue(criteriaType)`` 
        
        :param criteriaType: 
        :type criteriaType: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesCriteriaType` 
        :returns: a tuple 
        :rtype: A tuple consisting of (unit, criteriaValue). unit is a :py:class:`NXOpen.Unit`. criteriaValue is a float. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetCriteriaValue(self, criteriaType: TestValueTypesCriteriaType, criteriaValue: float, unit: NXOpen.Unit) -> None:
        """
        Sets the criteria value. An exception will be thrown if there is no criteria value associated with this test 
        
        Signature ``SetCriteriaValue(criteriaType, criteriaValue, unit)`` 
        
        :param criteriaType: 
        :type criteriaType: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesCriteriaType` 
        :param criteriaValue: 
        :type criteriaValue: float 
        :param unit: 
        :type unit: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetCriteriaValue(self, criteriaType: TestValueTypesCriteriaType, criteriaValue: str, unit: NXOpen.Unit) -> None:
        """
        Sets the criteria value. An exception will be thrown if there is no criteria value associated with this test 
        
        Signature ``SetCriteriaValue(criteriaType, criteriaValue, unit)`` 
        
        :param criteriaType: 
        :type criteriaType: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesCriteriaType` 
        :param criteriaValue: 
        :type criteriaValue: str 
        :param unit: 
        :type unit: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetIsSolverSpecificTest(self) -> tuple:
        """
        To know whether this quality test is a solver specific test and a system test  
        
        Signature ``GetIsSolverSpecificTest()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (isSolverSpecificTest, isSystemTest). isSolverSpecificTest is a bool. isSystemTest is a bool. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetElementReferences(self) -> 'list[TestValueTypesElementReference_Struct]':
        """
        Returns the element reference definitions associated with this test  
        
        Signature ``GetElementReferences()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesElementReference_Struct` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetToCustomerDefault(self) -> None:
        """
        Reset as customer default setting 
        
        Signature ``ResetToCustomerDefault()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    ElementSpecificTestCount: int = ...
    """
    Returns  the count of :py:class:`NXOpen.CAE.ModelCheck.ElementSpecificTestValue` in this test setting 
    
    <hr>
    
    Getter Method
    
    Signature ``ElementSpecificTestCount`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DoTest: bool = ...
    """
    Returns or sets  an option value indicating whether to do element quality check for this test  
    
    <hr>
    
    Getter Method
    
    Signature ``DoTest`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DoTest`` 
    
    :param doTest: 
    :type doTest: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: QualityTestValue = ...  # unknown typename


class ElementMaterialOrientationCheckBuilderMaterialOrientationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElementMaterialOrientationCheckBuilderMaterialOrientationType():
    """
    the material orientation type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Shell", "the material orientation of shell element"
       "SolidFirstDirection", "the first direction of solid element material orientation"
       "SolidSecondDirection", "the second direction of solid element material orientation"
       "SolidThirdDirection", "the third direction of solid element material orientation"
    """
    Shell = 0  # ElementMaterialOrientationCheckBuilderMaterialOrientationTypeMemberType
    SolidFirstDirection = 1  # ElementMaterialOrientationCheckBuilderMaterialOrientationTypeMemberType
    SolidSecondDirection = 2  # ElementMaterialOrientationCheckBuilderMaterialOrientationTypeMemberType
    SolidThirdDirection = 3  # ElementMaterialOrientationCheckBuilderMaterialOrientationTypeMemberType
    
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
    


class ElementMaterialOrientationCheckBuilder(NXOpen.Builder, ISelectionBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder` 
    used to check the material orientation for shell and solid elements.  
    
    Use :py:meth:`Builder.Commit` to calculate material orientation and to display 
    an orientation vector for each input element. 
    Use :py:meth:`NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.DoCheck`
    to calculate the material orientation for each input element and return the orientation vector 
    result. If an element fails when calculating it's material orientation, 
    the element will be displayed in red and outputed to listing information window.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateElementMaterialOrientationCheckBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class MaterialOrientationType():
        """
        the material orientation type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Shell", "the material orientation of shell element"
           "SolidFirstDirection", "the first direction of solid element material orientation"
           "SolidSecondDirection", "the second direction of solid element material orientation"
           "SolidThirdDirection", "the third direction of solid element material orientation"
        """
        Shell = 0  # ElementMaterialOrientationCheckBuilderMaterialOrientationTypeMemberType
        SolidFirstDirection = 1  # ElementMaterialOrientationCheckBuilderMaterialOrientationTypeMemberType
        SolidSecondDirection = 2  # ElementMaterialOrientationCheckBuilderMaterialOrientationTypeMemberType
        SolidThirdDirection = 3  # ElementMaterialOrientationCheckBuilderMaterialOrientationTypeMemberType
        
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
        
    
    
    def GetCheckOrientation(self, orientationType: ElementMaterialOrientationCheckBuilderMaterialOrientationType) -> bool:
        """
        Gets option value which indicates whether to check for the specified material orientation type  
        
        Signature ``GetCheckOrientation(orientationType)`` 
        
        :param orientationType: 
        :type orientationType: :py:class:`NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilderMaterialOrientationType` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCheckOrientation(self, orientationType: ElementMaterialOrientationCheckBuilderMaterialOrientationType, checkOrientation: bool) -> None:
        """
        Sets option value which indicates whether to check for the specified material orientation type 
        
        Signature ``SetCheckOrientation(orientationType, checkOrientation)`` 
        
        :param orientationType: 
        :type orientationType: :py:class:`NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilderMaterialOrientationType` 
        :param checkOrientation: 
        :type checkOrientation: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetOrientationColor(self, orientationType: ElementMaterialOrientationCheckBuilderMaterialOrientationType) -> NXOpen.NXColor:
        """
        Gets display color of a specified material orientation type  
        
        Signature ``GetOrientationColor(orientationType)`` 
        
        :param orientationType: 
        :type orientationType: :py:class:`NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilderMaterialOrientationType` 
        :returns: 
        :rtype: Id 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOrientationColor(self, orientationType: ElementMaterialOrientationCheckBuilderMaterialOrientationType, color: NXOpen.NXColor) -> None:
        """
        Sets display color of a specified material orientation type 
        
        Signature ``SetOrientationColor(orientationType, color)`` 
        
        :param orientationType: 
        :type orientationType: :py:class:`NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilderMaterialOrientationType` 
        :param color: 
        :type color: Id 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def DoCheck(self) -> tuple:
        """
        Calculates material orientation vector for input elements and returns the orientation vector result  
        
        Signature ``DoCheck()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (orienation, orientationType, elements). orienation is a list of :py:class:`NXOpen.Vector3d`.   material orientation vector orientationType is a list of :py:class:`NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilderMaterialOrientationType`. elements is a list of :py:class:`NXOpen.CAE.FEElement`.   the elements associated with the orientation vectors
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    SelectionList: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects to be checked.  
    
    The objects must be :py:class:`NXOpen.CAE.Mesh` or
    :py:class:`NXOpen.CAE.FEElement` 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CheckScopeOption: CheckScope = ...
    """
    Returns or sets  the check scope setting 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckScopeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckScopeOption`` 
    
    :param scope: 
    :type scope: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: ElementMaterialOrientationCheckBuilder = ...  # unknown typename


class ReverseShellElementNormalBuilderDisplayTypeValueMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReverseShellElementNormalBuilderDisplayTypeValue():
    """
    indicates how display type value is defined 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Arrows", " - "
       "SolidFaceColors", " - "
    """
    Arrows = 0  # ReverseShellElementNormalBuilderDisplayTypeValueMemberType
    SolidFaceColors = 1  # ReverseShellElementNormalBuilderDisplayTypeValueMemberType
    
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
    


class ReverseShellElementNormalBuilder(NXOpen.Builder, ISelectionBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder` used to reverse normals
    for specified shell elements.  
    
    You can reverse shell element normals by using either :py:meth:`Builder.Commit`
    or :py:meth:`NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.ReverseNormals`.
    The difference between these two methods is :py:meth:`Builder.Commit` reverses the normals
    and updates normal display, but it does not return the shell elements which were reversed
    successfully. :py:meth:`NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.ReverseNormals` 
    reverses normals and returns the shell elements which were reversed successfully.
    Both of the methods are only available in fem context.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateReverseShellElementNormalBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class DisplayTypeValue():
        """
        indicates how display type value is defined 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Arrows", " - "
           "SolidFaceColors", " - "
        """
        Arrows = 0  # ReverseShellElementNormalBuilderDisplayTypeValueMemberType
        SolidFaceColors = 1  # ReverseShellElementNormalBuilderDisplayTypeValueMemberType
        
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
        
    
    
    def DisplayNormals(self) -> None:
        """
        Display normals of :py:meth:`NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.SelectionList` 
        
        Signature ``DisplayNormals()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def ReverseNormals(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Reverses normals specified in :py:meth:`NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.SelectionList`
        and returns those elements whose normals were reversed successfully.  
        
        This method will only reverse
        the normals for shell elements in the current work fem part.
        
        Signature ``ReverseNormals()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def CreateInconsistentElementEdgeGroup(self) -> NXOpen.CAE.CaeGroup:
        """
        Creates inconsistent element edge group 
        
        Signature ``CreateInconsistentElementEdgeGroup()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.CaeGroup` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    DisplayType: ReverseShellElementNormalBuilderDisplayTypeValue = ...
    """
    Returns or sets  the display type 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilderDisplayTypeValue` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayType`` 
    
    :param displayType: 
    :type displayType: :py:class:`NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilderDisplayTypeValue` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    NegativeFaceColor: int = ...
    """
    Returns or sets  the negative face color 
    
    <hr>
    
    Getter Method
    
    Signature ``NegativeFaceColor`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NegativeFaceColor`` 
    
    :param negativeFaceColor: 
    :type negativeFaceColor: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    PositiveFaceColor: int = ...
    """
    Returns or sets  the positive face color 
    
    <hr>
    
    Getter Method
    
    Signature ``PositiveFaceColor`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PositiveFaceColor`` 
    
    :param positiveFaceColor: 
    :type positiveFaceColor: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    SelectionList: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects to be checked.  
    
    The objects must be :py:class:`NXOpen.CAE.Mesh` or
    :py:class:`NXOpen.CAE.FEElement` 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CheckScopeOption: CheckScope = ...
    """
    Returns or sets  the check scope setting 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckScopeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckScopeOption`` 
    
    :param scope: 
    :type scope: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: ReverseShellElementNormalBuilder = ...  # unknown typename


class TestResult(NXOpen.TransientObject):
    """
    Represents quality checking result of a quality test
    
    To obtain an instance of this class use CAE.ModelCheck.ElementTestResult.GetTestResults
    
    .. versionadded:: NX8.5.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def HasTestValue(self) -> bool:
        """
        Tells whether there is a test value associated with this test  
        
        Signature ``HasTestValue()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    TestType: TestValueTypesTestType = ...
    """
    Returns  the test type 
    
    <hr>
    
    Getter Method
    
    Signature ``TestType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesTestType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    TestValue: float = ...
    """
    Returns  the test value.  
    
    An exception will be thrown f there is no test value associated with this test 
    
    <hr>
    
    Getter Method
    
    Signature ``TestValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ValidatedTestResult: TestValueTypesResult = ...
    """
    Returns  the validation result of comparing test value with the criteria value.  
    
    if no test value is associated this test, the result just indicates the test 
    is passed or failed 
    
    <hr>
    
    Getter Method
    
    Signature ``ValidatedTestResult`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.TestValueTypesResult` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """


class ModelSetupCheckBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.ModelSetupCheckBuilder` which can be
    used to check if the active :py:class:`NXOpen.CAE.SimSolution` contains all the necessary 
    items for the analysis, including elements, loads, constraints and materials.  
    
    Also it could check 
    label conficts and component connect status.
    :py:meth:`Builder.Commit` performs the check. The check result is written into a report
    file or listed in a separate information window, along with an error summary for each topic  
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateModelSetupCheckBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    def DoCheck(self) -> int:
        """
        Performs model setup check 
        
        Signature ``DoCheck()`` 
        
        :returns:  Model setup checking result. Zero indicates the checking is successful  
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    CheckAllComponents: bool = ...
    """
    Returns or sets  the value indicating whether to check all components associated with the assembly FEM in the 
    model check, regardless of load status.  
    
    If false, only the fully loaded components are included 
    in the check 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckAllComponents`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckAllComponents`` 
    
    :param checkAllComponents: 
    :type checkAllComponents: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    CheckLabelConflicts: bool = ...
    """
    Returns or sets  the value indicating whether to check labeling conflicts for node, element and coordindate system across component FEMS
    and reports the label range in which the conflict occurs 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckLabelConflicts`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckLabelConflicts`` 
    
    :param checkLabelConflicts: 
    :type checkLabelConflicts: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    CheckUnconnectedComponent: bool = ...
    """
    Returns or sets  the option specifying whether to check for component FEMs that are not connected  
    
    <hr>
    
    Getter Method
    
    Signature ``CheckUnconnectedComponent`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckUnconnectedComponent`` 
    
    :param checkUnconnectedComponent: 
    :type checkUnconnectedComponent: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    IsDetailedMessage: bool = ...
    """
    Returns or sets  the value indicating whether to list comprehensive descriptions of any problems and suggest
    possible remedies.  
    
    If false, only the simple descriptions of problems are listed 
    
    <hr>
    
    Getter Method
    
    Signature ``IsDetailedMessage`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsDetailedMessage`` 
    
    :param isDetailedMessage: 
    :type isDetailedMessage: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ReportFileName: str = ...
    """
    Returns or sets  the full name of the report file.  
    
    If NULL, the report is listed in a separate listing window  
    
    <hr>
    
    Getter Method
    
    Signature ``ReportFileName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportFileName`` 
    
    :param reportFileName: 
    :type reportFileName: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Null: ModelSetupCheckBuilder = ...  # unknown typename


class AlignShellElementFirstEdgeBuilderElemSelectionModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AlignShellElementFirstEdgeBuilderElemSelectionMode():
    """
    the options to define the connection scope to the seed element for model checking 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ConnectedElementsinSeedMesh", " - "
       "AllVisibleConnectedShellElements", " - "
       "SelectedConnectedElements", " - "
    """
    ConnectedElementsinSeedMesh = 0  # AlignShellElementFirstEdgeBuilderElemSelectionModeMemberType
    AllVisibleConnectedShellElements = 1  # AlignShellElementFirstEdgeBuilderElemSelectionModeMemberType
    SelectedConnectedElements = 2  # AlignShellElementFirstEdgeBuilderElemSelectionModeMemberType
    
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
    


class AlignShellElementFirstEdgeBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilder` builder used to align the first edges of
    connected shell elements with a seed element edge.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateAlignShellElementFirstEdgeBuilder`
    
    Default values.
    
    ====================  ============================
    Property              Value
    ====================  ============================
    ElemSelectionMethod   ConnectedElementsinSeedMesh 
    ====================  ============================
    
    .. versionadded:: NX12.0.0
    """
    
    class ElemSelectionMode():
        """
        the options to define the connection scope to the seed element for model checking 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ConnectedElementsinSeedMesh", " - "
           "AllVisibleConnectedShellElements", " - "
           "SelectedConnectedElements", " - "
        """
        ConnectedElementsinSeedMesh = 0  # AlignShellElementFirstEdgeBuilderElemSelectionModeMemberType
        AllVisibleConnectedShellElements = 1  # AlignShellElementFirstEdgeBuilderElemSelectionModeMemberType
        SelectedConnectedElements = 2  # AlignShellElementFirstEdgeBuilderElemSelectionModeMemberType
        
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
        
    
    
    def DisplayFirstEdges(self) -> None:
        """
        Display first edges for connected elements, which are to be aligned with seed edge 
        
        Signature ``DisplayFirstEdges()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Direction: bool = ...
    """
    Returns or sets  the direction 
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction: 
    :type direction: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ElemSelectionMethod: AlignShellElementFirstEdgeBuilderElemSelectionMode = ...
    """
    Returns or sets  the element selection method 
    
    <hr>
    
    Getter Method
    
    Signature ``ElemSelectionMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilderElemSelectionMode` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ElemSelectionMethod`` 
    
    :param elemSelectionMethod: 
    :type elemSelectionMethod: :py:class:`NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilderElemSelectionMode` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Elements: NXOpen.CAE.SelectElementsBuilder = ...
    """
    Returns  the elements 
    
    <hr>
    
    Getter Method
    
    Signature ``Elements`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SelectElementsBuilder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SeedEdge: NXOpen.CAE.SelectElementsBuilder = ...
    """
    Returns  the seed edge 
    
    <hr>
    
    Getter Method
    
    Signature ``SeedEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SelectElementsBuilder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: AlignShellElementFirstEdgeBuilder = ...  # unknown typename


class ElementEdgeCheckBuilderScopeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElementEdgeCheckBuilderScope():
    """
    the Scope over which the Computation of free/non-manifold edges with be done 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "EntireModel", "Takes all elements in the model into account while computing"
       "VisibleModel", "Only takes visible elements into account while computing"
       "SelectedModels", "Only takes selected elements into account while computing"
    """
    EntireModel = 0  # ElementEdgeCheckBuilderScopeMemberType
    VisibleModel = 1  # ElementEdgeCheckBuilderScopeMemberType
    SelectedModels = 2  # ElementEdgeCheckBuilderScopeMemberType
    
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
    


class ElementEdgeCheckBuilder(NXOpen.Builder, ISelectionBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder` which can be
    used to detect free element edges or non-manifold edges.  
    
    A free edge is any Element edge that is not shared by any other element face (on
    either 2D or 3D elements ) within the defined scope of the check.
    A non-manifold edge is any Element edge that is shared more than 2 element faces (on
    either 2D or 3D elements ) within the defined scope of the check.
    
    The computation scope :py:meth:`ElementEdgeCheckBuilder.ComputationScope``
    will affect on the checking result. The free element edges or non-manifold edges found will
    be displayed using the display setting :py:class:`NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilderEdgeDisplayStyle_Struct`.
    You can execute checking through :py:meth:`Builder.Commit` or
    :py:meth:`NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.ExecuteCheck`. Commiting the builder
    performs checking and displays the free edges and non-manifold edges in graphic window.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateElementEdgeCheckBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class Scope():
        """
        the Scope over which the Computation of free/non-manifold edges with be done 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "EntireModel", "Takes all elements in the model into account while computing"
           "VisibleModel", "Only takes visible elements into account while computing"
           "SelectedModels", "Only takes selected elements into account while computing"
        """
        EntireModel = 0  # ElementEdgeCheckBuilderScopeMemberType
        VisibleModel = 1  # ElementEdgeCheckBuilderScopeMemberType
        SelectedModels = 2  # ElementEdgeCheckBuilderScopeMemberType
        
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
        
    
    
    class EdgeDisplayStyle():
        """
        the display style of the edges detected .  
        
        Constructor: 
        NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        Font: NXOpen.DisplayableObjectObjectFont = ...
        """
        line font 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.DisplayableObjectObjectFont`
        """
        Width: NXOpen.DisplayableObjectObjectWidth = ...
        """
        line width 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.DisplayableObjectObjectWidth`
        """
        Color: NXOpen.NXColor = ...
        """
        line color 
        <hr>
        
        Field Value
        Type:Id
        """
    
    
    def HideInputMeshes(self, hideInputMeshes: bool) -> None:
        """
        Hides or unhides the input meshes 
        
        Signature ``HideInputMeshes(hideInputMeshes)`` 
        
        :param hideInputMeshes: 
        :type hideInputMeshes: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def ExecuteCheck(self) -> tuple:
        """
        Finds free edges when :py:meth:`CAE.ModelCheck.ElementEdgeCheckBuilder.CheckFreeEdges`` is set,
        and non-manifold edges when :py:meth:`CAE.ModelCheck.ElementEdgeCheckBuilder.CheckNonManifoldEdges`` is set.  
        
        The method :py:meth:`Builder.Commit` will also do the same thing,
        but display the element edges instead of returning them.
        
        Signature ``ExecuteCheck()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (freeEdges, nonManifoldEdges). freeEdges is a list of :py:class:`NXOpen.CAE.FEElemEdge`.   free element edges nonManifoldEdges is a list of :py:class:`NXOpen.CAE.FEElemEdge`.   non-manifold element edges 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def DoCheck(self) -> tuple:
        """
        Finds free edges when :py:meth:`CAE.ModelCheck.ElementEdgeCheckBuilder.CheckFreeEdges`` is set,
        and non-manifold edges when :py:meth:`CAE.ModelCheck.ElementEdgeCheckBuilder.CheckNonManifoldEdges`` is set,
        returns the associated elements and output group for free and/or non-manifold element edges.  
        
        For the associated elements, if both checks are done at the same time, the elements associated to free edges are
        returned firstly in the list.
        
        Signature ``DoCheck()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (freeEdges, nonManifoldEdges, assoElems, outputGroup). freeEdges is a list of :py:class:`NXOpen.CAE.FEElemEdge`.   free element edges nonManifoldEdges is a list of :py:class:`NXOpen.CAE.FEElemEdge`.   non-manifold element edges assoElems is a list of :py:class:`NXOpen.CAE.FEElement`.   associated elements for free and/or non-manifold element edges,                                                                                         if both checks are done at the same time, the elements associated                                                                                         to free edges are returned firstly in the list.                                                                                      outputGroup is a :py:class:`NXOpen.CAE.CaeGroup`.   output group for free and/or non-manifold element edges 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    CheckFreeEdges: bool = ...
    """
    Returns or sets  the value indicating whether to check free edges or not 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckFreeEdges`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckFreeEdges`` 
    
    :param checkFreeEdges: 
    :type checkFreeEdges: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    CheckNonManifoldEdges: bool = ...
    """
    Returns or sets  the value indicating whether to check non-manifold edges or not 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckNonManifoldEdges`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckNonManifoldEdges`` 
    
    :param checkNonManifoldEdges: 
    :type checkNonManifoldEdges: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ComputationScope: ElementEdgeCheckBuilderScope = ...
    """
    Returns or sets  the computation scope 
    
    <hr>
    
    Getter Method
    
    Signature ``ComputationScope`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilderScope` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComputationScope`` 
    
    :param computationScope: 
    :type computationScope: :py:class:`NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilderScope` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    FreeEdgeDisplayStyle: ElementEdgeCheckBuilderEdgeDisplayStyle_Struct = ...
    """
    Returns or sets  the display style for free edges detected 
    
    <hr>
    
    Getter Method
    
    Signature ``FreeEdgeDisplayStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilderEdgeDisplayStyle_Struct` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FreeEdgeDisplayStyle`` 
    
    :param freeEdgesStyle: 
    :type freeEdgesStyle: :py:class:`NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilderEdgeDisplayStyle_Struct` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    NonManifoldEdgeDisplayStyle: ElementEdgeCheckBuilderEdgeDisplayStyle_Struct = ...
    """
    Returns or sets  the displaying style for non-manifold edges detected 
    
    <hr>
    
    Getter Method
    
    Signature ``NonManifoldEdgeDisplayStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilderEdgeDisplayStyle_Struct` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NonManifoldEdgeDisplayStyle`` 
    
    :param nonManifoldEdgeStyle: 
    :type nonManifoldEdgeStyle: :py:class:`NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilderEdgeDisplayStyle_Struct` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    SelectionList: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects to be checked.  
    
    The objects must be :py:class:`NXOpen.CAE.Mesh` or
    :py:class:`NXOpen.CAE.FEElement` 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CheckScopeOption: CheckScope = ...
    """
    Returns or sets  the check scope setting 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckScopeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckScopeOption`` 
    
    :param scope: 
    :type scope: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: ElementEdgeCheckBuilder = ...  # unknown typename


class DuplicateNodesCheckBuilderMergePreferenceMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DuplicateNodesCheckBuilderMergePreference():
    """
    Represents the duplicate nodes merging preference 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No preference"
       "KeepHighLabel", "Keep the nodes with higher labels"
       "KeepLowLabel", "Keep the nodes with lower labels"
       "KeepSelected", "Keep the nodes specified in the node list :py:meth:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.SelectPreferenceNodesList`"
       "RemoveSelected", "Merge the nodes specified in the node list :py:meth:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.SelectPreferenceNodesList`"
    """
    NotSet = 0  # DuplicateNodesCheckBuilderMergePreferenceMemberType
    KeepHighLabel = 1  # DuplicateNodesCheckBuilderMergePreferenceMemberType
    KeepLowLabel = 2  # DuplicateNodesCheckBuilderMergePreferenceMemberType
    KeepSelected = 3  # DuplicateNodesCheckBuilderMergePreferenceMemberType
    RemoveSelected = 4  # DuplicateNodesCheckBuilderMergePreferenceMemberType
    
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
    


class DuplicateNodesCheckBuilderListOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DuplicateNodesCheckBuilderListOption():
    """
    Represents the duplicate nodes merging preference 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", "List all duplicate node pairs found"
       "Mergeable", "List the duplicate node pairs mergeable"
       "Unmergeable", "List the duplicate node pairs unmergeable"
    """
    All = 0  # DuplicateNodesCheckBuilderListOptionMemberType
    Mergeable = 1  # DuplicateNodesCheckBuilderListOptionMemberType
    Unmergeable = 2  # DuplicateNodesCheckBuilderListOptionMemberType
    
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
    


class DuplicateNodesCheckBuilder(NXOpen.Builder, ISelectionBuilder):
    """
    Represents a :py:class:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder`
    to check for duplicate nodes within the candidate nodes.  
    
    Duplicate nodes are nodes which distance between each other is less than
    specific tolerance value and at least one duplicate node can be merged away.
    
    The general workflow is:
    
      #.  Set the candidate nodes 
      #.  Set the check settings and display settings data 
      #.  Identify the duplicate nodes 
      #.  Set the preference option 
      #.  Merge duplicate nodes 
    
    You can merge duplicate nodes through :py:meth:`Builder.Commit` or
    :py:meth:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.MergeDuplicateNodes`.
    Commits the builder to merge duplicate nodes and update the mesh in graphic window.
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.ModelCheckManager.CreateDuplicateNodesCheckBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class MergePreference():
        """
        Represents the duplicate nodes merging preference 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No preference"
           "KeepHighLabel", "Keep the nodes with higher labels"
           "KeepLowLabel", "Keep the nodes with lower labels"
           "KeepSelected", "Keep the nodes specified in the node list :py:meth:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.SelectPreferenceNodesList`"
           "RemoveSelected", "Merge the nodes specified in the node list :py:meth:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.SelectPreferenceNodesList`"
        """
        NotSet = 0  # DuplicateNodesCheckBuilderMergePreferenceMemberType
        KeepHighLabel = 1  # DuplicateNodesCheckBuilderMergePreferenceMemberType
        KeepLowLabel = 2  # DuplicateNodesCheckBuilderMergePreferenceMemberType
        KeepSelected = 3  # DuplicateNodesCheckBuilderMergePreferenceMemberType
        RemoveSelected = 4  # DuplicateNodesCheckBuilderMergePreferenceMemberType
        
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
        
    
    
    class ListOption():
        """
        Represents the duplicate nodes merging preference 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", "List all duplicate node pairs found"
           "Mergeable", "List the duplicate node pairs mergeable"
           "Unmergeable", "List the duplicate node pairs unmergeable"
        """
        All = 0  # DuplicateNodesCheckBuilderListOptionMemberType
        Mergeable = 1  # DuplicateNodesCheckBuilderListOptionMemberType
        Unmergeable = 2  # DuplicateNodesCheckBuilderListOptionMemberType
        
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
        
    
    
    class DisplaySettings():
        """
        Represents the display settings data .  
        
        Constructor: 
        NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.DisplaySettings()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        ShowDuplicateNodes: bool = ...
        """
        Whether to show duplicate nodes 
        <hr>
        
        Field Value
        Type:bool
        """
        ShowMergedNodeLabels: bool = ...
        """
        Whether to show merged node labels 
        <hr>
        
        Field Value
        Type:bool
        """
        ShowRetainedNodeLabels: bool = ...
        """
        Whether to show retained node labels 
        <hr>
        
        Field Value
        Type:bool
        """
        KeepNodesColor: NXOpen.NXColor = ...
        """
        The kept nodes display color 
        <hr>
        
        Field Value
        Type:Id
        """
        MergeNodesColor: NXOpen.NXColor = ...
        """
        The merged nodes display color 
        <hr>
        
        Field Value
        Type:Id
        """
        UnableToMergeNodesColor: NXOpen.NXColor = ...
        """
        Field Value
        Type:Id
        """
    
    
    def IdentifyDuplicateNodes(self) -> None:
        """
        Calculates to find the duplicate nodes and display them in
        :py:class:`NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilderDisplaySettings_Struct`.  
        
        The detected duplicate nodes are cached, to access the cached calculation result, you could use
        :py:meth:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.DuplicateNodeGroupsCount` and
        :py:meth:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.GetDuplicateNodes`. The previous
        cached data will be cleaned automatically when you start a new identification. 
        
        Signature ``IdentifyDuplicateNodes()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetDuplicateNodes(self, groupIndex: int) -> 'list[NXOpen.CAE.FENode]':
        """
        Returns the duplicate nodes of specified group index  
        
        Signature ``GetDuplicateNodes(groupIndex)`` 
        
        :param groupIndex: 
        :type groupIndex: int 
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def MergeDuplicateNodes(self) -> None:
        """
        Merges the duplicate nodes and clear all cached duplicate nodes in this builder.  
        
        The method :py:meth:`Builder.Commit` will also do the same thing. Duplicate nodes
        can only be merged when the context part of this builder is a :py:class:`NXOpen.CAE.BaseFemPart`. 
        
        Signature ``MergeDuplicateNodes()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    DisplaySettingsData: DuplicateNodesCheckBuilderDisplaySettings_Struct = ...
    """
    Returns or sets  the display settings for duplicate nodes 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplaySettingsData`` 
    
    :returns:  Display settings data  
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilderDisplaySettings_Struct` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplaySettingsData`` 
    
    :param displaySettings:  Display settings data  
    :type displaySettings: :py:class:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilderDisplaySettings_Struct` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    DuplicateNodeGroupsCount: int = ...
    """
    Returns  the duplicate nodes group count, each group contains nodes that are
    duplicates of each other and each group contains at least two duplicate nodes 
    
    <hr>
    
    Getter Method
    
    Signature ``DuplicateNodeGroupsCount`` 
    
    :returns:  Duplicate node groups count  
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    IgnoreNodesConnectedToTinyEdges: bool = ...
    """
    Returns or sets  a value indicating whether to ignore nodes connected to tiny edges 
    
    <hr>
    
    Getter Method
    
    Signature ``IgnoreNodesConnectedToTinyEdges`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IgnoreNodesConnectedToTinyEdges`` 
    
    :param ignoreTinyEdgeNodes: 
    :type ignoreTinyEdgeNodes: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    IgnoreNodesInSameMesh: bool = ...
    """
    Returns or sets  a value indicating whether to ignore nodes in same mesh 
    
    <hr>
    
    Getter Method
    
    Signature ``IgnoreNodesInSameMesh`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IgnoreNodesInSameMesh`` 
    
    :param ignoreSameMeshNodes: 
    :type ignoreSameMeshNodes: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ListingType: DuplicateNodesCheckBuilderListOption = ...
    """
    Returns or sets  an option indicating what information to be listed 
    
    <hr>
    
    Getter Method
    
    Signature ``ListingType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilderListOption` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ListingType`` 
    
    :param listOption: 
    :type listOption: :py:class:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilderListOption` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    MergeOccurrenceNodes: bool = ...
    """
    Returns or sets  a value indicating whether to merge occurrence nodes in afem context 
    
    <hr>
    
    Getter Method
    
    Signature ``MergeOccurrenceNodes`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MergeOccurrenceNodes`` 
    
    :param mergeOccurrenceNodes: 
    :type mergeOccurrenceNodes: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Preference: DuplicateNodesCheckBuilderMergePreference = ...
    """
    Returns or sets  the duplicate nodes merging preference 
    
    <hr>
    
    Getter Method
    
    Signature ``Preference`` 
    
    :returns:  Merge nodes preference  
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilderMergePreference` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Preference`` 
    
    :param mergePreference:  Merge nodes preference  
    :type mergePreference: :py:class:`NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilderMergePreference` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SelectPreferenceNodesList: NXOpen.CAE.SelectFENodeList = ...
    """
    Returns  the preference nodes select list for keep selected and remove selected options 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectPreferenceNodesList`` 
    
    :returns:  Preference nodes select list  
    :rtype: :py:class:`NXOpen.CAE.SelectFENodeList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SelectionList: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects for checking.  
    
    The objects must be :py:class:`NXOpen.CAE.Mesh` or
    :py:class:`NXOpen.CAE.FENode` 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Tolerance: NXOpen.Expression = ...
    """
    Returns  the tolerance used to determine if the nodes are duplicates of each other 
    
    <hr>
    
    Getter Method
    
    Signature ``Tolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CheckScopeOption: CheckScope = ...
    """
    Returns or sets  the check scope setting 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckScopeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckScopeOption`` 
    
    :param scope: 
    :type scope: :py:class:`NXOpen.CAE.ModelCheck.CheckScope` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: DuplicateNodesCheckBuilder = ...  # unknown typename


