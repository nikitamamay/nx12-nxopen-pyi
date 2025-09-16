# module 'NXOpen.Fields'
#
# Automatically generated 2025-06-09T14:38:46.649631
#
"""Default documentation for NXOpen.Fields."""

import typing

import NXOpen
import NXOpen.CAE.Xyplot



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class PathObjects(NXOpen.SelectObjectList):
    """
    Contains objects that define a lattice path  
    
    Not a KF builder; see Fields.FieldManager methods to create a Fields.PathObjects.
    
    .. versionadded:: NX6.0.1
    """
    
    def ReverseDirection(self) -> None:
        """
        Reverses the order of the objects in the path 
        
        Signature ``ReverseDirection()`` 
        
        .. versionadded:: NX6.0.1
        
        License requirements: None.
        """
        ...
    
    
    def ReverseSectionDirection(self, index: int) -> None:
        """
        Reverses the order of the objects in the path 
        
        Signature ``ReverseSectionDirection(index)`` 
        
        :param index: 
        :type index: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def HandleLatestSelDirection(self) -> None:
        """
        Check the direction of the lastest selection and reverse it if necessary 
        
        Signature ``HandleLatestSelDirection()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: PathObjects = ...  # unknown typename


class IApplicationData(NXOpen.INXObject):
    """
    Interface for all application specific data to be registered on fields. Only one 
    application specific data object per IApplication can be added on a field. 
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class Field(NXOpen.DisplayableObject):
    """
    Represents an Field abstract class. 
    
    Fields represent a way of defining a function for one or more dependent 
    domains/variables (see :py:class:`NXOpen.Fields.FieldVariable`) based on relationships 
    to one or more independent domains/variables (time, temperature, etc.).
    
    Fields are a generic, reusable concept that crosses many 
    areas of functionality.  Defined properly, they provide an extendable concept that can 
    service both simple and complicated needs, for example,  modeling elements, properties, 
    materials, boundary conditions in CAE/FEM applications.
    
    .. versionadded:: NX4.0.0
    """
    
    def GetFieldEvaluator(self) -> FieldEvaluator:
        """
        Returns a field evaluator which can be used to evaluate this field.  
        
        Signature ``GetFieldEvaluator()`` 
        
        :returns:  Field Evaluator  
        :rtype: :py:class:`NXOpen.Fields.FieldEvaluator` 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def GetFieldDrawhelper(self) -> FieldDrawHelper:
        """
        Returns a field drawhelper which can be used to get display attributes of this field.  
        
        Signature ``GetFieldDrawhelper()`` 
        
        :returns:  Field DrawHelper  
        :rtype: :py:class:`NXOpen.Fields.FieldDrawHelper` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPartContext(self) -> None:
        """
        Set part context.  
        
        Signature ``SetPartContext()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDrawHelper(self) -> FieldDrawHelper:
        """
        Creates a field drawhelper which can be used to get display attributes of this field.  
        
        Signature ``CreateDrawHelper()`` 
        
        :returns:  Field DrawHelper  
        :rtype: :py:class:`NXOpen.Fields.FieldDrawHelper` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CopyToPart(self, targetPart: NXOpen.BasePart) -> None:
        """
        Copy the field to the target part.  
        
        Signature ``CopyToPart(targetPart)`` 
        
        :param targetPart:  target part  
        :type targetPart: :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX6.0.1
           Use :py:meth:`NXOpen.Fields.Field.CreateCopyInPart` instead.
        
        License requirements: None.
        """
        ...
    
    
    def CreateCopyInPart(self, targetPart: NXOpen.BasePart) -> Field:
        """
        Copy the field to the target part.  
        
        Signature ``CreateCopyInPart(targetPart)`` 
        
        :param targetPart:  target part  
        :type targetPart: :py:class:`NXOpen.BasePart` 
        :returns:  newly created field  
        :rtype: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CopyAsTableToPart(self, targetPart: NXOpen.BasePart) -> None:
        """
        Create a new table field from this field (regardless of type).  
        
        Note
        * that the table will be created have the N number of rows, where
        * N is the product of the number of points for each independent variable, 
        * resulting in a grid (or lattice).  The resulting field will be in the
        * same part.
        
        Signature ``CopyAsTableToPart(targetPart)`` 
        
        :param targetPart:  target part  
        :type targetPart: :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX6.0.1
           Use :py:meth:`NXOpen.Fields.Field.CreateTableInPart` instead.
        
        License requirements: None.
        """
        ...
    
    
    def CreateTableInPart(self, targetPart: NXOpen.BasePart) -> FieldTable:
        """
        Create a new table field from this field (regardless of type).  
        
        Note
        * that the table will be created have the N number of rows, where
        * N is the product of the number of points for each independent variable, 
        * resulting in a grid (or lattice).  The resulting field will be in the
        * same part.
        
        Signature ``CreateTableInPart(targetPart)`` 
        
        :param targetPart:  target part  
        :type targetPart: :py:class:`NXOpen.BasePart` 
        :returns:  newly created table  
        :rtype: :py:class:`NXOpen.Fields.FieldTable` 
        
        .. versionadded:: NX6.0.1
        
        License requirements: None.
        """
        ...
    
    
    def Rename(self, newName: str) -> None:
        """
        Update the name of the field.  
        
        Signature ``Rename(newName)`` 
        
        :param newName:  new field name  
        :type newName: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSpatialMap(self, overrideMap: SpatialMap) -> None:
        """
        Set the spatial map for the formula field.  
        
        Signature ``SetSpatialMap(overrideMap)`` 
        
        :param overrideMap:  spatial map to set  
        :type overrideMap: :py:class:`NXOpen.Fields.SpatialMap` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSpatialMap(self) -> SpatialMap:
        """
        Returns the spatial map for the formula field if one exists.  
        
        Signature ``GetSpatialMap()`` 
        
        :returns:  spatial map   
        :rtype: :py:class:`NXOpen.Fields.SpatialMap` 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def Delete(self) -> None:
        """
        Delete this field; destroys the field and removes all references to it.  
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def XYGraphAndReturnPlots(self, indepVar: FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: 'list[FieldVariable]', constantIndepVarValueArray: 'list[float]', windowDevice: int, viewIndex: int, overlay: bool) -> 'list[NXOpen.CAE.Xyplot.Plot]':
        """
        Plots or overlays graphs of the Field's specified independent variable
        versus all the Field's dependent variables; returns newly created plot object(s).  
        
        Signature ``XYGraphAndReturnPlots(indepVar, abscissaMinimum, abscissaMaximum, abscissaPointCount, constantIndepVarArray, constantIndepVarValueArray, windowDevice, viewIndex, overlay)`` 
        
        :param indepVar:  the specified independent variable for which to create the graph  
        :type indepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param abscissaMinimum:  the minimum bounds along the abscissa   
        :type abscissaMinimum: float 
        :param abscissaMaximum:  the maximum bounds along the abscissa   
        :type abscissaMaximum: float 
        :param abscissaPointCount:  the number of points to graph along the abscissa.                                                                         the number of times to evaluate the graphed independent variable  
        :type abscissaPointCount: int 
        :param constantIndepVarArray:                                                                          independent variables to hold constant                                                                          If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param constantIndepVarValueArray:  independent variables constant values                                                                         If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarValueArray: list of float 
        :param windowDevice:  great than 0. the index of display device to show the graph. 1 represents main graphic window 
        :type windowDevice: int 
        :param viewIndex:  0 thru 8, viewport number to place the graph in  
        :type viewIndex: int 
        :param overlay:  create a new plot or add to existing  
        :type overlay: bool 
        :returns:  Created plot(s)  
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.Plot` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    
    
    def XYGraphScaleAndReturnPlots(self, indepVar: FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: 'list[FieldVariable]', constantIndepVarValueArray: 'list[float]', windowDevice: int, viewIndex: int, overlay: bool, scaleFactor: float) -> 'list[NXOpen.CAE.Xyplot.Plot]':
        """
        Plots or overlays graphs of the Field's specified independent variable 
        versus all the Field's scaled dependent variables; returns newly created plot object(s).  
        
        Signature ``XYGraphScaleAndReturnPlots(indepVar, abscissaMinimum, abscissaMaximum, abscissaPointCount, constantIndepVarArray, constantIndepVarValueArray, windowDevice, viewIndex, overlay, scaleFactor)`` 
        
        :param indepVar:  the specified independent variable for which to create the graph  
        :type indepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param abscissaMinimum:  the minimum bounds along the abscissa   
        :type abscissaMinimum: float 
        :param abscissaMaximum:  the maximum bounds along the abscissa   
        :type abscissaMaximum: float 
        :param abscissaPointCount:  the number of points to graph along the abscissa.                                                                         the number of times to evaluate the graphed independent variable  
        :type abscissaPointCount: int 
        :param constantIndepVarArray:                                                                          independent variables to hold constant                                                                          If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param constantIndepVarValueArray:  independent variables constant values                                                                         If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarValueArray: list of float 
        :param windowDevice:  great than 0. the index of display device to show the graph. 1 represents main graphic window 
        :type windowDevice: int 
        :param viewIndex:  0 thru 8, viewport number to place the graph in  
        :type viewIndex: int 
        :param overlay:  create a new plot or add to existing  
        :type overlay: bool 
        :param scaleFactor:  scale dependent variable(s)  
        :type scaleFactor: float 
        :returns:  Created plot(s)  
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.Plot` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def XYGraph(self, indepVar: FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: 'list[FieldVariable]', constantIndepVarValueArray: 'list[float]') -> None:
        """
        Creates displayed graphs of the Field's specified independent variable
        versus all the Field's dependent variables
        
        Signature ``XYGraph(indepVar, abscissaMinimum, abscissaMaximum, abscissaPointCount, constantIndepVarArray, constantIndepVarValueArray)`` 
        
        :param indepVar:  the specified independent variable for which to create the graph  
        :type indepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param abscissaMinimum:  the minimum bounds along the abscissa   
        :type abscissaMinimum: float 
        :param abscissaMaximum:  the maximum bounds along the abscissa   
        :type abscissaMaximum: float 
        :param abscissaPointCount:  the number of points to graph along the abscissa.                                                                         the number of times to evaluate the graphed independent variable  
        :type abscissaPointCount: int 
        :param constantIndepVarArray:                                                                          independent variables to hold constant                                                                          If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param constantIndepVarValueArray:  independent variables constant values                                                                         If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarValueArray: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def XYGraph(self, indepVar: FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: 'list[FieldVariable]', constantIndepVarValueArray: 'list[float]', viewIndex: int, overlay: bool) -> None:
        """
        Plots or overlays graphs of the Field's specified independent variable
        versus all the Field's dependent variables
        
        Signature ``XYGraph(indepVar, abscissaMinimum, abscissaMaximum, abscissaPointCount, constantIndepVarArray, constantIndepVarValueArray, viewIndex, overlay)`` 
        
        :param indepVar:  the specified independent variable for which to create the graph  
        :type indepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param abscissaMinimum:  the minimum bounds along the abscissa   
        :type abscissaMinimum: float 
        :param abscissaMaximum:  the maximum bounds along the abscissa   
        :type abscissaMaximum: float 
        :param abscissaPointCount:  the number of points to graph along the abscissa.                                                                         the number of times to evaluate the graphed independent variable  
        :type abscissaPointCount: int 
        :param constantIndepVarArray:                                                                          independent variables to hold constant                                                                          If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param constantIndepVarValueArray:  independent variables constant values                                                                         If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarValueArray: list of float 
        :param viewIndex:  0 thru 8, viewport number to place the graph in  
        :type viewIndex: int 
        :param overlay:  create a new plot or add to existing  
        :type overlay: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def XYGraph(self, indepVar: FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: 'list[FieldVariable]', constantIndepVarValueArray: 'list[float]', windowDevice: int, viewIndex: int, overlay: bool) -> None:
        """
        Plots or overlays graphs of the Field's specified independent variable
        versus all the Field's dependent variables
        
        Signature ``XYGraph(indepVar, abscissaMinimum, abscissaMaximum, abscissaPointCount, constantIndepVarArray, constantIndepVarValueArray, windowDevice, viewIndex, overlay)`` 
        
        :param indepVar:  the specified independent variable for which to create the graph  
        :type indepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param abscissaMinimum:  the minimum bounds along the abscissa   
        :type abscissaMinimum: float 
        :param abscissaMaximum:  the maximum bounds along the abscissa   
        :type abscissaMaximum: float 
        :param abscissaPointCount:  the number of points to graph along the abscissa.                                                                         the number of times to evaluate the graphed independent variable  
        :type abscissaPointCount: int 
        :param constantIndepVarArray:                                                                          independent variables to hold constant                                                                          If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param constantIndepVarValueArray:  independent variables constant values                                                                         If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarValueArray: list of float 
        :param windowDevice:  great than 0. the index of display device to show the graph. 1 represents main graphic window 
        :type windowDevice: int 
        :param viewIndex:  0 thru 8, viewport number to place the graph in  
        :type viewIndex: int 
        :param overlay:  create a new plot or add to existing  
        :type overlay: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def XYGraphArgand(self, indepVar: FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: 'list[FieldVariable]', constantIndepVarValueArray: 'list[float]', windowDevice: int, viewIndex: int) -> 'list[NXOpen.CAE.Xyplot.Plot]':
        """
        Plots the Field's specified independent variable 
        versus all the Field's scaled dependent variables as an Argand graph; returns newly created plot object(s).  
        
        Signature ``XYGraphArgand(indepVar, abscissaMinimum, abscissaMaximum, abscissaPointCount, constantIndepVarArray, constantIndepVarValueArray, windowDevice, viewIndex)`` 
        
        :param indepVar:  the specified independent variable for which to create the graph  
        :type indepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param abscissaMinimum:  the minimum bounds along the abscissa   
        :type abscissaMinimum: float 
        :param abscissaMaximum:  the maximum bounds along the abscissa   
        :type abscissaMaximum: float 
        :param abscissaPointCount:  the number of points to graph along the abscissa.                                                                         the number of times to evaluate the graphed independent variable  
        :type abscissaPointCount: int 
        :param constantIndepVarArray:                                                                          independent variables to hold constant                                                                          If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param constantIndepVarValueArray:  independent variables constant values                                                                         If the field has only 1 independent variable, this parameter is NULL  
        :type constantIndepVarValueArray: list of float 
        :param windowDevice:  great than 0. the index of display device to show the graph. 1 represents main graphic window 
        :type windowDevice: int 
        :param viewIndex:  0 thru 8, viewport number to place the graph in  
        :type viewIndex: int 
        :returns:  Created plot(s)  
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.Plot` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDescription(self, lines: 'list[str]') -> None:
        """
        Update the description of the field.  
        
        Signature ``SetDescription(lines)`` 
        
        :param lines:  new description  
        :type lines: list of str 
        
        .. versionadded:: NX6.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetDescription(self) -> 'list[str]':
        """
        Returns the description of the field.  
        
        Signature ``GetDescription()`` 
        
        :returns:  description  
        :rtype: list of str 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def SetIdLabel(self, idLabel: int) -> None:
        """
        Update the ID/Label of the field.  
        
        Signature ``SetIdLabel(idLabel)`` 
        
        :param idLabel:  ID/Label  
        :type idLabel: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetIdLabel(self) -> int:
        """
        Returns the ID/Label of the field.  
        
        Signature ``GetIdLabel()`` 
        
        :returns:  ID/Label  
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDependentVariables(self) -> 'list[FieldVariable]':
        """
        Returns the dependent variables for this :py:class:`NXOpen.Fields.Field`  
        
        Signature ``GetDependentVariables()`` 
        
        :returns:  dependent variables for this :py:class:`NXOpen.Fields.FieldVariable`   
        :rtype: list of :py:class:`NXOpen.Fields.FieldVariable` 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def GetIndependentVariables(self) -> 'list[FieldVariable]':
        """
        Returns the independent variables for this :py:class:`NXOpen.Fields.Field`  
        
        Signature ``GetIndependentVariables()`` 
        
        :returns:  independent variables for this :py:class:`NXOpen.Fields.FieldVariable`   
        :rtype: list of :py:class:`NXOpen.Fields.FieldVariable` 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def XYGraph3D(self, xAxisIndepVar: FieldVariable, xAxisBndsMinimum: float, xAxisBndsMaximum: float, xAxisBndsSampleSize: int, zAxisIndepVar: FieldVariable, zAxisBndsMinimum: float, zAxisBndsMaximum: float, zAxisBndsSampleSize: int, yAxisDepVar: FieldVariable, constantIndepVarArray: 'list[FieldVariable]', constantIndepVarValueArray: 'list[float]', interpolateTableData: bool, windowDevice: int, viewIndex: int, overlay: bool, scaleFactor: float) -> NXOpen.CAE.Xyplot.Plot:
        """
        Plots or overlays graphs of the Field's specified x-axis and z-axis independent variables
        versus the Field's specified y-axis dependent variable ; returns newly created plot object.  
        
        Signature ``XYGraph3D(xAxisIndepVar, xAxisBndsMinimum, xAxisBndsMaximum, xAxisBndsSampleSize, zAxisIndepVar, zAxisBndsMinimum, zAxisBndsMaximum, zAxisBndsSampleSize, yAxisDepVar, constantIndepVarArray, constantIndepVarValueArray, interpolateTableData, windowDevice, viewIndex, overlay, scaleFactor)`` 
        
        :param xAxisIndepVar:  the specified x-axis independent variable for which to create the graph  
        :type xAxisIndepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param xAxisBndsMinimum:  the minimum bounds along the x-axis   
        :type xAxisBndsMinimum: float 
        :param xAxisBndsMaximum:  the maximum bounds along the x-axis   
        :type xAxisBndsMaximum: float 
        :param xAxisBndsSampleSize:  the sample size to graph along the x-axis.                                                                      the number of times to evaluate the x-axis independent variable  
        :type xAxisBndsSampleSize: int 
        :param zAxisIndepVar:  the specified z-Axis independent variable for which to create the graph  
        :type zAxisIndepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param zAxisBndsMinimum:  the minimum bounds along the z-Axis   
        :type zAxisBndsMinimum: float 
        :param zAxisBndsMaximum:  the maximum bounds along the z-Axis   
        :type zAxisBndsMaximum: float 
        :param zAxisBndsSampleSize:  the sample size to graph along the z-Axis.                                                                      the number of times to evaluate the z-Axis independent variable  
        :type zAxisBndsSampleSize: int 
        :param yAxisDepVar:  the specified y-Axis dependent variable for which to create the graph  
        :type yAxisDepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param constantIndepVarArray:                                                                          independent variables to hold constant                                                                          If the field has only 2 independent variables, this parameter is NULL  
        :type constantIndepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param constantIndepVarValueArray:  independent variables constant values                                                                         If the field has only 2 independent variables, this parameter is NULL  
        :type constantIndepVarValueArray: list of float 
        :param interpolateTableData:  a true value means that the table field data will be interpolated if there are more than 2 independent variables.                                                                          a false value means that the data is plotted directly from the table and the constant values will be ignored.                                                                         this value is only used for table fields with over 2 independent variables. 
        :type interpolateTableData: bool 
        :param windowDevice:  greater than 0. the index of display device to show the graph. 1 represents main graphic window 
        :type windowDevice: int 
        :param viewIndex:  0 thru 8, viewport number to place the graph in  
        :type viewIndex: int 
        :param overlay:  create a new plot or add to existing  
        :type overlay: bool 
        :param scaleFactor:  scale dependent variable  
        :type scaleFactor: float 
        :returns:  Created plot(s)  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.Plot` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetApplicationData(self, applicationName: str) -> IApplicationData:
        """
        Retrieves the application data associated with the field for the specified application.  
        
        Signature ``GetApplicationData(applicationName)`` 
        
        :param applicationName: 
        :type applicationName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Fields.IApplicationData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddApplicationData(self, applicationData: IApplicationData) -> None:
        """
        Adds the specified application data object to the field
        
        NOTE: Only one application data object per IApplication can be added
        and the data must be owned by an IApplication with the same Part::Field::Main 
        as the field.  
        
        Signature ``AddApplicationData(applicationData)`` 
        
        :param applicationData: 
        :type applicationData: :py:class:`NXOpen.Fields.IApplicationData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    IsLocked: bool = ...
    """
    Returns  a value that indicates whether this field is locked against edits.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsLocked`` 
    
    :returns:  True if this is locked against edits.  
    :rtype: bool 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    """
    IsUserField: bool = ...
    """
    Returns  a value that indicates whether this field is a user created/managed field.  
    
    Many fields are created automatically by the system for internal uses. The life of these
    fields is managed by the objects that own them and so these fields are 
    not consider user fields. 
    
    <hr>
    
    Getter Method
    
    Signature ``IsUserField`` 
    
    :returns:  True if this is a user created/managed field  
    :rtype: bool 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    """
    Null: Field = ...  # unknown typename


class FieldReference(Field):
    """
    Represents an reference field  
    
    A Reference Field exposes data inside of an abstract data store.  An abstract data store
    is provided by an appropriate application data provider, and allows access to the provider
    data as a :py:class:`Fields.Field`
    
    To obtain a instance of this class use an appropriate application data provider.
    
    .. versionadded:: NX9.0.0
    """
    
    def SetSecondaryValuesOutsideTableInterpolation(self, interpolationMethod: FieldEvaluatorValuesOutsideTableInterpolationEnum) -> None:
        """
        If the reference field is heterogeneous, set the outside table values interpolation method for the secondary independent domain .  
        
        Otherwise, an error will be raised.
        
        Signature ``SetSecondaryValuesOutsideTableInterpolation(interpolationMethod)`` 
        
        :param interpolationMethod:  the outside table values interpolation method for sub fields 
        :type interpolationMethod: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSecondaryValuesOutsideTableInterpolation(self) -> FieldEvaluatorValuesOutsideTableInterpolationEnum:
        """
        If the reference field is heterogeneous, set the outside table values interpolation method for the secondary independent domain .  
        
        Otherwise, an error will be raised.
        
        Signature ``GetSecondaryValuesOutsideTableInterpolation()`` 
        
        :returns:  the outside table values interpolation method for sub fields 
        :rtype: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    ValuesOutsideTableInterpolation: FieldEvaluatorValuesOutsideTableInterpolationEnum = ...
    """
    Returns or sets  the outside table values interpolation method for linear interpolation.  
    
    If the reference field is heterogeneous, this method gets the outside table values interpolation method for the primary independent doamin and
    use set_secondary_values_outside_table_interpolation method for the secondary independent domain.
    
    <hr>
    
    Getter Method
    
    Signature ``ValuesOutsideTableInterpolation`` 
    
    :returns:  the outside table values interpolation method  
    :rtype: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValuesOutsideTableInterpolation`` 
    
    :param interpolationMethod:  the outside table values interpolation method  
    :type interpolationMethod: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: FieldReference = ...  # unknown typename


class DisplayPropertiesBuilderLineFontEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderLineFontEnum():
    """
    Field Line Display Fonts 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Solid", "Solid"
       "Dashed", "Dashed"
       "Phantom", "Phantom"
       "Centerline", "Centerline"
       "Dotted", "Dotted"
       "LongDashed", "LongDashed"
       "DottedDashed", " - "
    """
    Solid = 0  # DisplayPropertiesBuilderLineFontEnumMemberType
    Dashed = 1  # DisplayPropertiesBuilderLineFontEnumMemberType
    Phantom = 2  # DisplayPropertiesBuilderLineFontEnumMemberType
    Centerline = 3  # DisplayPropertiesBuilderLineFontEnumMemberType
    Dotted = 4  # DisplayPropertiesBuilderLineFontEnumMemberType
    LongDashed = 5  # DisplayPropertiesBuilderLineFontEnumMemberType
    DottedDashed = 6  # DisplayPropertiesBuilderLineFontEnumMemberType
    
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
    


class DisplayPropertiesBuilderLineWidthEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderLineWidthEnum():
    """
    Field Line Widths 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Normal", " - "
       "Thick", " - "
       "Thin", " - "
       "One", " - "
       "Two", " - "
       "Three", " - "
       "Four", " - "
       "Five", " - "
       "Six", " - "
       "Seven", " - "
       "Eight", " - "
       "Nine", " - "
    """
    Normal = 0  # DisplayPropertiesBuilderLineWidthEnumMemberType
    Thick = 1  # DisplayPropertiesBuilderLineWidthEnumMemberType
    Thin = 2  # DisplayPropertiesBuilderLineWidthEnumMemberType
    One = 5  # DisplayPropertiesBuilderLineWidthEnumMemberType
    Two = 6  # DisplayPropertiesBuilderLineWidthEnumMemberType
    Three = 7  # DisplayPropertiesBuilderLineWidthEnumMemberType
    Four = 8  # DisplayPropertiesBuilderLineWidthEnumMemberType
    Five = 9  # DisplayPropertiesBuilderLineWidthEnumMemberType
    Six = 10  # DisplayPropertiesBuilderLineWidthEnumMemberType
    Seven = 11  # DisplayPropertiesBuilderLineWidthEnumMemberType
    Eight = 12  # DisplayPropertiesBuilderLineWidthEnumMemberType
    Nine = 13  # DisplayPropertiesBuilderLineWidthEnumMemberType
    
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
    


class DisplayPropertiesBuilderIndepDomDispTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderIndepDomDispType():
    """
    Field Indep Dom Disp 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Normal", " - "
       "Point", " - "
       "PlusSign", " - "
       "Asterisk", " - "
       "Circle", " - "
       "PoundSign", " - "
       "Cross", " - "
       "Square", " - "
       "Triangle", " - "
       "Diamond", " - "
       "Centerline", " - "
       "Hide", " - "
    """
    Normal = 0  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    Point = 1  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    PlusSign = 2  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    Asterisk = 3  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    Circle = 4  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    PoundSign = 5  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    Cross = 6  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    Square = 7  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    Triangle = 8  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    Diamond = 9  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    Centerline = 10  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    Hide = 11  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
    
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
    


class DisplayPropertiesBuilderDispResolutionEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderDispResolutionEnum():
    """
    Field Disp Resolution 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Coarse", " - "
       "Standard", " - "
       "Fine", " - "
       "ExtraFine", " - "
       "SuperFine", " - "
       "UltraFine", " - "
       "UserSpecified", " - "
    """
    Coarse = 0  # DisplayPropertiesBuilderDispResolutionEnumMemberType
    Standard = 1  # DisplayPropertiesBuilderDispResolutionEnumMemberType
    Fine = 2  # DisplayPropertiesBuilderDispResolutionEnumMemberType
    ExtraFine = 3  # DisplayPropertiesBuilderDispResolutionEnumMemberType
    SuperFine = 4  # DisplayPropertiesBuilderDispResolutionEnumMemberType
    UltraFine = 5  # DisplayPropertiesBuilderDispResolutionEnumMemberType
    UserSpecified = 6  # DisplayPropertiesBuilderDispResolutionEnumMemberType
    
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
    


class DisplayPropertiesBuilderDepLabelValueEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderDepLabelValueEnum():
    """
    Field Dep Label Value 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "MinimumMaximum", " - "
       "Maximum", " - "
       "Minimum", " - "
       "All", " - "
    """
    NotSet = 0  # DisplayPropertiesBuilderDepLabelValueEnumMemberType
    MinimumMaximum = 1  # DisplayPropertiesBuilderDepLabelValueEnumMemberType
    Maximum = 2  # DisplayPropertiesBuilderDepLabelValueEnumMemberType
    Minimum = 3  # DisplayPropertiesBuilderDepLabelValueEnumMemberType
    All = 4  # DisplayPropertiesBuilderDepLabelValueEnumMemberType
    
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
    


class DisplayPropertiesBuilderDepDispTypeEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderDepDispTypeEnum():
    """
    Field Dep Disp Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Symbol", " - "
       "Surface", " - "
       "SurfaceEdges", " - "
       "Hide", " - "
    """
    Symbol = 0  # DisplayPropertiesBuilderDepDispTypeEnumMemberType
    Surface = 1  # DisplayPropertiesBuilderDepDispTypeEnumMemberType
    SurfaceEdges = 2  # DisplayPropertiesBuilderDepDispTypeEnumMemberType
    Hide = 3  # DisplayPropertiesBuilderDepDispTypeEnumMemberType
    
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
    


class DisplayPropertiesBuilderDepDomColorEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderDepDomColorEnum():
    """
    Field Dep Dom Color 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inherit", " - "
       "Specified", " - "
       "Spectrum", " - "
    """
    Inherit = 0  # DisplayPropertiesBuilderDepDomColorEnumMemberType
    Specified = 1  # DisplayPropertiesBuilderDepDomColorEnumMemberType
    Spectrum = 2  # DisplayPropertiesBuilderDepDomColorEnumMemberType
    
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
    


class DisplayPropertiesBuilderValuesEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderValuesEnum():
    """
    Field Values 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Hide", " - "
       "Point", " - "
       "PlusSign", " - "
       "Asterisk", " - "
       "Circle", " - "
       "PoundSign", " - "
       "Cross", " - "
       "Square", " - "
       "Triangle", " - "
       "Diamond", " - "
       "Centerline", " - "
    """
    Hide = 0  # DisplayPropertiesBuilderValuesEnumMemberType
    Point = 1  # DisplayPropertiesBuilderValuesEnumMemberType
    PlusSign = 2  # DisplayPropertiesBuilderValuesEnumMemberType
    Asterisk = 3  # DisplayPropertiesBuilderValuesEnumMemberType
    Circle = 4  # DisplayPropertiesBuilderValuesEnumMemberType
    PoundSign = 5  # DisplayPropertiesBuilderValuesEnumMemberType
    Cross = 6  # DisplayPropertiesBuilderValuesEnumMemberType
    Square = 7  # DisplayPropertiesBuilderValuesEnumMemberType
    Triangle = 8  # DisplayPropertiesBuilderValuesEnumMemberType
    Diamond = 9  # DisplayPropertiesBuilderValuesEnumMemberType
    Centerline = 10  # DisplayPropertiesBuilderValuesEnumMemberType
    
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
    


class DisplayPropertiesBuilderTblPointTypeEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderTblPointTypeEnum():
    """
    Field Tbl Point Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Hide", " - "
       "Show", " - "
    """
    Hide = 0  # DisplayPropertiesBuilderTblPointTypeEnumMemberType
    Show = 1  # DisplayPropertiesBuilderTblPointTypeEnumMemberType
    
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
    


class DisplayPropertiesBuilderValueRangeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderValueRange():
    """
    range for contour plots 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Auto", " - "
       "Specified", " - "
    """
    Auto = 0  # DisplayPropertiesBuilderValueRangeMemberType
    Specified = 1  # DisplayPropertiesBuilderValueRangeMemberType
    
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
    


class DisplayPropertiesBuilderScalarTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderScalarType():
    """
    Scalar Field Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Hide", " - "
       "Mag", " - "
    """
    Hide = 0  # DisplayPropertiesBuilderScalarTypeMemberType
    Mag = 1  # DisplayPropertiesBuilderScalarTypeMemberType
    
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
    


class DisplayPropertiesBuilderComplexScalarTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderComplexScalarType():
    """
    Complex Scalar Field Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Mag", " - "
       "Real", " - "
       "Imaginary", " - "
       "Phase", " - "
    """
    Mag = 0  # DisplayPropertiesBuilderComplexScalarTypeMemberType
    Real = 1  # DisplayPropertiesBuilderComplexScalarTypeMemberType
    Imaginary = 2  # DisplayPropertiesBuilderComplexScalarTypeMemberType
    Phase = 3  # DisplayPropertiesBuilderComplexScalarTypeMemberType
    
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
    


class DisplayPropertiesBuilderComplexVectorTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderComplexVectorType():
    """
    Complex Vector Field Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "XReal", " - "
       "YReal", " - "
       "ZReal", " - "
       "XImaginary", " - "
       "YImaginary", " - "
       "ZImaginary", " - "
    """
    XReal = 0  # DisplayPropertiesBuilderComplexVectorTypeMemberType
    YReal = 1  # DisplayPropertiesBuilderComplexVectorTypeMemberType
    ZReal = 2  # DisplayPropertiesBuilderComplexVectorTypeMemberType
    XImaginary = 3  # DisplayPropertiesBuilderComplexVectorTypeMemberType
    YImaginary = 4  # DisplayPropertiesBuilderComplexVectorTypeMemberType
    ZImaginary = 5  # DisplayPropertiesBuilderComplexVectorTypeMemberType
    
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
    


class DisplayPropertiesBuilderVectorTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderVectorType():
    """
    Vector Field Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", " - "
       "Y", " - "
       "Z", " - "
       "Mag", " - "
    """
    X = 0  # DisplayPropertiesBuilderVectorTypeMemberType
    Y = 1  # DisplayPropertiesBuilderVectorTypeMemberType
    Z = 2  # DisplayPropertiesBuilderVectorTypeMemberType
    Mag = 3  # DisplayPropertiesBuilderVectorTypeMemberType
    
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
    


class DisplayPropertiesBuilderLegacy3DTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderLegacy3DType():
    """
    Legacy_3D Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", " - "
       "Y", " - "
       "Z", " - "
    """
    X = 0  # DisplayPropertiesBuilderLegacy3DTypeMemberType
    Y = 1  # DisplayPropertiesBuilderLegacy3DTypeMemberType
    Z = 2  # DisplayPropertiesBuilderLegacy3DTypeMemberType
    
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
    


class DisplayPropertiesBuilderTensorTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderTensorType():
    """
    Tensor Field Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Xx", " - "
       "Yy", " - "
       "Zz", " - "
       "Xy", " - "
       "Yz", " - "
       "Zx", " - "
       "Mean", " - "
       "MidPrncpl", " - "
       "MinPrncpl", " - "
       "MaxPrncpl", " - "
       "Octahedral", " - "
       "VonMises", " - "
    """
    Xx = 0  # DisplayPropertiesBuilderTensorTypeMemberType
    Yy = 1  # DisplayPropertiesBuilderTensorTypeMemberType
    Zz = 2  # DisplayPropertiesBuilderTensorTypeMemberType
    Xy = 3  # DisplayPropertiesBuilderTensorTypeMemberType
    Yz = 4  # DisplayPropertiesBuilderTensorTypeMemberType
    Zx = 5  # DisplayPropertiesBuilderTensorTypeMemberType
    Mean = 6  # DisplayPropertiesBuilderTensorTypeMemberType
    MidPrncpl = 7  # DisplayPropertiesBuilderTensorTypeMemberType
    MinPrncpl = 8  # DisplayPropertiesBuilderTensorTypeMemberType
    MaxPrncpl = 9  # DisplayPropertiesBuilderTensorTypeMemberType
    Octahedral = 10  # DisplayPropertiesBuilderTensorTypeMemberType
    VonMises = 11  # DisplayPropertiesBuilderTensorTypeMemberType
    
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
    


class DisplayPropertiesBuilderBalStrainTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderBalStrainType():
    """
    Balance Strain Field Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Xx", " - "
       "Yy", " - "
       "Zz", " - "
       "Xy", " - "
       "Yz", " - "
       "Zx", " - "
       "OffSetXX", " - "
       "OffSetYY", " - "
       "OffSetZZ", " - "
       "OffSetXY", " - "
       "OffSetYZ", " - "
       "OffSetZX", " - "
    """
    Xx = 0  # DisplayPropertiesBuilderBalStrainTypeMemberType
    Yy = 1  # DisplayPropertiesBuilderBalStrainTypeMemberType
    Zz = 2  # DisplayPropertiesBuilderBalStrainTypeMemberType
    Xy = 3  # DisplayPropertiesBuilderBalStrainTypeMemberType
    Yz = 4  # DisplayPropertiesBuilderBalStrainTypeMemberType
    Zx = 5  # DisplayPropertiesBuilderBalStrainTypeMemberType
    OffSetXX = 6  # DisplayPropertiesBuilderBalStrainTypeMemberType
    OffSetYY = 7  # DisplayPropertiesBuilderBalStrainTypeMemberType
    OffSetZZ = 8  # DisplayPropertiesBuilderBalStrainTypeMemberType
    OffSetXY = 9  # DisplayPropertiesBuilderBalStrainTypeMemberType
    OffSetYZ = 10  # DisplayPropertiesBuilderBalStrainTypeMemberType
    OffSetZX = 11  # DisplayPropertiesBuilderBalStrainTypeMemberType
    
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
    


class DisplayPropertiesBuilderFieldQuantityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderFieldQuantityType():
    """
    Field Quanity Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Type0", " - "
       "Type1", " - "
       "Type2", " - "
       "Type3", " - "
       "Type4", " - "
       "Type5", " - "
       "Type6", " - "
       "Type7", " - "
       "Type8", " - "
       "Type9", " - "
       "Type10", " - "
       "Type11", " - "
       "Type12", " - "
       "Type13", " - "
       "Type14", " - "
       "Type15", " - "
    """
    Type0 = 0  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type1 = 1  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type2 = 2  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type3 = 3  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type4 = 4  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type5 = 5  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type6 = 6  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type7 = 7  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type8 = 8  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type9 = 9  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type10 = 10  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type11 = 11  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type12 = 12  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type13 = 13  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type14 = 14  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    Type15 = 15  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
    
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
    


class DisplayPropertiesBuilderLegendPosMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DisplayPropertiesBuilderLegendPos():
    """
    legend position 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Hide", " - "
       "Left", " - "
       "Right", " - "
    """
    Hide = 0  # DisplayPropertiesBuilderLegendPosMemberType
    Left = 1  # DisplayPropertiesBuilderLegendPosMemberType
    Right = 2  # DisplayPropertiesBuilderLegendPosMemberType
    
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
    


