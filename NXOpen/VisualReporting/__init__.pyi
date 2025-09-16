# module 'NXOpen.VisualReporting'
#
# Automatically generated 2025-06-09T14:38:48.503963
#
"""Default documentation for NXOpen.VisualReporting."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class VisualReportCollection(NXOpen.TaggedObjectCollection):
    """
    A collection of visual reports.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.VisualReporting.VisualReportManager`
    
    .. versionadded:: NX7.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> VisualReport:
        """
        Finds the :py:class:`NXOpen.VisualReporting.VisualReport` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Filename of the visual report to be found  
        :type journalIdentifier: str 
        :returns:  Visual report found, or null if no such visual report exists. 
        :rtype: :py:class:`NXOpen.VisualReporting.VisualReport` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    


class VisualReportExplorerExploreReportOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VisualReportExplorerExploreReportOption():
    """
    Represents whether Explore Report mode is on or off.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Off", "Explore Visual Report results is off"
       "On", "Explore Visual Report results is on"
    """
    Off = 0  # VisualReportExplorerExploreReportOptionMemberType
    On = 1  # VisualReportExplorerExploreReportOptionMemberType
    
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
    


class VisualReportExplorerReportOnObjectsOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VisualReportExplorerReportOnObjectsOption():
    """
    When the set of objects to report upon is changed, should the 
    contents of the set be replaced or extended.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Replace", "Replace the existing set of objects"
       "Add", "Add to the existing set of objects"
    """
    Replace = 0  # VisualReportExplorerReportOnObjectsOptionMemberType
    Add = 1  # VisualReportExplorerReportOnObjectsOptionMemberType
    
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
    


class VisualReportExplorerReportDownStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VisualReportExplorerReportDownStatus():
    """
    Status reported by :py:meth:`NXOpen.VisualReporting.VisualReportExplorer.ReportDown`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "There are no objects of interest below the specified objects"
       "End", "Report Down has reached the lowest level on all branches of the assembly"
       "More", "There are more objects of interest below the currently reported upon objects"
    """
    NotSet = 0  # VisualReportExplorerReportDownStatusMemberType
    End = 1  # VisualReportExplorerReportDownStatusMemberType
    More = 2  # VisualReportExplorerReportDownStatusMemberType
    
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
    


class VisualReportExplorer():
    """
    The Explorer of the results of a visual report.  
    
    The Visual Report Explorer enables a report to focus on specified objects
    or on a particular group in the visual report.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.VisualReporting.VisualReportManager`
    
    .. versionadded:: NX7.5.0
    """
    
    class ExploreReportOption():
        """
        Represents whether Explore Report mode is on or off.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Off", "Explore Visual Report results is off"
           "On", "Explore Visual Report results is on"
        """
        Off = 0  # VisualReportExplorerExploreReportOptionMemberType
        On = 1  # VisualReportExplorerExploreReportOptionMemberType
        
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
        
    
    
    class ReportOnObjectsOption():
        """
        When the set of objects to report upon is changed, should the 
        contents of the set be replaced or extended.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Replace", "Replace the existing set of objects"
           "Add", "Add to the existing set of objects"
        """
        Replace = 0  # VisualReportExplorerReportOnObjectsOptionMemberType
        Add = 1  # VisualReportExplorerReportOnObjectsOptionMemberType
        
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
        
    
    
    class ReportDownStatus():
        """
        Status reported by :py:meth:`NXOpen.VisualReporting.VisualReportExplorer.ReportDown`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "There are no objects of interest below the specified objects"
           "End", "Report Down has reached the lowest level on all branches of the assembly"
           "More", "There are more objects of interest below the currently reported upon objects"
        """
        NotSet = 0  # VisualReportExplorerReportDownStatusMemberType
        End = 1  # VisualReportExplorerReportDownStatusMemberType
        More = 2  # VisualReportExplorerReportDownStatusMemberType
        
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
        
    
    
    def ReportOnObjects(self, nxObjects: 'list[NXOpen.NXObject]', reportOnObjectsOption: VisualReportExplorerReportOnObjectsOption) -> None:
        """
        Set objects to report upon.  
        
        Signature ``ReportOnObjects(nxObjects, reportOnObjectsOption)`` 
        
        :param nxObjects:  Objects to report upon  
        :type nxObjects: list of :py:class:`NXOpen.NXObject` 
        :param reportOnObjectsOption:  Add to or replace objects in report  
        :type reportOnObjectsOption: :py:class:`NXOpen.VisualReporting.VisualReportExplorerReportOnObjectsOption` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveReportObjects(self, nxObjects: 'list[NXOpen.NXObject]') -> None:
        """
        Remove objects from report.  
        
        Signature ``RemoveReportObjects(nxObjects)`` 
        
        :param nxObjects:  Objects to remove from report  
        :type nxObjects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearReportObjects(self) -> None:
        """
        Remove all objects from the visual report.  
        
        Signature ``ClearReportObjects()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetReportObjects(self) -> None:
        """
        Resets the objects to report upon.  
        
        If there is no group to explore set, then all leaf nodes of the 
        assembly will be included in the report.
        If a group to explore is set, then elements of that group
        will be reported upon.  Where there are two elements of the group
        on the same branch of the assembly, the lowest will be reported upon.
        
        Signature ``ResetReportObjects()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetExploringGroup(self) -> GroupLabel:
        """
        Gets the exploring :py:class:`NXOpen.VisualReporting.GroupLabel`
        
        Signature ``GetExploringGroup()`` 
        
        :returns:  The exploring group  
        :rtype: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetGroupToExplore(self, groupLabel: GroupLabel) -> None:
        """
        Sets the :py:class:`NXOpen.VisualReporting.GroupLabel` to explore.  
        
        The :py:class:`NXOpen.VisualReporting.GroupLabel` to explore can be set to None.
        If there is no active visual report, then nothing will happen.
        Note that the :py:class:`NXOpen.VisualReporting.GroupLabel` should belong to the active visual report
        otherwise the call will fail.
        This method will also cause the objects reported upon to be reset in the
        same way as a call to :py:meth:`ResetReportObjects`.
        
        Signature ``SetGroupToExplore(groupLabel)`` 
        
        :param groupLabel:  The group to explore  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def ReportDown(self, reportOnObjectsOption: VisualReportExplorerReportOnObjectsOption) -> VisualReportExplorerReportDownStatus:
        """
        Report down the assembly, starting from the :py:meth:`NXOpen.Assemblies.ComponentAssembly.RootComponent`.
        A group to explore should have been specified for this method to         
        have any effect.
        The first time this method is called the operation will start from
        :py:meth:`NXOpen.Assemblies.ComponentAssembly.RootComponent`.
        On subsequent calls, the set of objects currently reported upon 
        will be used as the starting point.
        
        Signature ``ReportDown(reportOnObjectsOption)`` 
        
        :param reportOnObjectsOption:  Add to or replace objects in report  
        :type reportOnObjectsOption: :py:class:`NXOpen.VisualReporting.VisualReportExplorerReportOnObjectsOption` 
        :returns:  Status from the report down operation  
        :rtype: :py:class:`NXOpen.VisualReporting.VisualReportExplorerReportDownStatus` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def ReportDown(self, nxObjects: 'list[NXOpen.NXObject]', reportOnObjectsOption: VisualReportExplorerReportOnObjectsOption) -> VisualReportExplorerReportDownStatus:
        """
        Report down from a starting array of objects.
        A group to explore should have been specified for this method to
        have any effect.
        On subsequent calls to :py:meth:`NXOpen.VisualReporting.VisualReportExplorer.ReportDown`, with no nxObjects
        array, the set of objects currently reported upon will be used as the 
        starting point.
        
        Signature ``ReportDown(nxObjects, reportOnObjectsOption)`` 
        
        :param nxObjects:  Objects from which to start report down operation  
        :type nxObjects: list of :py:class:`NXOpen.NXObject` 
        :param reportOnObjectsOption:  Add to or replace objects in report  
        :type reportOnObjectsOption: :py:class:`NXOpen.VisualReporting.VisualReportExplorerReportOnObjectsOption` 
        :returns:  Status from the report down operation  
        :rtype: :py:class:`NXOpen.VisualReporting.VisualReportExplorerReportDownStatus` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ReportOnChildren(self, nxObjects: 'list[NXOpen.NXObject]', reportOnObjectsOption: VisualReportExplorerReportOnObjectsOption) -> None:
        """
        Report on the children of nxObjects.  
        
        The children will either replace the existing contents of the report
        or be added to the report.
        This operation is intended for :py:class:`NXOpen.Assemblies.Component`s
        and will report on direct children of the components.
        If an object is not an instance of :py:class:`NXOpen.Assemblies.Component`
        or if it has no children then nothing will be changed.
        
        Signature ``ReportOnChildren(nxObjects, reportOnObjectsOption)`` 
        
        :param nxObjects:  Objects whose children will be reported upon  
        :type nxObjects: list of :py:class:`NXOpen.NXObject` 
        :param reportOnObjectsOption:  Add to or replace objects in report  
        :type reportOnObjectsOption: :py:class:`NXOpen.VisualReporting.VisualReportExplorerReportOnObjectsOption` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ReportOnParents(self, nxObjects: 'list[NXOpen.NXObject]', reportOnObjectsOption: VisualReportExplorerReportOnObjectsOption) -> None:
        """
        Report on the parents of the nxObjects.  
        
        The parents will either replace the existing contents of the report
        or be added to the report.
        This operation is intended for :py:class:`NXOpen.Assemblies.Component`s
        and will report on the parent of the component.
        If the object is not an instance of :py:class:`NXOpen.Assemblies.Component`
        or if it has no parent then nothing will be changed.
        
        Signature ``ReportOnParents(nxObjects, reportOnObjectsOption)`` 
        
        :param nxObjects:  Objects whose parents will be reported upon  
        :type nxObjects: list of :py:class:`NXOpen.NXObject` 
        :param reportOnObjectsOption:  Add to or replace objects in report  
        :type reportOnObjectsOption: :py:class:`NXOpen.VisualReporting.VisualReportExplorerReportOnObjectsOption` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    ExploreReport: VisualReportExplorerExploreReportOption = ...
    """
    Returns or sets  the Explore Report setting
    
    <hr>
    
    Getter Method
    
    Signature ``ExploreReport`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportExplorerExploreReportOption` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExploreReport`` 
    
    :param exploreReportOption: 
    :type exploreReportOption: :py:class:`NXOpen.VisualReporting.VisualReportExplorerExploreReportOption` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """


class ClassifierTypeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClassifierTypeOption():
    """
    Represents the possible type options.
    for a :py:class:`NXOpen.VisualReporting.Classifier`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Simple", "Simple classifier type"
       "Value", "Value classifier type"
       "Range", "Range classifier type"
    """
    Simple = 0  # ClassifierTypeOptionMemberType
    Value = 1  # ClassifierTypeOptionMemberType
    Range = 2  # ClassifierTypeOptionMemberType
    
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
    


class ClassifierGroupingMethodOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClassifierGroupingMethodOption():
    """
    Represents the possible grouping method options.
    for a :py:class:`NXOpen.VisualReporting.Classifier`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Manual", "Grouping is manual"
       "Automatic", "Grouping is automatic"
       "SemiAutomatic", "Grouping is automatic but some :py:class:`NXOpen.VisualReporting.GroupLabel`s have been modified"
    """
    Manual = 0  # ClassifierGroupingMethodOptionMemberType
    Automatic = 1  # ClassifierGroupingMethodOptionMemberType
    SemiAutomatic = 2  # ClassifierGroupingMethodOptionMemberType
    
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
    


class ClassifierRangeMethodOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClassifierRangeMethodOption():
    """
    Represents the possible range method options.
    for a :py:class:`NXOpen.VisualReporting.Classifier`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Number", "A numeric range will be used"
       "Percentage", "A percentage range will be used"
    """
    Number = 0  # ClassifierRangeMethodOptionMemberType
    Percentage = 1  # ClassifierRangeMethodOptionMemberType
    
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
    


class ClassifierDateGroupMethodOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClassifierDateGroupMethodOption():
    """
    Represents the possible date grouping method options.
    for a :py:class:`NXOpen.VisualReporting.Classifier`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Day", "The date grouping by day will be used"
       "Week", "The date grouping by week will be used"
       "Month", "The date grouping by month will be used"
       "Year", "The date grouping by year will be used"
    """
    Day = 0  # ClassifierDateGroupMethodOptionMemberType
    Week = 1  # ClassifierDateGroupMethodOptionMemberType
    Month = 2  # ClassifierDateGroupMethodOptionMemberType
    Year = 3  # ClassifierDateGroupMethodOptionMemberType
    
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
    


class Classifier(NXOpen.NXObject):
    """
    A Classifier within a :py:class:`NXOpen.VisualReporting.Rule`.  
    
    .. versionadded:: NX8.0.0
    """
    
    class TypeOption():
        """
        Represents the possible type options.
        for a :py:class:`NXOpen.VisualReporting.Classifier`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Simple", "Simple classifier type"
           "Value", "Value classifier type"
           "Range", "Range classifier type"
        """
        Simple = 0  # ClassifierTypeOptionMemberType
        Value = 1  # ClassifierTypeOptionMemberType
        Range = 2  # ClassifierTypeOptionMemberType
        
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
        
    
    
    class GroupingMethodOption():
        """
        Represents the possible grouping method options.
        for a :py:class:`NXOpen.VisualReporting.Classifier`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Manual", "Grouping is manual"
           "Automatic", "Grouping is automatic"
           "SemiAutomatic", "Grouping is automatic but some :py:class:`NXOpen.VisualReporting.GroupLabel`s have been modified"
        """
        Manual = 0  # ClassifierGroupingMethodOptionMemberType
        Automatic = 1  # ClassifierGroupingMethodOptionMemberType
        SemiAutomatic = 2  # ClassifierGroupingMethodOptionMemberType
        
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
        
    
    
    class RangeMethodOption():
        """
        Represents the possible range method options.
        for a :py:class:`NXOpen.VisualReporting.Classifier`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Number", "A numeric range will be used"
           "Percentage", "A percentage range will be used"
        """
        Number = 0  # ClassifierRangeMethodOptionMemberType
        Percentage = 1  # ClassifierRangeMethodOptionMemberType
        
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
        
    
    
    class DateGroupMethodOption():
        """
        Represents the possible date grouping method options.
        for a :py:class:`NXOpen.VisualReporting.Classifier`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Day", "The date grouping by day will be used"
           "Week", "The date grouping by week will be used"
           "Month", "The date grouping by month will be used"
           "Year", "The date grouping by year will be used"
        """
        Day = 0  # ClassifierDateGroupMethodOptionMemberType
        Week = 1  # ClassifierDateGroupMethodOptionMemberType
        Month = 2  # ClassifierDateGroupMethodOptionMemberType
        Year = 3  # ClassifierDateGroupMethodOptionMemberType
        
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
        
    
    Null: Classifier = ...  # unknown typename


class UnmatchedResultCategory(NXOpen.NXObject):
    """
    An unmatched result category within a :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    .. versionadded:: NX8.0.0
    """
    Null: UnmatchedResultCategory = ...  # unknown typename


class VisualReportBuilderPropertyUsageOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VisualReportBuilderPropertyUsageOption():
    """
    Represents the usage option of reference :py:class:`NXOpen.VisualReporting.Property`
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Tooltip", "The property is used in tooltip only"
       "InfoView", "The property is used in info view only"
       "TooltipAndInfoView", " - "
    """
    Tooltip = 0  # VisualReportBuilderPropertyUsageOptionMemberType
    InfoView = 1  # VisualReportBuilderPropertyUsageOptionMemberType
    TooltipAndInfoView = 2  # VisualReportBuilderPropertyUsageOptionMemberType
    
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
    


class VisualReportBuilder(NXOpen.Builder):
    """
    A Builder for creating and editing :py:class:`NXOpen.VisualReporting.VisualReport`s.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.VisualReporting.VisualReportManager.CreateVisualReportBuilder`
    
    .. versionadded:: NX7.0.0
    """
    
    class PropertyUsageOption():
        """
        Represents the usage option of reference :py:class:`NXOpen.VisualReporting.Property`
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Tooltip", "The property is used in tooltip only"
           "InfoView", "The property is used in info view only"
           "TooltipAndInfoView", " - "
        """
        Tooltip = 0  # VisualReportBuilderPropertyUsageOptionMemberType
        InfoView = 1  # VisualReportBuilderPropertyUsageOptionMemberType
        TooltipAndInfoView = 2  # VisualReportBuilderPropertyUsageOptionMemberType
        
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
        
    
    
    def CreateVisualReport(self) -> VisualReport:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.VisualReport` and starts editing it.  
        
        The created :py:class:`NXOpen.VisualReporting.VisualReport` will not be added to the
        :py:class:`NXOpen.VisualReporting.VisualReportManager` until :py:meth:`Builder.Commit`
        or :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CommitAsCopy` is called on this builder.
        
        Signature ``CreateVisualReport()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.VisualReporting.VisualReport` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EditVisualReport(self, visualReport: VisualReport) -> None:
        """
        Starts editing a :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        The builder will create a
        copy of the given VisualReport and all edits will be applied to that copy. When
        :py:meth:`Builder.Commit` is called on this builder, the supplied
        VisualReport will be deleted and replaced with the new one. Alternatively if
        :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CommitAsCopy` is called, the copied :py:class:`NXOpen.VisualReporting.VisualReport`
        will be added to the :py:class:`NXOpen.VisualReporting.VisualReportManager` without deleting the one given in this function.
        
        Any current :py:class:`NXOpen.VisualReporting.VisualReport` which this builder is currently
        building will be deleted when this function is called.
        
        Signature ``EditVisualReport(visualReport)`` 
        
        :param visualReport:  The visual report  
        :type visualReport: :py:class:`NXOpen.VisualReporting.VisualReport` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CommitAsCopy(self) -> VisualReport:
        """
        When :py:meth:`Builder.Commit` is called on this builder, it will
        delete the original :py:class:`NXOpen.VisualReporting.VisualReport` whose copy the builder is editing and install the copied
        :py:class:`NXOpen.VisualReporting.VisualReport` to the :py:class:`NXOpen.VisualReporting.VisualReportManager`.  
        
        If it is required not to delete the original :py:class:`NXOpen.VisualReporting.VisualReport`,
        then :py:meth:`CommitAsCopy` can be called instead. This behaves
        just like :py:meth:`Builder.Commit` except it does not delete the
        original :py:class:`NXOpen.VisualReporting.VisualReport`.
        
        Signature ``CommitAsCopy()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.VisualReporting.VisualReport` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EnableUnmatchedGroupOfVisualReport(self, enableUnmatchedGroup: bool) -> None:
        """
        Sets whether use of :py:meth:`NXOpen.VisualReporting.VisualReport.UnmatchedGroupLabel`
        is enabled for the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this builder.  
        
        Signature ``EnableUnmatchedGroupOfVisualReport(enableUnmatchedGroup)`` 
        
        :param enableUnmatchedGroup:  Whether the unmatched group is enabled  
        :type enableUnmatchedGroup: bool 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRule(self, index: int) -> Rule:
        """
        Return the specified :py:class:`NXOpen.VisualReporting.Rule` from the :py:class:`NXOpen.VisualReporting.VisualReport`
        being built by this builder.  
        
        Signature ``GetRule(index)`` 
        
        :param index:  The index of the returned :py:class:`NXOpen.VisualReporting.Rule`.  
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.VisualReporting.Rule` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRules(self) -> 'list[Rule]':
        """
        Returns all the :py:class:`NXOpen.VisualReporting.Rule`s in the :py:class:`NXOpen.VisualReporting.VisualReport` 
        being built by this builder.  
        
        Signature ``GetRules()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.VisualReporting.Rule` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetClassifiersOfRule(self, rule: Rule) -> 'list[Classifier]':
        """
        Returns the :py:class:`NXOpen.VisualReporting.Classifier`s associated with this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``GetClassifiersOfRule(rule)`` 
        
        :param rule: 
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.VisualReporting.Classifier` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetActiveClassifierOfRule(self, rule: Rule) -> Classifier:
        """
        Gets the active :py:class:`NXOpen.VisualReporting.Classifier` in this :py:class:`NXOpen.VisualReporting.Rule`
        for a multiple properties report.  
        
        Signature ``GetActiveClassifierOfRule(rule)`` 
        
        :param rule: 
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns: 
        :rtype: :py:class:`NXOpen.VisualReporting.Classifier` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetActiveClassifierOfRule(self, rule: Rule, activeClassifier: Classifier) -> None:
        """
        Sets the active :py:class:`NXOpen.VisualReporting.Classifier` in this :py:class:`NXOpen.VisualReporting.Rule`
        for a multiple properties report.  
        
        Signature ``SetActiveClassifierOfRule(rule, activeClassifier)`` 
        
        :param rule: 
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param activeClassifier: 
        :type activeClassifier: :py:class:`NXOpen.VisualReporting.Classifier` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetReferencePropertiesOfReportingProperty(self) -> tuple:
        """
        Gets the message :py:class:`NXOpen.VisualReporting.Property`  list of the :py:class:`NXOpen.VisualReporting.Property`
        in the active :py:class:`NXOpen.VisualReporting.Classifier`.  
        
        Signature ``GetReferencePropertiesOfReportingProperty()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (properties, usages). properties is a list of :py:class:`NXOpen.VisualReporting.Property`.   The reference properties of propertyusages is a list of :py:class:`NXOpen.VisualReporting.VisualReportBuilderPropertyUsageOption`.   The usages 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetReferencePropertiesOfReportingProperty(self, properties: 'list[Property]', usages: 'list[VisualReportBuilderPropertyUsageOption]') -> None:
        """
        Sets the message :py:class:`NXOpen.VisualReporting.Property` list of the :py:class:`NXOpen.VisualReporting.Property`
        in the active :py:class:`NXOpen.VisualReporting.Classifier`.  
        
        Signature ``SetReferencePropertiesOfReportingProperty(properties, usages)`` 
        
        :param properties:  The reference properties of property 
        :type properties: list of :py:class:`NXOpen.VisualReporting.Property` 
        :param usages:  The usages  
        :type usages: list of :py:class:`NXOpen.VisualReporting.VisualReportBuilderPropertyUsageOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPropertyOfCondition(self, condition: Condition) -> Property:
        """
        Gets the :py:class:`NXOpen.VisualReporting.Property` of this condition.  
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``GetPropertyOfCondition(condition)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns:  The property  
        :rtype: :py:class:`NXOpen.VisualReporting.Property` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPropertyOfCondition(self, condition: Condition, property: Property) -> None:
        """
        Sets the :py:class:`NXOpen.VisualReporting.Property` of this condition.  
        
        If the
        :py:meth:`NXOpen.VisualReporting.Property` is set to None, then it is
        deleted.
        Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``SetPropertyOfCondition(condition, property)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param property:  The property being set  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemovePropertyFromCondition(self, condition: Condition) -> None:
        """
        Removes the current :py:class:`NXOpen.VisualReporting.Property` from this condition
        without deleting it.  
        
        Signature ``RemovePropertyFromCondition(condition)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOperatorTypeOfCondition(self, condition: Condition) -> ConditionOperatorOption:
        """
        Gets the :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` of this condition.  
        
        Only valid if
        :py:class:`NXOpen.VisualReporting.ConditionTypeOption` is
        :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``GetOperatorTypeOfCondition(condition)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns:  The operator type being set  
        :rtype: :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOperatorTypeOfCondition(self, condition: Condition, operatorType: ConditionOperatorOption) -> None:
        """
        Sets the :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` of this condition.  
        
        Only valid if
        :py:class:`NXOpen.VisualReporting.ConditionTypeOption` is
        :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``SetOperatorTypeOfCondition(condition, operatorType)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param operatorType:  The operator type being set  
        :type operatorType: :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetValueOfCondition(self, condition: Condition) -> str:
        """
        Gets the value of this :py:class:`NXOpen.VisualReporting.Condition`.  
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``GetValueOfCondition(condition)`` 
        
        :param condition: 
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValueOfCondition(self, condition: Condition, value: str) -> None:
        """
        Sets the value of this :py:class:`NXOpen.VisualReporting.Condition`.  
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``SetValueOfCondition(condition, value)`` 
        
        :param condition: 
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param value: 
        :type value: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPropertyForComparison(self, condition: Condition) -> Property:
        """
        Gets the :py:class:`NXOpen.VisualReporting.Property` in the value for comparison of this :py:class:`NXOpen.VisualReporting.Condition`.  
        
        Signature ``GetPropertyForComparison(condition)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns:  The property  
        :rtype: :py:class:`NXOpen.VisualReporting.Property` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPropertyForComparison(self, condition: Condition, property: Property) -> None:
        """
        Sets the :py:class:`NXOpen.VisualReporting.Property` in the value for comparison of this :py:class:`NXOpen.VisualReporting.Condition`.  
        
        If the
        :py:meth:`NXOpen.VisualReporting.Property` is set to None, then it is
        deleted.
        
        Signature ``SetPropertyForComparison(condition, property)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param property:  The property being set  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddChildToCondition(self, condition: Condition, childCondition: Condition) -> None:
        """
        Add a new child :py:class:`NXOpen.VisualReporting.Condition` to this condition.  
        
        If the child is already a
        child of another :py:class:`NXOpen.VisualReporting.Condition` or :py:class:`NXOpen.VisualReporting.Rule`, then it is
        removed from that other object. The new child must have been created in the same
        :py:class:`NXOpen.VisualReporting.VisualReport` as this parent condition. If this is a
        :py:class:`NXOpen.VisualReporting.ConditionTypeOption.NotCondition <NXOpen.VisualReporting.ConditionTypeOption>` then
        this replaces the existing child, and the existing child is deleted.
        
        Signature ``AddChildToCondition(condition, childCondition)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param childCondition:  The child condition being added  
        :type childCondition: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveChildFromCondition(self, condition: Condition, childCondition: Condition) -> None:
        """
        Removes a condition from its parent condition.  
        
        If the condition has an associated :py:class:`NXOpen.VisualReporting.Property`
        that will be deleted too. If the condition has any child conditions, those will all
        be deleted too.
        
        Signature ``RemoveChildFromCondition(condition, childCondition)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param childCondition:  The child condition being removed  
        :type childCondition: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetHasUserSpecifiedValueForCondition(self, condition: Condition) -> bool:
        """
        Gets :py:meth:`NXOpen.VisualReporting.Condition.HasUserSpecifiedValue` on the
        specified :py:class:`NXOpen.VisualReporting.Condition`.  
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``GetHasUserSpecifiedValueForCondition(condition)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns:  Whether the condition's value should be user-specified  
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetHasUserSpecifiedValueForCondition(self, condition: Condition, isUserSpecified: bool) -> None:
        """
        Sets :py:meth:`NXOpen.VisualReporting.Condition.HasUserSpecifiedValue` on the
        specified :py:class:`NXOpen.VisualReporting.Condition`.  
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``SetHasUserSpecifiedValueForCondition(condition, isUserSpecified)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param isUserSpecified:  Whether the condition's value should be user-specified  
        :type isUserSpecified: bool 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetUserPromptOfCondition(self, condition: Condition) -> str:
        """
        Gets the :py:meth:`NXOpen.VisualReporting.Condition.UserPrompt` of the
        specified :py:class:`NXOpen.VisualReporting.Condition`.  
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``GetUserPromptOfCondition(condition)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns:  The user-prompt   
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetUserPromptOfCondition(self, condition: Condition, userPrompt: str) -> None:
        """
        Sets the :py:meth:`NXOpen.VisualReporting.Condition.UserPrompt` of the
        specified :py:class:`NXOpen.VisualReporting.Condition`.  
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``SetUserPromptOfCondition(condition, userPrompt)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param userPrompt:  The user-prompt   
        :type userPrompt: str 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDescriptionOfCondition(self, condition: Condition) -> str:
        """
        Gets the :py:meth:`NXOpen.VisualReporting.Condition.Description` of the
        specified :py:class:`NXOpen.VisualReporting.Condition`.  
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``GetDescriptionOfCondition(condition)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns:  The description  
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDescriptionOfCondition(self, condition: Condition, description: str) -> None:
        """
        Sets the :py:meth:`NXOpen.VisualReporting.Condition.Description` of the
        specified :py:class:`NXOpen.VisualReporting.Condition`.  
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        
        Signature ``SetDescriptionOfCondition(condition, description)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param description:  The description  
        :type description: str 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetClassifierTypeOfRule(self, rule: Rule) -> ClassifierTypeOption:
        """
        Gets the reporting :py:class:`NXOpen.VisualReporting.ClassifierTypeOption` for the active :py:class:`NXOpen.VisualReporting.Classifier`
        in this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``GetClassifierTypeOfRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns:  The classifier type  
        :rtype: :py:class:`NXOpen.VisualReporting.ClassifierTypeOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetClassifierTypeOfRule(self, rule: Rule, classifierType: ClassifierTypeOption) -> Classifier:
        """
        Sets the reporting :py:class:`NXOpen.VisualReporting.ClassifierTypeOption` for the active :py:class:`NXOpen.VisualReporting.Classifier`
        in this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Note that the old :py:class:`NXOpen.VisualReporting.Classifier` in this :py:class:`NXOpen.VisualReporting.Rule` will be deleted 
        and a new :py:class:`NXOpen.VisualReporting.Classifier` will be created and set as the active :py:class:`NXOpen.VisualReporting.Classifier`
        in this :py:class:`NXOpen.VisualReporting.Rule`.
        
        Signature ``SetClassifierTypeOfRule(rule, classifierType)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param classifierType:  The classifier type being set  
        :type classifierType: :py:class:`NXOpen.VisualReporting.ClassifierTypeOption` 
        :returns:  The new active classifier  
        :rtype: :py:class:`NXOpen.VisualReporting.Classifier` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetReportingPropertyOfRule(self, rule: Rule) -> Property:
        """
        Gets the reporting :py:class:`NXOpen.VisualReporting.Property` for the active :py:class:`NXOpen.VisualReporting.Classifier`
        in this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``GetReportingPropertyOfRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns:  The property  
        :rtype: :py:class:`NXOpen.VisualReporting.Property` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetReportingPropertyOfRule(self, rule: Rule, reportingProperty: Property) -> None:
        """
        Sets the reporting :py:class:`NXOpen.VisualReporting.Property` for the active :py:class:`NXOpen.VisualReporting.Classifier`
        in this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        If the reporting :py:class:`NXOpen.VisualReporting.Property` of the rule is set to None, then it is deleted.
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Classifier` in this :py:class:`NXOpen.VisualReporting.Rule` whose
        :py:class:`NXOpen.VisualReporting.ClassifierTypeOption` is :py:class:`NXOpen.VisualReporting.ClassifierTypeOption.Value <NXOpen.VisualReporting.ClassifierTypeOption>`
        or :py:class:`NXOpen.VisualReporting.ClassifierTypeOption.Range <NXOpen.VisualReporting.ClassifierTypeOption>`.
        
        Signature ``SetReportingPropertyOfRule(rule, reportingProperty)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param reportingProperty:  The property being set  
        :type reportingProperty: :py:class:`NXOpen.VisualReporting.Property` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetReportingDatatypeOfRule(self, rule: Rule) -> PropertyDatatypeOption:
        """
        Gets the :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` of the active :py:class:`NXOpen.VisualReporting.Classifier`'s reporting :py:class:`NXOpen.VisualReporting.Property`
        in this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``GetReportingDatatypeOfRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns:  The datatype 
        :rtype: :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetReportingDatatypeOfRule(self, rule: Rule, datatype: PropertyDatatypeOption) -> None:
        """
        Sets the :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` of the active :py:class:`NXOpen.VisualReporting.Classifier`'s reporting :py:class:`NXOpen.VisualReporting.Property`
        in this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        However datatype must not be :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption.Unknown <NXOpen.VisualReporting.PropertyDatatypeOption>`.
        
        Signature ``SetReportingDatatypeOfRule(rule, datatype)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param datatype:  The datatype being set  
        :type datatype: :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveFilterConditionFromRule(self, rule: Rule) -> None:
        """
        Removes any existing filter :py:class:`NXOpen.VisualReporting.Condition` from this rule.  
        
        This will not delete
        the condition.
        
        Signature ``RemoveFilterConditionFromRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFilterConditionOfRule(self, rule: Rule) -> Condition:
        """
        Gets the filter :py:class:`NXOpen.VisualReporting.Condition` from this rule.  
        
        Signature ``GetFilterConditionOfRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns:  The filter condition  
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFilterConditionOfRule(self, rule: Rule, filterCondition: Condition) -> None:
        """
        Sets the filter :py:class:`NXOpen.VisualReporting.Condition` from this rule.  
        
        Setting this will delete
        any existing :py:meth:`NXOpen.VisualReporting.Rule.FilterCondition` and all of its children
        (except it won't delete the replacement :py:class:`NXOpen.VisualReporting.Condition` being set
        by this call).
        
        Signature ``SetFilterConditionOfRule(rule, filterCondition)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param filterCondition:  The filter condition being set  
        :type filterCondition: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetManualGroupingForRule(self, rule: Rule) -> bool:
        """
        Gets whether the :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption` of the active :py:class:`NXOpen.VisualReporting.Classifier`
        in this :py:class:`NXOpen.VisualReporting.Rule` is :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption.Manual <NXOpen.VisualReporting.ClassifierGroupingMethodOption>`.  
        
        Signature ``GetManualGroupingForRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns:  Whether manual grouping should be used  
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetManualGroupingForRule(self, rule: Rule, isManualGrouping: bool) -> None:
        """
        Sets whether the :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption` of the active :py:class:`NXOpen.VisualReporting.Classifier`
        in this :py:class:`NXOpen.VisualReporting.Rule` is :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption.Manual <NXOpen.VisualReporting.ClassifierGroupingMethodOption>`.  
        
        If it uses :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption.Manual <NXOpen.VisualReporting.ClassifierGroupingMethodOption>`, then no
        :py:class:`NXOpen.VisualReporting.GroupLabel`s will be automatically generated, and they should
        instead be added manually as required using :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateGroupLabel`.
        
        Signature ``SetManualGroupingForRule(rule, isManualGrouping)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param isManualGrouping:  Whether manual grouping should be used  
        :type isManualGrouping: bool 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetGroupingMethodOfRule(self, rule: Rule) -> ClassifierGroupingMethodOption:
        """
        Gets the :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption` of the active :py:class:`NXOpen.VisualReporting.Classifier`
        in this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``GetGroupingMethodOfRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns:  The grouping method  
        :rtype: :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetGroupingMethodOfRule(self, rule: Rule, groupingMethod: ClassifierGroupingMethodOption) -> None:
        """
        Sets the :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption` of the active :py:class:`NXOpen.VisualReporting.Classifier` 
        in the given :py:class:`NXOpen.VisualReporting.Rule`.  
        
        If the active :py:class:`NXOpen.VisualReporting.Classifier` uses manual grouping then no :py:class:`NXOpen.VisualReporting.GroupLabel`s 
        will be automatically generated, and they should instead be added using :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateGroupLabel`.
        
        Signature ``SetGroupingMethodOfRule(rule, groupingMethod)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param groupingMethod:  The grouping method  
        :type groupingMethod: :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRangeMethodOfRule(self, rule: Rule) -> ClassifierRangeMethodOption:
        """
        Gets the :py:class:`NXOpen.VisualReporting.ClassifierRangeMethodOption` of the active :py:class:`NXOpen.VisualReporting.Classifier` 
        in the given :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Only valid if the active :py:class:`NXOpen.VisualReporting.Classifier` in the rule 
        is :py:class:`NXOpen.VisualReporting.ClassifierTypeOption.Range <NXOpen.VisualReporting.ClassifierTypeOption>` type.
        
        Signature ``GetRangeMethodOfRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns:  The range method  
        :rtype: :py:class:`NXOpen.VisualReporting.ClassifierRangeMethodOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRangeMethodOfRule(self, rule: Rule, rangeMethod: ClassifierRangeMethodOption) -> None:
        """
        Sets the :py:class:`NXOpen.VisualReporting.ClassifierRangeMethodOption` of the active :py:class:`NXOpen.VisualReporting.Classifier` 
        in the given :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Only valid if the active :py:class:`NXOpen.VisualReporting.Classifier` in the rule 
        is :py:class:`NXOpen.VisualReporting.ClassifierTypeOption.Range <NXOpen.VisualReporting.ClassifierTypeOption>` type.
        
        Signature ``SetRangeMethodOfRule(rule, rangeMethod)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param rangeMethod:  The range method  
        :type rangeMethod: :py:class:`NXOpen.VisualReporting.ClassifierRangeMethodOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllGroupLabelsOfRule(self, rule: Rule) -> 'list[GroupLabel]':
        """
        Returns the :py:class:`NXOpen.VisualReporting.GroupLabel`s associated with the active :py:class:`NXOpen.VisualReporting.Classifier` 
        in this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``GetAllGroupLabelsOfRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns:  The manually defined groups  
        :rtype: list of :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetManualGroupLabelOfRule(self, rule: Rule, index: int) -> GroupLabel:
        """
        Returns the specified :py:class:`NXOpen.VisualReporting.GroupLabel`s associated with the active :py:class:`NXOpen.VisualReporting.Classifier` 
        in this :py:class:`NXOpen.VisualReporting.Rule` which are manually defined.  
        
        Signature ``GetManualGroupLabelOfRule(rule, index)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param index: 
        :type index: int 
        :returns:  The specified manually defined group  
        :rtype: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetManualGroupLabelsOfRule(self, rule: Rule) -> 'list[GroupLabel]':
        """
        Returns the :py:class:`NXOpen.VisualReporting.GroupLabel`s associated with the active :py:class:`NXOpen.VisualReporting.Classifier` 
        in this :py:class:`NXOpen.VisualReporting.Rule` which are manually defined.  
        
        Signature ``GetManualGroupLabelsOfRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns:  The manually defined groups  
        :rtype: list of :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteGroupLabel(self, rule: Rule, groupLabel: GroupLabel) -> None:
        """
        Deletes the given :py:class:`NXOpen.VisualReporting.GroupLabel` from the active :py:class:`NXOpen.VisualReporting.Classifier` 
        in this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``DeleteGroupLabel(rule, groupLabel)`` 
        
        :param rule:  The rule containing the group label  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UnsetUserNameOfGroupLabel(self, groupLabel: GroupLabel) -> None:
        """
        Resets the :py:meth:`NXOpen.VisualReporting.GroupLabel.IsNameUserSpecified`
        status of the given :py:class:`NXOpen.VisualReporting.GroupLabel` so that the name is now
        system-generated.  
        
        Signature ``UnsetUserNameOfGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetUserNameOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
        Gets the :py:meth:`NXOpen.NXObject.Name`
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``GetUserNameOfGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The name  
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetUserNameOfGroupLabel(self, groupLabel: GroupLabel, name: str) -> None:
        """
        Sets the :py:meth:`NXOpen.NXObject.Name`
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Calling this function
        will cause :py:meth:`NXOpen.VisualReporting.GroupLabel.IsNameUserSpecified`
        to return true.
        
        Signature ``SetUserNameOfGroupLabel(groupLabel, name)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param name:  The name  
        :type name: str 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLowerBoundOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
        Gets the :py:meth:`NXOpen.VisualReporting.GroupLabel.LowerBound`
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``GetLowerBoundOfGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The lower bound  
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLowerBoundOfGroupLabel(self, groupLabel: GroupLabel, lowerBound: str) -> None:
        """
        Sets the :py:meth:`NXOpen.VisualReporting.GroupLabel.LowerBound`
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``SetLowerBoundOfGroupLabel(groupLabel, lowerBound)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param lowerBound:  The lower bound  
        :type lowerBound: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetUpperBoundOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
        Gets the :py:meth:`NXOpen.VisualReporting.GroupLabel.UpperBound`
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``GetUpperBoundOfGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The upper bound  
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetUpperBoundOfGroupLabel(self, groupLabel: GroupLabel, upperBound: str) -> None:
        """
        Sets the :py:meth:`NXOpen.VisualReporting.GroupLabel.UpperBound`
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``SetUpperBoundOfGroupLabel(groupLabel, upperBound)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param upperBound:  The upper bound  
        :type upperBound: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetValueOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
        Gets the :py:meth:`NXOpen.VisualReporting.GroupLabel.Value`
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``GetValueOfGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The value  
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValueOfGroupLabel(self, groupLabel: GroupLabel, value: str) -> None:
        """
        Sets the :py:meth:`NXOpen.VisualReporting.GroupLabel.Value`
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``SetValueOfGroupLabel(groupLabel, value)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param value:  The value  
        :type value: str 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDisplayStyleForGroupLabel(self, groupLabel: GroupLabel) -> GroupLabelDisplayStyleOption:
        """
        Gets the :py:class:`NXOpen.VisualReporting.GroupLabelDisplayStyleOption` 
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        Signature ``GetDisplayStyleForGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The display style  
        :rtype: :py:class:`NXOpen.VisualReporting.GroupLabelDisplayStyleOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDisplayStyleForGroupLabel(self, groupLabel: GroupLabel, displayStyle: GroupLabelDisplayStyleOption) -> None:
        """
        Sets the :py:class:`NXOpen.VisualReporting.GroupLabelDisplayStyleOption` 
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        Signature ``SetDisplayStyleForGroupLabel(groupLabel, displayStyle)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param displayStyle:  The display style  
        :type displayStyle: :py:class:`NXOpen.VisualReporting.GroupLabelDisplayStyleOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColorOfGroupLabel(self, groupLabel: GroupLabel) -> NXOpen.NXColorRgb_Struct:
        """
        Gets the :py:meth:`NXOpen.VisualReporting.GroupLabel.Color`
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``GetColorOfGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The color  
        :rtype: :py:class:`NXOpen.NXColorRgb_Struct` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColorOfGroupLabel(self, groupLabel: GroupLabel, color: NXOpen.NXColorRgb_Struct) -> None:
        """
        Sets the :py:meth:`NXOpen.VisualReporting.GroupLabel.Color`
        of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        This also changes
        :py:meth:`NXOpen.VisualReporting.GroupLabel.DisplayStyle`
        to :py:class:`NXOpen.VisualReporting.GroupLabelDisplayStyleOption.SpecifiedColor <NXOpen.VisualReporting.GroupLabelDisplayStyleOption>`.
        
        Signature ``SetColorOfGroupLabel(groupLabel, color)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param color:  The color  
        :type color: :py:class:`NXOpen.NXColorRgb_Struct` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBitmapNameOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
        Gets the bitmap of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``GetBitmapNameOfGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The bitmap name  
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBitmapNameOfGroupLabel(self, groupLabel: GroupLabel, bitmapName: str) -> None:
        """
        Sets the bitmap of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``SetBitmapNameOfGroupLabel(groupLabel, bitmapName)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param bitmapName:  The bitmap name  
        :type bitmapName: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCustomMessageOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
        Gets the custom message of the given:py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``GetCustomMessageOfGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The bitmap name  
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCustomMessageOfGroupLabel(self, groupLabel: GroupLabel, customMessage: str) -> None:
        """
        Sets the custom message of the given :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``SetCustomMessageOfGroupLabel(groupLabel, customMessage)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param customMessage:  The bitmap name  
        :type customMessage: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateProperty(self, propertyType: PropertyTypeOption) -> Property:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.Property`, but does not add it to a
        :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        Signature ``CreateProperty(propertyType)`` 
        
        :param propertyType:  Property Type of the :py:class:`NXOpen.VisualReporting.Property` being created  
        :type propertyType: :py:class:`NXOpen.VisualReporting.PropertyTypeOption` 
        :returns:  The created property  
        :rtype: :py:class:`NXOpen.VisualReporting.Property` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteProperty(self, property: Property) -> None:
        """
        Delete :py:class:`NXOpen.VisualReporting.Property` which has no owner.  
        
        Before call this function,
        User must be sure there is no reference to this object
        
        Signature ``DeleteProperty(property)`` 
        
        :param property:  The property to be deleted 
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAndCondition(self) -> Condition:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.Condition`, but does not add it to a
        :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``CreateAndCondition()`` 
        
        :returns:  The created condition  
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateOrCondition(self) -> Condition:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.Condition`, but does not add it to a
        :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``CreateOrCondition()`` 
        
        :returns:  The created condition  
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateNotCondition(self) -> Condition:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.Condition`, but does not add it to a
        :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``CreateNotCondition()`` 
        
        :returns:  The created condition  
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateStringCondition(self, property: Property, value: str, operatorType: ConditionOperatorOption) -> Condition:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Datatype` is
        :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption.String <NXOpen.VisualReporting.PropertyDatatypeOption>`,
        but does not add it to a :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``CreateStringCondition(property, value, operatorType)`` 
        
        :param property:  The :py:class:`NXOpen.VisualReporting.Property` to which this condition will be applied  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        :param value:  The initial value  
        :type value: str 
        :param operatorType:  The initial operator  
        :type operatorType: :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` 
        :returns:  The created condition  
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateIntegerCondition(self, property: Property, value: int, operatorType: ConditionOperatorOption) -> Condition:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Datatype` is
        :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption.Integer <NXOpen.VisualReporting.PropertyDatatypeOption>`,
        but does not add it to a :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``CreateIntegerCondition(property, value, operatorType)`` 
        
        :param property:  The :py:class:`NXOpen.VisualReporting.Property` to which this condition will be applied  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        :param value:  The initial value  
        :type value: int 
        :param operatorType:  The initial operator  
        :type operatorType: :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` 
        :returns:  The created condition  
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateRealCondition(self, property: Property, value: float, operatorType: ConditionOperatorOption, tolerance: float) -> Condition:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Datatype` is
        :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption.Real <NXOpen.VisualReporting.PropertyDatatypeOption>`,
        but does not add it to a :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``CreateRealCondition(property, value, operatorType, tolerance)`` 
        
        :param property:  The :py:class:`NXOpen.VisualReporting.Property` to which this condition will be applied  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        :param value:  The initial value  
        :type value: float 
        :param operatorType:  The initial operator  
        :type operatorType: :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` 
        :param tolerance:  The tolerance used in comparisons  
        :type tolerance: float 
        :returns:  The created condition  
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateBooleanCondition(self, property: Property, value: bool, operatorType: ConditionOperatorOption) -> Condition:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Datatype` is
        :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption.Boolean <NXOpen.VisualReporting.PropertyDatatypeOption>`,
        but does not add it to a :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``CreateBooleanCondition(property, value, operatorType)`` 
        
        :param property:  The :py:class:`NXOpen.VisualReporting.Property` to which this condition will be applied  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        :param value:  The initial value  
        :type value: bool 
        :param operatorType:  The initial operator  
        :type operatorType: :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` 
        :returns:  The created condition  
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateNullCondition(self, property: Property, value: bool, operatorType: ConditionOperatorOption) -> Condition:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Datatype` is
        :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption.Null <NXOpen.VisualReporting.PropertyDatatypeOption>`,
        but does not add it to a :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``CreateNullCondition(property, value, operatorType)`` 
        
        :param property:  The :py:class:`NXOpen.VisualReporting.Property` to which this condition will be applied  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        :param value:  The initial value  
        :type value: bool 
        :param operatorType:  The initial operator  
        :type operatorType: :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` 
        :returns:  The created condition  
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDateCondition(self, property: Property, value: str, operatorType: ConditionOperatorOption) -> Condition:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.Condition` whose
        :py:meth:`NXOpen.VisualReporting.Condition.Datatype` is
        :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption.Date <NXOpen.VisualReporting.PropertyDatatypeOption>`,
        but does not add it to a :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``CreateDateCondition(property, value, operatorType)`` 
        
        :param property:  The :py:class:`NXOpen.VisualReporting.Property` to which this condition will be applied  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        :param value:  The initial value  
        :type value: str 
        :param operatorType:  The initial operator  
        :type operatorType: :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` 
        :returns:  The created condition  
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetParentCondition(self, condition: Condition) -> Condition:
        """
        Gets the parent condition of this :py:class:`NXOpen.VisualReporting.Condition`.  
        
        If this
        condition has no parent or if the parent isn't a condition
        then this returns None.
        
        Signature ``GetParentCondition(condition)`` 
        
        :param condition: 
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns: 
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsChildCondition(self, condition: Condition, childCondition: Condition) -> bool:
        """
        Returns whether the given :py:class:`NXOpen.VisualReporting.Condition` is an immediate child of this condition
        
        Signature ``IsChildCondition(condition, childCondition)`` 
        
        :param condition: 
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param childCondition:  The possible child Condition  
        :type childCondition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetChildCondition(self, condition: Condition, index: int) -> Condition:
        """
        Returns the specified child :py:class:`NXOpen.VisualReporting.Condition` from this :py:class:`NXOpen.VisualReporting.Condition`
        
        Signature ``GetChildCondition(condition, index)`` 
        
        :param condition: 
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param index:  The index of the returned Condition.  
        
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetChildConditions(self, condition: Condition) -> 'list[Condition]':
        """
        Returns all the child :py:class:`NXOpen.VisualReporting.Condition`s in this :py:class:`NXOpen.VisualReporting.Condition`
        
        Signature ``GetChildConditions(condition)`` 
        
        :param condition: 
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateGroupLabel(self, name: str, rule: Rule, afterGroupLabel: GroupLabel) -> GroupLabel:
        """
        Creates a new empty :py:class:`NXOpen.VisualReporting.GroupLabel`, and adds it to the given
        :py:class:`NXOpen.VisualReporting.Rule`.  
        
        This can only be called if the active :py:class:`NXOpen.VisualReporting.Classifier` 
        in this rule is using :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption.Manual <NXOpen.VisualReporting.ClassifierGroupingMethodOption>` grouping.
        
        Signature ``CreateGroupLabel(name, rule, afterGroupLabel)`` 
        
        :param name:  The initial name. If this name is empty then a system-generated name will be                                                                                                                    assigned when the owning :py:class:`NXOpen.VisualReporting.VisualReport` is next activated  
        :type name: str 
        :param rule:  The rule to which to add it  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param afterGroupLabel:  The group label after which to add it. If None then it is inserted                                                                                                                    at the beginning before any existing group labels  
        :type afterGroupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The created group label  
        :rtype: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetPropertySpecification(self, property: Property, key: str) -> None:
        """
        Sets the property specification of the :py:class:`NXOpen.VisualReporting.Property` being built by this builder.
        
        Signature ``SetPropertySpecification(property, key)`` 
        
        :param property:  The property being set  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        :param key:  property key  
        :type key: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetPropertySpecification(self, property: Property, key: str, name: str) -> None:
        """
        Sets the property specification of the :py:class:`NXOpen.VisualReporting.Property` being built by this builder.
        
        Signature ``SetPropertySpecification(property, key, name)`` 
        
        :param property:  The property being set  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        :param key:  property key  
        :type key: str 
        :param name:  property name  
        :type name: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPropertySpecification(self, property: Property) -> tuple:
        """
        Gets the property specification of the :py:class:`NXOpen.VisualReporting.Property` being built by this builder.  
        
        Signature ``GetPropertySpecification(property)`` 
        
        :param property:  The property being ask  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        :returns: a tuple 
        :rtype: A tuple consisting of (propertyType, key, name). propertyType is a :py:class:`NXOpen.VisualReporting.PropertyTypeOption`.   Property Type of the :py:class:`NXOpen.VisualReporting.Property` key is a str.   property key name is a str.   property name 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetReferencePropertiesOfReport(self) -> tuple:
        """
        Gets the message :py:class:`NXOpen.VisualReporting.Property`  list of the :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        Signature ``GetReferencePropertiesOfReport()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (properties, usages, notUsed). properties is a list of :py:class:`NXOpen.VisualReporting.Property`.   The reference properties of reportusages is a list of :py:class:`NXOpen.VisualReporting.VisualReportBuilderPropertyUsageOption`.   The usages of reportnotUsed is a int. 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetReferencePropertiesOfReport(self, properties: 'list[Property]', usages: 'list[VisualReportBuilderPropertyUsageOption]') -> None:
        """
        Sets the message :py:class:`NXOpen.VisualReporting.Property` list of the :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        Signature ``SetReferencePropertiesOfReport(properties, usages)`` 
        
        :param properties:  The reference properties of report 
        :type properties: list of :py:class:`NXOpen.VisualReporting.Property` 
        :param usages:  The usages of report 
        :type usages: list of :py:class:`NXOpen.VisualReporting.VisualReportBuilderPropertyUsageOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Save(self) -> None:
        """
        Saves the :py:class:`NXOpen.VisualReporting.VisualReport` to its current :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.FilenameOfVisualReport` .  
        
        Note that when NX is connected to Teamcenter, the :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.FilenameOfVisualReport` will be 
        updated to the report dataset identifier after the report is saved to Teamcenter database.
        
        Signature ``Save()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTagPriorityOfGroupLabel(self, groupLabel: GroupLabel) -> GroupLabelTagPriorityOption:
        """
        Gets the priority of the given:py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``GetTagPriorityOfGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The priority  
        :rtype: :py:class:`NXOpen.VisualReporting.GroupLabelTagPriorityOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTagPriorityOfGroupLabel(self, groupLabel: GroupLabel, tagPriority: GroupLabelTagPriorityOption) -> None:
        """
        Sets the priority of the given:py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``SetTagPriorityOfGroupLabel(groupLabel, tagPriority)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param tagPriority:  The priority  
        :type tagPriority: :py:class:`NXOpen.VisualReporting.GroupLabelTagPriorityOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetErrorLevelOfGroupLabel(self, groupLabel: GroupLabel) -> NXOpen.ValidationResult:
        """
        Gets the error level of the given:py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``GetErrorLevelOfGroupLabel(groupLabel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns:  The error level  
        :rtype: :py:class:`NXOpen.ValidationResult` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetErrorLevelOfGroupLabel(self, groupLabel: GroupLabel, errorLevel: NXOpen.ValidationResult) -> None:
        """
        Sets the priority of the given:py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``SetErrorLevelOfGroupLabel(groupLabel, errorLevel)`` 
        
        :param groupLabel:  The group label  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param errorLevel:  The error level  
        :type errorLevel: :py:class:`NXOpen.ValidationResult` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteChildCondition(self, condition: Condition, childCondition: Condition) -> None:
        """
        Deletes a :py:class:`NXOpen.VisualReporting.Condition` from its parent condition.  
        
        If there are :py:class:`NXOpen.VisualReporting.Property`s associated with this condition, these properties will be deleted.
        If there are child conditions associated with this condtion, these child conditions will be deleted too. 
        
        Signature ``DeleteChildCondition(condition, childCondition)`` 
        
        :param condition:  The condition  
        :type condition: :py:class:`NXOpen.VisualReporting.Condition` 
        :param childCondition:  The child condition being removed  
        :type childCondition: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDateGroupMethodOfRule(self, rule: Rule) -> ClassifierDateGroupMethodOption:
        """
        Gets the :py:class:`NXOpen.VisualReporting.ClassifierDateGroupMethodOption` of the active :py:class:`NXOpen.VisualReporting.Classifier` 
        in the given :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Only valid if the active :py:class:`NXOpen.VisualReporting.Classifier` in the rule 
        is :py:class:`NXOpen.VisualReporting.ClassifierTypeOption.Range <NXOpen.VisualReporting.ClassifierTypeOption>` type.
        
        Signature ``GetDateGroupMethodOfRule(rule)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :returns:  The range method  
        :rtype: :py:class:`NXOpen.VisualReporting.ClassifierDateGroupMethodOption` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetDateGroupMethodOfRule(self, rule: Rule, dateGroupMethod: ClassifierDateGroupMethodOption) -> None:
        """
        Sets the :py:class:`NXOpen.VisualReporting.ClassifierDateGroupMethodOption` of the active :py:class:`NXOpen.VisualReporting.Classifier` 
        in the given :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Only valid if the active :py:class:`NXOpen.VisualReporting.Classifier` in the rule 
        is :py:class:`NXOpen.VisualReporting.ClassifierTypeOption.Range <NXOpen.VisualReporting.ClassifierTypeOption>` type.
        
        Signature ``SetDateGroupMethodOfRule(rule, dateGroupMethod)`` 
        
        :param rule:  The rule  
        :type rule: :py:class:`NXOpen.VisualReporting.Rule` 
        :param dateGroupMethod:  The range method  
        :type dateGroupMethod: :py:class:`NXOpen.VisualReporting.ClassifierDateGroupMethodOption` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetObjectTypesOfVisualReport(self) -> 'list[VisualReportObjectTypeOption]':
        """
        Gets the :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption`s of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this builder.  
        
        Only valid if the :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` of the :py:class:`NXOpen.VisualReporting.VisualReport`
        is :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption.SubPart <NXOpen.VisualReporting.VisualReportScopeTypeOption>` type.
        
        Signature ``GetObjectTypesOfVisualReport()`` 
        
        :returns:  The object types  
        :rtype: list of :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetObjectTypesOfVisualReport(self, objectTypes: 'list[VisualReportObjectTypeOption]') -> None:
        """
        Sets the :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption`s of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this builder.  
        
        Only valid if the :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` of the :py:class:`NXOpen.VisualReporting.VisualReport`
        is :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption.SubPart <NXOpen.VisualReporting.VisualReportScopeTypeOption>` type.
        
        Signature ``SetObjectTypesOfVisualReport(objectTypes)`` 
        
        :param objectTypes:  The object types being set  
        :type objectTypes: list of :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    BitmapNameOfReport: str = ...
    """
    Returns or sets  the bitmap name of the :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    <hr>
    
    Getter Method
    
    Signature ``BitmapNameOfReport`` 
    
    :returns:  The bitmap name  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BitmapNameOfReport`` 
    
    :param bitmapName:  The bitmap name  
    :type bitmapName: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    BitmapNameOfReportingProperty: str = ...
    """
    Returns or sets  the bitmap name of the reporting :py:class:`NXOpen.VisualReporting.Property` in the active :py:class:`NXOpen.VisualReporting.Classifier`.  
    
    <hr>
    
    Getter Method
    
    Signature ``BitmapNameOfReportingProperty`` 
    
    :returns:  The bitmap name  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BitmapNameOfReportingProperty`` 
    
    :param bitmapName:  The bitmap name  
    :type bitmapName: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    CustomMessageOfReport: str = ...
    """
    Returns or sets the custom message of the :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomMessageOfReport`` 
    
    :returns:  The custom message  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomMessageOfReport`` 
    
    :param customMessage:  The custom message  
    :type customMessage: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    CustomMessageOfReportingProperty: str = ...
    """
    Returns or sets the custom message of the reporting :py:class:`NXOpen.VisualReporting.Property` in the active :py:class:`NXOpen.VisualReporting.Classifier`.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomMessageOfReportingProperty`` 
    
    :returns:  The custom message  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomMessageOfReportingProperty`` 
    
    :param customMessage:  The custom message  
    :type customMessage: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    DescriptionOfVisualReport: str = ...
    """
    Returns or sets  the description of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this
    builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``DescriptionOfVisualReport`` 
    
    :returns:  The description  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DescriptionOfVisualReport`` 
    
    :param description:  The description  
    :type description: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    DescriptiveCategoryOfVisualReport: str = ...
    """
    Returns or sets  the descriptive category of the :py:class:`NXOpen.VisualReporting.VisualReport`
    being built by this builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``DescriptiveCategoryOfVisualReport`` 
    
    :returns:  The category  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DescriptiveCategoryOfVisualReport`` 
    
    :param category:  The category being set  
    :type category: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    DestinationTeamcenterFolder: str = ...
    """
    Returns or sets  the destination Teamcenter folder for saving the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this
    builder to Teamcenter database.  
    
    Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
    This :py:meth:`NXOpen.VisualReporting.VisualReport.DestinationTeamcenterFolder` may return None if you haven't 
    set a folder name on this property.
    
    <hr>
    
    Getter Method
    
    Signature ``DestinationTeamcenterFolder`` 
    
    :returns:  The Teamcenter folder name  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DestinationTeamcenterFolder`` 
    
    :param foldername:  The Teamcenter folder name  
    :type foldername: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    FilenameOfVisualReport: str = ...
    """
    Returns or sets  the file name of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this
    builder.  
    
    Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
    If it is a new report, it will be the report dataset name. When the report is save by :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.Save`, 
    the report dataset identifier will be saved in this property.
    
    <hr>
    
    Getter Method
    
    Signature ``FilenameOfVisualReport`` 
    
    :returns:  The file name  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FilenameOfVisualReport`` 
    
    :param filename:  The file name  
    :type filename: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    KeywordsOfVisualReport: str = ...
    """
    Returns or sets  the keywords of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this
    builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``KeywordsOfVisualReport`` 
    
    :returns:  A comma separated string of keywords  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``KeywordsOfVisualReport`` 
    
    :param keywords:  A comma separated string of keywords  
    :type keywords: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ReportContextOfVisualReport: VisualReportReportContextOption = ...
    """
    Returns or sets  the :py:class:`NXOpen.VisualReporting.VisualReportReportContextOption` of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReportContextOfVisualReport`` 
    
    :returns:  The report context  
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportReportContextOption` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX9.0.3
       Use :py:meth:`NXOpen.VisualReporting.VisualReport.ReportContext` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportContextOfVisualReport`` 
    
    :param reportContext:  The report context being set  
    :type reportContext: :py:class:`NXOpen.VisualReporting.VisualReportReportContextOption` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX9.0.3
       Use :py:meth:`NXOpen.VisualReporting.VisualReport.ReportContext` instead.
    
    License requirements: None.
    """
    ReportNameOfVisualReport: str = ...
    """
    Returns or sets  the name of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReportNameOfVisualReport`` 
    
    :returns:  The name of the report  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportNameOfVisualReport`` 
    
    :param reportName:  The name of the report  
    :type reportName: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ReportingObjectTypeOfVisualReport: VisualReportReportingObjectTypeOption = ...
    """
    Returns or sets  the reporting object type of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this builder.  
    
    Only valid if the :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` of the :py:class:`NXOpen.VisualReporting.VisualReport`
    is :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption.Component <NXOpen.VisualReporting.VisualReportScopeTypeOption>` type.
    
    <hr>
    
    Getter Method
    
    Signature ``ReportingObjectTypeOfVisualReport`` 
    
    :returns:  The reporting object being set  
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportReportingObjectTypeOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportingObjectTypeOfVisualReport`` 
    
    :param reportingObjectType:  The reporting object being set  
    :type reportingObjectType: :py:class:`NXOpen.VisualReporting.VisualReportReportingObjectTypeOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ReportingStyleOfVisualReport: VisualReportReportingStyleOption = ...
    """
    Returns or sets  the reporting style of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReportingStyleOfVisualReport`` 
    
    :returns:  The reporting style  
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportReportingStyleOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportingStyleOfVisualReport`` 
    
    :param reportingStyle:  The reporting style being set  
    :type reportingStyle: :py:class:`NXOpen.VisualReporting.VisualReportReportingStyleOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SaveDestination: VisualReportSaveDestinationOption = ...
    """
    Returns or sets  the :py:class:`NXOpen.VisualReporting.VisualReportSaveDestinationOption` of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this
    builder.  
    
    Note that this property will always be :py:class:`NXOpen.VisualReporting.VisualReportSaveDestinationOption.Local <NXOpen.VisualReporting.VisualReportSaveDestinationOption>` when NX is not connected to Teamcenter.
    
    <hr>
    
    Getter Method
    
    Signature ``SaveDestination`` 
    
    :returns:  The destination option  
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportSaveDestinationOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SaveDestination`` 
    
    :param destinationOption:  The destination option  
    :type destinationOption: :py:class:`NXOpen.VisualReporting.VisualReportSaveDestinationOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ScopeTypeOfVisualReport: VisualReportScopeTypeOption = ...
    """
    Returns or sets  the :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption` of the :py:class:`NXOpen.VisualReporting.VisualReport` being built by this builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``ScopeTypeOfVisualReport`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScopeTypeOfVisualReport`` 
    
    :param scopeType: 
    :type scopeType: :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: VisualReportBuilder = ...  # unknown typename


class VisualReportReportingStyleOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VisualReportReportingStyleOption():
    """
    Represents the possible :py:meth:`NXOpen.VisualReporting.VisualReport.ReportingStyle`
    for a :py:class:`NXOpen.VisualReporting.VisualReport`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ColorObject", "Matching objects will be colored"
       "TagObject", "Matching objects will be tagged"
       "ColorAndTagObject", "Matching objects will be both colored and tagged"
    """
    ColorObject = 0  # VisualReportReportingStyleOptionMemberType
    TagObject = 1  # VisualReportReportingStyleOptionMemberType
    ColorAndTagObject = 2  # VisualReportReportingStyleOptionMemberType
    
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
    


class VisualReportReportingObjectTypeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VisualReportReportingObjectTypeOption():
    """
    Represents the possible :py:meth:`NXOpen.VisualReporting.VisualReport.ReportingObjectType`
    for a :py:class:`NXOpen.VisualReporting.VisualReport`.
    Only valid if the :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` of the :py:class:`NXOpen.VisualReporting.VisualReport`
    is :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption.Component <NXOpen.VisualReporting.VisualReportScopeTypeOption>` type.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Part", "The reporting objects are parts."
       "Component", "The reporting objects are components."
       "Inferred", "The reporting objects are inferred from the properties used in the report."
    """
    Part = 0  # VisualReportReportingObjectTypeOptionMemberType
    Component = 1  # VisualReportReportingObjectTypeOptionMemberType
    Inferred = 2  # VisualReportReportingObjectTypeOptionMemberType
    
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
    


class VisualReportSaveDestinationOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VisualReportSaveDestinationOption():
    """
    Represents the possible :py:meth:`NXOpen.VisualReporting.VisualReport.SaveDestination` options
    for a :py:class:`NXOpen.VisualReporting.VisualReport`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Local", "Saves the report in the local file system."
       "Teamcenter", "Saves the report in the Teamcenter database."
    """
    Local = 0  # VisualReportSaveDestinationOptionMemberType
    Teamcenter = 1  # VisualReportSaveDestinationOptionMemberType
    
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
    


class VisualReportScopeTypeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VisualReportScopeTypeOption():
    """
    Represents the possible :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` options
    for a :py:class:`NXOpen.VisualReporting.VisualReport`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Component", "The report is assembly component report"
       "SubPart", "The report is sub-part object report"
    """
    Component = 0  # VisualReportScopeTypeOptionMemberType
    SubPart = 1  # VisualReportScopeTypeOptionMemberType
    
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
    


class VisualReportObjectTypeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VisualReportObjectTypeOption():
    """
    Represents the possible report object type options
    for a :py:class:`NXOpen.VisualReporting.VisualReport`.
    Only valid if the :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` of the :py:class:`NXOpen.VisualReporting.VisualReport`
    is :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption.SubPart <NXOpen.VisualReporting.VisualReportScopeTypeOption>` type.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Body", "The report objects are bodies"
       "Face", "The report objects are faces"
    """
    Body = 0  # VisualReportObjectTypeOptionMemberType
    Face = 1  # VisualReportObjectTypeOptionMemberType
    
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
    


class VisualReportReportContextOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VisualReportReportContextOption():
    """
    Represents the possible :py:meth:`NXOpen.VisualReporting.VisualReport.ReportContext` options
    for a :py:class:`NXOpen.VisualReporting.VisualReport`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Assembly", "Collect objects from entire assembly"
       "WorkPart", "Collect objects from work part only"
    """
    Assembly = 0  # VisualReportReportContextOptionMemberType
    WorkPart = 1  # VisualReportReportContextOptionMemberType
    
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
    


class VisualReport(NXOpen.NXObject):
    """
    A visual report can be activated by the :py:class:`NXOpen.VisualReporting.VisualReportManager` to 
    apply colors to objects in the graphics window.  
    
    An active visual report groups objects according to filtering conditions and classification 
    rules.  The contents of the groups can be accessed via :py:meth:`NXOpen.VisualReporting.VisualReport.GetGroupLabels`
    and :py:meth:`NXOpen.VisualReporting.VisualReport.GetObjectsInGroup`.
    
    .. versionadded:: NX7.0.0
    """
    
    class ReportingStyleOption():
        """
        Represents the possible :py:meth:`NXOpen.VisualReporting.VisualReport.ReportingStyle`
        for a :py:class:`NXOpen.VisualReporting.VisualReport`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ColorObject", "Matching objects will be colored"
           "TagObject", "Matching objects will be tagged"
           "ColorAndTagObject", "Matching objects will be both colored and tagged"
        """
        ColorObject = 0  # VisualReportReportingStyleOptionMemberType
        TagObject = 1  # VisualReportReportingStyleOptionMemberType
        ColorAndTagObject = 2  # VisualReportReportingStyleOptionMemberType
        
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
        
    
    
    class ReportingObjectTypeOption():
        """
        Represents the possible :py:meth:`NXOpen.VisualReporting.VisualReport.ReportingObjectType`
        for a :py:class:`NXOpen.VisualReporting.VisualReport`.
        Only valid if the :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` of the :py:class:`NXOpen.VisualReporting.VisualReport`
        is :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption.Component <NXOpen.VisualReporting.VisualReportScopeTypeOption>` type.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Part", "The reporting objects are parts."
           "Component", "The reporting objects are components."
           "Inferred", "The reporting objects are inferred from the properties used in the report."
        """
        Part = 0  # VisualReportReportingObjectTypeOptionMemberType
        Component = 1  # VisualReportReportingObjectTypeOptionMemberType
        Inferred = 2  # VisualReportReportingObjectTypeOptionMemberType
        
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
        
    
    
    class SaveDestinationOption():
        """
        Represents the possible :py:meth:`NXOpen.VisualReporting.VisualReport.SaveDestination` options
        for a :py:class:`NXOpen.VisualReporting.VisualReport`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Local", "Saves the report in the local file system."
           "Teamcenter", "Saves the report in the Teamcenter database."
        """
        Local = 0  # VisualReportSaveDestinationOptionMemberType
        Teamcenter = 1  # VisualReportSaveDestinationOptionMemberType
        
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
        
    
    
    class ScopeTypeOption():
        """
        Represents the possible :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` options
        for a :py:class:`NXOpen.VisualReporting.VisualReport`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Component", "The report is assembly component report"
           "SubPart", "The report is sub-part object report"
        """
        Component = 0  # VisualReportScopeTypeOptionMemberType
        SubPart = 1  # VisualReportScopeTypeOptionMemberType
        
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
        
    
    
    class ObjectTypeOption():
        """
        Represents the possible report object type options
        for a :py:class:`NXOpen.VisualReporting.VisualReport`.
        Only valid if the :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` of the :py:class:`NXOpen.VisualReporting.VisualReport`
        is :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption.SubPart <NXOpen.VisualReporting.VisualReportScopeTypeOption>` type.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Body", "The report objects are bodies"
           "Face", "The report objects are faces"
        """
        Body = 0  # VisualReportObjectTypeOptionMemberType
        Face = 1  # VisualReportObjectTypeOptionMemberType
        
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
        
    
    
    class ReportContextOption():
        """
        Represents the possible :py:meth:`NXOpen.VisualReporting.VisualReport.ReportContext` options
        for a :py:class:`NXOpen.VisualReporting.VisualReport`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Assembly", "Collect objects from entire assembly"
           "WorkPart", "Collect objects from work part only"
        """
        Assembly = 0  # VisualReportReportContextOptionMemberType
        WorkPart = 1  # VisualReportReportContextOptionMemberType
        
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
        
    
    
    def Save(self) -> None:
        """
        Saves this :py:class:`NXOpen.VisualReporting.VisualReport` to its current :py:meth:`NXOpen.VisualReporting.VisualReport.Filename`.  
        
        Note that when NX is connected to Teamcenter, the :py:meth:`NXOpen.VisualReporting.VisualReport.Filename` will be 
        updated to the report dataset identifier after the report is saved to Teamcenter database.
        
        Signature ``Save()`` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    
    def GetRule(self, index: int) -> Rule:
        """
        Return the specified :py:class:`NXOpen.VisualReporting.Rule` from this :py:class:`NXOpen.VisualReporting.VisualReport`
        
        Signature ``GetRule(index)`` 
        
        :param index:  The index of the returned :py:class:`NXOpen.VisualReporting.Rule`.  
        
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.VisualReporting.Rule` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRules(self) -> 'list[Rule]':
        """
        Returns all the :py:class:`NXOpen.VisualReporting.Rule`s in this :py:class:`NXOpen.VisualReporting.VisualReport`
        
        Signature ``GetRules()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.VisualReporting.Rule` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetResultCategories(self) -> 'list[ResultCategory]':
        """
        Returns the :py:class:`NXOpen.VisualReporting.ResultCategory`s from the activated :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        There are no :py:class:`NXOpen.VisualReporting.ResultCategory`s if the :py:class:`NXOpen.VisualReporting.VisualReport` is not activated.
        
        Signature ``GetResultCategories()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.VisualReporting.ResultCategory` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetGroupLabelsOfResultCategory(self, category: ResultCategory) -> 'list[GroupLabel]':
        """
        Returns the result :py:class:`NXOpen.VisualReporting.GroupLabel`s of a :py:class:`NXOpen.VisualReporting.ResultCategory`
        from the activated :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        Signature ``GetGroupLabelsOfResultCategory(category)`` 
        
        :param category: 
        :type category: :py:class:`NXOpen.VisualReporting.ResultCategory` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetGroupLabels(self) -> 'list[GroupLabel]':
        """
        Returns the result :py:class:`NXOpen.VisualReporting.GroupLabel`s from the activated :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        There are no :py:class:`NXOpen.VisualReporting.GroupLabel`s if the :py:class:`NXOpen.VisualReporting.VisualReport` is not activated.
        You can acess the user defined :py:class:`NXOpen.VisualReporting.GroupLabel`s by :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.GetManualGroupLabelsOfRule`.
        
        Signature ``GetGroupLabels()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.VisualReporting.GroupLabel` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetObjectsInGroup(self, groupLabel: GroupLabel) -> 'list[NXOpen.NXObject]':
        """
        Returns the :py:class:`NXOpen.NXObject`s that belong to the group
        with this :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        Signature ``GetObjectsInGroup(groupLabel)`` 
        
        :param groupLabel:  A group label of this visual report  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetKeywords(self) -> str:
        """
        Gets a comma separated string of the keywords for this :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        Signature ``GetKeywords()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetKeywords(self, keywords: str) -> None:
        """
        Sets a comma separated string of the keywords for this :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        Signature ``SetKeywords(keywords)`` 
        
        :param keywords: 
        :type keywords: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    
    def RemoveResultCategory(self, theCategory: ResultCategory) -> None:
        """
        Removes the :py:class:`NXOpen.VisualReporting.ResultCategory` from :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        The :py:class:`NXOpen.VisualReporting.Classifier` which populates this :py:class:`NXOpen.VisualReporting.ResultCategory` 
        will also be removed from the :py:class:`NXOpen.VisualReporting.Rule` in the :py:class:`NXOpen.VisualReporting.VisualReport`.
        
        Signature ``RemoveResultCategory(theCategory)`` 
        
        :param theCategory: 
        :type theCategory: :py:class:`NXOpen.VisualReporting.ResultCategory` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    
    def GetAllDefinedProperties(self) -> 'list[Property]':
        """
        Returns the :py:class:`NXOpen.VisualReporting.Property`s which has been defined in this :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        The returned properties include those properties defined in :py:class:`NXOpen.VisualReporting.Condition`s, in :py:class:`NXOpen.VisualReporting.Classifier`s,
        and in the referenced properties.
        
        Signature ``GetAllDefinedProperties()`` 
        
        :returns:  Properties defined in this visual report  
        :rtype: list of :py:class:`NXOpen.VisualReporting.Property` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPropertyValueOfObject(self, property: Property, groupLabel: GroupLabel, nxObject: NXOpen.NXObject) -> str:
        """
        Returns the value of the :py:class:`NXOpen.VisualReporting.Property`s for the :py:class:`NXOpen.NXObject` in the result :py:class:`NXOpen.VisualReporting.GroupLabel`.  
        
        It will return None if the :py:class:`NXOpen.VisualReporting.VisualReport` is not activated, or the :py:class:`NXOpen.VisualReporting.Property`
        does not belong to the properties defined in this :py:class:`NXOpen.VisualReporting.VisualReport`, or the :py:class:`NXOpen.NXObject` doesn't belong to
        the specified result :py:class:`NXOpen.VisualReporting.GroupLabel`.
        
        Signature ``GetPropertyValueOfObject(property, groupLabel, nxObject)`` 
        
        :param property:  A property defined in this visual report  
        :type property: :py:class:`NXOpen.VisualReporting.Property` 
        :param groupLabel:  A result group of this visual report  
        :type groupLabel: :py:class:`NXOpen.VisualReporting.GroupLabel` 
        :param nxObject:  A :py:class:`NXOpen.NXObject` which belongs to the result group  
        :type nxObject: :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetObjectTypes(self) -> 'list[VisualReportObjectTypeOption]':
        """
        Returns the :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption`s of this :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        Only valid if the :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` of the :py:class:`NXOpen.VisualReporting.VisualReport`
        is :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption.SubPart <NXOpen.VisualReporting.VisualReportScopeTypeOption>` type.
        
        Signature ``GetObjectTypes()`` 
        
        :returns:  The object types  
        :rtype: list of :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    BitmapName: str = ...
    """
    Returns or sets  the bitmap name of this :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    <hr>
    
    Getter Method
    
    Signature ``BitmapName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BitmapName`` 
    
    :param bitmapName: 
    :type bitmapName: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    CustomMessage: str = ...
    """
    Returns or sets  the custom message of this :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomMessage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomMessage`` 
    
    :param customMessage: 
    :type customMessage: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    Description: str = ...
    """
    Returns or sets  the description of this :py:class:`NXOpen.VisualReporting.VisualReport`
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Description`` 
    
    :param description: 
    :type description: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    DescriptiveCategory: str = ...
    """
    Returns or sets  the category of this :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    <hr>
    
    Getter Method
    
    Signature ``DescriptiveCategory`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DescriptiveCategory`` 
    
    :param category: 
    :type category: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    DestinationTeamcenterFolder: str = ...
    """
    Returns or sets  the destination Teamcenter folder for saving the :py:class:`NXOpen.VisualReporting.VisualReport` to Teamcenter database.  
    
    Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
    This :py:meth:`NXOpen.VisualReporting.VisualReport.DestinationTeamcenterFolder` may return None if you haven't 
    set a folder name on this property.
    
    <hr>
    
    Getter Method
    
    Signature ``DestinationTeamcenterFolder`` 
    
    :returns:  The Teamcenter folder name  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DestinationTeamcenterFolder`` 
    
    :param foldername:  The Teamcenter folder name  
    :type foldername: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    Filename: str = ...
    """
    Returns or sets  the filename where this :py:class:`NXOpen.VisualReporting.VisualReport` was opened from or will be saved to.  
    
    Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
    If it is a new report, it will be the report dataset name. When the report is save by :py:meth:`NXOpen.VisualReporting.VisualReport.Save`, 
    the report dataset identifier will be saved in this property.
    
    <hr>
    
    Getter Method
    
    Signature ``Filename`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Filename`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    IsUnmatchedGroupEnabled: bool = ...
    """
    Returns or sets  whether use of :py:meth:`NXOpen.VisualReporting.VisualReport.UnmatchedGroupLabel`
    is enabled.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsUnmatchedGroupEnabled`` 
    
    :returns:  Whether the unmatched group is enabled  
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsUnmatchedGroupEnabled`` 
    
    :param isUnmatchedGroupEnabled:  Whether the unmatched group is enabled  
    :type isUnmatchedGroupEnabled: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    ReportContext: VisualReportReportContextOption = ...
    """
    Returns or sets  the :py:class:`NXOpen.VisualReporting.VisualReportReportContextOption` of this :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReportContext`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportReportContextOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportContext`` 
    
    :param reportContext: 
    :type reportContext: :py:class:`NXOpen.VisualReporting.VisualReportReportContextOption` 
    
    .. versionadded:: NX9.0.3
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    ReportingObjectType: VisualReportReportingObjectTypeOption = ...
    """
    Returns or sets  the :py:class:`NXOpen.VisualReporting.VisualReportReportingObjectTypeOption` of this :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    Only valid if the :py:meth:`NXOpen.VisualReporting.VisualReport.ScopeType` of the :py:class:`NXOpen.VisualReporting.VisualReport`
    is :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption.Component <NXOpen.VisualReporting.VisualReportScopeTypeOption>` type.
    
    <hr>
    
    Getter Method
    
    Signature ``ReportingObjectType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportReportingObjectTypeOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportingObjectType`` 
    
    :param reportingObjectType: 
    :type reportingObjectType: :py:class:`NXOpen.VisualReporting.VisualReportReportingObjectTypeOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    ReportingStyle: VisualReportReportingStyleOption = ...
    """
    Returns or sets  the :py:class:`NXOpen.VisualReporting.VisualReportReportingStyleOption` of this :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReportingStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportReportingStyleOption` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportingStyle`` 
    
    :param reportingStyle: 
    :type reportingStyle: :py:class:`NXOpen.VisualReporting.VisualReportReportingStyleOption` 
    
    .. versionadded:: NX7.5.1
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    SaveDestination: VisualReportSaveDestinationOption = ...
    """
    Returns or sets  the :py:class:`NXOpen.VisualReporting.VisualReportSaveDestinationOption` of the :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    Note that this property will always be :py:class:`NXOpen.VisualReporting.VisualReportSaveDestinationOption.Local <NXOpen.VisualReporting.VisualReportSaveDestinationOption>` when NX is not connected to Teamcenter.
    
    <hr>
    
    Getter Method
    
    Signature ``SaveDestination`` 
    
    :returns:  The destination option  
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportSaveDestinationOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SaveDestination`` 
    
    :param destinationOption:  The destination option  
    :type destinationOption: :py:class:`NXOpen.VisualReporting.VisualReportSaveDestinationOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    ScopeType: VisualReportScopeTypeOption = ...
    """
    Returns  the :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption` of this :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ScopeType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    UnmatchedGroupLabel: GroupLabel = ...
    """
    Returns  the :py:class:`NXOpen.VisualReporting.GroupLabel` which is used for unmatched object.  
    
    It will return None if the :py:class:`NXOpen.VisualReporting.VisualReport` is not activated.
    
    <hr>
    
    Getter Method
    
    Signature ``UnmatchedGroupLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.GroupLabel` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    UnmatchedResultCategory: UnmatchedResultCategory = ...
    """
    Returns  the :py:class:`NXOpen.VisualReporting.UnmatchedResultCategory` from the activated :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    It will return None if the :py:class:`NXOpen.VisualReporting.VisualReport` is not activated.
    
    <hr>
    
    Getter Method
    
    Signature ``UnmatchedResultCategory`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.UnmatchedResultCategory` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: VisualReport = ...  # unknown typename


class SpecifyDateBuilder(NXOpen.Builder):
    """
    Represents a Specify Date Builder  
    
    To create a new instance of this class, use :py:meth:`NXOpen.VisualReporting.VisualReportManager.CreateSpecifyDateBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Date: NXOpen.DateBuilder = ...
    """
    Returns  the date 
    
    <hr>
    
    Getter Method
    
    Signature ``Date`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DateBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    DateString: str = ...
    """
    Returns  the current date as string
    
    <hr>
    
    Getter Method
    
    Signature ``DateString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    RelativeDateString: str = ...
    """
    Returns or sets  the current relative date string 
    
    <hr>
    
    Getter Method
    
    Signature ``RelativeDateString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RelativeDateString`` 
    
    :param dateString: 
    :type dateString: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: SpecifyDateBuilder = ...  # unknown typename


class ConditionTypeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConditionTypeOption():
    """
    Represents the possible type options
    for a :py:class:`NXOpen.VisualReporting.Condition`. If the type is a
    :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
    the type of value can be found from :py:meth:`NXOpen.VisualReporting.Condition.Datatype`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AndCondition", " - "
       "OrCondition", " - "
       "NotCondition", " - "
       "ValueCondition", " - "
    """
    AndCondition = 0  # ConditionTypeOptionMemberType
    OrCondition = 1  # ConditionTypeOptionMemberType
    NotCondition = 2  # ConditionTypeOptionMemberType
    ValueCondition = 3  # ConditionTypeOptionMemberType
    
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
    


class ConditionOperatorOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConditionOperatorOption():
    """
    Represents the possible operator type options.
    for a :py:class:`NXOpen.VisualReporting.Condition`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "EqualOperator", " - "
       "LessThanOperator", " - "
       "NotLessThanOperator", " - "
       "GreaterThanOperator", " - "
       "NotGreaterThanOperator", " - "
       "NotEqualOperator", " - "
       "RegularExpressionOperator", " - "
       "ContainsOperator", " - "
       "DoesNotContainOperator", " - "
       "OnOrBeforeOperator", " - "
       "OnOrAfterOperator", " - "
    """
    EqualOperator = 0  # ConditionOperatorOptionMemberType
    LessThanOperator = 1  # ConditionOperatorOptionMemberType
    NotLessThanOperator = 2  # ConditionOperatorOptionMemberType
    GreaterThanOperator = 3  # ConditionOperatorOptionMemberType
    NotGreaterThanOperator = 4  # ConditionOperatorOptionMemberType
    NotEqualOperator = 5  # ConditionOperatorOptionMemberType
    RegularExpressionOperator = 6  # ConditionOperatorOptionMemberType
    ContainsOperator = 7  # ConditionOperatorOptionMemberType
    DoesNotContainOperator = 8  # ConditionOperatorOptionMemberType
    OnOrBeforeOperator = 9  # ConditionOperatorOptionMemberType
    OnOrAfterOperator = 10  # ConditionOperatorOptionMemberType
    
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
    


