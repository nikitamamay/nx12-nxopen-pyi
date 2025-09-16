# module 'NXOpen.CAE.Xyplot'
#
# Automatically generated 2025-06-09T14:38:44.621129
#

import typing

import NXOpen
import NXOpen.CAE
import NXOpen.CAE.FTK
import NXOpen.Display
import NXOpen.Preferences



class LimitsTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LimitsType():
    """
    Represents the axis limits type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FreeLimits", "Type to use source data limits as axis limits"
       "OptimizedLimits", "Type to optimize source data limits to natural axis limits"
       "FixedLimits", "Type to use customized data limits as axis limits"
    """
    FreeLimits = 0  # LimitsTypeMemberType
    OptimizedLimits = 1  # LimitsTypeMemberType
    FixedLimits = 2  # LimitsTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ComplexOption3DMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComplexOption3D():
    """
    Represents the 3D plot complex option 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Magnitude", "Magnitude of the complex data for 3D plot"
       "Phase", "Phase of the complex data for 3D plot"
       "Real", "Real part of the complex data for 3D plot"
       "Imaginary", "Imaginary part of the complex data for 3D plot"
       "Argand", "Argand for 3D plot which use the real z coordindate"
       "Orbit", "Orbit for 3D plot"
       "Nichols", "Nichols for 3D plot"
       "AtPhaseAngle", "At phase angle for 3D plot"
       "SignedMagnitude", "Signed magnitude for 3D plot"
    """
    Magnitude = 0  # ComplexOption3DMemberType
    Phase = 1  # ComplexOption3DMemberType
    Real = 2  # ComplexOption3DMemberType
    Imaginary = 3  # ComplexOption3DMemberType
    Argand = 4  # ComplexOption3DMemberType
    Orbit = 5  # ComplexOption3DMemberType
    Nichols = 6  # ComplexOption3DMemberType
    AtPhaseAngle = 7  # ComplexOption3DMemberType
    SignedMagnitude = 8  # ComplexOption3DMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IDisplayStyle():
    """
    Represents the interface for  plot display style classes  
    
    .. versionadded:: NX9.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class BaseDisplayStyleSetting(NXOpen.TaggedObject, IDisplayStyle):
    """
    Represent an abstract object on display style.  
    
    not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def Find(self, journalIdentifier: str) -> NXOpen.TaggedObject:
        """
        Finds the :py:class:`NXOpen.TaggedObject` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``Find(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier of the object  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CommitChange(self) -> None:
        """
        Commits any edits that have been applied to the display style.  
        
        Triggers the corresponding plot to update graph. 
        
        Signature ``CommitChange()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    JournalIdentifier: str = ...
    """
    Returns  the identifier that would be recorded in a journal for this object.  
    
    This may not be the same across different releases of the software. 
    
    <hr>
    
    Getter Method
    
    Signature ``JournalIdentifier`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Owner: IDisplayStyle = ...
    """
    Returns  the owner style 
    
    <hr>
    
    Getter Method
    
    Signature ``Owner`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.IDisplayStyle` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: BaseDisplayStyleSetting = ...  # unknown typename


class AxisStyleSetting(BaseDisplayStyleSetting):
    """
    Represents the axis display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    
    def GetLabelStyle(self) -> CustomTextStyleSetting:
        """
        Gets the label style  
        
        Signature ``GetLabelStyle()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Xyplot.CustomTextStyleSetting` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNumberStyle(self) -> TextStyleSetting:
        """
        Gets the number style  
        
        Signature ``GetNumberStyle()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Xyplot.TextStyleSetting` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDBSettings(self) -> NXOpen.CAE.SignalProcessingDBSettings:
        """
        Gets the dB settings  
        
        Signature ``GetDBSettings()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.SignalProcessingDBSettings` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFixedLimits(self) -> tuple:
        """
        Gets the fixed limits
        
        Signature ``GetFixedLimits()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (lowerLimit, upperLimit). lowerLimit is a float. upperLimit is a float. 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFixedLimits(self, lowerLimit: float, upperLimit: float) -> None:
        """
        Sets the fixed limits
        
        Signature ``SetFixedLimits(lowerLimit, upperLimit)`` 
        
        :param lowerLimit: 
        :type lowerLimit: float 
        :param upperLimit: 
        :type upperLimit: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def LogUnitChangedEvent(self) -> None:
        """
        Logs an update event for changing display unit before committing AxisStyleSetting change.  
        
        Signature ``LogUnitChangedEvent()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDisplayUnit(self) -> NXOpen.CAE.FTK.BaseUnit:
        """
        Gets display unit 
        
        Signature ``GetDisplayUnit()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    AxisType: AxisType = ...
    """
    Returns or sets  the axis scale type 
    
    <hr>
    
    Getter Method
    
    Signature ``AxisType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.AxisType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AxisType`` 
    
    :param axisType: 
    :type axisType: :py:class:`NXOpen.CAE.Xyplot.AxisType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    DbDecades: int = ...
    """
    Returns or sets  the number of dB decades to display.  
    
    Avaliable when :py:meth:`CAE.Xyplot.AxisStyleSetting.AxisType``
    is :py:class:`CAE.XyplotAxisType.Db <CAE.XyplotAxisType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``DbDecades`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Removed without replacement.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DbDecades`` 
    
    :param dbDecades: 
    :type dbDecades: int 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Removed without replacement.
    
    License requirements: None.
    """
    DbRef: float = ...
    """
    Returns or sets  the dB reference value for a dB axis type.  
    
    Avaliable when :py:meth:`CAE.Xyplot.AxisStyleSetting.AxisType``
    is :py:class:`CAE.XyplotAxisType.Db <CAE.XyplotAxisType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``DbRef`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.SignalProcessingDBSettings.DBReference`
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DbRef`` 
    
    :param dbRef: 
    :type dbRef: float 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.SignalProcessingDBSettings.SetDBReference`
    
    License requirements: None.
    """
    DbScale: AxisDBScale = ...
    """
    Returns or sets  the dB scale.  
    
    Avaliable when :py:meth:`CAE.Xyplot.AxisStyleSetting.AxisType``
    is :py:class:`CAE.XyplotAxisType.Db <CAE.XyplotAxisType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``DbScale`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.AxisDBScale` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.SignalProcessingDBSettings.DBFormat`
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DbScale`` 
    
    :param dbScale: 
    :type dbScale: :py:class:`NXOpen.CAE.Xyplot.AxisDBScale` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.SignalProcessingDBSettings.SetDBFormat`
    
    License requirements: None.
    """
    GraphOverhead: int = ...
    """
    Returns or sets  the round value to display.  
    
    It is a percent value. Avaliable when :py:meth:`CAE.Xyplot.AxisStyleSetting.AxisType``
    is not :py:class:`CAE.XyplotAxisType.Auto <CAE.XyplotAxisType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``GraphOverhead`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Removed without replacement.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GraphOverhead`` 
    
    :param graphOverhead: 
    :type graphOverhead: int 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Removed without replacement.
    
    License requirements: None.
    """
    LimitsType: LimitsType = ...
    """
    Returns or sets  the limits type
    
    <hr>
    
    Getter Method
    
    Signature ``LimitsType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.LimitsType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LimitsType`` 
    
    :param limitsType: 
    :type limitsType: :py:class:`NXOpen.CAE.Xyplot.LimitsType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LogDecades: int = ...
    """
    Returns or sets  the number of Log decades to display.  
    
    Avaliable when :py:meth:`CAE.Xyplot.AxisStyleSetting.AxisType``
    is :py:class:`CAE.XyplotAxisType.Log <CAE.XyplotAxisType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``LogDecades`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LogDecades`` 
    
    :param logDecades: 
    :type logDecades: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    UnitSystem: UnitSystem = ...
    """
    Returns or sets  the unit system 
    
    <hr>
    
    Getter Method
    
    Signature ``UnitSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.UnitSystem` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.AxisStyleSetting.UnitSystemType` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UnitSystem`` 
    
    :param unitSystem: 
    :type unitSystem: :py:class:`NXOpen.CAE.Xyplot.UnitSystem` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.AxisStyleSetting.UnitSystemType` instead.
    
    License requirements: None.
    """
    UnitSystemType: NXOpen.CAE.XyFunctionUnitSystem = ...
    """
    Returns or sets  the unit system type
    
    <hr>
    
    Getter Method
    
    Signature ``UnitSystemType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.XyFunctionUnitSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UnitSystemType`` 
    
    :param unitSystemType: 
    :type unitSystemType: :py:class:`NXOpen.CAE.XyFunctionUnitSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: AxisStyleSetting = ...  # unknown typename


class GridStyleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GridStyle():
    """
    Represents the grid style for plot 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoGrid", "No grid displayed"
       "GridOnly", "Only display grid"
       "TicksOnly", "Only display tick"
       "GridAndTicks", "Display both grid and tick"
       "DenseGrid", "Display dense grid"
    """
    NoGrid = 0  # GridStyleMemberType
    GridOnly = 1  # GridStyleMemberType
    TicksOnly = 2  # GridStyleMemberType
    GridAndTicks = 3  # GridStyleMemberType
    DenseGrid = 4  # GridStyleMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BaseSymbolStyleSetting(BaseDisplayStyleSetting):
    """
    Represents the base symbol display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    This is an abstract class.
    
    .. versionadded:: NX9.0.0
    """
    PointMarker: PointMarker = ...
    """
    Returns or sets  the point marker 
    
    <hr>
    
    Getter Method
    
    Signature ``PointMarker`` 
    
    :returns:     
    :rtype: :py:class:`NXOpen.CAE.Xyplot.PointMarker` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointMarker`` 
    
    :param pointMarker:     
    :type pointMarker: :py:class:`NXOpen.CAE.Xyplot.PointMarker` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: BaseSymbolStyleSetting = ...  # unknown typename


class BaseLineStyleSetting(BaseSymbolStyleSetting):
    """
    Represents the base line display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    Color: NXOpen.NXColor = ...
    """
    Returns or sets  the line color
    
    <hr>
    
    Getter Method
    
    Signature ``Color`` 
    
    :returns:  Text font color  
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Color`` 
    
    :param color:  Text font color  
    :type color: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Font: NXOpen.DisplayableObjectObjectFont = ...
    """
    Returns or sets  the line font 
    
    <hr>
    
    Getter Method
    
    Signature ``Font`` 
    
    :returns:  Text font  
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Font`` 
    
    :param font:  Text font  
    :type font: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Width: NXOpen.DisplayableObjectObjectWidth = ...
    """
    Returns or sets  the line width
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns:  Text line width  
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param lineWidth:  Text line width  
    :type lineWidth: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: BaseLineStyleSetting = ...  # unknown typename


class LineStyle3DSetting(BaseLineStyleSetting):
    """
    Represents the 3d line display style.  
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    Direction: Direction = ...
    """
    Returns or sets  the line direction 
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.CAE.Xyplot.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: LineStyle3DSetting = ...  # unknown typename


class BarChartStyleSetting(BaseSymbolStyleSetting):
    """
    Represents the bar chart display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    FillingColor: NXOpen.NXColor = ...
    """
    Returns or sets  the filling color 
    
    <hr>
    
    Getter Method
    
    Signature ``FillingColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FillingColor`` 
    
    :param fillingColor: 
    :type fillingColor: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    OutlineColor: NXOpen.NXColor = ...
    """
    Returns or sets  the outline color 
    
    <hr>
    
    Getter Method
    
    Signature ``OutlineColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutlineColor`` 
    
    :param outlineColor: 
    :type outlineColor: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    PointMarkerIdx: PointMarker = ...
    """
    Returns or sets  the point marker 
    
    <hr>
    
    Getter Method
    
    Signature ``PointMarkerIdx`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.PointMarker` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointMarkerIdx`` 
    
    :param pointMarker: 
    :type pointMarker: :py:class:`NXOpen.CAE.Xyplot.PointMarker` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowOutline: bool = ...
    """
    Returns or sets  the outline visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOutline`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOutline`` 
    
    :param showOutline: 
    :type showOutline: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowText: bool = ...
    """
    Returns or sets  the text visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowText`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowText`` 
    
    :param showText: 
    :type showText: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SpaceBetweenTextAndBar: int = ...
    """
    Returns or sets  the spaces between text and bar measured in percentage.  
    
    The acceptable range is 0-10. 
    
    <hr>
    
    Getter Method
    
    Signature ``SpaceBetweenTextAndBar`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpaceBetweenTextAndBar`` 
    
    :param spaceBetweenTextAndBar: 
    :type spaceBetweenTextAndBar: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: BarChartStyleSetting = ...  # unknown typename


class IDisplayableModel():
    """
    This class represents an interface to the XYPLOT displayable model  
    
    . 
    
    .. versionadded:: NX11.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class BaseModel(NXOpen.NXObject, IDisplayableModel):
    """
    Represents an abstract component object on a XY graphing.  
    
    not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def UpdateDisplay(self) -> None:
        """
        Updates model display 
        
        Signature ``UpdateDisplay()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: BaseModel = ...  # unknown typename


class BasicModel(BaseModel):
    """
    Represents a abstract component object on a XY graphing.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def Find(self, journalIdentifier: str) -> NXOpen.TaggedObject:
        """
        Finds the :py:class:`NXObject` with the given identifier as recorded in a journal. 
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``Find(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier of the object  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX12.0.0
           Use :py:meth:`NXOpen.INXObject.FindObject`
        
        License requirements: None.
        """
        ...
    
    DisplayStyle: IDisplayStyle = ...
    """
    Returns  the model display style 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayStyle`` 
    
    :returns:  Model display style  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.IDisplayStyle` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: BasicModel = ...  # unknown typename


class NoteModel(BasicModel):
    """
    Represents a note object on a plot.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def GetTexts(self) -> 'list[str]':
        """
        Gets the note content.  
        
        Signature ``GetTexts()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTexts(self, content: 'list[str]') -> None:
        """
        Sets the note content.  
        
        Signature ``SetTexts(content)`` 
        
        :param content: 
        :type content: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTextPosition(self) -> NXOpen.Point2d:
        """
        Gets the display position of note content.  
        
        Signature ``GetTextPosition()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Point2d` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTextPosition(self, position: NXOpen.Point2d) -> None:
        """
        Sets the display position of note content.  
        
        Signature ``SetTextPosition(position)`` 
        
        :param position: 
        :type position: :py:class:`NXOpen.Point2d` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Delete(self) -> None:
        """
        Deletes the note model 
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: NoteModel = ...  # unknown typename


class DecimalFormatMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DecimalFormat():
    """
    Represents the decimal number format 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Actual", "Show decimal automatically"
       "X", "Displays one digit followed by period"
       "Xx", "Displays two digits followed by period"
       "Xxx", "Displays three digits followed by period"
       "Xxxx", "Displays four digits followed by period"
       "Xexx", "Scientific notation with one digit followed by period,for example: 5.3E+05"
       "Xxexx", "Scientific notation with two digits followed by period"
       "Xxxexx", "Scientific notation with three digits followed by period"
       "Xxxxexx", "Scientific notation with four digits followed by period"
    """
    Actual = 0  # DecimalFormatMemberType
    X = 1  # DecimalFormatMemberType
    Xx = 2  # DecimalFormatMemberType
    Xxx = 3  # DecimalFormatMemberType
    Xxxx = 4  # DecimalFormatMemberType
    Xexx = 5  # DecimalFormatMemberType
    Xxexx = 6  # DecimalFormatMemberType
    Xxxexx = 7  # DecimalFormatMemberType
    Xxxxexx = 8  # DecimalFormatMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IVisibleDisplayStyle():
    """
    Represents the interface for visible display style classes.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class TextStyleSetting(BaseDisplayStyleSetting, IVisibleDisplayStyle):
    """
    Represents the text display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    Alignment: TextAlignment = ...
    """
    Returns or sets  the text alignment.  
    
    Only valid for title options, legend options and axis label options. 
    
    <hr>
    
    Getter Method
    
    Signature ``Alignment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.TextAlignment` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Alignment`` 
    
    :param alignment: 
    :type alignment: :py:class:`NXOpen.CAE.Xyplot.TextAlignment` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Color: NXOpen.NXColor = ...
    """
    Returns or sets  the text color 
    
    <hr>
    
    Getter Method
    
    Signature ``Color`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Color`` 
    
    :param color: 
    :type color: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Font: str = ...
    """
    Returns or sets  the text font 
    
    <hr>
    
    Getter Method
    
    Signature ``Font`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Font`` 
    
    :param font: 
    :type font: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FontStyle: NXOpen.Preferences.VisualizationFontsStyleType = ...
    """
    Returns or sets  the text font style.  
    
    Available when the text font is standard font. 
    
    <hr>
    
    Getter Method
    
    Signature ``FontStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Preferences.VisualizationFontsStyleType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FontStyle`` 
    
    :param fontStyle: 
    :type fontStyle: :py:class:`NXOpen.Preferences.VisualizationFontsStyleType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FontType: Fonttype = ...
    """
    Returns or sets  the text font type 
    
    <hr>
    
    Getter Method
    
    Signature ``FontType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.Fonttype` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FontType`` 
    
    :param fontType: 
    :type fontType: :py:class:`NXOpen.CAE.Xyplot.Fonttype` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    GlobalSizeScale: float = ...
    """
    Returns or sets  the scale of global text size.  
    
    It will be taken only when :py:meth:`CAE.Xyplot.TextStyleSetting.UseGlobalFontSetting`` is true,
    and :py:meth:`CAE.Xyplot.TextStyleSetting.IsGlobalSizeAutoScaled`` is false. 
    
    <hr>
    
    Getter Method
    
    Signature ``GlobalSizeScale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GlobalSizeScale`` 
    
    :param sizeScale: 
    :type sizeScale: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    IsGlobalSizeAutoScaled: bool = ...
    """
    Returns or sets  a value indicating whether to automatically adjust the scale of global text size to fit the screen.  
    
    It will be taken only when :py:meth:`CAE.Xyplot.TextStyleSetting.UseGlobalFontSetting`` is true. 
    
    <hr>
    
    Getter Method
    
    Signature ``IsGlobalSizeAutoScaled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsGlobalSizeAutoScaled`` 
    
    :param isGlobalSizeAutoScaled: 
    :type isGlobalSizeAutoScaled: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LeaderStyle: LeaderStyle = ...
    """
    Returns  the leader style 
    
    <hr>
    
    Getter Method
    
    Signature ``LeaderStyle`` 
    
    :returns:  Leader style  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.LeaderStyle` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    NumberFormat: NXOpen.CAE.NumberFormat = ...
    """
    Returns  the number format options 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberFormat`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.NumberFormat` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Orientation: TextOrientation = ...
    """
    Returns or sets  the text orientation.  
    
    Only invalid for legend options. 
    
    <hr>
    
    Getter Method
    
    Signature ``Orientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.TextOrientation` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Orientation`` 
    
    :param orientation: 
    :type orientation: :py:class:`NXOpen.CAE.Xyplot.TextOrientation` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Size: int = ...
    """
    Returns or sets  the text size.  
    
    The acceptable range is 1-10. 
    
    <hr>
    
    Getter Method
    
    Signature ``Size`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Size`` 
    
    :param size: 
    :type size: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TextBoxStyle: TextBoxStyleSetting = ...
    """
    Returns  the style of text box 
    
    <hr>
    
    Getter Method
    
    Signature ``TextBoxStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.TextBoxStyleSetting` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    UseGlobalFontSetting: bool = ...
    """
    Returns or sets  a value indicating whether to use the global setting of text font, font style and font size.  
    
    If True, you need to set text size scale by setting :py:meth:`CAE.Xyplot.TextStyleSetting.IsGlobalSizeAutoScaled`` or
    :py:meth:`CAE.Xyplot.TextStyleSetting.GlobalSizeScale`` 
    
    <hr>
    
    Getter Method
    
    Signature ``UseGlobalFontSetting`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseGlobalFontSetting`` 
    
    :param useGlobalFontSetting:     
    :type useGlobalFontSetting: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Weight: NXOpen.Display.TransientTextTextSize = ...
    """
    Returns or sets  the text weight.  
    
    Available when the text font is NX font. 
    
    <hr>
    
    Getter Method
    
    Signature ``Weight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TransientTextTextSize` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Weight`` 
    
    :param weight: 
    :type weight: :py:class:`NXOpen.Display.TransientTextTextSize` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param visibility: 
    :type visibility: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: TextStyleSetting = ...  # unknown typename