class DisplayPropertiesBuilder(NXOpen.Builder):
    """
    Represents a builder class for editing display properties of a :py:class:`NXOpen.Fields.Field`  
    
    Used to edit a :py:class:`NXOpen.Fields.Field` display properties.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Fields.FieldManager.CreateDisplayPropertiesBuilder`
    
    Default values.
    
    ============================  ======================================
    Property                      Value
    ============================  ======================================
    DepCalcSymblSize              0.1 
    ----------------------------  --------------------------------------
    DepDispType                   Symbol 
    ----------------------------  --------------------------------------
    DepDomColor                   Inherit 
    ----------------------------  --------------------------------------
    DepLabelValues                None 
    ----------------------------  --------------------------------------
    DepRangeMax                   0 
    ----------------------------  --------------------------------------
    DepRangeMin                   0 
    ----------------------------  --------------------------------------
    DisplayResolution             Standard 
    ----------------------------  --------------------------------------
    FaceAnalysis                  0 
    ----------------------------  --------------------------------------
    FieldQuantity                 Type0 
    ----------------------------  --------------------------------------
    IndepDispType                 Hide 
    ----------------------------  --------------------------------------
    Layer                         1 
    ----------------------------  --------------------------------------
    LegendPosition                Left 
    ----------------------------  --------------------------------------
    LineFont                      Solid 
    ----------------------------  --------------------------------------
    LineWidth                     Normal 
    ----------------------------  --------------------------------------
    PartiallyShaded               0 
    ----------------------------  --------------------------------------
    PrimaryVar.Value              0 (millimeters part), 0 (inches part) 
    ----------------------------  --------------------------------------
    Range                         Auto 
    ----------------------------  --------------------------------------
    RangeMax                      1 
    ----------------------------  --------------------------------------
    RangeMin                      1 
    ----------------------------  --------------------------------------
    ShowAxis                      0 
    ----------------------------  --------------------------------------
    ShowDefaultVal                0 
    ----------------------------  --------------------------------------
    ShowDescription               0 
    ----------------------------  --------------------------------------
    ShowLabels                    0 
    ----------------------------  --------------------------------------
    ShowMapTopo                   0 
    ----------------------------  --------------------------------------
    ShowName                      0 
    ----------------------------  --------------------------------------
    ShowOverflowValues            0 
    ----------------------------  --------------------------------------
    ShowSrcTblVals                1 
    ----------------------------  --------------------------------------
    ShowUndefValues               0 
    ----------------------------  --------------------------------------
    ShowUnderflowValues           0 
    ----------------------------  --------------------------------------
    SpectrumLevels                3 
    ----------------------------  --------------------------------------
    SurfaceOffset                 0 
    ----------------------------  --------------------------------------
    TblDepPtType (deprecated)     Hide 
    ----------------------------  --------------------------------------
    TblIndepPtType (deprecated)   Hide 
    ----------------------------  --------------------------------------
    Translucency                  0 
    ----------------------------  --------------------------------------
    XMax.Value                    0 (millimeters part), 1 (inches part) 
    ----------------------------  --------------------------------------
    XMin.Value                    0 (millimeters part), 0 (inches part) 
    ----------------------------  --------------------------------------
    XNum                          1 
    ----------------------------  --------------------------------------
    YMax.Value                    0 (millimeters part), 1 (inches part) 
    ----------------------------  --------------------------------------
    YMin.Value                    0 (millimeters part), 0 (inches part) 
    ----------------------------  --------------------------------------
    YNum                          1 
    ----------------------------  --------------------------------------
    ZMax.Value                    0 (millimeters part), 1 (inches part) 
    ----------------------------  --------------------------------------
    ZMin.Value                    0 (millimeters part), 0 (inches part) 
    ----------------------------  --------------------------------------
    ZNum                          1 
    ============================  ======================================
    
    .. versionadded:: NX6.0.1
    """
    
    class LineFontEnum():
        """
        Field Line Display Fonts 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Solid", "Solid"
           "Dashed", "Dashed"
           "Phantom", "Phantom"
           "Centerline", "Centerline"
           "Dotted", "Dotted"
           "LongDashed", "LongDashed"
           "DottedDashed", " - "
        """
        Solid = 0  # DisplayPropertiesBuilderLineFontEnumMemberType
        Dashed = 1  # DisplayPropertiesBuilderLineFontEnumMemberType
        Phantom = 2  # DisplayPropertiesBuilderLineFontEnumMemberType
        Centerline = 3  # DisplayPropertiesBuilderLineFontEnumMemberType
        Dotted = 4  # DisplayPropertiesBuilderLineFontEnumMemberType
        LongDashed = 5  # DisplayPropertiesBuilderLineFontEnumMemberType
        DottedDashed = 6  # DisplayPropertiesBuilderLineFontEnumMemberType
        
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
        
    
    
    class LineWidthEnum():
        """
        Field Line Widths 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Normal", " - "
           "Thick", " - "
           "Thin", " - "
           "One", " - "
           "Two", " - "
           "Three", " - "
           "Four", " - "
           "Five", " - "
           "Six", " - "
           "Seven", " - "
           "Eight", " - "
           "Nine", " - "
        """
        Normal = 0  # DisplayPropertiesBuilderLineWidthEnumMemberType
        Thick = 1  # DisplayPropertiesBuilderLineWidthEnumMemberType
        Thin = 2  # DisplayPropertiesBuilderLineWidthEnumMemberType
        One = 5  # DisplayPropertiesBuilderLineWidthEnumMemberType
        Two = 6  # DisplayPropertiesBuilderLineWidthEnumMemberType
        Three = 7  # DisplayPropertiesBuilderLineWidthEnumMemberType
        Four = 8  # DisplayPropertiesBuilderLineWidthEnumMemberType
        Five = 9  # DisplayPropertiesBuilderLineWidthEnumMemberType
        Six = 10  # DisplayPropertiesBuilderLineWidthEnumMemberType
        Seven = 11  # DisplayPropertiesBuilderLineWidthEnumMemberType
        Eight = 12  # DisplayPropertiesBuilderLineWidthEnumMemberType
        Nine = 13  # DisplayPropertiesBuilderLineWidthEnumMemberType
        
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
        
    
    
    class IndepDomDispType():
        """
        Field Indep Dom Disp 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Normal", " - "
           "Point", " - "
           "PlusSign", " - "
           "Asterisk", " - "
           "Circle", " - "
           "PoundSign", " - "
           "Cross", " - "
           "Square", " - "
           "Triangle", " - "
           "Diamond", " - "
           "Centerline", " - "
           "Hide", " - "
        """
        Normal = 0  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        Point = 1  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        PlusSign = 2  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        Asterisk = 3  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        Circle = 4  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        PoundSign = 5  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        Cross = 6  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        Square = 7  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        Triangle = 8  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        Diamond = 9  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        Centerline = 10  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        Hide = 11  # DisplayPropertiesBuilderIndepDomDispTypeMemberType
        
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
        
    
    
    class DispResolutionEnum():
        """
        Field Disp Resolution 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Coarse", " - "
           "Standard", " - "
           "Fine", " - "
           "ExtraFine", " - "
           "SuperFine", " - "
           "UltraFine", " - "
           "UserSpecified", " - "
        """
        Coarse = 0  # DisplayPropertiesBuilderDispResolutionEnumMemberType
        Standard = 1  # DisplayPropertiesBuilderDispResolutionEnumMemberType
        Fine = 2  # DisplayPropertiesBuilderDispResolutionEnumMemberType
        ExtraFine = 3  # DisplayPropertiesBuilderDispResolutionEnumMemberType
        SuperFine = 4  # DisplayPropertiesBuilderDispResolutionEnumMemberType
        UltraFine = 5  # DisplayPropertiesBuilderDispResolutionEnumMemberType
        UserSpecified = 6  # DisplayPropertiesBuilderDispResolutionEnumMemberType
        
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
        
    
    
    class DepLabelValueEnum():
        """
        Field Dep Label Value 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "MinimumMaximum", " - "
           "Maximum", " - "
           "Minimum", " - "
           "All", " - "
        """
        NotSet = 0  # DisplayPropertiesBuilderDepLabelValueEnumMemberType
        MinimumMaximum = 1  # DisplayPropertiesBuilderDepLabelValueEnumMemberType
        Maximum = 2  # DisplayPropertiesBuilderDepLabelValueEnumMemberType
        Minimum = 3  # DisplayPropertiesBuilderDepLabelValueEnumMemberType
        All = 4  # DisplayPropertiesBuilderDepLabelValueEnumMemberType
        
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
        
    
    
    class DepDispTypeEnum():
        """
        Field Dep Disp Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Symbol", " - "
           "Surface", " - "
           "SurfaceEdges", " - "
           "Hide", " - "
        """
        Symbol = 0  # DisplayPropertiesBuilderDepDispTypeEnumMemberType
        Surface = 1  # DisplayPropertiesBuilderDepDispTypeEnumMemberType
        SurfaceEdges = 2  # DisplayPropertiesBuilderDepDispTypeEnumMemberType
        Hide = 3  # DisplayPropertiesBuilderDepDispTypeEnumMemberType
        
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
        
    
    
    class DepDomColorEnum():
        """
        Field Dep Dom Color 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inherit", " - "
           "Specified", " - "
           "Spectrum", " - "
        """
        Inherit = 0  # DisplayPropertiesBuilderDepDomColorEnumMemberType
        Specified = 1  # DisplayPropertiesBuilderDepDomColorEnumMemberType
        Spectrum = 2  # DisplayPropertiesBuilderDepDomColorEnumMemberType
        
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
        
    
    
    class ValuesEnum():
        """
        Field Values 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Hide", " - "
           "Point", " - "
           "PlusSign", " - "
           "Asterisk", " - "
           "Circle", " - "
           "PoundSign", " - "
           "Cross", " - "
           "Square", " - "
           "Triangle", " - "
           "Diamond", " - "
           "Centerline", " - "
        """
        Hide = 0  # DisplayPropertiesBuilderValuesEnumMemberType
        Point = 1  # DisplayPropertiesBuilderValuesEnumMemberType
        PlusSign = 2  # DisplayPropertiesBuilderValuesEnumMemberType
        Asterisk = 3  # DisplayPropertiesBuilderValuesEnumMemberType
        Circle = 4  # DisplayPropertiesBuilderValuesEnumMemberType
        PoundSign = 5  # DisplayPropertiesBuilderValuesEnumMemberType
        Cross = 6  # DisplayPropertiesBuilderValuesEnumMemberType
        Square = 7  # DisplayPropertiesBuilderValuesEnumMemberType
        Triangle = 8  # DisplayPropertiesBuilderValuesEnumMemberType
        Diamond = 9  # DisplayPropertiesBuilderValuesEnumMemberType
        Centerline = 10  # DisplayPropertiesBuilderValuesEnumMemberType
        
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
        
    
    
    class TblPointTypeEnum():
        """
        Field Tbl Point Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Hide", " - "
           "Show", " - "
        """
        Hide = 0  # DisplayPropertiesBuilderTblPointTypeEnumMemberType
        Show = 1  # DisplayPropertiesBuilderTblPointTypeEnumMemberType
        
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
        
    
    
    class ValueRange():
        """
        range for contour plots 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Auto", " - "
           "Specified", " - "
        """
        Auto = 0  # DisplayPropertiesBuilderValueRangeMemberType
        Specified = 1  # DisplayPropertiesBuilderValueRangeMemberType
        
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
        
    
    
    class ScalarType():
        """
        Scalar Field Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Hide", " - "
           "Mag", " - "
        """
        Hide = 0  # DisplayPropertiesBuilderScalarTypeMemberType
        Mag = 1  # DisplayPropertiesBuilderScalarTypeMemberType
        
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
        
    
    
    class ComplexScalarType():
        """
        Complex Scalar Field Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Mag", " - "
           "Real", " - "
           "Imaginary", " - "
           "Phase", " - "
        """
        Mag = 0  # DisplayPropertiesBuilderComplexScalarTypeMemberType
        Real = 1  # DisplayPropertiesBuilderComplexScalarTypeMemberType
        Imaginary = 2  # DisplayPropertiesBuilderComplexScalarTypeMemberType
        Phase = 3  # DisplayPropertiesBuilderComplexScalarTypeMemberType
        
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
        
    
    
    class ComplexVectorType():
        """
        Complex Vector Field Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "XReal", " - "
           "YReal", " - "
           "ZReal", " - "
           "XImaginary", " - "
           "YImaginary", " - "
           "ZImaginary", " - "
        """
        XReal = 0  # DisplayPropertiesBuilderComplexVectorTypeMemberType
        YReal = 1  # DisplayPropertiesBuilderComplexVectorTypeMemberType
        ZReal = 2  # DisplayPropertiesBuilderComplexVectorTypeMemberType
        XImaginary = 3  # DisplayPropertiesBuilderComplexVectorTypeMemberType
        YImaginary = 4  # DisplayPropertiesBuilderComplexVectorTypeMemberType
        ZImaginary = 5  # DisplayPropertiesBuilderComplexVectorTypeMemberType
        
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
        
    
    
    class VectorType():
        """
        Vector Field Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "X", " - "
           "Y", " - "
           "Z", " - "
           "Mag", " - "
        """
        X = 0  # DisplayPropertiesBuilderVectorTypeMemberType
        Y = 1  # DisplayPropertiesBuilderVectorTypeMemberType
        Z = 2  # DisplayPropertiesBuilderVectorTypeMemberType
        Mag = 3  # DisplayPropertiesBuilderVectorTypeMemberType
        
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
        
    
    
    class Legacy3DType():
        """
        Legacy_3D Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "X", " - "
           "Y", " - "
           "Z", " - "
        """
        X = 0  # DisplayPropertiesBuilderLegacy3DTypeMemberType
        Y = 1  # DisplayPropertiesBuilderLegacy3DTypeMemberType
        Z = 2  # DisplayPropertiesBuilderLegacy3DTypeMemberType
        
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
        
    
    
    class TensorType():
        """
        Tensor Field Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Xx", " - "
           "Yy", " - "
           "Zz", " - "
           "Xy", " - "
           "Yz", " - "
           "Zx", " - "
           "Mean", " - "
           "MidPrncpl", " - "
           "MinPrncpl", " - "
           "MaxPrncpl", " - "
           "Octahedral", " - "
           "VonMises", " - "
        """
        Xx = 0  # DisplayPropertiesBuilderTensorTypeMemberType
        Yy = 1  # DisplayPropertiesBuilderTensorTypeMemberType
        Zz = 2  # DisplayPropertiesBuilderTensorTypeMemberType
        Xy = 3  # DisplayPropertiesBuilderTensorTypeMemberType
        Yz = 4  # DisplayPropertiesBuilderTensorTypeMemberType
        Zx = 5  # DisplayPropertiesBuilderTensorTypeMemberType
        Mean = 6  # DisplayPropertiesBuilderTensorTypeMemberType
        MidPrncpl = 7  # DisplayPropertiesBuilderTensorTypeMemberType
        MinPrncpl = 8  # DisplayPropertiesBuilderTensorTypeMemberType
        MaxPrncpl = 9  # DisplayPropertiesBuilderTensorTypeMemberType
        Octahedral = 10  # DisplayPropertiesBuilderTensorTypeMemberType
        VonMises = 11  # DisplayPropertiesBuilderTensorTypeMemberType
        
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
        
    
    
    class BalStrainType():
        """
        Balance Strain Field Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Xx", " - "
           "Yy", " - "
           "Zz", " - "
           "Xy", " - "
           "Yz", " - "
           "Zx", " - "
           "OffSetXX", " - "
           "OffSetYY", " - "
           "OffSetZZ", " - "
           "OffSetXY", " - "
           "OffSetYZ", " - "
           "OffSetZX", " - "
        """
        Xx = 0  # DisplayPropertiesBuilderBalStrainTypeMemberType
        Yy = 1  # DisplayPropertiesBuilderBalStrainTypeMemberType
        Zz = 2  # DisplayPropertiesBuilderBalStrainTypeMemberType
        Xy = 3  # DisplayPropertiesBuilderBalStrainTypeMemberType
        Yz = 4  # DisplayPropertiesBuilderBalStrainTypeMemberType
        Zx = 5  # DisplayPropertiesBuilderBalStrainTypeMemberType
        OffSetXX = 6  # DisplayPropertiesBuilderBalStrainTypeMemberType
        OffSetYY = 7  # DisplayPropertiesBuilderBalStrainTypeMemberType
        OffSetZZ = 8  # DisplayPropertiesBuilderBalStrainTypeMemberType
        OffSetXY = 9  # DisplayPropertiesBuilderBalStrainTypeMemberType
        OffSetYZ = 10  # DisplayPropertiesBuilderBalStrainTypeMemberType
        OffSetZX = 11  # DisplayPropertiesBuilderBalStrainTypeMemberType
        
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
        
    
    
    class FieldQuantityType():
        """
        Field Quanity Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Type0", " - "
           "Type1", " - "
           "Type2", " - "
           "Type3", " - "
           "Type4", " - "
           "Type5", " - "
           "Type6", " - "
           "Type7", " - "
           "Type8", " - "
           "Type9", " - "
           "Type10", " - "
           "Type11", " - "
           "Type12", " - "
           "Type13", " - "
           "Type14", " - "
           "Type15", " - "
        """
        Type0 = 0  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type1 = 1  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type2 = 2  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type3 = 3  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type4 = 4  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type5 = 5  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type6 = 6  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type7 = 7  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type8 = 8  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type9 = 9  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type10 = 10  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type11 = 11  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type12 = 12  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type13 = 13  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type14 = 14  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        Type15 = 15  # DisplayPropertiesBuilderFieldQuantityTypeMemberType
        
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
        
    
    
    class LegendPos():
        """
        legend position 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Hide", " - "
           "Left", " - "
           "Right", " - "
        """
        Hide = 0  # DisplayPropertiesBuilderLegendPosMemberType
        Left = 1  # DisplayPropertiesBuilderLegendPosMemberType
        Right = 2  # DisplayPropertiesBuilderLegendPosMemberType
        
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
        
    
    AxisColor: NXOpen.NXColor = ...
    """
    Returns or sets  the axis color 
    
    <hr>
    
    Getter Method
    
    Signature ``AxisColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AxisColor`` 
    
    :param axisColor: 
    :type axisColor: Id 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    BasicColor: NXOpen.NXColor = ...
    """
    Returns or sets  the basic color 
    
    <hr>
    
    Getter Method
    
    Signature ``BasicColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BasicColor`` 
    
    :param basicColor: 
    :type basicColor: Id 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    DepCalcSymblSize: float = ...
    """
    Returns or sets  the dep calc symbl size 
    
    <hr>
    
    Getter Method
    
    Signature ``DepCalcSymblSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DepCalcSymblSize`` 
    
    :param depCalcSymblSize: 
    :type depCalcSymblSize: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DepDispType: DisplayPropertiesBuilderDepDispTypeEnum = ...
    """
    Returns or sets  the dep disp type 
    
    <hr>
    
    Getter Method
    
    Signature ``DepDispType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDepDispTypeEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DepDispType`` 
    
    :param depDispType: 
    :type depDispType: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDepDispTypeEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    DepDomColor: DisplayPropertiesBuilderDepDomColorEnum = ...
    """
    Returns or sets  the dep dom color 
    
    <hr>
    
    Getter Method
    
    Signature ``DepDomColor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDepDomColorEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DepDomColor`` 
    
    :param depDomColor: 
    :type depDomColor: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDepDomColorEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    DepLabelValues: DisplayPropertiesBuilderDepLabelValueEnum = ...
    """
    Returns or sets  the dep label values 
    
    <hr>
    
    Getter Method
    
    Signature ``DepLabelValues`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDepLabelValueEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DepLabelValues`` 
    
    :param depLabelValues: 
    :type depLabelValues: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDepLabelValueEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    DepRangeMax: float = ...
    """
    Returns or sets  the dep range max 
    
    <hr>
    
    Getter Method
    
    Signature ``DepRangeMax`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DepRangeMax`` 
    
    :param depRangeMax: 
    :type depRangeMax: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DepRangeMin: float = ...
    """
    Returns or sets  the dependent range min 
    
    <hr>
    
    Getter Method
    
    Signature ``DepRangeMin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DepRangeMin`` 
    
    :param depRangeMin: 
    :type depRangeMin: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DepSelColor: NXOpen.NXColor = ...
    """
    Returns or sets  the dep sel color 
    
    <hr>
    
    Getter Method
    
    Signature ``DepSelColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DepSelColor`` 
    
    :param depSelColor: 
    :type depSelColor: Id 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    DepSymbolSize: float = ...
    """
    Returns or sets  the dep symbol size 
    
    <hr>
    
    Getter Method
    
    Signature ``DepSymbolSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DepSymbolSize`` 
    
    :param depSymbolSize: 
    :type depSymbolSize: float 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    DisplayResolution: DisplayPropertiesBuilderDispResolutionEnum = ...
    """
    Returns or sets  the display resolution 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayResolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDispResolutionEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayResolution`` 
    
    :param displayResolution: 
    :type displayResolution: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDispResolutionEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    DummyScale: float = ...
    """
    Returns or sets  the dummy scale 
    
    <hr>
    
    Getter Method
    
    Signature ``DummyScale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DummyScale`` 
    
    :param dummyScale: 
    :type dummyScale: float 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    FaceAnalysis: bool = ...
    """
    Returns or sets  the face analysis 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceAnalysis`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FaceAnalysis`` 
    
    :param faceAnalysis: 
    :type faceAnalysis: bool 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    FieldQuantity: DisplayPropertiesBuilderFieldQuantityType = ...
    """
    Returns or sets  the field quantity type
    
    <hr>
    
    Getter Method
    
    Signature ``FieldQuantity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderFieldQuantityType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FieldQuantity`` 
    
    :param fieldQuantity: 
    :type fieldQuantity: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderFieldQuantityType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IndepDispType: DisplayPropertiesBuilderIndepDomDispType = ...
    """
    Returns or sets  the indep disp type 
    
    <hr>
    
    Getter Method
    
    Signature ``IndepDispType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderIndepDomDispType` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IndepDispType`` 
    
    :param indepDispType: 
    :type indepDispType: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderIndepDomDispType` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    LabelColor: NXOpen.NXColor = ...
    """
    Returns or sets  the label color 
    
    <hr>
    
    Getter Method
    
    Signature ``LabelColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelColor`` 
    
    :param labelColor: 
    :type labelColor: Id 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    Layer: int = ...
    """
    Returns or sets  the layer 
    
    <hr>
    
    Getter Method
    
    Signature ``Layer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Layer`` 
    
    :param layer: 
    :type layer: int 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    LegendPosition: DisplayPropertiesBuilderLegendPos = ...
    """
    Returns or sets  the legend position 
    
    <hr>
    
    Getter Method
    
    Signature ``LegendPosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderLegendPos` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LegendPosition`` 
    
    :param legendPosition: 
    :type legendPosition: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderLegendPos` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LineFont: DisplayPropertiesBuilderLineFontEnum = ...
    """
    Returns or sets  the line font 
    
    <hr>
    
    Getter Method
    
    Signature ``LineFont`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderLineFontEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineFont`` 
    
    :param lineFont: 
    :type lineFont: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderLineFontEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    LineWidth: DisplayPropertiesBuilderLineWidthEnum = ...
    """
    Returns or sets  the line width 
    
    <hr>
    
    Getter Method
    
    Signature ``LineWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderLineWidthEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineWidth`` 
    
    :param lineWidth: 
    :type lineWidth: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderLineWidthEnum` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    OverflowColor: NXOpen.NXColor = ...
    """
    Returns or sets  the overflow color 
    
    <hr>
    
    Getter Method
    
    Signature ``OverflowColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OverflowColor`` 
    
    :param overflowColor: 
    :type overflowColor: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    PartiallyShaded: bool = ...
    """
    Returns or sets  the partially shaded 
    
    <hr>
    
    Getter Method
    
    Signature ``PartiallyShaded`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PartiallyShaded`` 
    
    :param partiallyShaded: 
    :type partiallyShaded: bool 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    PrimaryVar: NXOpen.Expression = ...
    """
    Returns  the primary var name 
    
    <hr>
    
    Getter Method
    
    Signature ``PrimaryVar`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Range: DisplayPropertiesBuilderValueRange = ...
    """
    Returns or sets  the range 
    
    <hr>
    
    Getter Method
    
    Signature ``Range`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderValueRange` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Range`` 
    
    :param range: 
    :type range: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderValueRange` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RangeMax: float = ...
    """
    Returns or sets  the legend range max 
    
    <hr>
    
    Getter Method
    
    Signature ``RangeMax`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RangeMax`` 
    
    :param rangeMax: 
    :type rangeMax: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RangeMin: float = ...
    """
    Returns or sets  the legend range min 
    
    <hr>
    
    Getter Method
    
    Signature ``RangeMin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RangeMin`` 
    
    :param rangeMin: 
    :type rangeMin: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowAxis: bool = ...
    """
    Returns or sets  the show axis 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowAxis`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowAxis`` 
    
    :param showAxis: 
    :type showAxis: bool 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    ShowDefaultVal: bool = ...
    """
    Returns or sets  the show default val 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowDefaultVal`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowDefaultVal`` 
    
    :param showDefaultVal: 
    :type showDefaultVal: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowDescription: bool = ...
    """
    Returns or sets  the show description 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowDescription`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowDescription`` 
    
    :param showDescription: 
    :type showDescription: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowLabels: bool = ...
    """
    Returns or sets  the show labels 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowLabels`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowLabels`` 
    
    :param showLabels: 
    :type showLabels: bool 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    ShowMapTopo: bool = ...
    """
    Returns or sets  the show map topo 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowMapTopo`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowMapTopo`` 
    
    :param showMapTopo: 
    :type showMapTopo: bool 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    ShowName: bool = ...
    """
    Returns or sets  the show name 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowName`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowName`` 
    
    :param showName: 
    :type showName: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowOverflowValues: bool = ...
    """
    Returns or sets  the show overflow 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOverflowValues`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOverflowValues`` 
    
    :param showOverflow: 
    :type showOverflow: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowSrcTblVals: bool = ...
    """
    Returns or sets  the show dep src tbl vals 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowSrcTblVals`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowSrcTblVals`` 
    
    :param showSrcTblVals: 
    :type showSrcTblVals: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowUndefValues: bool = ...
    """
    Returns or sets  the show new undefined values 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowUndefValues`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowUndefValues`` 
    
    :param showUndefinedValues: 
    :type showUndefinedValues: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowUndefinedValues: DisplayPropertiesBuilderValuesEnum = ...
    """
    Returns or sets  the show undefined values 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowUndefinedValues`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderValuesEnum` 
    
    .. versionadded:: NX6.0.1
    
    .. deprecated::  NX12.0.0
       This method is deprecated. Use :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.ShowUndefValues` Undefined values are no longer displayed with various symbols, but are only on or off.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowUndefinedValues`` 
    
    :param showUndefinedValues: 
    :type showUndefinedValues: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderValuesEnum` 
    
    .. versionadded:: NX6.0.1
    
    .. deprecated::  NX12.0.0
       This method is deprecated. Use :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.ShowUndefValues` Undefined values are no longer displayed with various symbols, but are only on or off. For backward compatibility, calling this method with hide is the same as calling the new method with false; any other value is the same as calling the new method with true. 
    
    License requirements: None.
    """
    ShowUnderflowValues: bool = ...
    """
    Returns or sets  the show underflow 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowUnderflowValues`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowUnderflowValues`` 
    
    :param showUnderflow: 
    :type showUnderflow: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SpectrumLevels: int = ...
    """
    Returns or sets  the spectrum levels 
    
    <hr>
    
    Getter Method
    
    Signature ``SpectrumLevels`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpectrumLevels`` 
    
    :param spectrumLevels: 
    :type spectrumLevels: int 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    SurfaceOffset: float = ...
    """
    Returns or sets  the surface offset 
    
    <hr>
    
    Getter Method
    
    Signature ``SurfaceOffset`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SurfaceOffset`` 
    
    :param surfaceOffset: 
    :type surfaceOffset: float 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    TblDepColor: NXOpen.NXColor = ...
    """
    Returns or sets  the table dependent color 
    
    <hr>
    
    Getter Method
    
    Signature ``TblDepColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.1
    
    .. deprecated::  NX12.0.0
       This function is deprecated, Tbl dependent Color can be obtained using :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.DepSelColor`.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TblDepColor`` 
    
    :param tblDepColor: 
    :type tblDepColor: Id 
    
    .. versionadded:: NX6.0.1
    
    .. deprecated::  NX12.0.0
       This function is deprecated, Tbl dependent Color can be set using :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.DepSelColor`.
    
    License requirements: None.
    """
    TblDepDomColor: DisplayPropertiesBuilderDepDomColorEnum = ...
    """
    Returns or sets  the table dependent domain color 
    
    <hr>
    
    Getter Method
    
    Signature ``TblDepDomColor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDepDomColorEnum` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX12.0.0
       This function is deprecated, Tbl dependent Color can be chosen using :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.DepDomColor`.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TblDepDomColor`` 
    
    :param depDomColor: 
    :type depDomColor: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDepDomColorEnum` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX12.0.0
       This function is deprecated, Tbl dependent Color can be chosen using :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.DepDomColor`.
    
    License requirements: None.
    """
    TblDepLabelValues: DisplayPropertiesBuilderDepLabelValueEnum = ...
    """
    Returns or sets  the table dependent label values 
    
    <hr>
    
    Getter Method
    
    Signature ``TblDepLabelValues`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDepLabelValueEnum` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TblDepLabelValues`` 
    
    :param tblDepLabelValues: 
    :type tblDepLabelValues: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderDepLabelValueEnum` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    TblDepPtType: DisplayPropertiesBuilderTblPointTypeEnum = ...
    """
    Returns or sets  the tbl dep pt type 
    
    <hr>
    
    Getter Method
    
    Signature ``TblDepPtType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderTblPointTypeEnum` 
    
    .. versionadded:: NX6.0.1
    
    .. deprecated::  NX12.0.0
       To show source table dependent values use :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.ShowSrcTblVals` to show source table values.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TblDepPtType`` 
    
    :param tblDepPtType: 
    :type tblDepPtType: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderTblPointTypeEnum` 
    
    .. versionadded:: NX6.0.1
    
    .. deprecated::  NX12.0.0
       Source table display no longer uses symbols, so this function has no meaning. Table values are only on or off; to show source table values use :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.ShowSrcTblVals` to show source table values.
    
    License requirements: None.
    """
    TblDepSymbolSize: float = ...
    """
    Returns or sets  the table dependent symbol size 
    
    <hr>
    
    Getter Method
    
    Signature ``TblDepSymbolSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TblDepSymbolSize`` 
    
    :param tblDepSymbolSize: 
    :type tblDepSymbolSize: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    TblIndepColor: NXOpen.NXColor = ...
    """
    Returns or sets  the tbl indep color 
    
    <hr>
    
    Getter Method
    
    Signature ``TblIndepColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.1
    
    .. deprecated::  NX12.0.0
       This function is deprecated. Table independent domain is no longer displayable so this property has no meaning. Dependent domain color can be obtained using :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.DepSelColor`.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TblIndepColor`` 
    
    :param tblIndepColor: 
    :type tblIndepColor: Id 
    
    .. versionadded:: NX6.0.1
    
    .. deprecated::  NX12.0.0
       This function is deprecated. Table independent domain is no longer displayable, so this function has no meaning. Table dependent domain color can be set using :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.DepSelColor`.
    
    License requirements: None.
    """
    TblIndepPtType: DisplayPropertiesBuilderValuesEnum = ...
    """
    Returns or sets  the tbl indep pt type 
    
    <hr>
    
    Getter Method
    
    Signature ``TblIndepPtType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderValuesEnum` 
    
    .. versionadded:: NX6.0.1
    
    .. deprecated::  NX12.0.0
       Table independent domain display no longer modifies the file and is included only to enable old journals to function without modification :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.ShowSrcTblVals` can be used to control source table values, but independent table values display is deprecated.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TblIndepPtType`` 
    
    :param tblIndepPtType: 
    :type tblIndepPtType: :py:class:`NXOpen.Fields.DisplayPropertiesBuilderValuesEnum` 
    
    .. versionadded:: NX6.0.1
    
    .. deprecated::  NX12.0.0
       Table Independent variable display no longer modifies the file and is included only to enable old journals to function without modification. :py:meth:`NXOpen.Fields.DisplayPropertiesBuilder.ShowSrcTblVals` can be used to show source table values, but independent table values display is deprecated.
    
    License requirements: None.
    """
    Translucency: int = ...
    """
    Returns or sets  the translucency 
    
    <hr>
    
    Getter Method
    
    Signature ``Translucency`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Translucency`` 
    
    :param translucency: 
    :type translucency: int 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    UndefValueColor: NXOpen.NXColor = ...
    """
    Returns or sets  the undef value color 
    
    <hr>
    
    Getter Method
    
    Signature ``UndefValueColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UndefValueColor`` 
    
    :param undefValueColor: 
    :type undefValueColor: Id 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    UnderflowColor: NXOpen.NXColor = ...
    """
    Returns or sets  the underflow color 
    
    <hr>
    
    Getter Method
    
    Signature ``UnderflowColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UnderflowColor`` 
    
    :param underflowColor: 
    :type underflowColor: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    XMax: NXOpen.Expression = ...
    """
    Returns  the x max 
    
    <hr>
    
    Getter Method
    
    Signature ``XMax`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    XMin: NXOpen.Expression = ...
    """
    Returns  the x min 
    
    <hr>
    
    Getter Method
    
    Signature ``XMin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    XNum: int = ...
    """
    Returns or sets  the x num 
    
    <hr>
    
    Getter Method
    
    Signature ``XNum`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XNum`` 
    
    :param xNum: 
    :type xNum: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    YMax: NXOpen.Expression = ...
    """
    Returns  the y max 
    
    <hr>
    
    Getter Method
    
    Signature ``YMax`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    YMin: NXOpen.Expression = ...
    """
    Returns  the y min 
    
    <hr>
    
    Getter Method
    
    Signature ``YMin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    YNum: int = ...
    """
    Returns or sets  the y num 
    
    <hr>
    
    Getter Method
    
    Signature ``YNum`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``YNum`` 
    
    :param yNum: 
    :type yNum: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ZMax: NXOpen.Expression = ...
    """
    Returns  the z max 
    
    <hr>
    
    Getter Method
    
    Signature ``ZMax`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ZMin: NXOpen.Expression = ...
    """
    Returns  the z min 
    
    <hr>
    
    Getter Method
    
    Signature ``ZMin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ZNum: int = ...
    """
    Returns or sets  the z num 
    
    <hr>
    
    Getter Method
    
    Signature ``ZNum`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZNum`` 
    
    :param zNum: 
    :type zNum: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: DisplayPropertiesBuilder = ...  # unknown typename


class FieldEvaluatorInterpolationEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FieldEvaluatorInterpolationEnum():
    """
    Interpolation type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No interpolation method; table can only be used as a lookup"
       "Linear1d", "Standard linear interpolation between bounding points"
       "NearestNeighbor1d", "Locates the nearest point and returns its value"
       "InverseDistanceWeighting1d", "Sum of the weighted value of all points, based on the inverse of the distance"
       "Delaunay2dFast", "Triangulates the independent values and uses the bounding triangle, sacrifices accuracy for speed"
       "Delaunay2dMedium", "Triangulates the independent values and uses the bounding triangle, compromise between accuracy and speed"
       "Delaunay2dAccurate", "Triangulates the independent values and uses the bounding triangle, sacrifices speed for accuracy"
       "NearestNeighbor2d", "Locates the nearest point in a plane and returns its value"
       "RenkaShepard2d", "Refined inverse distance weighting in 2D space"
       "InverseDistanceWeighting2d", "Sum of the weighted value of all points in 2D space, based on the inverse of the distance"
       "Delaunay3dFast", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices accuracy for speed"
       "Delaunay3dMedium", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, compromise between accuracy and speed"
       "Delaunay3dAccurate", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices speed for accuracy"
       "NearestNeighbor3d", "Locates the nearest point in space and returns its value"
       "RenkaShepard3d", "Refined inverse distance weighting in 3D space"
       "InverseDistanceWeighting3d", "Sum of the weighted value of all points in 3D space, based on the inverse of the distance"
       "NearestNeighborNd", "Locates the nearest point in N dimensional space and returns its value"
       "RenkaShepardNd", "Refined inverse distance weighting in N dimensional space"
       "InverseDistanceWeightingNd", "Sum of the weighted value of all points in N dimensional, based on the inverse of the distance"
       "ApproxNearestNeighbor2d", "Locates the approximate nearest point in a plane and returns its value"
       "ApproxNearestNeighbor3d", "Locates the approximate nearest point in space and returns its value"
       "ApproxNearestNeighborNd", "Locates the approximate nearest point in N dimensional space and returns its value"
       "Akima1d", "akima interpolation"
       "Akima721d", "akima72 interpolation"
       "Cubic1d", "cubic interpolation"
       "Bilinear2d", "linear interpolation in both directions"
       "Biakima2d", "akima interpolation in both directions"
       "Biakima722d", "akima72 interpolation in both directions"
       "Bicubic2d", "cubic interpolation in both directions"
       "AkimaLinear2d", "akima interpolation in x direction, linear in y direction"
       "Akima72Linear2d", "akima72 interpolation in x direction, linear in y direction"
       "CubicLinear2d", "cubic interpolation in x direction, linear in y direction"
    """
    NotSet = 0  # FieldEvaluatorInterpolationEnumMemberType
    Linear1d = 1  # FieldEvaluatorInterpolationEnumMemberType
    NearestNeighbor1d = 2  # FieldEvaluatorInterpolationEnumMemberType
    InverseDistanceWeighting1d = 3  # FieldEvaluatorInterpolationEnumMemberType
    Delaunay2dFast = 4  # FieldEvaluatorInterpolationEnumMemberType
    Delaunay2dMedium = 5  # FieldEvaluatorInterpolationEnumMemberType
    Delaunay2dAccurate = 6  # FieldEvaluatorInterpolationEnumMemberType
    NearestNeighbor2d = 7  # FieldEvaluatorInterpolationEnumMemberType
    RenkaShepard2d = 8  # FieldEvaluatorInterpolationEnumMemberType
    InverseDistanceWeighting2d = 9  # FieldEvaluatorInterpolationEnumMemberType
    Delaunay3dFast = 10  # FieldEvaluatorInterpolationEnumMemberType
    Delaunay3dMedium = 11  # FieldEvaluatorInterpolationEnumMemberType
    Delaunay3dAccurate = 12  # FieldEvaluatorInterpolationEnumMemberType
    NearestNeighbor3d = 13  # FieldEvaluatorInterpolationEnumMemberType
    RenkaShepard3d = 14  # FieldEvaluatorInterpolationEnumMemberType
    InverseDistanceWeighting3d = 15  # FieldEvaluatorInterpolationEnumMemberType
    NearestNeighborNd = 16  # FieldEvaluatorInterpolationEnumMemberType
    RenkaShepardNd = 17  # FieldEvaluatorInterpolationEnumMemberType
    InverseDistanceWeightingNd = 18  # FieldEvaluatorInterpolationEnumMemberType
    ApproxNearestNeighbor2d = 19  # FieldEvaluatorInterpolationEnumMemberType
    ApproxNearestNeighbor3d = 20  # FieldEvaluatorInterpolationEnumMemberType
    ApproxNearestNeighborNd = 21  # FieldEvaluatorInterpolationEnumMemberType
    Akima1d = 22  # FieldEvaluatorInterpolationEnumMemberType
    Akima721d = 23  # FieldEvaluatorInterpolationEnumMemberType
    Cubic1d = 24  # FieldEvaluatorInterpolationEnumMemberType
    Bilinear2d = 25  # FieldEvaluatorInterpolationEnumMemberType
    Biakima2d = 26  # FieldEvaluatorInterpolationEnumMemberType
    Biakima722d = 27  # FieldEvaluatorInterpolationEnumMemberType
    Bicubic2d = 28  # FieldEvaluatorInterpolationEnumMemberType
    AkimaLinear2d = 29  # FieldEvaluatorInterpolationEnumMemberType
    Akima72Linear2d = 30  # FieldEvaluatorInterpolationEnumMemberType
    CubicLinear2d = 31  # FieldEvaluatorInterpolationEnumMemberType
    
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
    


class FieldEvaluatorLinearLogOptionEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FieldEvaluatorLinearLogOptionEnum():
    """
    Log Options for Linear interpolator 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "LinearLinear", "Standard linear interpolation. Both Independent variable and Dependent variable scaling are linear"
       "LogLinear", "Independent variable scaling is logarithmic (ln), Dependent variable scaling is linear"
       "LinearLog", "Independent variable scaling is linear, Dependent variable scaling is logarithmic (ln)"
       "LogLog", "Both Independent variable and Dependent variable scaling are logarithmic (ln)"
    """
    LinearLinear = 0  # FieldEvaluatorLinearLogOptionEnumMemberType
    LogLinear = 1  # FieldEvaluatorLinearLogOptionEnumMemberType
    LinearLog = 2  # FieldEvaluatorLinearLogOptionEnumMemberType
    LogLog = 3  # FieldEvaluatorLinearLogOptionEnumMemberType
    
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
    


class FieldEvaluatorInverseDistanceWeightingEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FieldEvaluatorInverseDistanceWeightingEnum():
    """
    Options for IDW (inverse weighted distance) interpolator 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", "Sum of the weighted value of all points, based on the inverse of the distance"
       "Radius", "Sum of the weighted value of points within a radius (as a fraction of the bounding box diagonal), based on the inverse of the distance"
       "NearestPoints", "Sum of the weighted value of N nearest points (as a fraction of the total number of points), based on the inverse of the distance"
    """
    All = 0  # FieldEvaluatorInverseDistanceWeightingEnumMemberType
    Radius = 1  # FieldEvaluatorInverseDistanceWeightingEnumMemberType
    NearestPoints = 2  # FieldEvaluatorInverseDistanceWeightingEnumMemberType
    
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
    


class FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FieldEvaluatorValuesOutsideTableInterpolationEnum():
    """
    Options for outside table values interpolation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Undefined", "No interpolation result"
       "Extrapolate", "Extrapolates from the boundary out into space using the same interpolation method that the interpolator for interior table values uses"
       "Constant", "Returns the boundary value as interpolation result"
       "Linear", "Extrapolates from the boundary out into space using the linear extrapolation method"
       "Parabolic", "Extrapolates from the boundary out into space using the parabolic extrapolation method"
       "Cubic", "Extrapolates from the boundary out into space using the cubic extrapolation method"
    """
    Undefined = 0  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
    Extrapolate = 1  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
    Constant = 2  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
    Linear = 3  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
    Parabolic = 4  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
    Cubic = 5  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
    
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
    


class FieldEvaluator(NXOpen.TaggedObject):
    """
    Represents a Field Evaluator which can be used to evaluate a :py:class:`NXOpen.Fields.Field`. 
    
    Use :py:meth:`NXOpen.Fields.Field.GetFieldEvaluator` to obtain an instance of this class
    
    .. versionadded:: NX7.5.2
    """
    
    class InterpolationEnum():
        """
        Interpolation type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No interpolation method; table can only be used as a lookup"
           "Linear1d", "Standard linear interpolation between bounding points"
           "NearestNeighbor1d", "Locates the nearest point and returns its value"
           "InverseDistanceWeighting1d", "Sum of the weighted value of all points, based on the inverse of the distance"
           "Delaunay2dFast", "Triangulates the independent values and uses the bounding triangle, sacrifices accuracy for speed"
           "Delaunay2dMedium", "Triangulates the independent values and uses the bounding triangle, compromise between accuracy and speed"
           "Delaunay2dAccurate", "Triangulates the independent values and uses the bounding triangle, sacrifices speed for accuracy"
           "NearestNeighbor2d", "Locates the nearest point in a plane and returns its value"
           "RenkaShepard2d", "Refined inverse distance weighting in 2D space"
           "InverseDistanceWeighting2d", "Sum of the weighted value of all points in 2D space, based on the inverse of the distance"
           "Delaunay3dFast", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices accuracy for speed"
           "Delaunay3dMedium", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, compromise between accuracy and speed"
           "Delaunay3dAccurate", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices speed for accuracy"
           "NearestNeighbor3d", "Locates the nearest point in space and returns its value"
           "RenkaShepard3d", "Refined inverse distance weighting in 3D space"
           "InverseDistanceWeighting3d", "Sum of the weighted value of all points in 3D space, based on the inverse of the distance"
           "NearestNeighborNd", "Locates the nearest point in N dimensional space and returns its value"
           "RenkaShepardNd", "Refined inverse distance weighting in N dimensional space"
           "InverseDistanceWeightingNd", "Sum of the weighted value of all points in N dimensional, based on the inverse of the distance"
           "ApproxNearestNeighbor2d", "Locates the approximate nearest point in a plane and returns its value"
           "ApproxNearestNeighbor3d", "Locates the approximate nearest point in space and returns its value"
           "ApproxNearestNeighborNd", "Locates the approximate nearest point in N dimensional space and returns its value"
           "Akima1d", "akima interpolation"
           "Akima721d", "akima72 interpolation"
           "Cubic1d", "cubic interpolation"
           "Bilinear2d", "linear interpolation in both directions"
           "Biakima2d", "akima interpolation in both directions"
           "Biakima722d", "akima72 interpolation in both directions"
           "Bicubic2d", "cubic interpolation in both directions"
           "AkimaLinear2d", "akima interpolation in x direction, linear in y direction"
           "Akima72Linear2d", "akima72 interpolation in x direction, linear in y direction"
           "CubicLinear2d", "cubic interpolation in x direction, linear in y direction"
        """
        NotSet = 0  # FieldEvaluatorInterpolationEnumMemberType
        Linear1d = 1  # FieldEvaluatorInterpolationEnumMemberType
        NearestNeighbor1d = 2  # FieldEvaluatorInterpolationEnumMemberType
        InverseDistanceWeighting1d = 3  # FieldEvaluatorInterpolationEnumMemberType
        Delaunay2dFast = 4  # FieldEvaluatorInterpolationEnumMemberType
        Delaunay2dMedium = 5  # FieldEvaluatorInterpolationEnumMemberType
        Delaunay2dAccurate = 6  # FieldEvaluatorInterpolationEnumMemberType
        NearestNeighbor2d = 7  # FieldEvaluatorInterpolationEnumMemberType
        RenkaShepard2d = 8  # FieldEvaluatorInterpolationEnumMemberType
        InverseDistanceWeighting2d = 9  # FieldEvaluatorInterpolationEnumMemberType
        Delaunay3dFast = 10  # FieldEvaluatorInterpolationEnumMemberType
        Delaunay3dMedium = 11  # FieldEvaluatorInterpolationEnumMemberType
        Delaunay3dAccurate = 12  # FieldEvaluatorInterpolationEnumMemberType
        NearestNeighbor3d = 13  # FieldEvaluatorInterpolationEnumMemberType
        RenkaShepard3d = 14  # FieldEvaluatorInterpolationEnumMemberType
        InverseDistanceWeighting3d = 15  # FieldEvaluatorInterpolationEnumMemberType
        NearestNeighborNd = 16  # FieldEvaluatorInterpolationEnumMemberType
        RenkaShepardNd = 17  # FieldEvaluatorInterpolationEnumMemberType
        InverseDistanceWeightingNd = 18  # FieldEvaluatorInterpolationEnumMemberType
        ApproxNearestNeighbor2d = 19  # FieldEvaluatorInterpolationEnumMemberType
        ApproxNearestNeighbor3d = 20  # FieldEvaluatorInterpolationEnumMemberType
        ApproxNearestNeighborNd = 21  # FieldEvaluatorInterpolationEnumMemberType
        Akima1d = 22  # FieldEvaluatorInterpolationEnumMemberType
        Akima721d = 23  # FieldEvaluatorInterpolationEnumMemberType
        Cubic1d = 24  # FieldEvaluatorInterpolationEnumMemberType
        Bilinear2d = 25  # FieldEvaluatorInterpolationEnumMemberType
        Biakima2d = 26  # FieldEvaluatorInterpolationEnumMemberType
        Biakima722d = 27  # FieldEvaluatorInterpolationEnumMemberType
        Bicubic2d = 28  # FieldEvaluatorInterpolationEnumMemberType
        AkimaLinear2d = 29  # FieldEvaluatorInterpolationEnumMemberType
        Akima72Linear2d = 30  # FieldEvaluatorInterpolationEnumMemberType
        CubicLinear2d = 31  # FieldEvaluatorInterpolationEnumMemberType
        
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
        
    
    
    class LinearLogOptionEnum():
        """
        Log Options for Linear interpolator 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "LinearLinear", "Standard linear interpolation. Both Independent variable and Dependent variable scaling are linear"
           "LogLinear", "Independent variable scaling is logarithmic (ln), Dependent variable scaling is linear"
           "LinearLog", "Independent variable scaling is linear, Dependent variable scaling is logarithmic (ln)"
           "LogLog", "Both Independent variable and Dependent variable scaling are logarithmic (ln)"
        """
        LinearLinear = 0  # FieldEvaluatorLinearLogOptionEnumMemberType
        LogLinear = 1  # FieldEvaluatorLinearLogOptionEnumMemberType
        LinearLog = 2  # FieldEvaluatorLinearLogOptionEnumMemberType
        LogLog = 3  # FieldEvaluatorLinearLogOptionEnumMemberType
        
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
        
    
    
    class InverseDistanceWeightingEnum():
        """
        Options for IDW (inverse weighted distance) interpolator 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", "Sum of the weighted value of all points, based on the inverse of the distance"
           "Radius", "Sum of the weighted value of points within a radius (as a fraction of the bounding box diagonal), based on the inverse of the distance"
           "NearestPoints", "Sum of the weighted value of N nearest points (as a fraction of the total number of points), based on the inverse of the distance"
        """
        All = 0  # FieldEvaluatorInverseDistanceWeightingEnumMemberType
        Radius = 1  # FieldEvaluatorInverseDistanceWeightingEnumMemberType
        NearestPoints = 2  # FieldEvaluatorInverseDistanceWeightingEnumMemberType
        
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
        
    
    
    class ValuesOutsideTableInterpolationEnum():
        """
        Options for outside table values interpolation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Undefined", "No interpolation result"
           "Extrapolate", "Extrapolates from the boundary out into space using the same interpolation method that the interpolator for interior table values uses"
           "Constant", "Returns the boundary value as interpolation result"
           "Linear", "Extrapolates from the boundary out into space using the linear extrapolation method"
           "Parabolic", "Extrapolates from the boundary out into space using the parabolic extrapolation method"
           "Cubic", "Extrapolates from the boundary out into space using the cubic extrapolation method"
        """
        Undefined = 0  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
        Extrapolate = 1  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
        Constant = 2  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
        Linear = 3  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
        Parabolic = 4  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
        Cubic = 5  # FieldEvaluatorValuesOutsideTableInterpolationEnumMemberType
        
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
        
    
    
    def GetDependentVariables(self) -> 'list[FieldVariable]':
        """
        Returns the dependent variables for this :py:class:`NXOpen.Fields.FieldEvaluator`  
        
        Signature ``GetDependentVariables()`` 
        
        :returns:  dependent variables for this :py:class:`NXOpen.Fields.FieldEvaluator`   
        :rtype: list of :py:class:`NXOpen.Fields.FieldVariable` 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def GetIndependentVariables(self) -> 'list[FieldVariable]':
        """
        Returns the independent variables for this :py:class:`NXOpen.Fields.FieldEvaluator`  
        
        Signature ``GetIndependentVariables()`` 
        
        :returns:  independent variables for this :py:class:`NXOpen.Fields.FieldEvaluator`   
        :rtype: list of :py:class:`NXOpen.Fields.FieldVariable` 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def SetIndependentVariableValues(self, independentVariable: FieldVariable, values: 'list[float]') -> None:
        """
        Sets values at which the Field will be evaluated for this independent variable :py:class:`NXOpen.Fields.FieldVariable`.  
        
        The number of input values mush be the same for independent variables and these values are assumed to be in the same units as the 
        independent variable :py:class:`NXOpen.Fields.FieldVariable`.   
        
        Signature ``SetIndependentVariableValues(independentVariable, values)`` 
        
        :param independentVariable:  independent variable whose values are being set.  
        :type independentVariable: :py:class:`NXOpen.Fields.FieldVariable` 
        :param values:  the values for this independent variable where the field will be evaluated at.  
        :type values: list of float 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def Evaluate(self, dependentVariable: FieldVariable) -> 'list[float]':
        """
        Evaluate the Field at the specified independent variable :py:class:`NXOpen.Fields.FieldVariable` values and return the values for the specified dependent variable.  
        
        The number of output values will be the same as number of independent variables specified and these values will be in the same units as the 
        dependent variable :py:class:`NXOpen.Fields.FieldVariable`.   
        
        Signature ``Evaluate(dependentVariable)`` 
        
        :param dependentVariable:  dependent variable whose values are to be evaluated  
        :type dependentVariable: :py:class:`NXOpen.Fields.FieldVariable` 
        :returns:  the values evaluated for this dependent variable  
        :rtype: list of float 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def Delete(self) -> None:
        """
        Delete this field evaluator; destroys the field evaluator and removes all references to it.  
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    InterpolationMethod: FieldEvaluatorInterpolationEnum = ...
    """
    Returns or sets   
    the interpolation method used when this table data is evaluated.  
    
    <hr>
    
    Getter Method
    
    Signature ``InterpolationMethod`` 
    
    :returns:  the interpolation method    
    :rtype: :py:class:`NXOpen.Fields.FieldEvaluatorInterpolationEnum` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpolationMethod`` 
    
    :param interpolationMethod:  the interpolation method   
    :type interpolationMethod: :py:class:`NXOpen.Fields.FieldEvaluatorInterpolationEnum` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    """
    Null: FieldEvaluator = ...  # unknown typename


class ComplexVectorFieldWrapper(NXOpen.NXObject):
    """
    This class defines a complex value that is internally 
    backed up by a  field or six expressions.  
    
    .. versionadded:: NX12.0.0
    """
    
    def SetExpressions(self, expressions: 'list[NXOpen.Expression]') -> None:
        """
        Sets the implementation of the wrapper to the specified expressions 
        
        Signature ``SetExpressions(expressions)`` 
        
        :param expressions:  existing expressions that will be this wrapper's value  
        :type expressions: list of :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetExpressionByIndex(self, index: int) -> NXOpen.Expression:
        """
        Returns the indicated implementation if the wrapper is backed up by expressions; 
        NULL otherwise  
        
        Signature ``GetExpressionByIndex(index)`` 
        
        :param index:  0, 1 or 2  
        :type index: int 
        :returns:  existing expression or NULL  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetImaginaryExpressions(self, expressions: 'list[NXOpen.Expression]') -> None:
        """
        Sets the implementation of the wrapper to the specified expressions 
        
        Signature ``SetImaginaryExpressions(expressions)`` 
        
        :param expressions:  existing expressions that will be this wrapper's value  
        :type expressions: list of :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetImaginaryExpressionByIndex(self, index: int) -> NXOpen.Expression:
        """
        Returns the indicated implementation if the wrapper is backed up by expressions; 
        NULL otherwise  
        
        Signature ``GetImaginaryExpressionByIndex(index)`` 
        
        :param index:  0, 1 or 2  
        :type index: int 
        :returns:  existing expression or NULL  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetField(self, field: Field, scaleFactor: float) -> None:
        """
        Sets the implementation of the wrapper to the specified field 
        
        Signature ``SetField(field, scaleFactor)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :param scaleFactor:  the field will be multiplied by this scale factor when being evaluated  
        :type scaleFactor: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetField(self) -> Field:
        """
        Returns the implementation if the wrapper is backed up by a field; 
        NULL otherwise  
        
        Signature ``GetField()`` 
        
        :returns:  existing field or NULL  
        :rtype: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ComplexVectorFieldWrapper = ...  # unknown typename


class VectorFieldWrapper(NXOpen.NXObject):
    """
    This class defines a vector value that is internally 
    backed up by a (optionally scaled) field or three expressions.  
    
    .. versionadded:: NX6.0.0
    """
    
    def SetExpressions(self, expressions: 'list[NXOpen.Expression]') -> None:
        """
        Sets the implementation of the wrapper to the specified expressions 
        
        Signature ``SetExpressions(expressions)`` 
        
        :param expressions:  existing expressions that will be this wrapper's value  
        :type expressions: list of :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetExpressionByIndex(self, index: int) -> NXOpen.Expression:
        """
        Returns the indicated implementation if the wrapper is backed up by expressions; 
        NULL otherwise  
        
        Signature ``GetExpressionByIndex(index)`` 
        
        :param index:  0, 1 or 2  
        :type index: int 
        :returns:  existing expression or NULL  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetField(self, field: Field, scaleFactors: 'list[float]') -> None:
        """
        Sets the implementation of the wrapper to the specified field 
        
        Signature ``SetField(field, scaleFactors)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :param scaleFactors:  the field will be multiplied by this scale factor when being evaluated  
        :type scaleFactors: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetField(self) -> Field:
        """
        Returns the implementation if the wrapper is backed up by a field; 
        NULL otherwise  
        
        Signature ``GetField()`` 
        
        :returns:  existing field or NULL  
        :rtype: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    Null: VectorFieldWrapper = ...  # unknown typename


class FieldExpression(Field):
    """
    Represents the Field Expression class. 
    
    A field (see :py:class:`NXOpen.Fields.Field`) which has **<tt>exactly one</tt></b> dependent
    variable (see :py:class:`NXOpen.Fields.FieldVariable`), where the field function defintions
    is implemented using the NX Expression sub-system :py:class:`NXOpen.Expression`.
    
    .. versionadded:: NX4.0.0
    """
    
    def EditFieldExpression(self, fieldExpString: str, unitType: NXOpen.Unit, indepVarArray: 'list[FieldVariable]', updateFlag: bool) -> None:
        """
        Edit the expression field.  
        
        Specifies the new expression string and the array of variables used
        in the expression string.  Field expressions are children of
        :py:class:`NXOpen.Fields.FieldFormula`.
        
        Signature ``EditFieldExpression(fieldExpString, unitType, indepVarArray, updateFlag)`` 
        
        :param fieldExpString:  expression string to be associated with the field  
        :type fieldExpString: str 
        :param unitType:  unit of the field  
        :type unitType: :py:class:`NXOpen.Unit` 
        :param indepVarArray:  independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param updateFlag:  update flag  
        :type updateFlag: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFieldExpressionString(self, fieldExpString: str, updateFlag: bool) -> None:
        """
        Sets the new expression string to the expression field 
        
        Signature ``SetFieldExpressionString(fieldExpString, updateFlag)`` 
        
        :param fieldExpString:  expression string to be associated with the field  
        :type fieldExpString: str 
        :param updateFlag:  update flag  
        :type updateFlag: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFieldExpressionString(self) -> str:
        """
        Gets the expression string of the expression field  
        
        Signature ``GetFieldExpressionString()`` 
        
        :returns:  expression string associated with the field  
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: FieldExpression = ...  # unknown typename


