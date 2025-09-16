# module 'NXOpen.CAE.AeroStructures'
#
# Automatically generated 2025-06-09T14:38:44.605509
#

import typing

import NXOpen
import NXOpen.Annotations
import NXOpen.CAE
import NXOpen.Report



class LoadCaseCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of AeroStruct LoadCases   
    
    Use :py:meth:`CAE.AeroStructures.MarginSolution.LoadCaseCollection` to get the instance of this class.
    
    .. versionadded:: NX12.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, name: str) -> LoadCase:
        """
        Finds the :py:class:`NXOpen.CAE.AeroStructures.LoadCase` object with the given name.  
        
        Signature ``FindObject(name)`` 
        
        :param name:  Name of the LocalDefinition   
        :type name: str 
        :returns:  :py:class:`NXOpen.CAE.AeroStructures.LoadCase` object with this name.  
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.LoadCase` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CreateLoadCaseListBuilder(self) -> LoadCaseListBuilder:
        """
        Creates a :py:class:`NXOpen.CAE.AeroStructures.LoadCaseListBuilder`  
        
        Signature ``CreateLoadCaseListBuilder()`` 
        
        :returns:   Builder object 
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseListBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def DeleteLoadcase(self, loadcase: LoadCase) -> None:
        """
        Delete a AeroStruct loadcase.  
        
        Signature ``DeleteLoadcase(loadcase)`` 
        
        :param loadcase:  :py:class:`NXOpen.CAE.AeroStructures.LoadCase`  
        :type loadcase: :py:class:`NXOpen.CAE.AeroStructures.LoadCase` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    


class LoadCaseSet(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet`.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSetBuilder`
    
    .. versionadded:: NX12.0.0
    """
    Null: LoadCaseSet = ...  # unknown typename


class MarginResultTableDataProviderColumnTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MarginResultTableDataProviderColumnType():
    """
    Column type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Calculation", " - "
       "FailureMode", " - "
       "LoadCase", " - "
       "MarginOfSafety", " - "
       "GlobalRank", " - "
       "RankByCalculation", " - "
       "RankByFailureMode", " - "
       "RankByLoadCase", " - "
    """
    Calculation = 0  # MarginResultTableDataProviderColumnTypeMemberType
    FailureMode = 1  # MarginResultTableDataProviderColumnTypeMemberType
    LoadCase = 2  # MarginResultTableDataProviderColumnTypeMemberType
    MarginOfSafety = 3  # MarginResultTableDataProviderColumnTypeMemberType
    GlobalRank = 4  # MarginResultTableDataProviderColumnTypeMemberType
    RankByCalculation = 5  # MarginResultTableDataProviderColumnTypeMemberType
    RankByFailureMode = 6  # MarginResultTableDataProviderColumnTypeMemberType
    RankByLoadCase = 7  # MarginResultTableDataProviderColumnTypeMemberType
    
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
    