class CustomTextStyleSetting(TextStyleSetting):
    """
    Represents the text content definition in title options  
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    
    def GetUserDefinedText(self) -> 'list[str]':
        """
        Returns the text content defined by user.  
        
        Signature ``GetUserDefinedText()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetUserDefinedText(self, text: 'list[str]') -> None:
        """
        Sets the text content defined by user.  
        
        Signature ``SetUserDefinedText(text)`` 
        
        :param text: 
        :type text: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    UseAutomatic: bool = ...
    """
    Returns or sets  a value indicating whether to define text content automatically .  
    
    <hr>
    
    Getter Method
    
    Signature ``UseAutomatic`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseAutomatic`` 
    
    :param useAutomatic:     
    :type useAutomatic: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: CustomTextStyleSetting = ...  # unknown typename


class AxisLabelStyle(CustomTextStyleSetting):
    """
    Represents the axis label display style.  
    
    Call :py:meth:`CAE.Xyplot.IDisplayStyle.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    IncludeMeasureType: bool = ...
    """
    Returns or sets  the option specifies whether to include measure type in axis label 
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeMeasureType`` 
    
    :returns:  include measure type  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeMeasureType`` 
    
    :param hasIncludeMeasureType:  include measure type  
    :type hasIncludeMeasureType: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IncludeUnit: bool = ...
    """
    Returns or sets  the option specifies whether to include unit information in axis label 
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeUnit`` 
    
    :returns:  include unit  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeUnit`` 
    
    :param hasIncludeUnit:  include unit  
    :type hasIncludeUnit: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    UseSingleLine: bool = ...
    """
    Returns or sets  the option specifies whether to display axis label in a single line 
    
    <hr>
    
    Getter Method
    
    Signature ``UseSingleLine`` 
    
    :returns:  sinle line  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseSingleLine`` 
    
    :param isSingleLine:  sinle line  
    :type isSingleLine: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: AxisLabelStyle = ...  # unknown typename


class PhaseRangeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PhaseRangeOption():
    """
    Prepresents the phase range option 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NegativeTwoPiToZero", "Displays phase between -360 and 0"
       "ZeroToTwoPi", "Displays phase between 0 and 360"
       "NegativePiToPi", "Displays phase between -180 and 180"
       "NegativeOneHalfPiToHalfPi", "Displays phase between -270 and 90"
       "NegativeHalfPiToOneHalfPi", "Displays phase between -90 and 270"
    """
    NegativeTwoPiToZero = 0  # PhaseRangeOptionMemberType
    ZeroToTwoPi = 1  # PhaseRangeOptionMemberType
    NegativePiToPi = 2  # PhaseRangeOptionMemberType
    NegativeOneHalfPiToHalfPi = 3  # PhaseRangeOptionMemberType
    NegativeHalfPiToOneHalfPi = 4  # PhaseRangeOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ProbingStyle(BaseDisplayStyleSetting):
    """
    Manages the probing display styles.  
    
    Not support KF.
    """
    HelpLineStyle: CurveDisplaySettings = ...
    """
    Returns  the help line display style.  
    
    <hr>
    
    Getter Method
    
    Signature ``HelpLineStyle`` 
    
    :returns:  Probing help line style  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    StepLineStyle: CurveDisplaySettings = ...
    """
    Returns  the step line display style.  
    
    <hr>
    
    Getter Method
    
    Signature ``StepLineStyle`` 
    
    :returns:  Probing step line style  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    TextStyle: TextStyleSetting = ...
    """
    Returns  the text display style.  
    
    <hr>
    
    Getter Method
    
    Signature ``TextStyle`` 
    
    :returns:  Text display style  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.TextStyleSetting` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ProbingStyle = ...  # unknown typename


class GraphNameStyle(TextStyleSetting):
    """
    Represents the graph name display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    PositionOption: GraphNamePositionOption = ...
    """
    Returns or sets  the option specifies how to position the graph name 
    
    <hr>
    
    Getter Method
    
    Signature ``PositionOption`` 
    
    :returns:  postion option  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.GraphNamePositionOption` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PositionOption`` 
    
    :param positionOption:  postion option  
    :type positionOption: :py:class:`NXOpen.CAE.Xyplot.GraphNamePositionOption` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: GraphNameStyle = ...  # unknown typename


class PlotGraphTemplate(BaseDisplayStyleSetting):
    """
    Manages the plot graph template.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def ResetToDefault(self) -> None:
        """
        Resets the graph template to default values 
        
        Signature ``ResetToDefault()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ImportTemplate(self, strXmlFile: str) -> None:
        """
        Updates current graph template setting from a template xml file 
        
        Signature ``ImportTemplate(strXmlFile)`` 
        
        :param strXmlFile:  Template xml file name  
        :type strXmlFile: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ExportTemplate(self, strXmlFile: str) -> None:
        """
        Exports current graph template setting to a template xml file,
        it will override the template file if it is existing.  
        
        Signature ``ExportTemplate(strXmlFile)`` 
        
        :param strXmlFile:  Template xml file name  
        :type strXmlFile: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    AbscissaCustomMarkerLabel: str = ...
    """
    Returns or sets  the abscissa custom marker label 
    
    <hr>
    
    Getter Method
    
    Signature ``AbscissaCustomMarkerLabel`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AbscissaCustomMarkerLabel`` 
    
    :param xCustomMarkerLabel: 
    :type xCustomMarkerLabel: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DiagramDisplayStyles: DiagramDisplayStyles = ...
    """
    Returns  the diagram display styles.  
    
    <hr>
    
    Getter Method
    
    Signature ``DiagramDisplayStyles`` 
    
    :returns:  Diagram display styles  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.DiagramDisplayStyles` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    GeneralDisplayStyles: GeneralDisplayStyles = ...
    """
    Returns  the general display styles.  
    
    <hr>
    
    Getter Method
    
    Signature ``GeneralDisplayStyles`` 
    
    :returns:  General display styles  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.GeneralDisplayStyles` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    OrdinateCustomMarkerLabel: str = ...
    """
    Returns or sets  the ordinate custom marker label 
    
    <hr>
    
    Getter Method
    
    Signature ``OrdinateCustomMarkerLabel`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OrdinateCustomMarkerLabel`` 
    
    :param yCustomMarkerLabel: 
    :type yCustomMarkerLabel: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    WallDisplayStyles: WallDisplayStyles = ...
    """
    Returns  the wall display styles.  
    
    <hr>
    
    Getter Method
    
    Signature ``WallDisplayStyles`` 
    
    :returns:  Wall display styles  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.WallDisplayStyles` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ZCustomMarkerLabel: str = ...
    """
    Returns or sets  the z custom marker label 
    
    <hr>
    
    Getter Method
    
    Signature ``ZCustomMarkerLabel`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZCustomMarkerLabel`` 
    
    :param zCustomMarkerLabel: 
    :type zCustomMarkerLabel: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: PlotGraphTemplate = ...  # unknown typename


class Graph(BaseModel):
    """
    Manages the display graph.  
    
    Each graph has its owner axis and graph name. 
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def GetPointCount(self, recordIndex: int) -> int:
        """
        Gets the point count of specified record.  
        
        Signature ``GetPointCount(recordIndex)`` 
        
        :param recordIndex:  Record index  
        :type recordIndex: int 
        :returns:  Point count  
        :rtype: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateMarker(self, recordIndex: int, pointIndex: int) -> MarkerModel:
        """
        Creates a marker in the position of a source point.  
        
        <remarker>
        The record index is between 0 and :py:meth:`CAE.Xyplot.Graph.RecordCount`, 0 is inclusive. 
        The point index is between 0 and :py:meth:`CAE.Xyplot.Graph.GetPointCount`, 0 is inclusive. 
        </remarker>
        
        Signature ``CreateMarker(recordIndex, pointIndex)`` 
        
        :param recordIndex:  Record index  
        :type recordIndex: int 
        :param pointIndex:  Point index  
        :type pointIndex: int 
        :returns:  Marker model  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.MarkerModel` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateMarker(self, recordIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> MarkerModel:
        """
        <summary> Creates a marker in the linear interpolation position between two source points. </summary>
        <remarker>
        The record index is between 0 and :py:meth:`CAE.Xyplot.Graph.RecordCount`, 0 is inclusive. 
        The previous point index is between 0 and :py:meth:`CAE.Xyplot.Graph.GetPointCount`, 0 is inclusive.
        The next point index is between 0 and :py:meth:`CAE.Xyplot.Graph.GetPointCount`, 0 is inclusive. 
        The linear interpolation scale is between 0 and 1, both 0 and 1 are inclusive. 
        </remarker>
        
        Signature ``CreateMarker(recordIndex, prePointIndex, nextPointIndex, linearInterpoScale)`` 
        
        :param recordIndex:  Record index  
        :type recordIndex: int 
        :param prePointIndex:  Previous Point index  
        :type prePointIndex: int 
        :param nextPointIndex:  Next Point index  
        :type nextPointIndex: int 
        :param linearInterpoScale:  Interpolation Scale  
        :type linearInterpoScale: float 
        :returns:  Marker model  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.MarkerModel` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAssociativeMarker(self, recordIndex: int, attachType: AnchorType, absPercentage: float) -> MarkerModel:
        """
        Creates an associative marker.  
        
        <remarker>
        The record index is between 0 and :py:meth:`CAE.Xyplot.Graph.RecordCount`, 0 is inclusive.
        </remarker>
        
        Signature ``CreateAssociativeMarker(recordIndex, attachType, absPercentage)`` 
        
        :param recordIndex:  Record index  
        :type recordIndex: int 
        :param attachType:  Attachment Type  
        :type attachType: :py:class:`NXOpen.CAE.Xyplot.AnchorType` 
        :param absPercentage:  When attachment type is :py:class:`CAE.XyplotAnchorType.AbsPercentage <CAE.XyplotAnchorType>`,                                                                         a valid abscissa percentage(between 0 and 1, both 0 and 1 are inclusive) should be given.  
        :type absPercentage: float 
        :returns:  Marker model  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.MarkerModel` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetMarkers(self) -> 'list[MarkerModel]':
        """
        Gets all markers on the graph.  
        
        Signature ``GetMarkers()`` 
        
        :returns:  Marker models  
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.MarkerModel` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAnchorPointOfRecord(self, recordIndex: int, anchorType: AnchorType) -> tuple:
        """
        Gets anchor point of a record.  
        
        Signature ``GetAnchorPointOfRecord(recordIndex, anchorType)`` 
        
        :param recordIndex: 
        :type recordIndex: int 
        :param anchorType: 
        :type anchorType: :py:class:`NXOpen.CAE.Xyplot.AnchorType` 
        :returns: a tuple 
        :rtype: A tuple consisting of (hasAnchorPoint, anchorPoint). hasAnchorPoint is a bool. anchorPoint is a :py:class:`NXOpen.Point3d`. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRecordName(self, recordIndex: int) -> str:
        """
        Gets record name.  
        
        Signature ``GetRecordName(recordIndex)`` 
        
        :param recordIndex: 
        :type recordIndex: int 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetGridBoundingBox(self) -> tuple:
        """
        Gets the bounding box of the grid.  
        
        Signature ``GetGridBoundingBox()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (leftBottom, rightTop). leftBottom is a :py:class:`NXOpen.Point3d`. rightTop is a :py:class:`NXOpen.Point3d`. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAbscissaAxis(self) -> BasicModel:
        """
        Gets the abscissa axis.  
        
        Signature ``GetAbscissaAxis()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Xyplot.BasicModel` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOrdinateAxes(self) -> 'list[BasicModel]':
        """
        Gets the ordinate axes.  
        
        Signature ``GetOrdinateAxes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.BasicModel` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetZAxis(self) -> BasicModel:
        """
        Gets the Z axis.  
        
        Signature ``GetZAxis()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Xyplot.BasicModel` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDisplayStyleOfRecord(self, recordIndex: int, displayStyleIndex: int) -> None:
        """
        Sets the display style index for a plotted record.  
        
        The display style index is limitted from 0 to 19.
        
        Signature ``SetDisplayStyleOfRecord(recordIndex, displayStyleIndex)`` 
        
        :param recordIndex: 
        :type recordIndex: int 
        :param displayStyleIndex: 
        :type displayStyleIndex: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ZoomAlongX(self, startScale: float, endScale: float) -> None:
        """
        Zooms the graph along X direction by a scale range basing on current X axis display range.
        
          #. 
        The function just updates the model data. To make the display update to reflect the model change, please call
        :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` for an instance of :py:class:`CAE.Xyplot.Plot` or
        :py:class:`CAE.Xyplot.Graph`.
        
          #. 
        The scale range could be calculated from :py:meth:`CAE.Xyplot.AxisModel.CalculateZoomScale`
        
        Signature ``ZoomAlongX(startScale, endScale)`` 
        
        :param startScale:  the value must be between 0 and 1 
        :type startScale: float 
        :param endScale:  the value must be between 0 and 1 
        :type endScale: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ZoomAlongY(self, startScale: float, endScale: float) -> None:
        """
        Zooms the graph along Y direction by a scale range basing on current Y axis display range.
        
          #. 
        The function just updates the model data. To make the display update to reflect the model change, please call
        :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` for an instance of :py:class:`CAE.Xyplot.Plot` or
        :py:class:`CAE.Xyplot.Graph`.
        
          #. 
        The scale range could be calculated from :py:meth:`CAE.Xyplot.AxisModel.CalculateZoomScale`
        
        Signature ``ZoomAlongY(startScale, endScale)`` 
        
        :param startScale:  the value must be between 0 and 1 
        :type startScale: float 
        :param endScale:  the value must be between 0 and 1 
        :type endScale: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ZoomAlongZ(self, startScale: float, endScale: float) -> None:
        """
        Zooms the graph along Z direction by a scale range basing on current Z axis display range. It is only available to 3D plot.
        
          #. 
        The function just updates the model data. To make the display update to reflect the model change, please call
        :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` for an instance of :py:class:`CAE.Xyplot.Plot` or
        :py:class:`CAE.Xyplot.Graph`.
        
          #. 
        The scale range could be calculated from :py:meth:`CAE.Xyplot.AxisModel.CalculateZoomScale`
        
        Signature ``ZoomAlongZ(startScale, endScale)`` 
        
        :param startScale:  the value must be between 0 and 1 
        :type startScale: float 
        :param endScale:  the value must be between 0 and 1 
        :type endScale: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ZoomAlongXY(self, xStartScale: float, xEndScale: float, yStartScale: float, yEndScale: float) -> None:
        """
        Zooms the graph along both X and Y direction by scale ranges basing on current X and Y axis display range. It is only available to 2D plot.
        
          #. 
        The function just updates the model data. To make the display update to reflect the model change, please call
        :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` for an instance of :py:class:`CAE.Xyplot.Plot` or
        :py:class:`CAE.Xyplot.Graph`.
        
          #. 
        The scale range could be calculated from :py:meth:`CAE.Xyplot.AxisModel.CalculateZoomScale`
        
        Signature ``ZoomAlongXY(xStartScale, xEndScale, yStartScale, yEndScale)`` 
        
        :param xStartScale:  the value must be between 0 and 1 
        :type xStartScale: float 
        :param xEndScale:  the value must be between 0 and 1 
        :type xEndScale: float 
        :param yStartScale:  the value must be between 0 and 1 
        :type yStartScale: float 
        :param yEndScale:  the value must be between 0 and 1 
        :type yEndScale: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Unzoom(self) -> None:
        """
        Removes the zoom state for the graph and returns the display to the original state.
        
        The function just updates the model data. To make the display update to reflect the model change, please call
        :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` for an instance of :py:class:`CAE.Xyplot.Plot` or
        :py:class:`CAE.Xyplot.Graph`
        
        Signature ``Unzoom()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Find(self, journalIdentifier: str) -> NXOpen.TaggedObject:
        """
        Finds the :py:class:`NXObject` with the given identifier as recorded in a journal. 
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``Find(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier of the object  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX12.0.0
           Use :py:meth:`NXOpen.INXObject.FindObject`
        
        License requirements: None.
        """
        ...
    
    RecordCount: int = ...
    """
    Returns  the record count of the graph.  
    
    <hr>
    
    Getter Method
    
    Signature ``RecordCount`` 
    
    :returns:  Record count  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: Graph = ...  # unknown typename


class I3DDataGraph():
    """
    Represents a graph interface which input is 3D data 
    
    .
    <remarker>
    3D plot data can consist of multiple :py:class:`CAE.FTK.ArrayRecord2D` or a :py:class:`CAE.FTK.SectionBasedMatrixRecord`
    </remarker>
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class Graph3D(Graph, I3DDataGraph):
    """
    Manages the display graph 3d.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetSourcePointCount(self, recordIndex: int, sectionIndex: int) -> int:
        """
        Gets the source point count of specified record.  
        
        <remarker>
        The record index is between 0 and :py:meth:`CAE.Xyplot.Graph.RecordCount`, 0 is inclusive.
        </remarker>
        
        Signature ``GetSourcePointCount(recordIndex, sectionIndex)`` 
        
        :param recordIndex:  Record index  
        :type recordIndex: int 
        :param sectionIndex:  Section index  
        :type sectionIndex: int 
        :returns:  Point count  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateMarker(self, recordIndex: int, sectionIndex: int, pointIndex: int) -> MarkerModel:
        """
        Creates a marker in the position of a source point.  
        
        <remarker>
        The record index is between 0 and :py:meth:`CAE.Xyplot.Graph.RecordCount`, 0 is inclusive. 
        The point index is between 0 and :py:meth:`CAE.Xyplot.I3DDataGraph.GetSourcePointCount`, 0 is inclusive. 
        </remarker>
        
        Signature ``CreateMarker(recordIndex, sectionIndex, pointIndex)`` 
        
        :param recordIndex:  Record index  
        :type recordIndex: int 
        :param sectionIndex:  Section index  
        :type sectionIndex: int 
        :param pointIndex:  Point index  
        :type pointIndex: int 
        :returns:  Marker model  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.MarkerModel` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateMarker(self, recordIndex: int, sectionIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> MarkerModel:
        """
        <summary> Creates a marker in the linear interpolation position between two source points. </summary>
        <remarker>
        The record index is between 0 and :py:meth:`CAE.Xyplot.Graph.RecordCount`, 0 is inclusive. 
        The previous/next point index is between 0 and :py:meth:`CAE.Xyplot.I3DDataGraph.GetSourcePointCount`, 0 is inclusive.
        The linear interpolation scale is between 0 and 1, both 0 and 1 are inclusive. 
        </remarker>
        
        Signature ``CreateMarker(recordIndex, sectionIndex, prePointIndex, nextPointIndex, linearInterpoScale)`` 
        
        :param recordIndex:  Record index  
        :type recordIndex: int 
        :param sectionIndex:  Section index  
        :type sectionIndex: int 
        :param prePointIndex:  Previous Point index  
        :type prePointIndex: int 
        :param nextPointIndex:  Next Point index  
        :type nextPointIndex: int 
        :param linearInterpoScale:  Interpolation Scale  
        :type linearInterpoScale: float 
        :returns:  Marker model  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.MarkerModel` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Graph3D = ...  # unknown typename


class PreferenceTargetGraphicWindowOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PreferenceTargetGraphicWindowOption():
    """
    Defines the target graphic window type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Main", "Only shows plot graph on main graphic window"
       "Separate", "Only shows plot graph on a separate graphic window"
       "Both", "Shows plot graph on either main graphic window or a separate graphic window"
    """
    Main = 0  # PreferenceTargetGraphicWindowOptionMemberType
    Separate = 1  # PreferenceTargetGraphicWindowOptionMemberType
    Both = 2  # PreferenceTargetGraphicWindowOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PreferenceNewWindowChoiceMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PreferenceNewWindowChoice():
    """
    Defines whether to always show plot graph on a new separate graphic window 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Prompt", "Prompts user to show plot graph on either an existing or a new separate graphic window"
       "Always", "Always show plot graph on a new separate graphic window"
    """
    Prompt = 0  # PreferenceNewWindowChoiceMemberType
    Always = 1  # PreferenceNewWindowChoiceMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Preference(NXOpen.TaggedObject):
    """
    Manages the preference data.  
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    
    class TargetGraphicWindowOption():
        """
        Defines the target graphic window type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Main", "Only shows plot graph on main graphic window"
           "Separate", "Only shows plot graph on a separate graphic window"
           "Both", "Shows plot graph on either main graphic window or a separate graphic window"
        """
        Main = 0  # PreferenceTargetGraphicWindowOptionMemberType
        Separate = 1  # PreferenceTargetGraphicWindowOptionMemberType
        Both = 2  # PreferenceTargetGraphicWindowOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class NewWindowChoice():
        """
        Defines whether to always show plot graph on a new separate graphic window 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Prompt", "Prompts user to show plot graph on either an existing or a new separate graphic window"
           "Always", "Always show plot graph on a new separate graphic window"
        """
        Prompt = 0  # PreferenceNewWindowChoiceMemberType
        Always = 1  # PreferenceNewWindowChoiceMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
        Saves preference settings to memory file so that preference setting could be shared among sessions 
        
        Signature ``Save()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    AfuRecordZValue: NXOpen.CAE.FTK.DataManagerAfuRecordZValue = ...
    """
    Returns or sets  the Z value type for afu record in 3D plot 
    
    <hr>
    
    Getter Method
    
    Signature ``AfuRecordZValue`` 
    
    :returns:  The afu record z value  
    :rtype: :py:class:`NXOpen.CAE.FTK.DataManagerAfuRecordZValue` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AfuRecordZValue`` 
    
    :param afuZValue:  The 3D afu record z value  
    :type afuZValue: :py:class:`NXOpen.CAE.FTK.DataManagerAfuRecordZValue` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    MaximumLegendsInGraph: int = ...
    """
    Returns or sets  the maximum legend count on a graph.  
    
    If the record count on a graph
    exceeds this maximum number, legends will not be displayed and
    synchronized probing will be disabled. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumLegendsInGraph`` 
    
    :returns:  The maximum legend count  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.LegendTableStyle.MaximumLegendItemCount`
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumLegendsInGraph`` 
    
    :param legendCount:  The maximum legend count  
    :type legendCount: int 
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.LegendTableStyle.MaximumLegendItemCount`
    
    License requirements: None.
    """
    MaximumSubGraphsInStack: int = ...
    """
    Returns or sets  the maximum sub-graph count in a stacked graph  
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumSubGraphsInStack`` 
    
    :returns:  The maximum sub-graph count  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumSubGraphsInStack`` 
    
    :param graphCount:  The maximum sub-graph count  
    :type graphCount: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    NewWindowSetting: PreferenceNewWindowChoice = ...
    """
    Returns or sets  the new window setting value.  
    
    Avaliable when :py:meth:`CAE.Xyplot.Preference.TargetWindowSetting``
    is :py:class:`CAE.Xyplot.PreferenceTargetGraphicWindowOption.Separate <CAE.Xyplot.PreferenceTargetGraphicWindowOption>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``NewWindowSetting`` 
    
    :returns:  New window setting  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.PreferenceNewWindowChoice` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NewWindowSetting`` 
    
    :param newWindowSetting:  New window setting  
    :type newWindowSetting: :py:class:`NXOpen.CAE.Xyplot.PreferenceNewWindowChoice` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TargetWindowSetting: PreferenceTargetGraphicWindowOption = ...
    """
    Returns or sets  the target window setting value 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetWindowSetting`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.PreferenceTargetGraphicWindowOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetWindowSetting`` 
    
    :param targetWindowSetting: 
    :type targetWindowSetting: :py:class:`NXOpen.CAE.Xyplot.PreferenceTargetGraphicWindowOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    UpdateOverlayingAxisLimitsAutomatically: bool = ...
    """
    Returns or sets  the status whether to update the axis limits automatically when overlaying records at next time 
    
    <hr>
    
    Getter Method
    
    Signature ``UpdateOverlayingAxisLimitsAutomatically`` 
    
    :returns:  Whether to update axis limits  
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UpdateOverlayingAxisLimitsAutomatically`` 
    
    :param updateAxisLimits:  Whether to update axis limits  
    :type updateAxisLimits: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: Preference = ...  # unknown typename


class AnchorTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AnchorType():
    """
    Represents the anchor position of a record display, which is used to position a note 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "the normal marker without anchor type"
       "Start", "the position of start point in a record display"
       "End", "the position of end point in a record display"
       "MaximumValue", "the position of the point which has maximum value in a record display"
       "MinimumValue", "the position of the point which has minimum value in a record display"
       "AbsPercentage", "the position of the point in the set abscissa percentage"
    """
    NotSet = 0  # AnchorTypeMemberType
    Start = 1  # AnchorTypeMemberType
    End = 2  # AnchorTypeMemberType
    MaximumValue = 3  # AnchorTypeMemberType
    MinimumValue = 4  # AnchorTypeMemberType
    AbsPercentage = 5  # AnchorTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class WallDisplayStyles(NXOpen.TaggedObject):
    """
    Manages the wall display styles.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def GetTextStyleSetting(self, textType: TextType) -> TextStyleSetting:
        """
        Gets the text style.  
        
        Signature ``GetTextStyleSetting(textType)`` 
        
        :param textType:  Text type  
        :type textType: :py:class:`NXOpen.CAE.Xyplot.TextType` 
        :returns:  Text display style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.TextStyleSetting` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAxisStyleSetting(self, axisDirection: AxisDirection) -> AxisStyleSetting:
        """
        Gets the axis display style.  
        
        Signature ``GetAxisStyleSetting(axisDirection)`` 
        
        :param axisDirection:  Axis direction  
        :type axisDirection: :py:class:`NXOpen.CAE.Xyplot.AxisDirection` 
        :returns:  Axis style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.AxisStyleSetting` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLegendTableGroupStyle(self) -> LegendTableGroupStyle:
        """
        Gets the legend table group style  
        
        Signature ``GetLegendTableGroupStyle()`` 
        
        :returns:  Legend table group style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.LegendTableGroupStyle` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    GridLayoutStyleSetting: BaseGridLayoutStyleSetting = ...
    """
    Returns  the grid layout display style 
    
    <hr>
    
    Getter Method
    
    Signature ``GridLayoutStyleSetting`` 
    
    :returns:  Grid layout style  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.BaseGridLayoutStyleSetting` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ProbingStyle: ProbingStyle = ...
    """
    Returns  the probing display style 
    
    <hr>
    
    Getter Method
    
    Signature ``ProbingStyle`` 
    
    :returns:  Probing style  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.ProbingStyle` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: WallDisplayStyles = ...  # unknown typename


class WallDisplayStyles2DBarChart(WallDisplayStyles):
    """
    Manages the 2D bar chart wall display styles.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetArgumentAxisStyleSetting(self) -> ArgumentAxisStyleSetting:
        """
        Gets the argument axis display style.  
        
        Signature ``GetArgumentAxisStyleSetting()`` 
        
        :returns:  Argument Axis style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.ArgumentAxisStyleSetting` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: WallDisplayStyles2DBarChart = ...  # unknown typename


class DiagramDisplayStyles(BaseDisplayStyleSetting):
    """
    Manages the diagram display styles.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def GetGraphStyle(self, styleIndex: int) -> GraphStyle:
        """
        Gets the graph style.  
        
        The style index must be greater than or equal to 0 and
        less than :py:meth:`CAE.Xyplot.DiagramDisplayStyles.StyleCount`.  
        
        Signature ``GetGraphStyle(styleIndex)`` 
        
        :param styleIndex:  Style index  
        :type styleIndex: int 
        :returns:  Graph style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.GraphStyle` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetGraphStyle(self, styleIndex: int, graphStyle: GraphStyle) -> None:
        """
        Sets the graph style.  
        
        The style index must be greater than or equal to 0 and
        less than :py:meth:`CAE.Xyplot.DiagramDisplayStyles.StyleCount`. 
        
        Signature ``SetGraphStyle(styleIndex, graphStyle)`` 
        
        :param styleIndex:  Style index  
        :type styleIndex: int 
        :param graphStyle:  Graph style  
        :type graphStyle: :py:class:`NXOpen.CAE.Xyplot.GraphStyle` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLineStyleSetting(self, styleIndex: int) -> BaseLineStyleSetting:
        """
        Gets the line display style.  
        
        The style index must be greater than or equal to 0 and
        less than :py:meth:`CAE.Xyplot.DiagramDisplayStyles.StyleCount`.  
        
        Signature ``GetLineStyleSetting(styleIndex)`` 
        
        :param styleIndex:  Style index  
        :type styleIndex: int 
        :returns:  Line style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.BaseLineStyleSetting` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBarStyleSetting(self, styleIndex: int) -> BaseBarStyleSetting:
        """
        Gets the bar display style.  
        
        The style index must be greater than or equal to 0 and
        less than :py:meth:`CAE.Xyplot.DiagramDisplayStyles.StyleCount`.  
        
        Signature ``GetBarStyleSetting(styleIndex)`` 
        
        :param styleIndex:  Style index  
        :type styleIndex: int 
        :returns:  Bar style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.BaseBarStyleSetting` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPlateStyleSetting(self, styleIndex: int) -> BasePlateStyleSetting:
        """
        Gets the plate display style.  
        
        The style index must be greater than or equal to 0 and
        less than :py:meth:`CAE.Xyplot.DiagramDisplayStyles.StyleCount`.  
        
        Signature ``GetPlateStyleSetting(styleIndex)`` 
        
        :param styleIndex:  Style index  
        :type styleIndex: int 
        :returns:  Plate style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.BasePlateStyleSetting` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX12.0.0
           There is no replacement for this function
        
        License requirements: None.
        """
        ...
    
    
    def GetScatterStyleSetting(self, styleIndex: int) -> ScatterStyleSetting:
        """
        Gets the scatter display style.  
        
        The style index must be greater than or equal to 0 and
        less than :py:meth:`CAE.Xyplot.DiagramDisplayStyles.StyleCount`.  
        
        Signature ``GetScatterStyleSetting(styleIndex)`` 
        
        :param styleIndex:  Style index  
        :type styleIndex: int 
        :returns:  Scatter style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.ScatterStyleSetting` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSurfaceStyleSetting(self, styleIndex: int) -> SurfaceStyleSetting:
        """
        Gets the surface display style.  
        
        The style index must be greater than or equal to 0 and
        less than :py:meth:`CAE.Xyplot.DiagramDisplayStyles.StyleCount`.  
        
        Signature ``GetSurfaceStyleSetting(styleIndex)`` 
        
        :param styleIndex:  Style index  
        :type styleIndex: int 
        :returns:  Surface style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.SurfaceStyleSetting` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetVectorStyleSetting(self, styleIndex: int) -> VectorStyle2DSetting:
        """
        Gets the vector display style.  
        
        The style index must be greater than or equal to 0 and
        less than :py:meth:`CAE.Xyplot.DiagramDisplayStyles.StyleCount`.  
        
        Signature ``GetVectorStyleSetting(styleIndex)`` 
        
        :param styleIndex:  Style index  
        :type styleIndex: int 
        :returns:  Line style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.VectorStyle2DSetting` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    StyleCount: int = ...
    """
    Returns  the style count 
    
    <hr>
    
    Getter Method
    
    Signature ``StyleCount`` 
    
    :returns:  Style count  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: DiagramDisplayStyles = ...  # unknown typename


class Plot(BaseModel):
    """
    Manages the plot template   
    
    Not support KF.
    
    .. versionadded:: NX7.5.0
    """
    
    def GetRecordCount(self) -> int:
        """
        Returns the count of plotted records on the plot graph.  
        
        Signature ``GetRecordCount()`` 
        
        :returns:  Record count  
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetApplicationDataOfRecord(self, recordIndex: int) -> NXOpen.CAE.FTK.IApplicationData:
        """
        Returns application specific data associated to a record.  
        
        Signature ``GetApplicationDataOfRecord(recordIndex)`` 
        
        :param recordIndex:  The record index starts form 0 to record count -1. Get record count from :py:meth:`Plot.GetRecordCount`  
        :type recordIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.FTK.IApplicationData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveRecords(self, recordIndexes: 'list[int]', recordNames: 'list[str]', outputFileName: str, reportError: bool) -> None:
        """
        Saves plotted records on a graph to an afu file.  
        
        The record index is between 0 and the value returned from
        :py:meth:`NXOpen.CAE.Xyplot.Plot.GetRecordCount`. 
        
        Signature ``SaveRecords(recordIndexes, recordNames, outputFileName, reportError)`` 
        
        :param recordIndexes:  The index of records to be saved  
        :type recordIndexes: list of int 
        :param recordNames:  The output record names  
        :type recordNames: list of str 
        :param outputFileName:  The destination file with full file name.                                                                        The file suffix must be ".afu".  
        :type outputFileName: str 
        :param reportError: 
        :type reportError: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDeviceAndViewIndex(self) -> tuple:
        """
        Gets the window device and view index of the plot graph.  
        
        Signature ``GetDeviceAndViewIndex()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (windowDevice, viewIndex). windowDevice is a int.   the device of window viewIndex is a int.   the index of view 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetGraphs(self) -> 'list[Graph]':
        """
        Gets all graphs on the plot.  
        
        Signature ``GetGraphs()`` 
        
        :returns:  Graph objects  
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.Graph` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FitAxisLimit(self) -> None:
        """
        Update axis limits for an overlaying plot if current displayed axis limits in plot do not fit for all records.  
        
        Signature ``FitAxisLimit()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveRecordsToCsv(self, recordIndex: 'list[int]', recordNames: 'list[str]', csvFileName: str, isWriteHeader: bool) -> None:
        """
        Saves plotted records on a plot graph to a CSV file.  
        
        Signature ``SaveRecordsToCsv(recordIndex, recordNames, csvFileName, isWriteHeader)`` 
        
        :param recordIndex:  the indexes of records to be saved  
        :type recordIndex: list of int 
        :param recordNames: 
        :type recordNames: list of str 
        :param csvFileName:  the destination CSV file name  
        :type csvFileName: str 
        :param isWriteHeader: 
        :type isWriteHeader: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateNote(self, lines: 'list[str]', textPosition: NXOpen.Point2d) -> NoteModel:
        """
        Creates a note on the plot  
        
        Signature ``CreateNote(lines, textPosition)`` 
        
        :param lines: 
        :type lines: list of str 
        :param textPosition: 
        :type textPosition: :py:class:`NXOpen.Point2d` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Xyplot.NoteModel` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNotes(self) -> 'list[NoteModel]':
        """
        Gets all notes on the plot  
        
        Signature ``GetNotes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.NoteModel` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTitles(self) -> 'list[BasicModel]':
        """
        Gets the titles on the plot.  
        
        Signature ``GetTitles()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.BasicModel` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetViewBoundingBox(self) -> tuple:
        """
        Gets the bounding box of the plot view.  
        
        Signature ``GetViewBoundingBox()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (leftBottom, rightTop). leftBottom is a :py:class:`NXOpen.Point3d`. rightTop is a :py:class:`NXOpen.Point3d`. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def WriteToTemplateFile(self, inputTemplateFile: str) -> str:
        """
        Writes the template setting of plot to template file. 
        
          #. 
        If input file is a simple file: 
        
        If environment variable of UGII_USER_DIR is not set, it will be written into file under user environment directory. 
        
        If environment variable of UGII_USER_DIR is not set, it will write to write the template setting.
        
          #. 
        If input file is a file with full path, the template settings will be written into the file.
        
        Signature ``WriteToTemplateFile(inputTemplateFile)`` 
        
        :param inputTemplateFile:  simple name or file name with full path  
        :type inputTemplateFile: str 
        :returns:  the file name with full path  
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRecordDisplayVisibility(self, recordIndex: int) -> bool:
        """
        Gets the visibility of specified record.  
        
        Signature ``GetRecordDisplayVisibility(recordIndex)`` 
        
        :param recordIndex:  the index of specied record  
        :type recordIndex: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRecordDisplayVisibility(self, recordIndex: int, visibility: bool) -> None:
        """
        Sets the visibility of specified record.  
        
        Signature ``SetRecordDisplayVisibility(recordIndex, visibility)`` 
        
        :param recordIndex:  the index of specied record  
        :type recordIndex: int 
        :param visibility: 
        :type visibility: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetModels(self, type: ModelType) -> 'list[BasicModel]':
        """
        Gets the models by model type.  
        
        Signature ``GetModels(type)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.CAE.Xyplot.ModelType` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.BasicModel` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FitView(self) -> None:
        """
        Fits the display view on a reasonable region. 
        
        Signature ``FitView()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteRecord(self, recordIndex: int) -> None:
        """
        Deletes the nth record. 
        
        The record index must be greater or equal to 0, and less than :py:meth:`CAE.Xyplot.Plot.GetRecordCount`
        
        ** Procedure of deleting records from plot fully:</b>
        
          #. Call this method to delete record data from plot
          #. Call :py:meth:`CAE.Xyplot.Plot.CommitRecordsChange` to precess record data change and update data model
          #. Call :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` to regenerate display to reflect data change
          #. Optionally call :py:meth:`CAE.Xyplot.Plot.FitView` to make display fit the view;it is only required when the plot display boundary is changed
        
        Signature ``DeleteRecord(recordIndex)`` 
        
        :param recordIndex: 
        :type recordIndex: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CommitRecordsChange(self) -> None:
        """
        Accepts record changed and process data to update data model 
        
        This method is only to update data model, it needs call :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` to update display to reflect data change.
        
        Signature ``CommitRecordsChange()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLegendTables(self) -> 'list[LegendTable]':
        """
        Gets the legend table models on the plot.  
        
        Signature ``GetLegendTables()`` 
        
        :returns:  Legend Table Objects  
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.LegendTable` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Find(self, journalIdentifier: str) -> NXOpen.TaggedObject:
        """
        Finds the :py:class:`NXObject` with the given identifier as recorded in a journal. 
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``Find(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier of the object  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX12.0.0
           Use :py:meth:`NXOpen.INXObject.FindObject`
        
        License requirements: None.
        """
        ...
    
    PlotTemplate: PlotGraphTemplate = ...
    """
    Returns  the plot template 
    
    <hr>
    
    Getter Method
    
    Signature ``PlotTemplate`` 
    
    :returns:  Plot template  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.PlotGraphTemplate` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    SubGraphCountInStack: int = ...
    """
    Returns  the sub-graph count in a stacked plot.  
    
    <hr>
    
    Getter Method
    
    Signature ``SubGraphCountInStack`` 
    
    :returns:  Sub-graph count  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: Plot = ...  # unknown typename


class I3DDataPlot():
    """
    Represents a plot interface which input is 3D data 
    
    .
    <remarker>
    3D plot data can consist of multiple :py:class:`CAE.FTK.ArrayRecord2D` or a :py:class:`CAE.FTK.SectionBasedMatrixRecord`
    To the plot class which implements this interface, all input records will be represented as a whole data.
    </remarker>
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ColorMapPlot(Plot, I3DDataPlot):
    """
    Manages the display of color map plot. 
    
    Call :py:meth:`CAE.Xyplot.I3DDataPlot.EditRecords` to edit data for this class.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def EditRecords(self, records: 'list[NXOpen.CAE.FTK.BaseRecord]') -> None:
        """
        Edits records of plot.  
        
        ** Procedure of editing records of plot fully:</b>
        
          #. Call this method to edit record data
          #. Call :py:meth:`CAE.Xyplot.Plot.CommitRecordsChange` to precess record data change and update data model
          #. Call :py:meth:`CAE.Xyplot.IDisplayableModel.UpdateDisplay` to regenerate display to reflect data change
          #. Optionally call :py:meth:`CAE.Xyplot.Plot.FitView` to make display fit the view;it is only required when the plot display boundary is changed
        
        Signature ``EditRecords(records)`` 
        
        :param records: 
        :type records: list of :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ColorMapPlot = ...  # unknown typename


class TextBoxMarginOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TextBoxMarginOption():
    """
    Represents the margin position in a text box 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "The left margin of text box"
       "Top", "The top margin of text box"
       "Right", "The right margin of text box"
       "Bottom", "The bottom margin of text box"
    """
    Left = 0  # TextBoxMarginOptionMemberType
    Top = 1  # TextBoxMarginOptionMemberType
    Right = 2  # TextBoxMarginOptionMemberType
    Bottom = 3  # TextBoxMarginOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AngleAxisStyleSetting(BaseDisplayStyleSetting, IVisibleDisplayStyle):
    """
    Represents the angle axis display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    AngleUnit: AngleUnit = ...
    """
    Returns or sets  the angle axis number unit 
    
    <hr>
    
    Getter Method
    
    Signature ``AngleUnit`` 
    
    :returns:  Angle unit  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.AngleUnit` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AngleUnit`` 
    
    :param unit:  Angle unit  
    :type unit: :py:class:`NXOpen.CAE.Xyplot.AngleUnit` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LineDisplaySettings: CurveDisplaySettings = ...
    """
    Returns  the angle axis lines display styles 
    
    <hr>
    
    Getter Method
    
    Signature ``LineDisplaySettings`` 
    
    :returns:  Angle axis lines display styles  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param visibility: 
    :type visibility: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: AngleAxisStyleSetting = ...  # unknown typename


class AxisTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AxisType():
    """
    Represents the type of scale for X or Y axis 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Auto", "Automatic type"
       "Linear", "Linear type"
       "Log", "Log type"
       "Db", "Db type"
       "Octave", "Octave type"
       "OneThirdOctave", "1/3 Octave type"
       "OneTwelfthOctave", "1/12 Octave type"
    """
    Auto = 0  # AxisTypeMemberType
    Linear = 1  # AxisTypeMemberType
    Log = 2  # AxisTypeMemberType
    Db = 3  # AxisTypeMemberType
    Octave = 4  # AxisTypeMemberType
    OneThirdOctave = 5  # AxisTypeMemberType
    OneTwelfthOctave = 6  # AxisTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AxisItemStyle(TextStyleSetting):
    """
    Represents the axis item display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    MaximumCharacterCount: int = ...
    """
    Returns or sets  the maximum character count.  
    
    The minimum value is 1. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumCharacterCount`` 
    
    :returns:  maximum character count  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumCharacterCount`` 
    
    :param maximumCharacterCount:  maximum character count  
    :type maximumCharacterCount: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: AxisItemStyle = ...  # unknown typename


class AngleUnitMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AngleUnit():
    """
    Represents the angle axis display value unit 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Degree", "Display angle in degree unit"
       "Radian", "Display angle in radian unit"
       "Rev", "Display angle in rev unit"
    """
    Degree = 0  # AngleUnitMemberType
    Radian = 1  # AngleUnitMemberType
    Rev = 2  # AngleUnitMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GeneralDisplayStyles(BaseDisplayStyleSetting):
    """
    Manages the general display styles.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    PhaseAngle: float = ...
    """
    Returns or sets  the phase angle in degree 
    
    <hr>
    
    Getter Method
    
    Signature ``PhaseAngle`` 
    
    :returns:  Phase angle  
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PhaseAngle`` 
    
    :param phaseAngle:  Phase angle  
    :type phaseAngle: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    PhaseRangeOption: PhaseRangeOption = ...
    """
    Returns or sets  the phase range option 
    
    <hr>
    
    Getter Method
    
    Signature ``PhaseRangeOption`` 
    
    :returns:  Phase range option  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.PhaseRangeOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PhaseRangeOption`` 
    
    :param phaseRangeOption:  Phase range option  
    :type phaseRangeOption: :py:class:`NXOpen.CAE.Xyplot.PhaseRangeOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: GeneralDisplayStyles = ...  # unknown typename


class GeneralDisplayStyles2D(GeneralDisplayStyles):
    """
    Manages the general display styles for 2D plot.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def SwitchXYAxis(self) -> None:
        """
        Switches the X/Y axis 
        
        Signature ``SwitchXYAxis()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    ComplexOption: ComplexOption2D = ...
    """
    Returns or sets  the complex option 
    
    <hr>
    
    Getter Method
    
    Signature ``ComplexOption`` 
    
    :returns:  Complex option  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.ComplexOption2D` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComplexOption`` 
    
    :param complexOption:  Complex option  
    :type complexOption: :py:class:`NXOpen.CAE.Xyplot.ComplexOption2D` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ShowOrderedAbscissa: bool = ...
    """
    Returns or sets  a value indicating whether to show the data by ordered abscissa or not 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOrderedAbscissa`` 
    
    :returns:  Show ordered abscissa or not  
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOrderedAbscissa`` 
    
    :param ordered:  Show ordered abscissa or not  
    :type ordered: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: GeneralDisplayStyles2D = ...  # unknown typename


class PlotTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PlotType():
    """
    Represents the plot type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Plot2D", "2D plot"
       "Plot2DInStack", "2D plot in stacked sequence"
       "Plot3D", "3D plot"
       "PlotColorBar", "ColorBar plot"
       "PlotColorMap", "ColorMap plot"
       "PlotBarChart", "BarChart plot"
    """
    Plot2D = 0  # PlotTypeMemberType
    Plot2DInStack = 1  # PlotTypeMemberType
    Plot3D = 2  # PlotTypeMemberType
    PlotColorBar = 3  # PlotTypeMemberType
    PlotColorMap = 4  # PlotTypeMemberType
    PlotBarChart = 5  # PlotTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DiagramDisplayStyles2D(DiagramDisplayStyles):
    """
    Manages the display styles for 2D diagram.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetGraphOptionsStyle(self, styleIndex: int) -> GraphOptionsStyle2D:
        """
        Gets the nth graph options display style.  
        
        The style index must be greater than or equal to 0 and
        less than :py:meth:`CAE.Xyplot.DiagramDisplayStyles.StyleCount`.  
        
        Signature ``GetGraphOptionsStyle(styleIndex)`` 
        
        :param styleIndex: 
        :type styleIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Xyplot.GraphOptionsStyle2D` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: DiagramDisplayStyles2D = ...  # unknown typename


class BasePlotParameters(NXOpen.TransientObject):
    """
    Represents the parameters passed to create or modify a plot.  
    
    This is an abstract class
    
    .. versionadded:: NX9.0.0
    """
    
    def GetRecords(self) -> 'list[NXOpen.CAE.FTK.BaseRecord]':
        """
        Gets the records to be plotted  
        
        Signature ``GetRecords()`` 
        
        :returns:  Records  
        :rtype: list of :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRecords(self, records: 'list[NXOpen.CAE.FTK.BaseRecord]') -> None:
        """
        Sets the records to be plotted 
        
        Signature ``SetRecords(records)`` 
        
        :param records:  Records  
        :type records: list of :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Destroys the object 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    DeviceIndex: int = ...
    """
    Returns or sets  the index of device on which plot graph will be shown.  
    
    A value of 1 represents the main graphic window,
    a value greater than 2 represents separate graphic window. 
    
    <hr>
    
    Getter Method
    
    Signature ``DeviceIndex`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DeviceIndex`` 
    
    :param deviceIndex: 
    :type deviceIndex: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ViewPortIndex: int = ...
    """
    Returns or sets  the index of a view port on main graphic window, on which plot graph will be shown.  
    
    Only available when :py:meth:`CAE.Xyplot.BasePlotParameters.DeviceIndex`` is 1. 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewPortIndex`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ViewPortIndex`` 
    
    :param viewIndex: 
    :type viewIndex: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """


class BasePlateStyleSetting(BaseSymbolStyleSetting):
    """
    Represents the base plate display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       There is no replacement for this class.
    """
    FillingColor: NXOpen.NXColor = ...
    """
    Returns or sets  the filling color 
    
    <hr>
    
    Getter Method
    
    Signature ``FillingColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FillingColor`` 
    
    :param fillingColor: 
    :type fillingColor: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    OutlineColor: NXOpen.NXColor = ...
    """
    Returns or sets  the outline color 
    
    <hr>
    
    Getter Method
    
    Signature ``OutlineColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutlineColor`` 
    
    :param outlineColor: 
    :type outlineColor: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowOutline: bool = ...
    """
    Returns or sets  a value indicating whether to display the outline 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOutline`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOutline`` 
    
    :param showOutline: 
    :type showOutline: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: BasePlateStyleSetting = ...  # unknown typename


class PlateStyle2DSetting(BasePlateStyleSetting):
    """
    Represents the 2d plate display style.  
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       There is no replacement for this class.
    """
    Null: PlateStyle2DSetting = ...  # unknown typename


class AxisModel(BasicModel):
    """
    Represents an axis model object on a XY graphing.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetDisplayLimits(self) -> tuple:
        """
        Gets the display limit values in display unit 
        
        Signature ``GetDisplayLimits()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (startDisplayLimit, endDisplayLimit). startDisplayLimit is a float. endDisplayLimit is a float. 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CalculateZoomScale(self, newStartDisplayLimit: float, newEndDisplayLimit: float) -> tuple:
        """
        Gives expected display limits to calculate a zoom scale range which could be used by :py:class:`CAE.Xyplot.Graph` for zooming operation.  
        
        the new display limits must be less than the original display limits returned by :py:meth:`CAE.Xyplot.AxisModel.GetDisplayLimits`
        
        Signature ``CalculateZoomScale(newStartDisplayLimit, newEndDisplayLimit)`` 
        
        :param newStartDisplayLimit: 
        :type newStartDisplayLimit: float 
        :param newEndDisplayLimit: 
        :type newEndDisplayLimit: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (startScale, endScale). startScale is a float. endScale is a float. 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: AxisModel = ...  # unknown typename


class BaseBarStyleSetting(BaseSymbolStyleSetting):
    """
    Represents the base bar display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    FillingColor: NXOpen.NXColor = ...
    """
    Returns or sets  the filling color 
    
    <hr>
    
    Getter Method
    
    Signature ``FillingColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FillingColor`` 
    
    :param fillingColor: 
    :type fillingColor: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    OutlineColor: NXOpen.NXColor = ...
    """
    Returns or sets  the outline color 
    
    <hr>
    
    Getter Method
    
    Signature ``OutlineColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutlineColor`` 
    
    :param outlineColor: 
    :type outlineColor: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowOutline: bool = ...
    """
    Returns or sets  a value indicating whether to display the outline 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOutline`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOutline`` 
    
    :param showOutline: 
    :type showOutline: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Width: int = ...
    """
    Returns or sets  the bar width.  
    
    The range is from 0 to 100. 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param barWidth: 
    :type barWidth: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: BaseBarStyleSetting = ...  # unknown typename


class BarStyle2DSetting(BaseBarStyleSetting):
    """
    Represents the 2d bar display style.  
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    Null: BarStyle2DSetting = ...  # unknown typename


class LegendTable(BaseModel):
    """
    Manages the legend table.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetFreeTextOfLegendItem(self, dataIndex: int) -> str:
        """
        Gets the free text of legend table item  
        
        Signature ``GetFreeTextOfLegendItem(dataIndex)`` 
        
        :param dataIndex: the index of record index 
        :type dataIndex: int 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFreeTextOfLegendItem(self, dataIndex: int, freeText: str) -> None:
        """
        Sets the free text of legend table item 
        
        Signature ``SetFreeTextOfLegendItem(dataIndex, freeText)`` 
        
        :param dataIndex: the index of record index 
        :type dataIndex: int 
        :param freeText: 
        :type freeText: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetFreeTextOfLegendItem(self, dataIndex: int) -> None:
        """
        Resets the free text of legend table item 
        
        Signature ``ResetFreeTextOfLegendItem(dataIndex)`` 
        
        :param dataIndex: the index of record index 
        :type dataIndex: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    LegendTableStyle: LegendTableStyle = ...
    """
    Returns  the legend table style 
    
    <hr>
    
    Getter Method
    
    Signature ``LegendTableStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.LegendTableStyle` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: LegendTable = ...  # unknown typename


class I2DDataPlot():
    """
    Represents a plot interface which input should be a series of 2D data  
    
    .
    <remarker>
    This interface is suitable for those plots which own a series of 2d data, and each data can be drawn,edited and deleted independently;
    </remarker>
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class Plot2D(Plot, I2DDataPlot):
    """
    Manages the display of 2D plot. 
    
    Call :py:meth:`CAE.Xyplot.I2DDataPlot.EditRecord` to edit data for this class.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def EditRecord(self, nthRecordIdx: int, record: NXOpen.CAE.FTK.BaseRecord) -> None:
        """
        Edits nth record of plot.  
        
        ** Procedure of editing records of plot fully:</b>
        
          #. Call this method to edit record data
          #. Call :py:meth:`CAE.Xyplot.Plot.CommitRecordsChange` to precess record data change and update data model
          #. Call :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` to regenerate display to reflect data change
          #. Optionally call :py:meth:`CAE.Xyplot.Plot.FitView` to make display fit the view;it is only required when the plot display boundary is changed
        
        Signature ``EditRecord(nthRecordIdx, record)`` 
        
        :param nthRecordIdx: 
        :type nthRecordIdx: int 
        :param record: 
        :type record: :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Plot2D = ...  # unknown typename


class LineStyle2DSetting(BaseLineStyleSetting):
    """
    Represents the 2d line display style.  
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    Null: LineStyle2DSetting = ...  # unknown typename