class ComplexScalarFieldWrapper(NXOpen.NXObject):
    """
    This class defines a complex value that is internally 
    backed up by a  field or two expressions.  
    
    .. versionadded:: NX11.0.0
    """
    
    def SetExpression(self, expression: NXOpen.Expression) -> None:
        """
        Sets the implementation of the wrapper to the specified expressions 
        
        Signature ``SetExpression(expression)`` 
        
        :param expression:  existing expressions that will be this wrapper's value  
        :type expression: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetExpression(self) -> NXOpen.Expression:
        """
        Returns the indicated implementation if the wrapper is backed up by expressions; 
        NULL otherwise  
        
        Signature ``GetExpression()`` 
        
        :returns:  existing expression or NULL  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetImaginaryExpression(self, expression: NXOpen.Expression) -> None:
        """
        Sets the implementation of the wrapper to the specified expressions 
        
        Signature ``SetImaginaryExpression(expression)`` 
        
        :param expression:  existing expressions that will be this wrapper's value  
        :type expression: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetImaginaryExpression(self) -> NXOpen.Expression:
        """
        Returns the indicated implementation if the wrapper is backed up by expressions; 
        NULL otherwise  
        
        Signature ``GetImaginaryExpression()`` 
        
        :returns:  existing expression or NULL  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetField(self, field: Field) -> None:
        """
        Sets the implementation of the wrapper to the specified field 
        
        Signature ``SetField(field)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetField(self) -> Field:
        """
        Returns the implementation if the wrapper is backed up by a field; 
        NULL otherwise  
        
        Signature ``GetField()`` 
        
        :returns:  existing field or NULL  
        :rtype: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFieldWithScaleFactor(self, field: Field, scaleFactor: float) -> None:
        """
        Sets the implementation of the wrapper to the specified field and scale factor 
        
        Signature ``SetFieldWithScaleFactor(field, scaleFactor)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :param scaleFactor:  the field will be multiplied by this scale factor when being evaluated  
        :type scaleFactor: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ComplexScalarFieldWrapper = ...  # unknown typename


class ScalarFieldWrapper(NXOpen.NXObject):
    """
    This class defines a scalar value that is internally 
    backed up by a (optionally scaled) field or an expression.  
    
    .. versionadded:: NX6.0.0
    """
    
    def SetExpression(self, expression: NXOpen.Expression) -> None:
        """
        Sets the implementation of the wrapper to the specified expression 
        
        Signature ``SetExpression(expression)`` 
        
        :param expression:  an existing expression that will be this wrapper's value  
        :type expression: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetExpression(self) -> NXOpen.Expression:
        """
        Returns the implementation if the wrapper is backed up by an expression;
        NULL otherwise  
        
        Signature ``GetExpression()`` 
        
        :returns:  an existing expression or NULL  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetField(self, field: Field, scaleFactor: float) -> None:
        """
        Sets the implementation of the wrapper to the specified field 
        
        Signature ``SetField(field, scaleFactor)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :param scaleFactor:  the field will be multiplied by this scale factor when being evaluated  
        :type scaleFactor: float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetField(self) -> Field:
        """
        Returns the implementation if the wrapper is backed up by a field;
        NULL otherwise  
        
        Signature ``GetField()`` 
        
        :returns:  an existing field or NULL  
        :rtype: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFieldScaleFactor(self) -> float:
        """
        Returns the scale factor to be applied to the field, this is only applicable if the wrapper is backed up by a field  
        
        Signature ``GetFieldScaleFactor()`` 
        
        :returns:  the field will be multiplied by this scale factor when being evaluated  
        :rtype: float 
        
        .. versionadded:: NX8.0.3
        
        License requirements: None.
        """
        ...
    
    Null: ScalarFieldWrapper = ...  # unknown typename


class ExportData(NXOpen.TransientObject):
    """
    Represents data for field export  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Fields.FieldManager.CreateExportData`
    
    .. versionadded:: NX6.0.0
    """
    
    def AddField(self, field: Field) -> None:
        """
        Add a field 
        
        Signature ``AddField(field)`` 
        
        :param field:  field to add  
        :type field: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddFields(self, fields: 'list[Field]') -> None:
        """
        Add a field 
        
        Signature ``AddFields(fields)`` 
        
        :param fields:  fields to add  
        :type fields: list of :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFileName(self, fileName: str) -> None:
        """
        Set file name 
        
        Signature ``SetFileName(fileName)`` 
        
        :param fileName:  file name  
        :type fileName: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFields(self) -> 'list[Field]':
        """
        Gets the fields 
        
        Signature ``GetFields()`` 
        
        :returns:  fields  
        :rtype: list of :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFileName(self) -> str:
        """
        Get file name  
        
        Signature ``GetFileName()`` 
        
        :returns:  file name  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Destroys the object 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    


class ImportData(NXOpen.TransientObject):
    """
    Represents data transfer objectst for field import  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Fields.FieldManager.CreateImportData`
    
    .. versionadded:: NX6.0.0
    """
    
    def SetFileName(self, fileName: str) -> None:
        """
        Set file name 
        
        Signature ``SetFileName(fileName)`` 
        
        :param fileName:  file name  
        :type fileName: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFileName(self) -> str:
        """
        Get file name  
        
        Signature ``GetFileName()`` 
        
        :returns:  file name  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFields(self) -> 'list[Field]':
        """
        Return the fields that have been imported 
        
        Signature ``GetFields()`` 
        
        :returns:  the fields that have been imported  
        :rtype: list of :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetMessages(self) -> 'list[str]':
        """
        Return any diagnostic messages 
        
        Signature ``GetMessages()`` 
        
        :returns:  the diagnostic messages if any  
        :rtype: list of str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Destroys the object 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    


class FieldManager(NXOpen.NXObject):
    """
    Represents the manager class of the Fields  
    
    This manager class gives access to all the fields :py:class:`NXOpen.Fields.Field` within a part, 
    as well as the collection of domains :py:class:`NXOpen.Fields.FieldDomain`.
    
    It also provides creation methods for the various builders of fields and related classes.
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def CreateFieldExpression(self, fieldExpString: str, unitType: NXOpen.Unit) -> FieldExpression:
        """
        Creates a system :py:class:`NXOpen.Fields.FieldExpression` object.  Specifies the new expression 
        string.
        
        Signature ``CreateFieldExpression(fieldExpString, unitType)`` 
        
        :param fieldExpString:  expression string to be associated with the field  
        :type fieldExpString: str 
        :param unitType:  unit of the field  
        :type unitType: :py:class:`NXOpen.Unit` 
        :returns:  field  
        :rtype: :py:class:`NXOpen.Fields.FieldExpression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateFieldExpression(self, fieldExpString: str, unitType: NXOpen.Unit, indepVarArray: 'list[FieldVariable]') -> FieldExpression:
        """
        Creates a system :py:class:`NXOpen.Fields.FieldExpression` object with independent variables.
        Specifies the new expression string.
        
        This method is deprecated; field expressions are children of 
        :py:class:`NXOpen.Fields.FieldFormula` and should not be created independently.
        
        Signature ``CreateFieldExpression(fieldExpString, unitType, indepVarArray)`` 
        
        :param fieldExpString:  expression string to be associated with the field  
        :type fieldExpString: str 
        :param unitType:  unit of the field  
        :type unitType: :py:class:`NXOpen.Unit` 
        :param indepVarArray:  independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :returns:  field  
        :rtype: :py:class:`NXOpen.Fields.FieldExpression` 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Field expressions are owned by other objects.  They are managed by the creation and editing of the owning object and should not be created independently.
        
        License requirements: None.
        """
        ...
    
    
    def CreateSubFieldExpression(self, depVar: FieldVariable) -> FieldExpression:
        """
        Creates a system :py:class:`NXOpen.Fields.FieldExpression` object with independent variables.  
        
        Specifies the new expression string.
        
        This method is used to create sub expression fields for a 
        :py:class:`NXOpen.Fields.FieldFormula`.
        
        Signature ``CreateSubFieldExpression(depVar)`` 
        
        :param depVar:  dependent variables to be associated with the field  
        :type depVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :returns:  field  
        :rtype: :py:class:`NXOpen.Fields.FieldExpression` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateFieldFormula(self, fieldName: str, indepVarArray: 'list[FieldVariable]', depExpArray: 'list[FieldExpression]') -> FieldFormula:
        """
        Creates a :py:class:`NXOpen.Fields.FieldFormula` object with dependent :py:class:`NXOpen.Fields.FieldExpression`.  
        
        Signature ``CreateFieldFormula(fieldName, indepVarArray, depExpArray)`` 
        
        :param fieldName:  field name  
        :type fieldName: str 
        :param indepVarArray:  independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param depExpArray:  dependent expression fields to be associated with the formula field  
        :type depExpArray: list of :py:class:`NXOpen.Fields.FieldExpression` 
        :returns:  field  
        :rtype: :py:class:`NXOpen.Fields.FieldFormula` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateFieldTable(self, fieldName: str, indepVarArray: 'list[FieldVariable]', depVarArray: 'list[FieldVariable]', datapoints: 'list[float]') -> FieldTable:
        """
        Creates a :py:class:`NXOpen.Fields.FieldTable` object with dependent and independent variables 
        :py:class:`NXOpen.Fields.FieldVariable`.  
        
        Signature ``CreateFieldTable(fieldName, indepVarArray, depVarArray, datapoints)`` 
        
        :param fieldName:  field name  
        :type fieldName: str 
        :param indepVarArray:  independent variables to be associated with the table field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param depVarArray:  dependent variables to be associated with the table field  
        :type depVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param datapoints:  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows.  
        :type datapoints: list of float 
        :returns:  field  
        :rtype: :py:class:`NXOpen.Fields.FieldTable` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateFieldTableFromData(self, fieldNamePrefix: str, ivarUnit: NXOpen.Unit, dvarUnit: NXOpen.Unit, dvarType: FieldVariableValueType, datapoints: 'list[float]') -> FieldTable:
        """
        Creates a :py:class:`NXOpen.Fields.FieldTable` object with dependent and independent variables
        :py:class:`NXOpen.Fields.FieldVariable`.  
        
        This will create a 2 dimensional table, with the option to specify 
        the value type for the dependent variable.
        
        Signature ``CreateFieldTableFromData(fieldNamePrefix, ivarUnit, dvarUnit, dvarType, datapoints)`` 
        
        :param fieldNamePrefix:  field name prefix; e.g. "AFU Record"; field will have a unique generated name begining with this string  
        :type fieldNamePrefix: str 
        :param ivarUnit:  unit of the independent variable  
        :type ivarUnit: :py:class:`NXOpen.Unit` 
        :param dvarUnit:  unit of the dependent variable  
        :type dvarUnit: :py:class:`NXOpen.Unit` 
        :param dvarType:  dependent variable type (real/imaginary/complex...)  
        :type dvarType: :py:class:`NXOpen.Fields.FieldVariableValueType` 
        :param datapoints:  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows.  
        :type datapoints: list of float 
        :returns:  field  
        :rtype: :py:class:`NXOpen.Fields.FieldTable` 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def CreateFieldLink(self, fieldName: str, fieldToLink: Field) -> FieldLink:
        """
        Creates a :py:class:`NXOpen.Fields.FieldLink`.  
        
        Signature ``CreateFieldLink(fieldName, fieldToLink)`` 
        
        :param fieldName:  field name  
        :type fieldName: str 
        :param fieldToLink:  field to link  
        :type fieldToLink: :py:class:`NXOpen.Fields.Field` 
        :returns:  field  
        :rtype: :py:class:`NXOpen.Fields.FieldLink` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteField(self, field: Field) -> Field:
        """
        Deletes the specified :py:class:`NXOpen.Fields.Field` object; if the object cannot be deleted
        it is returned.  
        
        Signature ``DeleteField(field)`` 
        
        :param field:  field to delete  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :returns:  If the field cannot be deleted, it is returned; if the field is deleted, this will be NULL  
        :rtype: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateIndependentVariable(self, ownerField: Field, nameVariable: NameVariable, unitType: NXOpen.Unit, minValueSet: bool, minValueInclusive: bool, minValue: float, maxValueSet: bool, maxValueInclusive: bool, maxValue: float, numPtsSet: bool, numPts: int, defaultValueSet: bool, defaultValue: float) -> FieldVariable:
        """
        Create an independent variable to be added to the field 
        
        Signature ``CreateIndependentVariable(ownerField, nameVariable, unitType, minValueSet, minValueInclusive, minValue, maxValueSet, maxValueInclusive, maxValue, numPtsSet, numPts, defaultValueSet, defaultValue)`` 
        
        :param ownerField:  owner field  
        :type ownerField: :py:class:`NXOpen.Fields.Field` 
        :param nameVariable:  existing name variable  
        :type nameVariable: :py:class:`NXOpen.Fields.NameVariable` 
        :param unitType:  unit of the independent variable  
        :type unitType: :py:class:`NXOpen.Unit` 
        :param minValueSet:  logical value whether minimum value set  
        :type minValueSet: bool 
        :param minValueInclusive:  minimum value is itself included in range  
        :type minValueInclusive: bool 
        :param minValue:  minimum value of the variable range  
        :type minValue: float 
        :param maxValueSet:  logical value whether maximum value set  
        :type maxValueSet: bool 
        :param maxValueInclusive:  maximum value is itself included in range  
        :type maxValueInclusive: bool 
        :param maxValue:  maximum value of the variable range  
        :type maxValue: float 
        :param numPtsSet:  logical value whether num_pts set  
        :type numPtsSet: bool 
        :param numPts:  num_pts of the variable range  
        :type numPts: int 
        :param defaultValueSet:  logical value whether default value set  
        :type defaultValueSet: bool 
        :param defaultValue:  default value of the variable range  
        :type defaultValue: float 
        :returns:  independent variable created and associated to the field  
        :rtype: :py:class:`NXOpen.Fields.FieldVariable` 
        
        .. versionadded:: NX6.0.2
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateIndependentVariable(self, ownerField: Field, nameVariable: NameVariable, unitType: NXOpen.Unit, type: FieldVariableValueType, minValueSet: bool, minValueInclusive: bool, minValue: float, maxValueSet: bool, maxValueInclusive: bool, maxValue: float, numPtsSet: bool, numPts: int, defaultValueSet: bool, defaultValue: float) -> FieldVariable:
        """
        Create an independent variable to be added to the field, specifying the variable value type
        
        Signature ``CreateIndependentVariable(ownerField, nameVariable, unitType, type, minValueSet, minValueInclusive, minValue, maxValueSet, maxValueInclusive, maxValue, numPtsSet, numPts, defaultValueSet, defaultValue)`` 
        
        :param ownerField:  owner field  
        :type ownerField: :py:class:`NXOpen.Fields.Field` 
        :param nameVariable:  existing name variable  
        :type nameVariable: :py:class:`NXOpen.Fields.NameVariable` 
        :param unitType:  unit of the independent variable  
        :type unitType: :py:class:`NXOpen.Unit` 
        :param type:  variable value type  
        :type type: :py:class:`NXOpen.Fields.FieldVariableValueType` 
        :param minValueSet:  logical value whether minimum value set  
        :type minValueSet: bool 
        :param minValueInclusive:  minimum value is itself included in range  
        :type minValueInclusive: bool 
        :param minValue:  minimum value of the variable range  
        :type minValue: float 
        :param maxValueSet:  logical value whether maximum value set  
        :type maxValueSet: bool 
        :param maxValueInclusive:  maximum value is itself included in range  
        :type maxValueInclusive: bool 
        :param maxValue:  maximum value of the variable range  
        :type maxValue: float 
        :param numPtsSet:  logical value whether num_pts set  
        :type numPtsSet: bool 
        :param numPts:  num_pts of the variable range  
        :type numPts: int 
        :param defaultValueSet:  logical value whether default value set  
        :type defaultValueSet: bool 
        :param defaultValue:  default value of the variable range  
        :type defaultValue: float 
        :returns:  independent variable created and associated to the field  
        :rtype: :py:class:`NXOpen.Fields.FieldVariable` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def EditIndependentVariable(self, indepVar: FieldVariable, varName: str, unitType: NXOpen.Unit, minValueSet: bool, minValueInclusive: bool, minValue: float, maxValueSet: bool, maxValueInclusive: bool, maxValue: float, numPtsSet: bool, numPts: int, defaultValueSet: bool, defaultValue: float) -> None:
        """
        Edit an independent variable 
        
        Signature ``EditIndependentVariable(indepVar, varName, unitType, minValueSet, minValueInclusive, minValue, maxValueSet, maxValueInclusive, maxValue, numPtsSet, numPts, defaultValueSet, defaultValue)`` 
        
        :param indepVar:  indep var to edit  
        :type indepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param varName:  name of the independent variable to be created  
        :type varName: str 
        :param unitType:  unit of the independent variable  
        :type unitType: :py:class:`NXOpen.Unit` 
        :param minValueSet:  logical value whether minimum value set  
        :type minValueSet: bool 
        :param minValueInclusive:  minimum value is itself included in range  
        :type minValueInclusive: bool 
        :param minValue:  minimum value of the variable range  
        :type minValue: float 
        :param maxValueSet:  logical value whether maximum value set  
        :type maxValueSet: bool 
        :param maxValueInclusive:  maximum value is itself included in range  
        :type maxValueInclusive: bool 
        :param maxValue:  maximum value of the variable range  
        :type maxValue: float 
        :param numPtsSet:  logical value whether num_pts set  
        :type numPtsSet: bool 
        :param numPts:  num_pts of the variable range  
        :type numPts: int 
        :param defaultValueSet:  logical value whether default value set  
        :type defaultValueSet: bool 
        :param defaultValue:  default value of the variable range  
        :type defaultValue: float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def EditIndependentVariable(self, indepVar: FieldVariable, unitType: NXOpen.Unit) -> None:
        """
        Edit an independent variable 
        
        Signature ``EditIndependentVariable(indepVar, unitType)`` 
        
        :param indepVar:  indep var to edit  
        :type indepVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param unitType:  unit of the independent variable  
        :type unitType: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateDependentVariable(self, ownerField: Field, nameVariable: NameVariable, unitType: NXOpen.Unit) -> FieldVariable:
        """
        Create a dependent variable to be added to the field 
        
        Signature ``CreateDependentVariable(ownerField, nameVariable, unitType)`` 
        
        :param ownerField:  owner field  
        :type ownerField: :py:class:`NXOpen.Fields.Field` 
        :param nameVariable:  existing name variable  
        :type nameVariable: :py:class:`NXOpen.Fields.NameVariable` 
        :param unitType:  unit of the dependent variable  
        :type unitType: :py:class:`NXOpen.Unit` 
        :returns:  dependent variable created and associated to the field  
        :rtype: :py:class:`NXOpen.Fields.FieldVariable` 
        
        .. versionadded:: NX6.0.2
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateDependentVariable(self, ownerField: Field, nameVariable: NameVariable, unitType: NXOpen.Unit, type: FieldVariableValueType) -> FieldVariable:
        """
        Create a dependent variable to be added to the field, specifying the variable value type 
        
        Signature ``CreateDependentVariable(ownerField, nameVariable, unitType, type)`` 
        
        :param ownerField:  owner field  
        :type ownerField: :py:class:`NXOpen.Fields.Field` 
        :param nameVariable:  existing name variable  
        :type nameVariable: :py:class:`NXOpen.Fields.NameVariable` 
        :param unitType:  unit of the dependent variable  
        :type unitType: :py:class:`NXOpen.Unit` 
        :param type:  variable value type  
        :type type: :py:class:`NXOpen.Fields.FieldVariableValueType` 
        :returns:  dependent variable created and associated to the field  
        :rtype: :py:class:`NXOpen.Fields.FieldVariable` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def EditDependentVariable(self, depVar: FieldVariable, varName: str, unitType: NXOpen.Unit) -> None:
        """
        Edit dependent variable 
        
        Signature ``EditDependentVariable(depVar, varName, unitType)`` 
        
        :param depVar:  dep variable to edit  
        :type depVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param varName:  new name for variable, or NULL to skip updating name  
        :type varName: str 
        :param unitType:  new unit of the dependent variable  
        :type unitType: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def EditDependentVariable(self, depVar: FieldVariable, unitType: NXOpen.Unit) -> None:
        """
        Edit dependent variable 
        
        Signature ``EditDependentVariable(depVar, unitType)`` 
        
        :param depVar:  dep variable to edit  
        :type depVar: :py:class:`NXOpen.Fields.FieldVariable` 
        :param unitType:  new unit of the dependent variable  
        :type unitType: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateFieldWrapper(self, field: Field) -> FieldWrapper:
        """
        Create a field wrapper backed up by a field  
        
        Signature ``CreateFieldWrapper(field)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :returns:  scalar field wrapper created and associated to the field  
        :rtype: :py:class:`NXOpen.Fields.FieldWrapper` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateScalarFieldWrapperWithExpression(self, expression: NXOpen.Expression) -> ScalarFieldWrapper:
        """
        Create a field wrapper backed by a scalar expression  
        
        Signature ``CreateScalarFieldWrapperWithExpression(expression)`` 
        
        :param expression:  an existing expression that will be this wrapper's value  
        :type expression: :py:class:`NXOpen.Expression` 
        :returns:  scalar field wrapper created and associated to the expression  
        :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateScalarFieldWrapperWithField(self, field: Field, scaleFactor: float) -> ScalarFieldWrapper:
        """
        Create a scalar field wrapper backed up by a scaled scalar field  
        
        Signature ``CreateScalarFieldWrapperWithField(field, scaleFactor)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :param scaleFactor:  the field will be multiplied by this scale factor when being evaluated  
        :type scaleFactor: float 
        :returns:  scalar field wrapper created and associated to the field  
        :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateVectorFieldWrapperWithExpressions(self, expressions: 'list[NXOpen.Expression]') -> VectorFieldWrapper:
        """
        Create a vector field wrapper backed by three scalar expressions  
        
        Signature ``CreateVectorFieldWrapperWithExpressions(expressions)`` 
        
        :param expressions:  existing expressions that will be this wrapper's value  
        :type expressions: list of :py:class:`NXOpen.Expression` 
        :returns:  scalar field wrapper created and associated to the expression  
        :rtype: :py:class:`NXOpen.Fields.VectorFieldWrapper` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateVectorFieldWrapperWithField(self, field: Field, scaleFactors: 'list[float]') -> VectorFieldWrapper:
        """
        Create a vector field wrapper backed up by a scaled vector field  
        
        Signature ``CreateVectorFieldWrapperWithField(field, scaleFactors)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :param scaleFactors:  the field will be multiplied by this scale factor when being evaluated  
        :type scaleFactors: list of float 
        :returns:  vector field wrapper created and associated to the field  
        :rtype: :py:class:`NXOpen.Fields.VectorFieldWrapper` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateComplexScalarFieldWrapperWithExpressions(self, expressions: 'list[NXOpen.Expression]') -> ComplexScalarFieldWrapper:
        """
        Create a complex scalar field wrapper backed by two scalar expressions  
        
        Signature ``CreateComplexScalarFieldWrapperWithExpressions(expressions)`` 
        
        :param expressions:  existing expressions that will be this wrapper's value  
        :type expressions: list of :py:class:`NXOpen.Expression` 
        :returns:  scalar field wrapper created and associated to the expression  
        :rtype: :py:class:`NXOpen.Fields.ComplexScalarFieldWrapper` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateComplexScalarFieldWrapperWithField(self, field: Field) -> ComplexScalarFieldWrapper:
        """
        Create a complex scalar field wrapper backed up by a complex scalar field  
        
        Signature ``CreateComplexScalarFieldWrapperWithField(field)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :returns:  vector field wrapper created and associated to the field  
        :rtype: :py:class:`NXOpen.Fields.ComplexScalarFieldWrapper` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDisplayPropertiesBuilder(self, fieldArray: 'list[Field]') -> DisplayPropertiesBuilder:
        """
        Creates a :py:class:`NXOpen.Fields.DisplayPropertiesBuilder`  
        
        Signature ``CreateDisplayPropertiesBuilder(fieldArray)`` 
        
        :param fieldArray:  fields to edit display properties  
        :type fieldArray: list of :py:class:`NXOpen.Fields.Field` 
        :returns: 
        :rtype: :py:class:`NXOpen.Fields.DisplayPropertiesBuilder` 
        
        .. versionadded:: NX6.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CreateSpatialMapBuilder(self, spatialmap: SpatialMap) -> SpatialMapBuilder:
        """
        Creates a :py:class:`NXOpen.Fields.SpatialMapBuilder`  
        
        Signature ``CreateSpatialMapBuilder(spatialmap)`` 
        
        :param spatialmap:  Existing SpatialMap to edit; NULL to create  
        :type spatialmap: :py:class:`NXOpen.Fields.SpatialMap` 
        :returns: 
        :rtype: :py:class:`NXOpen.Fields.SpatialMapBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateExportData(self) -> ExportData:
        """
        Creates a Fields.  
        
        ExportData  
        
        Signature ``CreateExportData()`` 
        
        :returns:  the export data created  
        :rtype: :py:class:`NXOpen.Fields.ExportData` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ExportFields(self, exportData: ExportData) -> None:
        """
        Exports fields to a text file as defined by export_data parameter 
        
        Signature ``ExportFields(exportData)`` 
        
        :param exportData:  Export data  
        :type exportData: :py:class:`NXOpen.Fields.ExportData` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateImportData(self) -> ImportData:
        """
        Creates a Fields.  
        
        ImportData  
        
        Signature ``CreateImportData()`` 
        
        :returns:  the import data created  
        :rtype: :py:class:`NXOpen.Fields.ImportData` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ImportFields(self, importData: ImportData) -> None:
        """
        Imports fields from a text file as defined by import_data parameter 
        
        Signature ``ImportFields(importData)`` 
        
        :param importData:  Import data  
        :type importData: :py:class:`NXOpen.Fields.ImportData` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreatePathObjects(self) -> PathObjects:
        """
        Creates a :py:class:`NXOpen.Fields.PathObjects`  
        
        Signature ``CreatePathObjects()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Fields.PathObjects` 
        
        .. versionadded:: NX6.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetNameVariable(self, variableName: str, measureName: str) -> NameVariable:
        """
        Locate an existing, or create a new :py:class:`NXOpen.Fields.NameVariable` object  
        
        Signature ``GetNameVariable(variableName, measureName)`` 
        
        :param variableName:  alphanumeric string; if it matches an existing name variable, the measures must also match  
        :type variableName: str 
        :param measureName:  must match an existing measure name, or "Unitless"  
        :type measureName: str 
        :returns:  name variable with the specified measure and name  
        :rtype: :py:class:`NXOpen.Fields.NameVariable` 
        
        .. versionadded:: NX6.0.2
        
        License requirements: None.
        """
        ...
    
    
    def GetValidFieldId(self) -> int:
        """
        Get the next available ID for :py:class:`NXOpen.Fields.Field` object  
        
        Signature ``GetValidFieldId()`` 
        
        :returns:  valid id  
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateFieldLinksTable(self, fieldName: str, indepVarArray: 'list[FieldVariable]', depVarArray: 'list[FieldVariable]', datapoints: 'list[float]', linkFieldsArray: 'list[Field]') -> FieldLinksTable:
        """
        Creates a :py:class:`NXOpen.Fields.FieldLinksTable` object with dependent and independent variables 
        :py:class:`NXOpen.Fields.FieldVariable`.
        
        Signature ``CreateFieldLinksTable(fieldName, indepVarArray, depVarArray, datapoints, linkFieldsArray)`` 
        
        :param fieldName:  field name  
        :type fieldName: str 
        :param indepVarArray:  independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param depVarArray:  dependent variables of this and all linked fields  
        :type depVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param datapoints:  row based array of double values representing the first independent variable; the number of points should equal the number of rows.  
        :type datapoints: list of float 
        :param linkFieldsArray:  row based array of link field values representing the table; the number of fields should equal the number of rows. 
        :type linkFieldsArray: list of :py:class:`NXOpen.Fields.Field` 
        :returns:  links table field  
        :rtype: :py:class:`NXOpen.Fields.FieldLinksTable` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateFieldLinksTable(self, fieldName: str, indepVarArray: 'list[FieldVariable]', depVarArray: 'list[FieldVariable]', datapoints: 'list[float]', linkFieldsArray: 'list[Field]', managedFieldsArray: 'list[bool]') -> FieldLinksTable:
        """
        Creates a :py:class:`NXOpen.Fields.FieldLinksTable` object with dependent and independent variables 
        :py:class:`NXOpen.Fields.FieldVariable`.
        
        Signature ``CreateFieldLinksTable(fieldName, indepVarArray, depVarArray, datapoints, linkFieldsArray, managedFieldsArray)`` 
        
        :param fieldName:  field name  
        :type fieldName: str 
        :param indepVarArray:  independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param depVarArray:  dependent variables of this and all linked fields  
        :type depVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param datapoints:  row based array of double values representing the first independent variable; the number of points should equal the number of rows.  
        :type datapoints: list of float 
        :param linkFieldsArray:  row based array of link field values representing the table; the number of fields should equal the number of rows. 
        :type linkFieldsArray: list of :py:class:`NXOpen.Fields.Field` 
        :param managedFieldsArray:  row based array of logical values indicating the links table field should manage the specified fields . 
        :type managedFieldsArray: list of bool 
        :returns:  links table field  
        :rtype: :py:class:`NXOpen.Fields.FieldLinksTable` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateMeshSizeFieldData(self, elementSizeType: int, meshArray: 'list[NXOpen.TaggedObject]') -> Field:
        """
        Create Mesh Size Field :py:class:`NXOpen.Fields.Field` object
        
        Signature ``CreateMeshSizeFieldData(elementSizeType, meshArray)`` 
        
        :param elementSizeType:  At Centroid of Element Free Face and Elements=0,  At Centroid of Element Free Faces=1, At Centroid of Elements=2  
        :type elementSizeType: int 
        :param meshArray: 
        :type meshArray: list of :py:class:`NXOpen.TaggedObject` 
        :returns:  Created Field  
        :rtype: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ConvertToLinksTable(self, table: FieldTable) -> FieldLinksTable:
        """
        Creates and returns a :py:class:`NXOpen.Fields.FieldLinksTable` representation of this table.  
        
        Deletes the input table and updates all references to point to the links table.
        
        Signature ``ConvertToLinksTable(table)`` 
        
        :param table:  Table to be converted  
        :type table: :py:class:`NXOpen.Fields.FieldTable` 
        :returns:  table of fields  
        :rtype: :py:class:`NXOpen.Fields.FieldLinksTable` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateComplexScalarFieldWrapperWithFieldWithScaleFactor(self, field: Field, scaleFactor: float) -> ComplexScalarFieldWrapper:
        """
        Create a complex scalar field wrapper backed up by a complex scalar field with scale factor  
        
        Signature ``CreateComplexScalarFieldWrapperWithFieldWithScaleFactor(field, scaleFactor)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :param scaleFactor:  the field will be multiplied by this scale factor when being evaluated  
        :type scaleFactor: float 
        :returns:  scalar field wrapper created and associated to the field  
        :rtype: :py:class:`NXOpen.Fields.ComplexScalarFieldWrapper` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateComplexVectorFieldWrapperWithExpressions(self, expressions: 'list[NXOpen.Expression]') -> ComplexVectorFieldWrapper:
        """
        Create a complex vector field wrapper backed by six scalar expressions  
        
        Signature ``CreateComplexVectorFieldWrapperWithExpressions(expressions)`` 
        
        :param expressions:  existing expressions that will be this wrapper's value  
        :type expressions: list of :py:class:`NXOpen.Expression` 
        :returns:  scalar field wrapper created and associated to the expression  
        :rtype: :py:class:`NXOpen.Fields.ComplexVectorFieldWrapper` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateComplexVectorFieldWrapperWithField(self, field: Field, scaleFactor: float) -> ComplexVectorFieldWrapper:
        """
        Create a complex vector field wrapper backed up by a complex vector field  
        
        Signature ``CreateComplexVectorFieldWrapperWithField(field, scaleFactor)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        :param scaleFactor:  the field will be multiplied by this scale factor when being evaluated  
        :type scaleFactor: float 
        :returns:  vector field wrapper created and associated to the field  
        :rtype: :py:class:`NXOpen.Fields.ComplexVectorFieldWrapper` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateProfileField(self, fieldName: str, dependentUnit: NXOpen.Unit, sketch: NXOpen.Sketch, discreteType: int, numPoints: int, chordalTolerance: NXOpen.Expression, offset: NXOpen.Expression, scale: NXOpen.Expression, interpolationType: int) -> FieldProfileTable:
        """
        Creates a :py:class:`NXOpen.Fields.FieldProfileTable` object with dependent and independent variables 
        :py:class:`NXOpen.Fields.FieldVariable` and sketch curves:py:class:`NXOpen.Sketch`.  
        
        Signature ``CreateProfileField(fieldName, dependentUnit, sketch, discreteType, numPoints, chordalTolerance, offset, scale, interpolationType)`` 
        
        :param fieldName:  field name  
        :type fieldName: str 
        :param dependentUnit:  unit of the dependent variable  
        :type dependentUnit: :py:class:`NXOpen.Unit` 
        :param sketch:  sketch source for profile  
        :type sketch: :py:class:`NXOpen.Sketch` 
        :param discreteType: 
        :type discreteType: int 
        :param numPoints: 
        :type numPoints: int 
        :param chordalTolerance: 
        :type chordalTolerance: :py:class:`NXOpen.Expression` 
        :param offset:  offset expression for dependent variable  
        :type offset: :py:class:`NXOpen.Expression` 
        :param scale:  scale expression for dependent variable  
        :type scale: :py:class:`NXOpen.Expression` 
        :param interpolationType:  profile interpolation type 
        :type interpolationType: int 
        :returns:  profile table field  
        :rtype: :py:class:`NXOpen.Fields.FieldProfileTable` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CreateProfileExternalTable(self, fieldName: str, filePath: str, nbAbscisae: int, xColumn: int, yColumn: int, ordinateColumn: int, xOffset: NXOpen.Expression, yOffset: NXOpen.Expression, ordinateOffset: NXOpen.Expression, xScale: NXOpen.Expression, yScale: NXOpen.Expression, ordinateScale: NXOpen.Expression, xCyclic: bool, yCyclic: bool, interpolation: FieldEvaluatorInterpolationEnum, xExtrapolation: FieldEvaluatorValuesOutsideTableInterpolationEnum, yExtrapolation: FieldEvaluatorValuesOutsideTableInterpolationEnum, slopeLeft: NXOpen.Expression, slopeRight: NXOpen.Expression) -> FieldReference:
        """
        Creates an External Data Table Profile
        
        Signature ``CreateProfileExternalTable(fieldName, filePath, nbAbscisae, xColumn, yColumn, ordinateColumn, xOffset, yOffset, ordinateOffset, xScale, yScale, ordinateScale, xCyclic, yCyclic, interpolation, xExtrapolation, yExtrapolation, slopeLeft, slopeRight)`` 
        
        :param fieldName:  field name  
        :type fieldName: str 
        :param filePath: 
        :type filePath: str 
        :param nbAbscisae:  1 or 2  
        :type nbAbscisae: int 
        :param xColumn: 
        :type xColumn: int 
        :param yColumn: 
        :type yColumn: int 
        :param ordinateColumn: 
        :type ordinateColumn: int 
        :param xOffset: 
        :type xOffset: :py:class:`NXOpen.Expression` 
        :param yOffset: 
        :type yOffset: :py:class:`NXOpen.Expression` 
        :param ordinateOffset: 
        :type ordinateOffset: :py:class:`NXOpen.Expression` 
        :param xScale: 
        :type xScale: :py:class:`NXOpen.Expression` 
        :param yScale: 
        :type yScale: :py:class:`NXOpen.Expression` 
        :param ordinateScale: 
        :type ordinateScale: :py:class:`NXOpen.Expression` 
        :param xCyclic: 
        :type xCyclic: bool 
        :param yCyclic: 
        :type yCyclic: bool 
        :param interpolation: 
        :type interpolation: :py:class:`NXOpen.Fields.FieldEvaluatorInterpolationEnum` 
        :param xExtrapolation: 
        :type xExtrapolation: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
        :param yExtrapolation: 
        :type yExtrapolation: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
        :param slopeLeft: 
        :type slopeLeft: :py:class:`NXOpen.Expression` 
        :param slopeRight: 
        :type slopeRight: :py:class:`NXOpen.Expression` 
        :returns:  profile external data table ref field  
        :rtype: :py:class:`NXOpen.Fields.FieldReference` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EditProfileExternalTable(self, externalFileRefField: FieldReference, fieldName: str, filePath: str, nbAbscisae: int, xColumn: int, yColumn: int, ordinateColumn: int, xOffset: NXOpen.Expression, yOffset: NXOpen.Expression, ordinateOffset: NXOpen.Expression, xScale: NXOpen.Expression, yScale: NXOpen.Expression, ordinateScale: NXOpen.Expression, xCyclic: bool, yCyclic: bool, interpolation: FieldEvaluatorInterpolationEnum, xExtrapolation: FieldEvaluatorValuesOutsideTableInterpolationEnum, yExtrapolation: FieldEvaluatorValuesOutsideTableInterpolationEnum, slopeLeft: NXOpen.Expression, slopeRight: NXOpen.Expression) -> None:
        """
        Modifies an External Data Table Profile
        
        Signature ``EditProfileExternalTable(externalFileRefField, fieldName, filePath, nbAbscisae, xColumn, yColumn, ordinateColumn, xOffset, yOffset, ordinateOffset, xScale, yScale, ordinateScale, xCyclic, yCyclic, interpolation, xExtrapolation, yExtrapolation, slopeLeft, slopeRight)`` 
        
        :param externalFileRefField: 
        :type externalFileRefField: :py:class:`NXOpen.Fields.FieldReference` 
        :param fieldName:  field name  
        :type fieldName: str 
        :param filePath: 
        :type filePath: str 
        :param nbAbscisae:  1 or 2  
        :type nbAbscisae: int 
        :param xColumn: 
        :type xColumn: int 
        :param yColumn: 
        :type yColumn: int 
        :param ordinateColumn: 
        :type ordinateColumn: int 
        :param xOffset: 
        :type xOffset: :py:class:`NXOpen.Expression` 
        :param yOffset: 
        :type yOffset: :py:class:`NXOpen.Expression` 
        :param ordinateOffset: 
        :type ordinateOffset: :py:class:`NXOpen.Expression` 
        :param xScale: 
        :type xScale: :py:class:`NXOpen.Expression` 
        :param yScale: 
        :type yScale: :py:class:`NXOpen.Expression` 
        :param ordinateScale: 
        :type ordinateScale: :py:class:`NXOpen.Expression` 
        :param xCyclic: 
        :type xCyclic: bool 
        :param yCyclic: 
        :type yCyclic: bool 
        :param interpolation: 
        :type interpolation: :py:class:`NXOpen.Fields.FieldEvaluatorInterpolationEnum` 
        :param xExtrapolation: 
        :type xExtrapolation: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
        :param yExtrapolation: 
        :type yExtrapolation: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
        :param slopeLeft: 
        :type slopeLeft: :py:class:`NXOpen.Expression` 
        :param slopeRight: 
        :type slopeRight: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Domains: FieldDomainCollection = ...
    """
    Returns a collection of Domains 
    
    Signature ``Domains`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.FieldDomainCollection`
    """
    Fields: FieldCollection = ...
    """
    Returns a collection of Fields 
    
    Signature ``Fields`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.FieldCollection`
    """
    Null: FieldManager = ...  # unknown typename


class FieldTableInterpolationEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FieldTableInterpolationEnum():
    """
    Interpolation type This enumeration has been deprecated use :py:class:`NXOpen.Fields.FieldEvaluatorInterpolationEnum` instead.    
    
    .. deprecated::  NX7.5.2
       Use :py:class:`NXOpen.Fields.FieldEvaluatorInterpolationEnum` instead.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No interpolation method; table can only be used as a lookup"
       "Linear1d", "Standard linear interpolation between bounding points"
       "NearestNeighbor1d", "Locates the nearest point and returns its value"
       "InverseDistanceWeighting1d", "Sum of the weighted value of all points, based on the inverse of the distance"
       "Delaunay2dFast", "Triangulates the independent values and uses the bounding triangle, sacrifices accuracy for speed"
       "Delaunay2dMedium", "Triangulates the independent values and uses the bounding triangle, compromise between accuracy and speed"
       "Delaunay2dAccurate", "Triangulates the independent values and uses the bounding triangle, sacrifices speed for accuracy"
       "NearestNeighbor2d", "Locates the nearest point in a plane and returns its value"
       "RenkaShepard2d", "Refined inverse distance weighting in 2D space"
       "InverseDistanceWeighting2d", "Sum of the weighted value of all points in 2D space, based on the inverse of the distance"
       "Delaunay3dFast", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices accuracy for speed"
       "Delaunay3dMedium", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, compromise between accuracy and speed"
       "Delaunay3dAccurate", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices speed for accuracy"
       "NearestNeighbor3d", "Locates the nearest point in space and returns its value"
       "RenkaShepard3d", "Refined inverse distance weighting in 3D space"
       "InverseDistanceWeighting3d", "Sum of the weighted value of all points in 3D space, based on the inverse of the distance"
       "NearestNeighborNd", "Locates the nearest point in N dimensional space and returns its value"
       "RenkaShepardNd", "Refined inverse distance weighting in N dimensional space"
       "InverseDistanceWeightingNd", "Sum of the weighted value of all points in N dimensional, based on the inverse of the distance"
    """
    NotSet = 0  # FieldTableInterpolationEnumMemberType
    Linear1d = 1  # FieldTableInterpolationEnumMemberType
    NearestNeighbor1d = 2  # FieldTableInterpolationEnumMemberType
    InverseDistanceWeighting1d = 3  # FieldTableInterpolationEnumMemberType
    Delaunay2dFast = 4  # FieldTableInterpolationEnumMemberType
    Delaunay2dMedium = 5  # FieldTableInterpolationEnumMemberType
    Delaunay2dAccurate = 6  # FieldTableInterpolationEnumMemberType
    NearestNeighbor2d = 7  # FieldTableInterpolationEnumMemberType
    RenkaShepard2d = 8  # FieldTableInterpolationEnumMemberType
    InverseDistanceWeighting2d = 9  # FieldTableInterpolationEnumMemberType
    Delaunay3dFast = 10  # FieldTableInterpolationEnumMemberType
    Delaunay3dMedium = 11  # FieldTableInterpolationEnumMemberType
    Delaunay3dAccurate = 12  # FieldTableInterpolationEnumMemberType
    NearestNeighbor3d = 13  # FieldTableInterpolationEnumMemberType
    RenkaShepard3d = 14  # FieldTableInterpolationEnumMemberType
    InverseDistanceWeighting3d = 15  # FieldTableInterpolationEnumMemberType
    NearestNeighborNd = 16  # FieldTableInterpolationEnumMemberType
    RenkaShepardNd = 17  # FieldTableInterpolationEnumMemberType
    InverseDistanceWeightingNd = 18  # FieldTableInterpolationEnumMemberType
    
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
    


class FieldTableLoadFileOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FieldTableLoadFileOption():
    """
    Load file options
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Append", "Append data to the table removing duplicates"
       "Replace", "Replace data removing duplicates"
    """
    Append = 0  # FieldTableLoadFileOptionMemberType
    Replace = 1  # FieldTableLoadFileOptionMemberType
    
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
    


class FieldTable(Field):
    """
    Represents the Field Table class. 
    
    A field (see :py:class:`NXOpen.Fields.Field`) defined in terms of tabular data involving 
    one or more look-up independent columns and one or more dependent variables (see 
    :py:class:`NXOpen.Fields.FieldVariable`) which depend on the look-up columns.
    
    To obtain a instance of this class use :py:class:`NXOpen.Fields.FieldManager` .
    
    .. versionadded:: NX6.0.0
    """
    
    class InterpolationEnum():
        """
        Interpolation type This enumeration has been deprecated use :py:class:`NXOpen.Fields.FieldEvaluatorInterpolationEnum` instead.    
        
        .. deprecated::  NX7.5.2
           Use :py:class:`NXOpen.Fields.FieldEvaluatorInterpolationEnum` instead.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No interpolation method; table can only be used as a lookup"
           "Linear1d", "Standard linear interpolation between bounding points"
           "NearestNeighbor1d", "Locates the nearest point and returns its value"
           "InverseDistanceWeighting1d", "Sum of the weighted value of all points, based on the inverse of the distance"
           "Delaunay2dFast", "Triangulates the independent values and uses the bounding triangle, sacrifices accuracy for speed"
           "Delaunay2dMedium", "Triangulates the independent values and uses the bounding triangle, compromise between accuracy and speed"
           "Delaunay2dAccurate", "Triangulates the independent values and uses the bounding triangle, sacrifices speed for accuracy"
           "NearestNeighbor2d", "Locates the nearest point in a plane and returns its value"
           "RenkaShepard2d", "Refined inverse distance weighting in 2D space"
           "InverseDistanceWeighting2d", "Sum of the weighted value of all points in 2D space, based on the inverse of the distance"
           "Delaunay3dFast", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices accuracy for speed"
           "Delaunay3dMedium", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, compromise between accuracy and speed"
           "Delaunay3dAccurate", "Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices speed for accuracy"
           "NearestNeighbor3d", "Locates the nearest point in space and returns its value"
           "RenkaShepard3d", "Refined inverse distance weighting in 3D space"
           "InverseDistanceWeighting3d", "Sum of the weighted value of all points in 3D space, based on the inverse of the distance"
           "NearestNeighborNd", "Locates the nearest point in N dimensional space and returns its value"
           "RenkaShepardNd", "Refined inverse distance weighting in N dimensional space"
           "InverseDistanceWeightingNd", "Sum of the weighted value of all points in N dimensional, based on the inverse of the distance"
        """
        NotSet = 0  # FieldTableInterpolationEnumMemberType
        Linear1d = 1  # FieldTableInterpolationEnumMemberType
        NearestNeighbor1d = 2  # FieldTableInterpolationEnumMemberType
        InverseDistanceWeighting1d = 3  # FieldTableInterpolationEnumMemberType
        Delaunay2dFast = 4  # FieldTableInterpolationEnumMemberType
        Delaunay2dMedium = 5  # FieldTableInterpolationEnumMemberType
        Delaunay2dAccurate = 6  # FieldTableInterpolationEnumMemberType
        NearestNeighbor2d = 7  # FieldTableInterpolationEnumMemberType
        RenkaShepard2d = 8  # FieldTableInterpolationEnumMemberType
        InverseDistanceWeighting2d = 9  # FieldTableInterpolationEnumMemberType
        Delaunay3dFast = 10  # FieldTableInterpolationEnumMemberType
        Delaunay3dMedium = 11  # FieldTableInterpolationEnumMemberType
        Delaunay3dAccurate = 12  # FieldTableInterpolationEnumMemberType
        NearestNeighbor3d = 13  # FieldTableInterpolationEnumMemberType
        RenkaShepard3d = 14  # FieldTableInterpolationEnumMemberType
        InverseDistanceWeighting3d = 15  # FieldTableInterpolationEnumMemberType
        NearestNeighborNd = 16  # FieldTableInterpolationEnumMemberType
        RenkaShepardNd = 17  # FieldTableInterpolationEnumMemberType
        InverseDistanceWeightingNd = 18  # FieldTableInterpolationEnumMemberType
        
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
        
    
    
    class LoadFileOption():
        """
        Load file options
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Append", "Append data to the table removing duplicates"
           "Replace", "Replace data removing duplicates"
        """
        Append = 0  # FieldTableLoadFileOptionMemberType
        Replace = 1  # FieldTableLoadFileOptionMemberType
        
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
        
    
    
    def EditFieldTable(self, indepVarArray: 'list[FieldVariable]', depVarArray: 'list[FieldVariable]', datapoints: 'list[float]') -> None:
        """
        Edit the table field.  
        
        Specifies the new array of :py:class:`NXOpen.Fields.FieldVariable`s for 
        independent and dependent variables, as well as the new double values.
        
        Signature ``EditFieldTable(indepVarArray, depVarArray, datapoints)`` 
        
        :param indepVarArray:  independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param depVarArray:  dependent expression fields to be associated with the formula field  
        :type depVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param datapoints:  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows.  
        :type datapoints: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EditFieldTableComplexDisplay(self, indepVarArrayComplexDisplay: 'list[bool]', depVarArrayComplexDisplay: 'list[bool]') -> None:
        """
        Edit the table field complex display.  
        
        Specifies the new array of complex display flags for 
        independent and dependent variables.
        
        Signature ``EditFieldTableComplexDisplay(indepVarArrayComplexDisplay, depVarArrayComplexDisplay)`` 
        
        :param indepVarArrayComplexDisplay:  independent variable complex display flags to be associated with the field  
        :type indepVarArrayComplexDisplay: list of bool 
        :param depVarArrayComplexDisplay:  dependent variable complex display flags to be associated with the field  
        :type depVarArrayComplexDisplay: list of bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EditFieldTableComplexUnits(self, depVarArrayComplexUnits: 'list[NXOpen.Unit]') -> None:
        """
        Edit the table field complex units array.  
        
        Specifies the new array of complex phase unit tags for dependent variables.  
        A NULL unit in a given index indicates that the corresponding variable is not complex, or if it is complex, that the value
        is Real/Imaginary, in which both components have the same unit as the variable itself.  
        In the case where the unit is specified, the complex dep variables in magnitude/phase representation.  
        In that case the measure of the specified unit must be angle. 
        
        Signature ``EditFieldTableComplexUnits(depVarArrayComplexUnits)`` 
        
        :param depVarArrayComplexUnits: 
        :type depVarArrayComplexUnits: list of :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInterpolation(self, interpolationMethod: int) -> None:
        """
        Specified interpolation method, this method was deprecated in NX7.  
        
        5.2.
        
        Signature ``SetInterpolation(interpolationMethod)`` 
        
        :param interpolationMethod:  specified interpolation method; :py:class:`NXOpen.Fields.FieldTable` interpolation enum values for builtin methods.   
        :type interpolationMethod: int 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX7.5.2
           Use :py:meth:`NXOpen.Fields.FieldTable.InterpolationMethod`` instead.
        
        License requirements: None.
        """
        ...
    
    
    def GetIdwOptions(self) -> tuple:
        """
        Get the inverse distance weighting (IDW) interpolation options 
        
        Signature ``GetIdwOptions()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (nearestOption, nearestFraction). nearestOption is a :py:class:`NXOpen.Fields.FieldEvaluatorInverseDistanceWeightingEnum`.   nearest option nearestFraction is a float.   fraction 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetIdwOptions(self, nearestOption: FieldEvaluatorInverseDistanceWeightingEnum, nearestFraction: float) -> None:
        """
        Set the inverse distance weighting (IDW) interpolation options 
        
        Signature ``SetIdwOptions(nearestOption, nearestFraction)`` 
        
        :param nearestOption:  nearest option  
        :type nearestOption: :py:class:`NXOpen.Fields.FieldEvaluatorInverseDistanceWeightingEnum` 
        :param nearestFraction:  fraction  
        :type nearestFraction: float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def LoadFromFile(self, filename: str, loadFileOption: FieldTableLoadFileOption) -> None:
        """
        Populate the table from a file replacing or appending data 
        
        Signature ``LoadFromFile(filename, loadFileOption)`` 
        
        :param filename:  file to read rows from  
        :type filename: str 
        :param loadFileOption:  append or replace  
        :type loadFileOption: :py:class:`NXOpen.Fields.FieldTableLoadFileOption` 
        
        .. versionadded:: NX6.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetData(self, variable: FieldVariable) -> 'list[float]':
        """
        Returns the values for the given :py:class:`NXOpen.Fields.FieldVariable` in this :py:class:`NXOpen.Fields.FieldTable`.  
        
        The input :py:class:`NXOpen.Fields.FieldVariable` should be retrieved from the field using 
        :py:meth:`NXOpen.Fields.Field.GetIndependentVariables` or :py:meth:`NXOpen.Fields.Field.GetDependentVariables`. 
        The values are in the same :py:class:`NXOpen.Unit` as specified on the :py:class:`NXOpen.Fields.FieldVariable`.
        
        Signature ``GetData(variable)`` 
        
        :param variable:  variable whose table values are to be returned  
        :type variable: :py:class:`NXOpen.Fields.FieldVariable` 
        :returns:  the row values for this variable  
        :rtype: list of float 
        
        .. versionadded:: NX7.5.4
        
        License requirements: None.
        """
        ...
    
    
    def EditTableVariables(self, indepVarArray: 'list[FieldVariable]', depExpArray: 'list[FieldVariable]') -> None:
        """
        Edit the table field dependent variables.  
        
        Specifies the new dependent :py:class:`NXOpen.Fields.FieldVariable`
        array.  If retain number of rows is specified, the total number of rows will remain the same.  Columns with zeros will be added 
        as necessary, or data will be truncated.  This process will be handled for each set of variables, independent and dependent.
        Thus, if the number of independent columns increases and the dependent columns decrease, a column of zeros will be added for the
        new independent variable, and data will be dropped from the dependent values.
        
        Signature ``EditTableVariables(indepVarArray, depExpArray)`` 
        
        :param indepVarArray:  independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param depExpArray:  dependent field variables to be associated with the field  
        :type depExpArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    AnnTolerance: float = ...
    """
    Returns or sets  
    the approximate nearest neighbor (ANN) interpolation tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``AnnTolerance`` 
    
    :returns:  approximate nearest neighbor (ANN) interpolation tolerance  
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnnTolerance`` 
    
    :param annTolerance:  approximate nearest neighbor (ANN) interpolation tolerance   
    :type annTolerance: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Discontinuities: bool = ...
    """
    Returns  a flag specifying if the table has discontinuites 
    
    <hr>
    
    Getter Method
    
    Signature ``Discontinuities`` 
    
    :returns:  a flag specifying if the table has discontinuites  
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    IndependentValueDivisor: float = ...
    """
    Returns or sets  the linear interpolation divisor for field independent value, the zero value represents no divisor used 
    
    <hr>
    
    Getter Method
    
    Signature ``IndependentValueDivisor`` 
    
    :returns:  the interpolation divisor for independent value  
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IndependentValueDivisor`` 
    
    :param divisor:  the interpolation divisor for independent value  
    :type divisor: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    IndependentValueDivisorOption: bool = ...
    """
    Returns or sets  a value indicating whether to set the linear interpolation divisor for field independent value 
    
    <hr>
    
    Getter Method
    
    Signature ``IndependentValueDivisorOption`` 
    
    :returns:  the interpolation divisor flag for independent value  
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IndependentValueDivisorOption`` 
    
    :param divisorOption:  the interpolation divisor flag for independent value  
    :type divisorOption: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    IndependentValueShift: float = ...
    """
    Returns or sets  the linear interpolation shift for field independent value 
    
    <hr>
    
    Getter Method
    
    Signature ``IndependentValueShift`` 
    
    :returns:  the interpolation shift for independent value  
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IndependentValueShift`` 
    
    :param shift:  the interpolation shift for independent value  
    :type shift: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    IndependentValueShiftOption: bool = ...
    """
    Returns or sets  a value indicating whether to set the linear interpolation shift for field independent value 
    
    <hr>
    
    Getter Method
    
    Signature ``IndependentValueShiftOption`` 
    
    :returns:  the interpolation shift flag for independent value  
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IndependentValueShiftOption`` 
    
    :param shiftOption:  the interpolation shift flag for independent value  
    :type shiftOption: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    InterpolationMethod: FieldEvaluatorInterpolationEnum = ...
    """
    Returns or sets   
    the interpolation method used when this table data is evaluated.  
    
    <hr>
    
    Getter Method
    
    Signature ``InterpolationMethod`` 
    
    :returns:  the interpolation method    
    :rtype: :py:class:`NXOpen.Fields.FieldEvaluatorInterpolationEnum` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpolationMethod`` 
    
    :param interpolationMethod:  the interpolation method   
    :type interpolationMethod: :py:class:`NXOpen.Fields.FieldEvaluatorInterpolationEnum` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    """
    LatticeDataOption: bool = ...
    """
    Returns or sets   
    the lattice data option check used when this table data is in lattice format.  
    
    <hr>
    
    Getter Method
    
    Signature ``LatticeDataOption`` 
    
    :returns:  the lattice data check option    
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LatticeDataOption`` 
    
    :param latticeDataOption:  the lattice data check option   
    :type latticeDataOption: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LinearLogOption: FieldEvaluatorLinearLogOptionEnum = ...
    """
    Returns or sets   
    the linear/log option used when this table data is evaluated using the linear 1d interpolator.  
    
    <hr>
    
    Getter Method
    
    Signature ``LinearLogOption`` 
    
    :returns:  the log option    
    :rtype: :py:class:`NXOpen.Fields.FieldEvaluatorLinearLogOptionEnum` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LinearLogOption`` 
    
    :param linearOption:  the log option   
    :type linearOption: :py:class:`NXOpen.Fields.FieldEvaluatorLinearLogOptionEnum` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    NumLatticeDataColumn: int = ...
    """
    Returns or sets   
    the number of lattice data column option check used when this table data is in lattice format.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumLatticeDataColumn`` 
    
    :returns:  the lattice data column number  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumLatticeDataColumn`` 
    
    :param numLatticeDataColumn:  the lattice data column number   
    :type numLatticeDataColumn: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    PersistentInterpolator: bool = ...
    """
    Returns or sets  
    a flag specifying if interpolator is persistent between session 
    
    <hr>
    
    Getter Method
    
    Signature ``PersistentInterpolator`` 
    
    :returns:  persistent interpolator indicator   
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PersistentInterpolator`` 
    
    :param persistentInterpolator:  persistent interpolator indicator   
    :type persistentInterpolator: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ValuesOutsideTableInterpolation: FieldEvaluatorValuesOutsideTableInterpolationEnum = ...
    """
    Returns or sets  the outside table values interpolation method for standard linear interpolation 
    
    <hr>
    
    Getter Method
    
    Signature ``ValuesOutsideTableInterpolation`` 
    
    :returns:  the outside table values interpolation method  
    :rtype: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValuesOutsideTableInterpolation`` 
    
    :param interpolationMethod:  the outside table values interpolation method  
    :type interpolationMethod: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: FieldTable = ...  # unknown typename


class FieldLink(Field):
    """
    Represents the Field Link class. 
    
    A field (see :py:class:`Fields.Field`) which is implemented by another user
    created field of any type.  This provides the ability to override that field's map with a 
    localized map.
    
    .. versionadded:: NX6.0.0
    """
    
    def EditFieldLink(self, fieldToLink: Field) -> None:
        """
        Edit the link field.  
        
        Specifies the new :py:class:`Fields.Field`
        to link to.
        
        Signature ``EditFieldLink(fieldToLink)`` 
        
        :param fieldToLink:  field to link  
        :type fieldToLink: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    Null: FieldLink = ...  # unknown typename