class MarginResultTableDataProvider(NXOpen.NXObject):
    """
    MarginResultTableDataProvider used by the global results editor
    provides a table view of the results of all of a subset of the calculation of a margin solution.
    The columns can be configured thru RegisterColumn method   
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.AeroStructures.MarginSolution.CreateMarginResultTableDataProvider`
    
    .. versionadded:: NX12.0.0
    """
    
    class ColumnType():
        """
        Column type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Calculation", " - "
           "FailureMode", " - "
           "LoadCase", " - "
           "MarginOfSafety", " - "
           "GlobalRank", " - "
           "RankByCalculation", " - "
           "RankByFailureMode", " - "
           "RankByLoadCase", " - "
        """
        Calculation = 0  # MarginResultTableDataProviderColumnTypeMemberType
        FailureMode = 1  # MarginResultTableDataProviderColumnTypeMemberType
        LoadCase = 2  # MarginResultTableDataProviderColumnTypeMemberType
        MarginOfSafety = 3  # MarginResultTableDataProviderColumnTypeMemberType
        GlobalRank = 4  # MarginResultTableDataProviderColumnTypeMemberType
        RankByCalculation = 5  # MarginResultTableDataProviderColumnTypeMemberType
        RankByFailureMode = 6  # MarginResultTableDataProviderColumnTypeMemberType
        RankByLoadCase = 7  # MarginResultTableDataProviderColumnTypeMemberType
        
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
        
    
    
    def RegisterColumn(self, columnIdx: int, columnType: MarginResultTableDataProviderColumnType) -> None:
        """
        Register a new column 
        
        Signature ``RegisterColumn(columnIdx, columnType)`` 
        
        :param columnIdx:  the column index, this must correspond to the number of currently registered column otherwise the method fails  
        :type columnIdx: int 
        :param columnType:  the registered column type  
        :type columnType: :py:class:`NXOpen.CAE.AeroStructures.MarginResultTableDataProviderColumnType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: MarginResultTableDataProvider = ...  # unknown typename


class MarginSolution(NXOpen.NXObject, NXOpen.Report.IReportCollection):
    """
    Represents a :py:class:`NXOpen.CAE.AeroStructures.MarginSolution`.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.AeroStructures.MarginSolutionBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    def Rename(self, name: str) -> None:
        """
        Renames the meta solution
        
        Signature ``Rename(name)`` 
        
        :param name: 
        :type name: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    @typing.overload
    def CreateMarginResultTableDataProvider(self) -> MarginResultTableDataProvider:
        """
        Creates a :py:class:`NXOpen.CAE.AeroStructures.MarginResultTableDataProvider` 
        the table provider will be based on every calculation of this solution that have results 
        
        Signature ``CreateMarginResultTableDataProvider()`` 
        
        :returns:   margin result table data provider object 
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.MarginResultTableDataProvider` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def CreateMarginResultTableDataProvider(self, marginCalculations: 'list[MarginCalculation]') -> MarginResultTableDataProvider:
        """
        Creates a :py:class:`NXOpen.CAE.AeroStructures.MarginResultTableDataProvider` 
        Only the subset of calculation given in argument are taken into account rather than all the calculation of the solution.
        Furthermore only the ones with results are taken into account  
        
        Signature ``CreateMarginResultTableDataProvider(marginCalculations)`` 
        
        :param marginCalculations:  The list of calculations from the solution to consider, only the ones with results are taken into account  
        :type marginCalculations: list of :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` 
        :returns:   margin result table data provider object 
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.MarginResultTableDataProvider` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CreateReport(self, templateFile: str, reportName: str, listError: bool) -> NXOpen.Report.Report:
        """
        Creates a :py:class:`Report.Report` in this report collection.  
        
        NX will not create a report if the report name is empty or existed.  
        
        Signature ``CreateReport(templateFile, reportName, listError)`` 
        
        :param templateFile:   Template file name with full path  
        :type templateFile: str 
        :param reportName:   Report name  
        :type reportName: str 
        :param listError:  list error information in listing window  
        :type listError: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.Report.Report` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetReports(self) -> 'list[NXOpen.Report.Report]':
        """
        Gets all reports in the report collection.  
        
        Signature ``GetReports()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Report.Report` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_design_sim ("NX Design Simulation")
        """
        ...
    
    LoadCaseSetCollection: LoadCaseSetCollection = ...
    """
    Returns the :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSetCollection` belonging to this 
    
    Signature ``LoadCaseSetCollection`` 
    
    .. versionadded:: NX12.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSetCollection`
    """
    LoadCaseCollection: LoadCaseCollection = ...
    """
    Returns the :py:class:`NXOpen.CAE.AeroStructures.LoadCaseCollection` belonging to this 
    
    Signature ``LoadCaseCollection`` 
    
    .. versionadded:: NX12.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseCollection`
    """
    MarginCalculationCollection: MarginCalculationCollection = ...
    """
    Returns the :py:class:`NXOpen.CAE.AeroStructures.MarginCalculationCollection` belonging to this 
    
    Signature ``MarginCalculationCollection`` 
    
    .. versionadded:: NX12.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.AeroStructures.MarginCalculationCollection`
    """
    Null: MarginSolution = ...  # unknown typename


class MarginCalculation(NXOpen.NXObject):
    """
    This is the MarginCalculation  
    
    .. versionadded:: NX12.0.0
    """
    Null: MarginCalculation = ...  # unknown typename