class BaseGridLayoutStyleSetting(BaseDisplayStyleSetting):
    """
    Represents the base grid layout display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    BackgroundColor: NXOpen.NXColor = ...
    """
    Returns or sets  the background color 
    
    <hr>
    
    Getter Method
    
    Signature ``BackgroundColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BackgroundColor`` 
    
    :param bgColor: 
    :type bgColor: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ColorOfBackgroundPlane: NXOpen.NXColor = ...
    """
    Returns or sets  the color of grid background plane
    
    <hr>
    
    Getter Method
    
    Signature ``ColorOfBackgroundPlane`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColorOfBackgroundPlane`` 
    
    :param bgColor: 
    :type bgColor: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ContouringLevel: int = ...
    """
    Returns or sets  the contouring level.  
    
    The value is greater than 0. 
    
    <hr>
    
    Getter Method
    
    Signature ``ContouringLevel`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContouringLevel`` 
    
    :param contouringLevel: 
    :type contouringLevel: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ContouringRange: ContouringRange = ...
    """
    Returns or sets  the option to show contour range either on the border or the faces of the grid.  
    
    <hr>
    
    Getter Method
    
    Signature ``ContouringRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.ContouringRange` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContouringRange`` 
    
    :param contouringRange: 
    :type contouringRange: :py:class:`NXOpen.CAE.Xyplot.ContouringRange` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    DenseColor: NXOpen.NXColor = ...
    """
    Returns or sets  the grid dense line color 
    
    <hr>
    
    Getter Method
    
    Signature ``DenseColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.CurveDisplaySettings.Color` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DenseColor`` 
    
    :param color: 
    :type color: Id 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.CurveDisplaySettings.SetColor` instead.
    
    License requirements: None.
    """
    DenseGridDisplayStyleSettings: CurveDisplaySettings = ...
    """
    Returns  the dense grid display style 
    
    <hr>
    
    Getter Method
    
    Signature ``DenseGridDisplayStyleSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DisplayContouring: bool = ...
    """
    Returns or sets  a value indicating whether to display contouring 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayContouring`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayContouring`` 
    
    :param dispContouring: 
    :type dispContouring: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    GridColor: NXOpen.NXColor = ...
    """
    Returns or sets  the grid line color 
    
    <hr>
    
    Getter Method
    
    Signature ``GridColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.CurveDisplaySettings.Color` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GridColor`` 
    
    :param color: 
    :type color: Id 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.CurveDisplaySettings.SetColor` instead.
    
    License requirements: None.
    """
    GridFont: NXOpen.DisplayableObjectObjectFont = ...
    """
    Returns or sets  the grid line font 
    
    <hr>
    
    Getter Method
    
    Signature ``GridFont`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.CurveDisplaySettings.Font` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GridFont`` 
    
    :param gridFont: 
    :type gridFont: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.CurveDisplaySettings.SetFont` instead.
    
    License requirements: None.
    """
    GridWidth: NXOpen.DisplayableObjectObjectWidth = ...
    """
    Returns or sets  the grid line width 
    
    <hr>
    
    Getter Method
    
    Signature ``GridWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.CurveDisplaySettings.Width` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GridWidth`` 
    
    :param gridWidth: 
    :type gridWidth: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.CurveDisplaySettings.SetWidth` instead.
    
    License requirements: None.
    """
    MajorGridDisplayStyleSettings: CurveDisplaySettings = ...
    """
    Returns  the major grid display style 
    
    <hr>
    
    Getter Method
    
    Signature ``MajorGridDisplayStyleSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowBackground: bool = ...
    """
    Returns or sets  a value indicating whether to display the background 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowBackground`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowBackground`` 
    
    :param showBg: 
    :type showBg: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowBackgroundPlane: bool = ...
    """
    Returns or sets  a value indicating whether to display the grid background plane 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowBackgroundPlane`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowBackgroundPlane`` 
    
    :param showBg: 
    :type showBg: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    TicksDisplayStyleSettings: CurveDisplaySettings = ...
    """
    Returns  the ticks display style 
    
    <hr>
    
    Getter Method
    
    Signature ``TicksDisplayStyleSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    XyGridStyle: GridStyle = ...
    """
    Returns or sets  the grid style of XY plane 
    
    <hr>
    
    Getter Method
    
    Signature ``XyGridStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.GridStyle` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XyGridStyle`` 
    
    :param gridStyle: 
    :type gridStyle: :py:class:`NXOpen.CAE.Xyplot.GridStyle` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: BaseGridLayoutStyleSetting = ...  # unknown typename


class TextOrientationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TextOrientation():
    """
    Represents the text orientation 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Horizontal", "Horizontal text orientation"
       "Upward", "Upward text orientation"
       "Downward", "Downward text orientation"
    """
    Horizontal = 0  # TextOrientationMemberType
    Upward = 1  # TextOrientationMemberType
    Downward = 2  # TextOrientationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TextTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TextType():
    """
    Represents the label text type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Not defined type"
       "Title", "Title label"
       "Legend", "Legend label"
       "GraphName", "Graph name label"
       "PageNumber", "Page number label"
       "Marker", "Marker label"
       "Note", "Note label"
       "ProbingText", "Probing label"
       "XLabel", "X Axis name label"
       "YLabel", "Y Axis name label"
       "ZLabel", "Z Axis name label"
       "XNumber", "X Axis number label"
       "YNumber", "Y Axis number label"
       "ZNumber", "Z Axis number label"
       "ColorAxisLabel", "Color Axis name label"
       "ColorAxisNumber", "Color Axis name number"
       "UnknownResultText", "Unknown result text"
       "AngleAxisNumber", "Angle Axis name number"
       "AnnotationText", "Annotation text in vector plot"
       "ArgumentAxisNumber", "Argument Axis number label"
       "BarChartValueText", "Bar Chart Value text"
       "LegendTableText", "Legend Table text"
    """
    NotSet = 0  # TextTypeMemberType
    Title = 1  # TextTypeMemberType
    Legend = 2  # TextTypeMemberType
    GraphName = 3  # TextTypeMemberType
    PageNumber = 4  # TextTypeMemberType
    Marker = 5  # TextTypeMemberType
    Note = 6  # TextTypeMemberType
    ProbingText = 7  # TextTypeMemberType
    XLabel = 8  # TextTypeMemberType
    YLabel = 9  # TextTypeMemberType
    ZLabel = 10  # TextTypeMemberType
    XNumber = 11  # TextTypeMemberType
    YNumber = 12  # TextTypeMemberType
    ZNumber = 13  # TextTypeMemberType
    ColorAxisLabel = 14  # TextTypeMemberType
    ColorAxisNumber = 15  # TextTypeMemberType
    UnknownResultText = 16  # TextTypeMemberType
    AngleAxisNumber = 17  # TextTypeMemberType
    AnnotationText = 18  # TextTypeMemberType
    ArgumentAxisNumber = 19  # TextTypeMemberType
    BarChartValueText = 20  # TextTypeMemberType
    LegendTableText = 21  # TextTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UnknownResultScaleStyle(BaseDisplayStyleSetting, IVisibleDisplayStyle):
    """
    Represents the axis display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    Color: UnknownResultColor = ...
    """
    Returns or sets  the unknown result color 
    
    <hr>
    
    Getter Method
    
    Signature ``Color`` 
    
    :returns:  UnKnown result color  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.UnknownResultColor` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Color`` 
    
    :param unknownResultColor:  UnKnown result color  
    :type unknownResultColor: :py:class:`NXOpen.CAE.Xyplot.UnknownResultColor` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param visibility: 
    :type visibility: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: UnknownResultScaleStyle = ...  # unknown typename


class SurfaceStyleSetting(BaseSymbolStyleSetting):
    """
    Represents the surface display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    ColorOption: SurfaceColorOption = ...
    """
    Returns or sets  the color option 
    
    <hr>
    
    Getter Method
    
    Signature ``ColorOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.SurfaceColorOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColorOption`` 
    
    :param colorOption: 
    :type colorOption: :py:class:`NXOpen.CAE.Xyplot.SurfaceColorOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FillingColor: NXOpen.NXColor = ...
    """
    Returns or sets  the filling color 
    
    <hr>
    
    Getter Method
    
    Signature ``FillingColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FillingColor`` 
    
    :param fillingColor: 
    :type fillingColor: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    OutlineColor: NXOpen.NXColor = ...
    """
    Returns or sets  the outline color 
    
    <hr>
    
    Getter Method
    
    Signature ``OutlineColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutlineColor`` 
    
    :param outlineColor: 
    :type outlineColor: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowOutline: bool = ...
    """
    Returns or sets  a value indicating whether to display the outline 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOutline`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       There is no replacement for this function.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOutline`` 
    
    :param showOutline: 
    :type showOutline: bool 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       There is no replacement for this function.
    
    License requirements: None.
    """
    Null: SurfaceStyleSetting = ...  # unknown typename


class ContouringRangeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ContouringRange():
    """
    Represents the contouring range 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BorderGrid", "Option to show contour range on the border of the grid"
       "FullGrid", "Option to show contour range on the face of the grid"
    """
    BorderGrid = 0  # ContouringRangeMemberType
    FullGrid = 1  # ContouringRangeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GraphStyleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GraphStyle():
    """
    Represents the plot graph style 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Line", "Option to display plot in curve style"
       "Bar", "Option to display plot in bar style"
       "Plate", "Deprecated in NX12.0"
       "Surface", "Option to display plot in surface style"
       "Scatter", "Option to display plot in scatter style"
       "ColorBar", "Option to display plot in ColorBar style"
       "ColorMap", "Option to display plot in ColorMap style"
       "BarChart", "Option to display plot in BarChart style"
       "Vector", "Option to display plot in vector style"
    """
    Line = 0  # GraphStyleMemberType
    Bar = 1  # GraphStyleMemberType
    Plate = 2  # GraphStyleMemberType
    Surface = 3  # GraphStyleMemberType
    Scatter = 4  # GraphStyleMemberType
    ColorBar = 5  # GraphStyleMemberType
    ColorMap = 6  # GraphStyleMemberType
    BarChart = 7  # GraphStyleMemberType
    Vector = 8  # GraphStyleMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FrequencyBandSummationBandTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FrequencyBandSummationBandType():
    """
    Represents the frequency band summation band type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Octave", "Octave"
       "OneThirdOctave", "1/3 Octave"
       "OneTwelfthOctave", "1/12 Octave"
    """
    Octave = 0  # FrequencyBandSummationBandTypeMemberType
    OneThirdOctave = 1  # FrequencyBandSummationBandTypeMemberType
    OneTwelfthOctave = 2  # FrequencyBandSummationBandTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LegendTablePositionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LegendTablePositionType():
    """
    Represents the legend table position type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Floating", "The position of legend table can be dragged"
       "Docked", "The position of legend table is fixed"
    """
    Floating = 0  # LegendTablePositionTypeMemberType
    Docked = 1  # LegendTablePositionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GeneralDisplayStyles3D(GeneralDisplayStyles):
    """
    Manages the general display styles for 3D plot.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    ComplexOption: ComplexOption3D = ...
    """
    Returns or sets  the complex option 
    
    <hr>
    
    Getter Method
    
    Signature ``ComplexOption`` 
    
    :returns:  Complex option  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.ComplexOption3D` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComplexOption`` 
    
    :param complexOption:  Complex option  
    :type complexOption: :py:class:`NXOpen.CAE.Xyplot.ComplexOption3D` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: GeneralDisplayStyles3D = ...  # unknown typename


class AxisYStyleSetting(AxisStyleSetting):
    """
    Represents the axis y display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    BarLowerLimit: bool = ...
    """
    Returns or sets  the bar lower limit indicating whether a bar is plotted from minimum or zero position of axis y 
    
    <hr>
    
    Getter Method
    
    Signature ``BarLowerLimit`` 
    
    :returns:  Bar Lower Limit  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BarLowerLimit`` 
    
    :param barLowerLimit:  Bar Lower Limit  
    :type barLowerLimit: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: AxisYStyleSetting = ...  # unknown typename


class TextBoxStyleSetting(BaseDisplayStyleSetting):
    """
    Represents the text box display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    
    def GetLineStyle(self) -> CurveDisplaySettings:
        """
        Gets the text box line style 
        
        Signature ``GetLineStyle()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetMargin(self, marginOption: TextBoxMarginOption) -> float:
        """
        Gets the margin value of text box  
        
        Signature ``GetMargin(marginOption)`` 
        
        :param marginOption: margin option 
        :type marginOption: :py:class:`NXOpen.CAE.Xyplot.TextBoxMarginOption` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMargin(self, marginOption: TextBoxMarginOption, marginValue: float) -> None:
        """
        Sets the margin value of text box 
        
        Signature ``SetMargin(marginOption, marginValue)`` 
        
        :param marginOption: margin option 
        :type marginOption: :py:class:`NXOpen.CAE.Xyplot.TextBoxMarginOption` 
        :param marginValue: 
        :type marginValue: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Color: NXOpen.NXColor = ...
    """
    Returns or sets  the text box outline color
    
    <hr>
    
    Getter Method
    
    Signature ``Color`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Color`` 
    
    :param color: 
    :type color: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FillingColor: NXOpen.NXColor = ...
    """
    Returns or sets  the text box filling color
    
    <hr>
    
    Getter Method
    
    Signature ``FillingColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FillingColor`` 
    
    :param fillingColor: 
    :type fillingColor: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    IsFilled: bool = ...
    """
    Returns or sets  a value indicating whether to fill the text box 
    
    <hr>
    
    Getter Method
    
    Signature ``IsFilled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsFilled`` 
    
    :param isFilled: 
    :type isFilled: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  a value indicating whether to display the text box 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param visibility: 
    :type visibility: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: TextBoxStyleSetting = ...  # unknown typename


class PointMarkerMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PointMarker():
    """
    Represents the point marker 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No marker"
       "Plus", "Plus marker"
       "Dot", "Dot marker"
       "Asterisk", "Asterisk marker"
       "Circle", "Circle marker"
       "Poundsign", "Pound sign marker"
       "Cross", "Cross marker"
       "Square", "Square marker"
       "Triangle", "Triangle marker"
       "Diamond", "Diamond marker"
       "CenterLine", "Center line marker"
    """
    NotSet = 0  # PointMarkerMemberType
    Plus = 1  # PointMarkerMemberType
    Dot = 2  # PointMarkerMemberType
    Asterisk = 3  # PointMarkerMemberType
    Circle = 4  # PointMarkerMemberType
    Poundsign = 5  # PointMarkerMemberType
    Cross = 6  # PointMarkerMemberType
    Square = 7  # PointMarkerMemberType
    Triangle = 8  # PointMarkerMemberType
    Diamond = 9  # PointMarkerMemberType
    CenterLine = 10  # PointMarkerMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AxisDirectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AxisDirection():
    """
    Represents the axis direction 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", "X-axis"
       "Y", "Y-axis"
       "Z", "Z-axis"
    """
    X = 0  # AxisDirectionMemberType
    Y = 1  # AxisDirectionMemberType
    Z = 2  # AxisDirectionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BarColorOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BarColorOption():
    """
    Represents the bar filling color option 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fill", "Fill color or contour color with no shading"
       "Hidden", "Background color as fill"
       "Shaded", "Fill Color or contour color with shading"
    """
    Fill = 0  # BarColorOptionMemberType
    Hidden = 1  # BarColorOptionMemberType
    Shaded = 2  # BarColorOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UnknownResultColorMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UnknownResultColor():
    """
    Represents the color for unknow result 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "White", "white"
       "Grey", "grey"
    """
    White = 0  # UnknownResultColorMemberType
    Grey = 1  # UnknownResultColorMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BarChartPlot(Plot, I2DDataPlot):
    """
    Manages the display of bar chart plot. 
    
    Call :py:meth:`CAE.Xyplot.I2DDataPlot.EditRecord` to edit data for this class.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def EditRecord(self, nthRecordIdx: int, record: NXOpen.CAE.FTK.BaseRecord) -> None:
        """
        Edits nth record of plot.  
        
        ** Procedure of editing records of plot fully:</b>
        
          #. Call this method to edit record data
          #. Call :py:meth:`CAE.Xyplot.Plot.CommitRecordsChange` to precess record data change and update data model
          #. Call :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` to regenerate display to reflect data change
          #. Optionally call :py:meth:`CAE.Xyplot.Plot.FitView` to make display fit the view;it is only required when the plot display boundary is changed
        
        Signature ``EditRecord(nthRecordIdx, record)`` 
        
        :param nthRecordIdx: 
        :type nthRecordIdx: int 
        :param record: 
        :type record: :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: BarChartPlot = ...  # unknown typename


class WallDisplayStyles2D(WallDisplayStyles):
    """
    Manages the 2D wall display styles.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetAngleAxisStyleSetting(self) -> AngleAxisStyleSetting:
        """
        Gets the angle axis display style.  
        
        Signature ``GetAngleAxisStyleSetting()`` 
        
        :returns:  Angle Axis style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.AngleAxisStyleSetting` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: WallDisplayStyles2D = ...  # unknown typename


class Plot3D(Plot, I3DDataPlot):
    """
    Manages the display of 3D plot. 
    
    Call :py:meth:`CAE.Xyplot.I3DDataPlot.EditRecords` to edit data for this class.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def EditRecords(self, records: 'list[NXOpen.CAE.FTK.BaseRecord]') -> None:
        """
        Edits records of plot.  
        
        ** Procedure of editing records of plot fully:</b>
        
          #. Call this method to edit record data
          #. Call :py:meth:`CAE.Xyplot.Plot.CommitRecordsChange` to precess record data change and update data model
          #. Call :py:meth:`CAE.Xyplot.IDisplayableModel.UpdateDisplay` to regenerate display to reflect data change
          #. Optionally call :py:meth:`CAE.Xyplot.Plot.FitView` to make display fit the view;it is only required when the plot display boundary is changed
        
        Signature ``EditRecords(records)`` 
        
        :param records: 
        :type records: list of :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Plot3D = ...  # unknown typename


class ScatterStyleSetting(BaseSymbolStyleSetting):
    """
    Represents the scatter display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    Color: NXOpen.NXColor = ...
    """
    Returns or sets  the point color
    
    <hr>
    
    Getter Method
    
    Signature ``Color`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Color`` 
    
    :param color: 
    :type color: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: ScatterStyleSetting = ...  # unknown typename