class Condition(NXOpen.NXObject):
    """
    A Condition within a :py:class:`NXOpen.VisualReporting.Rule`.  
    
    .. versionadded:: NX7.0.0
    """
    
    class TypeOption():
        """
        Represents the possible type options
        for a :py:class:`NXOpen.VisualReporting.Condition`. If the type is a
        :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
        the type of value can be found from :py:meth:`NXOpen.VisualReporting.Condition.Datatype`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AndCondition", " - "
           "OrCondition", " - "
           "NotCondition", " - "
           "ValueCondition", " - "
        """
        AndCondition = 0  # ConditionTypeOptionMemberType
        OrCondition = 1  # ConditionTypeOptionMemberType
        NotCondition = 2  # ConditionTypeOptionMemberType
        ValueCondition = 3  # ConditionTypeOptionMemberType
        
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
        
    
    
    class OperatorOption():
        """
        Represents the possible operator type options.
        for a :py:class:`NXOpen.VisualReporting.Condition`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "EqualOperator", " - "
           "LessThanOperator", " - "
           "NotLessThanOperator", " - "
           "GreaterThanOperator", " - "
           "NotGreaterThanOperator", " - "
           "NotEqualOperator", " - "
           "RegularExpressionOperator", " - "
           "ContainsOperator", " - "
           "DoesNotContainOperator", " - "
           "OnOrBeforeOperator", " - "
           "OnOrAfterOperator", " - "
        """
        EqualOperator = 0  # ConditionOperatorOptionMemberType
        LessThanOperator = 1  # ConditionOperatorOptionMemberType
        NotLessThanOperator = 2  # ConditionOperatorOptionMemberType
        GreaterThanOperator = 3  # ConditionOperatorOptionMemberType
        NotGreaterThanOperator = 4  # ConditionOperatorOptionMemberType
        NotEqualOperator = 5  # ConditionOperatorOptionMemberType
        RegularExpressionOperator = 6  # ConditionOperatorOptionMemberType
        ContainsOperator = 7  # ConditionOperatorOptionMemberType
        DoesNotContainOperator = 8  # ConditionOperatorOptionMemberType
        OnOrBeforeOperator = 9  # ConditionOperatorOptionMemberType
        OnOrAfterOperator = 10  # ConditionOperatorOptionMemberType
        
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
        
    
    
    def IsChildCondition(self, childCondition: Condition) -> bool:
        """
        Returns whether the given :py:class:`NXOpen.VisualReporting.Condition` is an immediate child of this condition
        
        Signature ``IsChildCondition(childCondition)`` 
        
        :param childCondition:  The possible child Condition  
        :type childCondition: :py:class:`NXOpen.VisualReporting.Condition` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetChildCondition(self, index: int) -> Condition:
        """
        Return the specified child Condition from this :py:class:`NXOpen.VisualReporting.Condition`
        
        Signature ``GetChildCondition(index)`` 
        
        :param index:  The index of the returned Condition.  
        
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetChildConditions(self) -> 'list[Condition]':
        """
        Returns all the child Conditions in this :py:class:`NXOpen.VisualReporting.Condition`
        
        Signature ``GetChildConditions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.VisualReporting.Condition` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    Datatype: PropertyDatatypeOption = ...
    """
    Returns  the :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` of this :py:class:`NXOpen.VisualReporting.Condition`.  
    
    The returned data type will never be
    :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption.Unknown <NXOpen.VisualReporting.PropertyDatatypeOption>`.
    
    Note that this :py:meth:`NXOpen.VisualReporting.Condition.Datatype` cannot be modified. 
    Instead it is specified when creating this :py:class:`NXOpen.VisualReporting.Condition` by using the appropriate function:
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateStringCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateIntegerCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateRealCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateBooleanCondition`
    
    Note that the :py:class:`NXOpen.VisualReporting.Condition`s created using the following functions do not
    have :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption`s and calling this function will cause an error for these:
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateAndCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateOrCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateNotCondition`
    
    <hr>
    
    Getter Method
    
    Signature ``Datatype`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Description: str = ...
    """
    Returns or sets  the description for this :py:class:`NXOpen.VisualReporting.Condition`.  
    
    Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
    :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Description`` 
    
    :param description: 
    :type description: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    HasUserSpecifiedValue: bool = ...
    """
    Returns or sets  whether this :py:class:`NXOpen.VisualReporting.Condition` requires user input.  
    
    Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
    :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
    
    <hr>
    
    Getter Method
    
    Signature ``HasUserSpecifiedValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HasUserSpecifiedValue`` 
    
    :param isUserSpecified: 
    :type isUserSpecified: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    OperatorType: ConditionOperatorOption = ...
    """
    Returns or sets  the :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` of this :py:class:`NXOpen.VisualReporting.Condition`.  
    
    Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
    :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
    
    <hr>
    
    Getter Method
    
    Signature ``OperatorType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OperatorType`` 
    
    :param operatorType: 
    :type operatorType: :py:class:`NXOpen.VisualReporting.ConditionOperatorOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    ParentCondition: Condition = ...
    """
    Returns  the parent condition of this :py:class:`NXOpen.VisualReporting.Condition`.  
    
    If this
    condition has no parent or if the parent isn't a condition
    then this returns None.
    
    Note that this :py:meth:`NXOpen.VisualReporting.Condition.ParentCondition` cannot be modified. 
    Instead it is determined when inserting this :py:class:`NXOpen.VisualReporting.Condition` in the :py:class:`NXOpen.VisualReporting.Rule`
    by using the appropriate function:
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.SetFilterConditionOfRule`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.AddChildToCondition`
    
    <hr>
    
    Getter Method
    
    Signature ``ParentCondition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Property: Property = ...
    """
    Returns or sets  the :py:class:`NXOpen.VisualReporting.Property` of this :py:class:`NXOpen.VisualReporting.Condition`.  
    
    If the
    :py:meth:`NXOpen.VisualReporting.Property` is set to None, then it is
    deleted.
    Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
    :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
    
    <hr>
    
    Getter Method
    
    Signature ``Property`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.Property` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Property`` 
    
    :param property: 
    :type property: :py:class:`NXOpen.VisualReporting.Property` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    Type: ConditionTypeOption = ...
    """
    Returns  the :py:class:`NXOpen.VisualReporting.ConditionTypeOption` of this :py:class:`NXOpen.VisualReporting.Condition`
    
    Note that this :py:meth:`NXOpen.VisualReporting.Condition.Type` cannot be modified.  
    
    Instead it is determined when creating this :py:class:`NXOpen.VisualReporting.Condition` by using the appropriate function:
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateStringCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateIntegerCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateRealCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateBooleanCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateAndCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateOrCondition`
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateNotCondition`
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.ConditionTypeOption` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    UserPrompt: str = ...
    """
    Returns or sets  the user prompt for this :py:class:`NXOpen.VisualReporting.Condition`.  
    
    Only useful for a condition where
    :py:meth:`NXOpen.VisualReporting.Condition.HasUserSpecifiedValue` is true.
    Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
    :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
    
    <hr>
    
    Getter Method
    
    Signature ``UserPrompt`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UserPrompt`` 
    
    :param userPrompt: 
    :type userPrompt: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    Value: str = ...
    """
    Returns or sets  the value of this :py:class:`NXOpen.VisualReporting.Condition`.  
    
    Only valid for a :py:class:`NXOpen.VisualReporting.Condition` whose
    :py:meth:`NXOpen.VisualReporting.Condition.Type` is :py:class:`NXOpen.VisualReporting.ConditionTypeOption.ValueCondition <NXOpen.VisualReporting.ConditionTypeOption>`
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param conditionValue: 
    :type conditionValue: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    Null: Condition = ...  # unknown typename


class ResultCategory(NXOpen.NXObject):
    """
    A result category within a :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    .. versionadded:: NX8.0.0
    """
    BitmapName: str = ...
    """
    Returns or sets  the bitmap name of this :py:class:`NXOpen.VisualReporting.ResultCategory`.  
    
    <hr>
    
    Getter Method
    
    Signature ``BitmapName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BitmapName`` 
    
    :param bitmapName: 
    :type bitmapName: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    CustomMessage: str = ...
    """
    Returns or sets  the custom message of this :py:class:`NXOpen.VisualReporting.ResultCategory`.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomMessage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomMessage`` 
    
    :param customMessage: 
    :type customMessage: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    Null: ResultCategory = ...  # unknown typename


class VisualReportManager():
    """
    A manager for load, creation and activation of visual reports.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX7.0.0
    """
    
    def CreateVisualReportBuilder(self, visualReport: VisualReport) -> VisualReportBuilder:
        """
        Creates a :py:class:`NXOpen.VisualReporting.VisualReportBuilder` and starts
        editing a copy of the given :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        Signature ``CreateVisualReportBuilder(visualReport)`` 
        
        :param visualReport:  The VisualReport for which this builder is being created. Can be None  
        :type visualReport: :py:class:`NXOpen.VisualReporting.VisualReport` 
        :returns:  The created builder  
        :rtype: :py:class:`NXOpen.VisualReporting.VisualReportBuilder` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    
    def Open(self, filename: str) -> VisualReport:
        """
        Opens an existing :py:class:`NXOpen.VisualReporting.VisualReport`, but does not set it to be the 
        :py:meth:`NXOpen.VisualReporting.VisualReportManager.Current` visual report or activate it.  
        
        If the visual report file cannot be opened, or if there is a problem parsing the file,
        then an exception will be raised.
        
        If opening a managed report then it is recommended to use :py:meth:`NXOpen.VisualReporting.VisualReportManager.OpenReports`
        which can take a container path and list of dataset names
        
        Signature ``Open(filename)`` 
        
        :param filename:  The filename of the visual report to open  
        :type filename: str 
        :returns: 
        :rtype: :py:class:`NXOpen.VisualReporting.VisualReport` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    
    def Unload(self, visualReport: VisualReport) -> None:
        """
        Unloads an opened  :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        Signature ``Unload(visualReport)`` 
        
        :param visualReport: 
        :type visualReport: :py:class:`NXOpen.VisualReporting.VisualReport` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    
    def OpenReports(self, folders: 'list[str]', names: 'list[str]') -> 'list[VisualReport]':
        """
        Opens existing :py:class:`NXOpen.VisualReporting.VisualReport`, but does not set them to be the 
        :py:meth:`NXOpen.VisualReporting.VisualReportManager.Current` visual report or activate them.  
        
        If the visual report file cannot be opened, or if there is a problem parsing the file,
        then an exception will be raised.
        
        This can be used in native mode by sending in a folder path and filenames, or in
        managed mode using a container path and dataset names.
        
        Signature ``OpenReports(folders, names)`` 
        
        :param folders:  array of folders to be searched  
        :type folders: list of str 
        :param names:  array of report names  
        :type names: list of str 
        :returns:  array of opened reports  
        :rtype: list of :py:class:`NXOpen.VisualReporting.VisualReport` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    
    def ActivateCurrentVisualReport(self) -> None:
        """
        Activates the :py:meth:`NXOpen.VisualReporting.VisualReportManager.Current` visual report.  
        
        Signature ``ActivateCurrentVisualReport()`` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeactivateCurrentVisualReport(self) -> None:
        """
        Deactivates the :py:meth:`NXOpen.VisualReporting.VisualReportManager.Current` visual report.  
        
        Signature ``DeactivateCurrentVisualReport()`` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MergeReports(self, visualReports: 'list[VisualReport]', mergedReportName: str, mergedReportDescription: str) -> VisualReport:
        """
        Merges multiple existing :py:class:`NXOpen.VisualReporting.VisualReport` into one :py:class:`NXOpen.VisualReporting.VisualReport`, but does not set them to be the 
        :py:meth:`NXOpen.VisualReporting.VisualReportManager.Current` visual report or activate them, and does not save the merged :py:class:`NXOpen.VisualReporting.VisualReport`.  
        
        Signature ``MergeReports(visualReports, mergedReportName, mergedReportDescription)`` 
        
        :param visualReports:  array of existing reports  
        :type visualReports: list of :py:class:`NXOpen.VisualReporting.VisualReport` 
        :param mergedReportName:  name of the merged report  
        :type mergedReportName: str 
        :param mergedReportDescription:  description of the merged report  
        :type mergedReportDescription: str 
        :returns:  merged report  
        :rtype: :py:class:`NXOpen.VisualReporting.VisualReport` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    
    def CreateSpecifyDateBuilder(self) -> SpecifyDateBuilder:
        """
        Creates a :py:class:`NXOpen.VisualReporting.SpecifyDateBuilder`.  
        
        Signature ``CreateSpecifyDateBuilder()`` 
        
        :returns:  The created builder  
        :rtype: :py:class:`NXOpen.VisualReporting.SpecifyDateBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReportScopeTypeOption, objectTypes: 'list[VisualReportObjectTypeOption]', dataType: PropertyDatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getStringTypePropertyValue: typing.Callable) -> None:
        """
        Registers a string type property.
        
        The property key and property name should be unique in current session.
        Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
        
        Signature ``RegisterProperty(propertyKey, propertyName, scopeType, objectTypes, dataType, isValidInNative, isValidInTeamcenter, getStringTypePropertyValue)`` 
        
        :param propertyKey:  property key  
        :type propertyKey: str 
        :param propertyName:  property name  
        :type propertyName: str 
        :param scopeType:  property scope type  
        :type scopeType: :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption` 
        :param objectTypes:  object types 
        :type objectTypes: list of :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption` 
        :param dataType:  property data type  
        :type dataType: :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` 
        :param isValidInNative:  is property valid in native mode  
        :type isValidInNative: bool 
        :param isValidInTeamcenter:  is property valid in Teamcenter mode  
        :type isValidInTeamcenter: bool 
        :param getStringTypePropertyValue:  callback function that returns a string type property value  
        :type getStringTypePropertyValue: CallableObject 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    @typing.overload
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReportScopeTypeOption, objectTypes: 'list[VisualReportObjectTypeOption]', dataType: PropertyDatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getIntegerTypePropertyValue: typing.Callable) -> None:
        """
        Registers an integer type property.
        
        The property key and property name should be unique in current session.
        Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
        
        Signature ``RegisterProperty(propertyKey, propertyName, scopeType, objectTypes, dataType, isValidInNative, isValidInTeamcenter, getIntegerTypePropertyValue)`` 
        
        :param propertyKey:  property key  
        :type propertyKey: str 
        :param propertyName:  property name  
        :type propertyName: str 
        :param scopeType:  property scope type  
        :type scopeType: :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption` 
        :param objectTypes:  object types 
        :type objectTypes: list of :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption` 
        :param dataType:  property data type  
        :type dataType: :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` 
        :param isValidInNative:  is property valid in native mode  
        :type isValidInNative: bool 
        :param isValidInTeamcenter:  is property valid in Teamcenter mode  
        :type isValidInTeamcenter: bool 
        :param getIntegerTypePropertyValue:  callback function that returns a integer type property value  
        :type getIntegerTypePropertyValue: CallableObject 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    @typing.overload
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReportScopeTypeOption, objectTypes: 'list[VisualReportObjectTypeOption]', dataType: PropertyDatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getRealTypePropertyValue: typing.Callable) -> None:
        """
        Registers a double type property.
        
        The property key and property name should be unique in current session.
        Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
        
        Signature ``RegisterProperty(propertyKey, propertyName, scopeType, objectTypes, dataType, isValidInNative, isValidInTeamcenter, getRealTypePropertyValue)`` 
        
        :param propertyKey:  property key  
        :type propertyKey: str 
        :param propertyName:  property name  
        :type propertyName: str 
        :param scopeType:  property scope type  
        :type scopeType: :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption` 
        :param objectTypes:  object types 
        :type objectTypes: list of :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption` 
        :param dataType:  property data type  
        :type dataType: :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` 
        :param isValidInNative:  is property valid in native mode  
        :type isValidInNative: bool 
        :param isValidInTeamcenter:  is property valid in Teamcenter mode  
        :type isValidInTeamcenter: bool 
        :param getRealTypePropertyValue:  callback function that returns a double type property value  
        :type getRealTypePropertyValue: CallableObject 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    @typing.overload
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReportScopeTypeOption, objectTypes: 'list[VisualReportObjectTypeOption]', dataType: PropertyDatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getBooleanTypePropertyValue: typing.Callable) -> None:
        """
        Registers a boolean type property.
        
        The property key and property name should be unique in current session.
        Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
        
        Signature ``RegisterProperty(propertyKey, propertyName, scopeType, objectTypes, dataType, isValidInNative, isValidInTeamcenter, getBooleanTypePropertyValue)`` 
        
        :param propertyKey:  property key  
        :type propertyKey: str 
        :param propertyName:  property name  
        :type propertyName: str 
        :param scopeType:  property scope type  
        :type scopeType: :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption` 
        :param objectTypes:  object types 
        :type objectTypes: list of :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption` 
        :param dataType:  property data type  
        :type dataType: :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` 
        :param isValidInNative:  is property valid in native mode  
        :type isValidInNative: bool 
        :param isValidInTeamcenter:  is property valid in Teamcenter mode  
        :type isValidInTeamcenter: bool 
        :param getBooleanTypePropertyValue:  callback function that returns a bool property value  
        :type getBooleanTypePropertyValue: CallableObject 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    @typing.overload
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReportScopeTypeOption, objectTypes: 'list[VisualReportObjectTypeOption]', dataType: PropertyDatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getDateTypePropertyValue: typing.Callable) -> None:
        """
        Registers a :py:class:`NXOpen.NXObjectComputationalTime` type property.
        
        The property key and property name should be unique in current session.
        Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
        
        Signature ``RegisterProperty(propertyKey, propertyName, scopeType, objectTypes, dataType, isValidInNative, isValidInTeamcenter, getDateTypePropertyValue)`` 
        
        :param propertyKey:  property key  
        :type propertyKey: str 
        :param propertyName:  property name  
        :type propertyName: str 
        :param scopeType:  property scope type  
        :type scopeType: :py:class:`NXOpen.VisualReporting.VisualReportScopeTypeOption` 
        :param objectTypes:  object types 
        :type objectTypes: list of :py:class:`NXOpen.VisualReporting.VisualReportObjectTypeOption` 
        :param dataType:  property data type  
        :type dataType: :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` 
        :param isValidInNative:  is property valid in native mode  
        :type isValidInNative: bool 
        :param isValidInTeamcenter:  is property valid in Teamcenter mode  
        :type isValidInTeamcenter: bool 
        :param getDateTypePropertyValue:  callback function that returns a :py:class:`NXOpen.NXObjectComputationalTime` type property value  
        :type getDateTypePropertyValue: CallableObject 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    
    def UnregisterProperty(self, propertyKey: str) -> None:
        """
        Unregisters a property.  
        
        When the library which the property resides in is unloaded from NX session, this method should be called to unregister the property.
        
        Signature ``UnregisterProperty(propertyKey)`` 
        
        :param propertyKey:  property key  
        :type propertyKey: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    Current: VisualReport = ...
    """
    Returns or sets  
    the current :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    <hr>
    
    Getter Method
    
    Signature ``Current`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReport` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Current`` 
    
    :param visualReport: 
    :type visualReport: :py:class:`NXOpen.VisualReporting.VisualReport` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    VisualReports: VisualReportCollection = ...
    """
    Returns the :py:class:`NXOpen.VisualReporting.VisualReportCollection` belonging to this visual report manager 
    
    Signature ``VisualReports`` 
    
    .. versionadded:: NX7.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportCollection`
    """
    VisualReportExplorer: VisualReportExplorer = ...
    """
    Returns the :py:class:`NXOpen.VisualReporting.VisualReportExplorer` belonging to this visual report manager 
    
    Signature ``VisualReportExplorer`` 
    
    .. versionadded:: NX7.5.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.VisualReportExplorer`
    """


class Rule(NXOpen.NXObject):
    """
    A rule within a :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    .. versionadded:: NX7.0.0
    """
    
    def GetClassifiers(self) -> 'list[Classifier]':
        """
        Returns the :py:class:`NXOpen.VisualReporting.Classifier`s associated with this :py:class:`NXOpen.VisualReporting.Rule`.  
        
        Signature ``GetClassifiers()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.VisualReporting.Classifier` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetIsSmartGroupDateEnabled(self, classifier: Classifier) -> bool:
        """
        The :py:class:`NXOpen.VisualReporting.ClassifierDateGroupMethodOption` in this :py:class:`NXOpen.VisualReporting.Classifier` 
        in the :py:class:`NXOpen.VisualReporting.Rule` will be determined by the overall date range of all reported objects.  
        
        For example, if the date range spans over 18 monthes, group by year will be used, otherwise if it is over 3 months, group by month will be used.
        If the date range is small, within 2 weeks, group by day will be used. 
        
        Only valid for a :py:class:`NXOpen.VisualReporting.Classifier` whose :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption`
        is :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption.Automatic <NXOpen.VisualReporting.ClassifierGroupingMethodOption>` or
        :py:class:`NXOpen.VisualReporting.ClassifierGroupingMethodOption.SemiAutomatic <NXOpen.VisualReporting.ClassifierGroupingMethodOption>` and the
        :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` on the :py:class:`NXOpen.VisualReporting.Property`
        is :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption.Date <NXOpen.VisualReporting.PropertyDatatypeOption>`.
        
        Signature ``GetIsSmartGroupDateEnabled(classifier)`` 
        
        :param classifier: 
        :type classifier: :py:class:`NXOpen.VisualReporting.Classifier` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetIsSmartGroupDateEnabled(self, classifier: Classifier, isSmartGroupDateEnabled: bool) -> None:
        """
        The :py:class:`NXOpen.VisualReporting.ClassifierDateGroupMethodOption` in this :py:class:`NXOpen.VisualReporting.Classifier` 
        in the :py:class:`NXOpen.VisualReporting.Rule` will be determined by the overall date range of all reported objects.  
        
        Signature ``SetIsSmartGroupDateEnabled(classifier, isSmartGroupDateEnabled)`` 
        
        :param classifier: 
        :type classifier: :py:class:`NXOpen.VisualReporting.Classifier` 
        :param isSmartGroupDateEnabled: 
        :type isSmartGroupDateEnabled: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_visual_reporting ("Visual Reporting")
        """
        ...
    
    ActiveClassifier: Classifier = ...
    """
    Returns or sets  the active :py:class:`NXOpen.VisualReporting.Classifier` in this :py:class:`NXOpen.VisualReporting.Rule`
    for a multiple properties report.  
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveClassifier`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.Classifier` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveClassifier`` 
    
    :param activeClassifier: 
    :type activeClassifier: :py:class:`NXOpen.VisualReporting.Classifier` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    FilterCondition: Condition = ...
    """
    Returns or sets  the filter :py:class:`NXOpen.VisualReporting.Condition` from this :py:class:`NXOpen.VisualReporting.Rule`.  
    
    <hr>
    
    Getter Method
    
    Signature ``FilterCondition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.Condition` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FilterCondition`` 
    
    :param filterCondition: 
    :type filterCondition: :py:class:`NXOpen.VisualReporting.Condition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    Null: Rule = ...  # unknown typename


class PropertyTypeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PropertyTypeOption():
    """
    Represents the possible :py:meth:`NXOpen.VisualReporting.Property.PropertyType` options
    for a property
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ArrangementSpecificPositionProperty", "Arrangement specific positioning"
       "AttributeProperty", "Part attribute property"
       "ComponentGroupProperty", "Component group name"
       "ComponentNameProperty", "Component name"
       "DescriptivePartNameProperty", "Descriptive part name"
       "LoadStateProperty", "The load state of the component"
       "MassKgProperty", "The mass of the component in pounds"
       "MassLbProperty", "The mass of the component in kilograms"
       "ModifiedProperty", "Whether the component is modified"
       "MultiCadProperty", "Parts mastered in a CAD system other than NX"
       "PartNameProperty", "Part name"
       "PartUnitsProperty", "Part units"
       "PiecePartProperty", "Piece part"
       "PositionProperty", "The position of the component"
       "PositionControlProperty", "The position control of the component"
       "ReadOnlyProperty", "Whether the component is read-only"
       "ReferenceSetProperty", "The reference set used by the component"
       "RootPartProperty", "Root part occurrence"
       "SuppressionControlProperty", "The suppression control of the component"
       "WeightStatusProperty", "The weight status of the component"
       "TeamcenterProperty", "Teamcenter property"
       "ServerProperty", "Server Property defined in server side report"
       "DegreesOfFreedomProperty", "The freedom degree of the component"
       "RuleEvaluationResultProperty", "Rule Evaluation for results in part"
       "CheckMateResultProperty", "Check-Mate result"
       "LastModifiedDateProperty", "last modify date property"
       "RequirementsValidationStatusProperty", "Requirement validate result"
       "RepresentationProperty", "Representation Status"
       "LastModifiedUserProperty", "last modify user property"
       "ComponentProperty", "Assembly Navigator column property"
       "MassGmProperty", "The mass of the component in grams"
       "PartFamilyMemberProperty", "Part family member"
       "LinkedPartProperty", "Linked part"
       "ProductTemplateProperty", "Product Template"
       "BodyDensityProperty", "Body density property"
       "BodyMassProperty", "Body mass property"
       "BodyRadiusGyrationProperty", "Body radius gyration property"
       "BodySurfaceAreaProperty", "Body surface area property"
       "BodyTypeProperty", "Body type property"
       "BodyVolumeProperty", "Body volume property"
       "BodyWeightProperty", "Body weight property"
       "FaceAreaProperty", "Face area property"
       "FaceTypeProperty", "Face type property"
       "FaceMinRadiusProperty", "Face minimum radius property"
       "FacePerimeterProperty", "Face perimeter property"
       "FacePMIFCFProperty", "Face PMI FCF property"
       "FacePMIFCFCharacteristicsProperty", "Face PMI FCF characteristics property"
       "FacePMIFCFCharFormTolProperty", "Face PMI FCF form characteristics property"
       "FacePMIFCFCharLocationTolProperty", "Face PMI FCF location characteristics property"
       "FacePMIFCFCharOrientationTolProperty", "Face PMI FCF orientation characteristics property"
       "FacePMIFCFCharProfileTolProperty", "Face PMI FCF profile characteristics property"
       "FacePMIFCFCharRunoutTolProperty", "Face PMI FCF run out characteristics property"
       "FacePMIDatumFeatureProperty", "Face PMI datum feature property"
       "FacePMIDatumTargetProperty", "Face PMI datum target property"
       "ObjectAttributeProperty", "Subpart object attribute property"
       "ObjectCreatedByUserProperty", "Subpart object created by user property"
       "ObjectCreatedDateProperty", "Subpart object created date property"
       "ObjectCreatedVersionProperty", "Subpart object created version property"
       "ObjectRefByWaveLinkProperty", "Subpart object referenced by Wave link property"
       "ObjectWaveLinkedProperty", "Subpart object Wave linked property"
       "ObjectModifiedByUserProperty", "Subpart object modified by user property"
       "ObjectModifiedDateProperty", "Subpart object modified date property"
       "ObjectModifiedVersionProperty", "Subpart object modified version property"
       "PartitionMembershipProperty", "Partition Membership property"
       "ComponentAddedDateProperty", "Component Added Date"
       "TeamcenterObjectProperty", "Teamcenter Object property"
       "ComponentPatternTypeProperty", "Component Pattern Type property"
       "ObjectNameProperty", "Subpart object name property"
       "NXOpenProperty", "NX Open property"
       "SheetMetalBendAngleProperty", "Sheet Metal Bend Angle Property"
       "SheetMetalBendRadiusProperty", "Sheet Metal Bend Radius Property"
       "SheetMetalFaceTypeAllProperty", "Sheet Metal All Face Type Property"
       "SheetMetalFaceTypeBendProperty", "Sheet Metal Bend Face Type Property"
       "SheetMetalFaceTypeDeformProperty", "Sheet Metal Deform Face Type Property"
       "SheetMetalFaceTypeWebProperty", "Sheet Metal Web Face Type Property"
       "SheetMetalNeutralFactorProperty", "Sheet Metal Neutral Factor Property"
       "SheetMetalBodyTypeProperty", "Sheet Metal Body Type Property"
       "FeatureFailureProperty", "Feature failure component property"
    """
    ArrangementSpecificPositionProperty = 0  # PropertyTypeOptionMemberType
    AttributeProperty = 1  # PropertyTypeOptionMemberType
    ComponentGroupProperty = 2  # PropertyTypeOptionMemberType
    ComponentNameProperty = 3  # PropertyTypeOptionMemberType
    DescriptivePartNameProperty = 4  # PropertyTypeOptionMemberType
    LoadStateProperty = 5  # PropertyTypeOptionMemberType
    MassKgProperty = 6  # PropertyTypeOptionMemberType
    MassLbProperty = 7  # PropertyTypeOptionMemberType
    ModifiedProperty = 8  # PropertyTypeOptionMemberType
    MultiCadProperty = 9  # PropertyTypeOptionMemberType
    PartNameProperty = 10  # PropertyTypeOptionMemberType
    PartUnitsProperty = 11  # PropertyTypeOptionMemberType
    PiecePartProperty = 12  # PropertyTypeOptionMemberType
    PositionProperty = 13  # PropertyTypeOptionMemberType
    PositionControlProperty = 14  # PropertyTypeOptionMemberType
    ReadOnlyProperty = 15  # PropertyTypeOptionMemberType
    ReferenceSetProperty = 16  # PropertyTypeOptionMemberType
    RootPartProperty = 17  # PropertyTypeOptionMemberType
    SuppressionControlProperty = 18  # PropertyTypeOptionMemberType
    WeightStatusProperty = 19  # PropertyTypeOptionMemberType
    TeamcenterProperty = 20  # PropertyTypeOptionMemberType
    ServerProperty = 21  # PropertyTypeOptionMemberType
    DegreesOfFreedomProperty = 22  # PropertyTypeOptionMemberType
    RuleEvaluationResultProperty = 23  # PropertyTypeOptionMemberType
    CheckMateResultProperty = 24  # PropertyTypeOptionMemberType
    LastModifiedDateProperty = 25  # PropertyTypeOptionMemberType
    RequirementsValidationStatusProperty = 26  # PropertyTypeOptionMemberType
    RepresentationProperty = 27  # PropertyTypeOptionMemberType
    LastModifiedUserProperty = 28  # PropertyTypeOptionMemberType
    ComponentProperty = 29  # PropertyTypeOptionMemberType
    MassGmProperty = 30  # PropertyTypeOptionMemberType
    PartFamilyMemberProperty = 31  # PropertyTypeOptionMemberType
    LinkedPartProperty = 32  # PropertyTypeOptionMemberType
    ProductTemplateProperty = 33  # PropertyTypeOptionMemberType
    BodyDensityProperty = 34  # PropertyTypeOptionMemberType
    BodyMassProperty = 35  # PropertyTypeOptionMemberType
    BodyRadiusGyrationProperty = 36  # PropertyTypeOptionMemberType
    BodySurfaceAreaProperty = 37  # PropertyTypeOptionMemberType
    BodyTypeProperty = 38  # PropertyTypeOptionMemberType
    BodyVolumeProperty = 39  # PropertyTypeOptionMemberType
    BodyWeightProperty = 40  # PropertyTypeOptionMemberType
    FaceAreaProperty = 41  # PropertyTypeOptionMemberType
    FaceTypeProperty = 42  # PropertyTypeOptionMemberType
    FaceMinRadiusProperty = 43  # PropertyTypeOptionMemberType
    FacePerimeterProperty = 44  # PropertyTypeOptionMemberType
    FacePMIFCFProperty = 45  # PropertyTypeOptionMemberType
    FacePMIFCFCharacteristicsProperty = 46  # PropertyTypeOptionMemberType
    FacePMIFCFCharFormTolProperty = 47  # PropertyTypeOptionMemberType
    FacePMIFCFCharLocationTolProperty = 48  # PropertyTypeOptionMemberType
    FacePMIFCFCharOrientationTolProperty = 49  # PropertyTypeOptionMemberType
    FacePMIFCFCharProfileTolProperty = 50  # PropertyTypeOptionMemberType
    FacePMIFCFCharRunoutTolProperty = 51  # PropertyTypeOptionMemberType
    FacePMIDatumFeatureProperty = 52  # PropertyTypeOptionMemberType
    FacePMIDatumTargetProperty = 53  # PropertyTypeOptionMemberType
    ObjectAttributeProperty = 54  # PropertyTypeOptionMemberType
    ObjectCreatedByUserProperty = 55  # PropertyTypeOptionMemberType
    ObjectCreatedDateProperty = 56  # PropertyTypeOptionMemberType
    ObjectCreatedVersionProperty = 57  # PropertyTypeOptionMemberType
    ObjectRefByWaveLinkProperty = 58  # PropertyTypeOptionMemberType
    ObjectWaveLinkedProperty = 59  # PropertyTypeOptionMemberType
    ObjectModifiedByUserProperty = 60  # PropertyTypeOptionMemberType
    ObjectModifiedDateProperty = 61  # PropertyTypeOptionMemberType
    ObjectModifiedVersionProperty = 62  # PropertyTypeOptionMemberType
    PartitionMembershipProperty = 63  # PropertyTypeOptionMemberType
    ComponentAddedDateProperty = 64  # PropertyTypeOptionMemberType
    TeamcenterObjectProperty = 65  # PropertyTypeOptionMemberType
    ComponentPatternTypeProperty = 66  # PropertyTypeOptionMemberType
    ObjectNameProperty = 67  # PropertyTypeOptionMemberType
    NXOpenProperty = 68  # PropertyTypeOptionMemberType
    SheetMetalBendAngleProperty = 69  # PropertyTypeOptionMemberType
    SheetMetalBendRadiusProperty = 70  # PropertyTypeOptionMemberType
    SheetMetalFaceTypeAllProperty = 71  # PropertyTypeOptionMemberType
    SheetMetalFaceTypeBendProperty = 72  # PropertyTypeOptionMemberType
    SheetMetalFaceTypeDeformProperty = 73  # PropertyTypeOptionMemberType
    SheetMetalFaceTypeWebProperty = 74  # PropertyTypeOptionMemberType
    SheetMetalNeutralFactorProperty = 75  # PropertyTypeOptionMemberType
    SheetMetalBodyTypeProperty = 76  # PropertyTypeOptionMemberType
    FeatureFailureProperty = 77  # PropertyTypeOptionMemberType
    
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
    


class PropertyDatatypeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PropertyDatatypeOption():
    """
    Represents the possible :py:meth:`NXOpen.VisualReporting.Property.SystemDatatype` options
    for a property.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "String", "String data type"
       "Integer", "Integer data type"
       "Real", "Floating point data type"
       "Boolean", "Boolean data type"
       "Unknown", "The data type is unknown"
       "Null", "Null data type"
       "Date", "Date data type"
    """
    String = 0  # PropertyDatatypeOptionMemberType
    Integer = 1  # PropertyDatatypeOptionMemberType
    Real = 2  # PropertyDatatypeOptionMemberType
    Boolean = 3  # PropertyDatatypeOptionMemberType
    Unknown = 4  # PropertyDatatypeOptionMemberType
    Null = 5  # PropertyDatatypeOptionMemberType
    Date = 6  # PropertyDatatypeOptionMemberType
    
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
    