class NameVariable(NXOpen.NXObject):
    """
    This class stores the common name and measure for field variables.  
    
    .. versionadded:: NX6.0.2
    """
    Measure: str = ...
    """
    Returns  the measure of the variable 
    
    <hr>
    
    Getter Method
    
    Signature ``Measure`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.2
    
    License requirements: None.
    """
    Name: str = ...
    """
    Returns  the name of the variable 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.2
    
    License requirements: None.
    """
    Null: NameVariable = ...  # unknown typename


class SpatialMapBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Fields.SpatialMap` builder  
    
    Used to create and or edit a :py:class:`NXOpen.Fields.SpatialMap`.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Fields.FieldManager.CreateSpatialMapBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    def AutoTolerance(self) -> None:
        """
        The method to set the face tolerance to a default value based on the current state of the field 
        
        Signature ``AutoTolerance()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateLatticeMap(self, numOfLatticeColumn: int, numOfColumns: int, indepVarArray: 'list[FieldVariable]', datapoint: 'list[float]') -> tuple:
        """
        Create a lattice spatial map from the input datapoints array.  
        
        The number of columns in the datapoints
        array is specified by numOfColumns, and should include the total of all independent and dependent columns.
        Note that the number of dependent columns can be zero.  The independent domain must be x, y, z, xy, xz, yz or xyz and
        the number of columns must be greater than or equal to the count of the independent variables.
        
        The number of rows of data in the datapoints array is calculated by dividing the number of data points by the number of columns.
        
        If number of lattice columns is 1, then a parametric line based map will be created.
        
        Otherwise the lattice will be a M x N u-v grid, where M is the number of lattice columns and N is calculated based 
        on the number of rows in the data points array divded by the number of lattice columns  
        
        Signature ``CreateLatticeMap(numOfLatticeColumn, numOfColumns, indepVarArray, datapoint)`` 
        
        :param numOfLatticeColumn: 
        :type numOfLatticeColumn: int 
        :param numOfColumns: 
        :type numOfColumns: int 
        :param indepVarArray: 
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param datapoint: 
        :type datapoint: list of float 
        :returns: a tuple 
        :rtype: A tuple consisting of (latticeMap, parameterizedDatapoints). latticeMap is a :py:class:`NXOpen.Fields.SpatialMap`. parameterizedDatapoints is a list of float. 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    BoundedObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the bounded objects 
    
    <hr>
    
    Getter Method
    
    Signature ``BoundedObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    BoundingBoxMap: SpatialMapBoundingBoxMapEnum = ...
    """
    Returns or sets  the bounding box map 
    
    <hr>
    
    Getter Method
    
    Signature ``BoundingBoxMap`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.SpatialMapBoundingBoxMapEnum` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BoundingBoxMap`` 
    
    :param boundBoxMap: 
    :type boundBoxMap: :py:class:`NXOpen.Fields.SpatialMapBoundingBoxMapEnum` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ConstUObjects: PathObjectsList = ...
    """
    Returns  the list of :py:class:`NXOpen.Fields.PathObjects` objects that define sections of constant u 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstUObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.PathObjectsList` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    ConstVObjects: PathObjectsList = ...
    """
    Returns  the list of :py:class:`NXOpen.Fields.PathObjects` objects that define sections of constant v 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstVObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.PathObjectsList` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    ConstantUObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the const uobjects 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstantUObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX6.0.1
       Use :py:meth:`NXOpen.Fields.SpatialMapBuilder.ConstUObjects` instead.
    
    License requirements: None.
    """
    ConstantVObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the const vobjects 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstantVObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX6.0.1
       Use :py:meth:`NXOpen.Fields.SpatialMapBuilder.ConstVObjects` instead.
    
    License requirements: None.
    """
    CoordSystem: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the csys 
    
    <hr>
    
    Getter Method
    
    Signature ``CoordSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CoordSystem`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    FaceTolerance: NXOpen.Expression = ...
    """
    Returns  the face tolerance for 3D degenerate surface maps 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LatticePath: PathObjects = ...
    """
    Returns  the lattice path objects 
    
    <hr>
    
    Getter Method
    
    Signature ``LatticePath`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.PathObjects` 
    
    .. versionadded:: NX6.0.1
    
    License requirements: None.
    """
    MapSubtype: SpatialMapSubtypeEnum = ...
    """
    Returns or sets  the map subtype 
    
    <hr>
    
    Getter Method
    
    Signature ``MapSubtype`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.SpatialMapSubtypeEnum` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MapSubtype`` 
    
    :param mapSubType: 
    :type mapSubType: :py:class:`NXOpen.Fields.SpatialMapSubtypeEnum` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MapSubtypeMapping: SpatialMapSubtypeMappingEnum = ...
    """
    Returns or sets  the subtype mapping 
    
    <hr>
    
    Getter Method
    
    Signature ``MapSubtypeMapping`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.SpatialMapSubtypeMappingEnum` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MapSubtypeMapping`` 
    
    :param mapSubTypeMapping: 
    :type mapSubTypeMapping: :py:class:`NXOpen.Fields.SpatialMapSubtypeMappingEnum` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MapType: SpatialMapTypeEnum = ...
    """
    Returns or sets  the map type 
    
    <hr>
    
    Getter Method
    
    Signature ``MapType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.SpatialMapTypeEnum` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MapType`` 
    
    :param mapType: 
    :type mapType: :py:class:`NXOpen.Fields.SpatialMapTypeEnum` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MappingFaces: NXOpen.SelectNXObjectList = ...
    """
    Returns  the faces to be used as mapping objects 
    
    <hr>
    
    Getter Method
    
    Signature ``MappingFaces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    OppositeCorner: NXOpen.Point = ...
    """
    Returns or sets  the opposite corner 
    
    <hr>
    
    Getter Method
    
    Signature ``OppositeCorner`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OppositeCorner`` 
    
    :param oppositeCorner: 
    :type oppositeCorner: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Origin: NXOpen.Point = ...
    """
    Returns or sets  the origin 
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Origin`` 
    
    :param origin: 
    :type origin: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ParametricPlaneMap: SpatialMapParametricPlaneMapEnum = ...
    """
    Returns or sets  the parametric plane map 
    
    <hr>
    
    Getter Method
    
    Signature ``ParametricPlaneMap`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.SpatialMapParametricPlaneMapEnum` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ParametricPlaneMap`` 
    
    :param parmPlaneMap: 
    :type parmPlaneMap: :py:class:`NXOpen.Fields.SpatialMapParametricPlaneMapEnum` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: SpatialMapBuilder = ...  # unknown typename


class FieldWrapper(NXOpen.NXObject):
    """
    This class defines a value that is internally backed up by a field.  
    
    .. versionadded:: NX6.0.0
    """
    
    def SetField(self, field: Field) -> None:
        """
        Sets the implementation of the wrapper to the specified field 
        
        Signature ``SetField(field)`` 
        
        :param field:  an existing field that will be this wrapper's value  
        :type field: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetField(self) -> Field:
        """
        Returns the implementation  
        
        Signature ``GetField()`` 
        
        :returns:  an existing field  
        :rtype: :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    Null: FieldWrapper = ...  # unknown typename


class FieldProfileTableSamplingPointOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FieldProfileTableSamplingPointOption():
    """
    Discrete point type
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ChordalTolerance", "Chordal tolerance type"
       "EqualArcLength", "Equal arc length type"
    """
    ChordalTolerance = 0  # FieldProfileTableSamplingPointOptionMemberType
    EqualArcLength = 1  # FieldProfileTableSamplingPointOptionMemberType
    
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
    


class FieldProfileTable(FieldTable):
    """
    Represents the Field Profile class. 
    
    A field (see :py:class:`NXOpen.Fields.Field`) defined in terms of sketch curve with one independent 
    variable and one dependent variable (see :py:class:`NXOpen.Fields.FieldVariable`).
    
    To obtain a instance of this class use :py:class:`NXOpen.Fields.FieldManager` .
    
    .. versionadded:: NX11.0.1
    """
    
    class SamplingPointOption():
        """
        Discrete point type
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ChordalTolerance", "Chordal tolerance type"
           "EqualArcLength", "Equal arc length type"
        """
        ChordalTolerance = 0  # FieldProfileTableSamplingPointOptionMemberType
        EqualArcLength = 1  # FieldProfileTableSamplingPointOptionMemberType
        
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
        
    
    
    def SetUnitType(self, unitType: NXOpen.Unit) -> None:
        """
        Edit with unit type 
        
        Signature ``SetUnitType(unitType)`` 
        
        :param unitType: 
        :type unitType: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    ChordalTolerance: NXOpen.Expression = ...
    """
    Returns  the chordal tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``ChordalTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    NumberPoints: int = ...
    """
    Returns or sets  the number of points 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberPoints`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberPoints`` 
    
    :param numPoints: 
    :type numPoints: int 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Offset: NXOpen.Expression = ...
    """
    Returns  the offset 
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    SamplingPointType: FieldProfileTableSamplingPointOption = ...
    """
    Returns or sets  the discrete type 
    
    <hr>
    
    Getter Method
    
    Signature ``SamplingPointType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.FieldProfileTableSamplingPointOption` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SamplingPointType`` 
    
    :param samplingType: 
    :type samplingType: :py:class:`NXOpen.Fields.FieldProfileTableSamplingPointOption` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Scale: NXOpen.Expression = ...
    """
    Returns  the scale 
    
    <hr>
    
    Getter Method
    
    Signature ``Scale`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Sketch: NXOpen.Sketch = ...
    """
    Returns or sets  the field 
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Sketch` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Sketch` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: FieldProfileTable = ...  # unknown typename