class PlotParameters(BasePlotParameters):
    """
    Represents the parameters passed to create a plot.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Xyplot.XYPlotManager.NewPlotParameters`
    
    .. versionadded:: NX9.0.0
    """
    ComplexOption: int = ...
    """
    Returns or sets  the complex options,if complex option is smaller than zero, it will use default complex option from active template file  
    
    <hr>
    
    Getter Method
    
    Signature ``ComplexOption`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComplexOption`` 
    
    :param complexOption: 
    :type complexOption: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    IsToCreateStandalonePlot: bool = ...
    """
    Returns or sets  the create standalone plot  
    
    <hr>
    
    Getter Method
    
    Signature ``IsToCreateStandalonePlot`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsToCreateStandalonePlot`` 
    
    :param isToCreateStandalonePlot: 
    :type isToCreateStandalonePlot: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    PlotTemplate: PlotGraphTemplate = ...
    """
    Returns  the plot template to be used by the plot 
    
    <hr>
    
    Getter Method
    
    Signature ``PlotTemplate`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.PlotGraphTemplate` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    PlotType: PlotType = ...
    """
    Returns or sets  the plot type 
    
    <hr>
    
    Getter Method
    
    Signature ``PlotType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.PlotType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlotType`` 
    
    :param plotType: 
    :type plotType: :py:class:`NXOpen.CAE.Xyplot.PlotType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """


class GridStyle2DColorContour(BaseGridLayoutStyleSetting):
    """
    Manages the grid styles for colorbar and colormap plot.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    IsAutoOrderGrid: bool = ...
    """
    Returns or sets  the automatic show order grid value 
    
    <hr>
    
    Getter Method
    
    Signature ``IsAutoOrderGrid`` 
    
    :returns:  Automatic show order grid value  
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsAutoOrderGrid`` 
    
    :param isAutoOrderGrid:  Automatic show order grid value  
    :type isAutoOrderGrid: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    OrderGridCount: int = ...
    """
    Returns or sets  the count of order grid 
    
    <hr>
    
    Getter Method
    
    Signature ``OrderGridCount`` 
    
    :returns:  Count of order grid  
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OrderGridCount`` 
    
    :param orderGridCount:  Count of order grid  
    :type orderGridCount: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    OrderInterval: float = ...
    """
    Returns or sets  the interval of order line 
    
    <hr>
    
    Getter Method
    
    Signature ``OrderInterval`` 
    
    :returns:  interval of order grid  
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OrderInterval`` 
    
    :param orderInterval:  interval of order grid  
    :type orderInterval: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ShowOrderGrid: bool = ...
    """
    Returns or sets  the show order grid value 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOrderGrid`` 
    
    :returns:  Show order grid value  
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOrderGrid`` 
    
    :param isShowOrderGrid:  Show order grid value  
    :type isShowOrderGrid: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: GridStyle2DColorContour = ...  # unknown typename


