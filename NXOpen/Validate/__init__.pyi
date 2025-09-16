# module 'NXOpen.Validate'
#
# Automatically generated 2025-06-09T14:38:48.488462
#
"""Default documentation for NXOpen.Validate."""

import typing

import NXOpen
import NXOpen.GeometricUtilities



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class ParserDataSourceTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ParserDataSourceTypes():
    """
    The data source type of check result. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MostRecentRun", "Result of most recent run"
       "ResultFromPart", "Result from part"
       "ResultFromTeamcenter", "Result from Teamcenter"
       "ResultFromNXChecks", "Result from NX checks"
       "ResultFromLogFile", "Result from Log File"
    """
    MostRecentRun = 0  # ParserDataSourceTypesMemberType
    ResultFromPart = 1  # ParserDataSourceTypesMemberType
    ResultFromTeamcenter = 2  # ParserDataSourceTypesMemberType
    ResultFromNXChecks = 3  # ParserDataSourceTypesMemberType
    ResultFromLogFile = 4  # ParserDataSourceTypesMemberType
    
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
    


class Parser(NXOpen.TaggedObject):
    """
    Represents a NX :py:class:`NXOpen.Validate.Parser`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Validate.ValidationManager.CreateParser`
    
    .. versionadded:: NX7.5.0
    """
    
    class DataSourceTypes():
        """
        The data source type of check result. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MostRecentRun", "Result of most recent run"
           "ResultFromPart", "Result from part"
           "ResultFromTeamcenter", "Result from Teamcenter"
           "ResultFromNXChecks", "Result from NX checks"
           "ResultFromLogFile", "Result from Log File"
        """
        MostRecentRun = 0  # ParserDataSourceTypesMemberType
        ResultFromPart = 1  # ParserDataSourceTypesMemberType
        ResultFromTeamcenter = 2  # ParserDataSourceTypesMemberType
        ResultFromNXChecks = 3  # ParserDataSourceTypesMemberType
        ResultFromLogFile = 4  # ParserDataSourceTypesMemberType
        
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
        
    
    
    def Commit(self) -> None:
        """
        Runs parsing process 
        
        Signature ``Commit()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPartResultObjects(self) -> 'list[ResultObject]':
        """
        Gets part result objects 
        
        Signature ``GetPartResultObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Validate.ResultObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetProfileResultObjects(self) -> 'list[ResultObject]':
        """
        Gets profile result objects 
        
        Signature ``GetProfileResultObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Validate.ResultObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetProfileResultObjects(self, resultObject: ResultObject) -> 'list[ResultObject]':
        """
        Gets profile result objects from input object 
        
        Signature ``GetProfileResultObjects(resultObject)`` 
        
        :param resultObject: 
        :type resultObject: :py:class:`NXOpen.Validate.ResultObject` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Validate.ResultObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetTestResultObjects(self) -> 'list[ResultObject]':
        """
        Gets test result objects 
        
        Signature ``GetTestResultObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Validate.ResultObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetTestResultObjects(self, resultObject: ResultObject) -> 'list[ResultObject]':
        """
        Gets test result objects from input object 
        
        Signature ``GetTestResultObjects(resultObject)`` 
        
        :param resultObject: 
        :type resultObject: :py:class:`NXOpen.Validate.ResultObject` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Validate.ResultObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetObjectSetResultObjects(self, resultObject: ResultObject) -> 'list[ResultObject]':
        """
        Gets entity set result objects from input object 
        
        Signature ``GetObjectSetResultObjects(resultObject)`` 
        
        :param resultObject: 
        :type resultObject: :py:class:`NXOpen.Validate.ResultObject` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Validate.ResultObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetObjectResultObjects(self, resultObject: ResultObject) -> 'list[ResultObject]':
        """
        Gets entity result objects from input object 
        
        Signature ``GetObjectResultObjects(resultObject)`` 
        
        :param resultObject: 
        :type resultObject: :py:class:`NXOpen.Validate.ResultObject` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Validate.ResultObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteResultObject(self, resultObject: ResultObject) -> NXOpen.ErrorList:
        """
        Deletes result object, return error list  
        
        Signature ``DeleteResultObject(resultObject)`` 
        
        :param resultObject: 
        :type resultObject: :py:class:`NXOpen.Validate.ResultObject` 
        :returns:  List of errors encountered during the delete  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteResult(self, resultObject: ResultObject) -> int:
        """
        Deletes result object, return error code  
        
        Signature ``DeleteResult(resultObject)`` 
        
        :param resultObject: 
        :type resultObject: :py:class:`NXOpen.Validate.ResultObject` 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX8.0.3
        
        License requirements: None.
        """
        ...
    
    
    def ClearResultObjects(self) -> None:
        """
        Clears result objects 
        
        Signature ``ClearResultObjects()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    DataSource: ParserDataSourceTypes = ...
    """
    Returns or sets  the result data source type 
    
    <hr>
    
    Getter Method
    
    Signature ``DataSource`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.ParserDataSourceTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DataSource`` 
    
    :param dataSource: 
    :type dataSource: :py:class:`NXOpen.Validate.ParserDataSourceTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    MaxDisplayObjects: int = ...
    """
    Returns or sets  the Max entity count to display of current module 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxDisplayObjects`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxDisplayObjects`` 
    
    :param maxDisplayObjects: 
    :type maxDisplayObjects: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: Parser = ...  # unknown typename


class CheckerNode(NXOpen.TransientObject):
    """
    Represents a checker that validator will use to check against part node.  
    
    Checker node contains the information of checker class name and checker parameter attribute values. 
    If the checker class is a profile which contains child checker instances, you can set the enable flags to
    the child checker instances in the profile checker class to turn on or off the child checker instances.
    
    .. versionadded:: NX7.5.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetChildCheckerInstanceNames(self) -> 'list[str]':
        """
        Gets child checker instance names in a profile checker.  
        
        Signature ``GetChildCheckerInstanceNames()`` 
        
        :returns:  The instance names of child checkers in the profile checker  
        :rtype: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetChildCheckerEnabledFlags(self) -> tuple:
        """
        Gets child checker instance names and enable flags in a profile checker.  
        
        Signature ``GetChildCheckerEnabledFlags()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (enableFlags, childCheckerInstances). enableFlags is a list of bool.   The enable flags of child checkers in the profile checker childCheckerInstances is a list of str.   The instance names of child checkers in the profile checker 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetChildCheckerEnabledFlags(self, childCheckerInstances: 'list[str]', enableFlags: 'list[bool]') -> None:
        """
        Sets child checker enable flags in a profile checker.  
        
        Signature ``SetChildCheckerEnabledFlags(childCheckerInstances, enableFlags)`` 
        
        :param childCheckerInstances:  The instance names of child checkers in the profile checker  
        :type childCheckerInstances: list of str 
        :param enableFlags:  The enable flags of child checkers in the profile checker  
        :type enableFlags: list of bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetChildCheckerEnabledFlag(self, childCheckerInstance: str) -> bool:
        """
        Gets enable flag of child checker instance in a profile checker.  
        
        Signature ``GetChildCheckerEnabledFlag(childCheckerInstance)`` 
        
        :param childCheckerInstance:  The instance name of child checker in the profile checker  
        :type childCheckerInstance: str 
        :returns:  The enable flag of child checker in the profile checker.  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetChildCheckerEnabledFlag(self, childCheckerInstance: str, enableFlag: bool) -> None:
        """
        Sets enable flag of child checker instance in a profile checker.  
        
        Signature ``SetChildCheckerEnabledFlag(childCheckerInstance, enableFlag)`` 
        
        :param childCheckerInstance:  The instance name of child checker in the profile checker  
        :type childCheckerInstance: str 
        :param enableFlag:  The enable flag of child checker in the profile checker.  
        :type enableFlag: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    AttributeCustomizedFormulas: str = ...
    """
    Returns or sets  the customized formula lines of checker.  
    
    For example:
    
    "Disabled?;False;save_log_in_part;True"
    
    For more information, see the Knowledge Fusion and NX Open section of the Knowledge Fusion Help.
    
    <hr>
    
    Getter Method
    
    Signature ``AttributeCustomizedFormulas`` 
    
    :returns:  The formula lines of checker  
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AttributeCustomizedFormulas`` 
    
    :param formulaLines:  The formula lines of checker  
    :type formulaLines: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ClassName: str = ...
    """
    Returns or sets  the checker class name 
    
    <hr>
    
    Getter Method
    
    Signature ``ClassName`` 
    
    :returns:  checker class name  
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ClassName`` 
    
    :param className:  checker class name  
    :type className: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """


class OverrideBuilderRequestTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OverrideBuilderRequestTypes():
    """
    Represents the override request type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Permanent", " - "
       "Temporary", " - "
    """
    Permanent = 0  # OverrideBuilderRequestTypesMemberType
    Temporary = 1  # OverrideBuilderRequestTypesMemberType
    
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
    


class OverrideBuilderToStatesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OverrideBuilderToStates():
    """
    Represents the override request to state 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Passed", " - "
       "Failed", " - "
    """
    Passed = 0  # OverrideBuilderToStatesMemberType
    Failed = 1  # OverrideBuilderToStatesMemberType
    
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
    


class OverrideBuilderDecisionActionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OverrideBuilderDecisionActions():
    """
    Represents the override request decision action 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Approved", " - "
       "Rejected", " - "
       "Pending", " - "
    """
    Approved = 0  # OverrideBuilderDecisionActionsMemberType
    Rejected = 1  # OverrideBuilderDecisionActionsMemberType
    Pending = 2  # OverrideBuilderDecisionActionsMemberType
    
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
    


class OverrideBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Validate.Override` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Validate.ResultObject.CreateOverrideBuilder`
    
    Default values.
    
    ============  ==========
    Property      Value
    ============  ==========
    RequestType   Permanent 
    ------------  ----------
    ToState       Passed 
    ============  ==========
    
    .. versionadded:: NX8.5.0
    """
    
    class RequestTypes():
        """
        Represents the override request type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Permanent", " - "
           "Temporary", " - "
        """
        Permanent = 0  # OverrideBuilderRequestTypesMemberType
        Temporary = 1  # OverrideBuilderRequestTypesMemberType
        
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
        
    
    
    class ToStates():
        """
        Represents the override request to state 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Passed", " - "
           "Failed", " - "
        """
        Passed = 0  # OverrideBuilderToStatesMemberType
        Failed = 1  # OverrideBuilderToStatesMemberType
        
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
        
    
    
    class DecisionActions():
        """
        Represents the override request decision action 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Approved", " - "
           "Rejected", " - "
           "Pending", " - "
        """
        Approved = 0  # OverrideBuilderDecisionActionsMemberType
        Rejected = 1  # OverrideBuilderDecisionActionsMemberType
        Pending = 2  # OverrideBuilderDecisionActionsMemberType
        
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
        
    
    
    def GetDetailReason(self) -> 'list[str]':
        """
        Returns the detail reason  
        
        Signature ``GetDetailReason()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDetailReason(self, detailReason: 'list[str]') -> None:
        """
        Sets the detail reason 
        The detail reason is optional unless override reason configuration is mandatory in Teamcenter.  
        
        Signature ``SetDetailReason(detailReason)`` 
        
        :param detailReason: 
        :type detailReason: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def GetDecisionComments(self) -> 'list[str]':
        """
        Returns the decision comments  
        
        Signature ``GetDecisionComments()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDecisionComments(self, decisionComments: 'list[str]') -> None:
        """
        Sets the decision comments 
        The decision comments is optional.  
        
        Signature ``SetDecisionComments(decisionComments)`` 
        
        :param decisionComments: 
        :type decisionComments: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    Category: str = ...
    """
    Returns or sets  the category of override request.  
    
    The category is optional unless override reason configuration is mandatory in Teamcenter.
    
    <hr>
    
    Getter Method
    
    Signature ``Category`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Category`` 
    
    :param category: 
    :type category: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ug_checkmate ("UG Check Mate")
    """
    DecisionAction: OverrideBuilderDecisionActions = ...
    """
    Returns or sets  the decision action of override request
    The decision action is automatically pending while override request is created.  
    
    If any property of override request is changed, the decision action will be pending.
    
    <hr>
    
    Getter Method
    
    Signature ``DecisionAction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.OverrideBuilderDecisionActions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DecisionAction`` 
    
    :param decisionAction: 
    :type decisionAction: :py:class:`NXOpen.Validate.OverrideBuilderDecisionActions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ug_checkmate ("UG Check Mate")
    """
    DecisionUser: str = ...
    """
    Returns or sets  the decision user 
    The decision user is a Teamcenter user in the Validation Administration group.  
    
    If the decision user is empty, it means thant any user in the group can review override request.
    
    <hr>
    
    Getter Method
    
    Signature ``DecisionUser`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DecisionUser`` 
    
    :param decisionUser: 
    :type decisionUser: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ug_checkmate ("UG Check Mate")
    """
    Reason: str = ...
    """
    Returns or sets  the reason of override request.  
    
    The reason is optional unless override reason configuration is mandatory in Teamcenter.
    
    <hr>
    
    Getter Method
    
    Signature ``Reason`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Reason`` 
    
    :param reason: 
    :type reason: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ug_checkmate ("UG Check Mate")
    """
    RequestType: OverrideBuilderRequestTypes = ...
    """
    Returns or sets  the type of override request
    
    <hr>
    
    Getter Method
    
    Signature ``RequestType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.OverrideBuilderRequestTypes` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RequestType`` 
    
    :param requestType: 
    :type requestType: :py:class:`NXOpen.Validate.OverrideBuilderRequestTypes` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ug_checkmate ("UG Check Mate")
    """
    ToState: OverrideBuilderToStates = ...
    """
    Returns or sets  the to state of override request 
    
    <hr>
    
    Getter Method
    
    Signature ``ToState`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.OverrideBuilderToStates` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToState`` 
    
    :param toState: 
    :type toState: :py:class:`NXOpen.Validate.OverrideBuilderToStates` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ug_checkmate ("UG Check Mate")
    """
    Null: OverrideBuilder = ...  # unknown typename


class RequirementCheckSaveResultsToTeamcenterOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RequirementCheckSaveResultsToTeamcenterOptions():
    """
    This enum represents the Save Results to Teamcenter option 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DoNotSave", "Do not perform save."
       "SaveIfPassed", "Perform save only if the result is passed."
       "AlwaysSave", "Always perform save"
    """
    DoNotSave = 0  # RequirementCheckSaveResultsToTeamcenterOptionsMemberType
    SaveIfPassed = 1  # RequirementCheckSaveResultsToTeamcenterOptionsMemberType
    AlwaysSave = 2  # RequirementCheckSaveResultsToTeamcenterOptionsMemberType
    
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
    


class RequirementCheck(NXOpen.Validation):
    """
    Represents an NX :py:class:`NXOpen.Validate.RequirementCheck` object.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Validate.RequirementCheckCollection.CreateRequirementCheck`
    
    .. versionadded:: NX8.5.0
    """
    
    class SaveResultsToTeamcenterOptions():
        """
        This enum represents the Save Results to Teamcenter option 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DoNotSave", "Do not perform save."
           "SaveIfPassed", "Perform save only if the result is passed."
           "AlwaysSave", "Always perform save"
        """
        DoNotSave = 0  # RequirementCheckSaveResultsToTeamcenterOptionsMemberType
        SaveIfPassed = 1  # RequirementCheckSaveResultsToTeamcenterOptionsMemberType
        AlwaysSave = 2  # RequirementCheckSaveResultsToTeamcenterOptionsMemberType
        
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
        
    
    
    def SetFormula(self, formula: str) -> None:
        """
        Sets the formula of requirement check.  
        
        The requirement check will be re-evaluated. 
        
        Signature ``SetFormula(formula)`` 
        
        :param formula: 
        :type formula: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    CheckName: str = ...
    """
    Returns or sets  the name of requirement check shown in Requirements Validation dialog 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckName`` 
    
    :param checkName: 
    :type checkName: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Formula: str = ...
    """
    Returns  the formula of requirement check 
    
    <hr>
    
    Getter Method
    
    Signature ``Formula`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ParentRequirement: Requirement = ...
    """
    Returns or sets  the parent :py:class:`NXOpen.Validate.Requirement` 
    
    <hr>
    
    Getter Method
    
    Signature ``ParentRequirement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.Requirement` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ParentRequirement`` 
    
    :param parentRequirement: 
    :type parentRequirement: :py:class:`NXOpen.Validate.Requirement` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SaveResultsToTeamcenterOption: RequirementCheckSaveResultsToTeamcenterOptions = ...
    """
    Returns or sets  the Save Results to Teamcenter option 
    
    <hr>
    
    Getter Method
    
    Signature ``SaveResultsToTeamcenterOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.RequirementCheckSaveResultsToTeamcenterOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SaveResultsToTeamcenterOption`` 
    
    :param option: 
    :type option: :py:class:`NXOpen.Validate.RequirementCheckSaveResultsToTeamcenterOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: RequirementCheck = ...  # unknown typename


class XmlComparatorOptions_Struct():
    """
    Represents config options in comparison
    
    For example:
    
    case 1: Defines filter file to control what nodes will be compared;
    generates comparison report and log; ignores CDATA and processing 
    instruction nodes.
    
    compareOptions.ReportFile           = "auto_report.html";
    compareOptions.FilterFile           = "filter.xml";
    compareOptions.LogFile              = "log.log";
    compareOptions.IgnoreNamespaces     = FALSE;
    compareOptions.IgnoreUnmatchedNodes = FALSE;
    compareOptions.IgnoreComments       = FALSE;
    compareOptions.IgnoreCdata          = TRUE;
    compareOptions.IgnorePI             = TRUE;
    CompareXmlFiles("fileOne.xml", "fileTwo.xml", compareOptions)
    
    case 2: Compares all nodes and does not generate report file and log file.
    
    compareOptions.ReportFile           = None;
    compareOptions.FilterFile           = None;
    compareOptions.LogFile              = None;
    CompareXmlFiles("fileOne.xml", "fileTwo.xml", compareOptions)
    
    .
    Constructor: 
    NXOpen.Validate.XmlComparator.Options()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    FilterFile: str = ...
    """
    File specification of filter file.  
    
    The filter file defines what nodes will be compared and how to compare them.
    It can be None, which means all nodes will be compared. 
    <hr>
    
    Field Value
    Type:str
    """
    ReportFile: str = ...
    """
    File specification of report file.  
    
    The report file contains the detail comparison results.
    It can be None, which means the comparator won't generate a report file. 
    <hr>
    
    Field Value
    Type:str
    """
    LogFile: str = ...
    """
    File specification of comparison log file.  
    
    The log file contains detail comparison steps and comparison information.
    It can be None, which means the comparator won't generate a log file. 
    <hr>
    
    Field Value
    Type:str
    """
    IgnoreNamespaces: bool = ...
    """
    Ignores namespace definition during comparison.  
    
    But if the filter file has namespace definition, the comparator will ignore
    this option and always compare the nodes with namespace definitions. Default if false. 
    <hr>
    
    Field Value
    Type:bool
    """
    IgnoreUnmatchedNodes: bool = ...
    """
    Ignores unmatched nodes in comparison.  
    
    Default is false. 
    <hr>
    
    Field Value
    Type:bool
    """
    IgnoreComments: bool = ...
    """
    Ignores comment nodes in comparison.  
    
    Default is false. 
    <hr>
    
    Field Value
    Type:bool
    """
    IgnoreCdata: bool = ...
    """
    Ignores CDATA nodes in comparison.  
    
    Default is false. 
    <hr>
    
    Field Value
    Type:bool
    """
    IgnorePI: bool = ...
    """
    Ignores processing instruction nodes in comparison.  
    
    Default is false. 
    <hr>
    
    Field Value
    Type:bool
    """


class Requirement(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.Validate.Requirement` object.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Validate.RequirementBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    def NewCheck(self, name: str, formula: str) -> RequirementCheck:
        """
        Creates a :py:class:`NXOpen.Validate.RequirementCheck` for a requirement 
        
        Signature ``NewCheck(name, formula)`` 
        
        :param name:  name of requirement check  
        :type name: str 
        :param formula:  expression or formula of the requirement check  
        :type formula: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Validate.RequirementCheck` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def Delete(self) -> None:
        """
        Deletes a user requirement and child :py:class:`NXOpen.Validate.RequirementCheck` or removes a external requirement.  
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def RefreshFromExternalSource(self) -> None:
        """
        Refreshs a requirement from external source.  
        
        Signature ``RefreshFromExternalSource()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    Null: Requirement = ...  # unknown typename


class RequirementCheckCollection(NXOpen.TaggedObjectCollection):
    """
    Represents an NX :py:class:`NXOpen.Validate.RequirementCheckCollection` object.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX8.5.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateRequirementCheck(self) -> RequirementCheck:
        """
        Create a requirement check  
        
        Signature ``CreateRequirementCheck()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Validate.RequirementCheck` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    


class ValidationManager():
    """
    Represents an object that manages validator and parser associated instance objects. 
    
    It handles the creation of new validators and parsers.
    The ValidationManager also provides :py:meth:`NXOpen.Validate.ValidationManager.FindValidator` to 
    get validators in current session.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX7.5.0
    """
    
    def CreateValidator(self, name: str) -> Validator:
        """
        Creates a validator.  
        
        Signature ``CreateValidator(name)`` 
        
        :param name:  name of the validator  
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Validate.Validator` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def CreateParser(self, name: str) -> Parser:
        """
        Creates a parser.  
        
        Signature ``CreateParser(name)`` 
        
        :param name:  name of the parser  
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Validate.Parser` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def FindValidator(self, name: str) -> 'list[Validator]':
        """
        Finds validators in current session.  
        
        It will return all validators with the same name.
        
        Signature ``FindValidator(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Validate.Validator` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def DeleteValidator(self, validator: Validator) -> None:
        """
        Deletes a validator.  
        
        Signature ``DeleteValidator(validator)`` 
        
        :param validator: 
        :type validator: :py:class:`NXOpen.Validate.Validator` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def DeleteParser(self, parser: Parser) -> None:
        """
        Deletes a parser.  
        
        Signature ``DeleteParser(parser)`` 
        
        :param parser: 
        :type parser: :py:class:`NXOpen.Validate.Parser` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def FindParser(self, name: str) -> 'list[Parser]':
        """
        Finds parsers in current session.  
        
        It will return all parsers with the same name.
        
        Signature ``FindParser(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Validate.Parser` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    


class Override(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.Validate.Override` object.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Validate.OverrideBuilder`
    
    .. versionadded:: NX8.5.0
    """
    Null: Override = ...  # unknown typename


class RequirementCollectionSourceTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RequirementCollectionSourceTypeOptions():
    """
    This enum represents the type of external source where requirement is defined 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "LocalFile", " - "
       "TeamcenterFile", " - "
       "Teamcenter", " - "
       "MeasurableAttribute", " - "
    """
    LocalFile = 0  # RequirementCollectionSourceTypeOptionsMemberType
    TeamcenterFile = 1  # RequirementCollectionSourceTypeOptionsMemberType
    Teamcenter = 2  # RequirementCollectionSourceTypeOptionsMemberType
    MeasurableAttribute = 3  # RequirementCollectionSourceTypeOptionsMemberType
    
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
    


class RequirementCollection(NXOpen.TaggedObjectCollection):
    """
    Represents an NX :py:class:`NXOpen.Validate.RequirementCollection` object.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX8.5.0
    """
    
    class SourceTypeOptions():
        """
        This enum represents the type of external source where requirement is defined 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "LocalFile", " - "
           "TeamcenterFile", " - "
           "Teamcenter", " - "
           "MeasurableAttribute", " - "
        """
        LocalFile = 0  # RequirementCollectionSourceTypeOptionsMemberType
        TeamcenterFile = 1  # RequirementCollectionSourceTypeOptionsMemberType
        Teamcenter = 2  # RequirementCollectionSourceTypeOptionsMemberType
        MeasurableAttribute = 3  # RequirementCollectionSourceTypeOptionsMemberType
        
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
        
    
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateRequirementBuilder(self, requirement: Requirement) -> RequirementBuilder:
        """
        Creates a :py:class:`NXOpen.Validate.RequirementBuilder`  
        
        Signature ``CreateRequirementBuilder(requirement)`` 
        
        :param requirement: 
        :type requirement: :py:class:`NXOpen.Validate.Requirement` 
        :returns: 
        :rtype: :py:class:`NXOpen.Validate.RequirementBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, id: str) -> Requirement:
        """
        Finds the :py:class:`NXOpen.Validate.Requirement` with the given identifier.  
        
        An exception will be thrown if no object can be found with given identifier.  
        
        Signature ``FindObject(id)`` 
        
        :param id:  The identifier of the :py:class:`NXOpen.Validate.Requirement`  
        :type id: str 
        :returns:  :py:class:`NXOpen.Validate.Requirement` with the identifier  
        :rtype: :py:class:`NXOpen.Validate.Requirement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def LoadFromExternalSource(self, sourceType: RequirementCollectionSourceTypeOptions, source: str, revision: str, project: str) -> None:
        """
        Loads :py:class:`NXOpen.Validate.Requirement` from external source.  
        
        The source can be local file, Teamcenter requirement item or item revision, and Teamcenter spreadsheet dataset
        for which the input sourceType is LocalFile, Teamcenter and TeamcenterFile respectively.
        <br/>
        
        Example inputs when sourceType is LocalFile
        
          #. source: "C:\requirement.xml" or "C:\requirement_spreadsheet.xls"
          #. revision: empty string
          #. project: "category_A" It's a project node name in the source XML file or a sheet name in the source spreadsheet file.
        
        <br/>
        
        Example inputs when sourceType is Teamcenter
        
        If source is item revision 000084/A:
        
          #. source: "000084"
          #. revision: "A"
          #. project: empty string
        
        If source is item 000084:
        
          #. source: "000084"
          #. revision:empty string
          #. project: empty string
        
        <br/>
        Example inputs when sourceType is TeamcenterFile
        
        If source is a spreadsheet dataset in an item revision 000085/A:
        
          #. source: 000085
          #. revision: A
          #. project: "category_A" It's a sheet name in the source spreadsheet.
        
        If source is a spreadsheet dataset in item 000085:
        
          #. source: "000085"
          #. revision: empty string
          #. project: "category_A" It's a sheet name in the source spreadsheet.
        
        Signature ``LoadFromExternalSource(sourceType, source, revision, project)`` 
        
        :param sourceType:  Type of the external source  
        :type sourceType: :py:class:`NXOpen.Validate.RequirementCollectionSourceTypeOptions` 
        :param source:  File full path if sourceType is LocalFile; Item id if sourceType is Teamcenter or TeamcenterFile.  
        :type source: str 
        :param revision:  Only needed if sourceType is Teamcenter or TeamcenterFile. Revision id if source is an item revision. Null if source is an item.  
        :type revision: str 
        :param project:  Required if sourceType is LocalFile or TeamcenterFile.                                                                            Project name if the source is a XML file; Sheet name if source is a spreadsheet file.  
        :type project: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def RefreshFromExternalSource(self, requirementTags: 'list[Requirement]') -> None:
        """
        Refreshes the requirements from external source.  
        
        Signature ``RefreshFromExternalSource(requirementTags)`` 
        
        :param requirementTags: 
        :type requirementTags: list of :py:class:`NXOpen.Validate.Requirement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    RevisionRule: str = ...
    """
    Returns or sets  the revision rule for requirement from Teamcenter 
    
    <hr>
    
    Getter Method
    
    Signature ``RevisionRule`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RevisionRule`` 
    
    :param rule: 
    :type rule: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """


class PartNode(NXOpen.TransientObject):
    """
    Represents a part file that validator will check against.  
    
    Part node contains the information of part filename and part object. 
    You can create the part node by inputting part filename, or by inputting part object, or by inputting both.
    Validator will use the part object in the part node for checking. Only when the part object in the part node
    is None, then validator will use the part filename for checking.
    
    .. versionadded:: NX7.5.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    FileName: str = ...
    """
    Returns or sets  the part file name 
    
    <hr>
    
    Getter Method
    
    Signature ``FileName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FileName`` 
    
    :param fileName: 
    :type fileName: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PartObject: NXOpen.Part = ...
    """
    Returns or sets  the part object 
    
    <hr>
    
    Getter Method
    
    Signature ``PartObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PartObject`` 
    
    :param partObject: 
    :type partObject: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """


class Validator(NXOpen.TaggedObject):
    """
    Represents a NX :py:class:`NXOpen.Validate.Validator`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Validate.ValidationManager.CreateValidator`
    
    .. versionadded:: NX7.5.0
    """
    
    def Commit(self) -> NXOpen.ValidationResult:
        """
        Runs checking process and returns the checking status.  
        
        If failed checking statuses are found, it will return :py:class:`NXOpen.ValidationResult.Failed <NXOpen.ValidationResult>`. 
        Otherwise it will return :py:class:`NXOpen.ValidationResult.Pass <NXOpen.ValidationResult>`. 
        Call :py:meth:`NXOpen.Validate.Validator.GetLastErrorListFromCommit` for the execeptions happened during the checking process.
        
        Signature ``Commit()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ValidationResult` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def GetLastErrorListFromCommit(self) -> NXOpen.ErrorList:
        """
        Return the list of errors happened during last :py:meth:`NXOpen.Validate.Validator.Commit`.  
        
        Signature ``GetLastErrorListFromCommit()`` 
        
        :returns:  List of errors encountered during the checking process  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    @typing.overload
    def AppendPartNode(self, fileName: str) -> None:
        """
        Adds part node by part file name 
        
        Signature ``AppendPartNode(fileName)`` 
        
        :param fileName: 
        :type fileName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def AppendPartNode(self, partObject: NXOpen.Part) -> None:
        """
        Adds part node by part object 
        
        Signature ``AppendPartNode(partObject)`` 
        
        :param partObject: 
        :type partObject: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def AppendPartNodes(self, fileNames: 'list[str]') -> None:
        """
        Adds part nodes by part file names 
        
        Signature ``AppendPartNodes(fileNames)`` 
        
        :param fileNames: 
        :type fileNames: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def AppendPartNodes(self, partObject: 'list[NXOpen.Part]') -> None:
        """
        Adds part nodes by part objects 
        
        Signature ``AppendPartNodes(partObject)`` 
        
        :param partObject: 
        :type partObject: list of :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ErasePartNode(self, index: int) -> None:
        """
        Removes a part node 
        
        Signature ``ErasePartNode(index)`` 
        
        :param index: 
        :type index: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearPartNodes(self) -> None:
        """
        Clears part nodes 
        
        Signature ``ClearPartNodes()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def FindPartNode(self, index: int) -> PartNode:
        """
        Finds a part node  
        
        Signature ``FindPartNode(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Validate.PartNode` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPartNodes(self) -> 'list[PartNode]':
        """
        Returns all part nodes.  
        
        Signature ``GetPartNodes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Validate.PartNode` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def AppendCheckerNode(self, className: str) -> None:
        """
        Adds a checker node.  
        
        Signature ``AppendCheckerNode(className)`` 
        
        :param className:  checker class name  
        :type className: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def AppendCheckerNodes(self, classNames: 'list[str]') -> None:
        """
        Adds checker nodes.  
        
        Signature ``AppendCheckerNodes(classNames)`` 
        
        :param classNames:  checkers' class name array  
        :type classNames: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def EraseCheckerNode(self, delNdx: int) -> None:
        """
        Removes a checker node.  
        
        Signature ``EraseCheckerNode(delNdx)`` 
        
        :param delNdx: 
        :type delNdx: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def ClearCheckerNodes(self) -> None:
        """
        Clears checker nodes 
        
        Signature ``ClearCheckerNodes()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def FindCheckerNode(self, index: int) -> CheckerNode:
        """
        Returns a checker node.  
        
        Signature ``FindCheckerNode(index)`` 
        
        :param index: 
        :type index: int 
        :returns:  checker node  
        :rtype: :py:class:`NXOpen.Validate.CheckerNode` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def GetCheckerNodes(self) -> 'list[CheckerNode]':
        """
        Returns all checker nodes.  
        
        Signature ``GetCheckerNodes()`` 
        
        :returns:  checker name array  
        :rtype: list of :py:class:`NXOpen.Validate.CheckerNode` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    ValidatorOptions: ValidatorOptions = ...
    """
    Returns  the run options.  
    
    <hr>
    
    Getter Method
    
    Signature ``ValidatorOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.ValidatorOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_checkmate ("UG Check Mate")
    """
    Null: Validator = ...  # unknown typename


class ValidatorOptionsLogModeTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ValidatorOptionsLogModeTypes():
    """
    The log mode type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "LogPerSession", "Generate log per session"
       "LogPerPart", "Generate log per part"
    """
    LogPerSession = 0  # ValidatorOptionsLogModeTypesMemberType
    LogPerPart = 1  # ValidatorOptionsLogModeTypesMemberType
    
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
    


class ValidatorOptionsSaveModeTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ValidatorOptionsSaveModeTypes():
    """
    The save mode type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DoNotSave", "Do not perform save."
       "SaveIfPassed", "Perform save only if the checking is passed."
       "AlwaysSave", "Always perform save"
    """
    DoNotSave = 0  # ValidatorOptionsSaveModeTypesMemberType
    SaveIfPassed = 1  # ValidatorOptionsSaveModeTypesMemberType
    AlwaysSave = 2  # ValidatorOptionsSaveModeTypesMemberType
    
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
    


class ValidatorOptionsResultsDisplayModeTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ValidatorOptionsResultsDisplayModeTypes():
    """
    The results display mode type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AlwaysDisplay", "Always display results."
       "DisplayIfNotPass", "Display results if the checking is not passed."
       "DoNotDisplay", "Do not display results"
    """
    AlwaysDisplay = 0  # ValidatorOptionsResultsDisplayModeTypesMemberType
    DisplayIfNotPass = 1  # ValidatorOptionsResultsDisplayModeTypesMemberType
    DoNotDisplay = 2  # ValidatorOptionsResultsDisplayModeTypesMemberType
    
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
    


class ValidatorOptions(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Contains information about run options of check-mate checking process.  
    
    .. versionadded:: NX7.5.0
    """
    
    class LogModeTypes():
        """
        The log mode type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "LogPerSession", "Generate log per session"
           "LogPerPart", "Generate log per part"
        """
        LogPerSession = 0  # ValidatorOptionsLogModeTypesMemberType
        LogPerPart = 1  # ValidatorOptionsLogModeTypesMemberType
        
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
        
    
    
    class SaveModeTypes():
        """
        The save mode type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DoNotSave", "Do not perform save."
           "SaveIfPassed", "Perform save only if the checking is passed."
           "AlwaysSave", "Always perform save"
        """
        DoNotSave = 0  # ValidatorOptionsSaveModeTypesMemberType
        SaveIfPassed = 1  # ValidatorOptionsSaveModeTypesMemberType
        AlwaysSave = 2  # ValidatorOptionsSaveModeTypesMemberType
        
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
        
    
    
    class ResultsDisplayModeTypes():
        """
        The results display mode type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AlwaysDisplay", "Always display results."
           "DisplayIfNotPass", "Display results if the checking is not passed."
           "DoNotDisplay", "Do not display results"
        """
        AlwaysDisplay = 0  # ValidatorOptionsResultsDisplayModeTypesMemberType
        DisplayIfNotPass = 1  # ValidatorOptionsResultsDisplayModeTypesMemberType
        DoNotDisplay = 2  # ValidatorOptionsResultsDisplayModeTypesMemberType
        
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
    
    AutoDisplayResults: ValidatorOptionsResultsDisplayModeTypes = ...
    """
    Returns or sets  the configuration of auto display results 
    
    <hr>
    
    Getter Method
    
    Signature ``AutoDisplayResults`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.ValidatorOptionsResultsDisplayModeTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutoDisplayResults`` 
    
    :param displayResults: 
    :type displayResults: :py:class:`NXOpen.Validate.ValidatorOptionsResultsDisplayModeTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ExcludeNonOwnerParts: bool = ...
    """
    Returns or sets  the configuration of excluding parts not owned by the user.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExcludeNonOwnerParts`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExcludeNonOwnerParts`` 
    
    :param excludeNonOwnerParts: 
    :type excludeNonOwnerParts: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ExcludeReadonlyParts: bool = ...
    """
    Returns or sets  the configuration of excluding read-only parts.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExcludeReadonlyParts`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExcludeReadonlyParts`` 
    
    :param excludeReadonlyParts:  checksum of parameter  
    :type excludeReadonlyParts: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    GenerateCheckFlag: bool = ...
    """
    Returns or sets  the configuration of generating check flag if checking results are PASS 
    
    <hr>
    
    Getter Method
    
    Signature ``GenerateCheckFlag`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GenerateCheckFlag`` 
    
    :param generateCheckFlag: 
    :type generateCheckFlag: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    GenerateLogFile: bool = ...
    """
    Returns or sets  the configuration of generating log file after checking.  
    
    If True, log file will be generated. 
    
    <hr>
    
    Getter Method
    
    Signature ``GenerateLogFile`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GenerateLogFile`` 
    
    :param generateLogFile: 
    :type generateLogFile: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    LogFileDirectory: str = ...
    """
    Returns or sets  the configuration of log file directory where the log file will be saved.  
    
    <hr>
    
    Getter Method
    
    Signature ``LogFileDirectory`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LogFileDirectory`` 
    
    :param logFileDirectory: 
    :type logFileDirectory: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    LogFileMode: ValidatorOptionsLogModeTypes = ...
    """
    Returns or sets  the configuration of log file mode how to generate the log files.  
    
    <hr>
    
    Getter Method
    
    Signature ``LogFileMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.ValidatorOptionsLogModeTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LogFileMode`` 
    
    :param logFileMode: 
    :type logFileMode: :py:class:`NXOpen.Validate.ValidatorOptionsLogModeTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ResultsAutoUpdate: bool = ...
    """
    Returns or sets  the configuration of results auto update when work part change 
    
    <hr>
    
    Getter Method
    
    Signature ``ResultsAutoUpdate`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ResultsAutoUpdate`` 
    
    :param autoUpdate: 
    :type autoUpdate: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SavePartFile: ValidatorOptionsSaveModeTypes = ...
    """
    Returns or sets  the configuration of saving part file after checking finished.  
    
    If True, part file will be saved. 
    
    <hr>
    
    Getter Method
    
    Signature ``SavePartFile`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.ValidatorOptionsSaveModeTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SavePartFile`` 
    
    :param savePartFile: 
    :type savePartFile: :py:class:`NXOpen.Validate.ValidatorOptionsSaveModeTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SaveResultInPart: bool = ...
    """
    Returns or sets  the configuration of saving check results into part file.  
    
    If True, results will be saved in part file after checking finished. 
    
    <hr>
    
    Getter Method
    
    Signature ``SaveResultInPart`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SaveResultInPart`` 
    
    :param saveResultInPart:  checksum of parameter  
    :type saveResultInPart: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SaveResultInTeamcenter: ValidatorOptionsSaveModeTypes = ...
    """
    Returns or sets  the configuration of saving check results into Teamcenter.  
    
    If true, results will be saved into Teamcenter.
    This parameter is for NX Manager mode only 
    
    <hr>
    
    Getter Method
    
    Signature ``SaveResultInTeamcenter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.ValidatorOptionsSaveModeTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SaveResultInTeamcenter`` 
    
    :param saveResultInTeamcenter: 
    :type saveResultInTeamcenter: :py:class:`NXOpen.Validate.ValidatorOptionsSaveModeTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SkipChecking: bool = ...
    """
    Returns or sets  the configuration of skip checking based on result up-to-date status.  
    
    If True, checking will be skipped if the results are PASS and up-to-date. 
    
    <hr>
    
    Getter Method
    
    Signature ``SkipChecking`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SkipChecking`` 
    
    :param skipChecking: 
    :type skipChecking: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SkipCheckingDontLoadPart: bool = ...
    """
    Returns or sets  the configuration of skipping checking without loading parts 
    
    <hr>
    
    Getter Method
    
    Signature ``SkipCheckingDontLoadPart`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SkipCheckingDontLoadPart`` 
    
    :param skipCheckingDontLoadPart: 
    :type skipCheckingDontLoadPart: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SkipOverriddenResultOption: bool = ...
    """
    Returns or sets   the configuration of skip checking based on result overriden state.  
    
    If True, checking will be skipped if the results are overridden. 
    
    <hr>
    
    Getter Method
    
    Signature ``SkipOverriddenResultOption`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SkipOverriddenResultOption`` 
    
    :param skipOverriddenResult: 
    :type skipOverriddenResult: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StopOnError: bool = ...
    """
    Returns or sets  the configuration of stopping checking process on error status.  
    
    If True, stop checking when there is checker returned error status. 
    
    <hr>
    
    Getter Method
    
    Signature ``StopOnError`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StopOnError`` 
    
    :param stopOnError:  checksum of parameter  
    :type stopOnError: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    StopOnWarning: bool = ...
    """
    Returns or sets  the configuration of stopping checking on warning status.  
    
    If True, stop checking when there is checker returned warning status. 
    
    <hr>
    
    Getter Method
    
    Signature ``StopOnWarning`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StopOnWarning`` 
    
    :param stopOnWarning: 
    :type stopOnWarning: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    TreatWarningAsFail: bool = ...
    """
    Returns or sets  the configuration of treating warning status as fail status.  
    
    <hr>
    
    Getter Method
    
    Signature ``TreatWarningAsFail`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TreatWarningAsFail`` 
    
    :param treatWarningAsFail: 
    :type treatWarningAsFail: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: ValidatorOptions = ...  # unknown typename


class ResultObjectResultTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ResultObjectResultTypes():
    """
    The type of check result 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Part", "Part"
       "Profile", "Profile"
       "Test", "Test"
       "Object", "Object"
       "ObjectSet", "Object Set"
    """
    Part = 0  # ResultObjectResultTypesMemberType
    Profile = 1  # ResultObjectResultTypesMemberType
    Test = 2  # ResultObjectResultTypesMemberType
    Object = 3  # ResultObjectResultTypesMemberType
    ObjectSet = 4  # ResultObjectResultTypesMemberType
    
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
    


class ResultObject(NXOpen.NXObject):
    """
    Represents a check-mate result object.  
    
    .. versionadded:: NX7.5.0
    """
    
    class ResultTypes():
        """
        The type of check result 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Part", "Part"
           "Profile", "Profile"
           "Test", "Test"
           "Object", "Object"
           "ObjectSet", "Object Set"
        """
        Part = 0  # ResultObjectResultTypesMemberType
        Profile = 1  # ResultObjectResultTypesMemberType
        Test = 2  # ResultObjectResultTypesMemberType
        Object = 3  # ResultObjectResultTypesMemberType
        ObjectSet = 4  # ResultObjectResultTypesMemberType
        
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
        
    
    
    def CreateOverrideBuilder(self, overrideRequest: Override) -> OverrideBuilder:
        """
        Creates a :py:class:`NXOpen.Validate.OverrideBuilder`  
        
        Signature ``CreateOverrideBuilder(overrideRequest)`` 
        
        :param overrideRequest: 
        :type overrideRequest: :py:class:`NXOpen.Validate.Override` 
        :returns: 
        :rtype: :py:class:`NXOpen.Validate.OverrideBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    
    def DeleteOverride(self) -> None:
        """
        Deletes user override request :py:class:`NXOpen.Validate.Override`.  
        
        Signature ``DeleteOverride()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_checkmate ("UG Check Mate")
        """
        ...
    
    CategoryName: str = ...
    """
    Returns  the category name of check result.  
    
    Return empty if the ResultObject has no this property.
    
    <hr>
    
    Getter Method
    
    Signature ``CategoryName`` 
    
    :returns:  the category name of check result  
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ClassName: str = ...
    """
    Returns  the class name of check result.  
    
    Return empty if the ResultObject has no this property.
    
    <hr>
    
    Getter Method
    
    Signature ``ClassName`` 
    
    :returns:  the class name of check result  
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Disabled: bool = ...
    """
    Returns  the disabled status of check result.  
    
    <hr>
    
    Getter Method
    
    Signature ``Disabled`` 
    
    :returns:  the disabled of check result  
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Name: str = ...
    """
    Returns or sets  the name of check result 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  The name of check result  
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.NXObject.Name`` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name:  The name of check result  
    :type name: str 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.NXObject.Name`` instead.
    
    License requirements: None.
    """
    OutOfDate: bool = ...
    """
    Returns  the out of date status of check result.  
    
    Returns error code if part is unloaded. Result of unloaded part is assumed up to date. The program may not be able to detect the modifications in the part.
    
    <hr>
    
    Getter Method
    
    Signature ``OutOfDate`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Override: Override = ...
    """
    Returns  the override request object of check result 
    
    <hr>
    
    Getter Method
    
    Signature ``Override`` 
    
    :returns:  the Override request object of check result  
    :rtype: :py:class:`NXOpen.Validate.Override` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Status: NXOpen.ValidationResult = ...
    """
    Returns or sets  the error status of check result 
    
    <hr>
    
    Getter Method
    
    Signature ``Status`` 
    
    :returns:  The error level  
    :rtype: :py:class:`NXOpen.ValidationResult` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Status`` 
    
    :param status:  The error level  
    :type status: :py:class:`NXOpen.ValidationResult` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    TotalObjectsCount: int = ...
    """
    Returns  the total objects count of check result.  
    
    Return zero if the ResultObject has no this property.
    
    <hr>
    
    Getter Method
    
    Signature ``TotalObjectsCount`` 
    
    :returns:  the total objects count of check result  
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Type: ResultObjectResultTypes = ...
    """
    Returns or sets  the type of check result 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns:  The result type  
    :rtype: :py:class:`NXOpen.Validate.ResultObjectResultTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type:  The result type  
    :type type: :py:class:`NXOpen.Validate.ResultObjectResultTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: ResultObject = ...  # unknown typename


class RequirementBuilderSeverityOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RequirementBuilderSeverityOptions():
    """
    This enum represents the severity level when a requirement is not satisfied 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Error", " - "
       "Warning", " - "
       "Information", " - "
    """
    Error = 0  # RequirementBuilderSeverityOptionsMemberType
    Warning = 1  # RequirementBuilderSeverityOptionsMemberType
    Information = 2  # RequirementBuilderSeverityOptionsMemberType
    
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
    


class RequirementBuilderDataTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RequirementBuilderDataTypeOptions():
    """
    This enum represents the data type of the value in requirement 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Number", " - "
       "String", " - "
       "Boolean", " - "
       "Integer", " - "
       "Point", " - "
    """
    Number = 0  # RequirementBuilderDataTypeOptionsMemberType
    String = 1  # RequirementBuilderDataTypeOptionsMemberType
    Boolean = 2  # RequirementBuilderDataTypeOptionsMemberType
    Integer = 3  # RequirementBuilderDataTypeOptionsMemberType
    Point = 4  # RequirementBuilderDataTypeOptionsMemberType
    
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
    


class RequirementBuilderDefinitionMethodOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RequirementBuilderDefinitionMethodOptions():
    """
    This enum represents the type of requirement definition method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SingleSidedComparison", " - "
       "DoubleSidedComparison", " - "
       "SetOfValues", " - "
       "Formula", " - "
    """
    SingleSidedComparison = 0  # RequirementBuilderDefinitionMethodOptionsMemberType
    DoubleSidedComparison = 1  # RequirementBuilderDefinitionMethodOptionsMemberType
    SetOfValues = 2  # RequirementBuilderDefinitionMethodOptionsMemberType
    Formula = 3  # RequirementBuilderDefinitionMethodOptionsMemberType
    
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
    


class RequirementBuilderRelationalOperatorOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RequirementBuilderRelationalOperatorOptions():
    """
    This enum represents the relational operator for comparing values 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Equal", " - "
       "NotEqual", " - "
       "LessThan", " - "
       "LessThanOrEqual", " - "
       "GreaterThan", " - "
       "GreaterThanOrEqual", " - "
    """
    Equal = 0  # RequirementBuilderRelationalOperatorOptionsMemberType
    NotEqual = 1  # RequirementBuilderRelationalOperatorOptionsMemberType
    LessThan = 2  # RequirementBuilderRelationalOperatorOptionsMemberType
    LessThanOrEqual = 3  # RequirementBuilderRelationalOperatorOptionsMemberType
    GreaterThan = 4  # RequirementBuilderRelationalOperatorOptionsMemberType
    GreaterThanOrEqual = 5  # RequirementBuilderRelationalOperatorOptionsMemberType
    
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
    


class RequirementBuilderRequirementTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RequirementBuilderRequirementTypeOptions():
    """
    This enum represents the type of requirement 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ValidationLimit", " - "
       "DesignLimit", " - "
    """
    ValidationLimit = 0  # RequirementBuilderRequirementTypeOptionsMemberType
    DesignLimit = 1  # RequirementBuilderRequirementTypeOptionsMemberType
    
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
    


class RequirementBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Validate.Requirement` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Validate.RequirementCollection.CreateRequirementBuilder`
    
    Default values.
    
    =======================================  ======================
    Property                                 Value
    =======================================  ======================
    DataTypeOption                           Number 
    ---------------------------------------  ----------------------
    DefinitionMethodOption                   SingleSidedComparison 
    ---------------------------------------  ----------------------
    RelationalOperatorOption                 Equal 
    ---------------------------------------  ----------------------
    RelationalOperatorOptionOnMaximumValue   LessThan 
    ---------------------------------------  ----------------------
    RelationalOperatorOptionOnMinimumValue   LessThan 
    ---------------------------------------  ----------------------
    SeverityOption                           Error 
    =======================================  ======================
    
    .. versionadded:: NX8.5.0
    """
    
    class SeverityOptions():
        """
        This enum represents the severity level when a requirement is not satisfied 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Error", " - "
           "Warning", " - "
           "Information", " - "
        """
        Error = 0  # RequirementBuilderSeverityOptionsMemberType
        Warning = 1  # RequirementBuilderSeverityOptionsMemberType
        Information = 2  # RequirementBuilderSeverityOptionsMemberType
        
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
        
    
    
    class DataTypeOptions():
        """
        This enum represents the data type of the value in requirement 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Number", " - "
           "String", " - "
           "Boolean", " - "
           "Integer", " - "
           "Point", " - "
        """
        Number = 0  # RequirementBuilderDataTypeOptionsMemberType
        String = 1  # RequirementBuilderDataTypeOptionsMemberType
        Boolean = 2  # RequirementBuilderDataTypeOptionsMemberType
        Integer = 3  # RequirementBuilderDataTypeOptionsMemberType
        Point = 4  # RequirementBuilderDataTypeOptionsMemberType
        
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
        
    
    
    class DefinitionMethodOptions():
        """
        This enum represents the type of requirement definition method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SingleSidedComparison", " - "
           "DoubleSidedComparison", " - "
           "SetOfValues", " - "
           "Formula", " - "
        """
        SingleSidedComparison = 0  # RequirementBuilderDefinitionMethodOptionsMemberType
        DoubleSidedComparison = 1  # RequirementBuilderDefinitionMethodOptionsMemberType
        SetOfValues = 2  # RequirementBuilderDefinitionMethodOptionsMemberType
        Formula = 3  # RequirementBuilderDefinitionMethodOptionsMemberType
        
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
        
    
    
    class RelationalOperatorOptions():
        """
        This enum represents the relational operator for comparing values 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Equal", " - "
           "NotEqual", " - "
           "LessThan", " - "
           "LessThanOrEqual", " - "
           "GreaterThan", " - "
           "GreaterThanOrEqual", " - "
        """
        Equal = 0  # RequirementBuilderRelationalOperatorOptionsMemberType
        NotEqual = 1  # RequirementBuilderRelationalOperatorOptionsMemberType
        LessThan = 2  # RequirementBuilderRelationalOperatorOptionsMemberType
        LessThanOrEqual = 3  # RequirementBuilderRelationalOperatorOptionsMemberType
        GreaterThan = 4  # RequirementBuilderRelationalOperatorOptionsMemberType
        GreaterThanOrEqual = 5  # RequirementBuilderRelationalOperatorOptionsMemberType
        
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
        
    
    
    class RequirementTypeOptions():
        """
        This enum represents the type of requirement 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ValidationLimit", " - "
           "DesignLimit", " - "
        """
        ValidationLimit = 0  # RequirementBuilderRequirementTypeOptionsMemberType
        DesignLimit = 1  # RequirementBuilderRequirementTypeOptionsMemberType
        
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
        
    
    
    def GetValidValues(self) -> 'list[str]':
        """
        Returns the valid values  
        
        Signature ``GetValidValues()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValidValues(self, validValues: 'list[str]') -> None:
        """
        Sets the valid values 
        
        Signature ``SetValidValues(validValues)`` 
        
        :param validValues: 
        :type validValues: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRequirementDescription(self) -> 'list[str]':
        """
        Returns the requirement description  
        
        Signature ``GetRequirementDescription()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRequirementDescription(self, requirementDescription: 'list[str]') -> None:
        """
        Sets the requirement description 
        
        Signature ``SetRequirementDescription(requirementDescription)`` 
        
        :param requirementDescription: 
        :type requirementDescription: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    DataTypeOption: RequirementBuilderDataTypeOptions = ...
    """
    Returns or sets  the data type option 
    
    <hr>
    
    Getter Method
    
    Signature ``DataTypeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.RequirementBuilderDataTypeOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DataTypeOption`` 
    
    :param dataTypeOption: 
    :type dataTypeOption: :py:class:`NXOpen.Validate.RequirementBuilderDataTypeOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DefinitionMethodOption: RequirementBuilderDefinitionMethodOptions = ...
    """
    Returns or sets  the definition method option 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionMethodOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.RequirementBuilderDefinitionMethodOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefinitionMethodOption`` 
    
    :param definitionMethodOption: 
    :type definitionMethodOption: :py:class:`NXOpen.Validate.RequirementBuilderDefinitionMethodOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DoubleSidedMaximumValue: str = ...
    """
    Returns or sets  the maximum value in double sided comparison 
    
    <hr>
    
    Getter Method
    
    Signature ``DoubleSidedMaximumValue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DoubleSidedMaximumValue`` 
    
    :param doubleSidedMaximumValue: 
    :type doubleSidedMaximumValue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DoubleSidedMinimumValue: str = ...
    """
    Returns or sets  the minimum value in double sided comparison 
    
    <hr>
    
    Getter Method
    
    Signature ``DoubleSidedMinimumValue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DoubleSidedMinimumValue`` 
    
    :param doubleSidedMinimumValue: 
    :type doubleSidedMinimumValue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Formula: str = ...
    """
    Returns or sets  the user defined formula. Only effective when 
    :py:meth:`NXOpen.Validate.RequirementBuilder.DefinitionMethodOption`` is set to 
    :py:class:`NXOpen.Validate.RequirementBuilderDefinitionMethodOptions.Formula <NXOpen.Validate.RequirementBuilderDefinitionMethodOptions>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``Formula`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Formula`` 
    
    :param formula: 
    :type formula: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Name: str = ...
    """
    Returns or sets  the name of requirement 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RelationalOperatorOption: RequirementBuilderRelationalOperatorOptions = ...
    """
    Returns or sets  the relational operator option between expression label and the value in single sided comparison 
    
    <hr>
    
    Getter Method
    
    Signature ``RelationalOperatorOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.RequirementBuilderRelationalOperatorOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RelationalOperatorOption`` 
    
    :param relationalOperatorOption: 
    :type relationalOperatorOption: :py:class:`NXOpen.Validate.RequirementBuilderRelationalOperatorOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RelationalOperatorOptionOnMaximumValue: RequirementBuilderRelationalOperatorOptions = ...
    """
    Returns or sets  the relational operator between expression label and maximum value in double sided comparison:
    [expression] &lt; or &lt;= maximum value.  
    
    The valid operator is either LessThan or LessThanOrEqual.
    
    <hr>
    
    Getter Method
    
    Signature ``RelationalOperatorOptionOnMaximumValue`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.RequirementBuilderRelationalOperatorOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RelationalOperatorOptionOnMaximumValue`` 
    
    :param relationalOperatorOnMaximumValue: 
    :type relationalOperatorOnMaximumValue: :py:class:`NXOpen.Validate.RequirementBuilderRelationalOperatorOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RelationalOperatorOptionOnMinimumValue: RequirementBuilderRelationalOperatorOptions = ...
    """
    Returns or sets  the relational operator between minimum value and expression label in double sided comparison:
    minimum value &lt; or &lt;= [expression].  
    
    The valid operator is either LessThan or LessThanOrEqual.
    
    <hr>
    
    Getter Method
    
    Signature ``RelationalOperatorOptionOnMinimumValue`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.RequirementBuilderRelationalOperatorOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RelationalOperatorOptionOnMinimumValue`` 
    
    :param relationalOperatorOnMinimumValue: 
    :type relationalOperatorOnMinimumValue: :py:class:`NXOpen.Validate.RequirementBuilderRelationalOperatorOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RequirementTolerance: float = ...
    """
    Returns or sets  the tolerance for point type requirement 
    
    <hr>
    
    Getter Method
    
    Signature ``RequirementTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RequirementTolerance`` 
    
    :param requirementTolerance:  tolerance value to be set on requirement  
    :type requirementTolerance: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RequirementTypeOption: RequirementBuilderRequirementTypeOptions = ...
    """
    Returns or sets  the requirement type option 
    
    <hr>
    
    Getter Method
    
    Signature ``RequirementTypeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.RequirementBuilderRequirementTypeOptions` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RequirementTypeOption`` 
    
    :param requirementTypeOption:  type to set on requirement 
    :type requirementTypeOption: :py:class:`NXOpen.Validate.RequirementBuilderRequirementTypeOptions` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SeverityOption: RequirementBuilderSeverityOptions = ...
    """
    Returns or sets  the severity option 
    
    <hr>
    
    Getter Method
    
    Signature ``SeverityOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Validate.RequirementBuilderSeverityOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeverityOption`` 
    
    :param severityOption: 
    :type severityOption: :py:class:`NXOpen.Validate.RequirementBuilderSeverityOptions` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SingleSidedValue: str = ...
    """
    Returns or sets  the value for single sided comparison 
    
    <hr>
    
    Getter Method
    
    Signature ``SingleSidedValue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SingleSidedValue`` 
    
    :param singleSidedValue: 
    :type singleSidedValue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: RequirementBuilder = ...  # unknown typename


class XmlComparatorResultMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class XmlComparatorResult():
    """
    Specifies result of the comparison 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Identical", "Represents two xml files are identical"
       "Different", "Represents two xml files are different"
    """
    Identical = 0  # XmlComparatorResultMemberType
    Different = 1  # XmlComparatorResultMemberType
    
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
    


class XmlComparator():
    """
    Provides a generic comparator for finding differences between two XML
    format files.
    The comparator takes :py:class:`NXOpen.Validate.XmlComparatorOptions_Struct` to further control the
    comparison process. It returns :py:class:`NXOpen.Validate.XmlComparatorResult`, and generates report 
    of detailed differences in HTML file which can be viewed via web browser. 
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX6.0.2
    """
    
    class Result():
        """
        Specifies result of the comparison 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Identical", "Represents two xml files are identical"
           "Different", "Represents two xml files are different"
        """
        Identical = 0  # XmlComparatorResultMemberType
        Different = 1  # XmlComparatorResultMemberType
        
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
        
    
    
    class Options():
        """
        Represents config options in comparison
        
        For example:
        
        case 1: Defines filter file to control what nodes will be compared;
        generates comparison report and log; ignores CDATA and processing 
        instruction nodes.
        
        compareOptions.ReportFile           = "auto_report.html";
        compareOptions.FilterFile           = "filter.xml";
        compareOptions.LogFile              = "log.log";
        compareOptions.IgnoreNamespaces     = FALSE;
        compareOptions.IgnoreUnmatchedNodes = FALSE;
        compareOptions.IgnoreComments       = FALSE;
        compareOptions.IgnoreCdata          = TRUE;
        compareOptions.IgnorePI             = TRUE;
        CompareXmlFiles("fileOne.xml", "fileTwo.xml", compareOptions)
        
        case 2: Compares all nodes and does not generate report file and log file.
        
        compareOptions.ReportFile           = None;
        compareOptions.FilterFile           = None;
        compareOptions.LogFile              = None;
        CompareXmlFiles("fileOne.xml", "fileTwo.xml", compareOptions)
        
        .
        Constructor: 
        NXOpen.Validate.XmlComparator.Options()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        FilterFile: str = ...
        """
        File specification of filter file.  
        
        The filter file defines what nodes will be compared and how to compare them.
        It can be None, which means all nodes will be compared. 
        <hr>
        
        Field Value
        Type:str
        """
        ReportFile: str = ...
        """
        File specification of report file.  
        
        The report file contains the detail comparison results.
        It can be None, which means the comparator won't generate a report file. 
        <hr>
        
        Field Value
        Type:str
        """
        LogFile: str = ...
        """
        File specification of comparison log file.  
        
        The log file contains detail comparison steps and comparison information.
        It can be None, which means the comparator won't generate a log file. 
        <hr>
        
        Field Value
        Type:str
        """
        IgnoreNamespaces: bool = ...
        """
        Ignores namespace definition during comparison.  
        
        But if the filter file has namespace definition, the comparator will ignore
        this option and always compare the nodes with namespace definitions. Default if false. 
        <hr>
        
        Field Value
        Type:bool
        """
        IgnoreUnmatchedNodes: bool = ...
        """
        Ignores unmatched nodes in comparison.  
        
        Default is false. 
        <hr>
        
        Field Value
        Type:bool
        """
        IgnoreComments: bool = ...
        """
        Ignores comment nodes in comparison.  
        
        Default is false. 
        <hr>
        
        Field Value
        Type:bool
        """
        IgnoreCdata: bool = ...
        """
        Ignores CDATA nodes in comparison.  
        
        Default is false. 
        <hr>
        
        Field Value
        Type:bool
        """
        IgnorePI: bool = ...
        """
        Ignores processing instruction nodes in comparison.  
        
        Default is false. 
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    def CompareXmlFiles(self, workXmlFile: str, masterXmlFile: str, compareOptions: XmlComparatorOptions_Struct) -> XmlComparatorResult:
        """
        Compares two xml format files.  
        
        You can use :py:class:`NXOpen.Validate.XmlComparatorOptions_Struct`to customize the comparison process. 
        
        Signature ``CompareXmlFiles(workXmlFile, masterXmlFile, compareOptions)`` 
        
        :param workXmlFile:  The first xml file to be compared  
        :type workXmlFile: str 
        :param masterXmlFile:  The second xml file to be compared against  
        :type masterXmlFile: str 
        :param compareOptions:  comparison options  
        :type compareOptions: :py:class:`NXOpen.Validate.XmlComparatorOptions_Struct` 
        :returns:  comparison result  
        :rtype: :py:class:`NXOpen.Validate.XmlComparatorResult` 
        
        .. versionadded:: NX6.0.2
        
        License requirements: None.
        """
        ...
    