class FieldDrawHelper(NXOpen.TaggedObject):
    """
    Represents Field_DrawHelper. This class is to be used only for implementing  
    TESTING of Field Display functionality only.
    
    Use :py:meth:`NXOpen.Fields.Field.GetFieldDrawhelper` to obtain an instance of this class
    
    .. versionadded:: NX12.0.0
    """
    
    def GetReloadResult(self) -> bool:
        """
        Returns true if the drawhelper reload op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetReloadResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawSymbolsResult(self) -> bool:
        """
        Returns true if the drawhelper draw symbols op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawSymbolsResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawTableSymbolsResult(self) -> bool:
        """
        Returns true if the drawhelper draw table symbols op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawTableSymbolsResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawContoursResult(self) -> bool:
        """
        Returns true if the drawhelper draw contours op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawContoursResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawContoursWithEdgesResult(self) -> bool:
        """
        Returns true if the drawhelper draw contours with edges op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawContoursWithEdgesResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawAxesResult(self) -> bool:
        """
        Returns true if the drawhelper draw Axes op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawAxesResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawUserDefinedResolutionResult(self) -> bool:
        """
        Returns true if the drawhelper draw user defined resolution op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawUserDefinedResolutionResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawLegendResult(self) -> bool:
        """
        Returns true if the drawhelper legend op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawLegendResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLegendTearDownResult(self) -> bool:
        """
        Returns true if the drawhelper legend tear down op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetLegendTearDownResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawAxesLabelsResult(self) -> bool:
        """
        Returns true if the drawhelper draw Axes labels op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawAxesLabelsResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawIndepDomainResult(self) -> bool:
        """
        Returns true if the drawhelper draw Independent domain op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawIndepDomainResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawDefaultValueLabelsResult(self) -> bool:
        """
        Returns true if the drawhelper draw Default value labels op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawDefaultValueLabelsResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawDescriptionResult(self) -> bool:
        """
        Returns true if the drawhelper draw Description text op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawDescriptionResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawNameResult(self) -> bool:
        """
        Returns true if the drawhelper draw name text op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawNameResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawValueLabelsResult(self) -> bool:
        """
        Returns true if the drawhelper draw value labels op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawValueLabelsResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawTableValueLabelsResult(self) -> bool:
        """
        Returns true if the drawhelper draw table value labels op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawTableValueLabelsResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawUndefineSymbolValuesResult(self) -> bool:
        """
        Returns true if draw helper undefined value symbols draw op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawUndefineSymbolValuesResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawOverflowSymbolValuesResult(self) -> bool:
        """
        Returns true if draw helper underflow value symbols draw op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawOverflowSymbolValuesResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawUnderflowSymbolValuesResult(self) -> bool:
        """
        Returns true if draw helper overflow value symbols draw op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawUnderflowSymbolValuesResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawUndefineContourValuesResult(self) -> bool:
        """
        Returns true if draw helper undefined value contour draw op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawUndefineContourValuesResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawOverflowContourValuesResult(self) -> bool:
        """
        Returns true if draw helper underflow value contour draw op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawOverflowContourValuesResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDrawUnderflowContourValuesResult(self) -> bool:
        """
        Returns true if draw helper overflow value contour draw op is successful :py:class:`NXOpen.Fields.FieldDrawHelper`  
        
        Signature ``GetDrawUnderflowContourValuesResult()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: FieldDrawHelper = ...  # unknown typename


class FieldCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of Fields   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Fields.FieldManager`
    
    .. versionadded:: NX11.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    


class PathObjectsList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[PathObjects]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Fields.PathObjects` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: PathObjects) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Fields.PathObjects` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearIndex(self, deleteIdx: int) -> None:
        """
        Deletes the item at the index specified.  
        
        The size of the list does
        *   not change, but the item at this index is set to NULL.
        
        Signature ``ClearIndex(deleteIdx)`` 
        
        :param deleteIdx:  index of item to be deleted  
        :type deleteIdx: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindIndex(self, obj: PathObjects) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Fields.PathObjects` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> PathObjects:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Fields.PathObjects` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Erase(self, index: int) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to be. 
        
        Signature ``Erase(index)`` 
        
        :param index:  index of item to be removed from the list  
        :type index: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, index: int, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object at the given position from the list.
        The list is shifted so that there isn't a null where the object used to be. 
        
        Signature ``Erase(index, deleteOption)`` 
        
        :param index:  index of item to be removed from the list  
        :type index: int 
        :param deleteOption:  whether to delete the object  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: PathObjects) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Fields.PathObjects` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: PathObjects, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Fields.PathObjects` 
        :param deleteOption:  whether to delete the object  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Clear(self) -> None:
        """
        Clears the entire list without deleting the objects.  The caller is responsible for 
        accounting for these objects.  If they are not used or deleted by the time the part is 
        closed (in other words, leaked) an error will occur 
        
        Signature ``Clear()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Clear(self, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Clears the entire list 
        
        Signature ``Clear(deleteOption)`` 
        
        :param deleteOption:  whether to delete the objects when removing them  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetContents(self) -> 'list[PathObjects]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Fields.PathObjects` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[PathObjects]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Fields.PathObjects` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Swap(self, index1: int, index2: int) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(index1, index2)`` 
        
        :param index1:  location of the first item  
        :type index1: int 
        :param index2:  location of the second item  
        :type index2: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Swap(self, object1: PathObjects, object2: PathObjects) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Fields.PathObjects` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Fields.PathObjects` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: PathObjects) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Fields.PathObjects` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveToTop(self, index: int) -> None:
        """
        Move object at the specified location to the top of the list.  
        
        Signature ``MoveToTop(index)`` 
        
        :param index:  location of the item  
        :type index: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveToBottom(self, index: int) -> None:
        """
        Move object at the specified location to the bottom of the list.  
        
        Signature ``MoveToBottom(index)`` 
        
        :param index:  location of the item  
        :type index: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Length: int = ...
    """
    Returns  the length of the list 
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: PathObjectsList = ...  # unknown typename


class SpatialMapTypeEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SpatialMapTypeEnum():
    """
    Type of Spatial Map 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No Map"
       "Global", "Map to global csys - defaults to cartesian"
       "Cartesian", "Map to cartesian csys"
       "Cylindrical", "Map to cylindrical csys"
       "Spherical", "Map to spherical csys"
       "ParametricSpace", "Map to parametric space - see :py:class:`NXOpen.Fields.SpatialMapBoundingBoxMapEnum`"
       "ParametricPlane", "Map to parametric plane - see :py:class:`NXOpen.Fields.SpatialMapParametricPlaneMapEnum`"
       "ParametricLine", "Map to parametric line"
       "ImportedParametricLine", "map to imported parametric line"
    """
    NotSet = 0  # SpatialMapTypeEnumMemberType
    Global = 1  # SpatialMapTypeEnumMemberType
    Cartesian = 2  # SpatialMapTypeEnumMemberType
    Cylindrical = 3  # SpatialMapTypeEnumMemberType
    Spherical = 4  # SpatialMapTypeEnumMemberType
    ParametricSpace = 5  # SpatialMapTypeEnumMemberType
    ParametricPlane = 6  # SpatialMapTypeEnumMemberType
    ParametricLine = 7  # SpatialMapTypeEnumMemberType
    ImportedParametricLine = 8  # SpatialMapTypeEnumMemberType
    
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
    


class SpatialMapSubtypeEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SpatialMapSubtypeEnum():
    """
    Subtype of Spatial Map 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No subtype"
       "Surface", "3D degenerate to surface"
    """
    NotSet = 0  # SpatialMapSubtypeEnumMemberType
    Surface = 1  # SpatialMapSubtypeEnumMemberType
    
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
    


class SpatialMapSubtypeMappingEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SpatialMapSubtypeMappingEnum():
    """
    Subtype Mapping 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Faces", "Map 3D degenerate data to faces"
       "IsoSections", "Map 3D degenerate data using parametric plane using U curves"
       "IsoLines", "Map 3D degenerate data using parametric plane using UV curves"
    """
    Faces = 0  # SpatialMapSubtypeMappingEnumMemberType
    IsoSections = 1  # SpatialMapSubtypeMappingEnumMemberType
    IsoLines = 2  # SpatialMapSubtypeMappingEnumMemberType
    
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
    


class SpatialMapParametricPlaneMapEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SpatialMapParametricPlaneMapEnum():
    """
    Parametric Plane Map 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "IsoSections", " - "
       "IsoLines", " - "
       "ImportedIsoLines", " - "
    """
    IsoSections = 0  # SpatialMapParametricPlaneMapEnumMemberType
    IsoLines = 1  # SpatialMapParametricPlaneMapEnumMemberType
    ImportedIsoLines = 2  # SpatialMapParametricPlaneMapEnumMemberType
    
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
    


class SpatialMapBoundingBoxMapEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SpatialMapBoundingBoxMapEnum():
    """
    Bounding Box Map  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "OppositeCorner", " - "
       "Objects", " - "
    """
    OppositeCorner = 0  # SpatialMapBoundingBoxMapEnumMemberType
    Objects = 1  # SpatialMapBoundingBoxMapEnumMemberType
    
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
    


class SpatialMap(NXOpen.NXObject):
    """
    Represents the Field Domain Map  
    
    A Spatial Map provides a mapping from a field's independent domain into a new domain space.
    This Particular map type is designed to map into cartesian, cylindrical, spherical or parametric
    space, allowing the field to be used where these independent domains are required.
    
    To obtain an instance of this class see :py:class:`NXOpen.Fields.FieldManager`.
    
    .. versionadded:: NX6.0.0
    """
    
    class TypeEnum():
        """
        Type of Spatial Map 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No Map"
           "Global", "Map to global csys - defaults to cartesian"
           "Cartesian", "Map to cartesian csys"
           "Cylindrical", "Map to cylindrical csys"
           "Spherical", "Map to spherical csys"
           "ParametricSpace", "Map to parametric space - see :py:class:`NXOpen.Fields.SpatialMapBoundingBoxMapEnum`"
           "ParametricPlane", "Map to parametric plane - see :py:class:`NXOpen.Fields.SpatialMapParametricPlaneMapEnum`"
           "ParametricLine", "Map to parametric line"
           "ImportedParametricLine", "map to imported parametric line"
        """
        NotSet = 0  # SpatialMapTypeEnumMemberType
        Global = 1  # SpatialMapTypeEnumMemberType
        Cartesian = 2  # SpatialMapTypeEnumMemberType
        Cylindrical = 3  # SpatialMapTypeEnumMemberType
        Spherical = 4  # SpatialMapTypeEnumMemberType
        ParametricSpace = 5  # SpatialMapTypeEnumMemberType
        ParametricPlane = 6  # SpatialMapTypeEnumMemberType
        ParametricLine = 7  # SpatialMapTypeEnumMemberType
        ImportedParametricLine = 8  # SpatialMapTypeEnumMemberType
        
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
        
    
    
    class SubtypeEnum():
        """
        Subtype of Spatial Map 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No subtype"
           "Surface", "3D degenerate to surface"
        """
        NotSet = 0  # SpatialMapSubtypeEnumMemberType
        Surface = 1  # SpatialMapSubtypeEnumMemberType
        
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
        
    
    
    class SubtypeMappingEnum():
        """
        Subtype Mapping 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Faces", "Map 3D degenerate data to faces"
           "IsoSections", "Map 3D degenerate data using parametric plane using U curves"
           "IsoLines", "Map 3D degenerate data using parametric plane using UV curves"
        """
        Faces = 0  # SpatialMapSubtypeMappingEnumMemberType
        IsoSections = 1  # SpatialMapSubtypeMappingEnumMemberType
        IsoLines = 2  # SpatialMapSubtypeMappingEnumMemberType
        
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
        
    
    
    class ParametricPlaneMapEnum():
        """
        Parametric Plane Map 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "IsoSections", " - "
           "IsoLines", " - "
           "ImportedIsoLines", " - "
        """
        IsoSections = 0  # SpatialMapParametricPlaneMapEnumMemberType
        IsoLines = 1  # SpatialMapParametricPlaneMapEnumMemberType
        ImportedIsoLines = 2  # SpatialMapParametricPlaneMapEnumMemberType
        
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
        
    
    
    class BoundingBoxMapEnum():
        """
        Bounding Box Map  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "OppositeCorner", " - "
           "Objects", " - "
        """
        OppositeCorner = 0  # SpatialMapBoundingBoxMapEnumMemberType
        Objects = 1  # SpatialMapBoundingBoxMapEnumMemberType
        
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
        
    
    Null: SpatialMap = ...  # unknown typename


class FieldDomain(NXOpen.NXObject):
    """
    Represents the Field Domains.  
    
    In general usage a domain is most commonly used to describe a set of values for which
    a function is defined.  The value of the function within this "domain" is the function's "range".
    In NX, a domain defines a group of variables which define one or more quantifiable phenomenon
    which are inextricably related, for example "time", or "space" (three length variables which
    define the attribute of "location"), or force magnitude (single force value) or vector
    (XYZ components).
    
    **<tt>Independent domain</tt></b>
    
    The independent domain is the set of variables which vary independent of any other quantities.
    Essentially these are the "inputs" to a function.
    
    **<tt>Dependent domain</tt></b>
    
    The dependent domain is the set of variables which vary according to some function of 
    the inputs, or independent variables.  Essentially these are the "range" of a function.  If the
    dependent phenomenon has multiple components (e.g., location, vector or tensor quantities) the 
    dependent domain is expressed as multiple dependent variables.
    
    .. versionadded:: NX4.0.0
    """
    Null: FieldDomain = ...  # unknown typename


class FieldFormula(Field):
    """
    Represents the Field Formula class. 
    
    A field (see :py:class:`NXOpen.Fields.Field`) which has **<tt>n</tt></b> number of dependent
    variables, where each dependent variable (see :py:class:`NXOpen.Fields.FieldVariable`) is implemented using the NX Expression sub-system.
    In practical terms, a field formula is implemented using n number of field expressions
    :py:class:`NXOpen.Fields.FieldExpression`.
    
    .. versionadded:: NX6.0.0
    """
    
    def EditFieldFormula(self, indepVarArray: 'list[FieldVariable]', depExpArray: 'list[FieldExpression]') -> None:
        """
        Edit the formula field.  
        
        Specifies the new expression :py:class:`NXOpen.Fields.FieldExpression`
        array and the array of :py:class:`NXOpen.Fields.FieldVariable`s used.
        
        Signature ``EditFieldFormula(indepVarArray, depExpArray)`` 
        
        :param indepVarArray:  independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param depExpArray:  dependent field expressions to be associated with the field  
        :type depExpArray: list of :py:class:`NXOpen.Fields.FieldExpression` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDependentExpressions(self) -> 'list[FieldExpression]':
        """
        Returns the dependent field expressions associated with this formula 
        
        Signature ``GetDependentExpressions()`` 
        
        :returns:  dependent expressions   
        :rtype: list of :py:class:`NXOpen.Fields.FieldExpression` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EditFieldFormulaVariables(self, indepVarArray: 'list[FieldVariable]', depVarArray: 'list[FieldVariable]') -> None:
        """
        Edit the formula field variables.  
        
        Specifies the new dependent and independent :py:class:`NXOpen.Fields.FieldVariable`
        arrays.  The formula will be updated to reflect the changes (if any) to the variables.  If the dependent variables are changed, the expressions will be changed 
        to 0 if the new variable measure is incompatible with the old variable measure.  If the independent variables change, the expression will be changed
        to 0 if it contains any of the deleted variables.
        
        Signature ``EditFieldFormulaVariables(indepVarArray, depVarArray)`` 
        
        :param indepVarArray:  new independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param depVarArray:  new dependent field variables to be associated with the field  
        :type depVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: FieldFormula = ...  # unknown typename


class FieldVariableBounds_Struct():
    """
    Variable Bounds structure .  
    
    Constructor: 
    NXOpen.Fields.FieldVariable.Bounds()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    IsMinimumDefined: bool = ...
    """
    true if minimum bound is defined 
    <hr>
    
    Field Value
    Type:bool
    """
    IsMinimumInclusive: bool = ...
    """
    true if minimum bound is inclusive 
    <hr>
    
    Field Value
    Type:bool
    """
    MinimumValue: float = ...
    """
    minimum bound value 
    <hr>
    
    Field Value
    Type:float
    """
    IsMaximumDefined: bool = ...
    """
    true if maximum bound is defined 
    <hr>
    
    Field Value
    Type:bool
    """
    IsMaximumInclusive: bool = ...
    """
    true if maximum bound is inclusive 
    <hr>
    
    Field Value
    Type:bool
    """
    MaximumValue: float = ...
    """
    maximum bound value 
    <hr>
    
    Field Value
    Type:float
    """


class FieldLinksTable(Field):
    """
    Represents the Field LinksTable class. 
    
    A field (see :py:class:`NXOpen.Fields.Field`) defined in terms of tabular data involving 
    one look-up independent column, an equal number of look-up fields and one or more 
    dependent variables (see :py:class:`NXOpen.Fields.FieldVariable`).  This is similar to a table
    (see :py:class:`NXOpen.Fields.FieldTable`), except instead of the interpolation dependent 
    values being defined as numerical contants, they are defined by another field.
    
    To obtain a instance of this class use :py:class:`NXOpen.Fields.FieldManager` .
    
    .. versionadded:: NX9.0.0
    """
    
    @typing.overload
    def EditFieldLinksTable(self, indepVarArray: 'list[FieldVariable]', depVarArray: 'list[FieldVariable]', datapoints: 'list[float]', linkFieldsArray: 'list[Field]') -> None:
        """
        Edit the LinksTable field.  Specifies the new array of :py:class:`NXOpen.Fields.FieldVariable`s 
        for independent and dependent variables, as well as the new double values and linked fields.
        The datapoints and linked fields arrays are row based and number of each must equal the 
        num_rows. The data_points array represents the values for the first independent value.  For example, if 
        the LinksTable has a domain of txyz, the values in this array are all values of t.
        The linked fields array must consist of the fields with independent variables representing the 
        remaining variables in the independent domain of the LinksTable.  For example, if the LinksTable has 
        a domain of txyz, the independent domain of the fields in this array are all xyz.  NULL values are  allowed for 
        linked fields and indicate a discontinuity at the associated value of the first independent  variable.
        The dependent quantities are determined from the linked fields.  The linked fields must have the same 
        dependent variables as the Linkstable.
        
        Signature ``EditFieldLinksTable(indepVarArray, depVarArray, datapoints, linkFieldsArray)`` 
        
        :param indepVarArray:  independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param depVarArray:  dependent variables of this and all linked fields  
        :type depVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param datapoints:  row based array of double values representing the first independent variable; the number of points should equal the number of rows.  
        :type datapoints: list of float 
        :param linkFieldsArray:  row based array of link field values representing the table; the number of fields should equal the number of rows. 
        :type linkFieldsArray: list of :py:class:`NXOpen.Fields.Field` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def EditFieldLinksTable(self, indepVarArray: 'list[FieldVariable]', depVarArray: 'list[FieldVariable]', datapoints: 'list[float]', linkFieldsArray: 'list[Field]', managedFieldsArray: 'list[bool]') -> None:
        """
        Edit the LinksTable field.  Specifies the new array of :py:class:`NXOpen.Fields.FieldVariable`s 
        for independent and dependent variables, as well as the new double values and linked fields.
        The datapoints, linked fields, and the managed fields arrays are row based and number of each must equal the 
        num_rows. The data_points array represents the values for the first independent value.  For example, if 
        the LinksTable has a domain of txyz, the values in this array are all values of t.
        The linked fields array must consist of the fields with independent variables representing the 
        remaining variables in the independent domain of the LinksTable.  For example, if the LinksTable has 
        a domain of txyz, the independent domain of the fields in this array are all xyz.  NULL values are  allowed for 
        linked fields and indicate a discontinuity at the associated value of the first independent  variable.
        The dependent quantities are determined from the linked fields.  The linked fields must have the same 
        dependent variables as the Linkstable. The managed fields array identifies the fields that should be managed by the links table.
        
        Signature ``EditFieldLinksTable(indepVarArray, depVarArray, datapoints, linkFieldsArray, managedFieldsArray)`` 
        
        :param indepVarArray:  independent variables to be associated with the field  
        :type indepVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param depVarArray:  dependent variables of this and all linked fields  
        :type depVarArray: list of :py:class:`NXOpen.Fields.FieldVariable` 
        :param datapoints:  row based array of double values representing the first independent variable; the number of points should equal the number of rows.  
        :type datapoints: list of float 
        :param linkFieldsArray:  row based array of link field values representing the table; the number of fields should equal the number of rows. 
        :type linkFieldsArray: list of :py:class:`NXOpen.Fields.Field` 
        :param managedFieldsArray:  row based array of logical values indicating the links table field should manage the specified fields . 
        :type managedFieldsArray: list of bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSecondaryValuesOutsideTableInterpolation(self, interpolationMethod: FieldEvaluatorValuesOutsideTableInterpolationEnum) -> None:
        """
        Set the values outside table interpolation option for sub fields if the sub fields are tables  
        
        Signature ``SetSecondaryValuesOutsideTableInterpolation(interpolationMethod)`` 
        
        :param interpolationMethod:  the outside table values interpolation method for sub fields 
        :type interpolationMethod: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Discontinuities: bool = ...
    """
    Returns  a flag specifying if the table has discontinuites 
    
    <hr>
    
    Getter Method
    
    Signature ``Discontinuities`` 
    
    :returns:  a flag specifying if the links table or any referenced field tables has discontinuites  
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ValuesOutsideTableInterpolation: FieldEvaluatorValuesOutsideTableInterpolationEnum = ...
    """
    Returns or sets  the outside table values interpolation method for linear interpolation 
    
    <hr>
    
    Getter Method
    
    Signature ``ValuesOutsideTableInterpolation`` 
    
    :returns:  the outside table values interpolation method  
    :rtype: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValuesOutsideTableInterpolation`` 
    
    :param interpolationMethod:  the outside table values interpolation method  
    :type interpolationMethod: :py:class:`NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: FieldLinksTable = ...  # unknown typename


class FieldDomainCollection(NXOpen.TaggedObjectCollection):
    """
    Provides methods for manipulating the field domains  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Fields.FieldManager`
    
    .. versionadded:: NX4.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    


class IApplication(NXOpen.TaggedObject):
    """
    Interface for all applications registered with the Field subsystem. Each application
    type should only be registered once with the Field subsystem. Each application class is identified
    by its name. 
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX12.0.0
    """
    Name: str = ...
    """
    Returns  the name of the application.  
    
    This name should be unique for each application class.
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: IApplication = ...  # unknown typename


class FieldVariableTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FieldVariableType():
    """
    Variable Types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", " - "
       "Independent", " - "
       "Dependent", " - "
    """
    Unknown = -1  # FieldVariableTypeMemberType
    Independent = 0  # FieldVariableTypeMemberType
    Dependent = 1  # FieldVariableTypeMemberType
    
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
    


class FieldVariableValueTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FieldVariableValueType():
    """
    Variable value Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Real", "real"
       "Imaginary", "(Legacy) imaginary"
       "ComplexRealImaginary", "(Legacy) complex_real_imaginary"
       "ComplexMagnitudePhase", "(Legacy) complex_magnitude_phase"
       "Complex", "Complex"
       "Integer", "Integer"
    """
    Real = 0  # FieldVariableValueTypeMemberType
    Imaginary = 1  # FieldVariableValueTypeMemberType
    ComplexRealImaginary = 2  # FieldVariableValueTypeMemberType
    ComplexMagnitudePhase = 3  # FieldVariableValueTypeMemberType
    Complex = 4  # FieldVariableValueTypeMemberType
    Integer = 5  # FieldVariableValueTypeMemberType
    
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
    


class FieldVariable(NXOpen.NXObject):
    """
    Represents the Field Variables  
    
    A variable is a symbol on whose value a function, polynomial, etc., depends. For example,
    the variables in the function **<tt>f(x,y)</tt></b> are **<tt>x</tt></b> and **<tt>y</tt></b>. A
    function having a single variable is said to be univariate, one having two variables is said to be
    bivariate, and one having three or more variables is said to be multivariate.  In NX, variables in
    this sense are specifically referred to as independent variables.
    
    In NX, variables are also used to describe the output of a function; these are referred to
    as the **<tt>dependent variables</tt></b>.  In NX, a field with a single dependent variable is
    called a **<tt>scalar field</tt></b>, with three variables of the same measure a **<tt>vector field</tt></b>,
    all others are simply referred to as fields.
    
    In NX, all variables have a measure and associated unit type specification (see also
    :py:class:`NXOpen.Unit`).
    
    .. versionadded:: NX4.0.0
    """
    
    class Type():
        """
        Variable Types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unknown", " - "
           "Independent", " - "
           "Dependent", " - "
        """
        Unknown = -1  # FieldVariableTypeMemberType
        Independent = 0  # FieldVariableTypeMemberType
        Dependent = 1  # FieldVariableTypeMemberType
        
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
        
    
    
    class ValueType():
        """
        Variable value Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Real", "real"
           "Imaginary", "(Legacy) imaginary"
           "ComplexRealImaginary", "(Legacy) complex_real_imaginary"
           "ComplexMagnitudePhase", "(Legacy) complex_magnitude_phase"
           "Complex", "Complex"
           "Integer", "Integer"
        """
        Real = 0  # FieldVariableValueTypeMemberType
        Imaginary = 1  # FieldVariableValueTypeMemberType
        ComplexRealImaginary = 2  # FieldVariableValueTypeMemberType
        ComplexMagnitudePhase = 3  # FieldVariableValueTypeMemberType
        Complex = 4  # FieldVariableValueTypeMemberType
        Integer = 5  # FieldVariableValueTypeMemberType
        
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
        
    
    
    class Bounds():
        """
        Variable Bounds structure .  
        
        Constructor: 
        NXOpen.Fields.FieldVariable.Bounds()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        IsMinimumDefined: bool = ...
        """
        true if minimum bound is defined 
        <hr>
        
        Field Value
        Type:bool
        """
        IsMinimumInclusive: bool = ...
        """
        true if minimum bound is inclusive 
        <hr>
        
        Field Value
        Type:bool
        """
        MinimumValue: float = ...
        """
        minimum bound value 
        <hr>
        
        Field Value
        Type:float
        """
        IsMaximumDefined: bool = ...
        """
        true if maximum bound is defined 
        <hr>
        
        Field Value
        Type:bool
        """
        IsMaximumInclusive: bool = ...
        """
        true if maximum bound is inclusive 
        <hr>
        
        Field Value
        Type:bool
        """
        MaximumValue: float = ...
        """
        maximum bound value 
        <hr>
        
        Field Value
        Type:float
        """
    
    DefaultValue: float = ...
    """
    Returns  the variable's default value which is value used when evaluating a field and no value is specified  
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultValue`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    """
    Logarithmic: bool = ...
    """
    Returns  the flag indicating if the units for this variable are stored/retrieved as logarithmic units    
    
    <hr>
    
    Getter Method
    
    Signature ``Logarithmic`` 
    
    :returns:  a flag specifying if the variable units are logarithmic    
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    NameVariable: NameVariable = ...
    """
    Returns  the name variable for this variable.  
    
    <hr>
    
    Getter Method
    
    Signature ``NameVariable`` 
    
    :returns:  Units for this Variable   
    :rtype: :py:class:`NXOpen.Fields.NameVariable` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    """
    NumPoints: int = ...
    """
    Returns  the number of points used for this variable when generating a table    
    
    <hr>
    
    Getter Method
    
    Signature ``NumPoints`` 
    
    :returns:     
    :rtype: int 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    """
    Units: NXOpen.Unit = ...
    """
    Returns  the units for this variable, which can be None if the variable is unitless.  
    
    <hr>
    
    Getter Method
    
    Signature ``Units`` 
    
    :returns:  Units for this Variable   
    :rtype: :py:class:`NXOpen.Unit` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    """
    VariableBounds: FieldVariableBounds_Struct = ...
    """
    Returns  the variable's minimum and maximum bounds.  
    
    <hr>
    
    Getter Method
    
    Signature ``VariableBounds`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.FieldVariableBounds_Struct` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    """
    VariableType: FieldVariableType = ...
    """
    Returns  the type of variable.  
    
    <hr>
    
    Getter Method
    
    Signature ``VariableType`` 
    
    :returns:  Type of Variable   
    :rtype: :py:class:`NXOpen.Fields.FieldVariableType` 
    
    .. versionadded:: NX7.5.2
    
    License requirements: None.
    """
    Null: FieldVariable = ...  # unknown typename