class ColorMapGraph(Graph, I3DDataGraph):
    """
    Manages the display color map graph.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def CreateOrderMarker(self, orderValue: float) -> MarkerModel:
        """
        Creates the display order marker on the color map graph.  
        
        Signature ``CreateOrderMarker(orderValue)`` 
        
        :param orderValue:  Order Value  
        :type orderValue: float 
        :returns:  Marker model  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.MarkerModel` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSourcePointCount(self, recordIndex: int, sectionIndex: int) -> int:
        """
        Gets the source point count of specified record.  
        
        <remarker>
        The record index is between 0 and :py:meth:`CAE.Xyplot.Graph.RecordCount`, 0 is inclusive.
        </remarker>
        
        Signature ``GetSourcePointCount(recordIndex, sectionIndex)`` 
        
        :param recordIndex:  Record index  
        :type recordIndex: int 
        :param sectionIndex:  Section index  
        :type sectionIndex: int 
        :returns:  Point count  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateMarker(self, recordIndex: int, sectionIndex: int, pointIndex: int) -> MarkerModel:
        """
        Creates a marker in the position of a source point.  
        
        <remarker>
        The record index is between 0 and :py:meth:`CAE.Xyplot.Graph.RecordCount`, 0 is inclusive. 
        The point index is between 0 and :py:meth:`CAE.Xyplot.I3DDataGraph.GetSourcePointCount`, 0 is inclusive. 
        </remarker>
        
        Signature ``CreateMarker(recordIndex, sectionIndex, pointIndex)`` 
        
        :param recordIndex:  Record index  
        :type recordIndex: int 
        :param sectionIndex:  Section index  
        :type sectionIndex: int 
        :param pointIndex:  Point index  
        :type pointIndex: int 
        :returns:  Marker model  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.MarkerModel` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateMarker(self, recordIndex: int, sectionIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> MarkerModel:
        """
        <summary> Creates a marker in the linear interpolation position between two source points. </summary>
        <remarker>
        The record index is between 0 and :py:meth:`CAE.Xyplot.Graph.RecordCount`, 0 is inclusive. 
        The previous/next point index is between 0 and :py:meth:`CAE.Xyplot.I3DDataGraph.GetSourcePointCount`, 0 is inclusive.
        The linear interpolation scale is between 0 and 1, both 0 and 1 are inclusive. 
        </remarker>
        
        Signature ``CreateMarker(recordIndex, sectionIndex, prePointIndex, nextPointIndex, linearInterpoScale)`` 
        
        :param recordIndex:  Record index  
        :type recordIndex: int 
        :param sectionIndex:  Section index  
        :type sectionIndex: int 
        :param prePointIndex:  Previous Point index  
        :type prePointIndex: int 
        :param nextPointIndex:  Next Point index  
        :type nextPointIndex: int 
        :param linearInterpoScale:  Interpolation Scale  
        :type linearInterpoScale: float 
        :returns:  Marker model  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.MarkerModel` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ColorMapGraph = ...  # unknown typename


class GraphNamePositionOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GraphNamePositionOption():
    """
    Represents the position option of graph name 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "TopLeft", "Option to positon name on top left of grid plane"
       "TopCenter", "Option to positon name on top center of grid plane"
       "TopRight", "Option to positon name on top right of grid plane"
       "BottomLeft", "Option to positon name on bottom left of grid plane"
       "BottomCenter", "Option to positon name on bottom center of grid plane"
       "BottomRight", "Option to positon name on bottom right of grid plane"
    """
    TopLeft = 0  # GraphNamePositionOptionMemberType
    TopCenter = 1  # GraphNamePositionOptionMemberType
    TopRight = 2  # GraphNamePositionOptionMemberType
    BottomLeft = 3  # GraphNamePositionOptionMemberType
    BottomCenter = 4  # GraphNamePositionOptionMemberType
    BottomRight = 5  # GraphNamePositionOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ModelTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ModelType():
    """
    Represents the model type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Plot", " - "
       "Graph", " - "
       "RecordDisplay", " - "
       "Marker", " - "
       "Note", " - "
       "Title", " - "
       "GraphName", " - "
       "FunctionName", "the lable of a record for :py:class:`CAE.XyplotPlotType.PlotColorBar <CAE.XyplotPlotType>`"
       "XAxis", " - "
       "XAxisLabel", " - "
       "XAxisNumber", " - "
       "YAxis", " - "
       "YAxisLabel", " - "
       "YAxisNumber", " - "
       "ZAxis", " - "
       "ZAxisLabel", " - "
       "ZAxisNumber", " - "
       "ColorAxis", "the color indicator for :py:class:`CAE.XyplotPlotType.PlotColorBar <CAE.XyplotPlotType>` and :py:class:`CAE.XyplotPlotType.PlotColorMap <CAE.XyplotPlotType>`"
       "ColorAxisLabel", " - "
       "ColorAxisNumber", " - "
       "AngleAxis", "the axis to display angle divisions on circle grids"
       "AngleAxisNumber", "the angle axis number"
       "UnknownResult", "the label and color block to represent result value beyond color range on :py:class:`CAE.XyplotPlotType.PlotColorBar <CAE.XyplotPlotType>` and :py:class:`CAE.XyplotPlotType.PlotColorMap <CAE.XyplotPlotType>`"
       "PageNumber", " - "
       "Legend", " - "
       "LegendTable", " - "
    """
    Plot = 1  # ModelTypeMemberType
    Graph = 2  # ModelTypeMemberType
    RecordDisplay = 3  # ModelTypeMemberType
    Marker = 4  # ModelTypeMemberType
    Note = 5  # ModelTypeMemberType
    Title = 6  # ModelTypeMemberType
    GraphName = 7  # ModelTypeMemberType
    FunctionName = 8  # ModelTypeMemberType
    XAxis = 9  # ModelTypeMemberType
    XAxisLabel = 10  # ModelTypeMemberType
    XAxisNumber = 11  # ModelTypeMemberType
    YAxis = 12  # ModelTypeMemberType
    YAxisLabel = 13  # ModelTypeMemberType
    YAxisNumber = 14  # ModelTypeMemberType
    ZAxis = 15  # ModelTypeMemberType
    ZAxisLabel = 16  # ModelTypeMemberType
    ZAxisNumber = 17  # ModelTypeMemberType
    ColorAxis = 18  # ModelTypeMemberType
    ColorAxisLabel = 19  # ModelTypeMemberType
    ColorAxisNumber = 20  # ModelTypeMemberType
    AngleAxis = 21  # ModelTypeMemberType
    AngleAxisNumber = 22  # ModelTypeMemberType
    UnknownResult = 23  # ModelTypeMemberType
    PageNumber = 24  # ModelTypeMemberType
    Legend = 25  # ModelTypeMemberType
    LegendTable = 26  # ModelTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CoordinateTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CoordinateType():
    """
    Represents the swap axis  type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Xy", "no swap for 2d"
       "Yx", "swap x and y"
       "Xyz", "no swap for 3d"
       "Yxz", "swap x and y"
       "Zyx", "swap x and z"
       "Yzx", "swap x and y firstly and then swap y and z"
       "Xzy", "swap Z and y"
       "Zxy", "swap x and y firstly and then swap X and z"
    """
    Xy = 0  # CoordinateTypeMemberType
    Yx = 1  # CoordinateTypeMemberType
    Xyz = 2  # CoordinateTypeMemberType
    Yxz = 3  # CoordinateTypeMemberType
    Zyx = 4  # CoordinateTypeMemberType
    Yzx = 5  # CoordinateTypeMemberType
    Xzy = 6  # CoordinateTypeMemberType
    Zxy = 7  # CoordinateTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ColorScaleStyle(BaseDisplayStyleSetting):
    """
    Represents the color scale display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    AutoLevel: bool = ...
    """
    Returns or sets  the option indicates whether to define color level automatically 
    
    <hr>
    
    Getter Method
    
    Signature ``AutoLevel`` 
    
    :returns:  Auto level setting 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutoLevel`` 
    
    :param useAutoLevel:  Auto Level setting 
    :type useAutoLevel: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Level: int = ...
    """
    Returns or sets   the level setting 
    
    <hr>
    
    Getter Method
    
    Signature ``Level`` 
    
    :returns:  level setting 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Level`` 
    
    :param level:  Level setting 
    :type level: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: ColorScaleStyle = ...  # unknown typename


class WindowManager():
    """
    Manages the separate graphic windows.  
    
    The value of device index is greater than 0.
    This class is restricted to being called from a program running during an interactive NX session.
    If run from a non-interactive session it will return None. 
    To obtain an instance of this class use :py:meth:`NXOpen.CAE.Xyplot.XYPlotManager.WindowManager`.
    
    .. versionadded:: NX9.0.0
    """
    
    def NewWindow(self) -> int:
        """
        Creates a new window and returns the device index.  
        
        Signature ``NewWindow()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CloseWindow(self, deviceIndex: int) -> None:
        """
        Closes the window of specified device index.  
        
        Signature ``CloseWindow(deviceIndex)`` 
        
        :param deviceIndex: 
        :type deviceIndex: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetWindows(self) -> 'list[int]':
        """
        Gets the device indices of all the graphic windows.  
        
        Signature ``GetWindows()`` 
        
        :returns: 
        :rtype: list of int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    


class UnitSystemMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UnitSystem():
    """
    Represents the unit system   
    
    .. deprecated::  NX12.0.0
       Use :py:class:`NXOpen.CAE.XyFunctionUnitSystem`
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Function", "Function unit"
       "Model", "Model unit"
       "Si", "International standard unit"
       "Mn", "Milliforce unit"
       "Mm", "Millimeter unit"
       "In", "Inch unit"
       "Custom", "Custom unit"
    """
    Function = 0  # UnitSystemMemberType
    Model = 1  # UnitSystemMemberType
    Si = 2  # UnitSystemMemberType
    Mn = 3  # UnitSystemMemberType
    Mm = 4  # UnitSystemMemberType
    In = 5  # UnitSystemMemberType
    Custom = 6  # UnitSystemMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ICurveDisplaySettings():
    """
    Represents the interface for curve display style classes.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class CurveDisplaySettings(BaseDisplayStyleSetting, ICurveDisplaySettings):
    """
    Represents the curve display style.  
    
    Call Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    Color: NXOpen.NXColor = ...
    """
    Returns or sets  the line color 
    
    <hr>
    
    Getter Method
    
    Signature ``Color`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Color`` 
    
    :param color: 
    :type color: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Font: NXOpen.DisplayableObjectObjectFont = ...
    """
    Returns or sets  the line font 
    
    <hr>
    
    Getter Method
    
    Signature ``Font`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Font`` 
    
    :param gridFont: 
    :type gridFont: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Width: NXOpen.DisplayableObjectObjectWidth = ...
    """
    Returns or sets  the line width 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param gridWidth: 
    :type gridWidth: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: CurveDisplaySettings = ...  # unknown typename


class DiagramDisplayStyles2DBarChart(DiagramDisplayStyles):
    """
    Manages the 2D bar chart diagram display styles.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetBarChartStyleSetting(self, styleIndex: int) -> BarChartStyleSetting:
        """
        Gets the bar chart bar display style.  
        
        The style index must be greater than or equal to 0 and
        less than :py:meth:`CAE.Xyplot.DiagramDisplayStyles.StyleCount`.  
        
        Signature ``GetBarChartStyleSetting(styleIndex)`` 
        
        :param styleIndex:  Style index  
        :type styleIndex: int 
        :returns:  Bar Chart Bar style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.BarChartStyleSetting` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    SpaceBetweenFunctions: int = ...
    """
    Returns or sets  the space between functions measured in percentage.  
    
    The acceptable range is 0-10. 
    
    <hr>
    
    Getter Method
    
    Signature ``SpaceBetweenFunctions`` 
    
    :returns:  SpaceBetweenFunctions  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpaceBetweenFunctions`` 
    
    :param spaceBetweenFunctions:  SpaceBetweenFunctions  
    :type spaceBetweenFunctions: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SpaceBetweenItems: int = ...
    """
    Returns or sets  the space between items measured in percentage.  
    
    The acceptable range is 0-10. 
    
    <hr>
    
    Getter Method
    
    Signature ``SpaceBetweenItems`` 
    
    :returns:  SpaceBetweenItems  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpaceBetweenItems`` 
    
    :param spaceBetweenItems:  SpaceBetweenItems  
    :type spaceBetweenItems: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: DiagramDisplayStyles2DBarChart = ...  # unknown typename


class GraphOptionsStyle2D(BaseDisplayStyleSetting):
    """
    Manages the specific settings for 2D graph.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    FrequencyBandSummationBandType: FrequencyBandSummationBandType = ...
    """
    Returns or sets  a value specifies the frequency band summation band type 
    
    <hr>
    
    Getter Method
    
    Signature ``FrequencyBandSummationBandType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.FrequencyBandSummationBandType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FrequencyBandSummationBandType`` 
    
    :param freqBandSummationBandType: 
    :type freqBandSummationBandType: :py:class:`NXOpen.CAE.Xyplot.FrequencyBandSummationBandType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowFrequencyBandSummation: bool = ...
    """
    Returns or sets  a value specifies whether to show frequency band summation 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFrequencyBandSummation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFrequencyBandSummation`` 
    
    :param showFreqBandSummation: 
    :type showFreqBandSummation: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowTotalResponseLineForPolar: bool = ...
    """
    Returns or sets  a value specifies whether to show total response line for 2D polar plot 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowTotalResponseLineForPolar`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowTotalResponseLineForPolar`` 
    
    :param showTotalResponseLineForPolar: 
    :type showTotalResponseLineForPolar: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShowTotalResponseLineForVector: bool = ...
    """
    Returns or sets  a value specifies whether to show total response line for 2D vector plot 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowTotalResponseLineForVector`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowTotalResponseLineForVector`` 
    
    :param showTotalResponseLineForVector: 
    :type showTotalResponseLineForVector: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    TotalResponseLineSetting: CurveDisplaySettings = ...
    """
    Returns  the total response line setting 
    
    <hr>
    
    Getter Method
    
    Signature ``TotalResponseLineSetting`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: GraphOptionsStyle2D = ...  # unknown typename


class ColorBarPlot(Plot, I2DDataPlot):
    """
    Manages the display of color bar plot. 
    
    Call :py:meth:`CAE.Xyplot.I2DDataPlot.EditRecord` to edit data for this class.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def EditRecord(self, nthRecordIdx: int, record: NXOpen.CAE.FTK.BaseRecord) -> None:
        """
        Edits nth record of plot.  
        
        ** Procedure of editing records of plot fully:</b>
        
          #. Call this method to edit record data
          #. Call :py:meth:`CAE.Xyplot.Plot.CommitRecordsChange` to precess record data change and update data model
          #. Call :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` to regenerate display to reflect data change
          #. Optionally call :py:meth:`CAE.Xyplot.Plot.FitView` to make display fit the view;it is only required when the plot display boundary is changed
        
        Signature ``EditRecord(nthRecordIdx, record)`` 
        
        :param nthRecordIdx: 
        :type nthRecordIdx: int 
        :param record: 
        :type record: :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ColorBarPlot = ...  # unknown typename


class NoteStyleSetting(TextStyleSetting):
    """
    Represents the note display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetNoteTexts(self) -> 'list[str]':
        """
        Gets the note texts  
        
        Signature ``GetNoteTexts()`` 
        
        :returns:  Note Texts  
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNoteTexts(self, noteTexts: 'list[str]') -> None:
        """
        Sets the note texts 
        
        Signature ``SetNoteTexts(noteTexts)`` 
        
        :param noteTexts:  Note Texts  
        :type noteTexts: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: NoteStyleSetting = ...  # unknown typename


class LeaderStyle(NXOpen.TaggedObject):
    """
    Manages the Leader display styles.  
    
    Not support KF.
    """
    AnchorColor: NXOpen.NXColor = ...
    """
    Returns or sets  the anchor color 
    
    <hr>
    
    Getter Method
    
    Signature ``AnchorColor`` 
    
    :returns:  anchor color  
    :rtype: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnchorColor`` 
    
    :param color: 
    :type color: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LineStyle: CurveDisplaySettings = ...
    """
    Returns  the line display style.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineStyle`` 
    
    :returns:  Leader line style  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    PointMarker: PointMarker = ...
    """
    Returns or sets  the anchor point marker 
    
    <hr>
    
    Getter Method
    
    Signature ``PointMarker`` 
    
    :returns:  anchor point marker  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.PointMarker` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointMarker`` 
    
    :param pointMarker: 
    :type pointMarker: :py:class:`NXOpen.CAE.Xyplot.PointMarker` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: LeaderStyle = ...  # unknown typename


class WallDisplayStyles3D(WallDisplayStyles):
    """
    Manages the 3D wall display styles.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    ViewOrientation: NXOpen.Matrix3x3 = ...
    """
    Returns or sets  the view orientation matrix 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewOrientation`` 
    
    :returns:  Orientation matrix  
    :rtype: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ViewOrientation`` 
    
    :param orientation:  Orientation matrix  
    :type orientation: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: WallDisplayStyles3D = ...  # unknown typename


class GridLayoutStyle3DSetting(BaseGridLayoutStyleSetting):
    """
    Represents the 3d grid layout display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    ZxGridStyle: GridStyle = ...
    """
    Returns or sets  the grid style of ZX plane 
    
    <hr>
    
    Getter Method
    
    Signature ``ZxGridStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.GridStyle` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZxGridStyle`` 
    
    :param gridStyle: 
    :type gridStyle: :py:class:`NXOpen.CAE.Xyplot.GridStyle` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ZyGridStyle: GridStyle = ...
    """
    Returns or sets  the grid style of ZY plane 
    
    <hr>
    
    Getter Method
    
    Signature ``ZyGridStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.GridStyle` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZyGridStyle`` 
    
    :param gridStyle: 
    :type gridStyle: :py:class:`NXOpen.CAE.Xyplot.GridStyle` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: GridLayoutStyle3DSetting = ...  # unknown typename


class SurfaceColorOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceColorOption():
    """
    Represents the surface filling color option 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No shading"
       "Hidden", "Background color as fill"
       "Shaded", "Fill Color or contour color with shading"
    """
    NotSet = 0  # SurfaceColorOptionMemberType
    Hidden = 1  # SurfaceColorOptionMemberType
    Shaded = 2  # SurfaceColorOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ComplexOption2DBarChartMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComplexOption2DBarChart():
    """
    Represents the 2D bar chart plot complex option 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Magnitude", "Magnitude of the complex data for 2D bar chart plot"
       "Phase", "Phase of the complex data for 2D bar chart plot"
       "Real", "Real part of the complex data for 2D bar chart plot"
       "Imaginary", "Imaginary part of the complex data for 2D bar chart plot"
       "AtPhaseAngle", "At phase angle for 2D bar chart plot"
       "SignedMagnitude", "Signed magnitude for 2D bar chart plot"
    """
    Magnitude = 0  # ComplexOption2DBarChartMemberType
    Phase = 1  # ComplexOption2DBarChartMemberType
    Real = 2  # ComplexOption2DBarChartMemberType
    Imaginary = 3  # ComplexOption2DBarChartMemberType
    AtPhaseAngle = 4  # ComplexOption2DBarChartMemberType
    SignedMagnitude = 5  # ComplexOption2DBarChartMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ComplexOption2DColorContourMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComplexOption2DColorContour():
    """
    Represents the 2D color contour plot complex option 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Magnitude", "Magnitude of the complex data for 2D color contour plot plot"
       "Phase", "Phase of the complex data for 2D color contour plot plot"
       "Real", "Real part of the complex data for 2D color contour plot plot"
       "Imaginary", "Imaginary part of the complex data for 2D color contour plot plot"
       "AtPhaseAngle", "At phase angle for 2D color contour plot plot"
       "SignedMagnitude", "Signed magnitude for 2D color contour plot plot"
    """
    Magnitude = 0  # ComplexOption2DColorContourMemberType
    Phase = 1  # ComplexOption2DColorContourMemberType
    Real = 2  # ComplexOption2DColorContourMemberType
    Imaginary = 3  # ComplexOption2DColorContourMemberType
    AtPhaseAngle = 4  # ComplexOption2DColorContourMemberType
    SignedMagnitude = 5  # ComplexOption2DColorContourMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MarkerStyleSetting(TextStyleSetting):
    """
    Represents the marker display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetNoteTexts(self) -> 'list[str]':
        """
        Gets the note texts  
        
        Signature ``GetNoteTexts()`` 
        
        :returns:  Note Texts  
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNoteTexts(self, noteTexts: 'list[str]') -> None:
        """
        Sets the note texts 
        
        Signature ``SetNoteTexts(noteTexts)`` 
        
        :param noteTexts:  Note Texts  
        :type noteTexts: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    AbsPercentage: float = ...
    """
    Returns or sets  the scale of abscissa percentage setting, just for attachment type: Abscissa Percentage, and the value shuould be limited in [0.  
    
    0, 1.0] 
    
    <hr>
    
    Getter Method
    
    Signature ``AbsPercentage`` 
    
    :returns:  abscissa percentage  
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AbsPercentage`` 
    
    :param absPercentage:  abscissa percentage  
    :type absPercentage: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    AttachmentType: AnchorType = ...
    """
    Returns or sets  the attachment type for associative marker 
    
    <hr>
    
    Getter Method
    
    Signature ``AttachmentType`` 
    
    :returns:  attachment type  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.AnchorType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AttachmentType`` 
    
    :param anchorType:  attachment type  
    :type anchorType: :py:class:`NXOpen.CAE.Xyplot.AnchorType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    NoteTextVisibility: bool = ...
    """
    Returns or sets  the option specifies whether to show note text 
    
    <hr>
    
    Getter Method
    
    Signature ``NoteTextVisibility`` 
    
    :returns:  note text  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NoteTextVisibility`` 
    
    :param isNoteTextVisible:  note text  
    :type isNoteTextVisible: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    NumberTextVisibility: bool = ...
    """
    Returns or sets  the option specifies whether to show number text 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberTextVisibility`` 
    
    :returns:  number text  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberTextVisibility`` 
    
    :param isNumberTextVisible:  number text  
    :type isNumberTextVisible: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SnapToData: bool = ...
    """
    Returns or sets  the option specifies whether just to search source data when creating associative marker 
    
    <hr>
    
    Getter Method
    
    Signature ``SnapToData`` 
    
    :returns:  snap to data  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapToData`` 
    
    :param isSnapToData:  snap to data  
    :type isSnapToData: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: MarkerStyleSetting = ...  # unknown typename


class GeneralDisplayStyles2DColorContour(GeneralDisplayStyles):
    """
    Manages the general display styles for 2D color contour plot.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    ComplexOption: ComplexOption2DColorContour = ...
    """
    Returns or sets  the complex option 
    
    <hr>
    
    Getter Method
    
    Signature ``ComplexOption`` 
    
    :returns:  Complex option  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.ComplexOption2DColorContour` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComplexOption`` 
    
    :param complexOption:  Complex option  
    :type complexOption: :py:class:`NXOpen.CAE.Xyplot.ComplexOption2DColorContour` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: GeneralDisplayStyles2DColorContour = ...  # unknown typename


class ArgumentAxisStyleSetting(BaseDisplayStyleSetting):
    """
    Represents the argument axis display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetAbsCustomerRange(self) -> 'list[str]':
        """
        Gets the abscissa customer range  
        
        Signature ``GetAbsCustomerRange()`` 
        
        :returns:  Abscissa customer range  
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAbsCustomerRange(self, absCustomerRange: 'list[str]') -> None:
        """
        Sets the abscissa customer range 
        
        Signature ``SetAbsCustomerRange(absCustomerRange)`` 
        
        :param absCustomerRange:  Abscissa customer range  
        :type absCustomerRange: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAxisItemStyleSetting(self) -> TextStyleSetting:
        """
        Gets the axis item style  
        
        Signature ``GetAxisItemStyleSetting()`` 
        
        :returns:  Axis item style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.TextStyleSetting` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLabelStyle(self) -> CustomTextStyleSetting:
        """
        Gets the label style  
        
        Signature ``GetLabelStyle()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Xyplot.CustomTextStyleSetting` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    RangeAuto: bool = ...
    """
    Returns or sets  a value indicating whether to set axis range automatically 
    
    <hr>
    
    Getter Method
    
    Signature ``RangeAuto`` 
    
    :returns:  Range auto  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RangeAuto`` 
    
    :param rangeAutomation:  Range auto  
    :type rangeAutomation: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ArgumentAxisStyleSetting = ...  # unknown typename


class StackedPlot(Plot, I2DDataPlot):
    """
    Manages the display of stacked plot. 
    
    Call :py:meth:`CAE.Xyplot.I2DDataPlot.EditRecord` to edit data for this class.
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def EditRecord(self, nthRecordIdx: int, record: NXOpen.CAE.FTK.BaseRecord) -> None:
        """
        Edits nth record of plot.  
        
        ** Procedure of editing records of plot fully:</b>
        
          #. Call this method to edit record data
          #. Call :py:meth:`CAE.Xyplot.Plot.CommitRecordsChange` to precess record data change and update data model
          #. Call :py:meth:`CAE.Xyplot.BaseModel.UpdateDisplay` to regenerate display to reflect data change
          #. Optionally call :py:meth:`CAE.Xyplot.Plot.FitView` to make display fit the view;it is only required when the plot display boundary is changed
        
        Signature ``EditRecord(nthRecordIdx, record)`` 
        
        :param nthRecordIdx: 
        :type nthRecordIdx: int 
        :param record: 
        :type record: :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: StackedPlot = ...  # unknown typename


class MarkerModel(BasicModel):
    """
    Represents a marker object on a plotting graph.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def Delete(self) -> None:
        """
        Deletes the marker model 
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    PointIndex: int = ...
    """
    Returns  the point index of marker model.  
    
    <hr>
    
    Getter Method
    
    Signature ``PointIndex`` 
    
    :returns:  Point index  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    RecordIndex: int = ...
    """
    Returns  the record index of marker model.  
    
    <hr>
    
    Getter Method
    
    Signature ``RecordIndex`` 
    
    :returns:  Record index  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: MarkerModel = ...  # unknown typename


class LegendTableGroupStyle(BaseDisplayStyleSetting, IVisibleDisplayStyle):
    """
    Manages the legend table group styles.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetLegendTableStyle(self, legendTablePositionType: LegendTablePositionType) -> LegendTableStyle:
        """
        Gets legend table style by type.  
        
        Signature ``GetLegendTableStyle(legendTablePositionType)`` 
        
        :param legendTablePositionType: 
        :type legendTablePositionType: :py:class:`NXOpen.CAE.Xyplot.LegendTablePositionType` 
        :returns:  Legend Table style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.LegendTableStyle` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    ActiveLegendTablePosition: LegendTablePositionType = ...
    """
    Returns or sets  the active legend table position type 
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveLegendTablePosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.LegendTablePositionType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveLegendTablePosition`` 
    
    :param activeLegendTablePositionType:  Active Legend Table position type  
    :type activeLegendTablePositionType: :py:class:`NXOpen.CAE.Xyplot.LegendTablePositionType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param visibility: 
    :type visibility: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: LegendTableGroupStyle = ...  # unknown typename


class LegendTableStyle(BaseDisplayStyleSetting):
    """
    Manages the legend table styles.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetPositionType(self) -> LegendTablePositionType:
        """
        Gets the legend table style type  
        
        Signature ``GetPositionType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Xyplot.LegendTablePositionType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTextStyle(self) -> LegendTableTextStyle:
        """
        Gets the text style.  
        
        Signature ``GetTextStyle()`` 
        
        :returns:  Text display style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.LegendTableTextStyle` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetGridLineStyle(self) -> CurveDisplaySettings:
        """
        Gets the grid line style.  
        
        Signature ``GetGridLineStyle()`` 
        
        :returns:  Grid Line style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBorderLineStyle(self) -> CurveDisplaySettings:
        """
        Gets the border line style.  
        
        Signature ``GetBorderLineStyle()`` 
        
        :returns:  Border Line style  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.CurveDisplaySettings` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnTitles(self) -> 'list[str]':
        """
        Gets the legend table column titles 
        
        Signature ``GetColumnTitles()`` 
        
        :returns:  column titles 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnTitles(self, columnTitles: 'list[str]') -> None:
        """
        Sets the legend table column titles 
        
        Signature ``SetColumnTitles(columnTitles)`` 
        
        :param columnTitles:  column titles 
        :type columnTitles: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    BackgroundColor: NXOpen.NXColor = ...
    """
    Returns or sets  the legend table header background color 
    
    <hr>
    
    Getter Method
    
    Signature ``BackgroundColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BackgroundColor`` 
    
    :param backgroundColor: 
    :type backgroundColor: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    GridBackgroundColor: NXOpen.NXColor = ...
    """
    Returns or sets  the grid background color 
    
    <hr>
    
    Getter Method
    
    Signature ``GridBackgroundColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GridBackgroundColor`` 
    
    :param gridBackgroundColor: 
    :type gridBackgroundColor: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IsBorderLineVisible: bool = ...
    """
    Returns or sets  the border line visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``IsBorderLineVisible`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsBorderLineVisible`` 
    
    :param isBorderLineVisible: 
    :type isBorderLineVisible: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IsGridBackgroundFilled: bool = ...
    """
    Returns or sets  the value of controlling whether the grid background is filled 
    
    <hr>
    
    Getter Method
    
    Signature ``IsGridBackgroundFilled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsGridBackgroundFilled`` 
    
    :param isGridBackgroundFilled: 
    :type isGridBackgroundFilled: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IsGridLineVisible: bool = ...
    """
    Returns or sets  the grid line visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``IsGridLineVisible`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsGridLineVisible`` 
    
    :param isGridLineVisible: 
    :type isGridLineVisible: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IsHeaderVisible: bool = ...
    """
    Returns or sets  the legend table header visibility
    
    <hr>
    
    Getter Method
    
    Signature ``IsHeaderVisible`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsHeaderVisible`` 
    
    :param isHeaderVisible: 
    :type isHeaderVisible: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    MaximumLegendItemCount: int = ...
    """
    Returns or sets  the maximum displayable functions count on legend table page 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumLegendItemCount`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumLegendItemCount`` 
    
    :param maxLegendItemCount: 
    :type maxLegendItemCount: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: LegendTableStyle = ...  # unknown typename


class AxisDBScaleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AxisDBScale():
    """
    Represents the DB scale for plot 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Ten", "Db 10"
       "Twenty", "Db 20"
    """
    Ten = 0  # AxisDBScaleMemberType
    Twenty = 1  # AxisDBScaleMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ComplexOption2DMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComplexOption2D():
    """
    Represents the 2D plot complex option 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Magnitude", "Magnitude of the complex data for 2D plot"
       "MagnitudePhase", "Magnitude and phase angle of complex data for 2D plot"
       "Phase", "Only the phase of the complex data for 2D plot"
       "Real", "Only the real part of the complex data for 2D plot"
       "RealImaginary", "Real and imaginary of the complex data for 2D plot"
       "RealImaginaryPhase", "Real, imaginary and phase angle of the complex data for 2D plot"
       "Polar", "Polar for 2D plot"
       "Argand", "Argand for 2D plot"
       "Polar3D", "Polar for 3D plot"
       "Argand3D", "Argand for 3D plot which z coordindate come from the x coordinate"
       "PhaseMagnitude", "Phase angle and Magnitude of complex data for 2D plot"
       "ImaginaryReal", "Real and imaginary of the complex data for 2D plot"
       "PhaseRealImaginary", "Phase angle, real and imaginary of the complex data for 2D plot"
       "ImaginaryRealPhase", "Imaginary, real and phase angle of the complex data for 2D plot"
       "PhaseImaginaryReal", "Phase angle, imaginary and real of the complex data for 2D plot"
       "Nichols", "Nichols for 2D plot"
       "AtPhaseAngle", "At phase angle for 2D plot"
       "SignedMagnitude", "Signed magnitude for 2D plot"
       "Directivity", "Directivity for 2D plot"
       "Vector", "Vector for 2D plot"
    """
    Magnitude = 0  # ComplexOption2DMemberType
    MagnitudePhase = 1  # ComplexOption2DMemberType
    Phase = 2  # ComplexOption2DMemberType
    Real = 3  # ComplexOption2DMemberType
    RealImaginary = 4  # ComplexOption2DMemberType
    RealImaginaryPhase = 5  # ComplexOption2DMemberType
    Polar = 6  # ComplexOption2DMemberType
    Argand = 7  # ComplexOption2DMemberType
    Polar3D = 8  # ComplexOption2DMemberType
    Argand3D = 9  # ComplexOption2DMemberType
    PhaseMagnitude = 10  # ComplexOption2DMemberType
    ImaginaryReal = 11  # ComplexOption2DMemberType
    PhaseRealImaginary = 12  # ComplexOption2DMemberType
    ImaginaryRealPhase = 13  # ComplexOption2DMemberType
    PhaseImaginaryReal = 14  # ComplexOption2DMemberType
    Nichols = 15  # ComplexOption2DMemberType
    AtPhaseAngle = 16  # ComplexOption2DMemberType
    SignedMagnitude = 17  # ComplexOption2DMemberType
    Directivity = 18  # ComplexOption2DMemberType
    Vector = 19  # ComplexOption2DMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LegendTableTextStyle(TextStyleSetting):
    """
    Manages the legend table text styles.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetMargin(self, marginOption: TextBoxMarginOption) -> float:
        """
        Gets the margin value of legend table  
        
        Signature ``GetMargin(marginOption)`` 
        
        :param marginOption: margin option 
        :type marginOption: :py:class:`NXOpen.CAE.Xyplot.TextBoxMarginOption` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMargin(self, marginOption: TextBoxMarginOption, marginValue: float) -> None:
        """
        Sets the margin value of legend table 
        
        Signature ``SetMargin(marginOption, marginValue)`` 
        
        :param marginOption: margin option 
        :type marginOption: :py:class:`NXOpen.CAE.Xyplot.TextBoxMarginOption` 
        :param marginValue: 
        :type marginValue: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: LegendTableTextStyle = ...  # unknown typename


class VectorStyle2DSetting(BaseLineStyleSetting):
    """
    Represents the 2D vector display style.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetVectorColors(self) -> 'list[NXOpen.NXColor]':
        """
        Get the vector display colors  
        
        Signature ``GetVectorColors()`` 
        
        :returns:  Get the display vector colors  
        :rtype: list of Id 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetVectorColors(self, vectorColors: 'list[NXOpen.NXColor]') -> None:
        """
        Set the vector display colors 
        
        Signature ``SetVectorColors(vectorColors)`` 
        
        :param vectorColors:  Set the display vector colors  
        :type vectorColors: list of Id 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNthVectorColor(self, index: int) -> NXOpen.NXColor:
        """
        Get the nth vector display color  
        
        Signature ``GetNthVectorColor(index)`` 
        
        :param index: 
        :type index: int 
        :returns:  Get the nth display vector color  
        :rtype: Id 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNthVectorColors(self, index: int, vectorColors: NXOpen.NXColor) -> None:
        """
        Set the nth vector display color 
        
        Signature ``SetNthVectorColors(index, vectorColors)`` 
        
        :param index: 
        :type index: int 
        :param vectorColors:  Set the nth display vector color  
        :type vectorColors: Id 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    DrawText: bool = ...
    """
    Returns or sets  a value indicating whether to draw annotation text 
    
    <hr>
    
    Getter Method
    
    Signature ``DrawText`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DrawText`` 
    
    :param canDrawText:     
    :type canDrawText: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IsAutoTextCount: bool = ...
    """
    Returns or sets  a value indicating whether to customize annotation text count 
    
    <hr>
    
    Getter Method
    
    Signature ``IsAutoTextCount`` 
    
    :returns:      
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsAutoTextCount`` 
    
    :param isAutoTextCount:      
    :type isAutoTextCount: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    MaximumTextCount: int = ...
    """
    Returns or sets  the maximum of customized text count 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumTextCount`` 
    
    :returns:      
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumTextCount`` 
    
    :param maximumTextCount:      
    :type maximumTextCount: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    OverlapTextAndVector: bool = ...
    """
    Returns or sets  a value indicating whether to allow the annotation text overlap with vector 
    
    <hr>
    
    Getter Method
    
    Signature ``OverlapTextAndVector`` 
    
    :returns:  Whether to allow the annotation text to overlap with vector  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OverlapTextAndVector`` 
    
    :param overlapTextAndVector:  Whether to allow the annotation text to overlap with vector  
    :type overlapTextAndVector: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: VectorStyle2DSetting = ...  # unknown typename


class GeneralDisplayStyles2DBarChart(GeneralDisplayStyles):
    """
    Manages the general display styles for 2D bar chart plot.  
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    ComplexOption: ComplexOption2DBarChart = ...
    """
    Returns or sets  the complex option 
    
    <hr>
    
    Getter Method
    
    Signature ``ComplexOption`` 
    
    :returns:  Complex option  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.ComplexOption2DBarChart` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComplexOption`` 
    
    :param complexOption:  Complex option  
    :type complexOption: :py:class:`NXOpen.CAE.Xyplot.ComplexOption2DBarChart` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: GeneralDisplayStyles2DBarChart = ...  # unknown typename


class DirectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Direction():
    """
    Represents the direction option 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", "Option to show plot in the X axis direction"
       "Z", "Option to show plot in the Z axis direction"
       "Xz", "Option to show plot in the both X and Z axis direction"
    """
    X = 0  # DirectionMemberType
    Z = 1  # DirectionMemberType
    Xz = 2  # DirectionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FonttypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Fonttype():
    """
    Represents the font type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Nx", "NX Font"
       "Standard", "Standard Font"
    """
    Nx = 0  # FonttypeMemberType
    Standard = 1  # FonttypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PlateColorOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PlateColorOption():
    """
    Represents the plate filling color option 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fill", "Fill color with no shading"
       "Hidden", "Background color as fill"
       "Shaded", "Fill Color with shading"
    """
    Fill = 0  # PlateColorOptionMemberType
    Hidden = 1  # PlateColorOptionMemberType
    Shaded = 2  # PlateColorOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BaseTemplateManager(NXOpen.NXObject):
    """
    Manages the graph template   
    
    Not support KF.
    
    .. versionadded:: NX7.5.0
    """
    
    def LoadTemplate(self, templateFile: str) -> None:
        """
        Loads the graph template file 
        
        Signature ``LoadTemplate(templateFile)`` 
        
        :param templateFile:  Template file name with full path  
        :type templateFile: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def UnloadTemplate(self, templateFile: str) -> None:
        """
        Unloads the graph template file 
        
        Signature ``UnloadTemplate(templateFile)`` 
        
        :param templateFile:  Template file name with full path  
        :type templateFile: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def UnloadAllTemplates(self) -> None:
        """
        Unloads all graph template files 
        
        Signature ``UnloadAllTemplates()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetTemplate(self, templateFile: str) -> None:
        """
        Resets to default value 
        
        Signature ``ResetTemplate(templateFile)`` 
        
        :param templateFile:  Template file name with full path  
        :type templateFile: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteTemplate(self, templateFile: str) -> None:
        """
        Deletes template file 
        
        Signature ``DeleteTemplate(templateFile)`` 
        
        :param templateFile:  Template file name with full path  
        :type templateFile: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveTemplate(self, templateFile: str) -> None:
        """
        Saves to template file 
        
        Signature ``SaveTemplate(templateFile)`` 
        
        :param templateFile:  Template file name with full path  
        :type templateFile: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveAsTemplate(self, sourceTemplateFile: str, destinationTemplateFile: str) -> None:
        """
        Saves to new template file 
        
        Signature ``SaveAsTemplate(sourceTemplateFile, destinationTemplateFile)`` 
        
        :param sourceTemplateFile:  Source template file name with full path  
        :type sourceTemplateFile: str 
        :param destinationTemplateFile:  Destination template file name with full path  
        :type destinationTemplateFile: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def RenameTemplateFile(self, oldTemplateFile: str, newTemplateFileName: str) -> None:
        """
        Renames template file 
        
        Signature ``RenameTemplateFile(oldTemplateFile, newTemplateFileName)`` 
        
        :param oldTemplateFile:  old template file with full path  
        :type oldTemplateFile: str 
        :param newTemplateFileName:  new template file with simple name.  
        :type newTemplateFileName: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveAllTemplates(self) -> None:
        """
        Saves all templates 
        
        Signature ``SaveAllTemplates()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetSystemTemplate(self) -> None:
        """
        Resets system template  
        
        Signature ``ResetSystemTemplate()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDefaultTemplate(self) -> str:
        """
        Returns the default template file  
        
        Signature ``GetDefaultTemplate()`` 
        
        :returns:  Template file name with full path  
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultTemplate(self, templateFile: str) -> None:
        """
        Sets the default template file. 
        
          #. 
        If the input template file is NULL, it will remove default template state.
        
          #. 
        If the input template file is not NULL, it will set the input template as default template.
        
        Signature ``SetDefaultTemplate(templateFile)`` 
        
        :param templateFile:  Template file name with full path  
        :type templateFile: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ReloadAllTemplateFiles(self) -> None:
        """
        Reload all graph template files so that the modification on the 
        loaded graph template files are reset.  
        
        The unloaded files under 
        customer directories which is defined by environement variable 
        UGII_BASE_DIR, UGII_VENDOR_DIR, UGII_SITE_DIR and UGII_USER_DIR 
        will be reloaded. Also the graph templates in active root part directory 
        will be reloaded if they are unloaded.  
        
        Signature ``ReloadAllTemplateFiles()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    ActiveTemplate: str = ...
    """
    Returns or sets  the active template file 
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveTemplate`` 
    
    :returns:  Template file name with full path  
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.BaseTemplateManager.GetDefaultTemplate`
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveTemplate`` 
    
    :param templateFile:  Template file name with full path  
    :type templateFile: str 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.CAE.Xyplot.BaseTemplateManager.SetDefaultTemplate`
    
    License requirements: None.
    """
    Null: BaseTemplateManager = ...  # unknown typename


class ColorAxisStyleSetting(AxisStyleSetting):
    """
    Represents the axis display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    ColorScaleStyleSetting: ColorScaleStyle = ...
    """
    Returns  the color scale display style.  
    
    <hr>
    
    Getter Method
    
    Signature ``ColorScaleStyleSetting`` 
    
    :returns:  Color scale style  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.ColorScaleStyle` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    UnknownResultScaleStyleSetting: UnknownResultScaleStyle = ...
    """
    Returns  the unknown result scale display style.  
    
    <hr>
    
    Getter Method
    
    Signature ``UnknownResultScaleStyleSetting`` 
    
    :returns: Color scale style  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.UnknownResultScaleStyle` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: ColorAxisStyleSetting = ...  # unknown typename


class GridLayoutStyle2DSetting(BaseGridLayoutStyleSetting):
    """
    Represents the 2d grid layout display style.  
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    Null: GridLayoutStyle2DSetting = ...  # unknown typename


class OverlayParameters(BasePlotParameters):
    """
    Represents the parameters passed to overlay plot records on an existing plot graph.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Xyplot.XYPlotManager.NewOverlayParameters`
    
    .. versionadded:: NX9.0.0
    """
    SubGraphInStack: int = ...
    """
    Returns or sets  the index of subgraph on a stacked plot, on which the records will be
    overlaied.  
    
    The property is only available when overlaying records on
    a stacked plot. The index value is between 0 and the property value of
    :py:meth:`CAE.Xyplot.Plot.SubGraphCountInStack`. 
    
    <hr>
    
    Getter Method
    
    Signature ``SubGraphInStack`` 
    
    :returns:  The sub-graph index  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SubGraphInStack`` 
    
    :param subGraphIndex:  The sub-graph index  
    :type subGraphIndex: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """


class TextAlignmentMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TextAlignment():
    """
    Represents the text alignment 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "Left align text"
       "Center", "Center align text"
       "Right", "Right align text"
    """
    Left = 0  # TextAlignmentMemberType
    Center = 1  # TextAlignmentMemberType
    Right = 2  # TextAlignmentMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class XYPlotManager():
    """
    XYPlot function manager   
    
    To obtain an instance of this class use :py:meth:`NXOpen.Session.XYPlotManager`.
    
    .. versionadded:: NX7.5.0
    """
    
    def PlotRecords(self, plotParameters: PlotParameters) -> Plot:
        """
        Creates plot with given parameters  
        
        Signature ``PlotRecords(plotParameters)`` 
        
        :param plotParameters:  the plot parameters  
        :type plotParameters: :py:class:`NXOpen.CAE.Xyplot.PlotParameters` 
        :returns:  Created plot  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.Plot` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OverlayRecords(self, overlayParameters: OverlayParameters) -> Plot:
        """
        Overlay records with given parameters  
        
        Signature ``OverlayRecords(overlayParameters)`` 
        
        :param overlayParameters:  the overlay parameters  
        :type overlayParameters: :py:class:`NXOpen.CAE.Xyplot.OverlayParameters` 
        :returns:  Overlayed plot  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.Plot` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCurrentPlot(self, deviceIndex: int, viewIndex: int) -> Plot:
        """
        Gets the current plot on the view port of specific device  
        
        Signature ``GetCurrentPlot(deviceIndex, viewIndex)`` 
        
        :param deviceIndex:  Device index  
        :type deviceIndex: int 
        :param viewIndex:  View index  
        :type viewIndex: int 
        :returns:  Current plot  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.Plot` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ShowNextPlot(self, deviceIndex: int, viewIndex: int) -> None:
        """
        Shows the next plot on the view port of specific device 
        
        Signature ``ShowNextPlot(deviceIndex, viewIndex)`` 
        
        :param deviceIndex:  Device index  
        :type deviceIndex: int 
        :param viewIndex:  View index  
        :type viewIndex: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ShowPreviousPlot(self, deviceIndex: int, viewIndex: int) -> None:
        """
        Shows the previous plot on the view port of specific device 
        
        Signature ``ShowPreviousPlot(deviceIndex, viewIndex)`` 
        
        :param deviceIndex:  Device index  
        :type deviceIndex: int 
        :param viewIndex:  View index  
        :type viewIndex: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewPlotParameters(self) -> PlotParameters:
        """
        Creates an transient object :py:class:`NXOpen.CAE.Xyplot.PlotParameters` to contain the
        settings required by creating a plot.  
        
        The object should be destroyed after plot is created.  
        
        Signature ``NewPlotParameters()`` 
        
        :returns:  the plot parameters object created  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.PlotParameters` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewOverlayParameters(self) -> OverlayParameters:
        """
        Creates an transient object :py:class:`NXOpen.CAE.Xyplot.PlotParameters` to contain the settings
        required by overlaying new records on a plot.  
        
        The object should be destroyed after overlaying plot is created.  
        
        Signature ``NewOverlayParameters()`` 
        
        :returns:  the overlay parameters object created  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.OverlayParameters` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAvailableWindowDevices(self) -> 'list[int]':
        """
        Gets all window devices on which XY graph could be plotted  
        
        Signature ``GetAvailableWindowDevices()`` 
        
        :returns:  Available Plot Winodw Devices  
        :rtype: list of int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetWindowDevicesViews(self, windowDevice: int) -> 'list[int]':
        """
        Gets view count and views for specified window device  
        
        Signature ``GetWindowDevicesViews(windowDevice)`` 
        
        :param windowDevice:   window index   
        :type windowDevice: int 
        :returns:  the views on window device 
        :rtype: list of int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPlots(self, windowDevice: int, view: int) -> 'list[Plot]':
        """
        Gets all plots on a view of specified window device  
        
        Signature ``GetPlots(windowDevice, view)`` 
        
        :param windowDevice:   Plot index  
        :type windowDevice: int 
        :param view:   View index  
        :type view: int 
        :returns:  Plots       
        :rtype: list of :py:class:`NXOpen.CAE.Xyplot.Plot` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ReturnToModelView(self, view: int) -> None:
        """
        Clears all plots on a view of main graphics windows and returns to model view
        
        Signature ``ReturnToModelView(view)`` 
        
        :param view:   View index  
        :type view: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def WriteImageToClipBoard(self, deviceIndex: int, viewIndex: int, isUseWhiteBackGround: bool) -> None:
        """
        Write the image of current plot on a view to Windows's ClipBoard
        
        Signature ``WriteImageToClipBoard(deviceIndex, viewIndex, isUseWhiteBackGround)`` 
        
        :param deviceIndex:  Device index  
        :type deviceIndex: int 
        :param viewIndex:  View index  
        :type viewIndex: int 
        :param isUseWhiteBackGround: 
        :type isUseWhiteBackGround: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Plot:
        """
        Finds the :py:class:`CAE.Xyplot.Plot` with the given identifier as recorded in a journal 
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier of the :py:class:`CAE.Xyplot.Plot` to be found  
        :type journalIdentifier: str 
        :returns:  Plot object found, or null if no such plot exists  
        :rtype: :py:class:`NXOpen.CAE.Xyplot.Plot` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Preference: Preference = ...
    """
    Returns  the preference 
    
    <hr>
    
    Getter Method
    
    Signature ``Preference`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.Preference` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TemplateManager: BaseTemplateManager = ...
    """
    Returns  the template manager.  
    
    <hr>
    
    Getter Method
    
    Signature ``TemplateManager`` 
    
    :returns:  Template manager  
    :rtype: :py:class:`NXOpen.CAE.Xyplot.BaseTemplateManager` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    WindowManager: WindowManager = ...
    """
    Returns the :py:class:`NXOpen.CAE.Xyplot.WindowManager` belonging.  
    
    This class is restricted to being called from a program running during an interactive NX session.
    If run from a non-interactive session it will return None. 
    
    Signature ``WindowManager`` 
    
    .. versionadded:: NX9.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.WindowManager`
    """


class PlateStyle3DSetting(BasePlateStyleSetting):
    """
    Represents the 3d plate display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX12.0.0
       There is no replacement for this class.
    """
    ColorOption: PlateColorOption = ...
    """
    Returns or sets  the color option 
    
    <hr>
    
    Getter Method
    
    Signature ``ColorOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.PlateColorOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColorOption`` 
    
    :param colorOption: 
    :type colorOption: :py:class:`NXOpen.CAE.Xyplot.PlateColorOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Direction: Direction = ...
    """
    Returns or sets  the plate direction 
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.CAE.Xyplot.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: PlateStyle3DSetting = ...  # unknown typename


class BarStyle3DSetting(BaseBarStyleSetting):
    """
    Represents the 3d bar display style.  
    
    Call :py:meth:`CAE.Xyplot.BaseDisplayStyleSetting.CommitChange`
    to apply style changes to corresponding plot after it's modified.
    
    Not support KF.
    
    .. versionadded:: NX9.0.0
    """
    ColorOption: BarColorOption = ...
    """
    Returns or sets  the filling color option 
    
    <hr>
    
    Getter Method
    
    Signature ``ColorOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Xyplot.BarColorOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColorOption`` 
    
    :param colorOption: 
    :type colorOption: :py:class:`NXOpen.CAE.Xyplot.BarColorOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Depth: int = ...
    """
    Returns or sets  the bar depth.  
    
    The range is from 0 to 100. 
    
    <hr>
    
    Getter Method
    
    Signature ``Depth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Depth`` 
    
    :param barDepth: 
    :type barDepth: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: BarStyle3DSetting = ...  # unknown typename