class MarginSolutionBuilder(NXOpen.Builder):
    """
    This is a manager to the :py:class:`CAE.AeroStructures.MarginSolution` class.  
    
    Object of type :py:class:`CAE.AeroStructures.MarginSolution` can be
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.AeroStructures.MarginSolutionCollection.CreateMarginSolutionBuilder`
    
    .. versionadded:: NX12.0.0
    """
    Description: str = ...
    """
    Returns or sets   a Get the metasolution description
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``Description`` 
    
    :param title: 
    :type title: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Name: str = ...
    """
    Returns or sets  the metasolution name
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param title: 
    :type title: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ReferenceSolution: NXOpen.CAE.SimSolution = ...
    """
    Returns or sets  the referenced FE-Solution of the AeroStructure solution 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SimSolution` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceSolution`` 
    
    :param referenceSolution: 
    :type referenceSolution: :py:class:`NXOpen.CAE.SimSolution` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: MarginSolutionBuilder = ...  # unknown typename


class MarginCalculationBuilderCalculationStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MarginCalculationBuilderCalculationStatus():
    """
    the Status type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotRun", "has not run"
       "Error", "error"
       "Success", "success"
    """
    NotRun = 0  # MarginCalculationBuilderCalculationStatusMemberType
    Error = 1  # MarginCalculationBuilderCalculationStatusMemberType
    Success = 2  # MarginCalculationBuilderCalculationStatusMemberType
    
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
    


class MarginCalculationBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` builder.  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    
    class CalculationStatus():
        """
        the Status type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotRun", "has not run"
           "Error", "error"
           "Success", "success"
        """
        NotRun = 0  # MarginCalculationBuilderCalculationStatusMemberType
        Error = 1  # MarginCalculationBuilderCalculationStatusMemberType
        Success = 2  # MarginCalculationBuilderCalculationStatusMemberType
        
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
        
    
    
    def GetLocationOrigin(self) -> NXOpen.Point3d:
        """
        Retrieve the location origin point 
        
        Signature ``GetLocationOrigin()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetLocationDirection(self) -> NXOpen.Matrix3x3:
        """
        Retrieve the location direction matrix 
        
        Signature ``GetLocationDirection()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Matrix3x3` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CreatePropertyTable(self) -> NXOpen.BasePropertyTable:
        """
        Creates a PropertyTable  
        
        Signature ``CreatePropertyTable()`` 
        
        :returns:  the property table 
        :rtype: :py:class:`NXOpen.BasePropertyTable` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Annotation: NXOpen.Annotations.NoteBase = ...
    """
    Returns or sets  the Annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``Annotation`` 
    
    :returns:  the annotation 
    :rtype: :py:class:`NXOpen.Annotations.NoteBase` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``Annotation`` 
    
    :param annotation:  the annotation 
    :type annotation: :py:class:`NXOpen.Annotations.NoteBase` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Description: str = ...
    """
    Returns or sets  the description.  
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``Description`` 
    
    :param description: 
    :type description: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Loadcaseset: LoadCaseSet = ...
    """
    Returns or sets  the LoadCaseSet used by the calculation
    
    <hr>
    
    Getter Method
    
    Signature ``Loadcaseset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``Loadcaseset`` 
    
    :param lcset: 
    :type lcset: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    LocationCoordinatesystem: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the calculation location with direction as a coordinate system.  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationCoordinatesystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``LocationCoordinatesystem`` 
    
    :param location: 
    :type location: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    LocationPoint: NXOpen.Point = ...
    """
    Returns or sets  the calculation location as a single point.  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``LocationPoint`` 
    
    :param location: 
    :type location: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Methodkey: str = ...
    """
    Returns or sets  the MethodKey 
    
    <hr>
    
    Getter Method
    
    Signature ``Methodkey`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``Methodkey`` 
    
    :param methodkey: 
    :type methodkey: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Name: str = ...
    """
    Returns or sets  the name.  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    PropertyTable: NXOpen.BasePropertyTable = ...
    """
    Returns  the Property Table 
    
    <hr>
    
    Getter Method
    
    Signature ``PropertyTable`` 
    
    :returns:  the property table 
    :rtype: :py:class:`NXOpen.BasePropertyTable` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Status: MarginCalculationBuilderCalculationStatus = ...
    """
    Returns or sets  the execution status
    
    <hr>
    
    Getter Method
    
    Signature ``Status`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.AeroStructures.MarginCalculationBuilderCalculationStatus` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``Status`` 
    
    :param cstatus: 
    :type cstatus: :py:class:`NXOpen.CAE.AeroStructures.MarginCalculationBuilderCalculationStatus` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: MarginCalculationBuilder = ...  # unknown typename


class MarginSolutionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of  margin solution.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.AeroStructManager`
    
    .. versionadded:: NX12.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, name: str) -> MarginSolution:
        """
        Finds a AeroStruct margin solution with a specified name.  
        
        Signature ``FindObject(name)`` 
        
        :param name:  name of the AeroStruct margin   
        :type name: str 
        :returns:  The AeroStruct margin solution  
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.MarginSolution` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CreateMarginSolutionBuilder(self, metasolution: MarginSolution) -> MarginSolutionBuilder:
        """
        Creates the builder object of AeroStruct meta solution.  
        
        Signature ``CreateMarginSolutionBuilder(metasolution)`` 
        
        :param metasolution: 
        :type metasolution: :py:class:`NXOpen.CAE.AeroStructures.MarginSolution` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.MarginSolutionBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def DeleteMarginSolution(self, metasolution: MarginSolution) -> None:
        """
        Delete a AeroStruct metasolution.  
        
        Signature ``DeleteMarginSolution(metasolution)`` 
        
        :param metasolution:  The AeroStruct margin_solution to be deleted  
        :type metasolution: :py:class:`NXOpen.CAE.AeroStructures.MarginSolution` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CloneMarginSolution(self, source: MarginSolution) -> MarginSolution:
        """
        Clones a AeroStruct marginsolution.  
        
        Signature ``CloneMarginSolution(source)`` 
        
        :param source:  Source metasolution  
        :type source: :py:class:`NXOpen.CAE.AeroStructures.MarginSolution` 
        :returns:  Cloned metasolution  
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.MarginSolution` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def SetActiveMarginsolution(self, source: MarginSolution) -> None:
        """
        Activates the marginsolution.  
        
        Signature ``SetActiveMarginsolution(source)`` 
        
        :param source:  The metasolution to activate 
        :type source: :py:class:`NXOpen.CAE.AeroStructures.MarginSolution` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    


class MarginCalculationCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of  :py:class:`CAE.AeroStructures.MarginCalculation`.  
    
    Use :py:meth:`CAE.AeroStructures.MarginCalculationCollection` to get the instance of this class.
    
    .. versionadded:: NX12.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, name: str) -> MarginCalculation:
        """
        Finds the :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` object with the given name.  
        
        Signature ``FindObject(name)`` 
        
        :param name:  Name of the MarginCalculation   
        :type name: str 
        :returns:  :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` object with this name.  
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CreateMarginCalculationBuilder(self, margincalculation: MarginCalculation) -> MarginCalculationBuilder:
        """
        Creates a :py:class:`CAE.AeroStructures.MarginCalculationBuilder`  
        
        Signature ``CreateMarginCalculationBuilder(margincalculation)`` 
        
        :param margincalculation: 
        :type margincalculation: :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` 
        :returns:  Builder object 
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.MarginCalculationBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def DeleteCalculation(self, margincalculation: MarginCalculation) -> None:
        """
        Removes the calculation from the solution 
        
        Signature ``DeleteCalculation(margincalculation)`` 
        
        :param margincalculation:  :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` to be deleted  
        :type margincalculation: :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CloneCalculation(self, name: str, sourcemargincalculation: MarginCalculation) -> MarginCalculation:
        """
        Makes a copy the calculation and add it to the margin solution, replaces the given name if it is a duplicate  
        
        Signature ``CloneCalculation(name, sourcemargincalculation)`` 
        
        :param name:  Tentative name of the cloned MarginCalculation, will be changed if not unique   
        :type name: str 
        :param sourcemargincalculation: Source  :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` to clone  
        :type sourcemargincalculation: :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` 
        :returns: The resulting cloned :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation`  
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.MarginCalculation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    


class LoadCase(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.CAE.AeroStructures.LoadCase`.  
    
    .. versionadded:: NX12.0.0
    """
    Null: LoadCase = ...  # unknown typename


