# module 'NXOpen.CAE.AeroStructures.Author'
#
# Automatically generated 2025-06-09T14:38:44.605509
#

import typing

import NXOpen
import NXOpen.CAE
import NXOpen.CAE.AeroStructures



class OutputParameter(NXOpen.NXObject):
    """
    Parent class of all the typed output parameter classes   
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    Name: str = ...
    """
    Returns  the name.  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: OutputParameter = ...  # unknown typename


class CalculationContext(NXOpen.NXObject):
    """
    Calculation context is passed to the method implementation. 
    It contains methods to retrieve the load case set and input parameter values,
    method to set the output values and log messages   
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    
    def GetLoadCaseArray(self) -> 'list[NXOpen.CAE.AeroStructures.LoadCase]':
        """
        Get the load case array used by the calculation
        
        Signature ``GetLoadCaseArray()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.AeroStructures.LoadCase` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetInput(self, inputName: str) -> InputParameter:
        """
        Get an input parameter  
        
        Signature ``GetInput(inputName)`` 
        
        :param inputName: 
        :type inputName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.Author.InputParameter` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetOutputMs(self) -> OutputScalar:
        """
        Get MS output parameter  
        
        Signature ``GetOutputMs()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.Author.OutputScalar` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetOutput(self, outputName: str) -> OutputParameter:
        """
        Get an output parameter  
        
        Signature ``GetOutput(outputName)`` 
        
        :param outputName: 
        :type outputName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.AeroStructures.Author.OutputParameter` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetUnit(self, unitName: str) -> NXOpen.Unit:
        """
        Get unit from its name  
        
        Signature ``GetUnit(unitName)`` 
        
        :param unitName: 
        :type unitName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    @typing.overload
    def Log(self, message: str) -> None:
        """
        Log an info message
        
        Signature ``Log(message)`` 
        
        :param message:  an info message  
        :type message: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def Log(self, failureMode: str, lcIndex: int, message: str) -> None:
        """
        Log an info message indexed by possibly empty failure mode and load case
        
        Signature ``Log(failureMode, lcIndex, message)`` 
        
        :param failureMode:  a failure mode name (an empty string indicates that the message is not failure mode specific) 
        :type failureMode: str 
        :param lcIndex:  load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific)  
        :type lcIndex: int 
        :param message:  an info message 
        :type message: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def Log(self, failureMode: str, loadCase: str, message: str) -> None:
        """
        Log an info message indexed by possibly empty failure mode and load case
        
        Signature ``Log(failureMode, loadCase, message)`` 
        
        :param failureMode:  a failure mode name (an empty string indicates that the message is not failure mode specific) 
        :type failureMode: str 
        :param loadCase:  a load case name (an empty string indicates that the message is not load case specific) 
        :type loadCase: str 
        :param message:  an info message  
        :type message: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    @typing.overload
    def Warn(self, message: str) -> None:
        """
        Log a warning message
        
        Signature ``Warn(message)`` 
        
        :param message:  a warning message  
        :type message: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def Warn(self, failureMode: str, lcIndex: int, message: str) -> None:
        """
        Log a warning message indexed by possibly empty failure mode and load case
        
        Signature ``Warn(failureMode, lcIndex, message)`` 
        
        :param failureMode:  a failure mode name (an empty string indicates that the message is not failure mode specific) 
        :type failureMode: str 
        :param lcIndex:  load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific)  
        :type lcIndex: int 
        :param message:  a warning message 
        :type message: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def Warn(self, failureMode: str, loadCase: str, message: str) -> None:
        """
        Log a warning message indexed by possibly empty failure mode and load case
        
        Signature ``Warn(failureMode, loadCase, message)`` 
        
        :param failureMode:  a failure mode name (an empty string indicates that the message is not failure mode specific) 
        :type failureMode: str 
        :param loadCase:  a load case name (an empty string indicates that the message is not load case specific) 
        :type loadCase: str 
        :param message:  a warning message  
        :type message: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    @typing.overload
    def Error(self, message: str) -> None:
        """
        Log an error message
        
        Signature ``Error(message)`` 
        
        :param message:  an error message  
        :type message: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def Error(self, failureMode: str, lcIndex: int, message: str) -> None:
        """
        Log an error message indexed by possibly empty failure mode and load case
        
        Signature ``Error(failureMode, lcIndex, message)`` 
        
        :param failureMode:  a failure mode name (an empty string indicates that the message is not failure mode specific) 
        :type failureMode: str 
        :param lcIndex:  load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific)  
        :type lcIndex: int 
        :param message:  an error message 
        :type message: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def Error(self, failureMode: str, loadCase: str, message: str) -> None:
        """
        Log an error message indexed by possibly empty failure mode and load case
        
        Signature ``Error(failureMode, loadCase, message)`` 
        
        :param failureMode:  a failure mode name (an empty string indicates that the message is not failure mode specific) 
        :type failureMode: str 
        :param loadCase:  a load case name (an empty string indicates that the message is not load case specific) 
        :type loadCase: str 
        :param message:  an error message  
        :type message: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    LocationDirection: NXOpen.Matrix3x3 = ...
    """
    Returns  the location direction matrix
    
    <hr>
    
    Getter Method
    
    Signature ``LocationDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    LocationOrigin: NXOpen.Point3d = ...
    """
    Returns  the location origin point
    
    <hr>
    
    Getter Method
    
    Signature ``LocationOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Name: str = ...
    """
    Returns  the name.  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: CalculationContext = ...  # unknown typename


class MethodLibrary():
    """
    Represents a :py:class:`NXOpen.CAE.AeroStructures.Author.MethodLibrary` object.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX12.0.0
    """
    
    def RegisterEvaluate(self, methodID: str, version: int, cb: typing.Callable) -> None:
        """
        Routine to register an evaluate callback 
        
        Signature ``RegisterEvaluate(methodID, version, cb)`` 
        
        :param methodID: 
        :type methodID: str 
        :param version: 
        :type version: int 
        :param cb:  routine to register  
        :type cb: CallableObject 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RegisterValidate(self, methodID: str, version: int, cb: typing.Callable) -> None:
        """
        Routine to register a validate callback 
        
        Signature ``RegisterValidate(methodID, version, cb)`` 
        
        :param methodID: 
        :type methodID: str 
        :param version: 
        :type version: int 
        :param cb:  routine to register  
        :type cb: CallableObject 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    @staticmethod
    def GetMethodLibrary():
        ...
    


class OutputScalar(OutputParameter):
    """
    Represents a scalar output parameter  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    
    @typing.overload
    def SetValue(self, doubleVal: float) -> None:
        """
        Set scalar value according to default unit 
        
        Signature ``SetValue(doubleVal)`` 
        
        :param doubleVal:  the double value of the parameter 
        :type doubleVal: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, doubleVal: float, unitType: NXOpen.Unit) -> None:
        """
        Set scalar value with a specific unit type. 
        
        Signature ``SetValue(doubleVal, unitType)`` 
        
        :param doubleVal:  the double value of the parameter expressed in the specified unit 
        :type doubleVal: float 
        :param unitType:  the unit in which the value must be converted if necessary 
        :type unitType: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, fmName: str, doubleVal: float) -> None:
        """
        Set scalar value according to default unit for a failure mode 
        
        Signature ``SetValue(fmName, doubleVal)`` 
        
        :param fmName:  failure mode name  
        :type fmName: str 
        :param doubleVal:  the double value of the parameter 
        :type doubleVal: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, fmName: str, lcIndex: int, doubleVal: float) -> None:
        """
        Set scalar value according to default unit for a failure mode and a loadcase specified by its index
        
        Signature ``SetValue(fmName, lcIndex, doubleVal)`` 
        
        :param fmName:  failure mode name, if empty the value will be set for any failure mode  
        :type fmName: str 
        :param lcIndex:  load case index corresponding to the load case position in the load case array of the calculation context 
        :type lcIndex: int 
        :param doubleVal:  the double value of the parameter 
        :type doubleVal: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, fmName: str, doubleVal: float, unitType: NXOpen.Unit) -> None:
        """
        Set scalar value with a specific unit type for a failure mode 
        
        Signature ``SetValue(fmName, doubleVal, unitType)`` 
        
        :param fmName:  failure mode name  
        :type fmName: str 
        :param doubleVal:  the double value of the parameter 
        :type doubleVal: float 
        :param unitType:  the unit in which the value must be converted if necessary 
        :type unitType: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, fmName: str, lcIndex: int, doubleVal: float, unitType: NXOpen.Unit) -> None:
        """
        Set scalar valuewith a specific unit type  for a failure mode and a loadcase specified by its index
        
        Signature ``SetValue(fmName, lcIndex, doubleVal, unitType)`` 
        
        :param fmName:  failure mode name, if empty the value will be set for any failure mode  
        :type fmName: str 
        :param lcIndex:  load case index corresponding to the load case position in the load case array of the calculation context 
        :type lcIndex: int 
        :param doubleVal:  the double value of the parameter 
        :type doubleVal: float 
        :param unitType:  the unit in which the value must be converted if necessary 
        :type unitType: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Unit: NXOpen.Unit = ...
    """
    Returns  the unit type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Unit`` 
    
    :returns:  the unit in which the value is expressed 
    :rtype: :py:class:`NXOpen.Unit` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: OutputScalar = ...  # unknown typename


class OutputBoolean(OutputParameter):
    """
    Represents a boolean output parameter  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    
    @typing.overload
    def SetValue(self, boolVal: bool) -> None:
        """
        Set boolean value. 
        
        Signature ``SetValue(boolVal)`` 
        
        :param boolVal: 
        :type boolVal: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, fmName: str, boolVal: bool) -> None:
        """
        Set boolean value for a failure mode 
        
        Signature ``SetValue(fmName, boolVal)`` 
        
        :param fmName:  failure mode name  
        :type fmName: str 
        :param boolVal: 
        :type boolVal: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, fmName: str, lcIndex: int, boolVal: bool) -> None:
        """
        Set boolean value for a failure mode and a loadcase specified by its index
        
        Signature ``SetValue(fmName, lcIndex, boolVal)`` 
        
        :param fmName:  failure mode name, if empty the value will be set for any failure mode  
        :type fmName: str 
        :param lcIndex:  load case index corresponding to the load case position in the load case array of the calculation context 
        :type lcIndex: int 
        :param boolVal: 
        :type boolVal: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: OutputBoolean = ...  # unknown typename


class InputParameter(NXOpen.NXObject):
    """
    parent class of all typed input parameter classes  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    Name: str = ...
    """
    Returns  the name.  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: InputParameter = ...  # unknown typename


class InputText(InputParameter):
    """
    Represents a text input parameter  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    Value: str = ...
    """
    Returns  the value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: InputText = ...  # unknown typename


class InputBoolean(InputParameter):
    """
    Represents a boolean input parameter  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    Value: bool = ...
    """
    Returns  the value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: InputBoolean = ...  # unknown typename


class InputScalar(InputParameter):
    """
    Represents a scalar input parameter  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    
    @typing.overload
    def GetValue(self) -> float:
        """
        Get the value expressed in default unit 
        
        Signature ``GetValue()`` 
        
        :returns:  the double value of the parameter 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def GetValue(self, unitType: NXOpen.Unit) -> float:
        """
        Get the value using a specific unit type.  
        
        Signature ``GetValue(unitType)`` 
        
        :param unitType:  the unit in which the value must be converted if necessary 
        :type unitType: :py:class:`NXOpen.Unit` 
        :returns:  the double value of the parameter expressed in the specified unit 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Unit: NXOpen.Unit = ...
    """
    Returns  the unit type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Unit`` 
    
    :returns:  the unit in which the value is expressed 
    :rtype: :py:class:`NXOpen.Unit` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: InputScalar = ...  # unknown typename


class OutputText(OutputParameter):
    """
    Represents a text output parameter  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    
    @typing.overload
    def SetValue(self, textVal: str) -> None:
        """
        Set text value. 
        
        Signature ``SetValue(textVal)`` 
        
        :param textVal: 
        :type textVal: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, fmName: str, textVal: str) -> None:
        """
        Set text value for a failure mode 
        
        Signature ``SetValue(fmName, textVal)`` 
        
        :param fmName:  failure mode name  
        :type fmName: str 
        :param textVal: 
        :type textVal: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, fmName: str, lcIndex: int, textVal: str) -> None:
        """
        Set text value for a failure mode and a loadcase specified by its index
        
        Signature ``SetValue(fmName, lcIndex, textVal)`` 
        
        :param fmName:  failure mode name, if empty the value will be set for any failure mode  
        :type fmName: str 
        :param lcIndex:  load case index corresponding to the load case position in the load case array of the calculation context 
        :type lcIndex: int 
        :param textVal: 
        :type textVal: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: OutputText = ...  # unknown typename


class InputLoadLoadSupportTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class InputLoadLoadSupportType():
    """
    the support type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "not available (the aggregation has been done at the calculation level, GetValues() will return a vector of aggregated values)"
       "Node", "Node (the method has to aggregated values that have been extracted per node, GetValues() will return a table of values)"
       "Element", "Element (the method has to aggregated values that have been extracted per element, GetValues() will return a table of values)"
    """
    NotSet = 0  # InputLoadLoadSupportTypeMemberType
    Node = 1  # InputLoadLoadSupportTypeMemberType
    Element = 2  # InputLoadLoadSupportTypeMemberType
    
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
    


class InputLoad(InputParameter):
    """
    represent a load input parameter  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    
    class LoadSupportType():
        """
        the support type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "not available (the aggregation has been done at the calculation level, GetValues() will return a vector of aggregated values)"
           "Node", "Node (the method has to aggregated values that have been extracted per node, GetValues() will return a table of values)"
           "Element", "Element (the method has to aggregated values that have been extracted per element, GetValues() will return a table of values)"
        """
        NotSet = 0  # InputLoadLoadSupportTypeMemberType
        Node = 1  # InputLoadLoadSupportTypeMemberType
        Element = 2  # InputLoadLoadSupportTypeMemberType
        
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
        
    
    
    def GetNodes(self) -> 'list[NXOpen.CAE.FENode]':
        """
        Get support nodes 
        
        Signature ``GetNodes()`` 
        
        :returns:  the list of support nodes if available 
        :rtype: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetElements(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Get support elements 
        
        Signature ``GetElements()`` 
        
        :returns:  the list of support element if available 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    @typing.overload
    def GetValues(self) -> None:
        """Returns  the values"""
        ...
    
    @typing.overload
    def GetValues(self) -> NXOpen.GeneralScalarTable:
        """
        Getter Method
        
        Signature ``Values`` 
        
        :returns:  either a one dimentional two dimensional array of doubles 
        :rtype: :py:class:`NXOpen.GeneralScalarTable` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def GetValues(self, unitType: NXOpen.Unit) -> NXOpen.GeneralScalarTable:
        """
        Get value using a specific unit type.  
        
        Signature ``GetValues(unitType)`` 
        
        :param unitType:  the unit in which the value must be converted if necessary 
        :type unitType: :py:class:`NXOpen.Unit` 
        :returns:  either a one dimentional two dimensional array of doubles 
        :rtype: :py:class:`NXOpen.GeneralScalarTable` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Quantity: NXOpen.CAE.ResultQuantity = ...
    """
    Returns  the quantity 
    
    <hr>
    
    Getter Method
    
    Signature ``Quantity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResultQuantity` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SupportType: InputLoadLoadSupportType = ...
    """
    Returns  the support type 
    
    <hr>
    
    Getter Method
    
    Signature ``SupportType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.AeroStructures.Author.InputLoadLoadSupportType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Unit: NXOpen.Unit = ...
    """
    Returns  the unit type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Unit`` 
    
    :returns:  the unit in which the value is expressed 
    :rtype: :py:class:`NXOpen.Unit` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Values: NXOpen.GeneralScalarTable = ...
    """
    Returns  the values 
    
    <hr>
    
    Getter Method
    
    Signature ``Values`` 
    
    :returns:  either a one dimentional two dimensional array of doubles 
    :rtype: :py:class:`NXOpen.GeneralScalarTable` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: InputLoad = ...  # unknown typename


class OutputInteger(OutputParameter):
    """
    Represents an integer output parameter  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    
    @typing.overload
    def SetValue(self, intVal: int) -> None:
        """
        Set integer value. 
        
        Signature ``SetValue(intVal)`` 
        
        :param intVal: 
        :type intVal: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, fmName: str, intVal: int) -> None:
        """
        Set integer value for a failure mode 
        
        Signature ``SetValue(fmName, intVal)`` 
        
        :param fmName:  failure mode name  
        :type fmName: str 
        :param intVal: 
        :type intVal: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    @typing.overload
    def SetValue(self, fmName: str, lcIndex: int, intVal: int) -> None:
        """
        Set integer value for a failure mode and a loadcase specified by its index
        
        Signature ``SetValue(fmName, lcIndex, intVal)`` 
        
        :param fmName:  failure mode name, if empty the value will be set for any failure mode  
        :type fmName: str 
        :param lcIndex:  load case index corresponding to the load case position in the load case array of the calculation context 
        :type lcIndex: int 
        :param intVal: 
        :type intVal: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: OutputInteger = ...  # unknown typename


class ABBStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ABBStatus():
    """
    ABB return status 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Success", "ABB computation success"
       "Failed", "ABB computation failed"
    """
    Success = 0  # ABBStatusMemberType
    Failed = 1  # ABBStatusMemberType
    
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
    


class ABBEdgeSupportTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ABBEdgeSupportType():
    """
    Type of support along the edges, the choice is between SimplySupported and Clamped 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SimplySupported", "Simply supported"
       "Clamped", "Clamped"
    """
    SimplySupported = 0  # ABBEdgeSupportTypeMemberType
    Clamped = 1  # ABBEdgeSupportTypeMemberType
    
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
    


class ABBUnloadedEdgeSupportTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ABBUnloadedEdgeSupportType():
    """
    Type of support along unloaded edges, the choices are: {Clamped-Clamped, Simply Supported-Clamped, Simply Supported-Simply Supported, Free-Clamped, Free-Simply Supported} 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ClampedClamped", "Clamped-Clamped"
       "SimplySupportedClamped", "Simply Supported-Clamped"
       "SimplySupportedSimplySupported", "Simply Supported-Simply Supported"
       "FreeClamped", "Free-Clamped"
       "FreeSimplySupported", "Free-Simply Supported"
    """
    ClampedClamped = 0  # ABBUnloadedEdgeSupportTypeMemberType
    SimplySupportedClamped = 1  # ABBUnloadedEdgeSupportTypeMemberType
    SimplySupportedSimplySupported = 2  # ABBUnloadedEdgeSupportTypeMemberType
    FreeClamped = 3  # ABBUnloadedEdgeSupportTypeMemberType
    FreeSimplySupported = 4  # ABBUnloadedEdgeSupportTypeMemberType
    
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
    


class ABBMaterialBehaviourMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ABBMaterialBehaviour():
    """
    Material behaivour type, the choices are: {Elastic, Elastic-plastic} 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Elastic", "Elastic behaviour"
       "ElasticPlastic", "Elastic-plastic behaviour"
    """
    Elastic = 0  # ABBMaterialBehaviourMemberType
    ElasticPlastic = 1  # ABBMaterialBehaviourMemberType
    
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
    


class ABB():
    """
    Represents a AeroStruct application building block (ABB)   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX12.0.0
    """
    
    class Status():
        """
        ABB return status 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Success", "ABB computation success"
           "Failed", "ABB computation failed"
        """
        Success = 0  # ABBStatusMemberType
        Failed = 1  # ABBStatusMemberType
        
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
        
    
    
    class EdgeSupportType():
        """
        Type of support along the edges, the choice is between SimplySupported and Clamped 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SimplySupported", "Simply supported"
           "Clamped", "Clamped"
        """
        SimplySupported = 0  # ABBEdgeSupportTypeMemberType
        Clamped = 1  # ABBEdgeSupportTypeMemberType
        
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
        
    
    
    class UnloadedEdgeSupportType():
        """
        Type of support along unloaded edges, the choices are: {Clamped-Clamped, Simply Supported-Clamped, Simply Supported-Simply Supported, Free-Clamped, Free-Simply Supported} 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ClampedClamped", "Clamped-Clamped"
           "SimplySupportedClamped", "Simply Supported-Clamped"
           "SimplySupportedSimplySupported", "Simply Supported-Simply Supported"
           "FreeClamped", "Free-Clamped"
           "FreeSimplySupported", "Free-Simply Supported"
        """
        ClampedClamped = 0  # ABBUnloadedEdgeSupportTypeMemberType
        SimplySupportedClamped = 1  # ABBUnloadedEdgeSupportTypeMemberType
        SimplySupportedSimplySupported = 2  # ABBUnloadedEdgeSupportTypeMemberType
        FreeClamped = 3  # ABBUnloadedEdgeSupportTypeMemberType
        FreeSimplySupported = 4  # ABBUnloadedEdgeSupportTypeMemberType
        
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
        
    
    
    class MaterialBehaviour():
        """
        Material behaivour type, the choices are: {Elastic, Elastic-plastic} 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Elastic", "Elastic behaviour"
           "ElasticPlastic", "Elastic-plastic behaviour"
        """
        Elastic = 0  # ABBMaterialBehaviourMemberType
        ElasticPlastic = 1  # ABBMaterialBehaviourMemberType
        
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
        
    
    
    def GetUltimateLimitFactor(self) -> float:
        """
        Ultimate limit factor from the customer default
        
        Signature ``GetUltimateLimitFactor()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetIntegerNa(self) -> float:
        """
        Integer NA value
        
        Signature ``GetIntegerNa()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetPi(self) -> float:
        """
        PI number
        
        Signature ``GetPi()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetRealMax(self) -> float:
        """
        Maximum real number
        
        Signature ``GetRealMax()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetRealEpsilon(self) -> float:
        """
        Real epsilon
        
        Signature ``GetRealEpsilon()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetRealNa(self) -> float:
        """
        Real NA
        
        Signature ``GetRealNa()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def IsRealNa(self, value: float) -> bool:
        """
        Tests if a value is NA
        
        Signature ``IsRealNa(value)`` 
        
        :param value: 
        :type value: float 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetRealPositiveInfinity(self) -> float:
        """
        The positive infinity value
        
        Signature ``GetRealPositiveInfinity()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def IsRealPositiveInfinity(self, value: float) -> bool:
        """
        Tests if a value equals positive infinity
        
        Signature ``IsRealPositiveInfinity(value)`` 
        
        :param value: 
        :type value: float 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetRealNegativeInfinity(self) -> float:
        """
        The negative infinity value
        
        Signature ``GetRealNegativeInfinity()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def IsRealNegativeInfinity(self, value: float) -> bool:
        """
        Tests if a value equals negative infinity
        
        Signature ``IsRealNegativeInfinity(value)`` 
        
        :param value: 
        :type value: float 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMsThreshold(self) -> float:
        """
        The MS (margin of safety) threshold
        
        Signature ``GetMsThreshold()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CurvedMetallicPanelCompressiveBucklingCoefficient(self, b: float, t: float, r: float, nu: float) -> tuple:
        """
        Curves for finding 'kc' the compressive-buckling coefficient for curved sheet panel
        
        This curve is extracted from Bruhn manual, figure C9.1
        Used for finding 'kc' the compressive-buckling coefficient for curved sheet panel, with 
        simply-supported edges.
        
        Input
        b dimension in radial axis
        t thickness
        r radius
        nu Poisson coefficient
        Output
        kc compressive-buckling coefficient
        Returns
        Status of the calculation
        
        Signature ``CurvedMetallicPanelCompressiveBucklingCoefficient(b, t, r, nu)`` 
        
        :param b:  Dimension in radial axis  
        :type b: float 
        :param t:  Panel thickness  
        :type t: float 
        :param r:  Panel radius  
        :type r: float 
        :param nu:  Material Poisson coefficient  
        :type nu: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, kc). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. kc is a float.   Compressive-buckling coefficient 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CurvedMetallicPanelShearBucklingCoefficient(self, a: float, b: float, t: float, r: float, nu: float, bc: ABBEdgeSupportType) -> tuple:
        """
        Curves for finding 'ks' the shear-buckling coefficient for curved sheet panel
        
        These curves are extracted from Bruhn manual, figures C9.  
        
        2 to C9.5
        Used for finding 'ks' the shear-buckling coefficient for curved sheet panel, with 
        simply-supported or clamped edges.
        
        Input
        a Dimension in longitudinal axis
        b Dimension in radial axis
        t Thickness
        r Radius
        nu Poisson coefficient
        BC Type of support along the edges, the choice is between SimplySupported and Clamped
        Output
        ks Shear-buckling coefficient
        Returns
        False if input values are out of bounds
        
        Signature ``CurvedMetallicPanelShearBucklingCoefficient(a, b, t, r, nu, bc)`` 
        
        :param a:  Dimension in longitudinal axis  
        :type a: float 
        :param b:  Dimension in radial axis  
        :type b: float 
        :param t:  Thickness  
        :type t: float 
        :param r:  Radius  
        :type r: float 
        :param nu:  Poisson coefficient  
        :type nu: float 
        :param bc:  Type of support along the edges  
        :type bc: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType` 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ks). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ks is a float.   Compressive-buckling coefficient 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def EquivalentSectionProperties(self, n: 'list[float]', iAi: 'list[float]', iEi: 'list[float]', iIxxi: 'list[float]') -> tuple:
        """
        Compute equivalent section properties (area, center of gravity, Young's modulus and inertia) of a profile composed of different sub-sections.  
        
        Input
        n Number of sub-sections that compose the section
        Ai Areas of sub-sections
        Ycogi Center of gravity of sub-sections in Y direction
        Ei Young's modulus of sub-sections
        Ixxi Moments of inertia (Quadratic moments) of sub-sections around XX (expressed at the center of gravity of each sub-section)
        Output
        A Area of the equivalent section (sum of all sub-sections)
        E Young's modulus of the equivalent section
        Ycog Center of gravity of the equivalent section in Y direction
        Ixx Moment of inertia of the equivalent section around XX (expressed at the center of gravity of the equivalent section)
        
        Signature ``EquivalentSectionProperties(n, iAi, iEi, iIxxi)`` 
        
        :param n:  Number of sub-sections that compose the section  
        :type n: list of float 
        :param iAi:  Areas of sub-sections  
        :type iAi: list of float 
        :param iEi:  Young's modulus of sub-sections  
        :type iEi: list of float 
        :param iIxxi:  Moments of inertia (Quadratic moments) of sub-sections around XX (expressed at the center of gravity of each sub-section)  
        :type iIxxi: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, a, e, oYcog, oIxx). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. a is a list of float.   Area of the equivalent section (sum of all sub-sections) e is a list of float.   Young's modulus of the equivalent section oYcog is a list of float.   Center of gravity of the equivalent section in Y direction oIxx is a list of float.   Moment of inertia of the equivalent section around XX (expressed at the center of gravity of the equivalent section) 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def ExtrudedMetallicSubSectionCripplingAllowable(self, iFcy: float, e: float, fe: int, b: float, t: float) -> tuple:
        """
        Compute Crippling stress allowable for a given segment
        
        Crippling curves for a sub-section (also called a segment) of extruded metallic profiles.
        
        The computed value is 'Fcc'.
        'Fcc' is thresholded by 'Fcy', to avoid plasticity of material.
        Segment's width ('b') is assumed to be greater than its thickness ('t').
        
        Input
        Fcy Compressive yield allowable stress
        E Young's modulus
        FE Segment's number of free edges
        b Segment's width
        t Segment's thickness
        Output
        Fcc Equivalent stress allowable
        Returns
        Computation status
        
        Signature ``ExtrudedMetallicSubSectionCripplingAllowable(iFcy, e, fe, b, t)`` 
        
        :param iFcy:  Compressive yield allowable stress  
        :type iFcy: float 
        :param e:  Young's modulus  
        :type e: float 
        :param fe:  Segment's number of free edges  
        :type fe: int 
        :param b:  Segment's width  
        :type b: float 
        :param t:  Segment's thickness  
        :type t: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, iFcc). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. iFcc is a float.   Equivalent stress allowable 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def FlatMetallicPanelBendingBucklingCoefficient(self, aOverB: float, beta: float) -> tuple:
        """
        Curves for finding the bending buckling stress coefficient for thin flat plates
        
        Used for finding 'kb' the bending buckling stress coefficient as a function of:
        * 'a/b', the panel length ratio
        *  'a' is the unloaded edge length
        *  'b' is the loaded edge length
        * 'beta',  is the factor which, divided to b, gives the edge length in compression (while 
        the remaining edge length is in tension).
        
        Input
        a_over_b Panel length ratio
        beta loading length ratio
        Output
        kb bending buckling stress coefficient
        Returns
        False if input values are out of bounds
        
        Signature ``FlatMetallicPanelBendingBucklingCoefficient(aOverB, beta)`` 
        
        :param aOverB:  Panel length ratio  
        :type aOverB: float 
        :param beta:  Loading length ratio  
        :type beta: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, kb). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. kb is a float.   Bending buckling stress coefficient 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def FlatMetallicPanelCompressiveBucklingCoefficient(self, a: float, b: float, bcUnloaded: ABBUnloadedEdgeSupportType, bcLoaded: ABBEdgeSupportType) -> tuple:
        """
        Curves for finding 'kc' the compressive-buckling coefficient for rectangular metallic flat plate
        
        Used for finding 'kc' the compressive-buckling coefficient for rectangular metallic flat plate, 
        as a function of edge lengths and edge boundary conditions
        
        Input
        a    Unloaded edge length
        b    Loaded edge length
        BC_Unloaded Type of support along unloaded edges {Clamped-Clamped, Simply Supported-Clamped, Simply Supported-Simply Supported, Free-Clamped, Free-Simply Supported}
        BC_Loaded Type of support along loaded edges {Clamped or Simply Supported}
        Output
        kc Compressive buckling coefficient
        Returns
        Computation status
        
        Signature ``FlatMetallicPanelCompressiveBucklingCoefficient(a, b, bcUnloaded, bcLoaded)`` 
        
        :param a:  Unloaded edge length  
        :type a: float 
        :param b:  Loaded edge length  
        :type b: float 
        :param bcUnloaded:  Type of support along unloaded edges  
        :type bcUnloaded: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBUnloadedEdgeSupportType` 
        :param bcLoaded:  Type of support along loaded edges  
        :type bcLoaded: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType` 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, kc). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. kc is a float.   Compressive buckling coefficient 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def FlatMetallicPanelShearBucklingCoefficient(self, a: float, b: float, bc: ABBEdgeSupportType) -> tuple:
        """
        Curves for finding 'ks' the shear-buckling coefficient for flat rectangular plate
        
        These curves are inspired by Bruhn manual.
        Used for finding 'ks' the shear-buckling coefficient for flat rectangular plate, as a function of edge lengths and boundary conditions
        
        Input
        a  Longer plate dimension
        b  Shorter plate dimension
        BC Type of support along the edges {Simply Supported or Clamped}
        Output
        ks  Shear-buckling coefficient
        Returns
        Computation status
        
        Signature ``FlatMetallicPanelShearBucklingCoefficient(a, b, bc)`` 
        
        :param a:  Longer plate dimension  
        :type a: float 
        :param b:  Shorter plate dimension  
        :type b: float 
        :param bc:  Type of support along the edges  
        :type bc: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType` 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ks). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ks is a float.   Shear-buckling coefficient 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def LoadDistributionBoltsConcentricLoads(self, p: 'list[float]', iPsn: 'list[float]', nblcXnbbolt: int) -> tuple:
        """
        Computes bolt loads for multiple bolt fitting - Concentric load
        
        Formula
        Pn = P * (Psn / SUM(Psn))
        where:
        * 'P' is the load acting on the fitting
        * 'Psn' is the allowable strength of bolt n
        * 'Pn' is the shear load on bolt n
        
        Input
        nblc Number of load cases
        P Load acting on fitting (nblc)
        nbbolt Number of bolts
        Psn Allowable shear strength of bolt (nbbolt)
        Output
        Pn Shear load on bolt (nblc x nbbolt)
        Return
        Status of the calculation
        
        Signature ``LoadDistributionBoltsConcentricLoads(p, iPsn, nblcXnbbolt)`` 
        
        :param p:  Load acting on fitting (nblc)  
        :type p: list of float 
        :param iPsn:  Allowable shear strength of bolt (nbbolt)  
        :type iPsn: list of float 
        :param nblcXnbbolt: 
        :type nblcXnbbolt: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, oPn). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. oPn is a list of float.   Shear load on bolt (nblc x nbbolt) 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MaterialFsyEstimation(self, iFtyL: float, iFtyLT: float, iFcyL: float, iFcyLT: float, iFsu: float, iFtuL: float, iFtuLT: float) -> tuple:
        """
        Estimation of shear yield stress (Fsy)
        
        Shear yield stress allowable ('Fsy') is estimated on the basis of the following formula:
        'Fsy=( FtyL + FtyLT + FcyL + FcyLT ) / 4 * ( 2 * Fsu)/( FtuL + FtuLT )'
        where:
        * 'FtyL' is the tensile yield stress under longitudinal direction
        * 'FtyLT' is the tensile yield stress under long transverse direction
        * 'FcyL' is  the compressive yield stress under longitudinal direction
        * 'FcyLT' is the compressive yield stress under long transverse direction
        * 'Fsu' is the shear ultimate stress
        * 'FtuL' is the tensile ultimate stress under longitudinal direction
        * 'FtuLT' is the tensile ultimate stress under long transverse direction
        
        Input
        FtyL Tensile yield stress, longitudinal direction
        FtyLT Tensile yield stress, long transverse direction
        FcyL Compressive yield stress, longitudinal direction
        FcyLT Compressive yield stress, long transverse direction
        Fsu Shear ultimate stress
        FtuL Tensile ultimate stress, longitudinal direction
        FtuLT Tensile ultimate stress, long transverse direction
        Output
        Fsy Shear yield stress
        Return
        Status of the calculation
        
        Signature ``MaterialFsyEstimation(iFtyL, iFtyLT, iFcyL, iFcyLT, iFsu, iFtuL, iFtuLT)`` 
        
        :param iFtyL:  Tensile yield stress, longitudinal direction  
        :type iFtyL: float 
        :param iFtyLT:  Tensile yield stress, long transverse direction  
        :type iFtyLT: float 
        :param iFcyL:  Compressive yield stress, longitudinal direction  
        :type iFcyL: float 
        :param iFcyLT:  Compressive yield stress, long transverse direction  
        :type iFcyLT: float 
        :param iFsu:  Shear ultimate stress  
        :type iFsu: float 
        :param iFtuL:  Tensile ultimate stress, longitudinal direction  
        :type iFtuL: float 
        :param iFtuLT:  Tensile ultimate stress, long transverse direction  
        :type iFtuLT: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, oFsy). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. oFsy is a float.   Shear yield stress 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MetallicPanelCompressivePlasticityCurveBc1(self, x: float, n: float) -> tuple:
        """
        Metallic panel compressive plasticity curve BC1
        Curves for finding critical buckling stress / secant yield stress F0.  
        
        7
        
        Used for finding 'sigma_cr' the inelastic buckling strength of metallic flat rectangular plate in compression.
        The Boundary Condition for the unloaded edges is Simply Supported-Free. It computes:
        * 'sigma_cr /sigma_0.7' as a function of '(kc * pi^2E) / (12 * (1-nu^2) * sigma_0.7)(t/b)^2'  and 'n' where
        * 'sigma_cr' is the  critical stress allowable
        * 'sigma_0.7' is the [stress for secant modulus equal to 70% of Young modulus]
        * 'kc' is the buckling coefficient, computed in Figure FlatMetallicPanelCompressiveBucklingCoefficient
        * 'E' is the Young's modulus
        * 'nu' is the Poisson coefficient
        * 't' is the plate thickness
        * 'b' is the loaded edge length
        * 'n' is the Ramberg-Osgood parameter
        
        Input
        X Critical buckling stress (elastic) / secant yield stress F0.7
        n Ramberg-Osgood parameter
        Output
        Z Critical buckling stress (including plasticity) / secant yield stress F0.7
        Returns
        Status of the computation
        
        Signature ``MetallicPanelCompressivePlasticityCurveBc1(x, n)`` 
        
        :param x:  Critical buckling stress (elastic) / secant yield stress F0.7  
        :type x: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, z). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. z is a float.   Critical buckling stress (including plasticity) / secant yield stress F0.7 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MetallicPanelCompressivePlasticityCurveBc2(self, x: float, n: float) -> tuple:
        """
        Metallic panel compressive plasticity curve BC2
        Curves for finding critical inter-rivet buckling stress (or critical wrinkling stress) / secant yield stress F0.  
        
        7
        
        Used for finding 'Fir' or 'Fw'.
        It computes either:
        * 'Fir /F0.7' as a function of '(C * pi^2E)/(12 * (1-nu^2) * F0.7)(ts/p)^2' and 'n' where
        *  'Fir' is the Inter-Rivet Buckling stress allowable (with plasticity)
        *  'F0.7' is the [stress for secant modulus equal to 70% of Young modulus]
        *  'C' is the end fixity coefficient
        *  'E' is the Young's modulus
        *  'nu' is the Poisson coefficient
        *  'ts' is the thickness of the sheet
        *  'p' is the rivet spacing
        *  'n' is the Ramberg-Osgood parameter
        
        Or:
        * 'Fw /F0.7' as a function of '(kw * pi^2E)/(12 * (1-nu^2) * F0.7)(ts/bs)^2' and 'n' where
        *  'Fw' is the wrinkling stress allowable
        *  'kw' is the wrinkling failing stress coefficient
        *  'ts' is the thickness of the sheet
        *  'bs' is the stiffener spacing
        *  'n' is the Ramberg-Osgood parameter
        
        Input
        X Critical buckling stress (elastic) / secant yield stress F0.7
        n Ramberg-Osgood parameter
        Output
        Z Critical buckling/wrinkling stress (including plasticity) / secant yield stress F0.7
        Returns
        Status of the computation
        
        Signature ``MetallicPanelCompressivePlasticityCurveBc2(x, n)`` 
        
        :param x:  Critical buckling stress (elastic) / secant yield stress F0.7  
        :type x: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, z). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. z is a float.   Critical buckling/wrinkling stress (including plasticity) / secant yield stress F0.7 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MetallicPanelCompressivePlasticityCurveBc3(self, x: float, n: float) -> tuple:
        """
        Metallic panel compressive plasticity curve BC3
        Curves for finding critical buckling stress / secant yield stress F0.  
        
        7
        
        Used for finding 'sigma_cr' the inelastic buckling strength of metallic cylinder in compression.
        
        It computes:
        * 'sigma_cr /sigma_0.7' as a function of '(kc * pi^2E)/(12 * (1-nu^2) * sigma_0.7)(t/b)^2'  and 'n' where
        *  'sigma_cr' is the  critical stress allowable
        *  'sigma_0.7' is the [stress for secant modulus equal to 70% of Young's modulus]
        *  'kc' is the buckling coefficient, computed in Figure FlatMetallicPanelCompressiveBucklingCoefficient
        *  'E' is the Young's modulus
        *  'nu' is the Poisson coefficient
        *  't' is the plate thickness
        *  'b' is the loaded edge length
        *  'n' is the Ramberg-Osgood parameter
        
        Input
        X Critical buckling stress (elastic) / secant yield stress F0.7
        n Ramberg-Osgood parameter
        Output
        Z Critical buckling stress (including plasticity) / secant yield stress F0.7
        Returns
        Status of the computation
        
        Signature ``MetallicPanelCompressivePlasticityCurveBc3(x, n)`` 
        
        :param x:  Critical buckling stress (elastic) / secant yield stress F0.7  
        :type x: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, z). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. z is a float.   Critical buckling stress (including plasticity) / secant yield stress F0.7 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def SecantModulus(self, e: float, n: float, fy: float, sigma: float) -> tuple:
        """
        Secant modulus
        Computes the secant modulus from material properties and stress.  
        
        The secant modulus ('Es') is defined as the stress('f') to strain ('epsilon') ratio at each value of stress.
        
        The formula is 'Es = f / ( f / E + 0.002 * ( f / fy ) ^ n )'
        where:
        * 'f' is the stress
        * 'fy' is the yield stress
        * 'E' is the Young's modulus
        * 'n' is the Ramberg-Osgood parameter
        
        The formula can be applied in compression and is 'Es = f / ( f / Ec + 0.002 * ( f / Fcy ) ^ nc)'
        where:
        * 'Fcy' is the compressive yield stress
        * 'Ec' is the compressive Young's modulus
        * 'nc' is the compressive Ramberg-Osgood parameter
        
        Input
        E Young's modulus
        n Ramberg-Osgood parameter
        fy Yield stress
        sigma Stress
        Output
        Es Secant modulus
        Return
        Status of the computation 
        
        Signature ``SecantModulus(e, n, fy, sigma)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param fy:  Yield stress  
        :type fy: float 
        :param sigma:  Stress  
        :type sigma: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, iEs). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. iEs is a float.   Secant modulus 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def StressFromStrainInPlasticDomain(self, strain: float, e: float, iF02ys: float, n: float) -> tuple:
        """
        Compute stress from strain with the help of Ramberg-Osgood relationship
        
        The Ramberg-Osgood relationship allows to describe stress-strain curve with the help of a dedicated material parameter ('n').
        'e = f / E + 0.002 * ( f / f0.2ys ) ^ n'
        where:
        * 'e' is the total strain that takes into account elastic and plastic strains.
        * 'f' is the stress
        * 'E' is the material Young's modulus
        * 'f0.2ys' is the material yield allowable (Fcy or Fty depending load type).
        * 'n' is the Ramberg-Osgood parameter (in case of compressive load, it is common to call it 'nc').
        
        The Ramberg-Osgood equation can not be inverted. As a consequence, stress is determined by numerical iterative calculation.
        
        Input
        strain Total strain
        E Young's modulus
        F02ys Yield allowable (typically Fcy)
        n Ramberg-Osgood's parameter
        Output
        sigma Stress
        
        Signature ``StressFromStrainInPlasticDomain(strain, e, iF02ys, n)`` 
        
        :param strain:  Total strain  
        :type strain: float 
        :param e:  Young's modulus  
        :type e: float 
        :param iF02ys:  Yield allowable (typically Fcy)  
        :type iF02ys: float 
        :param n:  Ramberg-Osgood's parameter  
        :type n: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, sigma). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. sigma is a float.   Stress 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def StressF07(self, iFy: float, e: float, n: float) -> tuple:
        """
        Stress F0.  
        
        7
        Computes the stress for secant modulus equal to 70% of Young's modulus.
        
        The calculation is based upon the material properties. 'F0.7' is defined by:
        'F0.7/epsilon=0.7E', where 'epsilon' is the strain, and 'E' is the Young's modulus.
        The formula can be applied for tensile and compressive stress, hence:
        'F0.7 = ( (1/0.7 - 1) / 0.002 * Fty ^ n / E ) ^ ( 1 / ( n - 1 ) )' for tension, 
        and 'F0.7c = ( ( 1 / 0.7 - 1 ) / 0.002 * Fcy ^ nc / Ec ) ^ ( 1 / ( nc - 1 ) )' for compression.
        
        where:
        * 'Fcy' is the compressive yield stress allowable
        * 'Fty' the tensile yield stress allowable
        * 'n' the Ramberg-Osgood parameter
        * 'Ec' the compressive Young's modulus
        * 'nc' the compressive Ramberg-Osgood parameter
        
        Input
        Fy Yield stress allowable
        E Young's modulus
        n Ramberg-Osgood parameter
        Output
        F07 Secant yield stress F0.7
        
        Signature ``StressF07(iFy, e, n)`` 
        
        :param iFy:  Yield stress allowable 
        :type iFy: float 
        :param e:  Young's modulus  
        :type e: float 
        :param n:  Ramberg-Osgood's parameter  
        :type n: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, f07). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. f07 is a float.   Secant yield stress F0.7 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def TangentModulus(self, e: float, n: float, iFy: float, sigma: float) -> tuple:
        """
        Computes the tangent modulus from material properties and stress.  
        
        The tangent modulus ('Et') is defined as the slope of the stress('f')-strain('epsilon') curve at each value of stress.
        
        The formula is 'Et = f / ( f / E + 0.002 * n * ( f / FY ) ^ n )'
        where:
        * 'f' is the stress
        * 'FY' is the yield stress
        * 'E' is the Young's modulus
        * 'n' is the Ramberg-Osgood parameter
        
        The formula can be applied in compression and is 'Et=f/(f/Ec+0.002nc(f/(Fcy))^(nc))'
        where:
        * 'Fcy' is the compressive yield stress
        * 'Ec' is the compressive Young's modulus
        * 'nc' is the compressive Ramberg-Osgood parameter
        
        Input
        E Young's modulus
        n Ramberg-Osgood parameter
        Fy Yield stress
        sigma Stress
        Output
        Et Tangent modulus
        
        Signature ``TangentModulus(e, n, iFy, sigma)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param iFy:  Yield stress  
        :type iFy: float 
        :param sigma:  Stress  
        :type sigma: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, oEt). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. oEt is a float.   Tangent modulus 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsAllowable(self, allowable: float, value: 'list[float]') -> tuple:
        """
        MS allowable.  
        
        Computes margin of safety based on an allowable
        
        The formula is MS = Allowable / Value - 1
        
        where:
        * 'Allowable' is the manual input
        * 'Value' is the value coming from load extractor
        * 'MS' is the margin of safety
        
        Input
        Allowable Manual input
        Value(nblc) Value coming from load extractor
        Output
        MS(nblc) Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsAllowable(allowable, value)`` 
        
        :param allowable:  Manual input  
        :type allowable: float 
        :param value:  Value coming from load extractor  
        :type value: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsBearing(self, iFbr: float, d: float, t: float, factor: float, iPy: 'list[float]', iPz: 'list[float]') -> tuple:
        """
        MS bearing
        Computes margin of bearing
        
        The formula is 'MS = PBearingAllowable / P - 1'
        
        where 
        * 'PBearingAllowable' is the bearing load allowable ('PBearingAllowable = Fbr * D * t')
        'Fbr' is the bearing stress allowable
        'D' is the d iameter
        't' is the thickness
        * 'P' is the bearing load (P = FactorLoad * PExtracted)
        'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
        'PExtracted' is the extracted load ('PExtracted = sqrt( Py ^ 2 + Pz ^ 2 )')
        'Py' is the shear load in Y direction
        'Pz' is the shear load in Z direction
        
        Input
        Fbr        Bearing stress allowable
        D        Diameter
        t        Thickness
        Factor    Load factor
        Py        Shear load Y direction
        Pz        Shear load Z direction
        Output
        MS        Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsBearing(iFbr, d, t, factor, iPy, iPz)`` 
        
        :param iFbr:  Bearing stress allowable  
        :type iFbr: float 
        :param d:  Diameter  
        :type d: float 
        :param t:  Thickness  
        :type t: float 
        :param factor:  Load factor  
        :type factor: float 
        :param iPy:  Shear load Y direction  
        :type iPy: list of float 
        :param iPz:  Shear load Z direction  
        :type iPz: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsBoltBending(self, iMba: float, b: float, factor: float, iPy: 'list[float]', iPz: 'list[float]') -> tuple:
        """
        MS bolt bending
        Computes margin of safety of a bolt under bending load
        
        The formula is 'MS = MBendingAllowable / M - 1'
        
        where 
        * 'MBendingAllowable' is the bending moment allowable of the bolt.
        * 'M' is the bending moment applied to the bolt. ('M = b * P')
        where:
        'b' is the arm
        'P' is the load ('P = FactorLoad * PExtracted')
        'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
        'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
        'Py' is the shear load in Y direction
        'Pz' is the shear load in Z direction
        Input
        Mba       Bending moment allowable of bolt
        b         Arm
        Factor    Load factor
        Py        Shear load Y direction
        Pz        Shear load Z direction
        Output
        MS        Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsBoltBending(iMba, b, factor, iPy, iPz)`` 
        
        :param iMba:  Bending moment allowable of bolt  
        :type iMba: float 
        :param b:  Arm  
        :type b: float 
        :param factor:  Load factor  
        :type factor: float 
        :param iPy:  Shear load Y direction  
        :type iPy: list of float 
        :param iPz:  Shear load Z direction  
        :type iPz: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsBoltCombinedShearTension(self, iPTensileAllowable: float, iPTensileX: 'list[float]', iPShearAllowable: float, factor: float, iPy: 'list[float]', iPz: 'list[float]') -> tuple:
        """
        MS bolt combined shear tension
        Computes margin of safety of a bolt under shear load and tension load
        
        The formula is 'MS = 1 / sqrt( Rt ^ 2 + Rs ^ 3 )  - 1'
        where
        * Rt = PTensileX/PTensileAllowable
        * Rs = PShear/PShearAllowable
        *'PTensileAllowable' is the tensile load allowable of the bolt
        * 'PTensileX' is the tensile load applied on the fastener
        * 'PShearAllowable' is the single shear load allowable of the bolt
        * 'Pshear' is the shearing load applied through the shear area. PShear = FactorLoad * PExtracted
        * 'FactorLoad' is the ratio of load between extracted load PExtracted and PShear
        * 'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
        * 'Py' is the shear load in Y direction
        * 'Pz' is the shear load in Z direction
        
        Input
        nblc                Number of loadcases
        PTensileAllowable   Tensile load allowable
        PTensileX(nblc)     Tensile load
        PShearAllowable     Single shear load allowable
        Factor              Load factor
        Py(nblc)            Shear load Y direction
        Pz(nblc)            Shear load Z direction
        Output
        MS                  Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsBoltCombinedShearTension(iPTensileAllowable, iPTensileX, iPShearAllowable, factor, iPy, iPz)`` 
        
        :param iPTensileAllowable:  Tensile load allowable  
        :type iPTensileAllowable: float 
        :param iPTensileX:  Tensile load  
        :type iPTensileX: list of float 
        :param iPShearAllowable:  Single shear load allowable  
        :type iPShearAllowable: float 
        :param factor:  Load factor  
        :type factor: float 
        :param iPy:  Shear load Y direction  
        :type iPy: list of float 
        :param iPz:  Shear load Z direction  
        :type iPz: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsBoltCombinedShearTensionBending(self, iPTensileAllowable: float, iPTensileX: 'list[float]', iMAllowable: float, b: float, factorBend: float, iPyBend: 'list[float]', iPzBend: 'list[float]', iPShearAllowable: float, factorShear: float, iPyShear: 'list[float]', iPzShear: 'list[float]') -> tuple:
        """
        MS bolt combined shear tension bending
        Computes margin of safety of a bolt under shear, tension and bending load
        
        The formula is MS = 1 / sqrt ( ( Rt + Rb ) ^ 2 + Rs ^ 3 ) - 1
        where
        * Rt = PTensileX / PTensileAllowable
        * Rb = M / MAllowable
        * Rs = PShear / PShearAllowable
        
        Tensile data
        * 'PTensileAllowable' is the tensile load allowable of the bolt
        * 'PTensileX' is the tensile load applied on the fastener
        
        Bending data
        * 'MAllowable' is the bending moment allowable of the bolt
        * 'M' is the bending moment applied to the bolt. 
        M = b * PBend
        PBend = FactorLoadBend * sqrt(PyBend^2 + PzBend^2)
        * 'b' is the arm
        * 'FactorLoadBend' is the load factor for bending
        * 'PyBend' is the bending load in Y direction
        * 'PzBend' is the shear load in Z direction
        
        Shear data
        * 'PShearAllowable' is the single shear load allowable of the bolt
        * 'PShear' is the shearing load applied through the shear area.
        PShear = FactorLoadShear * sqrt(PyShear^2 + PzShear^2)
        * 'FactorLoadShear' is the load factor for shearing
        * 'PyShear' is the shear load in Y direction
        * 'PzShear' is the shear load in Z direction
        
        Input
        nblc                 Number of loadcases
        PTensileAllowable    Tensile load allowable
        PTensileX(nblc)      Tensile load
        
        MAllowable           Bending moment allowable of bolt
        b                    Arm
        FactorBend           Load factor for bending
        PyBend(nblc)         Bending load Y direction
        PzBend(nblc)         Bending load Z direction
        
        PShearAllowable      Single shear load allowable
        FactorShear          Load factor for shear
        PyShear(nblc)        Shear load Y direction
        PzShear(nblc)        Shear load Z direction
        Output
        MS                   Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsBoltCombinedShearTensionBending(iPTensileAllowable, iPTensileX, iMAllowable, b, factorBend, iPyBend, iPzBend, iPShearAllowable, factorShear, iPyShear, iPzShear)`` 
        
        :param iPTensileAllowable:  Tensile load allowable  
        :type iPTensileAllowable: float 
        :param iPTensileX:  Tensile load  
        :type iPTensileX: list of float 
        :param iMAllowable:  Bending moment allowable of bolt  
        :type iMAllowable: float 
        :param b:  Arm  
        :type b: float 
        :param factorBend:  Bending load factor  
        :type factorBend: float 
        :param iPyBend:  Bending load Y direction  
        :type iPyBend: list of float 
        :param iPzBend:  Bending load Z direction  
        :type iPzBend: list of float 
        :param iPShearAllowable:  Single shear load allowable  
        :type iPShearAllowable: float 
        :param factorShear:  Shear load factor  
        :type factorShear: float 
        :param iPyShear:  Shear load Y direction  
        :type iPyShear: list of float 
        :param iPzShear:  Shear load Z direction  
        :type iPzShear: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsBoltShear(self, iPShearAllowable: float, factor: float, iPy: 'list[float]', iPz: 'list[float]') -> tuple:
        """
        MS bolt shear
        Computes margin of safety of a bolt under shear load
        
        The formula is MS = PShearAllowable / P  - 1
        where
        * 'PShearAllowable' is the single shear load allowable of the bolt
        * 'P' is the shearing load applied through the shear area. P = FactorLoad * PExtracted
        * 'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
        * 'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
        * 'Py' is the shear load in Y direction
        * 'Pz' is the shear load in Z direction
        
        Input
        nblc                Number of loadcases    
        PShearAllowable     Single shear load allowable
        Factor              Load factor
        Py(nblc)            Shear load Y direction
        Pz(nblc)            Shear load Z direction
        Output
        MS                  Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsBoltShear(iPShearAllowable, factor, iPy, iPz)`` 
        
        :param iPShearAllowable:  Single shear load allowable  
        :type iPShearAllowable: float 
        :param factor:  Shear load factor  
        :type factor: float 
        :param iPy:  Shear load Y direction  
        :type iPy: list of float 
        :param iPz:  Shear load Z direction  
        :type iPz: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsNetSection(self, sigmaAllowable: float, d: float, t: float, b: float, factor: float, iPExtracted: 'list[float]') -> tuple:
        """
        MS Net section
        Computes margin of net section (due to bolt hole)
        
        The formula is MS = PNetSectionAllowable / P - 1
        
        where:
        * 'PNetSectionAllowable' is the net section load allowable. 
        PNetSectionAllowable = SigmaAllowable * t * ( b - D )
        * 'SigmaAllowable' is the material stress allowable. For instance, it could be Ftu
        * 'D'    is the hole diameter
        * 't' is the thickness
        * 'b' is the width of the net section
        
        * 'P' is the load. 
        P = FactorLoad * PExtracted
        * 'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
        * 'PExtracted' is the extracted load
        
        * 'MS' is the margin of safety
        
        Input
        SigmaAllowable        Material stress allowable
        D                     Diameter
        t                     Thickness
        b                     Width
        Factor                Load factor
        PExtracted(nblc)      Axial load (extracted)
        Output
        MS Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsNetSection(sigmaAllowable, d, t, b, factor, iPExtracted)`` 
        
        :param sigmaAllowable:  Material stress allowable  
        :type sigmaAllowable: float 
        :param d:  Diameter  
        :type d: float 
        :param t:  Thickness  
        :type t: float 
        :param b:  Width  
        :type b: float 
        :param factor:  Load factor  
        :type factor: float 
        :param iPExtracted:  Axial load (extracted)  
        :type iPExtracted: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsShearTearOut(self, tauAllowable: float, d: float, t: float, b: float, factor: float, iPExtracted: 'list[float]') -> tuple:
        """
        MS Shear Tear Out
        Computes margin of shear tear out (due to bolt hole)
        
        The formula is MS = PShearTearOutAllowable / P  - 1
        * 'PShearTearOutAllowable' is the shear tear out load allowable. PShearTearOutAllowable = tauAllowable * 2 * t * ( b - D / 2 )
        * 'tauAllowable' is the material shear stress allowable. For instance, it could be Fsu.
        * 'D' is the hole diameter
        * 't' is the thickness
        * 'b' is the distance from hole center to edge of the plate
        * 'P' is the axial load. P = FactorLoad * PExtracted
        * FactorLoad is the ratio of load between extracted load 'PExtracted' and 'P'
        * PExtracted is the extracted load.
        
        Input
        tauAllowable        Material shear stress allowable 
        D                   Diameter
        t                   Thickness
        b                   Edge distance
        Factor              Load factor
        nblc                Number of loadcases
        PExtracted(nblc)    Axial load (extracted)
        Output
        MS        Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsShearTearOut(tauAllowable, d, t, b, factor, iPExtracted)`` 
        
        :param tauAllowable:  Material shear stress allowable   
        :type tauAllowable: float 
        :param d:  Diameter  
        :type d: float 
        :param t:  Thickness  
        :type t: float 
        :param b:  Edge distance  
        :type b: float 
        :param factor:  Load factor  
        :type factor: float 
        :param iPExtracted:  Axial load (extracted)  
        :type iPExtracted: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsTsaiHillPlaneStress(self, matFcL: float, matFcLT: float, matFtL: float, matFtLT: float, matFS: float, fl: 'list[float]', flt: 'list[float]', fs: 'list[float]') -> tuple:
        """
        MS Tsai-Hill
        Computes margin of safety on the basis of Tsai-Hill failure theory (plane stresses hypothesis)
        
        The formula based on yield material allowables is 'MS=1-sqrt(((F_L)/FtcyL)^2+(FLT/FtcyLT)^2-((F_LF_(LT))/(FtcyLFtcyL))+(F_(S)/Fsy)^2)'
        where:
        * L and LT are material directions: 'Longitudinal' and 'Longitudinal' 'Transverse'.
        * 'F_L','FLT' and 'FS' are plane stresses. They are expressed under material direction (with 'S' for shear).
        * 'F(tc)yL', 'F(tc)yLT' and 'Fsy' are yield material stress allowables. 'tc' is for 'tensile' or 'compressive' properties. Choices are done depending on the type of the corresponding stresses ('F_L' and 'FLT').
        
        The formula can also be based on failure material allowables. 
        The formula is 'MS = 1 - sqrt ( (FL / F(tc)uL ) ^ 2 + ( FLT / F(tc)uLT ) ^ 2 - ( (FL * FLT) / ( F(tc)uL * F(tc)uL) ) + ( FS / Fsu ) ^ 2 )'
        
        where:
        * 'F(tc)uL','F(tc)uLT' and 'Fsu' are ultimate material stress allowables.
        
        Input
        Mat_FcL Material compressive stress, longitudinal direction
        Mat_FcLT Material compressive stress, long transverse direction
        Mat_FtL Material tensile stress, longitudinal direction
        Mat_FtLT Material tensile stress, long transverse direction
        Mat_FS Material shear stress
        nblc Number of load cases
        FL Stress(es), longitudinal direction
        FLT Stress(es), longitudinal transverse direction
        FS Shear stress(es)
        Output
        MS Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsTsaiHillPlaneStress(matFcL, matFcLT, matFtL, matFtLT, matFS, fl, flt, fs)`` 
        
        :param matFcL:  Material compressive allowable, longitudinal direction  
        :type matFcL: float 
        :param matFcLT:  Material compressive allowable, long transverse direction  
        :type matFcLT: float 
        :param matFtL:  Material tensile allowable, longitudinal direction  
        :type matFtL: float 
        :param matFtLT:  Material tensile allowable, long transverse direction  
        :type matFtLT: float 
        :param matFS:  Material shear allowable  
        :type matFS: float 
        :param fl:  Stresses, longitudinal direction  
        :type fl: list of float 
        :param flt:  Stresses, longitudinal transverse direction  
        :type flt: list of float 
        :param fs:  Shear stresses  
        :type fs: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsTrescaPlaneStress(self, fs: float, fx: 'list[float]', fy: 'list[float]', fxy: 'list[float]') -> tuple:
        """
        MS Tresca.  
        
        Computes margin of safety based on Tresca yield criterion under plane stress condition
        
        The yield criteria of isotropic materials limit the elastic domain during loading.
        According to the Tresca criterion, yield failure is expected when the greatest shear stress reaches the shear strength of the material.
        Thus, the maximum shear stress yield criterion can be specified as
        'max((|S1-S2|)/2 , (|S1-S3|)/2, (|S2-S3|)/2) &lt;= (FS)/2'
        where
        * 'S1', 'S2' and 'S3' are the principal stresses.
        * 'FS' is the material shear strength allowable
        
        A margin of safety can be derived from this formulation:
        'MS = (FS) / (max(|S1-S2| , |S1-S3|, |S2-S3|)) - 1'
        that must be greater than 0.
        
        In a plane stress configuration, principal stresses are computed as
        'S1 = (FX + FY)/2 + sqrt(((FX-FY)/2)^2 + FXY^2)'
        'S2 = (FX + FY)/2 - sqrt(((FX-FY)/2)^2 + FXY^2)'
        where
        * 'FX' the normal stress in the X direction
        * 'FY' the normal stress in the Y direction
        * 'FXY' the shearing stress
        
        Input
        FS Material shear strength allowable
        nblc Number of load cases
        FX Normal stress in the X direction
        FY Normal stress in the Z direction
        FXY Shear stress                    
        Output    
        MS Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsTrescaPlaneStress(fs, fx, fy, fxy)`` 
        
        :param fs:  Material shear strength allowable  
        :type fs: float 
        :param fx:  Normal stress in the X direction  
        :type fx: list of float 
        :param fy:  Normal stress in the Z direction  
        :type fy: list of float 
        :param fxy:  Shear stress  
        :type fxy: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsMaterialStressAllowable(self, allowable: float, sigma: 'list[float]') -> tuple:
        """
        MS material stress allowable.  
        
        Computes margin of safety based on a material allowable
        
        The formula is MS = StressAllowable / Stress - 1
        
        where:
        * 'Allowable' is the material stress allowable
        * 'Stress' is the stress
        * 'MS' is the margin of safety
        
        Input
        Allowable Material stress allowable
        sigma(nblc) Stress
        Output
        MS Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsMaterialStressAllowable(allowable, sigma)`` 
        
        :param allowable:  Material stress allowable  
        :type allowable: float 
        :param sigma:  Stress  
        :type sigma: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsPlateBuckling(self, e: float, nu: float, b: float, t: float, k: float, eta: float, sigma: 'list[float]') -> tuple:
        """
        MS Plate Buckling
        Computes margin of safety of a metallic plate under buckling load (generic formula)
        
        The formula is MS = Allowable / Stress - 1
        
        where:
        * 'Allowable' is the compressive buckling stress allowable
        * 'Stress' is the stress
        * 'MS' is the margin of safety
        
        Allowable = eta * PI^2*k*E/(12*(1-nu^2)) * (t/b)^2
        where
        * 'k' is the buckling coefficient
        * 'E' is the Young modulus
        * 'nu' is the elastic Poisson coefficient
        * 't' is the panel thickness
        * 'b' is the panel dimension
        * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
        
        Input
        E        Young modulus
        nu        Elastic Poisson coefficient
        b        Panel dimension
        t        Panel thickness
        k        Buckling coefficient
        eta        Plasticity reduction factor
        nblc    Number of load cases
        sigma    Stress coming from load extraction
        Output
        MS Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsPlateBuckling(e, nu, b, t, k, eta, sigma)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param nu:  Elastic Poisson coefficient  
        :type nu: float 
        :param b:  Panel dimension  
        :type b: float 
        :param t:  Panel thickness  
        :type t: float 
        :param k:  Buckling coefficient  
        :type k: float 
        :param eta:  Plasticity reduction factor  
        :type eta: float 
        :param sigma:  Stress coming from load extraction  
        :type sigma: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsPlateBucklingCurvedCompressive(self, e: float, nu: float, n: float, a: float, b: float, t: float, r: float, behaviour: ABBMaterialBehaviour, sigma: 'list[float]') -> tuple:
        """
        MS Plate Buckling Curved Compressive
        Computes margin of safety of a curved metallic rectangular panel under compressive load
        
        The formula is MS = Allowable / |Stress| - 1
        
        where:
        * 'Allowable' is the compressive buckling stress allowable
        * 'Stress' is the compressive stress (MS is not calculated in case of tensile stress),
        * 'MS' is the margin of safety
        
        Allowable = eta * PI^2*kc*E/(12*(1-nu^2)) * (t/c)^2
        where
        * 'kc' is the buckling coefficient
        * 'E' is the Young modulus
        * 'nu' is the elastic Poisson coefficient
        * 't' is the panel thickness
        * 'c' is the shorter panel dimension c = min(a,b)
        * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
        * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
        * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
        
        SigmaAllowablePlastic/Sigma0.7 = f(SigmaAllowableElastic/Sigma0.7)
        
        MetallicPanelCompressivePlasticityCurveBC3 with Sigma0.7 is the stress for secant modulus equal to 70% of Young modulus
        Input
        E            Young modulus
        nu            Elastic Poisson coefficient
        n            Ramberg-Osgood parameter
        a            Unloaded edge length
        b            Loaded edge length
        t            Panel thickness
        r            Panel radius of curvature
        behaviour     Material behaviour
        nblc        Number of load cases
        sigma        Stress coming from load extraction
        Output
        sigmaAllowable         Stress allowable
        MS                     Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsPlateBucklingCurvedCompressive(e, nu, n, a, b, t, r, behaviour, sigma)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param nu:  Elastic Poisson coefficient  
        :type nu: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param a:  Unloaded edge length  
        :type a: float 
        :param b:  Loaded edge length  
        :type b: float 
        :param t:  Panel thickness  
        :type t: float 
        :param r:  Panel radius of curvature  
        :type r: float 
        :param behaviour:  Material behaviour  
        :type behaviour: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBMaterialBehaviour` 
        :param sigma:  Stress coming from load extraction  
        :type sigma: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms, sigmaAllowable). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety sigmaAllowable is a float.   Stress allowable 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsPlateBucklingCurvedShear(self, e: float, nu: float, n: float, a: float, b: float, t: float, bc: ABBEdgeSupportType, r: float, behaviour: ABBMaterialBehaviour, sigma: 'list[float]') -> tuple:
        """
        MS Plate Buckling Curved Shear
        Computes margin of safety of a curved metallic rectangular panel under shear load
        
        The formula is MS = Allowable / |Stress| - 1
        
        where:
        * 'Allowable' is the compressive buckling stress allowable
        * 'Stress' is the compressive stress (MS is not calculated in case of tensile stress),
        * 'MS' is the margin of safety
        
        Allowable = eta * PI^2*ks*E/(12*(1-nu^2)) * (t/c)^2
        where
        * 'ks' is the buckling coefficient
        * 'E' is the Young modulus
        * 'nu' is the elastic Poisson coefficient
        * 't' is the panel thickness
        * 'c' is the shorter panel dimension c = min(a,b)
        * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
        * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
        * eta is obtained from the MetallicPanelCompressivePlasticityCurveBC1 charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
        * SigmaAllowablePlastic/Sigma0.7 = f(SigmaAllowableElastic/Sigma0.7)                
        * Sigma0.7 is the stress for secant modulus equal to 70% of Young modulus
        
        Input
        E            Young modulus
        nu           Elastic Poisson coefficient
        n            Ramberg-Osgood parameter
        a            Longer panel dimension
        b            Shorter panel dimension
        t            Panel thickness
        BC           Type of support along edges 
        r            Panel radius of curvature
        behaviour    Material behaviour
        nblc         Number of load cases
        sigma        Stress coming from load extraction
        Output
        sigmaAllowable         Stress allowable
        MS                     Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsPlateBucklingCurvedShear(e, nu, n, a, b, t, bc, r, behaviour, sigma)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param nu:  Elastic Poisson coefficient  
        :type nu: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param a:  Longer panel dimension  
        :type a: float 
        :param b:  Shorter panel dimension  
        :type b: float 
        :param t:  Panel thickness  
        :type t: float 
        :param bc:  Type of support along the edges  
        :type bc: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType` 
        :param r:  Panel radius of curvature  
        :type r: float 
        :param behaviour:  Material behaviour  
        :type behaviour: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBMaterialBehaviour` 
        :param sigma:  Stress coming from load extraction  
        :type sigma: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms, sigmaAllowable). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety sigmaAllowable is a float.   Stress allowable 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsPlateBucklingCurvedLongitudinalShearCombined(self, e: float, nu: float, n: float, a: float, b: float, t: float, bc: ABBEdgeSupportType, r: float, behaviour: ABBMaterialBehaviour, sigma: 'list[float]', tau: 'list[float]') -> tuple:
        """
        MS Plate Buckling Curved Longitudinal Shear Combined
        Computes margin of safety of a rectangular curved metallic panel in buckling under combined shear and longitudinal loads
        
        Under compressive loads
        
        Under compressive and shear loads, the interaction equation is:
        RL^2 + RS^2 = 1.0
        
        The Margin Safety is given by the following formula:
        
        MS=2/(RL+sqrt(RL^2+4*RS^2))-1
        where:
        
        * RL = sigma / sigma_cr is the stress ratio due to longitudinal stress, with:
        * sigma is the given longitudinal stress
        * sigma_cr is the compression stress allowable for buckling (sigma_cr &lt; 0, as consequence RL &lt; 0 in tension)
        
        * RS = tau / tau_cr is the stress ratio due to shear stress with:
        * tau is the given shear stress
        * tau_cr is the shear stress allowable for buckling (tau and tau_cr always positive)
        
        Under tensile loads
        
        Under tensile and shear loads, the interaction equation is:
        1/2 * RL + RS = 1.0
        
        The Margin Safety is given by the following formula:
        MS = (2 - RL) / ( 2 * RS ) - 1
        
        The panel edges are either clamped or simply supported.
        Plasticity is not taken into account.
        
        Input
        E            Young modulus
        nu           Elastic Poisson coefficient
        n            Ramberg-Osgood parameter
        a            Unloaded edge length
        b            Loaded edge length
        t            Panel thickness
        BC           Type of support along edges ('Clamped' or 'Simply Supported')
        r            Panel radius of curvature
        behaviour    Material behaviour ('Elastic' or 'Elastic-Plastic')
        nblc         Number of load cases
        sigma        Stress XX coming from load extraction
        tau          Stress YY coming from load extraction
        Output
        MS           Margin of safety
        sigmacr      Compressive stress allowable
        taucr        Shear stress allowable
        
        Return
        Status of the calculation
        
        Signature ``MsPlateBucklingCurvedLongitudinalShearCombined(e, nu, n, a, b, t, bc, r, behaviour, sigma, tau)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param nu:  Elastic Poisson coefficient  
        :type nu: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param a:  Unloaded edge length  
        :type a: float 
        :param b:  Loaded edge length  
        :type b: float 
        :param t:  Panel thickness  
        :type t: float 
        :param bc:  Type of support along the edges  
        :type bc: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType` 
        :param r:  Panel radius of curvature  
        :type r: float 
        :param behaviour:  Material behaviour  
        :type behaviour: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBMaterialBehaviour` 
        :param sigma:  Stress XX coming from load extraction  
        :type sigma: list of float 
        :param tau:  Stress YY coming from load extraction  
        :type tau: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms, sigmacr, taucr). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety sigmacr is a float.   Compressive stress allowable taucr is a float.   Shear stress allowable 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsPlateBucklingFlatBending(self, e: float, nu: float, n: float, a: float, b: float, beta: float, t: float, behaviour: ABBMaterialBehaviour, sigma1: 'list[float]', sigma2: 'list[float]') -> tuple:
        """
        MS Plate Buckling Flat Bending
        Computes margin of safety of a flat metallic rectangular panel under bending load
        
        The formula is MS = sigmaAllowable / abs(sigma) - 1
        
        where:
        * 'sigmaAllowable' is the bending buckling stress allowable
        * 'sigma' is the compressive stress at one edge of the panel, sigma = min( sigma1, sigma2 )
        * 'MS' is the margin of safety
        
        Allowable = eta * PI^2*kb*E/(12*(1-nu^2)) * (t/b)^2
        where
        * 'kb' is the bending buckling stress coefficient
        * 'E' is the Young's modulus
        * 'nu' is the elastic Poisson coefficient
        * 't' is the panel thickness
        * 'a' is the unloaded edge length
        * 'b' is the loaded edge length
        * 'beta' Loading length ratio,  the factor which, divided by b, gives the edge length in compression (while the remaining edge length is in tension).
        * 'beta' is calculated on the basis of sigma1 and sigma2 with an hypothesis of linear behaviour with the formula:
        * beta = (fc - ft) / fc where fc = min(sigma1, sigma2) and ft = max(sigma1, sigma2) )
        * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
        * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
        * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
        
        SigmaAllowablePlastic/Sigma0.7 = f(SigmaAllowableElastic/Sigma0.7)
        
        MetallicPanelCompressivePlasticityCurveBC2 with Sigma0.7 is the stress for secant modulus equal to 70% of Young modulus
        Input
        E            Young's modulus
        nu           Elastic Poisson coefficient
        n            Ramberg-Osgood parameter
        a            Unloaded edge length
        b            Loaded edge length
        beta         Loading length ratio. If not specified (beta = NA), beta is computed
        t            Panel thickness
        behaviour    Material behaviour
        nblc         Number of load cases
        sigma1       Stress XX Side1
        sigma2       Stress XX Side2
        Output
        sigmaAllowable         Stress allowable
        MS                     Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsPlateBucklingFlatBending(e, nu, n, a, b, beta, t, behaviour, sigma1, sigma2)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param nu:  Elastic Poisson coefficient  
        :type nu: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param a:  Unloaded edge length  
        :type a: float 
        :param b:  Loaded edge length  
        :type b: float 
        :param beta:  Loading length ratio  
        :type beta: float 
        :param t:  Panel thickness  
        :type t: float 
        :param behaviour:  Material behaviour  
        :type behaviour: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBMaterialBehaviour` 
        :param sigma1:  Stress XX Side1  
        :type sigma1: list of float 
        :param sigma2:  Stress XX Side2  
        :type sigma2: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms, sigmaAllowable). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety sigmaAllowable is a list of float.   Stress allowables 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsPlateBucklingFlatCompressive(self, e: float, nu: float, n: float, a: float, b: float, t: float, bcUnloaded: ABBUnloadedEdgeSupportType, bcLoaded: ABBEdgeSupportType, behaviour: ABBMaterialBehaviour, sigma: 'list[float]') -> tuple:
        """
        MS Plate Buckling Flat Compressive
        Computes margin of safety of a flat metallic rectangular panel under compressive load
        
        The formula is MS = sigmaAllowable / abs(sigma) - 1
        
        where:
        * 'sigmaAllowable' is the compressive buckling stress allowable,
        * 'sigma' is the compressive stress (MS is not calculated in case of tensile stress),
        * 'MS' is the margin of safety
        
        Allowable = eta * PI^2*kc*E/(12*(1-nu^2)) * (t/b)^2
        where
        * 'kc' is the bending buckling stress coefficient
        * 'E' is the Young's modulus
        * 'nu' is the elastic Poisson coefficient
        * 't' is the panel thickness
        * 'a' is the unloaded edge length
        * 'b' is the loaded edge length                
        * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
        * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
        * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
        
        SigmaAllowablePlastic/Sigma0.7 = f(SigmaAllowableElastic/Sigma0.7)
        MetallicPanelCompressivePlasticityCurveBC1 if the Boundary Condition for the unloaded edges is Simply Supported-Free,
        MetallicPanelCompressivePlasticityCurveBC2 if the boundary condition for the unloaded edges is different of Simply Supported-Free
        
        Input
        E            Young's modulus
        nu           Elastic Poisson coefficient
        n            Ramberg-Osgood parameter
        a            Unloaded edge length
        b            Loaded edge length
        t            Panel thickness        
        BC_Unloaded  Type of support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
        BC_Loaded    Type of support along loaded edges {'Clamped';'Simply Supported'}
        behaviour    Material behaviour
        nblc         Number of load cases
        sigma        Stress coming from load extractor
        Output
        sigmaAllowable         Stress allowable
        MS                     Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsPlateBucklingFlatCompressive(e, nu, n, a, b, t, bcUnloaded, bcLoaded, behaviour, sigma)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param nu:  Elastic Poisson coefficient  
        :type nu: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param a:  Unloaded edge length  
        :type a: float 
        :param b:  Loaded edge length  
        :type b: float 
        :param t:  Panel thickness  
        :type t: float 
        :param bcUnloaded:  Type of support along unloaded edges  
        :type bcUnloaded: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBUnloadedEdgeSupportType` 
        :param bcLoaded:  Type of support along loaded edges  
        :type bcLoaded: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType` 
        :param behaviour:  Material behaviour  
        :type behaviour: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBMaterialBehaviour` 
        :param sigma:  Stress coming from load extractor  
        :type sigma: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms, sigmaAllowable). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety sigmaAllowable is a float.   Stress allowable 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsPlateBucklingFlatShear(self, e: float, nu: float, n: float, a: float, b: float, t: float, bc: ABBEdgeSupportType, behaviour: ABBMaterialBehaviour, sigma: 'list[float]') -> tuple:
        """
        MS Plate Buckling Flat Shear
        Computes margin of safety of a flat metallic rectangular panel under shear load
        
        The formula is MS = sigmaAllowable / abs(sigma) - 1
        
        where:
        * 'sigmaAllowable' is the shear buckling stress allowable,
        * 'sigma' is the compressive stress (MS is not calculated in case of tensile stress),
        * 'MS' is the margin of safety
        
        Allowable = eta * PI^2*ks*E/(12*(1-nu^2)) * (t/b)^2
        where
        * 'ks' is the bending buckling stress coefficient
        * 'E' is the Young's modulus
        * 'nu' is the elastic Poisson coefficient
        * 't' is the panel thickness
        * 'a' is the panel longer dimension
        * 'b' is panel shorter dimension
        * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
        * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
        * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
        
        SigmaAllowablePlastic/Sigma0.7 = f(SigmaAllowableElastic/Sigma0.7)
        MetallicPanelCompressivePlasticityCurveBC1, Warning: in fact graph is fig C5.13 but it is C5.7 graph divided by 2
        
        Input
        E            Young's modulus
        nu           Elastic Poisson coefficient
        n            Ramberg-Osgood parameter
        a            Panel longer dimension
        b            Panel shorter dimension
        t            Panel thickness        
        BC           Type of support along the edges {'Clamped';'Simply Supported'}
        behaviour    Material behaviour
        nblc         Number of load cases
        sigma        Stress coming from load extractor
        Output
        sigmaAllowable         Stress allowable
        MS                     Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsPlateBucklingFlatShear(e, nu, n, a, b, t, bc, behaviour, sigma)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param nu:  Elastic Poisson coefficient  
        :type nu: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param a:  Unloaded edge length  
        :type a: float 
        :param b:  Loaded edge length  
        :type b: float 
        :param t:  Panel thickness  
        :type t: float 
        :param bc:  Type of support along the edges  
        :type bc: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType` 
        :param behaviour:  Material behaviour  
        :type behaviour: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBMaterialBehaviour` 
        :param sigma:  Stress coming from load extractor  
        :type sigma: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms, sigmaAllowable). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety sigmaAllowable is a float.   Stress allowable 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsPlateBucklingFlatLongitudinalBendingCombined(self, e: float, nu: float, n: float, a: float, b: float, t: float, bcUnloaded: ABBUnloadedEdgeSupportType, bcLoaded: ABBEdgeSupportType, behaviour: ABBMaterialBehaviour, sigma1: 'list[float]', sigma2: 'list[float]') -> tuple:
        """
        MS Plate Buckling Flat Longitudinal Bending Combined
        Computes margin of safety of a rectangular flat metallic panel in buckling under combined bending and longitudinal loads
        
        This formula is derived from the interaction equation 
        Rb ^ 1.75 + Rc = 1.0
        
        where:
        * Rc = sigmac / sigmacr is the stress ratio due to compression stress, with:
        * sigmac is the given longitudinal stress
        * sigmacr  is the compression stress allowable for buckling
        
        * Rb = sigmab / sigmabcr is the stress ratio due to bending stress with
        * sigmab is the given compressive stress due to bending
        * sigmabcr  is the bending stress allowable for buckling
        
        Input
        E            Young's modulus
        nu           Elastic Poisson coefficient
        n            Ramberg-Osgood parameter
        a            Unloaded edge length
        b            Loaded edge length
        beta         Loading length ratio
        t            Panel thickness        
        BC_Unloaded  Type of support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
        BC_Loaded    Type of support along loaded edges {'Clamped';'Simply Supported'}
        behaviour    Material behaviour
        nblc         Number of load cases
        sigma1       Stress XX Side1
        sigma2       Stress XX Side2
        Output
        sigmacr      Compressive stress allowable
        sigmabcr     Bending stress allowable
        MS           Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsPlateBucklingFlatLongitudinalBendingCombined(e, nu, n, a, b, t, bcUnloaded, bcLoaded, behaviour, sigma1, sigma2)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param nu:  Elastic Poisson coefficient  
        :type nu: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param a:  Unloaded edge length  
        :type a: float 
        :param b:  Loaded edge length  
        :type b: float 
        :param t:  Panel thickness  
        :type t: float 
        :param bcUnloaded:  Type of support along unloaded edges  
        :type bcUnloaded: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBUnloadedEdgeSupportType` 
        :param bcLoaded:  Type of support along loaded edges  
        :type bcLoaded: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType` 
        :param behaviour:  Material behaviour  
        :type behaviour: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBMaterialBehaviour` 
        :param sigma1:  Stress XX Side1  
        :type sigma1: list of float 
        :param sigma2:  Stress XX Side2  
        :type sigma2: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms, sigmacr, sigmabcr). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety sigmacr is a float.   Compressive stress allowable sigmabcr is a float.   Bending stress allowable 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsPlateBucklingFlatLongitudinalShearCombined(self, e: float, nu: float, n: float, a: float, b: float, t: float, bcUnloaded: ABBUnloadedEdgeSupportType, bcLoaded: ABBEdgeSupportType, behaviour: ABBMaterialBehaviour, sigma: 'list[float]', tau: 'list[float]') -> tuple:
        """
        MS Plate Buckling Flat Longitudinal Shear Combined
        Computes margin of safety of a rectangular flat metallic panel in buckling under combined shear and longitudinal loads
        
        Under longitudinal and shear loads, the interaction equation is:
        MS=2/(RL + sqrt(RL ^ 2 + 4 * RS ^ 2)
        
        This formula is derived from the interaction equation RL+R2S=1.0
        RL + RS ^ 2 = 1.0
        
        where:
        * RL = sigma / sigmacr is the stress ratio due to longitudinal stress, with:
        * sigma is the given longitudinal stress
        * sigmacr is the compression stress allowable for buckling (sigmacr &lt; 0, as consequence RL &lt; 0 in tension)
        * RS = tau / taucr is the stress ratio due to shear stress with
        * tau is the given shear stress
        * taucr is the shear stress allowable for buckling (taucr and tau always positive)
        
        The panel edges are either clamped or simply supported.
        
        Input
        E            Young's modulus
        nu           Elastic Poisson coefficient
        n            Ramberg-Osgood parameter
        a            Unloaded edge length
        b            Loaded edge length
        t            Panel thickness        
        BC_Unloaded  Type of support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
        BC_Loaded    Type of support along loaded edges {'Clamped';'Simply Supported'}
        behaviour    Material behaviour {'Elastic'; 'Elastic-Plastic'}
        nblc         Number of load cases
        sigma        Stress XX
        tau          Stress XY
        Output
        sigmacr         Compressive stress allowable
        taucr           Shear stress allowable
        MS              Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsPlateBucklingFlatLongitudinalShearCombined(e, nu, n, a, b, t, bcUnloaded, bcLoaded, behaviour, sigma, tau)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param nu:  Elastic Poisson coefficient  
        :type nu: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param a:  Unloaded edge length  
        :type a: float 
        :param b:  Loaded edge length  
        :type b: float 
        :param t:  Panel thickness  
        :type t: float 
        :param bcUnloaded:  Type of support along unloaded edges  
        :type bcUnloaded: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBUnloadedEdgeSupportType` 
        :param bcLoaded:  Type of support along loaded edges  
        :type bcLoaded: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType` 
        :param behaviour:  Material behaviour  
        :type behaviour: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBMaterialBehaviour` 
        :param sigma:  Stress XX  
        :type sigma: list of float 
        :param tau:  Stress XY  
        :type tau: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms, sigmacr, taucr). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety sigmacr is a float.   Compressive stress allowable taucr is a float.   Shear stress allowable 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MsPlateBucklingFlatShearBendingCombined(self, e: float, nu: float, n: float, a: float, b: float, t: float, bcUnloaded: ABBUnloadedEdgeSupportType, bcLoaded: ABBEdgeSupportType, behaviour: ABBMaterialBehaviour, sigma1: 'list[float]', sigma2: 'list[float]', tau: 'list[float]') -> tuple:
        """
        MS Plate Buckling Flat Shear Bending Combined
        Computes margin of safety of a rectangular flat metallic panel in buckling under combined bending and shear loads
        
        Under longitudinal and shear loads, the interaction equation is:
        MS = 1 / sqrt(Rb ^ 2 + Rs ^ 2)
        
        This formula is derived from the interaction equation 
        Rb ^ 2 + Rs ^ 2 = 1.0
        
        where:
        * Rb = sigmab / sigmabcr  is the stress ratio due to bendoing stress with
        * sigmab is the given compressive stress due to bending
        * sigmabcr is the bending stress allowable for buckling 
        * Rs = tau / taucr is the stress ratio due to shear stress with
        * tau is the given shear stress
        * taucr is the shear stress allowable for buckling (taucr and tau always positive)
        
        Input
        E            Young's modulus
        nu           Elastic Poisson coefficient
        n            Ramberg-Osgood parameter
        a            Unloaded edge length
        b            Loaded edge length
        t            Panel thickness        
        BC_Unloaded  Type of support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
        BC_Loaded    Type of support along loaded edges {'Clamped';'Simply Supported'}
        behaviour    Material behaviour {'Elastic'; 'Elastic-Plastic'}
        nblc         Number of load cases
        sigma1       Stress XX Side1
        sigma2       Stress XX Side2
        tau          Stress XY
        Output
        taucr           Shear stress allowable that takes into account compressive/tensile stress
        sigmabcr        Bending stress allowable
        MS              Margin of safety
        Return
        Status of the calculation
        
        Signature ``MsPlateBucklingFlatShearBendingCombined(e, nu, n, a, b, t, bcUnloaded, bcLoaded, behaviour, sigma1, sigma2, tau)`` 
        
        :param e:  Young's modulus  
        :type e: float 
        :param nu:  Elastic Poisson coefficient  
        :type nu: float 
        :param n:  Ramberg-Osgood parameter  
        :type n: float 
        :param a:  Unloaded edge length  
        :type a: float 
        :param b:  Loaded edge length  
        :type b: float 
        :param t:  Panel thickness  
        :type t: float 
        :param bcUnloaded:  Type of support along unloaded edges  
        :type bcUnloaded: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBUnloadedEdgeSupportType` 
        :param bcLoaded:  Type of support along loaded edges  
        :type bcLoaded: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType` 
        :param behaviour:  Material behaviour  
        :type behaviour: :py:class:`NXOpen.CAE.AeroStructures.Author.ABBMaterialBehaviour` 
        :param sigma1:  Stress XX Side 1 
        :type sigma1: list of float 
        :param sigma2:  Stress XX Side 2 
        :type sigma2: list of float 
        :param tau:  Stress XY  
        :type tau: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, ms, sigmabcr, taucr). status is a :py:class:`NXOpen.CAE.AeroStructures.Author.ABBStatus`. ms is a list of float.   Margin of safety sigmabcr is a float.   Bending stress allowable taucr is a float.   Shear stress allowable 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    @staticmethod
    def GetABB():
        ...
    


class InputInteger(InputParameter):
    """
    Represents an integer input parameter  
    
    No support for KF
    
    .. versionadded:: NX12.0.0
    """
    Value: int = ...
    """
    Returns  the value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: InputInteger = ...  # unknown typename