class Property(NXOpen.NXObject):
    """
    A property within either a :py:class:`NXOpen.VisualReporting.Rule` or a
    :py:class:`NXOpen.VisualReporting.Condition`, or used as referenced property 
    information for the report.  
    
    .. versionadded:: NX7.0.0
    """
    
    class TypeOption():
        """
        Represents the possible :py:meth:`NXOpen.VisualReporting.Property.PropertyType` options
        for a property
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ArrangementSpecificPositionProperty", "Arrangement specific positioning"
           "AttributeProperty", "Part attribute property"
           "ComponentGroupProperty", "Component group name"
           "ComponentNameProperty", "Component name"
           "DescriptivePartNameProperty", "Descriptive part name"
           "LoadStateProperty", "The load state of the component"
           "MassKgProperty", "The mass of the component in pounds"
           "MassLbProperty", "The mass of the component in kilograms"
           "ModifiedProperty", "Whether the component is modified"
           "MultiCadProperty", "Parts mastered in a CAD system other than NX"
           "PartNameProperty", "Part name"
           "PartUnitsProperty", "Part units"
           "PiecePartProperty", "Piece part"
           "PositionProperty", "The position of the component"
           "PositionControlProperty", "The position control of the component"
           "ReadOnlyProperty", "Whether the component is read-only"
           "ReferenceSetProperty", "The reference set used by the component"
           "RootPartProperty", "Root part occurrence"
           "SuppressionControlProperty", "The suppression control of the component"
           "WeightStatusProperty", "The weight status of the component"
           "TeamcenterProperty", "Teamcenter property"
           "ServerProperty", "Server Property defined in server side report"
           "DegreesOfFreedomProperty", "The freedom degree of the component"
           "RuleEvaluationResultProperty", "Rule Evaluation for results in part"
           "CheckMateResultProperty", "Check-Mate result"
           "LastModifiedDateProperty", "last modify date property"
           "RequirementsValidationStatusProperty", "Requirement validate result"
           "RepresentationProperty", "Representation Status"
           "LastModifiedUserProperty", "last modify user property"
           "ComponentProperty", "Assembly Navigator column property"
           "MassGmProperty", "The mass of the component in grams"
           "PartFamilyMemberProperty", "Part family member"
           "LinkedPartProperty", "Linked part"
           "ProductTemplateProperty", "Product Template"
           "BodyDensityProperty", "Body density property"
           "BodyMassProperty", "Body mass property"
           "BodyRadiusGyrationProperty", "Body radius gyration property"
           "BodySurfaceAreaProperty", "Body surface area property"
           "BodyTypeProperty", "Body type property"
           "BodyVolumeProperty", "Body volume property"
           "BodyWeightProperty", "Body weight property"
           "FaceAreaProperty", "Face area property"
           "FaceTypeProperty", "Face type property"
           "FaceMinRadiusProperty", "Face minimum radius property"
           "FacePerimeterProperty", "Face perimeter property"
           "FacePMIFCFProperty", "Face PMI FCF property"
           "FacePMIFCFCharacteristicsProperty", "Face PMI FCF characteristics property"
           "FacePMIFCFCharFormTolProperty", "Face PMI FCF form characteristics property"
           "FacePMIFCFCharLocationTolProperty", "Face PMI FCF location characteristics property"
           "FacePMIFCFCharOrientationTolProperty", "Face PMI FCF orientation characteristics property"
           "FacePMIFCFCharProfileTolProperty", "Face PMI FCF profile characteristics property"
           "FacePMIFCFCharRunoutTolProperty", "Face PMI FCF run out characteristics property"
           "FacePMIDatumFeatureProperty", "Face PMI datum feature property"
           "FacePMIDatumTargetProperty", "Face PMI datum target property"
           "ObjectAttributeProperty", "Subpart object attribute property"
           "ObjectCreatedByUserProperty", "Subpart object created by user property"
           "ObjectCreatedDateProperty", "Subpart object created date property"
           "ObjectCreatedVersionProperty", "Subpart object created version property"
           "ObjectRefByWaveLinkProperty", "Subpart object referenced by Wave link property"
           "ObjectWaveLinkedProperty", "Subpart object Wave linked property"
           "ObjectModifiedByUserProperty", "Subpart object modified by user property"
           "ObjectModifiedDateProperty", "Subpart object modified date property"
           "ObjectModifiedVersionProperty", "Subpart object modified version property"
           "PartitionMembershipProperty", "Partition Membership property"
           "ComponentAddedDateProperty", "Component Added Date"
           "TeamcenterObjectProperty", "Teamcenter Object property"
           "ComponentPatternTypeProperty", "Component Pattern Type property"
           "ObjectNameProperty", "Subpart object name property"
           "NXOpenProperty", "NX Open property"
           "SheetMetalBendAngleProperty", "Sheet Metal Bend Angle Property"
           "SheetMetalBendRadiusProperty", "Sheet Metal Bend Radius Property"
           "SheetMetalFaceTypeAllProperty", "Sheet Metal All Face Type Property"
           "SheetMetalFaceTypeBendProperty", "Sheet Metal Bend Face Type Property"
           "SheetMetalFaceTypeDeformProperty", "Sheet Metal Deform Face Type Property"
           "SheetMetalFaceTypeWebProperty", "Sheet Metal Web Face Type Property"
           "SheetMetalNeutralFactorProperty", "Sheet Metal Neutral Factor Property"
           "SheetMetalBodyTypeProperty", "Sheet Metal Body Type Property"
           "FeatureFailureProperty", "Feature failure component property"
        """
        ArrangementSpecificPositionProperty = 0  # PropertyTypeOptionMemberType
        AttributeProperty = 1  # PropertyTypeOptionMemberType
        ComponentGroupProperty = 2  # PropertyTypeOptionMemberType
        ComponentNameProperty = 3  # PropertyTypeOptionMemberType
        DescriptivePartNameProperty = 4  # PropertyTypeOptionMemberType
        LoadStateProperty = 5  # PropertyTypeOptionMemberType
        MassKgProperty = 6  # PropertyTypeOptionMemberType
        MassLbProperty = 7  # PropertyTypeOptionMemberType
        ModifiedProperty = 8  # PropertyTypeOptionMemberType
        MultiCadProperty = 9  # PropertyTypeOptionMemberType
        PartNameProperty = 10  # PropertyTypeOptionMemberType
        PartUnitsProperty = 11  # PropertyTypeOptionMemberType
        PiecePartProperty = 12  # PropertyTypeOptionMemberType
        PositionProperty = 13  # PropertyTypeOptionMemberType
        PositionControlProperty = 14  # PropertyTypeOptionMemberType
        ReadOnlyProperty = 15  # PropertyTypeOptionMemberType
        ReferenceSetProperty = 16  # PropertyTypeOptionMemberType
        RootPartProperty = 17  # PropertyTypeOptionMemberType
        SuppressionControlProperty = 18  # PropertyTypeOptionMemberType
        WeightStatusProperty = 19  # PropertyTypeOptionMemberType
        TeamcenterProperty = 20  # PropertyTypeOptionMemberType
        ServerProperty = 21  # PropertyTypeOptionMemberType
        DegreesOfFreedomProperty = 22  # PropertyTypeOptionMemberType
        RuleEvaluationResultProperty = 23  # PropertyTypeOptionMemberType
        CheckMateResultProperty = 24  # PropertyTypeOptionMemberType
        LastModifiedDateProperty = 25  # PropertyTypeOptionMemberType
        RequirementsValidationStatusProperty = 26  # PropertyTypeOptionMemberType
        RepresentationProperty = 27  # PropertyTypeOptionMemberType
        LastModifiedUserProperty = 28  # PropertyTypeOptionMemberType
        ComponentProperty = 29  # PropertyTypeOptionMemberType
        MassGmProperty = 30  # PropertyTypeOptionMemberType
        PartFamilyMemberProperty = 31  # PropertyTypeOptionMemberType
        LinkedPartProperty = 32  # PropertyTypeOptionMemberType
        ProductTemplateProperty = 33  # PropertyTypeOptionMemberType
        BodyDensityProperty = 34  # PropertyTypeOptionMemberType
        BodyMassProperty = 35  # PropertyTypeOptionMemberType
        BodyRadiusGyrationProperty = 36  # PropertyTypeOptionMemberType
        BodySurfaceAreaProperty = 37  # PropertyTypeOptionMemberType
        BodyTypeProperty = 38  # PropertyTypeOptionMemberType
        BodyVolumeProperty = 39  # PropertyTypeOptionMemberType
        BodyWeightProperty = 40  # PropertyTypeOptionMemberType
        FaceAreaProperty = 41  # PropertyTypeOptionMemberType
        FaceTypeProperty = 42  # PropertyTypeOptionMemberType
        FaceMinRadiusProperty = 43  # PropertyTypeOptionMemberType
        FacePerimeterProperty = 44  # PropertyTypeOptionMemberType
        FacePMIFCFProperty = 45  # PropertyTypeOptionMemberType
        FacePMIFCFCharacteristicsProperty = 46  # PropertyTypeOptionMemberType
        FacePMIFCFCharFormTolProperty = 47  # PropertyTypeOptionMemberType
        FacePMIFCFCharLocationTolProperty = 48  # PropertyTypeOptionMemberType
        FacePMIFCFCharOrientationTolProperty = 49  # PropertyTypeOptionMemberType
        FacePMIFCFCharProfileTolProperty = 50  # PropertyTypeOptionMemberType
        FacePMIFCFCharRunoutTolProperty = 51  # PropertyTypeOptionMemberType
        FacePMIDatumFeatureProperty = 52  # PropertyTypeOptionMemberType
        FacePMIDatumTargetProperty = 53  # PropertyTypeOptionMemberType
        ObjectAttributeProperty = 54  # PropertyTypeOptionMemberType
        ObjectCreatedByUserProperty = 55  # PropertyTypeOptionMemberType
        ObjectCreatedDateProperty = 56  # PropertyTypeOptionMemberType
        ObjectCreatedVersionProperty = 57  # PropertyTypeOptionMemberType
        ObjectRefByWaveLinkProperty = 58  # PropertyTypeOptionMemberType
        ObjectWaveLinkedProperty = 59  # PropertyTypeOptionMemberType
        ObjectModifiedByUserProperty = 60  # PropertyTypeOptionMemberType
        ObjectModifiedDateProperty = 61  # PropertyTypeOptionMemberType
        ObjectModifiedVersionProperty = 62  # PropertyTypeOptionMemberType
        PartitionMembershipProperty = 63  # PropertyTypeOptionMemberType
        ComponentAddedDateProperty = 64  # PropertyTypeOptionMemberType
        TeamcenterObjectProperty = 65  # PropertyTypeOptionMemberType
        ComponentPatternTypeProperty = 66  # PropertyTypeOptionMemberType
        ObjectNameProperty = 67  # PropertyTypeOptionMemberType
        NXOpenProperty = 68  # PropertyTypeOptionMemberType
        SheetMetalBendAngleProperty = 69  # PropertyTypeOptionMemberType
        SheetMetalBendRadiusProperty = 70  # PropertyTypeOptionMemberType
        SheetMetalFaceTypeAllProperty = 71  # PropertyTypeOptionMemberType
        SheetMetalFaceTypeBendProperty = 72  # PropertyTypeOptionMemberType
        SheetMetalFaceTypeDeformProperty = 73  # PropertyTypeOptionMemberType
        SheetMetalFaceTypeWebProperty = 74  # PropertyTypeOptionMemberType
        SheetMetalNeutralFactorProperty = 75  # PropertyTypeOptionMemberType
        SheetMetalBodyTypeProperty = 76  # PropertyTypeOptionMemberType
        FeatureFailureProperty = 77  # PropertyTypeOptionMemberType
        
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
        
    
    
    class DatatypeOption():
        """
        Represents the possible :py:meth:`NXOpen.VisualReporting.Property.SystemDatatype` options
        for a property.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "String", "String data type"
           "Integer", "Integer data type"
           "Real", "Floating point data type"
           "Boolean", "Boolean data type"
           "Unknown", "The data type is unknown"
           "Null", "Null data type"
           "Date", "Date data type"
        """
        String = 0  # PropertyDatatypeOptionMemberType
        Integer = 1  # PropertyDatatypeOptionMemberType
        Real = 2  # PropertyDatatypeOptionMemberType
        Boolean = 3  # PropertyDatatypeOptionMemberType
        Unknown = 4  # PropertyDatatypeOptionMemberType
        Null = 5  # PropertyDatatypeOptionMemberType
        Date = 6  # PropertyDatatypeOptionMemberType
        
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
        
    
    BitmapName: str = ...
    """
    Returns or sets  the bitmap name of this property.  
    
    <hr>
    
    Getter Method
    
    Signature ``BitmapName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BitmapName`` 
    
    :param bitmapName: 
    :type bitmapName: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    CustomMessage: str = ...
    """
    Returns or sets  the custom message of this property.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomMessage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomMessage`` 
    
    :param customMessage: 
    :type customMessage: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    PropertyType: PropertyTypeOption = ...
    """
    Returns  the :py:class:`NXOpen.VisualReporting.PropertyTypeOption` of this :py:class:`NXOpen.VisualReporting.Property`.  
    
    Note that this :py:meth:`NXOpen.VisualReporting.Property.PropertyType` cannot be modified. 
    Instead it is specified when creating this :py:class:`NXOpen.VisualReporting.Property` by using the appropriate function:
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateProperty`
    
    <hr>
    
    Getter Method
    
    Signature ``PropertyType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.PropertyTypeOption` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    SystemDatatype: PropertyDatatypeOption = ...
    """
    Returns  the preferred :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` that should be used for the
    owning :py:class:`NXOpen.VisualReporting.Condition` or :py:class:`NXOpen.VisualReporting.Classifier`.  
    
    This function will return a data type of 
    :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption.Unknown <NXOpen.VisualReporting.PropertyDatatypeOption>`
    for properties whose :py:meth:`NXOpen.VisualReporting.Property.PropertyType` is
    :py:class:`NXOpen.VisualReporting.PropertyTypeOption.TeamcenterProperty <NXOpen.VisualReporting.PropertyTypeOption>`, 
    :py:class:`NXOpen.VisualReporting.PropertyTypeOption.ServerProperty <NXOpen.VisualReporting.PropertyTypeOption>`, 
    or :py:class:`NXOpen.VisualReporting.PropertyTypeOption.AttributeProperty <NXOpen.VisualReporting.PropertyTypeOption>`
    where the preferred data type cannot be determined.
    
    Note that this :py:meth:`NXOpen.VisualReporting.Property.SystemDatatype` cannot be modified. 
    Instead it is determined when creating this :py:class:`NXOpen.VisualReporting.Property` by using the appropriate function:
    - :py:meth:`NXOpen.VisualReporting.VisualReportBuilder.CreateProperty`
    
    <hr>
    
    Getter Method
    
    Signature ``SystemDatatype`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.PropertyDatatypeOption` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Null: Property = ...  # unknown typename


class GroupLabelDisplayStyleOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GroupLabelDisplayStyleOption():
    """
    Represents the possible display style options
    for a :py:class:`NXOpen.VisualReporting.GroupLabel`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DeEmphasis", "Matching objects will be de-emphasized"
       "SpecifiedColor", "Matching objects will be shown using :py:meth:`NXOpen.VisualReporting.GroupLabel.Color`"
       "OriginalColor", "Matching objects will be shown using their original color"
       "AutomaticColor", "Matching objects will be shown using :py:meth:`NXOpen.VisualReporting.GroupLabel.Color` which is system determined"
    """
    DeEmphasis = 0  # GroupLabelDisplayStyleOptionMemberType
    SpecifiedColor = 1  # GroupLabelDisplayStyleOptionMemberType
    OriginalColor = 2  # GroupLabelDisplayStyleOptionMemberType
    AutomaticColor = 3  # GroupLabelDisplayStyleOptionMemberType
    
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
    


class GroupLabelTagPriorityOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GroupLabelTagPriorityOption():
    """
    Represents the possible priority options
    for a :py:class:`NXOpen.VisualReporting.GroupLabel`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Low", "Low priority"
       "Medium", "Medium priority"
       "High", "Hign priority"
    """
    Low = 0  # GroupLabelTagPriorityOptionMemberType
    Medium = 1  # GroupLabelTagPriorityOptionMemberType
    High = 2  # GroupLabelTagPriorityOptionMemberType
    
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
    


class GroupLabel(NXOpen.NXObject):
    """
    A group label corresponds to a group of objects in the results of an applied 
    :py:class:`NXOpen.VisualReporting.VisualReport`.  
    
    .. versionadded:: NX7.0.0
    """
    
    class DisplayStyleOption():
        """
        Represents the possible display style options
        for a :py:class:`NXOpen.VisualReporting.GroupLabel`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DeEmphasis", "Matching objects will be de-emphasized"
           "SpecifiedColor", "Matching objects will be shown using :py:meth:`NXOpen.VisualReporting.GroupLabel.Color`"
           "OriginalColor", "Matching objects will be shown using their original color"
           "AutomaticColor", "Matching objects will be shown using :py:meth:`NXOpen.VisualReporting.GroupLabel.Color` which is system determined"
        """
        DeEmphasis = 0  # GroupLabelDisplayStyleOptionMemberType
        SpecifiedColor = 1  # GroupLabelDisplayStyleOptionMemberType
        OriginalColor = 2  # GroupLabelDisplayStyleOptionMemberType
        AutomaticColor = 3  # GroupLabelDisplayStyleOptionMemberType
        
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
        
    
    
    class TagPriorityOption():
        """
        Represents the possible priority options
        for a :py:class:`NXOpen.VisualReporting.GroupLabel`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Low", "Low priority"
           "Medium", "Medium priority"
           "High", "Hign priority"
        """
        Low = 0  # GroupLabelTagPriorityOptionMemberType
        Medium = 1  # GroupLabelTagPriorityOptionMemberType
        High = 2  # GroupLabelTagPriorityOptionMemberType
        
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
        
    
    BitmapName: str = ...
    """
    Returns or sets  the bitmap name of this :py:class:`NXOpen.VisualReporting.GroupLabel`.  
    
    <hr>
    
    Getter Method
    
    Signature ``BitmapName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BitmapName`` 
    
    :param bitmapName: 
    :type bitmapName: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    Color: NXOpen.NXColorRgb_Struct = ...
    """
    Returns or sets  the color of the :py:class:`NXOpen.VisualReporting.GroupLabel` 
    
    <hr>
    
    Getter Method
    
    Signature ``Color`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXColorRgb_Struct` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Color`` 
    
    :param color: 
    :type color: :py:class:`NXOpen.NXColorRgb_Struct` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    CustomMessage: str = ...
    """
    Returns or sets  the custom message of this :py:class:`NXOpen.VisualReporting.GroupLabel`.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomMessage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomMessage`` 
    
    :param customMessage: 
    :type customMessage: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    DisplayStyle: GroupLabelDisplayStyleOption = ...
    """
    Returns or sets  the :py:class:`NXOpen.VisualReporting.GroupLabelDisplayStyleOption` of the :py:class:`NXOpen.VisualReporting.GroupLabel` 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.GroupLabelDisplayStyleOption` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayStyle`` 
    
    :param displayStyle: 
    :type displayStyle: :py:class:`NXOpen.VisualReporting.GroupLabelDisplayStyleOption` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    ErrorLevel: NXOpen.ValidationResult = ...
    """
    Returns or sets  the Error Level of this :py:class:`NXOpen.VisualReporting.GroupLabel`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ErrorLevel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ValidationResult` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ErrorLevel`` 
    
    :param errorLevel: 
    :type errorLevel: :py:class:`NXOpen.ValidationResult` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    IsManual: bool = ...
    """
    Returns or sets  whether the :py:class:`NXOpen.VisualReporting.GroupLabel` is manual.  
    
    It is manual if it either has a user-specified
    :py:meth:`NXOpen.NXObject.Name` or if its :py:meth:`NXOpen.VisualReporting.GroupLabel.DisplayStyle` is
    not :py:class:`NXOpen.VisualReporting.GroupLabelDisplayStyleOption.AutomaticColor <NXOpen.VisualReporting.GroupLabelDisplayStyleOption>`.
    You can change a :py:class:`NXOpen.VisualReporting.GroupLabel` from automatic to manual, but you cannot 
    change :py:class:`NXOpen.VisualReporting.GroupLabel` from manual to automatic.
    
    <hr>
    
    Getter Method
    
    Signature ``IsManual`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsManual`` 
    
    :param isManual: 
    :type isManual: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    IsNameUserSpecified: bool = ...
    """
    Returns or sets  whether the :py:class:`NXOpen.VisualReporting.GroupLabel` has a user-specified :py:meth:`NXOpen.NXObject.Name`.  
    
    If it isn't
    user-specified, then the system will generate its name automatically.
    
    <hr>
    
    Getter Method
    
    Signature ``IsNameUserSpecified`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsNameUserSpecified`` 
    
    :param isNameUserSpecified: 
    :type isNameUserSpecified: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    LowerBound: str = ...
    """
    Returns or sets  the lower bound value of the :py:class:`NXOpen.VisualReporting.GroupLabel` (if it is being grouped by range) 
    
    <hr>
    
    Getter Method
    
    Signature ``LowerBound`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LowerBound`` 
    
    :param fromValue: 
    :type fromValue: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    TagPriority: GroupLabelTagPriorityOption = ...
    """
    Returns or sets  the Tag Priority of this :py:class:`NXOpen.VisualReporting.GroupLabel`.  
    
    <hr>
    
    Getter Method
    
    Signature ``TagPriority`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.VisualReporting.GroupLabelTagPriorityOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TagPriority`` 
    
    :param tagPriority: 
    :type tagPriority: :py:class:`NXOpen.VisualReporting.GroupLabelTagPriorityOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    UpperBound: str = ...
    """
    Returns or sets  the upper bound value of the :py:class:`NXOpen.VisualReporting.GroupLabel` (if it is being grouped by range) 
    
    <hr>
    
    Getter Method
    
    Signature ``UpperBound`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UpperBound`` 
    
    :param upperBound: 
    :type upperBound: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    Value: str = ...
    """
    Returns or sets  the value of the :py:class:`NXOpen.VisualReporting.GroupLabel` (if it is being grouped by value) 
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param groupLabelValue: 
    :type groupLabelValue: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_visual_reporting ("Visual Reporting")
    """
    Null: GroupLabel = ...  # unknown typename