class ManualLoadExtraction(NXOpen.NXObject):
    """
    This is the ManualLoadExtraction class  
    
    .. versionadded:: NX12.0.0
    """
    
    def SetValues(self, keys: 'list[str]', values: 'list[float]') -> None:
        """
        Set values 
        
        Signature ``SetValues(keys, values)`` 
        
        :param keys:  list of keys (loadcase names)  
        :type keys: list of str 
        :param values:  list of values  
        :type values: list of float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: ManualLoadExtraction = ...  # unknown typename


class LoadCaseSetCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of AeroStruct LoadCases   
    
    Use :py:meth:`CAE.AeroStructures.MarginSolution.LoadCaseSetCollection` to get the instance of this class.
    
    .. versionadded:: NX12.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, name: str) -> LoadCaseSet:
        """
        Finds the :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet` object with the given name.  
        
        Signature ``FindObject(name)`` 
        
        :param name:  LoadCaseSet Name   
        :type name: str 
        :returns:  :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet` object with this name.  
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CreateLoadCaseSetBuilder(self, loadcaeset: LoadCaseSet) -> LoadCaseSetBuilder:
        """
        Creates a :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSetBuilder`  
        
        Signature ``CreateLoadCaseSetBuilder(loadcaeset)`` 
        
        :param loadcaeset:  :py:class:`NXOpen.CAE.AeroStructures.LoadCase` to be edited  
        :type loadcaeset: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet` 
        :returns:  Builder object 
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSetBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def DeleteLoadCaseSet(self, loadcaseset: LoadCaseSet) -> None:
        """
        Delete a AeroStruct loadcase set.  
        
        Signature ``DeleteLoadCaseSet(loadcaseset)`` 
        
        :param loadcaseset:  :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet`  
        :type loadcaseset: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CreateLoadCaseSet(self, builder: LoadCaseSetBuilder) -> None:
        """
        Create a AeroStruct loadcase set.  
        
        Signature ``CreateLoadCaseSet(builder)`` 
        
        :param builder:  :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSetBuilder`  
        :type builder: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSetBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CloneLoadCaseSet(self, loadcaseset: LoadCaseSet) -> None:
        """
        Create a AeroStruct loadcase set.  
        
        Signature ``CloneLoadCaseSet(loadcaseset)`` 
        
        :param loadcaseset:  :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet`  
        :type loadcaseset: :py:class:`NXOpen.CAE.AeroStructures.LoadCaseSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    


class LoadCaseSetBuilder(NXOpen.Builder):
    """
    This is a manager to the :py:class:`CAE.AeroStructures.LoadCaseSet` class.  
    
    Object of type :py:class:`CAE.AeroStructures.LoadCaseSet` can be
    created and edited only through this class
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.AeroStructures.LoadCaseSetCollection.CreateLoadCaseSetBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    def AddLoadCase(self, loadcase: LoadCase) -> None:
        """
        Insert a loadcase to the load case set builder 
        
        Signature ``AddLoadCase(loadcase)`` 
        
        :param loadcase: 
        :type loadcase: :py:class:`NXOpen.CAE.AeroStructures.LoadCase` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def RemoveLoadCase(self, loadcase: LoadCase) -> None:
        """
        Remove a loadcase from the load case set builder 
        
        Signature ``RemoveLoadCase(loadcase)`` 
        
        :param loadcase: 
        :type loadcase: :py:class:`NXOpen.CAE.AeroStructures.LoadCase` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Name: str = ...
    """
    Returns or sets  the load case set name
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param title: 
    :type title: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: LoadCaseSetBuilder = ...  # unknown typename


class LoadCaseListBuilder(NXOpen.Builder):
    """
    This is a manager to the loadcases of :py:class:`CAE.AeroStructures.MarginSolution` class.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.AeroStructures.LoadCaseCollection.CreateLoadCaseListBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    def RegisterCleanup(self) -> None:
        """
        Register the removable of orphaned load cases 
        
        Signature ``RegisterCleanup()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: LoadCaseListBuilder = ...  # unknown typename


