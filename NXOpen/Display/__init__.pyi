# module 'NXOpen.Display'
#
# Automatically generated 2025-06-09T14:38:45.542999
#
"""Default documentation for NXOpen.Display."""

import typing

import NXOpen
import NXOpen.GeometricUtilities



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class GridBuilderLineStyleTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GridBuilderLineStyleType():
    """
    Specifies line style to be used for major and minor lines of the grid.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Solid", " - "
       "Dashed", " - "
       "Phantom", " - "
       "Centerline", " - "
       "Dotted", " - "
       "Longdash", " - "
       "Dotdash", " - "
    """
    Solid = 0  # GridBuilderLineStyleTypeMemberType
    Dashed = 1  # GridBuilderLineStyleTypeMemberType
    Phantom = 2  # GridBuilderLineStyleTypeMemberType
    Centerline = 3  # GridBuilderLineStyleTypeMemberType
    Dotted = 4  # GridBuilderLineStyleTypeMemberType
    Longdash = 5  # GridBuilderLineStyleTypeMemberType
    Dotdash = 6  # GridBuilderLineStyleTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GridBuilderLineWeightTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GridBuilderLineWeightType():
    """
    Specifies line weight to be used for major and minor lines of the grid.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Thin", " - "
       "Normal", " - "
       "Thick", " - "
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
    Thin = 0  # GridBuilderLineWeightTypeMemberType
    Normal = 1  # GridBuilderLineWeightTypeMemberType
    Thick = 2  # GridBuilderLineWeightTypeMemberType
    One = 3  # GridBuilderLineWeightTypeMemberType
    Two = 4  # GridBuilderLineWeightTypeMemberType
    Three = 5  # GridBuilderLineWeightTypeMemberType
    Four = 6  # GridBuilderLineWeightTypeMemberType
    Five = 7  # GridBuilderLineWeightTypeMemberType
    Six = 8  # GridBuilderLineWeightTypeMemberType
    Seven = 9  # GridBuilderLineWeightTypeMemberType
    Eight = 10  # GridBuilderLineWeightTypeMemberType
    Nine = 11  # GridBuilderLineWeightTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GridBuilder(NXOpen.Builder):
    """
    Represents the builder for adding a grid :py:class:`NXOpen.Display.Grid`
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX6.0.0
    """
    
    class LineStyleType():
        """
        Specifies line style to be used for major and minor lines of the grid.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Solid", " - "
           "Dashed", " - "
           "Phantom", " - "
           "Centerline", " - "
           "Dotted", " - "
           "Longdash", " - "
           "Dotdash", " - "
        """
        Solid = 0  # GridBuilderLineStyleTypeMemberType
        Dashed = 1  # GridBuilderLineStyleTypeMemberType
        Phantom = 2  # GridBuilderLineStyleTypeMemberType
        Centerline = 3  # GridBuilderLineStyleTypeMemberType
        Dotted = 4  # GridBuilderLineStyleTypeMemberType
        Longdash = 5  # GridBuilderLineStyleTypeMemberType
        Dotdash = 6  # GridBuilderLineStyleTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LineWeightType():
        """
        Specifies line weight to be used for major and minor lines of the grid.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Thin", " - "
           "Normal", " - "
           "Thick", " - "
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
        Thin = 0  # GridBuilderLineWeightTypeMemberType
        Normal = 1  # GridBuilderLineWeightTypeMemberType
        Thick = 2  # GridBuilderLineWeightTypeMemberType
        One = 3  # GridBuilderLineWeightTypeMemberType
        Two = 4  # GridBuilderLineWeightTypeMemberType
        Three = 5  # GridBuilderLineWeightTypeMemberType
        Four = 6  # GridBuilderLineWeightTypeMemberType
        Five = 7  # GridBuilderLineWeightTypeMemberType
        Six = 8  # GridBuilderLineWeightTypeMemberType
        Seven = 9  # GridBuilderLineWeightTypeMemberType
        Eight = 10  # GridBuilderLineWeightTypeMemberType
        Nine = 11  # GridBuilderLineWeightTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def InheritSettings(self, grid: Grid) -> None:
        """
        Inherits the settings from the specified grid.  
        
        These includes
        settings such as 
        :py:meth:`Display.GridBuilder.MajorLineSpacing``.
        
        Signature ``InheritSettings(grid)`` 
        
        :param grid:  The grid. None is invalid.  
        :type grid: :py:class:`NXOpen.Display.Grid` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    LineColor: NXOpen.NXColor = ...
    """
    Returns or sets  the line color 
    
    <hr>
    
    Getter Method
    
    Signature ``LineColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineColor`` 
    
    :param lineColor: 
    :type lineColor: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MajorLineSpacing: float = ...
    """
    Returns or sets  the major line spacing 
    
    <hr>
    
    Getter Method
    
    Signature ``MajorLineSpacing`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MajorLineSpacing`` 
    
    :param majorLineSpacing: 
    :type majorLineSpacing: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MajorLineStyle: GridBuilderLineStyleType = ...
    """
    Returns or sets  the major line style 
    
    <hr>
    
    Getter Method
    
    Signature ``MajorLineStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.GridBuilderLineStyleType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MajorLineStyle`` 
    
    :param majorLineStyle: 
    :type majorLineStyle: :py:class:`NXOpen.Display.GridBuilderLineStyleType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MajorLineWeight: GridBuilderLineWeightType = ...
    """
    Returns or sets  the major line weight 
    
    <hr>
    
    Getter Method
    
    Signature ``MajorLineWeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.GridBuilderLineWeightType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MajorLineWeight`` 
    
    :param majorLineWeight: 
    :type majorLineWeight: :py:class:`NXOpen.Display.GridBuilderLineWeightType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MinorLineStyle: GridBuilderLineStyleType = ...
    """
    Returns or sets  the minor line style 
    
    <hr>
    
    Getter Method
    
    Signature ``MinorLineStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.GridBuilderLineStyleType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinorLineStyle`` 
    
    :param minorLineStyle: 
    :type minorLineStyle: :py:class:`NXOpen.Display.GridBuilderLineStyleType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MinorLineWeight: GridBuilderLineWeightType = ...
    """
    Returns or sets  the minor line weight 
    
    <hr>
    
    Getter Method
    
    Signature ``MinorLineWeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.GridBuilderLineWeightType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinorLineWeight`` 
    
    :param minorLineWeight: 
    :type minorLineWeight: :py:class:`NXOpen.Display.GridBuilderLineWeightType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MinorLinesPerMajor: int = ...
    """
    Returns or sets  the minor lines per major 
    
    <hr>
    
    Getter Method
    
    Signature ``MinorLinesPerMajor`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinorLinesPerMajor`` 
    
    :param minorLinesPerMajor: 
    :type minorLinesPerMajor: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Show: bool = ...
    """
    Returns or sets  the show 
    
    <hr>
    
    Getter Method
    
    Signature ``Show`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Show`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowMajorLines: bool = ...
    """
    Returns or sets  the show major lines 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowMajorLines`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowMajorLines`` 
    
    :param showMajorLines: 
    :type showMajorLines: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowOnTop: bool = ...
    """
    Returns or sets  the show on top 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOnTop`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOnTop`` 
    
    :param showOnTop: 
    :type showOnTop: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SnapPointsPerMinor: int = ...
    """
    Returns or sets  the snap points per minor 
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointsPerMinor`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointsPerMinor`` 
    
    :param snapPointsPerMinor: 
    :type snapPointsPerMinor: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SnapToGrid: bool = ...
    """
    Returns or sets  the snap to grid 
    
    <hr>
    
    Getter Method
    
    Signature ``SnapToGrid`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapToGrid`` 
    
    :param snapToGrid: 
    :type snapToGrid: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: GridBuilder = ...  # unknown typename


class BoundedGridBuilderShowLabelTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BoundedGridBuilderShowLabelType():
    """
    Specifies label option to be used for grid label display.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Always", "Always show label"
       "ParalleltoView", "Show labels when grid orientation is aligned with the view orientation"
       "NotSet", "Never show labels"
    """
    Always = 0  # BoundedGridBuilderShowLabelTypeMemberType
    ParalleltoView = 1  # BoundedGridBuilderShowLabelTypeMemberType
    NotSet = 2  # BoundedGridBuilderShowLabelTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BoundedGridBuilderLabelReferenceTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BoundedGridBuilderLabelReferenceType():
    """
    Specifies label reference.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Local", "Use local grid origin to determine grid line offset labels"
       "Wcs", "Use projection of WCS origin on the grid plane to determine grid line offset labels"
       "Absolute", "Use projection of absolute origin on the grid plane to determine grid line offset labels"
    """
    Local = 0  # BoundedGridBuilderLabelReferenceTypeMemberType
    Wcs = 1  # BoundedGridBuilderLabelReferenceTypeMemberType
    Absolute = 2  # BoundedGridBuilderLabelReferenceTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BoundedGridBuilder(GridBuilder):
    """
    Represents the builder for creating a bounded grid :py:class:`NXOpen.Display.BoundedGrid`.  
    
    This is an abstract class, and cannot be instantiated.
    
    Default values.
    
    =================================  ======
    Property                           Value
    =================================  ======
    SectionCurveSettings.ColorOption   Any 
    ---------------------------------  ------
    SectionCurveSettings.Show          false 
    =================================  ======
    
    .. versionadded:: NX6.0.0
    """
    
    class ShowLabelType():
        """
        Specifies label option to be used for grid label display.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Always", "Always show label"
           "ParalleltoView", "Show labels when grid orientation is aligned with the view orientation"
           "NotSet", "Never show labels"
        """
        Always = 0  # BoundedGridBuilderShowLabelTypeMemberType
        ParalleltoView = 1  # BoundedGridBuilderShowLabelTypeMemberType
        NotSet = 2  # BoundedGridBuilderShowLabelTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LabelReferenceType():
        """
        Specifies label reference.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Local", "Use local grid origin to determine grid line offset labels"
           "Wcs", "Use projection of WCS origin on the grid plane to determine grid line offset labels"
           "Absolute", "Use projection of absolute origin on the grid plane to determine grid line offset labels"
        """
        Local = 0  # BoundedGridBuilderLabelReferenceTypeMemberType
        Wcs = 1  # BoundedGridBuilderLabelReferenceTypeMemberType
        Absolute = 2  # BoundedGridBuilderLabelReferenceTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetCornerPoints(self) -> tuple:
        """
        Gets corner points of the grid  
        
        Signature ``GetCornerPoints()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (validCornerPoints, point1, point2, point3, point4). validCornerPoints is a bool.   Flag indicating whether the                                                        corner points are valid point1 is a :py:class:`NXOpen.Point3d`.   First corner point point2 is a :py:class:`NXOpen.Point3d`.   Second corner point point3 is a :py:class:`NXOpen.Point3d`.   Third corner point point4 is a :py:class:`NXOpen.Point3d`.   Fourth corner point 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCornerPoints(self, point1: NXOpen.Point3d, point2: NXOpen.Point3d, point3: NXOpen.Point3d, point4: NXOpen.Point3d) -> bool:
        """
        Sets corner points of the grid  
        
        Signature ``SetCornerPoints(point1, point2, point3, point4)`` 
        
        :param point1:  First corner point  
        :type point1: :py:class:`NXOpen.Point3d` 
        :param point2:  Second corner point  
        :type point2: :py:class:`NXOpen.Point3d` 
        :param point3:  Third corner point  
        :type point3: :py:class:`NXOpen.Point3d` 
        :param point4:  Fourth corner point  
        :type point4: :py:class:`NXOpen.Point3d` 
        :returns:  Flag indicating whether the
        corner points are valid  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveCurves(self, groupName: str) -> None:
        """
        Creates curves by intersecting the bounded grid with all bodies in 
        the part of the grid object.  
        
        The bodies that are visible in the work
        view are intersected. The curves are added to the group created with 
        the specified name. The group is displayed in the part navigator. The
        curves are created in the work part. These curves are not associated
        with the grid. These are just snapshot curves that can be used for
        modeling purposes. If the customer default "Load Solids/Sheets when
        Saving Section Curves" is enabled, the Save Copy of Section Curves 
        command in the datum plane grid dialog will cause solid/sheet bodies 
        to be loaded into memory for any visible lightweight bodies on the 
        section plane. This may increase the time and memory used by the 
        operation, but will ensure fully accurate section curves.
        
        Signature ``SaveCurves(groupName)`` 
        
        :param groupName:  Name of the group containing curves.                                             If None, a default name will be                                             used.  
        :type groupName: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    Associative: bool = ...
    """
    Returns or sets  the associative 
    
    <hr>
    
    Getter Method
    
    Signature ``Associative`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Associative`` 
    
    :param associative: 
    :type associative: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    LabelReference: BoundedGridBuilderLabelReferenceType = ...
    """
    Returns or sets  the label reference 
    
    <hr>
    
    Getter Method
    
    Signature ``LabelReference`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.BoundedGridBuilderLabelReferenceType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelReference`` 
    
    :param labelReference: 
    :type labelReference: :py:class:`NXOpen.Display.BoundedGridBuilderLabelReferenceType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    LocalOrigin: NXOpen.Point3d = ...
    """
    Returns or sets  the local origin 
    
    <hr>
    
    Getter Method
    
    Signature ``LocalOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LocalOrigin`` 
    
    :param localOrigin:  Label origin  
    :type localOrigin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SectionCurveSettings: SectionCurveSettingsBuilder = ...
    """
    Returns  the curve settings builder 
    
    <hr>
    
    Getter Method
    
    Signature ``SectionCurveSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.SectionCurveSettingsBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowLabel: BoundedGridBuilderShowLabelType = ...
    """
    Returns or sets  the show labels 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.BoundedGridBuilderShowLabelType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowLabel`` 
    
    :param showLabelType: 
    :type showLabelType: :py:class:`NXOpen.Display.BoundedGridBuilderShowLabelType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: BoundedGridBuilder = ...  # unknown typename


class DatumPlaneGridBuilderGridOrientationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DatumPlaneGridBuilderGridOrientationType():
    """
    Specifies grid orientation option to be used for grid display.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FromDatumPlane", "Grid display matches datum plane display"
       "Custom", "Grid size, location, and orientation can be customized using the manipulator controls"
    """
    FromDatumPlane = 0  # DatumPlaneGridBuilderGridOrientationTypeMemberType
    Custom = 1  # DatumPlaneGridBuilderGridOrientationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DatumPlaneGridBuilder(BoundedGridBuilder):
    """
    Represents the builder for adding a datum plane grid :py:class:`NXOpen.Display.DatumPlaneGrid` 
    to a datum plane.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Display.GridCollection.CreateDatumPlaneGridBuilder`
    
    Default values.
    
    ===================  ========================================
    Property             Value
    ===================  ========================================
    Associative          1 
    -------------------  ----------------------------------------
    GridOrientation      Custom 
    -------------------  ----------------------------------------
    LabelReference       Local 
    -------------------  ----------------------------------------
    MajorLineSpacing     100 (millimeters part), 1 (inches part) 
    -------------------  ----------------------------------------
    MajorLineStyle       Solid 
    -------------------  ----------------------------------------
    MajorLineWeight      Normal 
    -------------------  ----------------------------------------
    MinorLineStyle       Dashed 
    -------------------  ----------------------------------------
    MinorLineWeight      Thin 
    -------------------  ----------------------------------------
    MinorLinesPerMajor   1 
    -------------------  ----------------------------------------
    Show                 1 
    -------------------  ----------------------------------------
    ShowLabel            Always 
    -------------------  ----------------------------------------
    ShowMajorLines       1 
    -------------------  ----------------------------------------
    ShowOnTop            0 
    -------------------  ----------------------------------------
    SnapPointsPerMinor   1 
    -------------------  ----------------------------------------
    SnapToGrid           0 
    ===================  ========================================
    
    .. versionadded:: NX6.0.0
    """
    
    class GridOrientationType():
        """
        Specifies grid orientation option to be used for grid display.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FromDatumPlane", "Grid display matches datum plane display"
           "Custom", "Grid size, location, and orientation can be customized using the manipulator controls"
        """
        FromDatumPlane = 0  # DatumPlaneGridBuilderGridOrientationTypeMemberType
        Custom = 1  # DatumPlaneGridBuilderGridOrientationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetDatumPlanes(self) -> 'list[NXOpen.DatumPlane]':
        """
        Get the list of datum planes.  
        
        Signature ``GetDatumPlanes()`` 
        
        :returns:  datum plane list  
        :rtype: list of :py:class:`NXOpen.DatumPlane` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDatumPlanes(self, datumPlanes: 'list[NXOpen.DatumPlane]') -> None:
        """
        Set the list of datum planes.  
        
        When editing an existing datum plane grid, 
        only a single datum plane may be set and it must meet the following conditions:
        - one that currently does not have a grid associated to it
        - one that matches :py:meth:`NXOpen.Display.DatumPlaneGridBuilder.GetDatumPlanes`
        
        Signature ``SetDatumPlanes(datumPlanes)`` 
        
        :param datumPlanes:  datum plane list  
        :type datumPlanes: list of :py:class:`NXOpen.DatumPlane` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    GridOrientation: DatumPlaneGridBuilderGridOrientationType = ...
    """
    Returns or sets  the grid orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``GridOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DatumPlaneGridBuilderGridOrientationType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GridOrientation`` 
    
    :param gridOrientation: 
    :type gridOrientation: :py:class:`NXOpen.Display.DatumPlaneGridBuilderGridOrientationType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: DatumPlaneGridBuilder = ...  # unknown typename


class PointCloud(NXOpen.DisplayableObject):
    """
    Represents a :py:class:`NXOpen.Display.PointCloud` imported from point data files.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Display.PointCloudBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def Load(self) -> None:
        """
        Loads the selected point cloud.  
        
        Signature ``Load()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
        """
        ...
    
    
    def Unload(self) -> None:
        """
        Unloads the selected point cloud.  
        
        Signature ``Unload()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: PointCloud = ...  # unknown typename


class IDynamicSectionCutCreator(NXOpen.INXObject):
    """
    Represents a dynamic section-cut creator that generates dynamic
    section-cuts (see :py:class:`NXOpen.Display.DynamicSectionCut`).  
    
    Examples of dynamic section-cut creator are:
    :py:class:`NXOpen.Display.DynamicSection`
    :py:class:`NXOpen.Display.Grid`
    
    Dynamic sectioncut creator is not supported in KF.
    
    .. versionadded:: NX10.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class DynamicSection(NXOpen.NXObject, IDynamicSectionCutCreator):
    """
    Represents a dynamic section   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Display.DynamicSectionBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    def UpdateSectionCuts(self, updateOption: NXOpen.UpdateOption) -> None:
        """
        Updates the section-cuts (curves) associated with the dynamic 
        section object if they are out-of-date.  
        
        If the section object is out-of-date, then it is first logged for 
        update. If update option is :py:class:`NXOpen.UpdateOption.Now <NXOpen.UpdateOption>`, 
        then the update is performed immediately. If the user wants to update 
        multiple section objects, then it is optimal to specify the update option 
        as :py:class:`NXOpen.UpdateOption.Later <NXOpen.UpdateOption>` and perform 
        update at the end using :py:meth:`NXOpen.Update.DoUpdate`.
        
        An valid undo mark :py:class:`NXOpen.SessionUndoMarkId_Struct` must have been 
        set so that the session can be rolled back successfully if an error occurs.
        See :py:meth:`NXOpen.Session.SetUndoMark`.
        
        Signature ``UpdateSectionCuts(updateOption)`` 
        
        :param updateOption:  Update option  
        :type updateOption: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Find(self, journalIdentifier: str) -> DynamicSectionCut:
        """
        Finds the :py:class:`NXOpen.Display.DynamicSectionCut` 
        with the given identifier as recorded in a journal.  
        
        An object may 
        not return the same value as its JournalIdentifier in different 
        versions of  the software. However newer versions of the software 
        should find the same object when FindObject is passed older versions 
        of its journal identifier. In general, this method should not be 
        used in handwritten code and exists to support record and playback 
        of journals.
        
        An exception will be thrown if no object can be found with the 
        given journal identifier.  
        
        Signature ``Find(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Display.DynamicSectionCut` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSectionCuts(self, contextOccurrence: NXOpen.NXObject, view: NXOpen.View) -> 'list[DynamicSectionCut]':
        """
        Gets section-cuts generated by the sectioning the model shown
        in the specified view.  
        
        View must belong to the same part as the section-cut creator. If
        no view is specified, then section-cuts generated from the 
        sectionable entities in the part are returned.
        
        If a view is specified, then :py:class:`NXOpen.Assemblies.Explosion`
        active in the view is used to get section-cuts for the explosion.
        If the view does not have any active explosion, then
        section-cuts generated from the sectionable entities in the part 
        are returned. 
        
        Signature ``GetSectionCuts(contextOccurrence, view)`` 
        
        :param contextOccurrence:  This can be None. If non None, then this must                    be an occurrence.                  
        :type contextOccurrence: :py:class:`NXOpen.NXObject` 
        :param view: 
        :type view: :py:class:`NXOpen.View` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Display.DynamicSectionCut` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: DynamicSection = ...  # unknown typename


class TrueShadingCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection SHED objects
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX6.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateTrueShadingBuilder(self, sObj: TrueShading) -> TrueShadingBuilder:
        """
        Creates a :py:class:`NXOpen.Display.TrueShadingBuilder` object 
        if SHED is None.  
        
        Otherwise, a TrueShading object will be edited 
        
        Signature ``CreateTrueShadingBuilder(sObj)`` 
        
        :param sObj:  If SHED object is not None, then this object will be edited  
        :type sObj: :py:class:`NXOpen.Display.TrueShading` 
        :returns:  return SHED object builder  
        :rtype: :py:class:`NXOpen.Display.TrueShadingBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> TrueShading:
        """
        Finds the :py:class:`NXOpen.Display.TrueShading` with the given identifier
        as recorded in a journal.  
        
        An object may not return the same value as its 
        JournalIdentifier in different versions of the software. However newer versions 
        of the software should find the same object when FindObject is passed older versions 
        of its journal identifier. In general, this method should not be used in handwritten
        code and exists to support record and playback of journals.
        
        An exception will be thrown if no object found with the given journal identifier. 
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  SHED object found  
        :rtype: :py:class:`NXOpen.Display.TrueShading` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    


class TransientTextViewTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransientTextViewType():
    """
    the view or views in which the transient text is to be displayed.  Note that this
    property is only used when the view property is other than None. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "WorkViewOnly", " - "
       "AllActiveViews", " - "
       "ViewOfLastCursor", " - "
       "AllViewsButDrawing", " - "
       "AllActiveMemberViews", " - "
       "FirstViewFound", " - "
    """
    WorkViewOnly = 0  # TransientTextViewTypeMemberType
    AllActiveViews = 1  # TransientTextViewTypeMemberType
    ViewOfLastCursor = 2  # TransientTextViewTypeMemberType
    AllViewsButDrawing = 3  # TransientTextViewTypeMemberType
    AllActiveMemberViews = 4  # TransientTextViewTypeMemberType
    FirstViewFound = 5  # TransientTextViewTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TransientTextStandardTextRefMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransientTextStandardTextRef():
    """
    This enumerated type specifies the type of reference point used in the text box
    for standard_text methods. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SystemDefault", "Display the text using the system default reference point position"
       "BaselineStart", "Display the text starting on the baseline, at the left end of the text box for left-to-right text, or at the right end of the text box for right-to-left text"
       "BaselineCenter", "Display the text with the given position in the horizontal center of the text box at the baseline"
       "BaselineEnd", "Display the text starting on the baseline, at the right end of the text box for left-to-right text, or at the left end of the text box for right-to-left text"
       "TopLeft", "Display the text with the given position in the top left of the text box"
       "TopCenter", "Display the text with the given position in the top center of the text box"
       "TopRight", "Display the text with the given position in the top right of the text box"
       "MiddleLeft", "Display the text with the given position in the middle left of the text box"
       "MiddleCenter", "Display the text with the given position in middle center of text box"
       "MiddleRight", "Display the text with the given position in middle right of text box"
       "BottomLeft", "Display the text with the given position in bottom left of text box"
       "BottomCenter", "Display the text with the given position in bottom center of text box"
       "BottomRight", "Display the text with the given position in bottom right of text box"
    """
    SystemDefault = 0  # TransientTextStandardTextRefMemberType
    BaselineStart = 0  # TransientTextStandardTextRefMemberType
    BaselineCenter = 1  # TransientTextStandardTextRefMemberType
    BaselineEnd = 2  # TransientTextStandardTextRefMemberType
    TopLeft = 3  # TransientTextStandardTextRefMemberType
    TopCenter = 4  # TransientTextStandardTextRefMemberType
    TopRight = 5  # TransientTextStandardTextRefMemberType
    MiddleLeft = 6  # TransientTextStandardTextRefMemberType
    MiddleCenter = 7  # TransientTextStandardTextRefMemberType
    MiddleRight = 8  # TransientTextStandardTextRefMemberType
    BottomLeft = 9  # TransientTextStandardTextRefMemberType
    BottomCenter = 10  # TransientTextStandardTextRefMemberType
    BottomRight = 11  # TransientTextStandardTextRefMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TransientTextTextSizeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransientTextTextSize():
    """
    Provides a way to specify the size of the desired text, as small,
    medium or large (normal is a synonym for medium). 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Small", " - "
       "Normal", " - "
       "Medium", " - "
       "Large", " - "
       "NumSizes", " - "
    """
    Small = 0  # TransientTextTextSizeMemberType
    Normal = 1  # TransientTextTextSizeMemberType
    Medium = 1  # TransientTextTextSizeMemberType
    Large = 2  # TransientTextTextSizeMemberType
    NumSizes = 3  # TransientTextTextSizeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TransientText(NXOpen.TransientObject):
    """
    Represents temporary text strings which can be used for Temporary Display   
    
    .. versionadded:: NX8.0.0
    """
    
    class ViewType():
        """
        the view or views in which the transient text is to be displayed.  Note that this
        property is only used when the view property is other than None. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "WorkViewOnly", " - "
           "AllActiveViews", " - "
           "ViewOfLastCursor", " - "
           "AllViewsButDrawing", " - "
           "AllActiveMemberViews", " - "
           "FirstViewFound", " - "
        """
        WorkViewOnly = 0  # TransientTextViewTypeMemberType
        AllActiveViews = 1  # TransientTextViewTypeMemberType
        ViewOfLastCursor = 2  # TransientTextViewTypeMemberType
        AllViewsButDrawing = 3  # TransientTextViewTypeMemberType
        AllActiveMemberViews = 4  # TransientTextViewTypeMemberType
        FirstViewFound = 5  # TransientTextViewTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class StandardTextRef():
        """
        This enumerated type specifies the type of reference point used in the text box
        for standard_text methods. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SystemDefault", "Display the text using the system default reference point position"
           "BaselineStart", "Display the text starting on the baseline, at the left end of the text box for left-to-right text, or at the right end of the text box for right-to-left text"
           "BaselineCenter", "Display the text with the given position in the horizontal center of the text box at the baseline"
           "BaselineEnd", "Display the text starting on the baseline, at the right end of the text box for left-to-right text, or at the left end of the text box for right-to-left text"
           "TopLeft", "Display the text with the given position in the top left of the text box"
           "TopCenter", "Display the text with the given position in the top center of the text box"
           "TopRight", "Display the text with the given position in the top right of the text box"
           "MiddleLeft", "Display the text with the given position in the middle left of the text box"
           "MiddleCenter", "Display the text with the given position in middle center of text box"
           "MiddleRight", "Display the text with the given position in middle right of text box"
           "BottomLeft", "Display the text with the given position in bottom left of text box"
           "BottomCenter", "Display the text with the given position in bottom center of text box"
           "BottomRight", "Display the text with the given position in bottom right of text box"
        """
        SystemDefault = 0  # TransientTextStandardTextRefMemberType
        BaselineStart = 0  # TransientTextStandardTextRefMemberType
        BaselineCenter = 1  # TransientTextStandardTextRefMemberType
        BaselineEnd = 2  # TransientTextStandardTextRefMemberType
        TopLeft = 3  # TransientTextStandardTextRefMemberType
        TopCenter = 4  # TransientTextStandardTextRefMemberType
        TopRight = 5  # TransientTextStandardTextRefMemberType
        MiddleLeft = 6  # TransientTextStandardTextRefMemberType
        MiddleCenter = 7  # TransientTextStandardTextRefMemberType
        MiddleRight = 8  # TransientTextStandardTextRefMemberType
        BottomLeft = 9  # TransientTextStandardTextRefMemberType
        BottomCenter = 10  # TransientTextStandardTextRefMemberType
        BottomRight = 11  # TransientTextStandardTextRefMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TextSize():
        """
        Provides a way to specify the size of the desired text, as small,
        medium or large (normal is a synonym for medium). 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Small", " - "
           "Normal", " - "
           "Medium", " - "
           "Large", " - "
           "NumSizes", " - "
        """
        Small = 0  # TransientTextTextSizeMemberType
        Normal = 1  # TransientTextTextSizeMemberType
        Medium = 1  # TransientTextTextSizeMemberType
        Large = 2  # TransientTextTextSizeMemberType
        NumSizes = 3  # TransientTextTextSizeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayTemporaryAbsoluteGeometry(self, fontIndex: int, view: NXOpen.View, viewType: TransientTextViewType, object: NXOpen.DisplayableObject, position: NXOpen.Point3d) -> None:
        """
        Displays text as temporary display using absolute geometry.  
        
        Insure that
        you have set all needed properties before using this method.  Note that
        the text will be displayed on the Absolute XY plane. 
        
        Signature ``DisplayTemporaryAbsoluteGeometry(fontIndex, view, viewType, object, position)`` 
        
        :param fontIndex:  The index of the font to be used.  This may                                                           be 0, which means to use the default font.  
        :type fontIndex: int 
        :param view:  The view in which to display the text.                                                           This may be None, in which case the                                                           viewType argument is used.  
        :type view: :py:class:`NXOpen.View` 
        :param viewType:  Used only when view is None.  
        :type viewType: :py:class:`NXOpen.Display.TransientTextViewType` 
        :param object:  May be None, in which case the                                                                 text will be drawn at the given position.                                                                 If not None, draw the text at the                                                                 attention point of object.  
        :type object: :py:class:`NXOpen.DisplayableObject` 
        :param position:  In Absolute Coordinates  
        :type position: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayTemporaryScreenGeometry(self, fontIndex: int, view: NXOpen.View, viewType: TransientTextViewType, object: NXOpen.DisplayableObject, position: NXOpen.Point3d) -> None:
        """
        Displays text as temporary display using screen geometry.  
        
        Insure that
        you have set all needed properties before using this method.  This method
        is not supported for 2D output such as CGM.  Note that the text will be displayed
        on the Absolute XY plane. 
        
        Signature ``DisplayTemporaryScreenGeometry(fontIndex, view, viewType, object, position)`` 
        
        :param fontIndex:  The index of the font to be used.  This may                                                           be 0, which means to use the default font.  
        :type fontIndex: int 
        :param view:  The view in which to display the text.                                                           This may be None, in which case the                                                           viewType argument is used.  
        :type view: :py:class:`NXOpen.View` 
        :param viewType:  Used only when view is None.  
        :type viewType: :py:class:`NXOpen.Display.TransientTextViewType` 
        :param object:  May be None, in which case the                                                                      text will be drawn at the given position.                                                                      If not None, draw the text at the                                                                      attention point of object.  
        :type object: :py:class:`NXOpen.DisplayableObject` 
        :param position:  In Absolute Coordinates  
        :type position: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayTemporaryAbsRotScreenSizeGeometry(self, fontIndex: int, view: NXOpen.View, viewType: TransientTextViewType, object: NXOpen.DisplayableObject, position: NXOpen.Point3d) -> None:
        """
        Displays text as temporary display using screen geometry but with rotation
        defined in absolute space.  
        
        The text will be displayed on the XY plane of
        the absolute coordinate system.  Insure that you have set all needed properties
        before using this method.  This method is not supported for 2D output such as CGM. 
        
        Signature ``DisplayTemporaryAbsRotScreenSizeGeometry(fontIndex, view, viewType, object, position)`` 
        
        :param fontIndex:  The index of the font to be used.  This may                                                           be 0, which means to use the default font.  
        :type fontIndex: int 
        :param view:  The view in which to display the text.                                                           This may be None, in which case the                                                           viewType argument is used.  
        :type view: :py:class:`NXOpen.View` 
        :param viewType:  Used only when view is None.  
        :type viewType: :py:class:`NXOpen.Display.TransientTextViewType` 
        :param object:  May be None, in which case the                                                                      text will be drawn at the given position.                                                                      If not None, draw the text at the                                                                      attention point of object.  
        :type object: :py:class:`NXOpen.DisplayableObject` 
        :param position:  In Absolute Coordinates  
        :type position: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddTextString(self, textString: str) -> None:
        """
        Adds a text string to the TransientText object.  
        
        A TransientText object
        may have one or more text strings.  If an attempt is made to display
        a TransientText object with zero text strings, an error will be returned. 
        
        Signature ``AddTextString(textString)`` 
        
        :param textString: 
        :type textString: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAbsoluteTextSize(self) -> tuple:
        """
        Returns the size of the text, in absolute coordinate, in units of the displayed part.  
        
        These values are only only used by
        :py:meth:`Display.TransientText.DisplayTemporaryAbsoluteGeometry`. 
        
        Signature ``GetAbsoluteTextSize()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (glyphWidth, glyphHeight). glyphWidth is a float. glyphHeight is a float. 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAbsoluteTextSize(self, glyphWidth: float, glyphHeight: float) -> None:
        """
        Sets the size of the text, in absolute coordinates, in units of the displayed part.  
        
        These values are only used by
        :py:meth:`Display.TransientText.DisplayTemporaryAbsoluteGeometry`.
        
        Signature ``SetAbsoluteTextSize(glyphWidth, glyphHeight)`` 
        
        :param glyphWidth: 
        :type glyphWidth: float 
        :param glyphHeight: 
        :type glyphHeight: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    Color: int = ...
    """
    Returns or sets  the index of the color to be used to display the transient text.  
    
    If not specified,
    the System Color will be used. 
    
    <hr>
    
    Getter Method
    
    Signature ``Color`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Color`` 
    
    :param colorIndex: 
    :type colorIndex: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    FontStyle: str = ...
    """
    Returns or sets   the style of font to be used to display the transient text.  
    
    Every text font has at least
    one style.  To determine which styles a font has, use UF_UGFONT_ask_font_styles.
    If not specified, the default font style for the font will be used.
    
    <hr>
    
    Getter Method
    
    Signature ``FontStyle`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FontStyle`` 
    
    :param fontStyle: 
    :type fontStyle: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ReferencePositionType: TransientTextStandardTextRef = ...
    """
    Returns or sets  the position of the text relative to positions on the text box 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferencePositionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TransientTextStandardTextRef` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferencePositionType`` 
    
    :param referencePositionType: 
    :type referencePositionType: :py:class:`NXOpen.Display.TransientTextStandardTextRef` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ScreenTextSize: TransientTextTextSize = ...
    """
    Returns or sets  the approximate size of the text (small, mendium, large) as measured on
    the graphics screen.  
    
    This property is not used by
    :py:meth:`Display.TransientText.DisplayTemporaryAbsoluteGeometry`. 
    
    <hr>
    
    Getter Method
    
    Signature ``ScreenTextSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TransientTextTextSize` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScreenTextSize`` 
    
    :param textSize: 
    :type textSize: :py:class:`NXOpen.Display.TransientTextTextSize` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """


class GridCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of plane grid objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX6.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreatePlaneGridBuilder(self, grid: PlaneGrid) -> PlaneGridBuilder:
        """
        Creates a :py:class:`NXOpen.Display.PlaneGridBuilder` object
        used to build a bounded grid on a plane.  
        
        If the grid is not None, the planar grid object will be edited.
        
        Signature ``CreatePlaneGridBuilder(grid)`` 
        
        :param grid:  If grid is not None,                                                                                   then this object will be                                                                                   edited  
        :type grid: :py:class:`NXOpen.Display.PlaneGrid` 
        :returns:  plane grid builder  
        :rtype: :py:class:`NXOpen.Display.PlaneGridBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateDatumPlaneGridBuilder(self, grid: DatumPlaneGrid) -> DatumPlaneGridBuilder:
        """
        Creates a :py:class:`NXOpen.Display.DatumPlaneGridBuilder` object
        used to edit the supplied datum plane grid.
        
        Signature ``CreateDatumPlaneGridBuilder(grid)`` 
        
        :param grid:  If grid is not None,                                                                                             then this object will be                                                                                             edited  
        :type grid: :py:class:`NXOpen.Display.DatumPlaneGrid` 
        :returns:  datum plane grid builder  
        :rtype: :py:class:`NXOpen.Display.DatumPlaneGridBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateDatumPlaneGridBuilder(self, datumPlanes: 'list[NXOpen.DatumPlane]') -> DatumPlaneGridBuilder:
        """
        Creates a :py:class:`NXOpen.Display.DatumPlaneGridBuilder` object 
        used to build datum plane grids based on the supplied datum plane list.
        
        Signature ``CreateDatumPlaneGridBuilder(datumPlanes)`` 
        
        :param datumPlanes:  datum plane list  
        :type datumPlanes: list of :py:class:`NXOpen.DatumPlane` 
        :returns:  datum plane grid builder  
        :rtype: :py:class:`NXOpen.Display.DatumPlaneGridBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Grid:
        """
        Finds the :py:class:`NXOpen.Display.Grid` with the given identifier  
        as recorded in a journal.  
        
        An object may not return the same value as 
        its JournalIdentifier in different versions of the software. However  
        newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In 
        general,this method should not be used in handwritten code and exists 
        to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given 
        journal identifier. 
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  Grid found  
        :rtype: :py:class:`NXOpen.Display.Grid` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDatumPlaneGrid(self, datumPlane: NXOpen.DatumPlane) -> DatumPlaneGrid:
        """
        Finds the datum grid associated with the specified datum plane.  
        
        Signature ``GetDatumPlaneGrid(datumPlane)`` 
        
        :param datumPlane:  datum plane  
        :type datumPlane: :py:class:`NXOpen.DatumPlane` 
        :returns:  Datum plane grid. None indicates no grid is associated
        with the datum plane.  
        :rtype: :py:class:`NXOpen.Display.DatumPlaneGrid` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreatePlanarShipGridBuilder(self, grid: PlanarShipGrid) -> PlanarShipGridBuilder:
        """
        Creates a :py:class:`NXOpen.Display.PlanarShipGridBuilder` object
        used to build a planar ship grid on a datum plane.  
        
        If the grid is not None, the planar ship grid object will be edited.
        
        Signature ``CreatePlanarShipGridBuilder(grid)`` 
        
        :param grid:  If grid is not None,                                                                                                         this object will be edited  
        :type grid: :py:class:`NXOpen.Display.PlanarShipGrid` 
        :returns:  planar ship grid builder  
        :rtype: :py:class:`NXOpen.Display.PlanarShipGridBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_concept ("Ship Concept")
        """
        ...
    


class TrueStudioBuilderGlobalMaterialMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TrueStudioBuilderGlobalMaterial():
    """
    Types of True Studio Global Material display.  This material is displayed on objects when no other material has been applied. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PlasticColorwash", "Uses the object's color with plastic material characteristics."
       "ShinyMetalColorwash", "Uses the object's color with shiny metal material characteristics."
       "Clay", "Overrides the object color with a clay material display."
       "Plasticine", "Overrides the object color with a plasticine material display."
       "Chrome", "Overrides the object color with a chrome material display."
    """
    PlasticColorwash = 0  # TrueStudioBuilderGlobalMaterialMemberType
    ShinyMetalColorwash = 1  # TrueStudioBuilderGlobalMaterialMemberType
    Clay = 2  # TrueStudioBuilderGlobalMaterialMemberType
    Plasticine = 3  # TrueStudioBuilderGlobalMaterialMemberType
    Chrome = 4  # TrueStudioBuilderGlobalMaterialMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TrueStudioBuilderRenderMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TrueStudioBuilderRenderMethod():
    """
    Types of True Studio Render Methods.  The render method is used to specify display quality or real-time performance 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FullRender", "All rendering effects are honored."
       "ImprovedRender", "Some rendering effects are not honored. Can be faster than Full Render."
       "PreviewRender", "Many rendering effects are not honored. Faster than Full and Improved Render."
    """
    FullRender = 0  # TrueStudioBuilderRenderMethodMemberType
    ImprovedRender = 1  # TrueStudioBuilderRenderMethodMemberType
    PreviewRender = 2  # TrueStudioBuilderRenderMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TrueStudioBuilder(NXOpen.Builder):
    """
    The TrueStudioBuillder manages Advanced Studio visualization display   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Display.TrueStudioCollection.CreateTrueStudioBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    class GlobalMaterial():
        """
        Types of True Studio Global Material display.  This material is displayed on objects when no other material has been applied. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PlasticColorwash", "Uses the object's color with plastic material characteristics."
           "ShinyMetalColorwash", "Uses the object's color with shiny metal material characteristics."
           "Clay", "Overrides the object color with a clay material display."
           "Plasticine", "Overrides the object color with a plasticine material display."
           "Chrome", "Overrides the object color with a chrome material display."
        """
        PlasticColorwash = 0  # TrueStudioBuilderGlobalMaterialMemberType
        ShinyMetalColorwash = 1  # TrueStudioBuilderGlobalMaterialMemberType
        Clay = 2  # TrueStudioBuilderGlobalMaterialMemberType
        Plasticine = 3  # TrueStudioBuilderGlobalMaterialMemberType
        Chrome = 4  # TrueStudioBuilderGlobalMaterialMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class RenderMethod():
        """
        Types of True Studio Render Methods.  The render method is used to specify display quality or real-time performance 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FullRender", "All rendering effects are honored."
           "ImprovedRender", "Some rendering effects are not honored. Can be faster than Full Render."
           "PreviewRender", "Many rendering effects are not honored. Faster than Full and Improved Render."
        """
        FullRender = 0  # TrueStudioBuilderRenderMethodMemberType
        ImprovedRender = 1  # TrueStudioBuilderRenderMethodMemberType
        PreviewRender = 2  # TrueStudioBuilderRenderMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    GlobalMaterialType: TrueStudioBuilderGlobalMaterial = ...
    """
    Returns or sets  the Global Material Type is used in Advanced Studio display when no material has been applied to the object.  
    
    <hr>
    
    Getter Method
    
    Signature ``GlobalMaterialType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TrueStudioBuilderGlobalMaterial` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GlobalMaterialType`` 
    
    :param globalMaterialType: 
    :type globalMaterialType: :py:class:`NXOpen.Display.TrueStudioBuilderGlobalMaterial` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ModeToggle: bool = ...
    """
    Returns or sets  the Mode Toggle controls whether Advanced Studio display is enabled.  
    
    <hr>
    
    Getter Method
    
    Signature ``ModeToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ModeToggle`` 
    
    :param modeToggle: 
    :type modeToggle: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    RenderMethodType: TrueStudioBuilderRenderMethod = ...
    """
    Returns or sets  the Render Method Type is used in Advanced Studio display to control the display quality and performance 
    
    <hr>
    
    Getter Method
    
    Signature ``RenderMethodType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TrueStudioBuilderRenderMethod` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RenderMethodType`` 
    
    :param renderMethodType: 
    :type renderMethodType: :py:class:`NXOpen.Display.TrueStudioBuilderRenderMethod` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: TrueStudioBuilder = ...  # unknown typename


class ImageBase(NXOpen.DisplayableObject):
    """
    Represents a :py:class:`NXOpen.Display.ImageBase` that provides  
    definition, orientation, sizing, and display setting controls for image 
    based objects.  
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX9.0.0
    """
    Null: ImageBase = ...  # unknown typename


class EntitySelectionPlane(NXOpen.DisplayableObject):
    """
    Represents a grid on a datum plane   
    
    Entity selection planes are not supported in KF.
    
    .. versionadded:: NX8.0.0
    """
    Null: EntitySelectionPlane = ...  # unknown typename


class PlanarShipGrid(EntitySelectionPlane):
    """
    Represents a planar ship grid.  
    
    Planar ship grid is not supported in KF.
    
    .. versionadded:: NX8.0.0
    """
    
    def IsDatumPlaneInGrid(self, datumplaneTag: NXOpen.DatumPlane) -> bool:
        """
        Returns the flag to indicate whether the specific datum plane is in grid or not.  
        
        Signature ``IsDatumPlaneInGrid(datumplaneTag)`` 
        
        :param datumplaneTag: 
        :type datumplaneTag: :py:class:`NXOpen.DatumPlane` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_concept ("Ship Concept")
        """
        ...
    
    
    def AddDatumPlanes(self, datumplaneTags: 'list[NXOpen.DatumPlane]') -> None:
        """
        Adds intersected datum planes into the planar grid.  
        
        Signature ``AddDatumPlanes(datumplaneTags)`` 
        
        :param datumplaneTags:  Array of datum planes  
        :type datumplaneTags: list of :py:class:`NXOpen.DatumPlane` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_concept ("Ship Concept")
        """
        ...
    
    
    def RemoveDatumPlanes(self, datumplaneTags: 'list[NXOpen.DatumPlane]') -> None:
        """
        Removes the specific datum planes from the planar grid.  
        
        Signature ``RemoveDatumPlanes(datumplaneTags)`` 
        
        :param datumplaneTags:  Array of datum planes  
        :type datumplaneTags: list of :py:class:`NXOpen.DatumPlane` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_concept ("Ship Concept")
        """
        ...
    
    Null: PlanarShipGrid = ...  # unknown typename


class WallMaterialTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WallMaterialType():
    """
    Defines the material characteristics of a stage wall.
    
    .. deprecated::  NX10.0.0
       Use :py:class:`NXOpen.Display.WallWallMaterialTextureType` instead.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ShadowCatcher", "The wall is transparent, and is used to display shadows. Use this to cast shadows onto a "virtual" background image of an environment."
       "Reflective", "The wall is reflective. For example, use this on a "bottom" wall to display a shiny floor."
       "Invisible", "The wall is not displayed. For example, use this on all the walls except the "bottom" if you only need to display a floor."
    """
    ShadowCatcher = 0  # WallMaterialTypeMemberType
    Reflective = 1  # WallMaterialTypeMemberType
    Invisible = 2  # WallMaterialTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class WallMaterialTextureTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WallMaterialTextureType():
    """
    the new wall material texture type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ShadowCatcher", "The wall is transparent, and is used to display shadows. Use this to cast shadows onto a "virtual" background image of an environment."
       "ImageFile", "The wall uses image for tiling. For example, use this on a "bottom" wall to display a tiled shiny floor."
       "Invisible", "The wall is not displayed. For example, use this on all the walls except the "bottom" if you only need to display a floor."
    """
    ShadowCatcher = 0  # WallMaterialTextureTypeMemberType
    ImageFile = 1  # WallMaterialTextureTypeMemberType
    Invisible = 2  # WallMaterialTextureTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Wall(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.Wall`
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateWall`
    
    .. versionadded:: NX5.0.0
    """
    
    class MaterialType():
        """
        Defines the material characteristics of a stage wall.
        
        .. deprecated::  NX10.0.0
           Use :py:class:`NXOpen.Display.WallWallMaterialTextureType` instead.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ShadowCatcher", "The wall is transparent, and is used to display shadows. Use this to cast shadows onto a "virtual" background image of an environment."
           "Reflective", "The wall is reflective. For example, use this on a "bottom" wall to display a shiny floor."
           "Invisible", "The wall is not displayed. For example, use this on all the walls except the "bottom" if you only need to display a floor."
        """
        ShadowCatcher = 0  # WallMaterialTypeMemberType
        Reflective = 1  # WallMaterialTypeMemberType
        Invisible = 2  # WallMaterialTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class MaterialTextureType():
        """
        the new wall material texture type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ShadowCatcher", "The wall is transparent, and is used to display shadows. Use this to cast shadows onto a "virtual" background image of an environment."
           "ImageFile", "The wall uses image for tiling. For example, use this on a "bottom" wall to display a tiled shiny floor."
           "Invisible", "The wall is not displayed. For example, use this on all the walls except the "bottom" if you only need to display a floor."
        """
        ShadowCatcher = 0  # WallMaterialTextureTypeMemberType
        ImageFile = 1  # WallMaterialTextureTypeMemberType
        Invisible = 2  # WallMaterialTextureTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Image: Image = ...
    """
    Returns or sets  the walls's image builder 
    
    <hr>
    
    Getter Method
    
    Signature ``Image`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Image`` 
    
    :param imageBuilder: 
    :type imageBuilder: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ImageFilename: str = ...
    """
    Returns or sets  the stage wall's image filename 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageFilename`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageFilename`` 
    
    :param newImageFileName: 
    :type newImageFileName: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    PatternRepeatFactor: float = ...
    """
    Returns or sets  the pattern repeat factor - the number of times the image repeats 
    
    <hr>
    
    Getter Method
    
    Signature ``PatternRepeatFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX10.0.0
       This functionality is moved to :py:class:`NXOpen.Display.Image`.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PatternRepeatFactor`` 
    
    :param patternRepeatFactor: 
    :type patternRepeatFactor: float 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX10.0.0
       This functionality is moved to :py:class:`NXOpen.Display.Image`.
    
    License requirements: None.
    """
    Reflectivity: float = ...
    """
    Returns or sets  the reflectivity of a wall - the percentage of the environment reflected off of the wall 
    
    <hr>
    
    Getter Method
    
    Signature ``Reflectivity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Reflectivity`` 
    
    :param reflectivity: 
    :type reflectivity: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    WallMaterialTextureType: WallMaterialTextureType = ...
    """
    Returns or sets  the wall material texture type - either shadow_catcher, image file, or invisible 
    
    <hr>
    
    Getter Method
    
    Signature ``WallMaterialTextureType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.WallMaterialTextureType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WallMaterialTextureType`` 
    
    :param wallMaterialType: 
    :type wallMaterialType: :py:class:`NXOpen.Display.WallMaterialTextureType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    WallMaterialType: WallMaterialType = ...
    """
    Returns or sets  the wall material type - either shadow_catcher, reflective, or invisible 
    
    <hr>
    
    Getter Method
    
    Signature ``WallMaterialType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.WallMaterialType` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`NXOpen.Display.Wall.WallMaterialTextureType`` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WallMaterialType`` 
    
    :param wallMaterialType: 
    :type wallMaterialType: :py:class:`NXOpen.Display.WallMaterialType` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`NXOpen.Display.Wall.WallMaterialTextureType`` instead.
    
    License requirements: None.
    """
    Null: Wall = ...  # unknown typename


class TrueStudioCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection TrueStudio objects
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX6.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateTrueStudioBuilder(self, sObj: TrueStudio) -> TrueStudioBuilder:
        """
        Creates a :py:class:`NXOpen.Display.TrueStudioBuilder` object 
        if TrueStudio is None.  
        
        Otherwise, a TrueStudio object will be edited 
        
        Signature ``CreateTrueStudioBuilder(sObj)`` 
        
        :param sObj:  If TrueStudio object is not None, then this object will be edited  
        :type sObj: :py:class:`NXOpen.Display.TrueStudio` 
        :returns:  return TrueStudio object builder  
        :rtype: :py:class:`NXOpen.Display.TrueStudioBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> TrueStudio:
        """
        Finds the :py:class:`NXOpen.Display.TrueStudio` with the given identifier
        as recorded in a journal.  
        
        An object may not return the same value as its 
        JournalIdentifier in different versions of the software. However newer versions 
        of the software should find the same object when FindObject is passed older versions 
        of its journal identifier. In general, this method should not be used in handwritten
        code and exists to support record and playback of journals.
        
        An exception will be thrown if no object found with the given journal identifier. 
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  TrueStudio object found  
        :rtype: :py:class:`NXOpen.Display.TrueStudio` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    


class DynamicSectionTypesActivePlaneMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DynamicSectionTypesActivePlane():
    """
    Specifies active clip plane in the active plane pair.
    This is used in "Two Parallel Planes" and "Box" type Sections.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Primary", "Primary"
       "Secondary", "Secondary"
    """
    Primary = 0  # DynamicSectionTypesActivePlaneMemberType
    Secondary = 1  # DynamicSectionTypesActivePlaneMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DynamicSectionTypesAxisMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DynamicSectionTypesAxis():
    """
    Specifies axis. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Arbitrary axis"
       "X", "X axis"
       "Y", "Y axis"
       "Z", "Z axis"
    """
    NotSet = 0  # DynamicSectionTypesAxisMemberType
    X = 1  # DynamicSectionTypesAxisMemberType
    Y = 2  # DynamicSectionTypesAxisMemberType
    Z = 3  # DynamicSectionTypesAxisMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DynamicSectionTypesCapColorOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DynamicSectionTypesCapColorOption():
    """
    Specifies cap color type to be used for the cap. When
    cap color type is body, then user-specified color is ignored.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Body", "Use body color"
       "Any", "User-specified color is used"
    """
    Body = 0  # DynamicSectionTypesCapColorOptionMemberType
    Any = 1  # DynamicSectionTypesCapColorOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DynamicSectionTypesClipMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DynamicSectionTypesClip():
    """
    Specifies clipping type. 
    The "Slice" type is only available for "One Plane" section.
    "Section" will clip data that lies on the opposite side of 
    the plane normal of the clipping plane.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Section", "One sided clip"
       "Slice", "Slice type clip"
    """
    Section = 0  # DynamicSectionTypesClipMemberType
    Slice = 1  # DynamicSectionTypesClipMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DynamicSectionTypesCoordinateSystemMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DynamicSectionTypesCoordinateSystem():
    """
    Specifies the coordinate system used for creating
    principal planes i.e. X, Y, Z planes. Note that the 
    coordinate system is only used during plane creation to
    set initial reference. When using WCS, the X plane will
    be created such that its normal aligns with WCS X direction.
    
    All APIs that accept/receive geometric works in absolute
    coordinates.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Absolute", "Absolute"
       "Wcs", "WCS"
    """
    Absolute = 0  # DynamicSectionTypesCoordinateSystemMemberType
    Wcs = 1  # DynamicSectionTypesCoordinateSystemMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DynamicSectionTypesCurveColorOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DynamicSectionTypesCurveColorOption():
    """
    Specifies the color of the curves created by the
    section plane. When color is set to body color, user
    specified color will be ignored.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Body", "Use body color"
       "Any", "Use specified color"
    """
    Body = 0  # DynamicSectionTypesCurveColorOptionMemberType
    Any = 1  # DynamicSectionTypesCurveColorOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DynamicSectionTypesTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DynamicSectionTypesType():
    """
    Specifies different type of sectioning. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "OnePlane", "One plane section"
       "TwoParallelPlanes", "Two parallel plane section"
       "Box", "Box section"
    """
    OnePlane = 0  # DynamicSectionTypesTypeMemberType
    TwoParallelPlanes = 1  # DynamicSectionTypesTypeMemberType
    Box = 2  # DynamicSectionTypesTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DynamicSectionTypes():
    """
    Represents a enumerations used by Dynamic Section Builder.  
    
    No Creator since it only includes enums
    
    .. versionadded:: NX5.0.0
    """
    
    class ActivePlane():
        """
        Specifies active clip plane in the active plane pair.
        This is used in "Two Parallel Planes" and "Box" type Sections.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Primary", "Primary"
           "Secondary", "Secondary"
        """
        Primary = 0  # DynamicSectionTypesActivePlaneMemberType
        Secondary = 1  # DynamicSectionTypesActivePlaneMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Axis():
        """
        Specifies axis. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Arbitrary axis"
           "X", "X axis"
           "Y", "Y axis"
           "Z", "Z axis"
        """
        NotSet = 0  # DynamicSectionTypesAxisMemberType
        X = 1  # DynamicSectionTypesAxisMemberType
        Y = 2  # DynamicSectionTypesAxisMemberType
        Z = 3  # DynamicSectionTypesAxisMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CapColorOption():
        """
        Specifies cap color type to be used for the cap. When
        cap color type is body, then user-specified color is ignored.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Body", "Use body color"
           "Any", "User-specified color is used"
        """
        Body = 0  # DynamicSectionTypesCapColorOptionMemberType
        Any = 1  # DynamicSectionTypesCapColorOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Clip():
        """
        Specifies clipping type. 
        The "Slice" type is only available for "One Plane" section.
        "Section" will clip data that lies on the opposite side of 
        the plane normal of the clipping plane.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Section", "One sided clip"
           "Slice", "Slice type clip"
        """
        Section = 0  # DynamicSectionTypesClipMemberType
        Slice = 1  # DynamicSectionTypesClipMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CoordinateSystem():
        """
        Specifies the coordinate system used for creating
        principal planes i.e. X, Y, Z planes. Note that the 
        coordinate system is only used during plane creation to
        set initial reference. When using WCS, the X plane will
        be created such that its normal aligns with WCS X direction.
        
        All APIs that accept/receive geometric works in absolute
        coordinates.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Absolute", "Absolute"
           "Wcs", "WCS"
        """
        Absolute = 0  # DynamicSectionTypesCoordinateSystemMemberType
        Wcs = 1  # DynamicSectionTypesCoordinateSystemMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CurveColorOption():
        """
        Specifies the color of the curves created by the
        section plane. When color is set to body color, user
        specified color will be ignored.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Body", "Use body color"
           "Any", "Use specified color"
        """
        Body = 0  # DynamicSectionTypesCurveColorOptionMemberType
        Any = 1  # DynamicSectionTypesCurveColorOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Type():
        """
        Specifies different type of sectioning. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "OnePlane", "One plane section"
           "TwoParallelPlanes", "Two parallel plane section"
           "Box", "Box section"
        """
        OnePlane = 0  # DynamicSectionTypesTypeMemberType
        TwoParallelPlanes = 1  # DynamicSectionTypesTypeMemberType
        Box = 2  # DynamicSectionTypesTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    


class RayTracedStudioBuilderStationaryDisplayQualityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioBuilderStationaryDisplayQualityType():
    """
    To specify the quality and performance of the Ray Traced Studio display. 
    In the RTRT stationary mode, when dynamic interaction stops, these are High. Medium, and Low options.
    In the IRay+ dynamci rendering mode, these become Photoreal, Qualtiy Interactive, and Fast Interactive options.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "High", "Very good ray traced display quality (Photoreal for Iray+)"
       "Medium", "Good ray traced display quality with good performance (Qualtiy Interactive for Iray+)"
       "Low", "The fastest ray traced display performance with preview quality (Fast Interactive for Iray+)"
    """
    High = 0  # RayTracedStudioBuilderStationaryDisplayQualityTypeMemberType
    Medium = 1  # RayTracedStudioBuilderStationaryDisplayQualityTypeMemberType
    Low = 2  # RayTracedStudioBuilderStationaryDisplayQualityTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.RayTracedStudioBuilder`.  
    
    Ray Traced Studio displays CPU-based real-time ray tracing results of a model
    dynamically.
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateRayTracedStudioBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    class StationaryDisplayQualityType():
        """
        To specify the quality and performance of the Ray Traced Studio display. 
        In the RTRT stationary mode, when dynamic interaction stops, these are High. Medium, and Low options.
        In the IRay+ dynamci rendering mode, these become Photoreal, Qualtiy Interactive, and Fast Interactive options.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "High", "Very good ray traced display quality (Photoreal for Iray+)"
           "Medium", "Good ray traced display quality with good performance (Qualtiy Interactive for Iray+)"
           "Low", "The fastest ray traced display performance with preview quality (Fast Interactive for Iray+)"
        """
        High = 0  # RayTracedStudioBuilderStationaryDisplayQualityTypeMemberType
        Medium = 1  # RayTracedStudioBuilderStationaryDisplayQualityTypeMemberType
        Low = 2  # RayTracedStudioBuilderStationaryDisplayQualityTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def UpdateRayTracedDisplay(self) -> None:
        """
        Update the Ray Traced Studio display.  
        
        Use when geometry has changed to completely regenerate the display.  
        
        Signature ``UpdateRayTracedDisplay()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def StartRayTracedDisplay(self) -> None:
        """
        Start the Ray Traced Studio display after it has been stopped using the Stop action.  
        
        Signature ``StartRayTracedDisplay()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def StopRayTracedDisplay(self) -> None:
        """
        Stop the Ray Traced Studio progressive display.  
        
        Use the Start action to re-start the display. 
        
        Signature ``StopRayTracedDisplay()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RayTracedEditor(self) -> None:
        """
        Launch the Ray Traced Studio Editor command 
        
        Signature ``RayTracedEditor()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RayTracedRenderingStart(self) -> None:
        """
        Start Ray Traced Studio static image rendering 
        
        Signature ``RayTracedRenderingStart()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RayTracedRenderingErase(self) -> None:
        """
        Erase Ray Traced Studio static (still) image from the Ray Traced Studio window 
        
        Signature ``RayTracedRenderingErase()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RayTracedRenderingSave(self) -> None:
        """
        Save a copy of the Ray Traced Studio static (still) image display from the window to an image file 
        
        Signature ``RayTracedRenderingSave()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    Brightness: float = ...
    """
    Returns or sets  the brightness for Iray Tonemap setting 
    
    <hr>
    
    Getter Method
    
    Signature ``Brightness`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``Brightness`` 
    
    :param brightness: 
    :type brightness: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    StationaryQuality: RayTracedStudioBuilderStationaryDisplayQualityType = ...
    """
    Returns or sets  the Ray Traced Studio stationary display quality when dynamic interaction stops 
    
    <hr>
    
    Getter Method
    
    Signature ``StationaryQuality`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioBuilderStationaryDisplayQualityType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StationaryQuality`` 
    
    :param stationaryQuality: 
    :type stationaryQuality: :py:class:`NXOpen.Display.RayTracedStudioBuilderStationaryDisplayQualityType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: RayTracedStudioBuilder = ...  # unknown typename


class IrayPlusMaterialAttribute(NXOpen.TaggedObject):
    """
    Represents an IrayPlus Attribute 
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    IrayPlusMaterialAttribute is not supported in KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def SetValueFromString(self, attribueValue: str) -> None:
        """
        Sets attribute's value for specific attribute object.  
        
        Users can follow the steps: 
        (1) Use :py:meth:`NXOpen.Display.IrayPlusMaterialEditorBuilder.GetComponentParameter`
        to get all the attribute objects of specific material component.
        (2)Iterate all these attribute objects. Find the specific attribute you want 
        to modify. For example user want to ReflectionColour-ColourOffset in ClearCoat layer.
        (3)Pass the attribute object and the new attribute value "1.000000000000000,
        0.000000000000000,0.000000000000000" as parameter to call this function.
        
        Signature ``SetValueFromString(attribueValue)`` 
        
        :param attribueValue: 
        :type attribueValue: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetValueAsString(self) -> str:
        """
        Gets an attribute's value as string for specific attribute object 
        The attribute object can be queried from function:
        :py:meth:`NXOpen.Display.IrayPlusMaterialEditorBuilder.GetComponentParameter`.  
        
        NOTE: The returned attribueValue TEXT should be freed (TEXT_free) by the caller.
        
        Signature ``GetValueAsString()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    ParameterName: str = ...
    """
    Returns or sets  the parameter name of specific material object.  
    
    <hr>
    
    Getter Method
    
    Signature ``ParameterName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ParameterName`` 
    
    :param parameterName: 
    :type parameterName: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: IrayPlusMaterialAttribute = ...  # unknown typename


class CameraBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CameraBuilderTypes():
    """
    the camera types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Parallel", "Parallel Projection"
       "Perspective", "Perspective Projection"
    """
    Parallel = 0  # CameraBuilderTypesMemberType
    Perspective = 1  # CameraBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CameraBuilderLensAngleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CameraBuilderLensAngle():
    """
    the way to define the field of view angle 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Stock", "Stock Lenses"
       "Fov", "Field of View"
       "Magnification", "Magnification"
    """
    Stock = 0  # CameraBuilderLensAngleMemberType
    Fov = 1  # CameraBuilderLensAngleMemberType
    Magnification = 2  # CameraBuilderLensAngleMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CameraBuilderStockLensMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CameraBuilderStockLens():
    """
    Predefined lenses: 28, 35, 50, 70, 105, 135, 210, 300mm 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "S28", "28mm"
       "S35", "35mm"
       "S50", "50mm"
       "S70", "70mm"
       "S105", "105mm"
       "S135", "135mm"
       "S210", "210mm"
       "S300", "300mm"
    """
    S28 = 0  # CameraBuilderStockLensMemberType
    S35 = 1  # CameraBuilderStockLensMemberType
    S50 = 2  # CameraBuilderStockLensMemberType
    S70 = 3  # CameraBuilderStockLensMemberType
    S105 = 4  # CameraBuilderStockLensMemberType
    S135 = 5  # CameraBuilderStockLensMemberType
    S210 = 6  # CameraBuilderStockLensMemberType
    S300 = 7  # CameraBuilderStockLensMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CameraBuilderFovMeasuredMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CameraBuilderFovMeasured():
    """
    either horizontal or vertical measure 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Horizontally", "Horizontal"
       "Vertically", "Vertical"
    """
    Horizontally = 0  # CameraBuilderFovMeasuredMemberType
    Vertically = 1  # CameraBuilderFovMeasuredMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CameraBuilderLensFlareMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CameraBuilderLensFlare():
    """
    Predefined lens flare types: Standard, 35mm, 50mm, 105mm, 
    polygonal, 35mm poly, 50mm poly, 105mm poly, spark, star 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Standard", "Standard lens"
       "S35", "35mm"
       "S50", "50mm"
       "S105", "105mm"
       "Polygonal", "polygonal"
       "P35", "35mm poly"
       "P50", "50mm poly"
       "P105", "105mm poly"
       "Spark", "spark lens"
       "Star", "star lens"
    """
    Standard = 0  # CameraBuilderLensFlareMemberType
    S35 = 1  # CameraBuilderLensFlareMemberType
    S50 = 2  # CameraBuilderLensFlareMemberType
    S105 = 3  # CameraBuilderLensFlareMemberType
    Polygonal = 4  # CameraBuilderLensFlareMemberType
    P35 = 5  # CameraBuilderLensFlareMemberType
    P50 = 6  # CameraBuilderLensFlareMemberType
    P105 = 7  # CameraBuilderLensFlareMemberType
    Spark = 8  # CameraBuilderLensFlareMemberType
    Star = 9  # CameraBuilderLensFlareMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CameraBuilderApertureMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CameraBuilderAperture():
    """
    Predefined apertures: f2.8, f5.6, f8, f11, f16, f22 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "F28", "f2.8"
       "F56", "f5.6"
       "F8", "f8"
       "F11", "f11"
       "F16", "f16"
       "F22", "f22"
    """
    F28 = 0  # CameraBuilderApertureMemberType
    F56 = 1  # CameraBuilderApertureMemberType
    F8 = 2  # CameraBuilderApertureMemberType
    F11 = 3  # CameraBuilderApertureMemberType
    F16 = 4  # CameraBuilderApertureMemberType
    F22 = 5  # CameraBuilderApertureMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CameraBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.CameraBuilder`
    
    Cameras are not supported in KF.
    
    .. versionadded:: NX5.0.0
    """
    
    class Types():
        """
        the camera types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Parallel", "Parallel Projection"
           "Perspective", "Perspective Projection"
        """
        Parallel = 0  # CameraBuilderTypesMemberType
        Perspective = 1  # CameraBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LensAngle():
        """
        the way to define the field of view angle 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Stock", "Stock Lenses"
           "Fov", "Field of View"
           "Magnification", "Magnification"
        """
        Stock = 0  # CameraBuilderLensAngleMemberType
        Fov = 1  # CameraBuilderLensAngleMemberType
        Magnification = 2  # CameraBuilderLensAngleMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class StockLens():
        """
        Predefined lenses: 28, 35, 50, 70, 105, 135, 210, 300mm 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "S28", "28mm"
           "S35", "35mm"
           "S50", "50mm"
           "S70", "70mm"
           "S105", "105mm"
           "S135", "135mm"
           "S210", "210mm"
           "S300", "300mm"
        """
        S28 = 0  # CameraBuilderStockLensMemberType
        S35 = 1  # CameraBuilderStockLensMemberType
        S50 = 2  # CameraBuilderStockLensMemberType
        S70 = 3  # CameraBuilderStockLensMemberType
        S105 = 4  # CameraBuilderStockLensMemberType
        S135 = 5  # CameraBuilderStockLensMemberType
        S210 = 6  # CameraBuilderStockLensMemberType
        S300 = 7  # CameraBuilderStockLensMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FovMeasured():
        """
        either horizontal or vertical measure 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Horizontally", "Horizontal"
           "Vertically", "Vertical"
        """
        Horizontally = 0  # CameraBuilderFovMeasuredMemberType
        Vertically = 1  # CameraBuilderFovMeasuredMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LensFlare():
        """
        Predefined lens flare types: Standard, 35mm, 50mm, 105mm, 
        polygonal, 35mm poly, 50mm poly, 105mm poly, spark, star 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Standard", "Standard lens"
           "S35", "35mm"
           "S50", "50mm"
           "S105", "105mm"
           "Polygonal", "polygonal"
           "P35", "35mm poly"
           "P50", "50mm poly"
           "P105", "105mm poly"
           "Spark", "spark lens"
           "Star", "star lens"
        """
        Standard = 0  # CameraBuilderLensFlareMemberType
        S35 = 1  # CameraBuilderLensFlareMemberType
        S50 = 2  # CameraBuilderLensFlareMemberType
        S105 = 3  # CameraBuilderLensFlareMemberType
        Polygonal = 4  # CameraBuilderLensFlareMemberType
        P35 = 5  # CameraBuilderLensFlareMemberType
        P50 = 6  # CameraBuilderLensFlareMemberType
        P105 = 7  # CameraBuilderLensFlareMemberType
        Spark = 8  # CameraBuilderLensFlareMemberType
        Star = 9  # CameraBuilderLensFlareMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Aperture():
        """
        Predefined apertures: f2.8, f5.6, f8, f11, f16, f22 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "F28", "f2.8"
           "F56", "f5.6"
           "F8", "f8"
           "F11", "f11"
           "F16", "f16"
           "F22", "f22"
        """
        F28 = 0  # CameraBuilderApertureMemberType
        F56 = 1  # CameraBuilderApertureMemberType
        F8 = 2  # CameraBuilderApertureMemberType
        F11 = 3  # CameraBuilderApertureMemberType
        F16 = 4  # CameraBuilderApertureMemberType
        F22 = 5  # CameraBuilderApertureMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    ApertureType: CameraBuilderAperture = ...
    """
    Returns or sets  the aperture 
    
    <hr>
    
    Getter Method
    
    Signature ``ApertureType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.CameraBuilderAperture` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ApertureType`` 
    
    :param apertureType: 
    :type apertureType: :py:class:`NXOpen.Display.CameraBuilderAperture` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    BackClippingDistance: float = ...
    """
    Returns or sets  the back clipping distance 
    
    <hr>
    
    Getter Method
    
    Signature ``BackClippingDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BackClippingDistance`` 
    
    :param backClippingDistance: 
    :type backClippingDistance: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CameraMatrix: NXOpen.Matrix3x3 = ...
    """
    Returns or sets  the camera rotation matrix 
    
    <hr>
    
    Getter Method
    
    Signature ``CameraMatrix`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CameraMatrix`` 
    
    :param cameraMatrix: 
    :type cameraMatrix: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CameraName: str = ...
    """
    Returns or sets  the camera name as a TEXT string.  
    
    Note that internally the camera name
    is stored as a char* string.  Any characters which cannot be
    mapped to 8-bit characters will be replaced by # characters. 
    
    <hr>
    
    Getter Method
    
    Signature ``CameraName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CameraName`` 
    
    :param cameraName: 
    :type cameraName: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CameraNameChar: str = ...
    """
    Returns or sets  the camera name as a char string 
    
    <hr>
    
    Getter Method
    
    Signature ``CameraNameChar`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CameraNameChar`` 
    
    :param cameraName: 
    :type cameraName: str 
    
    .. versionadded:: NX5.0.1
    
    License requirements: None.
    """
    CameraPosition: NXOpen.Point3d = ...
    """
    Returns or sets  the coordinates of the camera point 
    
    <hr>
    
    Getter Method
    
    Signature ``CameraPosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CameraPosition`` 
    
    :param position: 
    :type position: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    DepthOfFieldToggle: bool = ...
    """
    Returns or sets  the depth of field toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``DepthOfFieldToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DepthOfFieldToggle`` 
    
    :param depthOfFieldToggle: 
    :type depthOfFieldToggle: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    FieldOfViewAngle: float = ...
    """
    Returns or sets  the field of view angle 
    
    <hr>
    
    Getter Method
    
    Signature ``FieldOfViewAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FieldOfViewAngle`` 
    
    :param fieldOfViewAngle: 
    :type fieldOfViewAngle: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    FieldOfViewMeasured: CameraBuilderFovMeasured = ...
    """
    Returns or sets  the field of view measured 
    
    <hr>
    
    Getter Method
    
    Signature ``FieldOfViewMeasured`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.CameraBuilderFovMeasured` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FieldOfViewMeasured`` 
    
    :param fovMeasuredType: 
    :type fovMeasuredType: :py:class:`NXOpen.Display.CameraBuilderFovMeasured` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    FocalDistance: float = ...
    """
    Returns or sets  the focal distance 
    
    <hr>
    
    Getter Method
    
    Signature ``FocalDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FocalDistance`` 
    
    :param focalDistance: 
    :type focalDistance: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    FrontClippingDistance: float = ...
    """
    Returns or sets  the front clipping distance 
    
    <hr>
    
    Getter Method
    
    Signature ``FrontClippingDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FrontClippingDistance`` 
    
    :param frontClippingDistance: 
    :type frontClippingDistance: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    HiddenLensFlareToggle: bool = ...
    """
    Returns or sets  the hidden lens flare toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``HiddenLensFlareToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HiddenLensFlareToggle`` 
    
    :param hiddenLensFlareToggle: 
    :type hiddenLensFlareToggle: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    LensAngleType: CameraBuilderLensAngle = ...
    """
    Returns or sets  the lens angle 
    
    <hr>
    
    Getter Method
    
    Signature ``LensAngleType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.CameraBuilderLensAngle` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LensAngleType`` 
    
    :param lensAngleType: 
    :type lensAngleType: :py:class:`NXOpen.Display.CameraBuilderLensAngle` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    LensFlareIntensity: float = ...
    """
    Returns or sets  the lens flare intensity 
    
    <hr>
    
    Getter Method
    
    Signature ``LensFlareIntensity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LensFlareIntensity`` 
    
    :param lensFlareIntensity: 
    :type lensFlareIntensity: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    LensFlareToggle: bool = ...
    """
    Returns or sets  the lens flare toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``LensFlareToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LensFlareToggle`` 
    
    :param lensFlareToggle: 
    :type lensFlareToggle: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    LensFlareType: CameraBuilderLensFlare = ...
    """
    Returns or sets  the lens flare type 
    
    <hr>
    
    Getter Method
    
    Signature ``LensFlareType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.CameraBuilderLensFlare` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LensFlareType`` 
    
    :param lensFlareType: 
    :type lensFlareType: :py:class:`NXOpen.Display.CameraBuilderLensFlare` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Magnification: float = ...
    """
    Returns or sets  the magnification 
    
    <hr>
    
    Getter Method
    
    Signature ``Magnification`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Magnification`` 
    
    :param magnification: 
    :type magnification: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    PerspectiveDistance: float = ...
    """
    Returns or sets  the perspective distance 
    
    <hr>
    
    Getter Method
    
    Signature ``PerspectiveDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PerspectiveDistance`` 
    
    :param perspectiveDistance: 
    :type perspectiveDistance: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    StockLensType: CameraBuilderStockLens = ...
    """
    Returns or sets  the stock lens type 
    
    <hr>
    
    Getter Method
    
    Signature ``StockLensType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.CameraBuilderStockLens` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StockLensType`` 
    
    :param stockLensType: 
    :type stockLensType: :py:class:`NXOpen.Display.CameraBuilderStockLens` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    TargetMatrix: NXOpen.Matrix3x3 = ...
    """
    Returns or sets  the target point rotation matrix 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetMatrix`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetMatrix`` 
    
    :param matrix: 
    :type matrix: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    TargetPosition: NXOpen.Point3d = ...
    """
    Returns or sets  the coordinates of the target point 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetPosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetPosition`` 
    
    :param position: 
    :type position: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Type: CameraBuilderTypes = ...
    """
    Returns or sets  the camera type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.CameraBuilderTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Display.CameraBuilderTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    UseTargetPoint: bool = ...
    """
    Returns or sets  whether to use the target point 
    
    <hr>
    
    Getter Method
    
    Signature ``UseTargetPoint`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseTargetPoint`` 
    
    :param useTargetPoint: 
    :type useTargetPoint: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: CameraBuilder = ...  # unknown typename


class Image(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.Image`
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateImage`
    
    .. versionadded:: NX5.0.0
    """
    
    def ImageFileSelect(self) -> None:
        """
        Gets an image file using file selection.  
        
        Signature ``ImageFileSelect()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ImagePaletteSelect(self) -> None:
        """
        Gets an image file from the image palette.  
        
        Signature ``ImagePaletteSelect()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ImagePreviewToggle: bool = ...
    """
    Returns or sets  the image preview toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``ImagePreviewToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImagePreviewToggle`` 
    
    :param imagePreviewToggle: 
    :type imagePreviewToggle: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    PatternRepeatFactor: float = ...
    """
    Returns or sets  the pattern repeat factor - the number of times the image repeats; non integer patternRepeatFactor numbers result in partial repeats.  
    
    <hr>
    
    Getter Method
    
    Signature ``PatternRepeatFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PatternRepeatFactor`` 
    
    :param patternRepeatFactor: 
    :type patternRepeatFactor: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: Image = ...  # unknown typename


class DynamicSectionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of dynamic section objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX6.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    @typing.overload
    def CreateSectionBuilder(self, section: DynamicSection, view: NXOpen.ModelingView) -> DynamicSectionBuilder:
        """
        Creates a :py:class:`NXOpen.Display.DynamicSectionBuilder` object if the section 
        is None. Otherwise, a Section object will be edited.
        
        The specified view can be None, in which case the section object is not 
        activated in any view.
        
        Signature ``CreateSectionBuilder(section, view)`` 
        
        :param section: 
        :type section: :py:class:`NXOpen.Display.DynamicSection` 
        :param view: 
        :type view: :py:class:`NXOpen.ModelingView` 
        :returns: 
        :rtype: :py:class:`NXOpen.Display.DynamicSectionBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateSectionBuilder(self, view: NXOpen.ModelingView) -> DynamicSectionBuilder:
        """
        Creates a :py:class:`NXOpen.Display.DynamicSectionBuilder` object that is used
        to edit a section object in the specified view. If no section object is available
        for the view, then a new one is created.
        
        The specified view can not be None, otherwise an exception will be raised.
        
        Signature ``CreateSectionBuilder(view)`` 
        
        :param view: 
        :type view: :py:class:`NXOpen.ModelingView` 
        :returns: 
        :rtype: :py:class:`NXOpen.Display.DynamicSectionBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CopySections(self, sections: 'list[DynamicSection]', deleteOriginals: bool) -> 'list[DynamicSection]':
        """
        Copies the specified dynamic sections in the part.  
        
        A copy of each
        specified dynamic section will be created and then added to the part. 
        It is  ensured that each dynamic section object in the part has a 
        unique name. Hence, it is possible that the name of a pasted section  
        object is different from that of the input section object if its name 
        clashes with an existing section object in the part.
        
        The section objects being copied must have been loaded in the memory.
        Otherwise this method will throw an exception.
        
        Signature ``CopySections(sections, deleteOriginals)`` 
        
        :param sections:  The objects to be pasted in the part  
        :type sections: list of :py:class:`NXOpen.Display.DynamicSection` 
        :param deleteOriginals:  Flag indicating whether the input sections should be deleted  
        :type deleteOriginals: bool 
        :returns:  Copied section objects in the part.  
        :rtype: list of :py:class:`NXOpen.Display.DynamicSection` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteSections(self, addUndoMark: bool, sections: 'list[DynamicSection]') -> None:
        """
        Deletes the specified dynamic sections in the part.  
        
        All views in
        which the dynamic sections were active are updated to reflect the
        change. An update will be performed to remove deleted objects.
        
        Signature ``DeleteSections(addUndoMark, sections)`` 
        
        :param addUndoMark:   Determines if a visible undo mark is added  
        :type addUndoMark: bool 
        :param sections:  The dynamic sections to be deleted  
        :type sections: list of :py:class:`NXOpen.Display.DynamicSection` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> DynamicSection:
        """
        Finds the :py:class:`NXOpen.Display.DynamicSection` with the given identifier as 
        recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier
        in different versions of the software. However newer versions of the software should find 
        the same object when FindObject is passed older versions of its journal identifier. In general,
        this method should not be used in handwritten code and exists to support record and 
        playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier. 
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  Section found  
        :rtype: :py:class:`NXOpen.Display.DynamicSection` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveToDefaultLayer(self, dynamicSections: 'list[DynamicSection]') -> None:
        """
        Moves the specified dynamic sections in the part to default layer.  
        
        The default settings are obtained from the view sectioning 
        customer defaults. 
        
        Signature ``MoveToDefaultLayer(dynamicSections)`` 
        
        :param dynamicSections:  The dynamic sections to be modified  
        :type dynamicSections: list of :py:class:`NXOpen.Display.DynamicSection` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    


class SelPrefMouseGestureMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SelPrefMouseGesture():
    """
    Represents the mouse gesture type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Lasso", "multi-select using lasso"
       "Rectangle", "multi-select using rectangle"
       "Circle", "multi-select using circle"
    """
    Lasso = 0  # SelPrefMouseGestureMemberType
    Rectangle = 1  # SelPrefMouseGestureMemberType
    Circle = 2  # SelPrefMouseGestureMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SelPrefSelectionRuleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SelPrefSelectionRule():
    """
    Represents the selection rule type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", "multi-select rule inside"
       "Outside", "multi-select rule outside"
       "Crossing", "multi-select rule crossing"
       "InsideCrossing", "multi-select rule inside or crossing"
       "OutsideCrossing", "multi-select rule outside or crossing"
    """
    Inside = 0  # SelPrefSelectionRuleMemberType
    Outside = 1  # SelPrefSelectionRuleMemberType
    Crossing = 2  # SelPrefSelectionRuleMemberType
    InsideCrossing = 3  # SelPrefSelectionRuleMemberType
    OutsideCrossing = 4  # SelPrefSelectionRuleMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SelPrefShadedViewsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SelPrefShadedViews():
    """
    Represents the shaded views type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "HighlightEdges", "highlight face by edges"
       "HighlightFaces", "highlight face by face"
    """
    HighlightEdges = 0  # SelPrefShadedViewsMemberType
    HighlightFaces = 1  # SelPrefShadedViewsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SelPrefFaceAnalysisViewsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SelPrefFaceAnalysisViews():
    """
    Represents the face analysis views type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "HighlightEdges", "highlight face by edges"
       "HighlightFaces", "highlight face by face"
    """
    HighlightEdges = 0  # SelPrefFaceAnalysisViewsMemberType
    HighlightFaces = 1  # SelPrefFaceAnalysisViewsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SelPrefSelectionRadiusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SelPrefSelectionRadius():
    """
    Represents the selection radius type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Medium", "selection ball size medium"
       "Small", "selection ball size small"
       "Large", "selection ball size large"
    """
    Medium = 0  # SelPrefSelectionRadiusMemberType
    Small = 1  # SelPrefSelectionRadiusMemberType
    Large = 2  # SelPrefSelectionRadiusMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SelPrefMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SelPrefMethod():
    """
    Represents the chaining method type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Simple", "chaining method simple"
       "Wcs", "chaining method wcs"
       "WcsLeft", "chaining method wcs left"
       "WcsRight", "chaining method wcs right"
    """
    Simple = 0  # SelPrefMethodMemberType
    Wcs = 1  # SelPrefMethodMemberType
    WcsLeft = 2  # SelPrefMethodMemberType
    WcsRight = 3  # SelPrefMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SelPref(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.SelPref`
    
    To obtain a instance of this class use :py:meth:`Display.SelPrefCollection.CreateSelPref`
    
    .. versionadded:: NX5.0.0
    """
    
    class MouseGesture():
        """
        Represents the mouse gesture type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Lasso", "multi-select using lasso"
           "Rectangle", "multi-select using rectangle"
           "Circle", "multi-select using circle"
        """
        Lasso = 0  # SelPrefMouseGestureMemberType
        Rectangle = 1  # SelPrefMouseGestureMemberType
        Circle = 2  # SelPrefMouseGestureMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SelectionRule():
        """
        Represents the selection rule type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", "multi-select rule inside"
           "Outside", "multi-select rule outside"
           "Crossing", "multi-select rule crossing"
           "InsideCrossing", "multi-select rule inside or crossing"
           "OutsideCrossing", "multi-select rule outside or crossing"
        """
        Inside = 0  # SelPrefSelectionRuleMemberType
        Outside = 1  # SelPrefSelectionRuleMemberType
        Crossing = 2  # SelPrefSelectionRuleMemberType
        InsideCrossing = 3  # SelPrefSelectionRuleMemberType
        OutsideCrossing = 4  # SelPrefSelectionRuleMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ShadedViews():
        """
        Represents the shaded views type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "HighlightEdges", "highlight face by edges"
           "HighlightFaces", "highlight face by face"
        """
        HighlightEdges = 0  # SelPrefShadedViewsMemberType
        HighlightFaces = 1  # SelPrefShadedViewsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FaceAnalysisViews():
        """
        Represents the face analysis views type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "HighlightEdges", "highlight face by edges"
           "HighlightFaces", "highlight face by face"
        """
        HighlightEdges = 0  # SelPrefFaceAnalysisViewsMemberType
        HighlightFaces = 1  # SelPrefFaceAnalysisViewsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SelectionRadius():
        """
        Represents the selection radius type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Medium", "selection ball size medium"
           "Small", "selection ball size small"
           "Large", "selection ball size large"
        """
        Medium = 0  # SelPrefSelectionRadiusMemberType
        Small = 1  # SelPrefSelectionRadiusMemberType
        Large = 2  # SelPrefSelectionRadiusMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Method():
        """
        Represents the chaining method type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Simple", "chaining method simple"
           "Wcs", "chaining method wcs"
           "WcsLeft", "chaining method wcs left"
           "WcsRight", "chaining method wcs right"
        """
        Simple = 0  # SelPrefMethodMemberType
        Wcs = 1  # SelPrefMethodMemberType
        WcsLeft = 2  # SelPrefMethodMemberType
        WcsRight = 3  # SelPrefMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Delay: int = ...
    """
    Returns or sets  the delay 
    
    <hr>
    
    Getter Method
    
    Signature ``Delay`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Delay`` 
    
    :param delay: 
    :type delay: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    FaceAnalysisViewsType: SelPrefFaceAnalysisViews = ...
    """
    Returns or sets  the face analysis views type 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceAnalysisViewsType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.SelPrefFaceAnalysisViews` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FaceAnalysisViewsType`` 
    
    :param faceAnalysisViewsType: 
    :type faceAnalysisViewsType: :py:class:`NXOpen.Display.SelPrefFaceAnalysisViews` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    HighlightHiddenEdgesToggle: bool = ...
    """
    Returns or sets  the highlight hidden edges toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``HighlightHiddenEdgesToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HighlightHiddenEdgesToggle`` 
    
    :param highlightHiddenEdgesToggle: 
    :type highlightHiddenEdgesToggle: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    HighlightOriginalToggle: bool = ...
    """
    Returns or sets  the highlight original
    
    <hr>
    
    Getter Method
    
    Signature ``HighlightOriginalToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HighlightOriginalToggle`` 
    
    :param highlightOriginalToggle: 
    :type highlightOriginalToggle: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    HighlightSelectionOnRolloverToggle: bool = ...
    """
    Returns or sets  the highlight selection on rollover toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``HighlightSelectionOnRolloverToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HighlightSelectionOnRolloverToggle`` 
    
    :param highlightSelectionOnRolloverToggle: 
    :type highlightSelectionOnRolloverToggle: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    HighlightWithThickWidthToggle: bool = ...
    """
    Returns or sets  the highlight with thick width toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``HighlightWithThickWidthToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HighlightWithThickWidthToggle`` 
    
    :param highlightWithThickWidthToggle: 
    :type highlightWithThickWidthToggle: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    MethodType: SelPrefMethod = ...
    """
    Returns or sets  the method type 
    
    <hr>
    
    Getter Method
    
    Signature ``MethodType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.SelPrefMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MethodType`` 
    
    :param methodType: 
    :type methodType: :py:class:`NXOpen.Display.SelPrefMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    MouseGestureType: SelPrefMouseGesture = ...
    """
    Returns or sets  the mouse gesture type 
    
    <hr>
    
    Getter Method
    
    Signature ``MouseGestureType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.SelPrefMouseGesture` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MouseGestureType`` 
    
    :param mouseGestureType: 
    :type mouseGestureType: :py:class:`NXOpen.Display.SelPrefMouseGesture` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    QuickPickLockDialogPosition: bool = ...
    """
    Returns or sets  the quick pick lock dialog position 
    
    <hr>
    
    Getter Method
    
    Signature ``QuickPickLockDialogPosition`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``QuickPickLockDialogPosition`` 
    
    :param quickPickLockDialogPosition: 
    :type quickPickLockDialogPosition: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    QuickPickOnDelayToggle: bool = ...
    """
    Returns or sets  the quick pick on delay toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``QuickPickOnDelayToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``QuickPickOnDelayToggle`` 
    
    :param quickPickOnDelayToggle: 
    :type quickPickOnDelayToggle: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    RolloverDelay: int = ...
    """
    Returns or sets  the rollover delay 
    
    <hr>
    
    Getter Method
    
    Signature ``RolloverDelay`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RolloverDelay`` 
    
    :param rolloverDelay: 
    :type rolloverDelay: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    SelectionRadiusType: SelPrefSelectionRadius = ...
    """
    Returns or sets  the selection radius type 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionRadiusType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.SelPrefSelectionRadius` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectionRadiusType`` 
    
    :param selectionRadiusType: 
    :type selectionRadiusType: :py:class:`NXOpen.Display.SelPrefSelectionRadius` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    SelectionRuleType: SelPrefSelectionRule = ...
    """
    Returns or sets  the selection rule type 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionRuleType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.SelPrefSelectionRule` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectionRuleType`` 
    
    :param selectionRuleType: 
    :type selectionRuleType: :py:class:`NXOpen.Display.SelPrefSelectionRule` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ShadedViewsType: SelPrefShadedViews = ...
    """
    Returns or sets  the shaded views type 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadedViewsType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.SelPrefShadedViews` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadedViewsType`` 
    
    :param shadedViewsType: 
    :type shadedViewsType: :py:class:`NXOpen.Display.SelPrefShadedViews` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ShowCrosshairsToggle: bool = ...
    """
    Returns or sets  the show crosshairs toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowCrosshairsToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowCrosshairsToggle`` 
    
    :param showCrosshairsToggle: 
    :type showCrosshairsToggle: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Tolerance: float = ...
    """
    Returns or sets  the tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Tolerance`` 
    
    :param tolerance: 
    :type tolerance: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    TooltipOnRolloverToggle: bool = ...
    """
    Returns or sets  the tooltip on rollover toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``TooltipOnRolloverToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TooltipOnRolloverToggle`` 
    
    :param tooltipOnRolloverToggle: 
    :type tooltipOnRolloverToggle: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: SelPref = ...  # unknown typename


class SelPrefCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection SelPref
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateSelPref(self) -> SelPref:
        """
        Create a :py:class:`NXOpen.Display.SelPref` object  
        
        Signature ``CreateSelPref()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Display.SelPref` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class DynamicSectionCut(NXOpen.NXObject):
    """
    Represents a dynamic section-cut generated by sectioning an object
    such as a :py:class:`NXOpen.IBody` or a 
    :py:class:`NXOpen.Assemblies.Component`.  
    
    Dynamic sectioncut is not supported in KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def PrepareForMeasure(self, contextOccurrence: NXOpen.NXObject, view: NXOpen.View) -> None:
        """
        Prepares the section-cut for measurement.  
        
        This may create
        curves necessary to do measurement operation. The curves are
        displayed as part of preparation for measurement. The curves
        may be detroyed at the end of measure operation (see
        :py:meth:`NXOpen.Session.DeleteTransientDynamicSectionCutData`.
        
        Signature ``PrepareForMeasure(contextOccurrence, view)`` 
        
        :param contextOccurrence:  This can be None. If non None, then this must                    be an occurrence in the part of section-cut occurrence.                     In this case, occurrences of curves associated with the                     section-cut are setup for measurement.                  
        :type contextOccurrence: :py:class:`NXOpen.NXObject` 
        :param view:  This can be None. If a valid view is specified,                     then it is used to skip invisible body occurrences in a                     component for creation of curves used for measurement.                     If curves have already been created, then view is ignored.                   
        :type view: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    CutObject: NXOpen.INXObject = ...
    """
    Returns  the object from which this section-cut is generated.  
    
    E.g.; a body, a body occurrence, a component.
    
    <hr>
    
    Getter Method
    
    Signature ``CutObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.INXObject` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: DynamicSectionCut = ...  # unknown typename


class PlaneGridBuilder(BoundedGridBuilder):
    """
    Represents the builder for adding a bounded grid :py:class:`NXOpen.Display.PlaneGrid` 
    to a plane.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Display.GridCollection.CreatePlaneGridBuilder`
    
    Default values.
    
    ===================  ========================================
    Property             Value
    ===================  ========================================
    Associative          1 
    -------------------  ----------------------------------------
    LabelReference       Local 
    -------------------  ----------------------------------------
    MajorLineSpacing     100 (millimeters part), 1 (inches part) 
    -------------------  ----------------------------------------
    MajorLineStyle       Solid 
    -------------------  ----------------------------------------
    MajorLineWeight      Normal 
    -------------------  ----------------------------------------
    MinorLineStyle       Dashed 
    -------------------  ----------------------------------------
    MinorLineWeight      Thin 
    -------------------  ----------------------------------------
    MinorLinesPerMajor   1 
    -------------------  ----------------------------------------
    Show                 1 
    -------------------  ----------------------------------------
    ShowLabel            Always 
    -------------------  ----------------------------------------
    ShowMajorLines       1 
    -------------------  ----------------------------------------
    ShowOnTop            0 
    -------------------  ----------------------------------------
    SnapPointsPerMinor   1 
    -------------------  ----------------------------------------
    SnapToGrid           0 
    ===================  ========================================
    
    .. versionadded:: NX6.0.0
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the plane 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: PlaneGridBuilder = ...  # unknown typename


class DecalCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection decal material texture 
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX6.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateDecalBuilder(self, decal: NXOpen.TaggedObject) -> DecalBuilder:
        """
        Creates a :py:class:`NXOpen.Display.DecalBuilder` object if decal is None.  
        
        Otherwise, a Decal object will be edited  
        
        Signature ``CreateDecalBuilder(decal)`` 
        
        :param decal:  If decal is not None, then this object will be edited  
        :type decal: :py:class:`NXOpen.TaggedObject` 
        :returns:  return decal builder  
        :rtype: :py:class:`NXOpen.Display.DecalBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDecalBuilderFull(self, decal: NXOpen.TaggedObject) -> DecalBuilder:
        """
        Creates a :py:class:`NXOpen.Display.DecalBuilder` object with image referenced object if decal is None.  
        
        Otherwise, a Decal object will be edited  
        
        Signature ``CreateDecalBuilderFull(decal)`` 
        
        :param decal:  If decal is not None, then this object will be edited  
        :type decal: :py:class:`NXOpen.TaggedObject` 
        :returns:  return decal builder  
        :rtype: :py:class:`NXOpen.Display.DecalBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindDecalObject(self, journalIdentifier: str) -> NXOpen.Decal:
        """
        Finds the :py:class:`NXOpen.Decal` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindDecalObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  Decal found  
        :rtype: :py:class:`NXOpen.Decal` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    


class ShadowsRealTimeStateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ShadowsRealTimeState():
    """
    Real time type settings - environment_shadow_catcher_only is enabled only in Basic Studio mode 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Disabled", "Realtime is disabled"
       "EnvironmentShadowCatcherOnly", "Realtime Environment or shadow catcher only"
       "InterObject", "Realtime Inter-object shadows"
    """
    Disabled = 0  # ShadowsRealTimeStateMemberType
    EnvironmentShadowCatcherOnly = 1  # ShadowsRealTimeStateMemberType
    InterObject = 2  # ShadowsRealTimeStateMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ShadowsSsaoQualityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ShadowsSsaoQualityType():
    """
    Shadows SSAO quality settings 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Low", "Low quality setting"
       "Medium", "Medium quality setting"
       "High", "High quality setting"
       "VeryHigh", "Very High quality setting"
    """
    Low = 0  # ShadowsSsaoQualityTypeMemberType
    Medium = 1  # ShadowsSsaoQualityTypeMemberType
    High = 2  # ShadowsSsaoQualityTypeMemberType
    VeryHigh = 3  # ShadowsSsaoQualityTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ShadowsSsaoContrastTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ShadowsSsaoContrastType():
    """
    Shadows SSAO contrast settings 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "no contrast"
       "Low", "low contrast"
       "Medium", "Medium contrast"
       "High", "High contrast"
       "ExtraHigh", "Extra High contrast"
    """
    NotSet = 0  # ShadowsSsaoContrastTypeMemberType
    Low = 1  # ShadowsSsaoContrastTypeMemberType
    Medium = 2  # ShadowsSsaoContrastTypeMemberType
    High = 3  # ShadowsSsaoContrastTypeMemberType
    ExtraHigh = 4  # ShadowsSsaoContrastTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Shadows(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.Shadows`
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateShadows`
    
    .. versionadded:: NX7.5.3
    """
    
    class RealTimeState():
        """
        Real time type settings - environment_shadow_catcher_only is enabled only in Basic Studio mode 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Disabled", "Realtime is disabled"
           "EnvironmentShadowCatcherOnly", "Realtime Environment or shadow catcher only"
           "InterObject", "Realtime Inter-object shadows"
        """
        Disabled = 0  # ShadowsRealTimeStateMemberType
        EnvironmentShadowCatcherOnly = 1  # ShadowsRealTimeStateMemberType
        InterObject = 2  # ShadowsRealTimeStateMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SsaoQualityType():
        """
        Shadows SSAO quality settings 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Low", "Low quality setting"
           "Medium", "Medium quality setting"
           "High", "High quality setting"
           "VeryHigh", "Very High quality setting"
        """
        Low = 0  # ShadowsSsaoQualityTypeMemberType
        Medium = 1  # ShadowsSsaoQualityTypeMemberType
        High = 2  # ShadowsSsaoQualityTypeMemberType
        VeryHigh = 3  # ShadowsSsaoQualityTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SsaoContrastType():
        """
        Shadows SSAO contrast settings 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "no contrast"
           "Low", "low contrast"
           "Medium", "Medium contrast"
           "High", "High contrast"
           "ExtraHigh", "Extra High contrast"
        """
        NotSet = 0  # ShadowsSsaoContrastTypeMemberType
        Low = 1  # ShadowsSsaoContrastTypeMemberType
        Medium = 2  # ShadowsSsaoContrastTypeMemberType
        High = 3  # ShadowsSsaoContrastTypeMemberType
        ExtraHigh = 4  # ShadowsSsaoContrastTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AmbientOcclusion: bool = ...
    """
    Returns or sets  the shadows SSAO ambient occlusion 
    
    <hr>
    
    Getter Method
    
    Signature ``AmbientOcclusion`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AmbientOcclusion`` 
    
    :param shadowsSSAODisplayEnabled: 
    :type shadowsSSAODisplayEnabled: bool 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    GenerateHqiShadows: bool = ...
    """
    Returns or sets  the High Quality Image settings 
    
    <hr>
    
    Getter Method
    
    Signature ``GenerateHqiShadows`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GenerateHqiShadows`` 
    
    :param generateHQIShadows: 
    :type generateHQIShadows: bool 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    RealTimeType: ShadowsRealTimeState = ...
    """
    Returns or sets  the Real Time Settings 
    
    <hr>
    
    Getter Method
    
    Signature ``RealTimeType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ShadowsRealTimeState` 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RealTimeType`` 
    
    :param realTimeType: 
    :type realTimeType: :py:class:`NXOpen.Display.ShadowsRealTimeState` 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    ShadowCatcherSelection: NXOpen.SelectNXObjectList = ...
    """
    Returns  the Shadow Catcher Selection 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadowCatcherSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    ShadowsEnabled: bool = ...
    """
    Returns or sets  the Overall Shadows 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadowsEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadowsEnabled`` 
    
    :param shadowsEnabled: 
    :type shadowsEnabled: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    """
    SoftShadowsBiasOffset: float = ...
    """
    Returns or sets  the Soft Shadows bias offset 
    
    <hr>
    
    Getter Method
    
    Signature ``SoftShadowsBiasOffset`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SoftShadowsBiasOffset`` 
    
    :param softShadowsBiasOffset: 
    :type softShadowsBiasOffset: float 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    SoftShadowsEdges: int = ...
    """
    Returns or sets  the Soft Shadows edges (softness) 
    
    <hr>
    
    Getter Method
    
    Signature ``SoftShadowsEdges`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SoftShadowsEdges`` 
    
    :param softShadowsEdges: 
    :type softShadowsEdges: int 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    SoftShadowsEnabled: bool = ...
    """
    Returns or sets  the Soft Shadows 
    
    <hr>
    
    Getter Method
    
    Signature ``SoftShadowsEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SoftShadowsEnabled`` 
    
    :param softShadowsEnabled: 
    :type softShadowsEnabled: bool 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    SoftShadowsGradientClamp: float = ...
    """
    Returns or sets  the Soft Shadows gradient clamp 
    
    <hr>
    
    Getter Method
    
    Signature ``SoftShadowsGradientClamp`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SoftShadowsGradientClamp`` 
    
    :param softShadowsGradientClamp: 
    :type softShadowsGradientClamp: float 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    SoftShadowsQuality: int = ...
    """
    Returns or sets  the Soft Shadows quality 
    
    <hr>
    
    Getter Method
    
    Signature ``SoftShadowsQuality`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SoftShadowsQuality`` 
    
    :param softShadowsQuality: 
    :type softShadowsQuality: int 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    SsaoBlurRadius: float = ...
    """
    Returns or sets  the shadows SSAO Blur Radius 
    
    <hr>
    
    Getter Method
    
    Signature ``SsaoBlurRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SsaoBlurRadius`` 
    
    :param blurRadius: 
    :type blurRadius: float 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    SsaoContrast: ShadowsSsaoContrastType = ...
    """
    Returns or sets  the shadows SSAO contrast 
    
    <hr>
    
    Getter Method
    
    Signature ``SsaoContrast`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ShadowsSsaoContrastType` 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SsaoContrast`` 
    
    :param contrast: 
    :type contrast: :py:class:`NXOpen.Display.ShadowsSsaoContrastType` 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    SsaoQuality: ShadowsSsaoQualityType = ...
    """
    Returns or sets  the shadows SSAO quality 
    
    <hr>
    
    Getter Method
    
    Signature ``SsaoQuality`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ShadowsSsaoQualityType` 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SsaoQuality`` 
    
    :param shadowsSSAOQuality: 
    :type shadowsSSAOQuality: :py:class:`NXOpen.Display.ShadowsSsaoQualityType` 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    SsaoRadius: float = ...
    """
    Returns or sets  the shadows SSAO radius 
    
    <hr>
    
    Getter Method
    
    Signature ``SsaoRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SsaoRadius`` 
    
    :param radius: 
    :type radius: float 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    UseShadowCatcher: bool = ...
    """
    Returns or sets  the Shadow Catcher 
    
    <hr>
    
    Getter Method
    
    Signature ``UseShadowCatcher`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseShadowCatcher`` 
    
    :param useShadowCatcher: 
    :type useShadowCatcher: bool 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    Null: Shadows = ...  # unknown typename


class TrueStudio(NXOpen.NXObject):
    """
    Represents a True Shading object   
    
    TrueStudio is not supported in KF.
    
    .. versionadded:: NX6.0.0
    """
    Null: TrueStudio = ...  # unknown typename


class ExtractScene(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.ExtractScene`
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateExtractScene`
    
    .. versionadded:: NX5.0.0
    """
    
    def Information(self) -> None:
        """
        The scene information 
        
        Signature ``Information()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ImageFileSelect(self) -> None:
        """
        Gets an image file using file selection.  
        
        Signature ``ImageFileSelect()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSceneDescription(self) -> 'list[str]':
        """
        Returns the scene description  
        
        Signature ``GetSceneDescription()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSceneDescription(self, sceneDescription: 'list[str]') -> None:
        """
        Sets the scene description 
        
        Signature ``SetSceneDescription(sceneDescription)`` 
        
        :param sceneDescription: 
        :type sceneDescription: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    SceneName: str = ...
    """
    Returns or sets  the scene name 
    
    <hr>
    
    Getter Method
    
    Signature ``SceneName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SceneName`` 
    
    :param sceneName: 
    :type sceneName: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: ExtractScene = ...  # unknown typename


class ImageCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of image objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX9.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> ImageBase:
        """
        Finds the :py:class:`NXOpen.Display.ImageBase` with the given identifier  
        as recorded in a journal.  
        
        An object may not return the same value as 
        its JournalIdentifier in different versions of the software. However  
        newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In 
        general,this method should not be used in handwritten code and exists 
        to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given 
        journal identifier. 
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  Image found  
        :rtype: :py:class:`NXOpen.Display.ImageBase` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateRasterImageBuilder(self, image: RasterImage) -> RasterImageBuilder:
        """
        Creates a :py:class:`NXOpen.Display.RasterImageBuilder` object
        used to build an image.  
        
        If the image is not None, the image object will be edited.
        
        Signature ``CreateRasterImageBuilder(image)`` 
        
        :param image:  If image is not None,                                                                                        this object will be edited  
        :type image: :py:class:`NXOpen.Display.RasterImage` 
        :returns:  raster image builder  
        :rtype: :py:class:`NXOpen.Display.RasterImageBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    


class EnvironmentBuilderImageBlurTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EnvironmentBuilderImageBlurType():
    """
    lighting image blurr type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Low", " - "
       "Medium", " - "
       "High", " - "
    """
    NotSet = 0  # EnvironmentBuilderImageBlurTypeMemberType
    Low = 1  # EnvironmentBuilderImageBlurTypeMemberType
    Medium = 2  # EnvironmentBuilderImageBlurTypeMemberType
    High = 3  # EnvironmentBuilderImageBlurTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EnvironmentBuilderImageUpVectorTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EnvironmentBuilderImageUpVectorTypes():
    """
    up vector type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AlignWithFloorPlane", " - "
       "UserDefined", " - "
    """
    AlignWithFloorPlane = 0  # EnvironmentBuilderImageUpVectorTypesMemberType
    UserDefined = 1  # EnvironmentBuilderImageUpVectorTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EnvironmentBuilderToneMappingTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EnvironmentBuilderToneMappingTypes():
    """
    tone mapping type - do not enable until NX11 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SystemScene", " - "
       "UserDefined", " - "
    """
    SystemScene = 0  # EnvironmentBuilderToneMappingTypesMemberType
    UserDefined = 1  # EnvironmentBuilderToneMappingTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EnvironmentBuilderGroundPlaneTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EnvironmentBuilderGroundPlaneTypes():
    """
    Represents an index to a ground plane type define 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Yz", "Use yz plane for the ground."
       "Xz", "Use xz plane for the ground."
       "Xy", "Use xy plane for the ground."
       "UserDefined", "Use user defined plane for the ground."
    """
    Yz = 0  # EnvironmentBuilderGroundPlaneTypesMemberType
    Xz = 1  # EnvironmentBuilderGroundPlaneTypesMemberType
    Xy = 2  # EnvironmentBuilderGroundPlaneTypesMemberType
    UserDefined = 3  # EnvironmentBuilderGroundPlaneTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EnvironmentBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`Display.EnvironmentBuilder`
    This controls environment image, tone mapping, and stages.  
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateEnvironmentBuilder`
    
    .. versionadded:: NX10.0.2
    """
    
    class ImageBlurType():
        """
        lighting image blurr type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Low", " - "
           "Medium", " - "
           "High", " - "
        """
        NotSet = 0  # EnvironmentBuilderImageBlurTypeMemberType
        Low = 1  # EnvironmentBuilderImageBlurTypeMemberType
        Medium = 2  # EnvironmentBuilderImageBlurTypeMemberType
        High = 3  # EnvironmentBuilderImageBlurTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ImageUpVectorTypes():
        """
        up vector type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AlignWithFloorPlane", " - "
           "UserDefined", " - "
        """
        AlignWithFloorPlane = 0  # EnvironmentBuilderImageUpVectorTypesMemberType
        UserDefined = 1  # EnvironmentBuilderImageUpVectorTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ToneMappingTypes():
        """
        tone mapping type - do not enable until NX11 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SystemScene", " - "
           "UserDefined", " - "
        """
        SystemScene = 0  # EnvironmentBuilderToneMappingTypesMemberType
        UserDefined = 1  # EnvironmentBuilderToneMappingTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class GroundPlaneTypes():
        """
        Represents an index to a ground plane type define 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Yz", "Use yz plane for the ground."
           "Xz", "Use xz plane for the ground."
           "Xy", "Use xy plane for the ground."
           "UserDefined", "Use user defined plane for the ground."
        """
        Yz = 0  # EnvironmentBuilderGroundPlaneTypesMemberType
        Xz = 1  # EnvironmentBuilderGroundPlaneTypesMemberType
        Xy = 2  # EnvironmentBuilderGroundPlaneTypesMemberType
        UserDefined = 3  # EnvironmentBuilderGroundPlaneTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CommitAndDisplay(self, view: NXOpen.View, updateIblDisplay: bool, updateEnvCubeDisplay: bool) -> None:
        """
        Saves the attributes and optionally updates the display of image-based lighting 
        
        Signature ``CommitAndDisplay(view, updateIblDisplay, updateEnvCubeDisplay)`` 
        
        :param view:  View of the image-based lighting attributes  
        :type view: :py:class:`NXOpen.View` 
        :param updateIblDisplay:  True if the image-based lighting display should be updated  
        :type updateIblDisplay: bool 
        :param updateEnvCubeDisplay:  True if the cube display should be updated  
        :type updateEnvCubeDisplay: bool 
        
        .. versionadded:: NX10.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def CommitOffset(self, view: NXOpen.View) -> None:
        """
        Updates the data and display for a change to the ground's offset 
        
        Signature ``CommitOffset(view)`` 
        
        :param view: 
        :type view: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def FloorXaxis(self) -> None:
        """
        The environment's floor to align with the WCS x-axis 
        
        Signature ``FloorXaxis()`` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def FloorYaxis(self) -> None:
        """
        The environment's floor to align with the WCS y-axis 
        
        Signature ``FloorYaxis()`` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def FloorZaxis(self) -> None:
        """
        The environment's floor to align with the WCS z-axis 
        
        Signature ``FloorZaxis()`` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def AlignFloorPlane(self, specifyFloorPlane: NXOpen.Plane) -> None:
        """
        The environment's floor aligns with the given plane.  
        
        Signature ``AlignFloorPlane(specifyFloorPlane)`` 
        
        :param specifyFloorPlane: 
        :type specifyFloorPlane: :py:class:`NXOpen.Plane` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    ColorSaturation: float = ...
    """
    Returns or sets  the image-based lighting color saturation 
    
    <hr>
    
    Getter Method
    
    Signature ``ColorSaturation`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``ColorSaturation`` 
    
    :param colorSaturation: 
    :type colorSaturation: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    GroundPlaneType: EnvironmentBuilderGroundPlaneTypes = ...
    """
    Returns or sets  the ground orientation define 
    
    <hr>
    
    Getter Method
    
    Signature ``GroundPlaneType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.EnvironmentBuilderGroundPlaneTypes` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GroundPlaneType`` 
    
    :param planeType: 
    :type planeType: :py:class:`NXOpen.Display.EnvironmentBuilderGroundPlaneTypes` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    """
    GroundReflection: bool = ...
    """
    Returns or sets  whether to enable ground reflection 
    
    <hr>
    
    Getter Method
    
    Signature ``GroundReflection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``GroundReflection`` 
    
    :param groundReflection: 
    :type groundReflection: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    GroundVisibility: bool = ...
    """
    Returns or sets  whether to enable ground visibility or not 
    
    <hr>
    
    Getter Method
    
    Signature ``GroundVisibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``GroundVisibility`` 
    
    :param groundVisibility: 
    :type groundVisibility: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    Image: Image = ...
    """
    Returns or sets  the image-based lighting's image builder 
    
    <hr>
    
    Getter Method
    
    Signature ``Image`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``Image`` 
    
    :param imageBuilder: 
    :type imageBuilder: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    ImageBlur: EnvironmentBuilderImageBlurType = ...
    """
    Returns or sets  the blurr of the lighting image 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageBlur`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.EnvironmentBuilderImageBlurType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``ImageBlur`` 
    
    :param imageBlurr: 
    :type imageBlurr: :py:class:`NXOpen.Display.EnvironmentBuilderImageBlurType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    ImageFilename: str = ...
    """
    Returns or sets  the image filename used for image-based lighting 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageFilename`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``ImageFilename`` 
    
    :param imageFileName: 
    :type imageFileName: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    ImageRotation: float = ...
    """
    Returns or sets  the image rotation angle (in degrees) 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageRotation`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``ImageRotation`` 
    
    :param imageRotation: 
    :type imageRotation: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    ImageUpVector: NXOpen.Direction = ...
    """
    Returns or sets  the image up vector direction, relative to the absolute coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageUpVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``ImageUpVector`` 
    
    :param imageUpVector: 
    :type imageUpVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    ImageUpVectorType: EnvironmentBuilderImageUpVectorTypes = ...
    """
    Returns or sets  the image up vector define 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageUpVectorType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.EnvironmentBuilderImageUpVectorTypes` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``ImageUpVectorType`` 
    
    :param imageUpVector: 
    :type imageUpVector: :py:class:`NXOpen.Display.EnvironmentBuilderImageUpVectorTypes` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    LightIntensity: float = ...
    """
    Returns or sets  the intensity of the light effects 
    
    <hr>
    
    Getter Method
    
    Signature ``LightIntensity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``LightIntensity`` 
    
    :param lightIntensity: 
    :type lightIntensity: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    LwrtAngle: float = ...
    """
    Returns or sets  the angle of the lwrt image-based lighting light effects 
    
    <hr>
    
    Getter Method
    
    Signature ``LwrtAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``LwrtAngle`` 
    
    :param lwrtAngle: 
    :type lwrtAngle: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    LwrtIntensity: float = ...
    """
    Returns or sets  the intensity of the lwrt image-based lighting light effects 
    
    <hr>
    
    Getter Method
    
    Signature ``LwrtIntensity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``LwrtIntensity`` 
    
    :param lwrtIntensity: 
    :type lwrtIntensity: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    LwrtQuality: float = ...
    """
    Returns or sets  the quality of the lwrt image-based lighting light effects 1 to 7 
    
    <hr>
    
    Getter Method
    
    Signature ``LwrtQuality`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``LwrtQuality`` 
    
    :param lwrtQuality: 
    :type lwrtQuality: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    OffsetExpression: NXOpen.Expression = ...
    """
    Returns  the environment offset expression
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetExpression`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    Reflectivity: float = ...
    """
    Returns or sets  the ground reflectivity 
    
    <hr>
    
    Getter Method
    
    Signature ``Reflectivity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``Reflectivity`` 
    
    :param reflectivity: 
    :type reflectivity: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    SizeExpression: NXOpen.Expression = ...
    """
    Returns  the environment size expression
    
    <hr>
    
    Getter Method
    
    Signature ``SizeExpression`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    SpecifyGroundPlane: NXOpen.Plane = ...
    """
    Returns or sets  the specify ground plane 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifyGroundPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpecifyGroundPlane`` 
    
    :param specifyPlane: 
    :type specifyPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    """
    UseEnvironment: bool = ...
    """
    Returns or sets  whether image-based lighting (IBL) is enabled 
    
    <hr>
    
    Getter Method
    
    Signature ``UseEnvironment`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``UseEnvironment`` 
    
    :param useIBL: 
    :type useIBL: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    UseLightsForShadowCatcherInLwrt: bool = ...
    """
    Returns or sets  whether Advanced Studio display (lwrt) uses individual light sources or image-based lighting for shadow catcher 
    
    <hr>
    
    Getter Method
    
    Signature ``UseLightsForShadowCatcherInLwrt`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``UseLightsForShadowCatcherInLwrt`` 
    
    :param useLightsForShadowCatcherInLwrt: 
    :type useLightsForShadowCatcherInLwrt: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    UseLwrtEnvironment: bool = ...
    """
    Returns or sets  whether image-based lighting is enabled in Advanced Studio (lwrt) display 
    
    <hr>
    
    Getter Method
    
    Signature ``UseLwrtEnvironment`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``UseLwrtEnvironment`` 
    
    :param useLwrtIBL: 
    :type useLwrtIBL: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    ViewFitToStage: bool = ...
    """
    Returns or sets  whether to fit view to stage 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewFitToStage`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``ViewFitToStage`` 
    
    :param viewFitToStage: 
    :type viewFitToStage: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    Null: EnvironmentBuilder = ...  # unknown typename


class ImageBaseBuilderBasePointChoicesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageBaseBuilderBasePointChoices():
    """
    Specifies image reference base point choice. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BottomLeft", "bottom left"
       "BottomCenter", "bottom center"
       "BottomRight", "bottom left"
       "MiddleLeft", "middle left"
       "MiddleCenter", "middle center"
       "MiddleRight", "middle right"
       "TopLeft", "top left"
       "TopCenter", "top center"
       "TopRight", "top right"
       "UserDefined", "user defined"
    """
    BottomLeft = 0  # ImageBaseBuilderBasePointChoicesMemberType
    BottomCenter = 1  # ImageBaseBuilderBasePointChoicesMemberType
    BottomRight = 2  # ImageBaseBuilderBasePointChoicesMemberType
    MiddleLeft = 3  # ImageBaseBuilderBasePointChoicesMemberType
    MiddleCenter = 4  # ImageBaseBuilderBasePointChoicesMemberType
    MiddleRight = 5  # ImageBaseBuilderBasePointChoicesMemberType
    TopLeft = 6  # ImageBaseBuilderBasePointChoicesMemberType
    TopCenter = 7  # ImageBaseBuilderBasePointChoicesMemberType
    TopRight = 8  # ImageBaseBuilderBasePointChoicesMemberType
    UserDefined = 9  # ImageBaseBuilderBasePointChoicesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageBaseBuilderReferenceDirectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageBaseBuilderReferenceDirection():
    """
    Specifies image alignment reference direction type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Horizontal", "horizontal reference direction"
       "Vertical", "vertical reference direction"
    """
    Horizontal = 0  # ImageBaseBuilderReferenceDirectionMemberType
    Vertical = 1  # ImageBaseBuilderReferenceDirectionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageBaseBuilderInsertionPointMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageBaseBuilderInsertionPoint():
    """
    Describes insertion point type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Default", "default insertion point type"
       "UserDefined", "user defined insertion point type"
    """
    Default = 0  # ImageBaseBuilderInsertionPointMemberType
    UserDefined = 1  # ImageBaseBuilderInsertionPointMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageBaseBuilderSizeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageBaseBuilderSizeOptions():
    """
    Describes size options. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UserDefined", "user defined option"
       "ImageSize", "image size option"
       "ReferenceScaling", "reference scaling option"
    """
    UserDefined = 0  # ImageBaseBuilderSizeOptionsMemberType
    ImageSize = 1  # ImageBaseBuilderSizeOptionsMemberType
    ReferenceScaling = 2  # ImageBaseBuilderSizeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageBaseBuilderImageColorModesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageBaseBuilderImageColorModes():
    """
    Describes image color modes. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Rgb", "rgb color mode"
       "Greyscale", "grey scale color mode"
       "Monochrome", "monochrome color mode"
    """
    Rgb = 0  # ImageBaseBuilderImageColorModesMemberType
    Greyscale = 1  # ImageBaseBuilderImageColorModesMemberType
    Monochrome = 2  # ImageBaseBuilderImageColorModesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageBaseBuilderTransparencyColorFromMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageBaseBuilderTransparencyColorFrom():
    """
    Transparency Color From 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No Transparency Color"
       "FromImage", "Transparency Color from image"
       "PixelColor", " - "
    """
    NotSet = 0  # ImageBaseBuilderTransparencyColorFromMemberType
    FromImage = 1  # ImageBaseBuilderTransparencyColorFromMemberType
    PixelColor = 2  # ImageBaseBuilderTransparencyColorFromMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageBaseBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.ImageBaseBuilder`.  
    
    Serves as the base class for all :py:class:`NXOpen.Display.ImageBase` builders.
    :py:class:`NXOpen.Display.ImageBase` base class provides definition, orientation,
    sizing, and display setting controls for image based objects. 
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX9.0.0
    """
    
    class BasePointChoices():
        """
        Specifies image reference base point choice. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BottomLeft", "bottom left"
           "BottomCenter", "bottom center"
           "BottomRight", "bottom left"
           "MiddleLeft", "middle left"
           "MiddleCenter", "middle center"
           "MiddleRight", "middle right"
           "TopLeft", "top left"
           "TopCenter", "top center"
           "TopRight", "top right"
           "UserDefined", "user defined"
        """
        BottomLeft = 0  # ImageBaseBuilderBasePointChoicesMemberType
        BottomCenter = 1  # ImageBaseBuilderBasePointChoicesMemberType
        BottomRight = 2  # ImageBaseBuilderBasePointChoicesMemberType
        MiddleLeft = 3  # ImageBaseBuilderBasePointChoicesMemberType
        MiddleCenter = 4  # ImageBaseBuilderBasePointChoicesMemberType
        MiddleRight = 5  # ImageBaseBuilderBasePointChoicesMemberType
        TopLeft = 6  # ImageBaseBuilderBasePointChoicesMemberType
        TopCenter = 7  # ImageBaseBuilderBasePointChoicesMemberType
        TopRight = 8  # ImageBaseBuilderBasePointChoicesMemberType
        UserDefined = 9  # ImageBaseBuilderBasePointChoicesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ReferenceDirection():
        """
        Specifies image alignment reference direction type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Horizontal", "horizontal reference direction"
           "Vertical", "vertical reference direction"
        """
        Horizontal = 0  # ImageBaseBuilderReferenceDirectionMemberType
        Vertical = 1  # ImageBaseBuilderReferenceDirectionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class InsertionPoint():
        """
        Describes insertion point type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Default", "default insertion point type"
           "UserDefined", "user defined insertion point type"
        """
        Default = 0  # ImageBaseBuilderInsertionPointMemberType
        UserDefined = 1  # ImageBaseBuilderInsertionPointMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SizeOptions():
        """
        Describes size options. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "UserDefined", "user defined option"
           "ImageSize", "image size option"
           "ReferenceScaling", "reference scaling option"
        """
        UserDefined = 0  # ImageBaseBuilderSizeOptionsMemberType
        ImageSize = 1  # ImageBaseBuilderSizeOptionsMemberType
        ReferenceScaling = 2  # ImageBaseBuilderSizeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ImageColorModes():
        """
        Describes image color modes. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Rgb", "rgb color mode"
           "Greyscale", "grey scale color mode"
           "Monochrome", "monochrome color mode"
        """
        Rgb = 0  # ImageBaseBuilderImageColorModesMemberType
        Greyscale = 1  # ImageBaseBuilderImageColorModesMemberType
        Monochrome = 2  # ImageBaseBuilderImageColorModesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TransparencyColorFrom():
        """
        Transparency Color From 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No Transparency Color"
           "FromImage", "Transparency Color from image"
           "PixelColor", " - "
        """
        NotSet = 0  # ImageBaseBuilderTransparencyColorFromMemberType
        FromImage = 1  # ImageBaseBuilderTransparencyColorFromMemberType
        PixelColor = 2  # ImageBaseBuilderTransparencyColorFromMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def AlignImageToReferenceDirection(self) -> None:
        """
        Align Image to Reference Direction
        
        Signature ``AlignImageToReferenceDirection()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RotateLeft(self) -> None:
        """
        Rotates the image 90 degrees counter-clockwise.  
        
        Signature ``RotateLeft()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RotateRight(self) -> None:
        """
        Rotates the image 90 degrees clockwise.  
        
        Signature ``RotateRight()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FlipHorizontal(self) -> None:
        """
        Flips the image horizontally.  
        
        Signature ``FlipHorizontal()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FlipVertical(self) -> None:
        """
        Flips the image vertically.  
        
        Signature ``FlipVertical()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OrientViewToImage(self) -> None:
        """
        Orients and fits the work view's view direction along the reverse normal direction of the image 
        
        Signature ``OrientViewToImage()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetImagesInPart(self) -> 'list[str]':
        """
        Provide a list of names of the :py:class:`NXOpen.Display.ImageData`
        objects saved in current part file.  
        
        Signature ``GetImagesInPart()`` 
        
        :returns:  Array of :py:class:`NXOpen.Display.ImageData` names  
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetImageFromPart(self, imageName: str) -> None:
        """
        Set a :py:class:`NXOpen.Display.ImageData` object currently 
        stored in the part as the image used by the builder.  
        
        Signature ``SetImageFromPart(imageName)`` 
        
        :param imageName:  Name of :py:class:`NXOpen.Display.ImageData` object  
        :type imageName: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCornerPoints(self) -> tuple:
        """
        Get the image corner points.  
        
        The points define a rectangular region
        and are ordered counter-clockwise.
        
        Signature ``GetCornerPoints()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (point1, point2, point3, point4). point1 is a :py:class:`NXOpen.Point3d`.   first corner point of image point2 is a :py:class:`NXOpen.Point3d`.   second corner point of image point3 is a :py:class:`NXOpen.Point3d`.   third corner point of image point4 is a :py:class:`NXOpen.Point3d`.   fourth corner point of image 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCornerPoints(self, point1: NXOpen.Point3d, point2: NXOpen.Point3d, point3: NXOpen.Point3d, point4: NXOpen.Point3d) -> None:
        """
        Set the image corner points.  
        
        The points must define a rectangular
        region and be ordered counter-clockwise.
        
        Signature ``SetCornerPoints(point1, point2, point3, point4)`` 
        
        :param point1:  first corner point of image  
        :type point1: :py:class:`NXOpen.Point3d` 
        :param point2:  second corner point of image  
        :type point2: :py:class:`NXOpen.Point3d` 
        :param point3:  third corner point of image  
        :type point3: :py:class:`NXOpen.Point3d` 
        :param point4:  fourth corner point of image  
        :type point4: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTransparentPixelColor(self) -> 'list[float]':
        """
        Gets the transparency color (RGB value) of the image. Only valid
        when :py:meth:`NXOpen.Display.ImageBaseBuilder.TransparencyColorOption`
        is set to :py:class:`NXOpen.Display.ImageBaseBuilderTransparencyColorFrom.PixelColor <NXOpen.Display.ImageBaseBuilderTransparencyColorFrom>`. 
        
        The length of the output array will always be 3.  Each color value of 
        the double array is in the range 0.0 to 1.0. 
        
        Signature ``GetTransparentPixelColor()`` 
        
        :returns:  RGB color array  
        :rtype: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTransparentPixelColor(self, transparencyColor: 'list[float]') -> None:
        """
        Sets the transparency color (RGB value) of the image. Only valid
        when :py:meth:`NXOpen.Display.ImageBaseBuilder.TransparencyColorOption`
        is set to :py:class:`NXOpen.Display.ImageBaseBuilderTransparencyColorFrom.PixelColor <NXOpen.Display.ImageBaseBuilderTransparencyColorFrom>`. 
        
        The length of the input array should always be 3.  Each color value of 
        the double array must be in the range 0.0 to 1.0. 
        
        Signature ``SetTransparentPixelColor(transparencyColor)`` 
        
        :param transparencyColor:  RGB color array  
        :type transparencyColor: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetForegroundColor(self) -> 'list[float]':
        """
        Gets the foreground color (RGB value) of the image. Only valid
        when :py:meth:`NXOpen.Display.ImageBaseBuilder.ColorMode`
        is set to :py:class:`NXOpen.Display.ImageBaseBuilderImageColorModes.Greyscale <NXOpen.Display.ImageBaseBuilderImageColorModes>`. 
        
        The length of the output array will always be 3.  Each color value of 
        the double array is in the range 0.0 to 1.0. 
        
        Signature ``GetForegroundColor()`` 
        
        :returns:  RGB color array  
        :rtype: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetForegroundColor(self, foregroundColor: 'list[float]') -> None:
        """
        Sets the foreground color (RGB value) of the image. Only valid
        when :py:meth:`NXOpen.Display.ImageBaseBuilder.ColorMode`
        is set to :py:class:`NXOpen.Display.ImageBaseBuilderImageColorModes.Greyscale <NXOpen.Display.ImageBaseBuilderImageColorModes>`. 
        
        The length of the input array should always be 3.  Each color value of 
        the double array must be in the range 0.0 to 1.0. 
        
        Signature ``SetForegroundColor(foregroundColor)`` 
        
        :param foregroundColor:  RGB color array  
        :type foregroundColor: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBackgroundColor(self) -> 'list[float]':
        """
        Gets the background color (RGB value) of the image. Only valid
        when :py:meth:`NXOpen.Display.ImageBaseBuilder.ColorMode`
        is set to :py:class:`NXOpen.Display.ImageBaseBuilderImageColorModes.Greyscale <NXOpen.Display.ImageBaseBuilderImageColorModes>`. 
        
        The length of the output array will always be 3.  Each color value of 
        the double array is in the range 0.0 to 1.0. 
        
        Signature ``GetBackgroundColor()`` 
        
        :returns:  RGB color array  
        :rtype: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBackgroundColor(self, backgroundColor: 'list[float]') -> None:
        """
        Sets the background color (RGB value) of the image. Only valid
        when :py:meth:`NXOpen.Display.ImageBaseBuilder.ColorMode`
        is set to :py:class:`NXOpen.Display.ImageBaseBuilderImageColorModes.Greyscale <NXOpen.Display.ImageBaseBuilderImageColorModes>`. 
        
        The length of the input array should always be 3.  Each color value of 
        the double array must be in the range 0.0 to 1.0. 
        
        Signature ``SetBackgroundColor(backgroundColor)`` 
        
        :param backgroundColor:  RGB color array  
        :type backgroundColor: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetImageSize(self) -> None:
        """
        Resets the image to its original size.  
        
        Signature ``ResetImageSize()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    BasePointChoice: ImageBaseBuilderBasePointChoices = ...
    """
    Returns or sets  the image reference base point choice.  
    
    If you choose 
    :py:class:`NXOpen.Display.ImageBaseBuilderBasePointChoices.UserDefined <NXOpen.Display.ImageBaseBuilderBasePointChoices>`, 
    use :py:meth:`NXOpen.Display.ImageBaseBuilder.UserBasePoint` 
    to set a point as the User-Defined point. 
    
    <hr>
    
    Getter Method
    
    Signature ``BasePointChoice`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBaseBuilderBasePointChoices` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BasePointChoice`` 
    
    :param basePoint: 
    :type basePoint: :py:class:`NXOpen.Display.ImageBaseBuilderBasePointChoices` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ColorMode: ImageBaseBuilderImageColorModes = ...
    """
    Returns or sets  the color mode to display the image.  
    
    <hr>
    
    Getter Method
    
    Signature ``ColorMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBaseBuilderImageColorModes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColorMode`` 
    
    :param colorMode: 
    :type colorMode: :py:class:`NXOpen.Display.ImageBaseBuilderImageColorModes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Height: NXOpen.Expression = ...
    """
    Returns the height of the image as an :py:class:`NXOpen.Expression`. 
    The returned :py:class:`NXOpen.Expression` is **not</b> associative to this object. 
    
    When :py:meth:`NXOpen.Display.ImageBaseBuilder.SizeOption` 
    is set to :py:class:`NXOpen.Display.ImageBaseBuilderSizeOptions.UserDefined <NXOpen.Display.ImageBaseBuilderSizeOptions>`,
    set the size of the image using :py:meth:`NXOpen.Display.ImageBaseBuilder.SetCornerPoints`.
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ImageFile: str = ...
    """
    Returns or sets  the image file 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageFile`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ImageReferencePoint1: NXOpen.Point = ...
    """
    Returns or sets the image reference point1. Only valid when 
    :py:meth:`NXOpen.Display.ImageBaseBuilder.SizeOption` is set to 
    :py:class:`NXOpen.Display.ImageBaseBuilderSizeOptions.ReferenceScaling <NXOpen.Display.ImageBaseBuilderSizeOptions>`. 
    
    Reference Scaling provides sizing the image by defining image reference 
    points and matching them with corresponding model reference points.
    
    <hr>
    
    Getter Method
    
    Signature ``ImageReferencePoint1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageReferencePoint1`` 
    
    :param imageReferencePoint1: 
    :type imageReferencePoint1: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ImageReferencePoint2: NXOpen.Point = ...
    """
    Returns or sets the image reference point2. Only valid when 
    :py:meth:`NXOpen.Display.ImageBaseBuilder.SizeOption` is set to 
    :py:class:`NXOpen.Display.ImageBaseBuilderSizeOptions.ReferenceScaling <NXOpen.Display.ImageBaseBuilderSizeOptions>`. 
    
    Reference Scaling provides sizing the image by defining image reference 
    points and matching them with corresponding model reference points.
    
    <hr>
    
    Getter Method
    
    Signature ``ImageReferencePoint2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageReferencePoint2`` 
    
    :param imageReferencePoint2: 
    :type imageReferencePoint2: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ImageReferencePoint3: NXOpen.Point = ...
    """
    Returns or sets the image reference point3. Only valid when 
    :py:meth:`NXOpen.Display.ImageBaseBuilder.SizeOption` is set to 
    :py:class:`NXOpen.Display.ImageBaseBuilderSizeOptions.ReferenceScaling <NXOpen.Display.ImageBaseBuilderSizeOptions>`
    and :py:meth:`NXOpen.Display.ImageBaseBuilder.LockAspectRatio` 
    is False. 
    
    Reference Scaling provides sizing the image by defining image reference 
    points and matching them with corresponding model reference points.
    
    <hr>
    
    Getter Method
    
    Signature ``ImageReferencePoint3`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageReferencePoint3`` 
    
    :param imageReferencePoint3: 
    :type imageReferencePoint3: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    InsertionPointOption: ImageBaseBuilderInsertionPoint = ...
    """
    Returns or sets  the image insertion point type 
    
    <hr>
    
    Getter Method
    
    Signature ``InsertionPointOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBaseBuilderInsertionPoint` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InsertionPointOption`` 
    
    :param insertPoint: 
    :type insertPoint: :py:class:`NXOpen.Display.ImageBaseBuilderInsertionPoint` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LockAspectRatio: bool = ...
    """
    Returns or sets  the lock aspect ratio 
    
    <hr>
    
    Getter Method
    
    Signature ``LockAspectRatio`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LockAspectRatio`` 
    
    :param lockAspectRatio: 
    :type lockAspectRatio: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ModelReferencePoint1: NXOpen.Point = ...
    """
    Returns or sets the model reference point1. Only valid when 
    :py:meth:`NXOpen.Display.ImageBaseBuilder.SizeOption` is set to 
    :py:class:`NXOpen.Display.ImageBaseBuilderSizeOptions.ReferenceScaling <NXOpen.Display.ImageBaseBuilderSizeOptions>`. 
    
    Reference Scaling provides sizing the image by defining image reference 
    points and matching them with corresponding model reference points.
    
    <hr>
    
    Getter Method
    
    Signature ``ModelReferencePoint1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ModelReferencePoint1`` 
    
    :param modelReferencePoint1: 
    :type modelReferencePoint1: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ModelReferencePoint2: NXOpen.Point = ...
    """
    Returns or sets the model reference point2. Only valid when 
    :py:meth:`NXOpen.Display.ImageBaseBuilder.SizeOption` is set to 
    :py:class:`NXOpen.Display.ImageBaseBuilderSizeOptions.ReferenceScaling <NXOpen.Display.ImageBaseBuilderSizeOptions>`. 
    
    Reference Scaling provides sizing the image by defining image reference 
    points and matching them with corresponding model reference points.
    
    <hr>
    
    Getter Method
    
    Signature ``ModelReferencePoint2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ModelReferencePoint2`` 
    
    :param modelReferencePoint2: 
    :type modelReferencePoint2: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ModelReferencePoint3: NXOpen.Point = ...
    """
    Returns or sets the model reference point3. Only valid when 
    :py:meth:`NXOpen.Display.ImageBaseBuilder.SizeOption` is set to 
    :py:class:`NXOpen.Display.ImageBaseBuilderSizeOptions.ReferenceScaling <NXOpen.Display.ImageBaseBuilderSizeOptions>`
    and :py:meth:`NXOpen.Display.ImageBaseBuilder.LockAspectRatio` 
    is False. 
    
    Reference Scaling provides sizing the image by defining image reference 
    points and matching them with corresponding model reference points.
    
    <hr>
    
    Getter Method
    
    Signature ``ModelReferencePoint3`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ModelReferencePoint3`` 
    
    :param modelReferencePoint3: 
    :type modelReferencePoint3: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    OverallTranslucency: int = ...
    """
    Returns or sets  the overall translucency.  
    
    The range of this value is 0 to 100. 
    
    <hr>
    
    Getter Method
    
    Signature ``OverallTranslucency`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OverallTranslucency`` 
    
    :param overallTranslucency: 
    :type overallTranslucency: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    PixelColorTolerance: int = ...
    """
    Returns or sets  the transparency pixel color tolerance.  
    
    The range of this value is 
    0 to 255.
    
    <hr>
    
    Getter Method
    
    Signature ``PixelColorTolerance`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PixelColorTolerance`` 
    
    :param colorTolerence: 
    :type colorTolerence: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ReferenceDirectionOption: ImageBaseBuilderReferenceDirection = ...
    """
    Returns or sets  the image alignment reference direction type.  
    
    :py:class:`NXOpen.Display.ImageBaseBuilderReferenceDirection.Horizontal <NXOpen.Display.ImageBaseBuilderReferenceDirection>`
    means rotate the image to align its horizontal direction with the user-specified 
    reference direction (if defined). 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceDirectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBaseBuilderReferenceDirection` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceDirectionOption`` 
    
    :param referenceDirection: 
    :type referenceDirection: :py:class:`NXOpen.Display.ImageBaseBuilderReferenceDirection` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RotateAngleOfReferenceVector: NXOpen.Expression = ...
    """
    Returns  the current rotation angle of image from aligned reference direction 
    
    <hr>
    
    Getter Method
    
    Signature ``RotateAngleOfReferenceVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    SizeOption: ImageBaseBuilderSizeOptions = ...
    """
    Returns or sets  the size option 
    
    <hr>
    
    Getter Method
    
    Signature ``SizeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBaseBuilderSizeOptions` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SizeOption`` 
    
    :param sizeOption: 
    :type sizeOption: :py:class:`NXOpen.Display.ImageBaseBuilderSizeOptions` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TransparencyColorOption: ImageBaseBuilderTransparencyColorFrom = ...
    """
    Returns or sets  the transparency color option 
    
    <hr>
    
    Getter Method
    
    Signature ``TransparencyColorOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBaseBuilderTransparencyColorFrom` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TransparencyColorOption`` 
    
    :param transparencyColorOption: 
    :type transparencyColorOption: :py:class:`NXOpen.Display.ImageBaseBuilderTransparencyColorFrom` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    UserBasePoint: NXOpen.Point = ...
    """
    Returns or sets the user defined base point. Only valid when 
    :py:meth:`NXOpen.Display.ImageBaseBuilder.BasePointChoice` is set to 
    :py:class:`NXOpen.Display.ImageBaseBuilderBasePointChoices.UserDefined <NXOpen.Display.ImageBaseBuilderBasePointChoices>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``UserBasePoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UserBasePoint`` 
    
    :param basePoint: 
    :type basePoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    UserInsertionPoint: NXOpen.Point = ...
    """
    Returns or sets  the user defined insertion point 
    
    <hr>
    
    Getter Method
    
    Signature ``UserInsertionPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UserInsertionPoint`` 
    
    :param insertPoint: 
    :type insertPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    UserReferenceDirection: NXOpen.Direction = ...
    """
    Returns or sets  the user defined reference direction vector.  
    
    A direction normal to 
    the plane of the image is invalid.
    
    <hr>
    
    Getter Method
    
    Signature ``UserReferenceDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UserReferenceDirection`` 
    
    :param userDirection: 
    :type userDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Width: NXOpen.Expression = ...
    """
    Returns the width of the image as an :py:class:`NXOpen.Expression`. 
    The returned :py:class:`NXOpen.Expression` is **not</b> associative to this object. 
    
    When :py:meth:`NXOpen.Display.ImageBaseBuilder.SizeOption` 
    is set to :py:class:`NXOpen.Display.ImageBaseBuilderSizeOptions.UserDefined <NXOpen.Display.ImageBaseBuilderSizeOptions>`,
    set the size of the image using :py:meth:`NXOpen.Display.ImageBaseBuilder.SetCornerPoints`.
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: ImageBaseBuilder = ...  # unknown typename


class RasterImageBuilder(ImageBaseBuilder):
    """
    Represents a :py:class:`NXOpen.Display.RasterImageBuilder`.  
    
    :py:class:`NXOpen.Display.RasterImage` provides placing an imported image 
    onto a plane (with controls for orientation, sizing, and display) to use as
    a reference in the model to create geometry. 
    
    To create a new instance of this class, use :py:meth:`NXOpen.Display.ImageCollection.CreateRasterImageBuilder`
    
    Default values.
    
    =========================  ============
    Property                   Value
    =========================  ============
    BasePointChoice            BottomLeft 
    -------------------------  ------------
    ColorMode                  Rgb 
    -------------------------  ------------
    InsertionPointOption       Default 
    -------------------------  ------------
    LockAspectRatio            1 
    -------------------------  ------------
    OverallTranslucency        0 
    -------------------------  ------------
    PixelColorTolerance        32 
    -------------------------  ------------
    ReferenceDirectionOption   Horizontal 
    -------------------------  ------------
    SizeOption                 UserDefined 
    -------------------------  ------------
    TransparencyColorOption    None 
    =========================  ============
    
    .. versionadded:: NX9.0.0
    """
    Target: NXOpen.Plane = ...
    """
    Returns or sets  the plane the raster image is placed onto 
    
    <hr>
    
    Getter Method
    
    Signature ``Target`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Target`` 
    
    :param targetObject: 
    :type targetObject: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: RasterImageBuilder = ...  # unknown typename


class DecalBuilderImageSizeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DecalBuilderImageSize():
    """
    image size type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "TrueSize", "use true image size"
       "OneTwentyEight", "resize image to 128 x 128"
       "TwoFiftySix", "resize iamge to 256 x 256"
       "FiveTwelve", "resize image to 512 x 512"
       "OneOTwoFour", "resize image to 1024 x1024"
       "TwoOFourEight", "resize image to 2048x2048"
       "FourONineSix", "resize image to 4096x 4096"
    """
    TrueSize = 0  # DecalBuilderImageSizeMemberType
    OneTwentyEight = 1  # DecalBuilderImageSizeMemberType
    TwoFiftySix = 2  # DecalBuilderImageSizeMemberType
    FiveTwelve = 3  # DecalBuilderImageSizeMemberType
    OneOTwoFour = 4  # DecalBuilderImageSizeMemberType
    TwoOFourEight = 5  # DecalBuilderImageSizeMemberType
    FourONineSix = 6  # DecalBuilderImageSizeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DecalBuilderDecalIlluminationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DecalBuilderDecalIllumination():
    """
    decal illumination type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UseUnderlyingMaterial", "base decal reflectivity on underlying material"
       "UseDecalMaterial", "set decal's reflectivity"
    """
    UseUnderlyingMaterial = 0  # DecalBuilderDecalIlluminationMemberType
    UseDecalMaterial = 1  # DecalBuilderDecalIlluminationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DecalBuilderDecalReflectivitiesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DecalBuilderDecalReflectivities():
    """
    decal reflectivity type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UseMatte", " - "
       "UsePlastic", " - "
       "UseMirror", " - "
       "UseMetal", " - "
       "UseGlass", " - "
    """
    UseMatte = 0  # DecalBuilderDecalReflectivitiesMemberType
    UsePlastic = 1  # DecalBuilderDecalReflectivitiesMemberType
    UseMirror = 2  # DecalBuilderDecalReflectivitiesMemberType
    UseMetal = 3  # DecalBuilderDecalReflectivitiesMemberType
    UseGlass = 4  # DecalBuilderDecalReflectivitiesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DecalBuilderAnchorMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DecalBuilderAnchor():
    """
    image anchor 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "TopLeft", "anchor at top left corner of decal image"
       "Center", "anchor in the middle of decal image"
       "BottomLeft", "anchor at the bottom left corner of decal image"
       "TopMiddle", "anchor at top middle corner of decal image"
       "TopRight", "anchor at top right corner of decal image"
       "LeftMiddle", "anchor at left middle corner of decal image"
       "RightMiddle", "anchor at right middle corner of decal image"
       "BottomMiddle", "anchor at bottom middle corner of decal image"
       "BottomRight", "anchor at bottom right corner of decal image"
    """
    TopLeft = 0  # DecalBuilderAnchorMemberType
    Center = 1  # DecalBuilderAnchorMemberType
    BottomLeft = 2  # DecalBuilderAnchorMemberType
    TopMiddle = 3  # DecalBuilderAnchorMemberType
    TopRight = 4  # DecalBuilderAnchorMemberType
    LeftMiddle = 5  # DecalBuilderAnchorMemberType
    RightMiddle = 6  # DecalBuilderAnchorMemberType
    BottomMiddle = 7  # DecalBuilderAnchorMemberType
    BottomRight = 8  # DecalBuilderAnchorMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DecalBuilderScalingMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DecalBuilderScaling():
    """
    decal scaling type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ToFace", "scale the decal based on face size"
       "ToImageSize", "scale the decal based on true decal image size"
       "ToUniformScale", "scale the decal based on uniform scale"
       "ToNonUniformScale", "scale the decal based on both width and height scale"
    """
    ToFace = 0  # DecalBuilderScalingMemberType
    ToImageSize = 1  # DecalBuilderScalingMemberType
    ToUniformScale = 2  # DecalBuilderScalingMemberType
    ToNonUniformScale = 3  # DecalBuilderScalingMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DecalBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.DecalBuilder` 
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    .. versionadded:: NX6.0.0
    """
    
    class ImageSize():
        """
        image size type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "TrueSize", "use true image size"
           "OneTwentyEight", "resize image to 128 x 128"
           "TwoFiftySix", "resize iamge to 256 x 256"
           "FiveTwelve", "resize image to 512 x 512"
           "OneOTwoFour", "resize image to 1024 x1024"
           "TwoOFourEight", "resize image to 2048x2048"
           "FourONineSix", "resize image to 4096x 4096"
        """
        TrueSize = 0  # DecalBuilderImageSizeMemberType
        OneTwentyEight = 1  # DecalBuilderImageSizeMemberType
        TwoFiftySix = 2  # DecalBuilderImageSizeMemberType
        FiveTwelve = 3  # DecalBuilderImageSizeMemberType
        OneOTwoFour = 4  # DecalBuilderImageSizeMemberType
        TwoOFourEight = 5  # DecalBuilderImageSizeMemberType
        FourONineSix = 6  # DecalBuilderImageSizeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DecalIllumination():
        """
        decal illumination type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "UseUnderlyingMaterial", "base decal reflectivity on underlying material"
           "UseDecalMaterial", "set decal's reflectivity"
        """
        UseUnderlyingMaterial = 0  # DecalBuilderDecalIlluminationMemberType
        UseDecalMaterial = 1  # DecalBuilderDecalIlluminationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DecalReflectivities():
        """
        decal reflectivity type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "UseMatte", " - "
           "UsePlastic", " - "
           "UseMirror", " - "
           "UseMetal", " - "
           "UseGlass", " - "
        """
        UseMatte = 0  # DecalBuilderDecalReflectivitiesMemberType
        UsePlastic = 1  # DecalBuilderDecalReflectivitiesMemberType
        UseMirror = 2  # DecalBuilderDecalReflectivitiesMemberType
        UseMetal = 3  # DecalBuilderDecalReflectivitiesMemberType
        UseGlass = 4  # DecalBuilderDecalReflectivitiesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Anchor():
        """
        image anchor 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "TopLeft", "anchor at top left corner of decal image"
           "Center", "anchor in the middle of decal image"
           "BottomLeft", "anchor at the bottom left corner of decal image"
           "TopMiddle", "anchor at top middle corner of decal image"
           "TopRight", "anchor at top right corner of decal image"
           "LeftMiddle", "anchor at left middle corner of decal image"
           "RightMiddle", "anchor at right middle corner of decal image"
           "BottomMiddle", "anchor at bottom middle corner of decal image"
           "BottomRight", "anchor at bottom right corner of decal image"
        """
        TopLeft = 0  # DecalBuilderAnchorMemberType
        Center = 1  # DecalBuilderAnchorMemberType
        BottomLeft = 2  # DecalBuilderAnchorMemberType
        TopMiddle = 3  # DecalBuilderAnchorMemberType
        TopRight = 4  # DecalBuilderAnchorMemberType
        LeftMiddle = 5  # DecalBuilderAnchorMemberType
        RightMiddle = 6  # DecalBuilderAnchorMemberType
        BottomMiddle = 7  # DecalBuilderAnchorMemberType
        BottomRight = 8  # DecalBuilderAnchorMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Scaling():
        """
        decal scaling type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ToFace", "scale the decal based on face size"
           "ToImageSize", "scale the decal based on true decal image size"
           "ToUniformScale", "scale the decal based on uniform scale"
           "ToNonUniformScale", "scale the decal based on both width and height scale"
        """
        ToFace = 0  # DecalBuilderScalingMemberType
        ToImageSize = 1  # DecalBuilderScalingMemberType
        ToUniformScale = 2  # DecalBuilderScalingMemberType
        ToNonUniformScale = 3  # DecalBuilderScalingMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetObject(self) -> NXOpen.NXObject:
        """
        Returns the object currently being edited by this builder.  
        
        If
        a new object is being created, and the builder has not yet
        been commited, returns None.
        
        Signature ``GetObject()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTransparencyColor(self) -> 'list[float]':
        """
        Returns the transparency color  
        
        Signature ``GetTransparencyColor()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTransparencyColor(self, transparencyColor: 'list[float]') -> None:
        """
        Sets the transparency color 
        
        Signature ``SetTransparencyColor(transparencyColor)`` 
        
        :param transparencyColor: 
        :type transparencyColor: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetImagesInPart(self) -> 'list[str]':
        """
        Provide a list of names of the :py:class:`NXOpen.Display.ImageData`
        objects saved in current part file.  
        
        Signature ``GetImagesInPart()`` 
        
        :returns:  Array of :py:class:`NXOpen.Display.ImageData` names  
        :rtype: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetImageFromPart(self, imageName: str) -> None:
        """
        Set a :py:class:`NXOpen.Display.ImageData` object currently
        stored in the part as the image used by the builder.  
        
        Signature ``SetImageFromPart(imageName)`` 
        
        :param imageName:  Name of :py:class:`NXOpen.Display.ImageData` object  
        :type imageName: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    AnchorType: DecalBuilderAnchor = ...
    """
    Returns or sets  the anchor type 
    
    <hr>
    
    Getter Method
    
    Signature ``AnchorType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DecalBuilderAnchor` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnchorType`` 
    
    :param anchorType: 
    :type anchorType: :py:class:`NXOpen.Display.DecalBuilderAnchor` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    AspectRatio: float = ...
    """
    Returns or sets  the decal image aspect ratio 
    
    <hr>
    
    Getter Method
    
    Signature ``AspectRatio`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AspectRatio`` 
    
    :param aspectRatio: 
    :type aspectRatio: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    DecalName: str = ...
    """
    Returns or sets  the decal name 
    
    <hr>
    
    Getter Method
    
    Signature ``DecalName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DecalName`` 
    
    :param decalName: 
    :type decalName: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    DecalReflectivity: float = ...
    """
    Returns or sets  the decal reflectivity 
    
    <hr>
    
    Getter Method
    
    Signature ``DecalReflectivity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DecalReflectivity`` 
    
    :param decalReflectivity: 
    :type decalReflectivity: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    EnableEngraving: bool = ...
    """
    Returns or sets  the engraving enable toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``EnableEngraving`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnableEngraving`` 
    
    :param enableEngraving: 
    :type enableEngraving: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    EngravingAmplitude: float = ...
    """
    Returns or sets  the decal engraving amplitude 
    
    <hr>
    
    Getter Method
    
    Signature ``EngravingAmplitude`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EngravingAmplitude`` 
    
    :param engravingAmplitude: 
    :type engravingAmplitude: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    EngravingSoftness: float = ...
    """
    Returns or sets  the engraving softness 
    
    <hr>
    
    Getter Method
    
    Signature ``EngravingSoftness`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EngravingSoftness`` 
    
    :param engravingSoftness: 
    :type engravingSoftness: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    HeightScale: float = ...
    """
    Returns or sets  the decal height scale 
    
    <hr>
    
    Getter Method
    
    Signature ``HeightScale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HeightScale`` 
    
    :param heightScale: 
    :type heightScale: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    IlluminationType: DecalBuilderDecalIllumination = ...
    """
    Returns or sets  the illumination type 
    
    <hr>
    
    Getter Method
    
    Signature ``IlluminationType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DecalBuilderDecalIllumination` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IlluminationType`` 
    
    :param illuminationType: 
    :type illuminationType: :py:class:`NXOpen.Display.DecalBuilderDecalIllumination` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Image: Image = ...
    """
    Returns or sets  the image builder 
    
    <hr>
    
    Getter Method
    
    Signature ``Image`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Image`` 
    
    :param imageBuilder: 
    :type imageBuilder: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ImageFilename: str = ...
    """
    Returns or sets  the decal image file name 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageFilename`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageFilename`` 
    
    :param imageFileName: 
    :type imageFileName: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ImageSizeType: DecalBuilderImageSize = ...
    """
    Returns or sets  the image size type 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageSizeType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DecalBuilderImageSize` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageSizeType`` 
    
    :param imageSizeType: 
    :type imageSizeType: :py:class:`NXOpen.Display.DecalBuilderImageSize` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    NormalVector: NXOpen.Direction = ...
    """
    Returns or sets  the decal normal vector 
    
    <hr>
    
    Getter Method
    
    Signature ``NormalVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NormalVector`` 
    
    :param normalVector: 
    :type normalVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    NormalVectorValue: NXOpen.Vector3d = ...
    """
    Returns or sets  the decal normal vector value 
    
    <hr>
    
    Getter Method
    
    Signature ``NormalVectorValue`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NormalVectorValue`` 
    
    :param normalVectorValue: 
    :type normalVectorValue: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Object: NXOpen.SelectNXObjectList = ...
    """
    Returns  the object(face, body and facetted body) to apply the decal to 
    
    <hr>
    
    Getter Method
    
    Signature ``Object`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
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
    OriginPosition: NXOpen.Point3d = ...
    """
    Returns or sets  the origin_pos 
    
    <hr>
    
    Getter Method
    
    Signature ``OriginPosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OriginPosition`` 
    
    :param originPosition: 
    :type originPosition: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    OverwriteExistingFile: bool = ...
    """
    Returns or sets  the overwrite existing file option - true to overwrite and return no error, false to return error 
    
    <hr>
    
    Getter Method
    
    Signature ``OverwriteExistingFile`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OverwriteExistingFile`` 
    
    :param overwriteExistingFile: 
    :type overwriteExistingFile: bool 
    
    .. versionadded:: NX10.0.3
    
    License requirements: None.
    """
    ReflectivityType: DecalBuilderDecalReflectivities = ...
    """
    Returns or sets  the reflectivity type 
    
    <hr>
    
    Getter Method
    
    Signature ``ReflectivityType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DecalBuilderDecalReflectivities` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReflectivityType`` 
    
    :param reflectivityType: 
    :type reflectivityType: :py:class:`NXOpen.Display.DecalBuilderDecalReflectivities` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    """
    Rotation: float = ...
    """
    Returns or sets  the decal rotation 
    
    <hr>
    
    Getter Method
    
    Signature ``Rotation`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Rotation`` 
    
    :param rotation: 
    :type rotation: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Scale: float = ...
    """
    Returns or sets  the decal scale 
    
    <hr>
    
    Getter Method
    
    Signature ``Scale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Scale`` 
    
    :param scale: 
    :type scale: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ScalingType: DecalBuilderScaling = ...
    """
    Returns or sets  the scaling type 
    
    <hr>
    
    Getter Method
    
    Signature ``ScalingType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DecalBuilderScaling` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScalingType`` 
    
    :param scalingType: 
    :type scalingType: :py:class:`NXOpen.Display.DecalBuilderScaling` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    StencilPreview: bool = ...
    """
    Returns or sets  the stencil preview toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``StencilPreview`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StencilPreview`` 
    
    :param stencilPreview: 
    :type stencilPreview: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    TransparencyTolerance: int = ...
    """
    Returns or sets  the transparency tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``TransparencyTolerance`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TransparencyTolerance`` 
    
    :param transparencyTolerance: 
    :type transparencyTolerance: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    UpVector: NXOpen.Direction = ...
    """
    Returns or sets  the decal up vector 
    
    <hr>
    
    Getter Method
    
    Signature ``UpVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UpVector`` 
    
    :param upVector: 
    :type upVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    UpVectorValue: NXOpen.Vector3d = ...
    """
    Returns or sets  the decal up vector value 
    
    <hr>
    
    Getter Method
    
    Signature ``UpVectorValue`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UpVectorValue`` 
    
    :param upVectorValue: 
    :type upVectorValue: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    WidthScale: float = ...
    """
    Returns or sets  the decal width scale 
    
    <hr>
    
    Getter Method
    
    Signature ``WidthScale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WidthScale`` 
    
    :param widthScale: 
    :type widthScale: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: DecalBuilder = ...  # unknown typename


class SectionCurveSettingsBuilderColorOptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionCurveSettingsBuilderColorOptionType():
    """
    Specifies the color of the curves. When color is set to 
    body color, user specified color will be ignored.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Body", "Use body color"
       "Any", "Use specified color"
    """
    Body = 0  # SectionCurveSettingsBuilderColorOptionTypeMemberType
    Any = 1  # SectionCurveSettingsBuilderColorOptionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionCurveSettingsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Display.SectionCurveSettingsBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    class ColorOptionType():
        """
        Specifies the color of the curves. When color is set to 
        body color, user specified color will be ignored.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Body", "Use body color"
           "Any", "Use specified color"
        """
        Body = 0  # SectionCurveSettingsBuilderColorOptionTypeMemberType
        Any = 1  # SectionCurveSettingsBuilderColorOptionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    Color: NXOpen.NXColor = ...
    """
    Returns or sets  the curve color.  
    
    Used when the curve color option is set to
    :py:class:`NXOpen.Display.SectionCurveSettingsBuilderColorOptionType.Any
    <NXOpen.Display.SectionCurveSettingsBuilderColorOptionType>`.
    
    <hr>
    
    Getter Method
    
    Signature ``Color`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Color`` 
    
    :param curveColor: 
    :type curveColor: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ColorOption: SectionCurveSettingsBuilderColorOptionType = ...
    """
    Returns or sets  the curve color option 
    
    <hr>
    
    Getter Method
    
    Signature ``ColorOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.SectionCurveSettingsBuilderColorOptionType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColorOption`` 
    
    :param curveColorOption: 
    :type curveColorOption: :py:class:`NXOpen.Display.SectionCurveSettingsBuilderColorOptionType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Show: bool = ...
    """
    Returns or sets  the curve on off flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``Show`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Show`` 
    
    :param showCurves: 
    :type showCurves: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: SectionCurveSettingsBuilder = ...  # unknown typename


class TrueShadingBuilderMaterialTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TrueShadingBuilderMaterialType():
    """
    Global material and per object overriding material types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "GlobalWashShinyMetal", "Shiny Metal Wash"
       "GlobalWashBrushedMetal", "Brushed Metal Wash"
       "GlobalWashShinyPlastic", "Shiny Plastic Wash"
       "GlobalWashAnalysis", "Surface Analysis Wash"
       "GlobalWashFlat", "Low Sheen Plastic Wash"
       "GlobalRedGlossyPlastic", "Red Glossy Plastic"
       "GlobalBlueGlossyPlastic", "Blue Glossy Plastic"
       "GlobalGreenGlossyPlastic", "Green Glossy Plastic"
       "GlobalGrayGlossyPlastic", "Gray Glossy Plastic"
       "GlobalBlackGlossyPlastic", "Black Glossy Plastic"
       "GlobalBrownGlossyPlastic", "Brown Glossy Plastic"
       "GlobalYellowGlossyPlastic", "Yellow Glossy Plastic"
       "GlobalTealGlossyPlastic", "Teal Glossy Plastic"
       "GlobalWhiteGlossyPlastic", "White Glossy Plastic"
       "GlobalClearPlastic", "Clear Plastic"
       "GlobalChrome", "Chrome"
       "GlobalCopper", "Copper"
       "GlobalGold", "Gold"
       "GlobalBrass", "Brass"
       "GlobalSteel", "Steel"
       "GlobalBrushedChrome", "Brushed Chrome"
       "GlobalBrushedAluminum", "Brushed Aluminum"
       "GlobalBrushedTitanium", "Brushed Titanium"
       "GlobalGlassClear", "Clear Glass"
       "GlobalGlassSmokey", "Smokey Glass"
       "GlobalMetallicPaintRed", "Red Metallic Paint"
       "GlobalMetallicPaintGray", "Gray Metallic Paint"
       "GlobalMetallicPaintBlack", "Black Metallic Paint"
       "GlobalMetallicPaintBlue", "Blue Metallic Paint"
       "GlobalRubber", "Black Rubber"
       "OverrideRedGlossyPlastic", "Red Glossy Plastic"
       "OverrideBlueGlossyPlastic", "Blue Glossy Plastic"
       "OverrideGreenGlossyPlastic", "Green Glossy Plastic"
       "OverrideGrayGlossyPlastic", "Gray Glossy Plastic"
       "OverrideBlackGlossyPlastic", "Black Glossy Plastic"
       "OverrideBrownGlossyPlastic", "Brown Glossy Plastic"
       "OverrideYellowGlossyPlastic", "Yellow Glossy Plastic"
       "OverrideTealGlossyPlastic", "Teal Glossy Plastic"
       "OverrideWhiteGlossyPlastic", "White Glossy Plastic"
       "OverrideClearPlastic", "Clear Plastic"
       "OverrideChrome", "Chrome"
       "OverrideCopper", "Copper"
       "OverrideGold", "Gold"
       "OverrideBrass", "Brass"
       "OverrideSteel", "Steel"
       "OverrideBrushedChrome", "Brushed Chrome"
       "OverrideBrushedAluminum", "Brushed Aluminum"
       "OverrideBrushedTitanium", "Brushed Titanium"
       "OverrideGlassClear", "Clear Glass"
       "OverrideGlassSmokey", "Smokey Glass"
       "OverrideMetallicPaintRed", "Red Metallic Paint"
       "OverrideMetallicPaintGray", "Gray Metallic Paint"
       "OverrideMetallicPaintBlack", "Black Metallic Paint"
       "OverrideMetallicPaintBlue", "Blue Metallic Paint"
       "OverrideRubber", "Black Rubber"
       "OverrideRoughMetalMedGray", "Medium Grey Texture"
       "OverrideRoughMetalDkGray", "Dark Grey Texture"
       "OverrideRoughPlasticBlueGray", "Blue Grey Texture"
       "OverrideRoughPlasticTan", "Tan Texture"
    """
    GlobalWashShinyMetal = 0  # TrueShadingBuilderMaterialTypeMemberType
    GlobalWashBrushedMetal = 1  # TrueShadingBuilderMaterialTypeMemberType
    GlobalWashShinyPlastic = 2  # TrueShadingBuilderMaterialTypeMemberType
    GlobalWashAnalysis = 3  # TrueShadingBuilderMaterialTypeMemberType
    GlobalWashFlat = 4  # TrueShadingBuilderMaterialTypeMemberType
    GlobalRedGlossyPlastic = 5  # TrueShadingBuilderMaterialTypeMemberType
    GlobalBlueGlossyPlastic = 6  # TrueShadingBuilderMaterialTypeMemberType
    GlobalGreenGlossyPlastic = 7  # TrueShadingBuilderMaterialTypeMemberType
    GlobalGrayGlossyPlastic = 8  # TrueShadingBuilderMaterialTypeMemberType
    GlobalBlackGlossyPlastic = 9  # TrueShadingBuilderMaterialTypeMemberType
    GlobalBrownGlossyPlastic = 10  # TrueShadingBuilderMaterialTypeMemberType
    GlobalYellowGlossyPlastic = 11  # TrueShadingBuilderMaterialTypeMemberType
    GlobalTealGlossyPlastic = 12  # TrueShadingBuilderMaterialTypeMemberType
    GlobalWhiteGlossyPlastic = 13  # TrueShadingBuilderMaterialTypeMemberType
    GlobalClearPlastic = 14  # TrueShadingBuilderMaterialTypeMemberType
    GlobalChrome = 15  # TrueShadingBuilderMaterialTypeMemberType
    GlobalCopper = 16  # TrueShadingBuilderMaterialTypeMemberType
    GlobalGold = 17  # TrueShadingBuilderMaterialTypeMemberType
    GlobalBrass = 18  # TrueShadingBuilderMaterialTypeMemberType
    GlobalSteel = 19  # TrueShadingBuilderMaterialTypeMemberType
    GlobalBrushedChrome = 20  # TrueShadingBuilderMaterialTypeMemberType
    GlobalBrushedAluminum = 21  # TrueShadingBuilderMaterialTypeMemberType
    GlobalBrushedTitanium = 22  # TrueShadingBuilderMaterialTypeMemberType
    GlobalGlassClear = 23  # TrueShadingBuilderMaterialTypeMemberType
    GlobalGlassSmokey = 24  # TrueShadingBuilderMaterialTypeMemberType
    GlobalMetallicPaintRed = 25  # TrueShadingBuilderMaterialTypeMemberType
    GlobalMetallicPaintGray = 26  # TrueShadingBuilderMaterialTypeMemberType
    GlobalMetallicPaintBlack = 27  # TrueShadingBuilderMaterialTypeMemberType
    GlobalMetallicPaintBlue = 28  # TrueShadingBuilderMaterialTypeMemberType
    GlobalRubber = 29  # TrueShadingBuilderMaterialTypeMemberType
    OverrideRedGlossyPlastic = 30  # TrueShadingBuilderMaterialTypeMemberType
    OverrideBlueGlossyPlastic = 31  # TrueShadingBuilderMaterialTypeMemberType
    OverrideGreenGlossyPlastic = 32  # TrueShadingBuilderMaterialTypeMemberType
    OverrideGrayGlossyPlastic = 33  # TrueShadingBuilderMaterialTypeMemberType
    OverrideBlackGlossyPlastic = 34  # TrueShadingBuilderMaterialTypeMemberType
    OverrideBrownGlossyPlastic = 35  # TrueShadingBuilderMaterialTypeMemberType
    OverrideYellowGlossyPlastic = 36  # TrueShadingBuilderMaterialTypeMemberType
    OverrideTealGlossyPlastic = 37  # TrueShadingBuilderMaterialTypeMemberType
    OverrideWhiteGlossyPlastic = 38  # TrueShadingBuilderMaterialTypeMemberType
    OverrideClearPlastic = 39  # TrueShadingBuilderMaterialTypeMemberType
    OverrideChrome = 40  # TrueShadingBuilderMaterialTypeMemberType
    OverrideCopper = 41  # TrueShadingBuilderMaterialTypeMemberType
    OverrideGold = 42  # TrueShadingBuilderMaterialTypeMemberType
    OverrideBrass = 43  # TrueShadingBuilderMaterialTypeMemberType
    OverrideSteel = 44  # TrueShadingBuilderMaterialTypeMemberType
    OverrideBrushedChrome = 45  # TrueShadingBuilderMaterialTypeMemberType
    OverrideBrushedAluminum = 46  # TrueShadingBuilderMaterialTypeMemberType
    OverrideBrushedTitanium = 47  # TrueShadingBuilderMaterialTypeMemberType
    OverrideGlassClear = 48  # TrueShadingBuilderMaterialTypeMemberType
    OverrideGlassSmokey = 49  # TrueShadingBuilderMaterialTypeMemberType
    OverrideMetallicPaintRed = 50  # TrueShadingBuilderMaterialTypeMemberType
    OverrideMetallicPaintGray = 51  # TrueShadingBuilderMaterialTypeMemberType
    OverrideMetallicPaintBlack = 52  # TrueShadingBuilderMaterialTypeMemberType
    OverrideMetallicPaintBlue = 53  # TrueShadingBuilderMaterialTypeMemberType
    OverrideRubber = 54  # TrueShadingBuilderMaterialTypeMemberType
    OverrideRoughMetalMedGray = 55  # TrueShadingBuilderMaterialTypeMemberType
    OverrideRoughMetalDkGray = 56  # TrueShadingBuilderMaterialTypeMemberType
    OverrideRoughPlasticBlueGray = 57  # TrueShadingBuilderMaterialTypeMemberType
    OverrideRoughPlasticTan = 58  # TrueShadingBuilderMaterialTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TrueShadingBuilderEnvironmentMapTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TrueShadingBuilderEnvironmentMapType():
    """
    Global environment reflection map types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Default", "No reflection map"
       "MetalShiny1", "Shiny Metal Reflection 1"
       "MetalShiny2", "Shiny Metal Reflection 2"
       "MetalBrushed1", "Brushed Metal Reflection 1"
       "MetalBrushed2", "Brushed Metal Reflection 2"
       "Glossy1", "Glossy Reflection 1"
       "Glossy2", "Glossy Reflection 2"
       "SurfaceAnalysisLines", "Surface Analysis Lines Reflection"
       "SurfaceAnalysisHorizon", "Surface Analysis Horizontal Lines Reflection"
       "AutoPhotoStudio", "Automotive Lighting Reflection"
       "CustomImage", "Custom Image Reflection"
    """
    Default = 0  # TrueShadingBuilderEnvironmentMapTypeMemberType
    MetalShiny1 = 1  # TrueShadingBuilderEnvironmentMapTypeMemberType
    MetalShiny2 = 2  # TrueShadingBuilderEnvironmentMapTypeMemberType
    MetalBrushed1 = 3  # TrueShadingBuilderEnvironmentMapTypeMemberType
    MetalBrushed2 = 4  # TrueShadingBuilderEnvironmentMapTypeMemberType
    Glossy1 = 5  # TrueShadingBuilderEnvironmentMapTypeMemberType
    Glossy2 = 6  # TrueShadingBuilderEnvironmentMapTypeMemberType
    SurfaceAnalysisLines = 7  # TrueShadingBuilderEnvironmentMapTypeMemberType
    SurfaceAnalysisHorizon = 8  # TrueShadingBuilderEnvironmentMapTypeMemberType
    AutoPhotoStudio = 9  # TrueShadingBuilderEnvironmentMapTypeMemberType
    CustomImage = 10  # TrueShadingBuilderEnvironmentMapTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TrueShadingBuilderBgdTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TrueShadingBuilderBgdType():
    """
    Background colors and image types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DarkGraduated", "Graduated dark colored background"
       "LightGraduated", "Graduated light colored background"
       "Black", "Plain dark Colored background"
       "White", "Plain light Colored background"
       "CustomPlain", "Customized plain colored background"
       "CustomGraduated", "Customized graduated colored background"
       "InheritShadedBackground", "Use same background color as in shaded display mode"
       "ImageBackground", "Use one of the predefined images as background"
       "PureWhite", "Plain light Colored background"
    """
    DarkGraduated = 0  # TrueShadingBuilderBgdTypeMemberType
    LightGraduated = 1  # TrueShadingBuilderBgdTypeMemberType
    Black = 2  # TrueShadingBuilderBgdTypeMemberType
    White = 3  # TrueShadingBuilderBgdTypeMemberType
    CustomPlain = 4  # TrueShadingBuilderBgdTypeMemberType
    CustomGraduated = 5  # TrueShadingBuilderBgdTypeMemberType
    InheritShadedBackground = 6  # TrueShadingBuilderBgdTypeMemberType
    ImageBackground = 7  # TrueShadingBuilderBgdTypeMemberType
    PureWhite = 8  # TrueShadingBuilderBgdTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TrueShadingBuilderBgdImageTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TrueShadingBuilderBgdImageType():
    """
    Background image types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Image1", "Predefined image 1 background"
       "Image2", "Predefined image 2 background"
       "Image3", "Predefined image 3 background"
       "Image4", "Predefined image 4 background"
       "Image5", "Predefined image 5 background"
       "Image6", "Predefined image 6 background"
       "CustomImage", "Custom image background"
    """
    Image1 = 0  # TrueShadingBuilderBgdImageTypeMemberType
    Image2 = 1  # TrueShadingBuilderBgdImageTypeMemberType
    Image3 = 2  # TrueShadingBuilderBgdImageTypeMemberType
    Image4 = 3  # TrueShadingBuilderBgdImageTypeMemberType
    Image5 = 4  # TrueShadingBuilderBgdImageTypeMemberType
    Image6 = 5  # TrueShadingBuilderBgdImageTypeMemberType
    CustomImage = 6  # TrueShadingBuilderBgdImageTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TrueShadingBuilderSurfaceOrientTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TrueShadingBuilderSurfaceOrientType():
    """
    Shadow plane projection orientation types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Do not project shadows"
       "Bottom", "Project shadows onto the floor"
       "Back", "Project shadows onto the back wall"
       "BottomFixed", "Project shadows onto a fixed oriented floor"
    """
    NotSet = 0  # TrueShadingBuilderSurfaceOrientTypeMemberType
    Bottom = 1  # TrueShadingBuilderSurfaceOrientTypeMemberType
    Back = 2  # TrueShadingBuilderSurfaceOrientTypeMemberType
    BottomFixed = 3  # TrueShadingBuilderSurfaceOrientTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TrueShadingBuilderSHEDLightCollectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TrueShadingBuilderSHEDLightCollectionType():
    """
    Scene lighting collection types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DefaultLights", "Scene lighting collection 1"
       "Lighting1", "Scene lighting collection 2"
       "Lighting2", "Scene lighting collection 3"
       "Lighting3", "Scene lighting collection 4"
       "Lighting4", "Scene lighting collection 5"
       "Custom", "Custom lighting configuration"
    """
    DefaultLights = 0  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
    Lighting1 = 1  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
    Lighting2 = 2  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
    Lighting3 = 3  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
    Lighting4 = 4  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
    Custom = 5  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TrueShadingBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.TrueShading` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Display.TrueShadingCollection.CreateTrueShadingBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    class MaterialType():
        """
        Global material and per object overriding material types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "GlobalWashShinyMetal", "Shiny Metal Wash"
           "GlobalWashBrushedMetal", "Brushed Metal Wash"
           "GlobalWashShinyPlastic", "Shiny Plastic Wash"
           "GlobalWashAnalysis", "Surface Analysis Wash"
           "GlobalWashFlat", "Low Sheen Plastic Wash"
           "GlobalRedGlossyPlastic", "Red Glossy Plastic"
           "GlobalBlueGlossyPlastic", "Blue Glossy Plastic"
           "GlobalGreenGlossyPlastic", "Green Glossy Plastic"
           "GlobalGrayGlossyPlastic", "Gray Glossy Plastic"
           "GlobalBlackGlossyPlastic", "Black Glossy Plastic"
           "GlobalBrownGlossyPlastic", "Brown Glossy Plastic"
           "GlobalYellowGlossyPlastic", "Yellow Glossy Plastic"
           "GlobalTealGlossyPlastic", "Teal Glossy Plastic"
           "GlobalWhiteGlossyPlastic", "White Glossy Plastic"
           "GlobalClearPlastic", "Clear Plastic"
           "GlobalChrome", "Chrome"
           "GlobalCopper", "Copper"
           "GlobalGold", "Gold"
           "GlobalBrass", "Brass"
           "GlobalSteel", "Steel"
           "GlobalBrushedChrome", "Brushed Chrome"
           "GlobalBrushedAluminum", "Brushed Aluminum"
           "GlobalBrushedTitanium", "Brushed Titanium"
           "GlobalGlassClear", "Clear Glass"
           "GlobalGlassSmokey", "Smokey Glass"
           "GlobalMetallicPaintRed", "Red Metallic Paint"
           "GlobalMetallicPaintGray", "Gray Metallic Paint"
           "GlobalMetallicPaintBlack", "Black Metallic Paint"
           "GlobalMetallicPaintBlue", "Blue Metallic Paint"
           "GlobalRubber", "Black Rubber"
           "OverrideRedGlossyPlastic", "Red Glossy Plastic"
           "OverrideBlueGlossyPlastic", "Blue Glossy Plastic"
           "OverrideGreenGlossyPlastic", "Green Glossy Plastic"
           "OverrideGrayGlossyPlastic", "Gray Glossy Plastic"
           "OverrideBlackGlossyPlastic", "Black Glossy Plastic"
           "OverrideBrownGlossyPlastic", "Brown Glossy Plastic"
           "OverrideYellowGlossyPlastic", "Yellow Glossy Plastic"
           "OverrideTealGlossyPlastic", "Teal Glossy Plastic"
           "OverrideWhiteGlossyPlastic", "White Glossy Plastic"
           "OverrideClearPlastic", "Clear Plastic"
           "OverrideChrome", "Chrome"
           "OverrideCopper", "Copper"
           "OverrideGold", "Gold"
           "OverrideBrass", "Brass"
           "OverrideSteel", "Steel"
           "OverrideBrushedChrome", "Brushed Chrome"
           "OverrideBrushedAluminum", "Brushed Aluminum"
           "OverrideBrushedTitanium", "Brushed Titanium"
           "OverrideGlassClear", "Clear Glass"
           "OverrideGlassSmokey", "Smokey Glass"
           "OverrideMetallicPaintRed", "Red Metallic Paint"
           "OverrideMetallicPaintGray", "Gray Metallic Paint"
           "OverrideMetallicPaintBlack", "Black Metallic Paint"
           "OverrideMetallicPaintBlue", "Blue Metallic Paint"
           "OverrideRubber", "Black Rubber"
           "OverrideRoughMetalMedGray", "Medium Grey Texture"
           "OverrideRoughMetalDkGray", "Dark Grey Texture"
           "OverrideRoughPlasticBlueGray", "Blue Grey Texture"
           "OverrideRoughPlasticTan", "Tan Texture"
        """
        GlobalWashShinyMetal = 0  # TrueShadingBuilderMaterialTypeMemberType
        GlobalWashBrushedMetal = 1  # TrueShadingBuilderMaterialTypeMemberType
        GlobalWashShinyPlastic = 2  # TrueShadingBuilderMaterialTypeMemberType
        GlobalWashAnalysis = 3  # TrueShadingBuilderMaterialTypeMemberType
        GlobalWashFlat = 4  # TrueShadingBuilderMaterialTypeMemberType
        GlobalRedGlossyPlastic = 5  # TrueShadingBuilderMaterialTypeMemberType
        GlobalBlueGlossyPlastic = 6  # TrueShadingBuilderMaterialTypeMemberType
        GlobalGreenGlossyPlastic = 7  # TrueShadingBuilderMaterialTypeMemberType
        GlobalGrayGlossyPlastic = 8  # TrueShadingBuilderMaterialTypeMemberType
        GlobalBlackGlossyPlastic = 9  # TrueShadingBuilderMaterialTypeMemberType
        GlobalBrownGlossyPlastic = 10  # TrueShadingBuilderMaterialTypeMemberType
        GlobalYellowGlossyPlastic = 11  # TrueShadingBuilderMaterialTypeMemberType
        GlobalTealGlossyPlastic = 12  # TrueShadingBuilderMaterialTypeMemberType
        GlobalWhiteGlossyPlastic = 13  # TrueShadingBuilderMaterialTypeMemberType
        GlobalClearPlastic = 14  # TrueShadingBuilderMaterialTypeMemberType
        GlobalChrome = 15  # TrueShadingBuilderMaterialTypeMemberType
        GlobalCopper = 16  # TrueShadingBuilderMaterialTypeMemberType
        GlobalGold = 17  # TrueShadingBuilderMaterialTypeMemberType
        GlobalBrass = 18  # TrueShadingBuilderMaterialTypeMemberType
        GlobalSteel = 19  # TrueShadingBuilderMaterialTypeMemberType
        GlobalBrushedChrome = 20  # TrueShadingBuilderMaterialTypeMemberType
        GlobalBrushedAluminum = 21  # TrueShadingBuilderMaterialTypeMemberType
        GlobalBrushedTitanium = 22  # TrueShadingBuilderMaterialTypeMemberType
        GlobalGlassClear = 23  # TrueShadingBuilderMaterialTypeMemberType
        GlobalGlassSmokey = 24  # TrueShadingBuilderMaterialTypeMemberType
        GlobalMetallicPaintRed = 25  # TrueShadingBuilderMaterialTypeMemberType
        GlobalMetallicPaintGray = 26  # TrueShadingBuilderMaterialTypeMemberType
        GlobalMetallicPaintBlack = 27  # TrueShadingBuilderMaterialTypeMemberType
        GlobalMetallicPaintBlue = 28  # TrueShadingBuilderMaterialTypeMemberType
        GlobalRubber = 29  # TrueShadingBuilderMaterialTypeMemberType
        OverrideRedGlossyPlastic = 30  # TrueShadingBuilderMaterialTypeMemberType
        OverrideBlueGlossyPlastic = 31  # TrueShadingBuilderMaterialTypeMemberType
        OverrideGreenGlossyPlastic = 32  # TrueShadingBuilderMaterialTypeMemberType
        OverrideGrayGlossyPlastic = 33  # TrueShadingBuilderMaterialTypeMemberType
        OverrideBlackGlossyPlastic = 34  # TrueShadingBuilderMaterialTypeMemberType
        OverrideBrownGlossyPlastic = 35  # TrueShadingBuilderMaterialTypeMemberType
        OverrideYellowGlossyPlastic = 36  # TrueShadingBuilderMaterialTypeMemberType
        OverrideTealGlossyPlastic = 37  # TrueShadingBuilderMaterialTypeMemberType
        OverrideWhiteGlossyPlastic = 38  # TrueShadingBuilderMaterialTypeMemberType
        OverrideClearPlastic = 39  # TrueShadingBuilderMaterialTypeMemberType
        OverrideChrome = 40  # TrueShadingBuilderMaterialTypeMemberType
        OverrideCopper = 41  # TrueShadingBuilderMaterialTypeMemberType
        OverrideGold = 42  # TrueShadingBuilderMaterialTypeMemberType
        OverrideBrass = 43  # TrueShadingBuilderMaterialTypeMemberType
        OverrideSteel = 44  # TrueShadingBuilderMaterialTypeMemberType
        OverrideBrushedChrome = 45  # TrueShadingBuilderMaterialTypeMemberType
        OverrideBrushedAluminum = 46  # TrueShadingBuilderMaterialTypeMemberType
        OverrideBrushedTitanium = 47  # TrueShadingBuilderMaterialTypeMemberType
        OverrideGlassClear = 48  # TrueShadingBuilderMaterialTypeMemberType
        OverrideGlassSmokey = 49  # TrueShadingBuilderMaterialTypeMemberType
        OverrideMetallicPaintRed = 50  # TrueShadingBuilderMaterialTypeMemberType
        OverrideMetallicPaintGray = 51  # TrueShadingBuilderMaterialTypeMemberType
        OverrideMetallicPaintBlack = 52  # TrueShadingBuilderMaterialTypeMemberType
        OverrideMetallicPaintBlue = 53  # TrueShadingBuilderMaterialTypeMemberType
        OverrideRubber = 54  # TrueShadingBuilderMaterialTypeMemberType
        OverrideRoughMetalMedGray = 55  # TrueShadingBuilderMaterialTypeMemberType
        OverrideRoughMetalDkGray = 56  # TrueShadingBuilderMaterialTypeMemberType
        OverrideRoughPlasticBlueGray = 57  # TrueShadingBuilderMaterialTypeMemberType
        OverrideRoughPlasticTan = 58  # TrueShadingBuilderMaterialTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class EnvironmentMapType():
        """
        Global environment reflection map types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Default", "No reflection map"
           "MetalShiny1", "Shiny Metal Reflection 1"
           "MetalShiny2", "Shiny Metal Reflection 2"
           "MetalBrushed1", "Brushed Metal Reflection 1"
           "MetalBrushed2", "Brushed Metal Reflection 2"
           "Glossy1", "Glossy Reflection 1"
           "Glossy2", "Glossy Reflection 2"
           "SurfaceAnalysisLines", "Surface Analysis Lines Reflection"
           "SurfaceAnalysisHorizon", "Surface Analysis Horizontal Lines Reflection"
           "AutoPhotoStudio", "Automotive Lighting Reflection"
           "CustomImage", "Custom Image Reflection"
        """
        Default = 0  # TrueShadingBuilderEnvironmentMapTypeMemberType
        MetalShiny1 = 1  # TrueShadingBuilderEnvironmentMapTypeMemberType
        MetalShiny2 = 2  # TrueShadingBuilderEnvironmentMapTypeMemberType
        MetalBrushed1 = 3  # TrueShadingBuilderEnvironmentMapTypeMemberType
        MetalBrushed2 = 4  # TrueShadingBuilderEnvironmentMapTypeMemberType
        Glossy1 = 5  # TrueShadingBuilderEnvironmentMapTypeMemberType
        Glossy2 = 6  # TrueShadingBuilderEnvironmentMapTypeMemberType
        SurfaceAnalysisLines = 7  # TrueShadingBuilderEnvironmentMapTypeMemberType
        SurfaceAnalysisHorizon = 8  # TrueShadingBuilderEnvironmentMapTypeMemberType
        AutoPhotoStudio = 9  # TrueShadingBuilderEnvironmentMapTypeMemberType
        CustomImage = 10  # TrueShadingBuilderEnvironmentMapTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BgdType():
        """
        Background colors and image types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DarkGraduated", "Graduated dark colored background"
           "LightGraduated", "Graduated light colored background"
           "Black", "Plain dark Colored background"
           "White", "Plain light Colored background"
           "CustomPlain", "Customized plain colored background"
           "CustomGraduated", "Customized graduated colored background"
           "InheritShadedBackground", "Use same background color as in shaded display mode"
           "ImageBackground", "Use one of the predefined images as background"
           "PureWhite", "Plain light Colored background"
        """
        DarkGraduated = 0  # TrueShadingBuilderBgdTypeMemberType
        LightGraduated = 1  # TrueShadingBuilderBgdTypeMemberType
        Black = 2  # TrueShadingBuilderBgdTypeMemberType
        White = 3  # TrueShadingBuilderBgdTypeMemberType
        CustomPlain = 4  # TrueShadingBuilderBgdTypeMemberType
        CustomGraduated = 5  # TrueShadingBuilderBgdTypeMemberType
        InheritShadedBackground = 6  # TrueShadingBuilderBgdTypeMemberType
        ImageBackground = 7  # TrueShadingBuilderBgdTypeMemberType
        PureWhite = 8  # TrueShadingBuilderBgdTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BgdImageType():
        """
        Background image types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Image1", "Predefined image 1 background"
           "Image2", "Predefined image 2 background"
           "Image3", "Predefined image 3 background"
           "Image4", "Predefined image 4 background"
           "Image5", "Predefined image 5 background"
           "Image6", "Predefined image 6 background"
           "CustomImage", "Custom image background"
        """
        Image1 = 0  # TrueShadingBuilderBgdImageTypeMemberType
        Image2 = 1  # TrueShadingBuilderBgdImageTypeMemberType
        Image3 = 2  # TrueShadingBuilderBgdImageTypeMemberType
        Image4 = 3  # TrueShadingBuilderBgdImageTypeMemberType
        Image5 = 4  # TrueShadingBuilderBgdImageTypeMemberType
        Image6 = 5  # TrueShadingBuilderBgdImageTypeMemberType
        CustomImage = 6  # TrueShadingBuilderBgdImageTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SurfaceOrientType():
        """
        Shadow plane projection orientation types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Do not project shadows"
           "Bottom", "Project shadows onto the floor"
           "Back", "Project shadows onto the back wall"
           "BottomFixed", "Project shadows onto a fixed oriented floor"
        """
        NotSet = 0  # TrueShadingBuilderSurfaceOrientTypeMemberType
        Bottom = 1  # TrueShadingBuilderSurfaceOrientTypeMemberType
        Back = 2  # TrueShadingBuilderSurfaceOrientTypeMemberType
        BottomFixed = 3  # TrueShadingBuilderSurfaceOrientTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SHEDLightCollectionType():
        """
        Scene lighting collection types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DefaultLights", "Scene lighting collection 1"
           "Lighting1", "Scene lighting collection 2"
           "Lighting2", "Scene lighting collection 3"
           "Lighting3", "Scene lighting collection 4"
           "Lighting4", "Scene lighting collection 5"
           "Custom", "Custom lighting configuration"
        """
        DefaultLights = 0  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
        Lighting1 = 1  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
        Lighting2 = 2  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
        Lighting3 = 3  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
        Lighting4 = 4  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
        Custom = 5  # TrueShadingBuilderSHEDLightCollectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def AssignOverrideMaterial(self, overrideMaterialType: TrueShadingBuilderMaterialType) -> None:
        """
        Assigns an overriding material type to one or more selected objects 
        
        Signature ``AssignOverrideMaterial(overrideMaterialType)`` 
        
        :param overrideMaterialType:  New material type  
        :type overrideMaterialType: :py:class:`NXOpen.Display.TrueShadingBuilderMaterialType` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton0(self) -> None:
        """
        Global material button 1 
        
        Signature ``GButton0()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton1(self) -> None:
        """
        Global material button 2 
        
        Signature ``GButton1()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton2(self) -> None:
        """
        Global material button 3 
        
        Signature ``GButton2()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton3(self) -> None:
        """
        Global material button 4 
        
        Signature ``GButton3()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton4(self) -> None:
        """
        Global material button 5 
        
        Signature ``GButton4()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton5(self) -> None:
        """
        Global material button 6 
        
        Signature ``GButton5()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton6(self) -> None:
        """
        Global material button 7 
        
        Signature ``GButton6()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton7(self) -> None:
        """
        Global material button 8 
        
        Signature ``GButton7()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton8(self) -> None:
        """
        Global material button 9 
        
        Signature ``GButton8()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton9(self) -> None:
        """
        Global material button 10 
        
        Signature ``GButton9()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton10(self) -> None:
        """
        Global material button 11 
        
        Signature ``GButton10()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton11(self) -> None:
        """
        Global material button 12 
        
        Signature ``GButton11()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton12(self) -> None:
        """
        Global material button 13 
        
        Signature ``GButton12()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton13(self) -> None:
        """
        Global material button 14 
        
        Signature ``GButton13()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton14(self) -> None:
        """
        Global material button 15 
        
        Signature ``GButton14()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton15(self) -> None:
        """
        Global material button 16 
        
        Signature ``GButton15()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton16(self) -> None:
        """
        Global material button 17 
        
        Signature ``GButton16()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton17(self) -> None:
        """
        Global material button 18 
        
        Signature ``GButton17()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton18(self) -> None:
        """
        Global material button 19 
        
        Signature ``GButton18()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton19(self) -> None:
        """
        Global material button 20 
        
        Signature ``GButton19()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton20(self) -> None:
        """
        Global material button 21 
        
        Signature ``GButton20()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton21(self) -> None:
        """
        Global material button 22 
        
        Signature ``GButton21()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton22(self) -> None:
        """
        Global material button 23 
        
        Signature ``GButton22()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton23(self) -> None:
        """
        Global material button 24 
        
        Signature ``GButton23()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton24(self) -> None:
        """
        Global material button 25 
        
        Signature ``GButton24()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton25(self) -> None:
        """
        Global material button 26 
        
        Signature ``GButton25()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton26(self) -> None:
        """
        Global material button 27 
        
        Signature ``GButton26()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton27(self) -> None:
        """
        Global material button 28 
        
        Signature ``GButton27()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton28(self) -> None:
        """
        Global material button 29 
        
        Signature ``GButton28()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GButton29(self) -> None:
        """
        Global material button 30 
        
        Signature ``GButton29()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton0(self) -> None:
        """
        Per Object override material button 1 
        
        Signature ``OButton0()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton1(self) -> None:
        """
        Per Object override material button 2 
        
        Signature ``OButton1()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton2(self) -> None:
        """
        Per Object override material button 3 
        
        Signature ``OButton2()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton3(self) -> None:
        """
        Per Object override material button 4 
        
        Signature ``OButton3()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton4(self) -> None:
        """
        Per Object override material button 5 
        
        Signature ``OButton4()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton5(self) -> None:
        """
        Per Object override material button 6 
        
        Signature ``OButton5()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton6(self) -> None:
        """
        Per Object override material button 7 
        
        Signature ``OButton6()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton7(self) -> None:
        """
        Per Object override material button 8 
        
        Signature ``OButton7()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton8(self) -> None:
        """
        Per Object override material button 9 
        
        Signature ``OButton8()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton9(self) -> None:
        """
        Per Object override material button 10 
        
        Signature ``OButton9()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton10(self) -> None:
        """
        Per Object override material button 11 
        
        Signature ``OButton10()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton11(self) -> None:
        """
        Per Object override material button 12 
        
        Signature ``OButton11()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton12(self) -> None:
        """
        Per Object override material button 13 
        
        Signature ``OButton12()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton13(self) -> None:
        """
        Per Object override material button 14 
        
        Signature ``OButton13()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton14(self) -> None:
        """
        Per Object override material button 15 
        
        Signature ``OButton14()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton15(self) -> None:
        """
        Per Object override material button 16 
        
        Signature ``OButton15()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton16(self) -> None:
        """
        Per Object override material button 17 
        
        Signature ``OButton16()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton17(self) -> None:
        """
        Per Object override material button 18 
        
        Signature ``OButton17()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton18(self) -> None:
        """
        Per Object override material button 19 
        
        Signature ``OButton18()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton19(self) -> None:
        """
        Per Object override material button 20 
        
        Signature ``OButton19()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton20(self) -> None:
        """
        Per Object override material button 21 
        
        Signature ``OButton20()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton21(self) -> None:
        """
        Per Object override material button 22 
        
        Signature ``OButton21()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton22(self) -> None:
        """
        Per Object override material button 23 
        
        Signature ``OButton22()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton23(self) -> None:
        """
        Per Object override material button 24 
        
        Signature ``OButton23()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton24(self) -> None:
        """
        Per Object override material button 25 
        
        Signature ``OButton24()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton25(self) -> None:
        """
        Per Object override material button 26 
        
        Signature ``OButton25()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton26(self) -> None:
        """
        Per Object override material button 27 
        
        Signature ``OButton26()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton27(self) -> None:
        """
        Per Object override material button 28 
        
        Signature ``OButton27()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OButton28(self) -> None:
        """
        Per Object override material button 29 
        
        Signature ``OButton28()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ORemoveButton(self) -> None:
        """
        Removes override material from selected object(s) 
        
        Signature ``ORemoveButton()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBgdTopRgbcolorPicker(self) -> 'list[float]':
        """
        Returns the RGB values of background top color picker  
        
        Signature ``GetBgdTopRgbcolorPicker()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBgdTopRgbcolorPicker(self, bgdTopRGBColorPicker: 'list[float]') -> None:
        """
        Sets the RGB values of background top color picker 
        
        Signature ``SetBgdTopRgbcolorPicker(bgdTopRGBColorPicker)`` 
        
        :param bgdTopRGBColorPicker:  Array of 3 RGB values, each between 0 and 1  
        :type bgdTopRGBColorPicker: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBgdBottomRgbcolorPicker(self) -> 'list[float]':
        """
        Returns the RGB values of background bottom color picker  
        
        Signature ``GetBgdBottomRgbcolorPicker()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBgdBottomRgbcolorPicker(self, bgdBottomRGBColorPicker: 'list[float]') -> None:
        """
        Sets the RGB values of background bottom color picker 
        
        Signature ``SetBgdBottomRgbcolorPicker(bgdBottomRGBColorPicker)`` 
        
        :param bgdBottomRGBColorPicker:  Array of 3 RGB values, each between 0 and 1  
        :type bgdBottomRGBColorPicker: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetGridRgbcolorPicker(self) -> 'list[float]':
        """
        Returns the grid RGB color values picker  
        
        Signature ``GetGridRgbcolorPicker()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetGridRgbcolorPicker(self, gridRGBColorPicker: 'list[float]') -> None:
        """
        Sets the grid RGB color picker 
        
        Signature ``SetGridRgbcolorPicker(gridRGBColorPicker)`` 
        
        :param gridRGBColorPicker:  Array of 3 RGB values, each between 0 and 1  
        :type gridRGBColorPicker: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ProtectUpdate(self) -> None:
        """
        Protects update 
        
        Signature ``ProtectUpdate()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    BgdImageEnum: TrueShadingBuilderBgdImageType = ...
    """
    Returns or sets  the background image list enum 
    
    <hr>
    
    Getter Method
    
    Signature ``BgdImageEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TrueShadingBuilderBgdImageType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BgdImageEnum`` 
    
    :param bgdImageEnum: 
    :type bgdImageEnum: :py:class:`NXOpen.Display.TrueShadingBuilderBgdImageType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    BgdImageFileBrowser: str = ...
    """
    Returns or sets  the background image filename 
    
    <hr>
    
    Getter Method
    
    Signature ``BgdImageFileBrowser`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BgdImageFileBrowser`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    BgdTypeEnum: TrueShadingBuilderBgdType = ...
    """
    Returns or sets  the background color or background image type enum 
    
    <hr>
    
    Getter Method
    
    Signature ``BgdTypeEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TrueShadingBuilderBgdType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BgdTypeEnum`` 
    
    :param bgdTypeEnum: 
    :type bgdTypeEnum: :py:class:`NXOpen.Display.TrueShadingBuilderBgdType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    EnvironmentMapEnum: TrueShadingBuilderEnvironmentMapType = ...
    """
    Returns or sets  the reflection environment map enum type 
    
    <hr>
    
    Getter Method
    
    Signature ``EnvironmentMapEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TrueShadingBuilderEnvironmentMapType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnvironmentMapEnum`` 
    
    :param environmentMapEnum: 
    :type environmentMapEnum: :py:class:`NXOpen.Display.TrueShadingBuilderEnvironmentMapType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    EnvironmentMapFileBrowser: str = ...
    """
    Returns or sets  the reflection environment map filename 
    
    <hr>
    
    Getter Method
    
    Signature ``EnvironmentMapFileBrowser`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnvironmentMapFileBrowser`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    GlobalMaterialType: TrueShadingBuilderMaterialType = ...
    """
    Returns or sets  the globalMaterialType 
    
    <hr>
    
    Getter Method
    
    Signature ``GlobalMaterialType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TrueShadingBuilderMaterialType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GlobalMaterialType`` 
    
    :param globalMaterialType: 
    :type globalMaterialType: :py:class:`NXOpen.Display.TrueShadingBuilderMaterialType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    InheritModelTogggle: bool = ...
    """
    Returns or sets  the shadow plane grid to inherit Model grid attributes toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``InheritModelTogggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InheritModelTogggle`` 
    
    :param inheritModelTogggle: 
    :type inheritModelTogggle: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    LightCollectionEnum: TrueShadingBuilderSHEDLightCollectionType = ...
    """
    Returns or sets  the light collection enum 
    
    <hr>
    
    Getter Method
    
    Signature ``LightCollectionEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TrueShadingBuilderSHEDLightCollectionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LightCollectionEnum`` 
    
    :param lightCollectionEnum: 
    :type lightCollectionEnum: :py:class:`NXOpen.Display.TrueShadingBuilderSHEDLightCollectionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    LightDimmerValue: float = ...
    """
    Returns or sets  the light dimmer value 
    
    <hr>
    
    Getter Method
    
    Signature ``LightDimmerValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LightDimmerValue`` 
    
    :param lightDimmerValue: 
    :type lightDimmerValue: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ObjSpecificSelection: NXOpen.SelectNXObjectList = ...
    """
    Returns  the selected object(s) list  
    
    <hr>
    
    Getter Method
    
    Signature ``ObjSpecificSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    PlanarReflectionToggle: bool = ...
    """
    Returns or sets  the planar reflection visibility toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``PlanarReflectionToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlanarReflectionToggle`` 
    
    :param planarReflectionToggle: 
    :type planarReflectionToggle: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    PlanarShadowToggle: bool = ...
    """
    Returns or sets  the planar shadow visibility toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``PlanarShadowToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlanarShadowToggle`` 
    
    :param planarShadowToggle: 
    :type planarShadowToggle: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    PlaneGridToggle: bool = ...
    """
    Returns or sets  the shadow plane grid visibility toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneGridToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneGridToggle`` 
    
    :param planeGridToggle: 
    :type planeGridToggle: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    PlaneOffsetFixedToggle: bool = ...
    """
    Returns or sets  the shadow plane with fixed offset toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneOffsetFixedToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneOffsetFixedToggle`` 
    
    :param planeOffsetFixedToggle: 
    :type planeOffsetFixedToggle: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    PlaneOffsetValue: float = ...
    """
    Returns or sets  the offset distance between the shadow plane and the nearest vertex of the displayed object 
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneOffsetValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneOffsetValue`` 
    
    :param planeOffsetValue: 
    :type planeOffsetValue: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ReflectivityValue: float = ...
    """
    Returns or sets  the reflectivity value 
    
    <hr>
    
    Getter Method
    
    Signature ``ReflectivityValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReflectivityValue`` 
    
    :param reflectivityValue: 
    :type reflectivityValue: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShedModeToggle: bool = ...
    """
    Returns or sets  the True Shading display toggle state 
    
    <hr>
    
    Getter Method
    
    Signature ``ShedModeToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShedModeToggle`` 
    
    :param shedModeToggle: 
    :type shedModeToggle: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SnapFloorToggle: bool = ...
    """
    Returns or sets  the toggle forces the shadow plane to snap to the nearest object vertex 
    
    <hr>
    
    Getter Method
    
    Signature ``SnapFloorToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapFloorToggle`` 
    
    :param snapFloorToggle: 
    :type snapFloorToggle: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SoftShadowsToggle: bool = ...
    """
    Returns or sets  the soft shadows toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``SoftShadowsToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SoftShadowsToggle`` 
    
    :param softShadowsToggle: 
    :type softShadowsToggle: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SpecifyPlane: NXOpen.Plane = ...
    """
    Returns or sets  the custom plane definition for the shadow projection 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifyPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpecifyPlane`` 
    
    :param specifyPlane: 
    :type specifyPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SurfaceOrientEnum: TrueShadingBuilderSurfaceOrientType = ...
    """
    Returns or sets  the shadow plane surface orientation enum 
    
    <hr>
    
    Getter Method
    
    Signature ``SurfaceOrientEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.TrueShadingBuilderSurfaceOrientType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SurfaceOrientEnum`` 
    
    :param surfaceOrientEnum: 
    :type surfaceOrientEnum: :py:class:`NXOpen.Display.TrueShadingBuilderSurfaceOrientType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: TrueShadingBuilder = ...  # unknown typename


class Grid(NXOpen.DisplayableObject, IDynamicSectionCutCreator):
    """
    Represents a grid   
    
    Grids are not supported in KF.
    
    .. versionadded:: NX6.0.0
    """
    
    def Find(self, journalIdentifier: str) -> DynamicSectionCut:
        """
        Finds the :py:class:`NXOpen.Display.DynamicSectionCut` 
        with the given identifier as recorded in a journal.  
        
        An object may 
        not return the same value as its JournalIdentifier in different 
        versions of  the software. However newer versions of the software 
        should find the same object when FindObject is passed older versions 
        of its journal identifier. In general, this method should not be 
        used in handwritten code and exists to support record and playback 
        of journals.
        
        An exception will be thrown if no object can be found with the 
        given journal identifier.  
        
        Signature ``Find(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Display.DynamicSectionCut` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSectionCuts(self, contextOccurrence: NXOpen.NXObject, view: NXOpen.View) -> 'list[DynamicSectionCut]':
        """
        Gets section-cuts generated by the sectioning the model shown
        in the specified view.  
        
        View must belong to the same part as the section-cut creator. If
        no view is specified, then section-cuts generated from the 
        sectionable entities in the part are returned.
        
        If a view is specified, then :py:class:`NXOpen.Assemblies.Explosion`
        active in the view is used to get section-cuts for the explosion.
        If the view does not have any active explosion, then
        section-cuts generated from the sectionable entities in the part 
        are returned. 
        
        Signature ``GetSectionCuts(contextOccurrence, view)`` 
        
        :param contextOccurrence:  This can be None. If non None, then this must                    be an occurrence.                  
        :type contextOccurrence: :py:class:`NXOpen.NXObject` 
        :param view: 
        :type view: :py:class:`NXOpen.View` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Display.DynamicSectionCut` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Grid = ...  # unknown typename


class BoundedGrid(Grid):
    """
    Represents a bounded grid   
    
    Bounded grids are not supported in KF.
    
    .. versionadded:: NX6.0.0
    """
    Null: BoundedGrid = ...  # unknown typename


class PlaneGrid(BoundedGrid):
    """
    Represents a grid on a bounded plane   
    
    Plane grids are not supported in KF.
    
    .. versionadded:: NX6.0.0
    """
    Null: PlaneGrid = ...  # unknown typename


class StageWallTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StageWallType():
    """
    Represents an index to a particular wall in the 
    stage.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "The left wall of the stage."
       "Right", "The right wall of the stage."
       "Top", "The top wall or "ceiling" of the stage."
       "Bottom", "The bottom wall or "floor" of the stage."
       "Front", "The front wall of the stage."
       "Back", "The back wall of the stage."
       "Total", "The total number of walls in the stage."
    """
    Left = 0  # StageWallTypeMemberType
    Right = 1  # StageWallTypeMemberType
    Top = 2  # StageWallTypeMemberType
    Bottom = 3  # StageWallTypeMemberType
    Front = 4  # StageWallTypeMemberType
    Back = 5  # StageWallTypeMemberType
    Total = 6  # StageWallTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StageOrientationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StageOrientationType():
    """
    Represents an index to a floor plane type define 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Yz", "Use yz plane for the stage floor."
       "Xz", "Use xz plane for the stage floor."
       "Xy", "Use xy plane for the stage floor."
       "UserDefined", "Use user defined plane for the stage floor."
    """
    Yz = 0  # StageOrientationTypeMemberType
    Xz = 1  # StageOrientationTypeMemberType
    Xy = 2  # StageOrientationTypeMemberType
    UserDefined = 3  # StageOrientationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Stage(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.Stage`
    A stage is an environment cube, a six-sided room, that can have between 
    one and six visible walls.  
    
    You optionally specify a stage in Studio 
    rendering styles and High Quality Images.
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateStage`
    
    .. versionadded:: NX5.0.0
    """
    
    class WallType():
        """
        Represents an index to a particular wall in the 
        stage.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Left", "The left wall of the stage."
           "Right", "The right wall of the stage."
           "Top", "The top wall or "ceiling" of the stage."
           "Bottom", "The bottom wall or "floor" of the stage."
           "Front", "The front wall of the stage."
           "Back", "The back wall of the stage."
           "Total", "The total number of walls in the stage."
        """
        Left = 0  # StageWallTypeMemberType
        Right = 1  # StageWallTypeMemberType
        Top = 2  # StageWallTypeMemberType
        Bottom = 3  # StageWallTypeMemberType
        Front = 4  # StageWallTypeMemberType
        Back = 5  # StageWallTypeMemberType
        Total = 6  # StageWallTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OrientationType():
        """
        Represents an index to a floor plane type define 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Yz", "Use yz plane for the stage floor."
           "Xz", "Use xz plane for the stage floor."
           "Xy", "Use xy plane for the stage floor."
           "UserDefined", "Use user defined plane for the stage floor."
        """
        Yz = 0  # StageOrientationTypeMemberType
        Xz = 1  # StageOrientationTypeMemberType
        Xy = 2  # StageOrientationTypeMemberType
        UserDefined = 3  # StageOrientationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def FloorXaxis(self) -> None:
        """
        The stage's bottom wall to align with the WCS x-axis 
        
        Signature ``FloorXaxis()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FloorYaxis(self) -> None:
        """
        The stage's bottom wall to align with the WCS y-axis 
        
        Signature ``FloorYaxis()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FloorZaxis(self) -> None:
        """
        The stage's bottom wall to align with the WCS z-axis 
        
        Signature ``FloorZaxis()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AlignFloorPlane(self, specifyFloorPlane: NXOpen.Plane) -> None:
        """
        The stage's bottom wall (floor) aligns with the given plane.  
        
        Signature ``AlignFloorPlane(specifyFloorPlane)`` 
        
        :param specifyFloorPlane: 
        :type specifyFloorPlane: :py:class:`NXOpen.Plane` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetWallFromList(self, index: StageWallType) -> Wall:
        """
        Returns a wall builder, given by the index, in the array of walls for the given stage  
        
        Signature ``GetWallFromList(index)`` 
        
        :param index:  index to the array of walls  
        :type index: :py:class:`NXOpen.Display.StageWallType` 
        :returns:  the wall  
        :rtype: :py:class:`NXOpen.Display.Wall` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetWallInList(self, index: StageWallType, wall: Wall) -> None:
        """
        Sets a wall builder in the array at the given index 
        
        Signature ``SetWallInList(index, wall)`` 
        
        :param index:  index to the array of walls  
        :type index: :py:class:`NXOpen.Display.StageWallType` 
        :param wall:  the wall  
        :type wall: :py:class:`NXOpen.Display.Wall` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CommitWall(self, view: NXOpen.View, currentWallIndex: int, updateStageDatabase: bool) -> None:
        """
        Updates the data and display for a given wall 
        
        Signature ``CommitWall(view, currentWallIndex, updateStageDatabase)`` 
        
        :param view:  view of the stage and walls  
        :type view: :py:class:`NXOpen.View` 
        :param currentWallIndex:  the index of the wall in the stage builder array  
        :type currentWallIndex: int 
        :param updateStageDatabase:  if true, commit the stage builder  
        :type updateStageDatabase: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CommitOffset(self, view: NXOpen.View) -> None:
        """
        Updates the data and display for a change to the stage's offset 
        
        Signature ``CommitOffset(view)`` 
        
        :param view:  view of the stage  
        :type view: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    FloorOrientationType: StageOrientationType = ...
    """
    Returns or sets  the floor orientation define 
    
    <hr>
    
    Getter Method
    
    Signature ``FloorOrientationType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.StageOrientationType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FloorOrientationType`` 
    
    :param floorOrientationType: 
    :type floorOrientationType: :py:class:`NXOpen.Display.StageOrientationType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Offset: float = ...
    """
    Returns or sets  the offset distance to translate the stage in the z-direction, in part units 
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`NXOpen.Display.Stage.OffsetExpression`instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Offset`` 
    
    :param offset: 
    :type offset: float 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX10.0.0
       This functionality is no longer supported.
    
    License requirements: None.
    """
    OffsetExpression: NXOpen.Expression = ...
    """
    Returns  the stage offset expression
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetExpression`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Size: float = ...
    """
    Returns or sets  the size all of the stage walls (length and width), in part units 
    
    <hr>
    
    Getter Method
    
    Signature ``Size`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`NXOpen.Display.Stage.SizeExpression` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Size`` 
    
    :param size: 
    :type size: float 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX10.0.0
       This functionality is no longer supported.
    
    License requirements: None.
    """
    SizeExpression: NXOpen.Expression = ...
    """
    Returns  the stage size expression
    
    <hr>
    
    Getter Method
    
    Signature ``SizeExpression`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    SpecifyFloorPlane: NXOpen.Plane = ...
    """
    Returns or sets  the specify floor plane 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifyFloorPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpecifyFloorPlane`` 
    
    :param specifyFloorPlane: 
    :type specifyFloorPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: Stage = ...  # unknown typename


class SaveImageFileBrowserBuilderFileFormatsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SaveImageFileBrowserBuilderFileFormats():
    """
    To specify the Ray Traced Studio static image file format 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Tif", "Tagged Image File Format (TIFF) file format"
       "Png", "Portable Network Graphic (PNG) file format"
       "Jpg", "Joint Photographic Experts Group (JPEG) file format"
    """
    Tif = 0  # SaveImageFileBrowserBuilderFileFormatsMemberType
    Png = 1  # SaveImageFileBrowserBuilderFileFormatsMemberType
    Jpg = 2  # SaveImageFileBrowserBuilderFileFormatsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SaveImageFileBrowserBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.SaveImageFileBrowserBuilder`.  
    
    Saves an image file using a file browser.
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateSaveImageFileBrowserBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    class FileFormats():
        """
        To specify the Ray Traced Studio static image file format 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Tif", "Tagged Image File Format (TIFF) file format"
           "Png", "Portable Network Graphic (PNG) file format"
           "Jpg", "Joint Photographic Experts Group (JPEG) file format"
        """
        Tif = 0  # SaveImageFileBrowserBuilderFileFormatsMemberType
        Png = 1  # SaveImageFileBrowserBuilderFileFormatsMemberType
        Jpg = 2  # SaveImageFileBrowserBuilderFileFormatsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    FileFormat: SaveImageFileBrowserBuilderFileFormats = ...
    """
    Returns or sets  the Ray Traced Studio static image file format 
    
    <hr>
    
    Getter Method
    
    Signature ``FileFormat`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.SaveImageFileBrowserBuilderFileFormats` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FileFormat`` 
    
    :param fileFormat: 
    :type fileFormat: :py:class:`NXOpen.Display.SaveImageFileBrowserBuilderFileFormats` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    NativeImageFileBrowser: str = ...
    """
    Returns or sets  the Ray Traced Studio static image file browser 
    
    <hr>
    
    Getter Method
    
    Signature ``NativeImageFileBrowser`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NativeImageFileBrowser`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    UseTransparentBackground: bool = ...
    """
    Returns or sets  the Ray Traced Studio static image transparent background setting 
    
    <hr>
    
    Getter Method
    
    Signature ``UseTransparentBackground`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseTransparentBackground`` 
    
    :param useTransparentBackground: 
    :type useTransparentBackground: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: SaveImageFileBrowserBuilder = ...  # unknown typename


class BackgroundCategoryTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BackgroundCategoryType():
    """
    background 2D3D types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Flat", "2D Background"
       "Dome", "3D Dome"
    """
    Flat = 0  # BackgroundCategoryTypeMemberType
    Dome = 1  # BackgroundCategoryTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BackgroundTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BackgroundType():
    """
    background types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Plain", "single color background"
       "Graduated", "two color background, which varies between them"
       "Image", "an image file displayed in the background"
       "HemiDome", "an 3D HDR image displayed in the background"
    """
    Plain = 0  # BackgroundTypeMemberType
    Graduated = 1  # BackgroundTypeMemberType
    Image = 2  # BackgroundTypeMemberType
    HemiDome = 3  # BackgroundTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BackgroundBackgroundDomeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BackgroundBackgroundDomeType():
    """
    dome types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Finite", "finite 3D dome"
       "Infinite", "infinite 3D dome"
    """
    Finite = 0  # BackgroundBackgroundDomeTypeMemberType
    Infinite = 1  # BackgroundBackgroundDomeTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Background(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.Background`
    Background defines how background pixels are displayed.  
    
    The background
    resides on a virtual plane at the back of a view.  This background is used
    for display in Studio rendering style and High Quality Images.
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateBackground`
    
    .. versionadded:: NX5.0.0
    """
    
    class CategoryType():
        """
        background 2D3D types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Flat", "2D Background"
           "Dome", "3D Dome"
        """
        Flat = 0  # BackgroundCategoryTypeMemberType
        Dome = 1  # BackgroundCategoryTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Type():
        """
        background types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Plain", "single color background"
           "Graduated", "two color background, which varies between them"
           "Image", "an image file displayed in the background"
           "HemiDome", "an 3D HDR image displayed in the background"
        """
        Plain = 0  # BackgroundTypeMemberType
        Graduated = 1  # BackgroundTypeMemberType
        Image = 2  # BackgroundTypeMemberType
        HemiDome = 3  # BackgroundTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BackgroundDomeType():
        """
        dome types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Finite", "finite 3D dome"
           "Infinite", "infinite 3D dome"
        """
        Finite = 0  # BackgroundBackgroundDomeTypeMemberType
        Infinite = 1  # BackgroundBackgroundDomeTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetBottomColor(self) -> 'list[float]':
        """
        Returns the bottom color  
        
        Signature ``GetBottomColor()`` 
        
        :returns:  Array of 3 rgb values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBottomColor(self, bottomColor: 'list[float]') -> None:
        """
        Sets the bottom color 
        
        Signature ``SetBottomColor(bottomColor)`` 
        
        :param bottomColor:  Array of 3 rgb values, each between 0 and 1  
        :type bottomColor: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTopColor(self) -> 'list[float]':
        """
        Returns the top color  
        
        Signature ``GetTopColor()`` 
        
        :returns:  Array of 3 rgb values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTopColor(self, topColor: 'list[float]') -> None:
        """
        Sets the top color 
        
        Signature ``SetTopColor(topColor)`` 
        
        :param topColor:  Array of 3 rgb values, each between 0 and 1  
        :type topColor: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    BackgroundCategory: BackgroundCategoryType = ...
    """
    Returns or sets  the background 2D or 3D type 
    
    <hr>
    
    Getter Method
    
    Signature ``BackgroundCategory`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.BackgroundCategoryType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BackgroundCategory`` 
    
    :param backgroundCategoryType: 
    :type backgroundCategoryType: :py:class:`NXOpen.Display.BackgroundCategoryType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    """
    BackgroundType: BackgroundType = ...
    """
    Returns or sets  the background type 
    
    <hr>
    
    Getter Method
    
    Signature ``BackgroundType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.BackgroundType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BackgroundType`` 
    
    :param backgroundType: 
    :type backgroundType: :py:class:`NXOpen.Display.BackgroundType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    DomeImage: Image = ...
    """
    Returns or sets  the dome background's image builder 
    
    <hr>
    
    Getter Method
    
    Signature ``DomeImage`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DomeImage`` 
    
    :param domeImageBuilder: 
    :type domeImageBuilder: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DomeImageFilename: str = ...
    """
    Returns or sets  the background's dome image filename 
    
    <hr>
    
    Getter Method
    
    Signature ``DomeImageFilename`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DomeImageFilename`` 
    
    :param domeImageFileName: 
    :type domeImageFileName: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DomeOrigin: NXOpen.Point = ...
    """
    Returns or sets  the origin 
    
    <hr>
    
    Getter Method
    
    Signature ``DomeOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DomeOrigin`` 
    
    :param origin: 
    :type origin: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DomeSize: float = ...
    """
    Returns or sets  the dome size 
    
    <hr>
    
    Getter Method
    
    Signature ``DomeSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DomeSize`` 
    
    :param domeSize: 
    :type domeSize: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DomeType: BackgroundBackgroundDomeType = ...
    """
    Returns or sets  the dome type 
    
    <hr>
    
    Getter Method
    
    Signature ``DomeType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.BackgroundBackgroundDomeType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DomeType`` 
    
    :param domeType: 
    :type domeType: :py:class:`NXOpen.Display.BackgroundBackgroundDomeType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Image: Image = ...
    """
    Returns or sets  the background's image builder 
    
    <hr>
    
    Getter Method
    
    Signature ``Image`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Image`` 
    
    :param imageBuilder: 
    :type imageBuilder: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ImageFilename: str = ...
    """
    Returns or sets  the background's image filename 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageFilename`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageFilename`` 
    
    :param imageFileName: 
    :type imageFileName: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ImageHorizon: float = ...
    """
    Returns or sets  the dome image horizon 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageHorizon`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageHorizon`` 
    
    :param imageHorizon: 
    :type imageHorizon: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ImageRotation: float = ...
    """
    Returns or sets  the image rotation angle (in degrees) 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageRotation`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageRotation`` 
    
    :param imageRotation: 
    :type imageRotation: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ImageUpVector: NXOpen.Direction = ...
    """
    Returns or sets  the image up vector direction, relative to the absolute coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageUpVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageUpVector`` 
    
    :param imageUpVector: 
    :type imageUpVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    UseStageSizeAndOrientation: bool = ...
    """
    Returns or sets  whether to use stage Size and Orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``UseStageSizeAndOrientation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseStageSizeAndOrientation`` 
    
    :param StageSizeAndOrientation: 
    :type StageSizeAndOrientation: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: Background = ...  # unknown typename


class PointCloudClippingBoxesListItemBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[PointCloudClippingBoxesListItemBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: PointCloudClippingBoxesListItemBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        
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
    
    
    def FindIndex(self, obj: PointCloudClippingBoxesListItemBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> PointCloudClippingBoxesListItemBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        
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
    def Erase(self, obj: PointCloudClippingBoxesListItemBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: PointCloudClippingBoxesListItemBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
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
    
    
    def GetContents(self) -> 'list[PointCloudClippingBoxesListItemBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[PointCloudClippingBoxesListItemBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        
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
    def Swap(self, object1: PointCloudClippingBoxesListItemBuilder, object2: PointCloudClippingBoxesListItemBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: PointCloudClippingBoxesListItemBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        
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
    Null: PointCloudClippingBoxesListItemBuilderList = ...  # unknown typename


class IrayPlusMaterialAttributeEnum(IrayPlusMaterialAttribute):
    """
    Represents a IrayPlus Enum Attribute 
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    IrayPlusMaterialAttributeEnum is not supported in KF.
    
    .. versionadded:: NX12.0.0
    """
    EnumValue: int = ...
    """
    Returns or sets  the enum value 
    
    <hr>
    
    Getter Method
    
    Signature ``EnumValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnumValue`` 
    
    :param enumValue: 
    :type enumValue: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: IrayPlusMaterialAttributeEnum = ...  # unknown typename


class PlanarShipGridBuilderIntersectOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PlanarShipGridBuilderIntersectOption():
    """
    Settings that indicate how to search for objects that intersect the plane. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Everything", "all objects will be searched for intersections with the plane"
       "SelectedObjects", "only the selected objects will be searched for intersections with the plane"
       "ShipGridAndSelected", "intersect the ship grid and selected objects with the plane"
    """
    Everything = 0  # PlanarShipGridBuilderIntersectOptionMemberType
    SelectedObjects = 1  # PlanarShipGridBuilderIntersectOptionMemberType
    ShipGridAndSelected = 2  # PlanarShipGridBuilderIntersectOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PlanarShipGridBuilderLabelDisplayOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PlanarShipGridBuilderLabelDisplayOption():
    """
    Settings that indicate what grid lines should be labelled. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ShowAll", "Display label for every grid line"
       "ShowEveryOther", "Display label for every other grid line"
       "ShowEveryThird", "Display label for every third grid line"
       "ShowEveryFourth", "Display label for every fourth grid line"
       "HideAll", "Hide label for all grid lines"
    """
    ShowAll = 0  # PlanarShipGridBuilderLabelDisplayOptionMemberType
    ShowEveryOther = 1  # PlanarShipGridBuilderLabelDisplayOptionMemberType
    ShowEveryThird = 2  # PlanarShipGridBuilderLabelDisplayOptionMemberType
    ShowEveryFourth = 3  # PlanarShipGridBuilderLabelDisplayOptionMemberType
    HideAll = 4  # PlanarShipGridBuilderLabelDisplayOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PlanarShipGridBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.PlanarShipGrid` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Display.GridCollection.CreatePlanarShipGridBuilder`
    
    Default values.
    
    =======================  ===========
    Property                 Value
    =======================  ===========
    IntersectType            Everything 
    -----------------------  -----------
    LabelDisplayType         ShowAll 
    -----------------------  -----------
    LabelSettingInheritted   0 
    -----------------------  -----------
    LineFontType             Solid 
    -----------------------  -----------
    LineSettingInheritted    1 
    -----------------------  -----------
    LineWidthType            Normal 
    =======================  ===========
    
    .. versionadded:: NX8.0.0
    """
    
    class IntersectOption():
        """
        Settings that indicate how to search for objects that intersect the plane. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Everything", "all objects will be searched for intersections with the plane"
           "SelectedObjects", "only the selected objects will be searched for intersections with the plane"
           "ShipGridAndSelected", "intersect the ship grid and selected objects with the plane"
        """
        Everything = 0  # PlanarShipGridBuilderIntersectOptionMemberType
        SelectedObjects = 1  # PlanarShipGridBuilderIntersectOptionMemberType
        ShipGridAndSelected = 2  # PlanarShipGridBuilderIntersectOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LabelDisplayOption():
        """
        Settings that indicate what grid lines should be labelled. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ShowAll", "Display label for every grid line"
           "ShowEveryOther", "Display label for every other grid line"
           "ShowEveryThird", "Display label for every third grid line"
           "ShowEveryFourth", "Display label for every fourth grid line"
           "HideAll", "Hide label for all grid lines"
        """
        ShowAll = 0  # PlanarShipGridBuilderLabelDisplayOptionMemberType
        ShowEveryOther = 1  # PlanarShipGridBuilderLabelDisplayOptionMemberType
        ShowEveryThird = 2  # PlanarShipGridBuilderLabelDisplayOptionMemberType
        ShowEveryFourth = 3  # PlanarShipGridBuilderLabelDisplayOptionMemberType
        HideAll = 4  # PlanarShipGridBuilderLabelDisplayOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetExtent(self) -> tuple:
        """
        Get corner points of the grid extent.  
        
        The extent is a rectangle.
        The four points: point1, point2, point3, point4 are in clockwise 
        or counterclockwise direction.
        
        Signature ``GetExtent()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (valid, point1, point2, point3, point4). valid is a bool.   Flag indicating whether the corner points are valid point1 is a :py:class:`NXOpen.Point3d`.   First corner point point2 is a :py:class:`NXOpen.Point3d`.   Second corner point point3 is a :py:class:`NXOpen.Point3d`.   Third corner point point4 is a :py:class:`NXOpen.Point3d`.   Fourth corner point 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetExtent(self, point1: NXOpen.Point3d, point2: NXOpen.Point3d, point3: NXOpen.Point3d, point4: NXOpen.Point3d) -> bool:
        """
        Set corner points for the grid extent.  
        
        The extent is a rectangle.
        The four points: point1, point2, point3, point4 should be in
        clockwise or counterclockwise direction.
        
        Signature ``SetExtent(point1, point2, point3, point4)`` 
        
        :param point1:  First corner point  
        :type point1: :py:class:`NXOpen.Point3d` 
        :param point2:  Second corner point  
        :type point2: :py:class:`NXOpen.Point3d` 
        :param point3:  Third corner point  
        :type point3: :py:class:`NXOpen.Point3d` 
        :param point4:  Fourth corner point  
        :type point4: :py:class:`NXOpen.Point3d` 
        :returns:  Flag indicating whether the corner points are valid  
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetIntersectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Get the objects that were searched to find intersections with the plane.  
        
        Signature ``GetIntersectedObjects()`` 
        
        :returns:  Array of intersected objects  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetIntersectedObjects(self, intersectedObjects: 'list[NXOpen.TaggedObject]') -> None:
        """
        Set the objects that are to be searched to find intersections with the plane.  
        
        Signature ``SetIntersectedObjects(intersectedObjects)`` 
        
        :param intersectedObjects:  Array of intersected objects  
        :type intersectedObjects: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SwitchLabelLocationX(self) -> None:
        """
        Switch label location in X direction.  
        
        Signature ``SwitchLabelLocationX()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SwitchLabelLocationY(self) -> None:
        """
        Switch label location in Y direction.  
        
        Signature ``SwitchLabelLocationY()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SwitchLabelLocationZ(self) -> None:
        """
        Switch label location in Z direction.  
        
        Signature ``SwitchLabelLocationZ()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    BasePlane: NXOpen.DatumPlane = ...
    """
    Returns or sets  the base plane where the planar ship grid is created.  
    
    <hr>
    
    Getter Method
    
    Signature ``BasePlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DatumPlane` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    
    <hr>
    
    Setter Method
    
    Signature ``BasePlane`` 
    
    :param basePlane: 
    :type basePlane: :py:class:`NXOpen.DatumPlane` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    IntersectType: PlanarShipGridBuilderIntersectOption = ...
    """
    Returns or sets  the value that determines how to find objects that intersect the plane.  
    
    <hr>
    
    Getter Method
    
    Signature ``IntersectType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.PlanarShipGridBuilderIntersectOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    
    <hr>
    
    Setter Method
    
    Signature ``IntersectType`` 
    
    :param intersectType: 
    :type intersectType: :py:class:`NXOpen.Display.PlanarShipGridBuilderIntersectOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    LabelColor: NXOpen.NXColor = ...
    """
    Returns or sets  the grid line label color.  
    
    Only used if the color is not inherited from the intersected plane.
    
    <hr>
    
    Getter Method
    
    Signature ``LabelColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    
    <hr>
    
    Setter Method
    
    Signature ``LabelColor`` 
    
    :param labelColor: 
    :type labelColor: Id 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    LabelDisplayType: PlanarShipGridBuilderLabelDisplayOption = ...
    """
    Returns or sets  the setting that indicates what grid lines are to be labelled.  
    
    <hr>
    
    Getter Method
    
    Signature ``LabelDisplayType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.PlanarShipGridBuilderLabelDisplayOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    
    <hr>
    
    Setter Method
    
    Signature ``LabelDisplayType`` 
    
    :param labelDisplayType: 
    :type labelDisplayType: :py:class:`NXOpen.Display.PlanarShipGridBuilderLabelDisplayOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    LabelSettingInheritted: bool = ...
    """
    Returns or sets  the setting that indicates whether the grid line label will inherit the intersected plane's color 
    
    <hr>
    
    Getter Method
    
    Signature ``LabelSettingInheritted`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    
    <hr>
    
    Setter Method
    
    Signature ``LabelSettingInheritted`` 
    
    :param labelSettingInheritted: 
    :type labelSettingInheritted: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    LineColor: NXOpen.NXColor = ...
    """
    Returns or sets  the grid line color.  
    
    Only used if the color is not inherited from the intersected plane. 
    
    <hr>
    
    Getter Method
    
    Signature ``LineColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    
    <hr>
    
    Setter Method
    
    Signature ``LineColor`` 
    
    :param lineColor: 
    :type lineColor: Id 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    LineFontType: NXOpen.DisplayableObjectObjectFont = ...
    """
    Returns or sets  the grid line font.  
    
    Only used if the font is not inherited from the intersected plane. 
    
    <hr>
    
    Getter Method
    
    Signature ``LineFontType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    
    <hr>
    
    Setter Method
    
    Signature ``LineFontType`` 
    
    :param lineFontType: 
    :type lineFontType: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    LineSettingInheritted: bool = ...
    """
    Returns or sets  the setting that indicates whether the grid line will inherit the intersected plane's color/font/width.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineSettingInheritted`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    
    <hr>
    
    Setter Method
    
    Signature ``LineSettingInheritted`` 
    
    :param lineSettingInheritted: 
    :type lineSettingInheritted: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    LineWidthType: NXOpen.DisplayableObjectObjectWidth = ...
    """
    Returns or sets  the grid line width.  
    
    Only used if the width is not inherited from the intersected plane. 
    
    <hr>
    
    Getter Method
    
    Signature ``LineWidthType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    
    <hr>
    
    Setter Method
    
    Signature ``LineWidthType`` 
    
    :param lineWidthType: 
    :type lineWidthType: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    Null: PlanarShipGridBuilder = ...  # unknown typename


class ReflectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReflectionType():
    """
    where the reflections for rendering will be obtained 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Background", "use the background for reflections"
       "Stage", "use the stage for reflections"
       "Ibl", "use the image-based lighting image for reflections"
       "Image", "use the given image file for reflection"
    """
    Background = 0  # ReflectionTypeMemberType
    Stage = 1  # ReflectionTypeMemberType
    Ibl = 2  # ReflectionTypeMemberType
    Image = 3  # ReflectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Reflection(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.Reflection`
    Reflection defines the source of reflection in shiny objects for Studio
    rendering style or High Quality Images.  
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateReflection`
    
    .. versionadded:: NX5.0.0
    """
    
    class Type():
        """
        where the reflections for rendering will be obtained 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Background", "use the background for reflections"
           "Stage", "use the stage for reflections"
           "Ibl", "use the image-based lighting image for reflections"
           "Image", "use the given image file for reflection"
        """
        Background = 0  # ReflectionTypeMemberType
        Stage = 1  # ReflectionTypeMemberType
        Ibl = 2  # ReflectionTypeMemberType
        Image = 3  # ReflectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Image: Image = ...
    """
    Returns or sets  the reflections's image builder 
    
    <hr>
    
    Getter Method
    
    Signature ``Image`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Image`` 
    
    :param imageBuilder: 
    :type imageBuilder: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ImageFilename: str = ...
    """
    Returns or sets  the reflection's image filename 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageFilename`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageFilename`` 
    
    :param imageFileName: 
    :type imageFileName: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ReflectionMap: ReflectionType = ...
    """
    Returns or sets  the reflection type 
    
    <hr>
    
    Getter Method
    
    Signature ``ReflectionMap`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ReflectionType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReflectionMap`` 
    
    :param reflectionMap: 
    :type reflectionMap: :py:class:`NXOpen.Display.ReflectionType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: Reflection = ...  # unknown typename


class Scene(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.Scene`
    A scene is comprised of background, stage, reflection, lights and 
    image-based lighting subobjects.  
    
    You optionally specify a scene for
    display in Studio rendering style and High Quality Images.
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateScene`
    
    .. versionadded:: NX5.0.0
    """
    Background: Background = ...
    """
    Returns  the background - use to define how background pixels are displayed 
    
    <hr>
    
    Getter Method
    
    Signature ``Background`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Background` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    EnvironmentBuilder: EnvironmentBuilder = ...
    """
    Returns  the environment_builder - use to define the environment 
    
    <hr>
    
    Getter Method
    
    Signature ``EnvironmentBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.EnvironmentBuilder` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    """
    ImageBasedLighting: ImageBasedLighting = ...
    """
    Returns  the image-based lighting - optionally use to by-pass lights with 
    image-based lighting, where lighting effects are derived from a
    given image file 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageBasedLighting`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBasedLighting` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Lighting: Lighting = ...
    """
    Returns  the lights - use to define light settings for the given lights 
    
    <hr>
    
    Getter Method
    
    Signature ``Lighting`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Lighting` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Reflection: Reflection = ...
    """
    Returns  the reflection - use to define what will be reflected in shiny objects 
    
    <hr>
    
    Getter Method
    
    Signature ``Reflection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Reflection` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Stage: Stage = ...
    """
    Returns  the stage - use to optionally define a box that can have between 
    one and six visible "walls" 
    
    <hr>
    
    Getter Method
    
    Signature ``Stage`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Stage` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: Scene = ...  # unknown typename


class IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeType():
    """
    To specify the quality and performance of the Ray Traced Studio display when dynamic interaction stops 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Photoreal", "Very good ray traced display quality when dynamic interaction stops"
       "QualityInteractive", "Good ray traced display quality with good performance when dynamic interaction stops"
       "FastInteractive", "The fastest ray traced display performance with preview quality when dynamic interaction stops"
    """
    Photoreal = 0  # IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeTypeMemberType
    QualityInteractive = 1  # IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeTypeMemberType
    FastInteractive = 2  # IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatType():
    """
    To specify the Ray Traced Studio static image file format 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Tif", "Tagged Image File Format (TIFF) file format"
       "Png", "Portable Network Graphic (PNG) file format"
       "Jpg", "Joint Photographic Experts Group (JPEG) file format"
    """
    Tif = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatTypeMemberType
    Png = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatTypeMemberType
    Jpg = 2  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsType():
    """
    To specify the Ray Traced Studio static image units 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Pixels", "static image size specified in pixel"
       "Millimeters", "static image size specified in millimeters"
       "Inches", "static image size specified in inches"
    """
    Pixels = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsTypeMemberType
    Millimeters = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsTypeMemberType
    Inches = 2  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageSizeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageSizeType():
    """
    To specify the Ray Traced Studio static image size 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "RenderWindow", "Ray Traced Studio window size used for static image output"
       "UserDefined", "user specified size for static image output"
    """
    RenderWindow = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageSizeTypeMemberType
    UserDefined = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageSizeTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageOrientationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageOrientationType():
    """
    To specify the Ray Traced Studio static image orientation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Landscape", "static image orientation where width is greater than height"
       "Portrait", "static image orientation where height is greater than width"
    """
    Landscape = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageOrientationTypeMemberType
    Portrait = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageOrientationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionType():
    """
    To specify the Ray Traced Studio static image resolution 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "High", "static image output resolution of 300 DPI (dots per inch)"
       "Medium", "static image output resolution of 150 DPI (dots per inch)"
       "Low", "static image output resolution of 72 DPI (dots per inch)"
       "UserDefined", "user specified image output resolution in DPI (dots per inch)"
    """
    High = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionTypeMemberType
    Medium = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionTypeMemberType
    Low = 2  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionTypeMemberType
    UserDefined = 3  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderVideoTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderVideoType():
    """
    To specify the Ray Traced Studio remote rendering video mode   
    
    .. deprecated::  NX12.0.0
       This is removed. The video mode is determined by the Ray Traced Studio render mode.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Streaming", " - "
       "Synchronous", " - "
    """
    Streaming = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderVideoTypeMemberType
    Synchronous = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderVideoTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatType():
    """
    To specify the Ray Traced Studio remote rendering format 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "H264", " - "
       "Lossless", " - "
       "Png", " - "
       "Jpeg", " - "
    """
    H264 = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatTypeMemberType
    Lossless = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatTypeMemberType
    Png = 2  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatTypeMemberType
    Jpeg = 3  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderType():
    """
    To specify the Ray Traced Studio remote rendering type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Cluster", "Network Cluster"
       "Vca", "VCA"
    """
    Cluster = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderTypeMemberType
    Vca = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IRayPlusStudioEditorBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilder`.  
    
    Ray Traced Studio Editor controls display and output of CPU-based real-time ray tracing.
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateIrayPlusStudioEditorBuilder`
    
    .. versionadded:: NX10.0.2
    """
    
    class DynamicIRayPlusStudioRenderModeType():
        """
        To specify the quality and performance of the Ray Traced Studio display when dynamic interaction stops 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Photoreal", "Very good ray traced display quality when dynamic interaction stops"
           "QualityInteractive", "Good ray traced display quality with good performance when dynamic interaction stops"
           "FastInteractive", "The fastest ray traced display performance with preview quality when dynamic interaction stops"
        """
        Photoreal = 0  # IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeTypeMemberType
        QualityInteractive = 1  # IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeTypeMemberType
        FastInteractive = 2  # IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class IRayPlusStudioStaticImageFileFormatType():
        """
        To specify the Ray Traced Studio static image file format 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Tif", "Tagged Image File Format (TIFF) file format"
           "Png", "Portable Network Graphic (PNG) file format"
           "Jpg", "Joint Photographic Experts Group (JPEG) file format"
        """
        Tif = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatTypeMemberType
        Png = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatTypeMemberType
        Jpg = 2  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class IRayPlusStudioStaticImageUnitsType():
        """
        To specify the Ray Traced Studio static image units 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Pixels", "static image size specified in pixel"
           "Millimeters", "static image size specified in millimeters"
           "Inches", "static image size specified in inches"
        """
        Pixels = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsTypeMemberType
        Millimeters = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsTypeMemberType
        Inches = 2  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class IRayPlusStudioStaticImageSizeType():
        """
        To specify the Ray Traced Studio static image size 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "RenderWindow", "Ray Traced Studio window size used for static image output"
           "UserDefined", "user specified size for static image output"
        """
        RenderWindow = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageSizeTypeMemberType
        UserDefined = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageSizeTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class IRayPlusStudioStaticImageOrientationType():
        """
        To specify the Ray Traced Studio static image orientation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Landscape", "static image orientation where width is greater than height"
           "Portrait", "static image orientation where height is greater than width"
        """
        Landscape = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageOrientationTypeMemberType
        Portrait = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageOrientationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class IRayPlusStudioStaticImageResolutionType():
        """
        To specify the Ray Traced Studio static image resolution 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "High", "static image output resolution of 300 DPI (dots per inch)"
           "Medium", "static image output resolution of 150 DPI (dots per inch)"
           "Low", "static image output resolution of 72 DPI (dots per inch)"
           "UserDefined", "user specified image output resolution in DPI (dots per inch)"
        """
        High = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionTypeMemberType
        Medium = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionTypeMemberType
        Low = 2  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionTypeMemberType
        UserDefined = 3  # IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class IRayPlusStudioRemoteRenderVideoType():
        """
        To specify the Ray Traced Studio remote rendering video mode   
        
        .. deprecated::  NX12.0.0
           This is removed. The video mode is determined by the Ray Traced Studio render mode.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Streaming", " - "
           "Synchronous", " - "
        """
        Streaming = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderVideoTypeMemberType
        Synchronous = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderVideoTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class IRayPlusStudioRemoteRenderFormatType():
        """
        To specify the Ray Traced Studio remote rendering format 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "H264", " - "
           "Lossless", " - "
           "Png", " - "
           "Jpeg", " - "
        """
        H264 = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatTypeMemberType
        Lossless = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatTypeMemberType
        Png = 2  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatTypeMemberType
        Jpeg = 3  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class IRayPlusStudioRemoteRenderType():
        """
        To specify the Ray Traced Studio remote rendering type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Cluster", "Network Cluster"
           "Vca", "VCA"
        """
        Cluster = 0  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderTypeMemberType
        Vca = 1  # IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    DynamicIRayPlusCaustics: bool = ...
    """
    Returns or sets  the Ray Traced Studio dynamic antialiasing quality when dynamic interaction stops 
    
    <hr>
    
    Getter Method
    
    Signature ``DynamicIRayPlusCaustics`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``DynamicIRayPlusCaustics`` 
    
    :param dynamicIRayPlusCaustics: 
    :type dynamicIRayPlusCaustics: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    DynamicIRayPlusStudioRenderMode: IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeType = ...
    """
    Returns or sets  the Ray Traced Studio dynamic display rendering mode 
    
    <hr>
    
    Getter Method
    
    Signature ``DynamicIRayPlusStudioRenderMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``DynamicIRayPlusStudioRenderMode`` 
    
    :param dynamicIRayPlusStudioRenderMode: 
    :type dynamicIRayPlusStudioRenderMode: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderDynamicIRayPlusStudioRenderModeType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    DynamicIRayPlusStudioTime: NXOpen.DateBuilder = ...
    """
    Returns  the Ray Traced Studio dynamic display time-based rendering mode timer (read only) 
    
    <hr>
    
    Getter Method
    
    Signature ``DynamicIRayPlusStudioTime`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DateBuilder` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImageDotsPerInch: int = ...
    """
    Returns or sets  the Ray Traced Studio static image dots per inch (DPI) 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImageDotsPerInch`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImageDotsPerInch`` 
    
    :param iRayPlusStudioStaticImageDotsPerInch: 
    :type iRayPlusStudioStaticImageDotsPerInch: int 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImageDoubleHeight: float = ...
    """
    Returns or sets  the Ray Traced Studio static image height 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImageDoubleHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImageDoubleHeight`` 
    
    :param iRayPlusStudioStaticImageDoubleHeight: 
    :type iRayPlusStudioStaticImageDoubleHeight: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImageDoubleWidth: float = ...
    """
    Returns or sets  the Ray Traced Studio static image width 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImageDoubleWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImageDoubleWidth`` 
    
    :param iRayPlusStudioStaticImageDoubleWidth: 
    :type iRayPlusStudioStaticImageDoubleWidth: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImageFileFormat: IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatType = ...
    """
    Returns or sets  the Ray Traced Studio static output image file format 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImageFileFormat`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImageFileFormat`` 
    
    :param iRayPlusStudioStaticImageFileFormat: 
    :type iRayPlusStudioStaticImageFileFormat: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageFileFormatType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImageLockAspectRatio: bool = ...
    """
    Returns or sets  the Ray Traced Studio static image aspect ratio will be maintained 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImageLockAspectRatio`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImageLockAspectRatio`` 
    
    :param iRayPlusStudioStaticImageLockAspectRatio: 
    :type iRayPlusStudioStaticImageLockAspectRatio: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImageOrientation: IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageOrientationType = ...
    """
    Returns or sets  the Ray Traced Studio static image orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImageOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageOrientationType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImageOrientation`` 
    
    :param iRayPlusStudioStaticImageOrientation: 
    :type iRayPlusStudioStaticImageOrientation: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageOrientationType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImagePixelHeight: int = ...
    """
    Returns or sets  the Ray Traced Studio static image pixel height 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImagePixelHeight`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImagePixelHeight`` 
    
    :param iRayPlusStudioStaticImagePixelHeight: 
    :type iRayPlusStudioStaticImagePixelHeight: int 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImagePixelWidth: int = ...
    """
    Returns or sets  the Ray Traced Studio static image pixel width 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImagePixelWidth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImagePixelWidth`` 
    
    :param iRayPlusStudioStaticImagePixelWidth: 
    :type iRayPlusStudioStaticImagePixelWidth: int 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImageResolution: IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionType = ...
    """
    Returns or sets  the Ray Traced Studio static image resolution 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImageResolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImageResolution`` 
    
    :param iRayPlusStudioStaticImageResolution: 
    :type iRayPlusStudioStaticImageResolution: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageResolutionType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImageSize: IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageSizeType = ...
    """
    Returns or sets  the Ray Traced Studio static image size 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImageSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageSizeType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImageSize`` 
    
    :param iRayPlusStudioStaticImageSize: 
    :type iRayPlusStudioStaticImageSize: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageSizeType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioStaticImageUnits: IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsType = ...
    """
    Returns or sets  the Ray Traced Studio static image units 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioStaticImageUnits`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioStaticImageUnits`` 
    
    :param iRayPlusStudioStaticImageUnits: 
    :type iRayPlusStudioStaticImageUnits: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioStaticImageUnitsType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    IRayPlusStudioshowStatusIndicator: bool = ...
    """
    Returns or sets  the Ray Traced Studio progess status indicator percent complete display 
    
    <hr>
    
    Getter Method
    
    Signature ``IRayPlusStudioshowStatusIndicator`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``IRayPlusStudioshowStatusIndicator`` 
    
    :param iRayPlusStudioshowStatusIndicator: 
    :type iRayPlusStudioshowStatusIndicator: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    RemoteRenderFormat: IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatType = ...
    """
    Returns or sets  the Ray Traced Studio display remote rendering format 
    
    <hr>
    
    Getter Method
    
    Signature ``RemoteRenderFormat`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``RemoteRenderFormat`` 
    
    :param remoteRenderFormatType: 
    :type remoteRenderFormatType: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderFormatType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    RemoteRenderIP: str = ...
    """
    Returns or sets  the Ray Traced Studio display remote rendering IP address 
    
    <hr>
    
    Getter Method
    
    Signature ``RemoteRenderIP`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``RemoteRenderIP`` 
    
    :param remoteRenderIP: 
    :type remoteRenderIP: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    RemoteRenderSecurityToken: str = ...
    """
    Returns or sets  the Ray Traced Studio display remote rendering security token 
    
    <hr>
    
    Getter Method
    
    Signature ``RemoteRenderSecurityToken`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``RemoteRenderSecurityToken`` 
    
    :param remoteRenderSecurityToken: 
    :type remoteRenderSecurityToken: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    RemoteRenderToggle: bool = ...
    """
    Returns or sets  the Ray Traced Studio display if remote rendering is used 
    
    <hr>
    
    Getter Method
    
    Signature ``RemoteRenderToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``RemoteRenderToggle`` 
    
    :param remoteRenderToggle: 
    :type remoteRenderToggle: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    RemoteRenderType: IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderType = ...
    """
    Returns or sets  the Ray Traced Studio display remote rendering type 
    
    <hr>
    
    Getter Method
    
    Signature ``RemoteRenderType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``RemoteRenderType`` 
    
    :param remoteRenderType: 
    :type remoteRenderType: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderType` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    RemoteRenderVideoMode: IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderVideoType = ...
    """
    Returns or sets  the Ray Traced Studio display remote rendering video mode 
    
    <hr>
    
    Getter Method
    
    Signature ``RemoteRenderVideoMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderVideoType` 
    
    .. versionadded:: NX10.0.2
    
    .. deprecated::  NX12.0.0
       This is removed. The video mode is determined by the Ray Traced Studio render mode.
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``RemoteRenderVideoMode`` 
    
    :param remoteRenderVideoType: 
    :type remoteRenderVideoType: :py:class:`NXOpen.Display.IRayPlusStudioEditorBuilderIRayPlusStudioRemoteRenderVideoType` 
    
    .. versionadded:: NX10.0.2
    
    .. deprecated::  NX12.0.0
       This is removed. The video mode is determined by the Ray Traced Studio render mode.
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    StaticIRayPlusStudioTime: NXOpen.DateBuilder = ...
    """
    Returns  the Ray Traced Studio static display time-based rendering timer (read only) 
    
    <hr>
    
    Getter Method
    
    Signature ``StaticIRayPlusStudioTime`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DateBuilder` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    Null: IRayPlusStudioEditorBuilder = ...  # unknown typename


class PointCloudBuilderColorModesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PointCloudBuilderColorModes():
    """
    Specifies point cloud color display mode choice. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Individual", "individual"
       "Uniform", "uniform"
    """
    Individual = 0  # PointCloudBuilderColorModesMemberType
    Uniform = 1  # PointCloudBuilderColorModesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PointCloudBuilderBrightnessModesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PointCloudBuilderBrightnessModes():
    """
    Specifies point cloud brightness display mode choice. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Uniform", "uniform"
       "Shaded", "Shaded"
    """
    Uniform = 0  # PointCloudBuilderBrightnessModesMemberType
    Shaded = 1  # PointCloudBuilderBrightnessModesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PointCloudBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`Display.PointCloudBuilder`.  
    
    :py:class:`NXOpen.Display.PointCloud`is a cloud object based on an
    imported point data files file (e.g. a POD file from Bentley). The point data
    (list of coordinates) itself won't be stored within NX part file but an object
    ("Reference Point Cloud") is created which references to the point data file
    and stores several meta data like clipping areas, display and current location.
    When loaded the point cloud will be visible as defined in the object parameters.
    Access to the point cloud like display, measurement, blanking/showing, sectioning,
    POD file loading will requires license checkout of the new basic point cloud 
    license. For deleting a Reference Point Cloud object the license is not required.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Display.PointCloudCollection.CreatePointCloudBuilder`
    
    Default values.
    
    ======================  ===========
    Property                Value
    ======================  ===========
    LoadPointDataWithPart   1 
    ----------------------  -----------
    PointBrightnessMode     Uniform 
    ----------------------  -----------
    PointColorMode          Individual 
    ----------------------  -----------
    PointDensity            100.0 
    ----------------------  -----------
    PointSize               1 
    ======================  ===========
    
    .. versionadded:: NX11.0.0
    """
    
    class ColorModes():
        """
        Specifies point cloud color display mode choice. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Individual", "individual"
           "Uniform", "uniform"
        """
        Individual = 0  # PointCloudBuilderColorModesMemberType
        Uniform = 1  # PointCloudBuilderColorModesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BrightnessModes():
        """
        Specifies point cloud brightness display mode choice. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Uniform", "uniform"
           "Shaded", "Shaded"
        """
        Uniform = 0  # PointCloudBuilderBrightnessModesMemberType
        Shaded = 1  # PointCloudBuilderBrightnessModesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def LoadPointData(self) -> None:
        """
        Loads the selected point cloud data now.  
        
        Signature ``LoadPointData()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
        """
        ...
    
    
    def CreateClippingBoxesListItemBuilder(self) -> PointCloudClippingBoxesListItemBuilder:
        """
        Creates a :py:class:`Display.PointCloudClippingBoxesListItemBuilder`.  
        
        Signature ``CreateClippingBoxesListItemBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
        """
        ...
    
    ClippingBoxesList: PointCloudClippingBoxesListItemBuilderList = ...
    """
    Returns  the list of :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` defining the clipping boxes parameters.  
    
    <hr>
    
    Getter Method
    
    Signature ``ClippingBoxesList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilderList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LoadPointDataWithPart: bool = ...
    """
    Returns or sets  the indication if the point cloud data will be loaded with part load.  
    
    <hr>
    
    Getter Method
    
    Signature ``LoadPointDataWithPart`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LoadPointDataWithPart`` 
    
    :param loadPointDataWithPart: 
    :type loadPointDataWithPart: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
    """
    PointBrightnessMode: PointCloudBuilderBrightnessModes = ...
    """
    Returns or sets  the point brightness display mode 
    
    <hr>
    
    Getter Method
    
    Signature ``PointBrightnessMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.PointCloudBuilderBrightnessModes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointBrightnessMode`` 
    
    :param pointBrightnessMode: 
    :type pointBrightnessMode: :py:class:`NXOpen.Display.PointCloudBuilderBrightnessModes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
    """
    PointColorMode: PointCloudBuilderColorModes = ...
    """
    Returns or sets  the point color display mode 
    
    <hr>
    
    Getter Method
    
    Signature ``PointColorMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.PointCloudBuilderColorModes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointColorMode`` 
    
    :param pointColorMode: 
    :type pointColorMode: :py:class:`NXOpen.Display.PointCloudBuilderColorModes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
    """
    PointDataFile: str = ...
    """
    Returns or sets  the point cloud data file.  
    
    <hr>
    
    Getter Method
    
    Signature ``PointDataFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointDataFile`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
    """
    PointDensity: float = ...
    """
    Returns or sets  the point density 
    
    <hr>
    
    Getter Method
    
    Signature ``PointDensity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointDensity`` 
    
    :param pointDensity: 
    :type pointDensity: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
    """
    PointSize: int = ...
    """
    Returns or sets  the point size 
    
    <hr>
    
    Getter Method
    
    Signature ``PointSize`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointSize`` 
    
    :param pointSize: 
    :type pointSize: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
    """
    Null: PointCloudBuilder = ...  # unknown typename


class RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityType():
    """
    To specify the quality and performance of the interactive, dynamic Ray Traced Studio display.  Affects the number of tiles presented in the display. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "High", "Very small tiles used during progressive updates of ray traced display"
       "Medium", "Medium sized tiles used during progressive updates of ray traced display"
       "Low", "Larger tiles used during progressive updates of ray traced display for faster display time"
    """
    High = 0  # RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityTypeMemberType
    Medium = 1  # RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityTypeMemberType
    Low = 2  # RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityType():
    """
    To specify the quality and performance of the Ray Traced Studio display when dynamic interaction stops 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "High", "Very good ray traced display quality when dynamic interaction stops"
       "Medium", "Good ray traced display quality with good performance when dynamic interaction stops"
       "Low", "The fastest ray traced display performance with preview quality when dynamic interaction stops"
    """
    High = 0  # RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityTypeMemberType
    Medium = 1  # RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityTypeMemberType
    Low = 2  # RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioEditorBuilderStationaryAntialiasingTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioEditorBuilderStationaryAntialiasingType():
    """
    To specify the antialiasing quality during stationary Ray Traced Studio display when dynamic interaction stops 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Medium", "Good antialiasing performed when dynamic interaction stops"
       "Low", "Coarse antialiasing performed when dynamic interaction stops"
       "NotSet", "No antialiasing performed to provide quick, preview of ray traced display when dynamic interaction stops"
    """
    Medium = 0  # RayTracedStudioEditorBuilderStationaryAntialiasingTypeMemberType
    Low = 1  # RayTracedStudioEditorBuilderStationaryAntialiasingTypeMemberType
    NotSet = 2  # RayTracedStudioEditorBuilderStationaryAntialiasingTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioEditorBuilderStaticRayTracedStudioQualityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioEditorBuilderStaticRayTracedStudioQualityType():
    """
    To specify the quality and performance of the Ray Traced Studio display during static image rendering 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "High", "Very good ray traced display quality for static image rendering"
       "Medium", "Good quality ray traced display with good performance for static image rendering"
       "Low", "The fastest ray traced display performance with preview quality for static image rendering"
       "UserDefined", "User specified ray traced display quality for static image rendering"
    """
    High = 0  # RayTracedStudioEditorBuilderStaticRayTracedStudioQualityTypeMemberType
    Medium = 1  # RayTracedStudioEditorBuilderStaticRayTracedStudioQualityTypeMemberType
    Low = 2  # RayTracedStudioEditorBuilderStaticRayTracedStudioQualityTypeMemberType
    UserDefined = 3  # RayTracedStudioEditorBuilderStaticRayTracedStudioQualityTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioEditorBuilderStaticAntialiasingTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioEditorBuilderStaticAntialiasingType():
    """
    To specify the antialiasing quality during stationary Ray Traced Studio display during static image rendering 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "High", "Very good antialiasing performed for static image rendering"
       "Medium", "Good antialiasing performed for static image rendering"
       "Low", "Coarse antialiasing performed for static image rendering"
       "NotSet", "No antialiasing performed to provide quick, preview of ray traced display for static image rendering"
    """
    High = 0  # RayTracedStudioEditorBuilderStaticAntialiasingTypeMemberType
    Medium = 1  # RayTracedStudioEditorBuilderStaticAntialiasingTypeMemberType
    Low = 2  # RayTracedStudioEditorBuilderStaticAntialiasingTypeMemberType
    NotSet = 3  # RayTracedStudioEditorBuilderStaticAntialiasingTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatType():
    """
    To specify the Ray Traced Studio static image file format 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Tif", "Tagged Image File Format (TIFF) file format"
       "Png", "Portable Network Graphic (PNG) file format"
       "Jpg", "Joint Photographic Experts Group (JPEG) file format"
    """
    Tif = 0  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatTypeMemberType
    Png = 1  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatTypeMemberType
    Jpg = 2  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsType():
    """
    To specify the Ray Traced Studio static image units 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Pixels", "static image size specified in pixel"
       "Millimeters", "static image size specified in millimeters"
       "Inches", "static image size specified in inches"
    """
    Pixels = 0  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsTypeMemberType
    Millimeters = 1  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsTypeMemberType
    Inches = 2  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioEditorBuilderRayTracedStudioStaticImageSizeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioEditorBuilderRayTracedStudioStaticImageSizeType():
    """
    To specify the Ray Traced Studio static image size 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "RenderWindow", "Ray Traced Studio window size used for static image output"
       "UserDefined", "user specified size for static image output"
    """
    RenderWindow = 0  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageSizeTypeMemberType
    UserDefined = 1  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageSizeTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioEditorBuilderRayTracedStudioStaticImageOrientationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioEditorBuilderRayTracedStudioStaticImageOrientationType():
    """
    To specify the Ray Traced Studio static image orientation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Landscape", "static image orientation where width is greater than height"
       "Portrait", "static image orientation where height is greater than width"
    """
    Landscape = 0  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageOrientationTypeMemberType
    Portrait = 1  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageOrientationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionType():
    """
    To specify the Ray Traced Studio static image resolution 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "High", "static image output resolution of 300 DPI (dots per inch)"
       "Medium", "static image output resolution of 150 DPI (dots per inch)"
       "Low", "static image output resolution of 72 DPI (dots per inch)"
       "UserDefined", "user specified image output resolution in DPI (dots per inch)"
    """
    High = 0  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionTypeMemberType
    Medium = 1  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionTypeMemberType
    Low = 2  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionTypeMemberType
    UserDefined = 3  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RayTracedStudioEditorBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.RayTracedStudioEditorBuilder`.  
    
    Ray Traced Studio Editor controls display and output of CPU-based real-time ray tracing.
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateRayTracedStudioEditorBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    class DynamicRayTracedStudioTilingQualityType():
        """
        To specify the quality and performance of the interactive, dynamic Ray Traced Studio display.  Affects the number of tiles presented in the display. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "High", "Very small tiles used during progressive updates of ray traced display"
           "Medium", "Medium sized tiles used during progressive updates of ray traced display"
           "Low", "Larger tiles used during progressive updates of ray traced display for faster display time"
        """
        High = 0  # RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityTypeMemberType
        Medium = 1  # RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityTypeMemberType
        Low = 2  # RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class StationaryRayTracedStudioQualityType():
        """
        To specify the quality and performance of the Ray Traced Studio display when dynamic interaction stops 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "High", "Very good ray traced display quality when dynamic interaction stops"
           "Medium", "Good ray traced display quality with good performance when dynamic interaction stops"
           "Low", "The fastest ray traced display performance with preview quality when dynamic interaction stops"
        """
        High = 0  # RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityTypeMemberType
        Medium = 1  # RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityTypeMemberType
        Low = 2  # RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class StationaryAntialiasingType():
        """
        To specify the antialiasing quality during stationary Ray Traced Studio display when dynamic interaction stops 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Medium", "Good antialiasing performed when dynamic interaction stops"
           "Low", "Coarse antialiasing performed when dynamic interaction stops"
           "NotSet", "No antialiasing performed to provide quick, preview of ray traced display when dynamic interaction stops"
        """
        Medium = 0  # RayTracedStudioEditorBuilderStationaryAntialiasingTypeMemberType
        Low = 1  # RayTracedStudioEditorBuilderStationaryAntialiasingTypeMemberType
        NotSet = 2  # RayTracedStudioEditorBuilderStationaryAntialiasingTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class StaticRayTracedStudioQualityType():
        """
        To specify the quality and performance of the Ray Traced Studio display during static image rendering 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "High", "Very good ray traced display quality for static image rendering"
           "Medium", "Good quality ray traced display with good performance for static image rendering"
           "Low", "The fastest ray traced display performance with preview quality for static image rendering"
           "UserDefined", "User specified ray traced display quality for static image rendering"
        """
        High = 0  # RayTracedStudioEditorBuilderStaticRayTracedStudioQualityTypeMemberType
        Medium = 1  # RayTracedStudioEditorBuilderStaticRayTracedStudioQualityTypeMemberType
        Low = 2  # RayTracedStudioEditorBuilderStaticRayTracedStudioQualityTypeMemberType
        UserDefined = 3  # RayTracedStudioEditorBuilderStaticRayTracedStudioQualityTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class StaticAntialiasingType():
        """
        To specify the antialiasing quality during stationary Ray Traced Studio display during static image rendering 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "High", "Very good antialiasing performed for static image rendering"
           "Medium", "Good antialiasing performed for static image rendering"
           "Low", "Coarse antialiasing performed for static image rendering"
           "NotSet", "No antialiasing performed to provide quick, preview of ray traced display for static image rendering"
        """
        High = 0  # RayTracedStudioEditorBuilderStaticAntialiasingTypeMemberType
        Medium = 1  # RayTracedStudioEditorBuilderStaticAntialiasingTypeMemberType
        Low = 2  # RayTracedStudioEditorBuilderStaticAntialiasingTypeMemberType
        NotSet = 3  # RayTracedStudioEditorBuilderStaticAntialiasingTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class RayTracedStudioStaticImageFileFormatType():
        """
        To specify the Ray Traced Studio static image file format 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Tif", "Tagged Image File Format (TIFF) file format"
           "Png", "Portable Network Graphic (PNG) file format"
           "Jpg", "Joint Photographic Experts Group (JPEG) file format"
        """
        Tif = 0  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatTypeMemberType
        Png = 1  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatTypeMemberType
        Jpg = 2  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class RayTracedStudioStaticImageUnitsType():
        """
        To specify the Ray Traced Studio static image units 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Pixels", "static image size specified in pixel"
           "Millimeters", "static image size specified in millimeters"
           "Inches", "static image size specified in inches"
        """
        Pixels = 0  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsTypeMemberType
        Millimeters = 1  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsTypeMemberType
        Inches = 2  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class RayTracedStudioStaticImageSizeType():
        """
        To specify the Ray Traced Studio static image size 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "RenderWindow", "Ray Traced Studio window size used for static image output"
           "UserDefined", "user specified size for static image output"
        """
        RenderWindow = 0  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageSizeTypeMemberType
        UserDefined = 1  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageSizeTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class RayTracedStudioStaticImageOrientationType():
        """
        To specify the Ray Traced Studio static image orientation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Landscape", "static image orientation where width is greater than height"
           "Portrait", "static image orientation where height is greater than width"
        """
        Landscape = 0  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageOrientationTypeMemberType
        Portrait = 1  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageOrientationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class RayTracedStudioStaticImageResolutionType():
        """
        To specify the Ray Traced Studio static image resolution 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "High", "static image output resolution of 300 DPI (dots per inch)"
           "Medium", "static image output resolution of 150 DPI (dots per inch)"
           "Low", "static image output resolution of 72 DPI (dots per inch)"
           "UserDefined", "user specified image output resolution in DPI (dots per inch)"
        """
        High = 0  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionTypeMemberType
        Medium = 1  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionTypeMemberType
        Low = 2  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionTypeMemberType
        UserDefined = 3  # RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    DynamicRayTracedStudioTilingQuality: RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityType = ...
    """
    Returns or sets  the Ray Traced Studio tiling quality during interactive dynamic display 
    
    <hr>
    
    Getter Method
    
    Signature ``DynamicRayTracedStudioTilingQuality`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DynamicRayTracedStudioTilingQuality`` 
    
    :param dynamicRayTracedStudioTilingQuality: 
    :type dynamicRayTracedStudioTilingQuality: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderDynamicRayTracedStudioTilingQualityType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioDisplayGamma: float = ...
    """
    Returns or sets  the Ray Traced Studio display gamma, controls the overall contrast or brightness of the image's midtone values.  
    
    A higher gamma value yields an overall brighter image. 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioDisplayGamma`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioDisplayGamma`` 
    
    :param rayTracedStudioDisplayGamma: 
    :type rayTracedStudioDisplayGamma: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImageDotsPerInch: int = ...
    """
    Returns or sets  the Ray Traced Studio static image dots per inch (DPI) 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImageDotsPerInch`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImageDotsPerInch`` 
    
    :param rayTracedStudioStaticImageDotsPerInch: 
    :type rayTracedStudioStaticImageDotsPerInch: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImageDoubleHeight: float = ...
    """
    Returns or sets  the Ray Traced Studio static image height 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImageDoubleHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImageDoubleHeight`` 
    
    :param rayTracedStudioStaticImageDoubleHeight: 
    :type rayTracedStudioStaticImageDoubleHeight: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImageDoubleWidth: float = ...
    """
    Returns or sets  the Ray Traced Studio static image width 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImageDoubleWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImageDoubleWidth`` 
    
    :param rayTracedStudioStaticImageDoubleWidth: 
    :type rayTracedStudioStaticImageDoubleWidth: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImageFileFormat: RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatType = ...
    """
    Returns or sets  the Ray Traced Studio static output image file format 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImageFileFormat`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImageFileFormat`` 
    
    :param rayTracedStudioStaticImageFileFormat: 
    :type rayTracedStudioStaticImageFileFormat: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderRayTracedStudioStaticImageFileFormatType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImageLockAspectRatio: bool = ...
    """
    Returns or sets  the Ray Traced Studio static image aspect ratio will be maintained 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImageLockAspectRatio`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImageLockAspectRatio`` 
    
    :param rayTracedStudioStaticImageLockAspectRatio: 
    :type rayTracedStudioStaticImageLockAspectRatio: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImageOrientation: RayTracedStudioEditorBuilderRayTracedStudioStaticImageOrientationType = ...
    """
    Returns or sets  the Ray Traced Studio static image orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImageOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderRayTracedStudioStaticImageOrientationType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImageOrientation`` 
    
    :param rayTracedStudioStaticImageOrientation: 
    :type rayTracedStudioStaticImageOrientation: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderRayTracedStudioStaticImageOrientationType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImagePixelHeight: int = ...
    """
    Returns or sets  the Ray Traced Studio static image pixel height 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImagePixelHeight`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImagePixelHeight`` 
    
    :param rayTracedStudioStaticImagePixelHeight: 
    :type rayTracedStudioStaticImagePixelHeight: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImagePixelWidth: int = ...
    """
    Returns or sets  the Ray Traced Studio static image pixel width 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImagePixelWidth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImagePixelWidth`` 
    
    :param rayTracedStudioStaticImagePixelWidth: 
    :type rayTracedStudioStaticImagePixelWidth: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImageResolution: RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionType = ...
    """
    Returns or sets  the Ray Traced Studio static image resolution 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImageResolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImageResolution`` 
    
    :param rayTracedStudioStaticImageResolution: 
    :type rayTracedStudioStaticImageResolution: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderRayTracedStudioStaticImageResolutionType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImageSize: RayTracedStudioEditorBuilderRayTracedStudioStaticImageSizeType = ...
    """
    Returns or sets  the Ray Traced Studio static image size 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImageSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderRayTracedStudioStaticImageSizeType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImageSize`` 
    
    :param rayTracedStudioStaticImageSize: 
    :type rayTracedStudioStaticImageSize: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderRayTracedStudioStaticImageSizeType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RayTracedStudioStaticImageUnits: RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsType = ...
    """
    Returns or sets  the Ray Traced Studio static image units 
    
    <hr>
    
    Getter Method
    
    Signature ``RayTracedStudioStaticImageUnits`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RayTracedStudioStaticImageUnits`` 
    
    :param rayTracedStudioStaticImageUnits: 
    :type rayTracedStudioStaticImageUnits: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderRayTracedStudioStaticImageUnitsType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    StaticAntialiasing: RayTracedStudioEditorBuilderStaticAntialiasingType = ...
    """
    Returns or sets  the Ray Traced Studio static image antialiasing quality 
    
    <hr>
    
    Getter Method
    
    Signature ``StaticAntialiasing`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderStaticAntialiasingType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StaticAntialiasing`` 
    
    :param staticAntialiasing: 
    :type staticAntialiasing: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderStaticAntialiasingType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    StaticRayTracedStudioQuality: RayTracedStudioEditorBuilderStaticRayTracedStudioQualityType = ...
    """
    Returns or sets  the Ray Traced Studio static image quality 
    
    <hr>
    
    Getter Method
    
    Signature ``StaticRayTracedStudioQuality`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderStaticRayTracedStudioQualityType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StaticRayTracedStudioQuality`` 
    
    :param staticRayTracedStudioQuality: 
    :type staticRayTracedStudioQuality: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderStaticRayTracedStudioQualityType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    StaticRayTracedStudioRenderDepth: int = ...
    """
    Returns or sets  the Ray Traced Studio static image render depth, controls the iterations of ray tracing reflection and refraction calculations 
    
    <hr>
    
    Getter Method
    
    Signature ``StaticRayTracedStudioRenderDepth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StaticRayTracedStudioRenderDepth`` 
    
    :param staticRayTracedStudioRenderDepth: 
    :type staticRayTracedStudioRenderDepth: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    StationaryAntialiasing: RayTracedStudioEditorBuilderStationaryAntialiasingType = ...
    """
    Returns or sets  the Ray Traced Studio stationary antialiasing quality when dynamic interaction stops 
    
    <hr>
    
    Getter Method
    
    Signature ``StationaryAntialiasing`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderStationaryAntialiasingType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StationaryAntialiasing`` 
    
    :param stationaryAntialiasing: 
    :type stationaryAntialiasing: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderStationaryAntialiasingType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    StationaryRayTracedStudioQuality: RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityType = ...
    """
    Returns or sets  the Ray Traced Studio stationary display quality when dynamic interaction stops 
    
    <hr>
    
    Getter Method
    
    Signature ``StationaryRayTracedStudioQuality`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StationaryRayTracedStudioQuality`` 
    
    :param stationaryRayTracedStudioQuality: 
    :type stationaryRayTracedStudioQuality: :py:class:`NXOpen.Display.RayTracedStudioEditorBuilderStationaryRayTracedStudioQualityType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    StationaryRayTracedStudioshowStatusIndicator: bool = ...
    """
    Returns or sets  the stationary Ray Traced Studio progess status indicator percent complete display 
    
    <hr>
    
    Getter Method
    
    Signature ``StationaryRayTracedStudioshowStatusIndicator`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StationaryRayTracedStudioshowStatusIndicator`` 
    
    :param stationaryRayTracedStudioshowStatusIndicator: 
    :type stationaryRayTracedStudioshowStatusIndicator: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: RayTracedStudioEditorBuilder = ...  # unknown typename


class PerspectiveOptionsBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.PerspectiveOptionsBuilder`
    
    Cameras are not supported in KF.
    
    .. versionadded:: NX8.0.0
    """
    
    def ApplyLastDistanceChange(self) -> None:
        """
        Sets the work view to have the camera distance, which is the distance from the camera's
        position to the target position in the work view which was specified in the last use of
        :py:meth:`NXOpen.Display.PerspectiveOptionsBuilder.CameraDistance`
        The camera distance has no meaning for an orthographic view, so this method does nothing
        if the work view is an orthographic view.  
        
        Signature ``ApplyLastDistanceChange()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Cancel(self) -> None:
        """
        Cancels the Perspective Options Builder.  
        
        The camera distance of the work view
        is restored to the value it had when the builder was created.
        The camera distance has no meaning for an orthographic view, so this method does nothing
        if the work view is an orthographic view.
        
        Signature ``Cancel()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    CameraDistance: float = ...
    """
    Returns or sets  the camera distance:  The distance from the camera's position to the
    target position in the work view view when it is a perspective view.  
    
    The camera distance has no meaning for an orthographic view, so this property is not
    applicable if the work view is an orthographic view.           
    
    <hr>
    
    Getter Method
    
    Signature ``CameraDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CameraDistance`` 
    
    :param cameraDistance: 
    :type cameraDistance: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: PerspectiveOptionsBuilder = ...  # unknown typename


class CameraCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection cameras
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    @typing.overload
    def CreateCameraBuilder(self, camera: Camera) -> CameraBuilder:
        """
        Creates a :py:class:`NXOpen.Display.CameraBuilder` object if camera is None. 
        Otherwise, a Camera object will be edited. If camera is not None and the camera is
        associated with a view other than the work view, then the camera will be applied to
        the current work view.  
        
        Signature ``CreateCameraBuilder(camera)`` 
        
        :param camera:  If camera is not None, then this object will be edited  
        :type camera: :py:class:`NXOpen.Display.Camera` 
        :returns:  return camera builder  
        :rtype: :py:class:`NXOpen.Display.CameraBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateCameraBuilder(self, camera: Camera, applyCameraToView: bool) -> CameraBuilder:
        """
        Creates a :py:class:`NXOpen.Display.CameraBuilder` object if camera is None.
        Otherwise, a Camera object will be edited. If camera is not None and the camera is
        associated with a view other than the work view, then the camera will be applied to the
        current work view if and only if applyCameraToView is true. 
        
        Signature ``CreateCameraBuilder(camera, applyCameraToView)`` 
        
        :param camera:  If camera is not None, then this object will be edited  
        :type camera: :py:class:`NXOpen.Display.Camera` 
        :param applyCameraToView:  true if the camera is to be applied to its view  
        :type applyCameraToView: bool 
        :returns:  return camera builder  
        :rtype: :py:class:`NXOpen.Display.CameraBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateCameraBuilder(self, view: NXOpen.View, layout: NXOpen.Layout, camera: Camera) -> CameraBuilder:
        """
        Creates a :py:class:`NXOpen.Display.CameraBuilder` object if camera is None.
        Otherwise, a Camera object will be edited.  Initializes the camera with data from the view
        in the layout.  If camera is not None and the camera is associated with a view other
        than the work view, then the camera will be applied to the current work view. 
        
        Signature ``CreateCameraBuilder(view, layout, camera)`` 
        
        :param view:  Use this view's data to initialize the camera  
        :type view: :py:class:`NXOpen.View` 
        :param layout:  Layout of the view  
        :type layout: :py:class:`NXOpen.Layout` 
        :param camera:  If camera is not None, then this object will be edited  
        :type camera: :py:class:`NXOpen.Display.Camera` 
        :returns:  return camera builder  
        :rtype: :py:class:`NXOpen.Display.CameraBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateCameraBuilder(self, view: NXOpen.View, layout: NXOpen.Layout, camera: Camera, applyCameraToView: bool) -> CameraBuilder:
        """
        Creates a :py:class:`NXOpen.Display.CameraBuilder` object if camera is None.
        Otherwise, a Camera object will be edited.  Initializes the camera with data from the view
        in the layout.  If camera is not None and the camera is associated with a view other
        than the work view, then the camera will be applied to the current work view if and only if
        applyCameraToView is truel.
        
        Signature ``CreateCameraBuilder(view, layout, camera, applyCameraToView)`` 
        
        :param view:  Use this view's data to initialize the camera  
        :type view: :py:class:`NXOpen.View` 
        :param layout:  Layout of the view  
        :type layout: :py:class:`NXOpen.Layout` 
        :param camera:  If camera is not None, then this object will be edited  
        :type camera: :py:class:`NXOpen.Display.Camera` 
        :param applyCameraToView:  true if the camera is to be applied to its view  
        :type applyCameraToView: bool 
        :returns:  return camera builder  
        :rtype: :py:class:`NXOpen.Display.CameraBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Camera:
        """
        Finds the :py:class:`NXOpen.Display.Camera` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  Camera found  
        :rtype: :py:class:`NXOpen.Display.Camera` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class LightBuilderShadowTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LightBuilderShadowType():
    """
    shadow types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No shadows will be produced."
       "SoftEdged", "Soft-edged,approximated shadows will be generated using a shadow mapping algorithm."
       "HardEdged", "Hard-edged, precise shadows will be generated using a ray-tracing algorithm."
       "TranslucentHard", "Hard-edged, precise shadows will be generated using a ray-tracing algorithm. Shadows from translucent objects will also be generated and their color will be determined by the transparent object's color."
    """
    NotSet = 0  # LightBuilderShadowTypeMemberType
    SoftEdged = 1  # LightBuilderShadowTypeMemberType
    HardEdged = 2  # LightBuilderShadowTypeMemberType
    TranslucentHard = 3  # LightBuilderShadowTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LightBuilderLightModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LightBuilderLightMode():
    """
    light_mode 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FixedToObserver", " - "
       "FixedToThePart", " - "
    """
    FixedToObserver = 0  # LightBuilderLightModeMemberType
    FixedToThePart = 1  # LightBuilderLightModeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LightBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.LightBuilder`
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateLightBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class ShadowType():
        """
        shadow types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No shadows will be produced."
           "SoftEdged", "Soft-edged,approximated shadows will be generated using a shadow mapping algorithm."
           "HardEdged", "Hard-edged, precise shadows will be generated using a ray-tracing algorithm."
           "TranslucentHard", "Hard-edged, precise shadows will be generated using a ray-tracing algorithm. Shadows from translucent objects will also be generated and their color will be determined by the transparent object's color."
        """
        NotSet = 0  # LightBuilderShadowTypeMemberType
        SoftEdged = 1  # LightBuilderShadowTypeMemberType
        HardEdged = 2  # LightBuilderShadowTypeMemberType
        TranslucentHard = 3  # LightBuilderShadowTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LightMode():
        """
        light_mode 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FixedToObserver", " - "
           "FixedToThePart", " - "
        """
        FixedToObserver = 0  # LightBuilderLightModeMemberType
        FixedToThePart = 1  # LightBuilderLightModeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    ConeAngle: float = ...
    """
    Returns or sets  the cone angle - only applicable to spot light types 
    
    <hr>
    
    Getter Method
    
    Signature ``ConeAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConeAngle`` 
    
    :param coneAngle: 
    :type coneAngle: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    DestinationPosition: NXOpen.Point = ...
    """
    Returns or sets  the destination position - only applicable to spot light types 
    
    <hr>
    
    Getter Method
    
    Signature ``DestinationPosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DestinationPosition`` 
    
    :param destinationPosition: 
    :type destinationPosition: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Intensity: float = ...
    """
    Returns or sets  the brightness intensity for a given light 
    
    <hr>
    
    Getter Method
    
    Signature ``Intensity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Intensity`` 
    
    :param intensity: 
    :type intensity: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    LightShadowType: LightBuilderShadowType = ...
    """
    Returns or sets  the light shadow type - not applicable to ambient or eye light types 
    
    <hr>
    
    Getter Method
    
    Signature ``LightShadowType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.LightBuilderShadowType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LightShadowType`` 
    
    :param lightShadowType: 
    :type lightShadowType: :py:class:`NXOpen.Display.LightBuilderShadowType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    LightType: NXOpen.LightType = ...
    """
    Returns or sets  the light type for a particular light 
    
    <hr>
    
    Getter Method
    
    Signature ``LightType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LightType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LightType`` 
    
    :param lightType: 
    :type lightType: :py:class:`NXOpen.LightType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    SourcePosition: NXOpen.Point = ...
    """
    Returns or sets  the source position - only applicable to spot and point light types 
    
    <hr>
    
    Getter Method
    
    Signature ``SourcePosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SourcePosition`` 
    
    :param sourcePosition: 
    :type sourcePosition: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    UseWithAdvancedStudioImageBasedLighting: bool = ...
    """
    Returns or sets  the flag to indicate whether the given light is to be used with image based lighting in the advanced studio display.  
    
    <hr>
    
    Getter Method
    
    Signature ``UseWithAdvancedStudioImageBasedLighting`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseWithAdvancedStudioImageBasedLighting`` 
    
    :param useWithAdvancedStudioIBl: 
    :type useWithAdvancedStudioIBl: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    UseWithIbl: bool = ...
    """
    Returns or sets  the use_with_ibl flag for a given light 
    
    <hr>
    
    Getter Method
    
    Signature ``UseWithIbl`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX10.0.0
       This funcationality is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseWithIbl`` 
    
    :param useWithIBL: 
    :type useWithIBL: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX10.0.0
       This funcationality is no longer supported.
    
    License requirements: None.
    """
    UseWithRayTracedImageBasedLighting: bool = ...
    """
    Returns or sets  the flag to indicate whether the given light is to be used with image based lighting in ray traced rendering.  
    
    <hr>
    
    Getter Method
    
    Signature ``UseWithRayTracedImageBasedLighting`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseWithRayTracedImageBasedLighting`` 
    
    :param useWithRayTracedIBL: 
    :type useWithRayTracedIBL: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: LightBuilder = ...  # unknown typename


class TrueShading(NXOpen.NXObject):
    """
    Represents a True Shading object   
    
    TrueShading is not supported in KF.
    
    .. versionadded:: NX6.0.0
    """
    Null: TrueShading = ...  # unknown typename


class StudioImageCaptureBuilderUnitsEnumTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StudioImageCaptureBuilderUnitsEnumType():
    """
    Provide the following resolution unit options to screen capture 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Pixels", "Use pixel to define resolution"
       "Mm", "Use Millimeters to define resolution"
       "Inches", "Use Inched to define resolution"
    """
    Pixels = 0  # StudioImageCaptureBuilderUnitsEnumTypeMemberType
    Mm = 1  # StudioImageCaptureBuilderUnitsEnumTypeMemberType
    Inches = 2  # StudioImageCaptureBuilderUnitsEnumTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StudioImageCaptureBuilderOrientEnumTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StudioImageCaptureBuilderOrientEnumType():
    """
    Provide the following options to image orientation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Landscape", "Capture image in landscape mode"
       "Portrait", "Capture image in portrait mode"
    """
    Landscape = 0  # StudioImageCaptureBuilderOrientEnumTypeMemberType
    Portrait = 1  # StudioImageCaptureBuilderOrientEnumTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StudioImageCaptureBuilderDrawingSizeEnumType():
    """
    Provide the following standard Drawing sizes 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Isoa4", "Use ISO A4 drawing size"
       "Isoa3", "Use ISO A3 drawing size"
       "Isoa2", "Use ISO A2 drawing size"
       "Isoa1", "Use ISO A1 drawing size"
       "Isoa0", "Use ISO A0 drawing size"
       "Ansia", "Use ANSI A drawing size"
       "Ansib", "Use ANSI B drawing size"
       "Ansic", "Use ANSI C drawing size"
       "Ansid", "Use ANSI D drawing size"
       "Ansie", "Use ANSI E drawing size"
       "Custom", "Use custom defined drawing size"
    """
    Isoa4 = 0  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    Isoa3 = 1  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    Isoa2 = 2  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    Isoa1 = 3  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    Isoa0 = 4  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    Ansia = 5  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    Ansib = 6  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    Ansic = 7  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    Ansid = 8  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    Ansie = 9  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    Custom = 10  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StudioImageCaptureBuilderDPIEnumTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StudioImageCaptureBuilderDPIEnumType():
    """
    Provide the following screen capture resolutions in dots per inch 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Dpi72", "Set image at 72 DPI resolution"
       "Dpi150", "Set image at 150 DPI resolution"
    """
    Dpi72 = 0  # StudioImageCaptureBuilderDPIEnumTypeMemberType
    Dpi150 = 1  # StudioImageCaptureBuilderDPIEnumTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StudioImageCaptureBuilderAASamplesEnumTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StudioImageCaptureBuilderAASamplesEnumType():
    """
    Provide the following anti-aliasing sample size for off screen image capture 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Sam0X", "Do not set sampling option"
       "Sam2X", "Set sampling at 2 times"
       "Sam4X", "Set sampling at 4 times"
       "Sam8X", "Set sampling at 8 times"
       "Sam16X", "Set sampling at 16 times"
    """
    Sam0X = 0  # StudioImageCaptureBuilderAASamplesEnumTypeMemberType
    Sam2X = 1  # StudioImageCaptureBuilderAASamplesEnumTypeMemberType
    Sam4X = 2  # StudioImageCaptureBuilderAASamplesEnumTypeMemberType
    Sam8X = 3  # StudioImageCaptureBuilderAASamplesEnumTypeMemberType
    Sam16X = 4  # StudioImageCaptureBuilderAASamplesEnumTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class StudioImageCaptureBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.StudioImageCaptureBuilder`  
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateStudioImageCaptureBuilder`
    
    Default values.
    
    ================  ==========
    Property          Value
    ================  ==========
    AASamplesEnum     Sam0X 
    ----------------  ----------
    DpiEnum           Dpi72 
    ----------------  ----------
    DrawingSizeEnum   Isoa4 
    ----------------  ----------
    OrientEnum        Landscape 
    ----------------  ----------
    UnitsEnum         Pixels 
    ================  ==========
    
    .. versionadded:: NX6.0.4
    """
    
    class UnitsEnumType():
        """
        Provide the following resolution unit options to screen capture 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Pixels", "Use pixel to define resolution"
           "Mm", "Use Millimeters to define resolution"
           "Inches", "Use Inched to define resolution"
        """
        Pixels = 0  # StudioImageCaptureBuilderUnitsEnumTypeMemberType
        Mm = 1  # StudioImageCaptureBuilderUnitsEnumTypeMemberType
        Inches = 2  # StudioImageCaptureBuilderUnitsEnumTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OrientEnumType():
        """
        Provide the following options to image orientation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Landscape", "Capture image in landscape mode"
           "Portrait", "Capture image in portrait mode"
        """
        Landscape = 0  # StudioImageCaptureBuilderOrientEnumTypeMemberType
        Portrait = 1  # StudioImageCaptureBuilderOrientEnumTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DrawingSizeEnumType():
        """
        Provide the following standard Drawing sizes 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Isoa4", "Use ISO A4 drawing size"
           "Isoa3", "Use ISO A3 drawing size"
           "Isoa2", "Use ISO A2 drawing size"
           "Isoa1", "Use ISO A1 drawing size"
           "Isoa0", "Use ISO A0 drawing size"
           "Ansia", "Use ANSI A drawing size"
           "Ansib", "Use ANSI B drawing size"
           "Ansic", "Use ANSI C drawing size"
           "Ansid", "Use ANSI D drawing size"
           "Ansie", "Use ANSI E drawing size"
           "Custom", "Use custom defined drawing size"
        """
        Isoa4 = 0  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        Isoa3 = 1  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        Isoa2 = 2  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        Isoa1 = 3  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        Isoa0 = 4  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        Ansia = 5  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        Ansib = 6  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        Ansic = 7  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        Ansid = 8  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        Ansie = 9  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        Custom = 10  # StudioImageCaptureBuilderDrawingSizeEnumTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DPIEnumType():
        """
        Provide the following screen capture resolutions in dots per inch 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Dpi72", "Set image at 72 DPI resolution"
           "Dpi150", "Set image at 150 DPI resolution"
        """
        Dpi72 = 0  # StudioImageCaptureBuilderDPIEnumTypeMemberType
        Dpi150 = 1  # StudioImageCaptureBuilderDPIEnumTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class AASamplesEnumType():
        """
        Provide the following anti-aliasing sample size for off screen image capture 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Sam0X", "Do not set sampling option"
           "Sam2X", "Set sampling at 2 times"
           "Sam4X", "Set sampling at 4 times"
           "Sam8X", "Set sampling at 8 times"
           "Sam16X", "Set sampling at 16 times"
        """
        Sam0X = 0  # StudioImageCaptureBuilderAASamplesEnumTypeMemberType
        Sam2X = 1  # StudioImageCaptureBuilderAASamplesEnumTypeMemberType
        Sam4X = 2  # StudioImageCaptureBuilderAASamplesEnumTypeMemberType
        Sam8X = 3  # StudioImageCaptureBuilderAASamplesEnumTypeMemberType
        Sam16X = 4  # StudioImageCaptureBuilderAASamplesEnumTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetImageDimensionsDouble(self) -> 'list[float]':
        """
        Gets the double image dimensions, height and width  
        
        Signature ``GetImageDimensionsDouble()`` 
        
        :returns:  array of 2 doubles  
        :rtype: list of float 
        
        .. versionadded:: NX6.0.4
        
        License requirements: None.
        """
        ...
    
    
    def SetImageDimensionsDouble(self, imageDimensionsDouble: 'list[float]') -> None:
        """
        Sets the double image dimensions, height and width 
        
        Signature ``SetImageDimensionsDouble(imageDimensionsDouble)`` 
        
        :param imageDimensionsDouble:  array of 2 doubles  
        :type imageDimensionsDouble: list of float 
        
        .. versionadded:: NX6.0.4
        
        License requirements: None.
        """
        ...
    
    
    def GetImageDimensionsInteger(self) -> 'list[int]':
        """
        Gets the integer image dimensions, height and width  
        
        Signature ``GetImageDimensionsInteger()`` 
        
        :returns:  array of 2 integers  
        :rtype: list of int 
        
        .. versionadded:: NX6.0.4
        
        License requirements: None.
        """
        ...
    
    
    def SetImageDimensionsInteger(self, imageDimensionsInteger: 'list[int]') -> None:
        """
        Sets the integer image dimensions, height and width 
        
        Signature ``SetImageDimensionsInteger(imageDimensionsInteger)`` 
        
        :param imageDimensionsInteger:  array of 2 integers  
        :type imageDimensionsInteger: list of int 
        
        .. versionadded:: NX6.0.4
        
        License requirements: None.
        """
        ...
    
    AASamplesEnum: StudioImageCaptureBuilderAASamplesEnumType = ...
    """
    Returns or sets  the antialiasing samples enum 
    
    <hr>
    
    Getter Method
    
    Signature ``AASamplesEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.StudioImageCaptureBuilderAASamplesEnumType` 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AASamplesEnum`` 
    
    :param aASamplesEnum: 
    :type aASamplesEnum: :py:class:`NXOpen.Display.StudioImageCaptureBuilderAASamplesEnumType` 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    """
    DpiEnum: StudioImageCaptureBuilderDPIEnumType = ...
    """
    Returns or sets  the dpi enum 
    
    <hr>
    
    Getter Method
    
    Signature ``DpiEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.StudioImageCaptureBuilderDPIEnumType` 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DpiEnum`` 
    
    :param dpiEnum: 
    :type dpiEnum: :py:class:`NXOpen.Display.StudioImageCaptureBuilderDPIEnumType` 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    """
    DrawingSizeEnum: StudioImageCaptureBuilderDrawingSizeEnumType = ...
    """
    Returns or sets  the drawing size enum 
    
    <hr>
    
    Getter Method
    
    Signature ``DrawingSizeEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.StudioImageCaptureBuilderDrawingSizeEnumType` 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DrawingSizeEnum`` 
    
    :param drawingSizeEnum: 
    :type drawingSizeEnum: :py:class:`NXOpen.Display.StudioImageCaptureBuilderDrawingSizeEnumType` 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    """
    NativeFileBrowser: str = ...
    """
    Returns or sets  the native file browser for image type to produce 
    
    <hr>
    
    Getter Method
    
    Signature ``NativeFileBrowser`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NativeFileBrowser`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    """
    OrientEnum: StudioImageCaptureBuilderOrientEnumType = ...
    """
    Returns or sets  the orient enum 
    
    <hr>
    
    Getter Method
    
    Signature ``OrientEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.StudioImageCaptureBuilderOrientEnumType` 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OrientEnum`` 
    
    :param orientEnum: 
    :type orientEnum: :py:class:`NXOpen.Display.StudioImageCaptureBuilderOrientEnumType` 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    """
    UnitsEnum: StudioImageCaptureBuilderUnitsEnumType = ...
    """
    Returns or sets  the units enum 
    
    <hr>
    
    Getter Method
    
    Signature ``UnitsEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.StudioImageCaptureBuilderUnitsEnumType` 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UnitsEnum`` 
    
    :param unitsEnum: 
    :type unitsEnum: :py:class:`NXOpen.Display.StudioImageCaptureBuilderUnitsEnumType` 
    
    .. versionadded:: NX6.0.4
    
    License requirements: None.
    """
    Null: StudioImageCaptureBuilder = ...  # unknown typename


class PointCloudCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of point cloud objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX11.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> PointCloud:
        """
        Finds the :py:class:`NXOpen.Display.PointCloud` with the given   
        identifier as recorded in a journal.  
        
        An object may not return the same  
        value as its JournalIdentifier in different versions of the software.   
        However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In 
        general, this method should not be used in handwritten code and exists 
        to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given 
        journal identifier. 
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  Reference point cloud found  
        :rtype: :py:class:`NXOpen.Display.PointCloud` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreatePointCloudBuilder(self, referencePointCloud: PointCloud) -> PointCloudBuilder:
        """
        Creates a :py:class:`NXOpen.Display.PointCloudBuilder` object
        used to build a point cloud.  
        
        If the referencePointCloud is not None, the referencePointCloud object will be edited.
        
        Signature ``CreatePointCloudBuilder(referencePointCloud)`` 
        
        :param referencePointCloud:  If referencePointCloud is not None,                                                                                                     this object will be edited  
        :type referencePointCloud: :py:class:`NXOpen.Display.PointCloud` 
        :returns:  Point cloud builder  
        :rtype: :py:class:`NXOpen.Display.PointCloudBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
        """
        ...
    


class NonProportionalZoomMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NonProportionalZoomMethodType():
    """
    Sets the kind of mouse interaction that will define the non-proportional zoom. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Rectangle", "Uses a rectangular region to be zoomed."
       "Dynamic", "Defines a line to define aspect ratio of non-proportional zoom."
    """
    Rectangle = 0  # NonProportionalZoomMethodTypeMemberType
    Dynamic = 1  # NonProportionalZoomMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NonProportionalZoom(NXOpen.Builder):
    """
    Provides non-proportional zoom capability   
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateNonProportionalZoom`
    
    Default values.
    
    ================  ========
    Property          Value
    ================  ========
    AnchorCenter      0 
    ----------------  --------
    Method            Dynamic 
    ----------------  --------
    ZoomSensitivity   5 
    ================  ========
    
    .. versionadded:: NX7.0.0
    """
    
    class MethodType():
        """
        Sets the kind of mouse interaction that will define the non-proportional zoom. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Rectangle", "Uses a rectangular region to be zoomed."
           "Dynamic", "Defines a line to define aspect ratio of non-proportional zoom."
        """
        Rectangle = 0  # NonProportionalZoomMethodTypeMemberType
        Dynamic = 1  # NonProportionalZoomMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Start(self, view: NXOpen.View) -> None:
        """
        Prepares NX to receive one or more gestures delimited by pairs of points
        which define a non-proportional zoom.  
        
        This function records the display state
        to which the view will return when non-proportional zoom is disabled. In a typical
        scenario, call start.  Then call first point accompanied by one or more calls to
        second point, followed by a call to finish, followed optionaly by further 
        first point/second point/finish combinations of calls. 
        
        Signature ``Start(view)`` 
        
        :param view:  the view to receive gestures  
        :type view: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def FirstPoint(self, point1: NXOpen.Point3d, view: NXOpen.View) -> None:
        """
        Scales the specified view non-proportionally in the horizontal (X) and vertical (Y)
        dimensions, based on a mouse gesture defined by two points in a view.  
        
        Based on
        :py:class:`NXOpen.Display.NonProportionalZoomMethodType` setting, the gesture may be
        interpreted as a bounding box or a line, but will determine the XY aspect ratio and the zoom.
        
        In batch mode, the the aspect ratio, scale and center of the view are modified,
        but no display occurs.
        
        Signature ``FirstPoint(point1, view)`` 
        
        :param point1:  First point in a mouse gesture to define a non-proportional zoom  
        :type point1: :py:class:`NXOpen.Point3d` 
        :param view:  Apply pan (if any) and scale in this view only, if it still exists  
        :type view: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def SecondPoint(self, point2: NXOpen.Point3d, view: NXOpen.View) -> None:
        """
        Scales the specified view non-proportionally in the horizontal (X) and vertical (Y)
        dimensions, based on a mouse gesture defined by two points in a view.  
        
        Call this once
        for every call to first point, to redefine a non-proportional zoom.
        
        In batch mode, the the aspect ratio, scale and center of the view are modified,
        but no display occurs.
        
        Signature ``SecondPoint(point2, view)`` 
        
        :param point2:  Second point in a mouse gesture to define a non-proportional zoom  
        :type point2: :py:class:`NXOpen.Point3d` 
        :param view:  Apply pan (if any) and scale in this view only, if it still exists  
        :type view: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def Finish(self, view: NXOpen.View) -> None:
        """
        Signals the completion of a non-proportional zoom defined by one or more pairs
        of points defined by a mouse gesture.  
        
        Signature ``Finish(view)`` 
        
        :param view:  the view to receive gestures  
        :type view: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def Enable(self, enable: bool) -> None:
        """
        Enables non-proportional zoom.  
        
        In batch mode, the the aspect ratio, scale and center of the view are modified,
        but no display occurs.
        
        Signature ``Enable(enable)`` 
        
        :param enable:  True if using the previously defined non-proportional zoom  
        :type enable: bool 
        
        .. versionadded:: NX7.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    AnchorCenter: bool = ...
    """
    Returns or sets  a value indicating if the display will be recentered on the initial line endpoint 
    
    <hr>
    
    Getter Method
    
    Signature ``AnchorCenter`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnchorCenter`` 
    
    :param anchorCenter: 
    :type anchorCenter: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Method: NonProportionalZoomMethodType = ...
    """
    Returns or sets  the type of mouse interaction used to define the non-proportional zoom.  
    
    <hr>
    
    Getter Method
    
    Signature ``Method`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.NonProportionalZoomMethodType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Method`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Display.NonProportionalZoomMethodType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ZoomSensitivity: int = ...
    """
    Returns or sets  the sensitivity of the zoom relative to the length of the drawn line 
    
    <hr>
    
    Getter Method
    
    Signature ``ZoomSensitivity`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZoomSensitivity`` 
    
    :param sensitivity: 
    :type sensitivity: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: NonProportionalZoom = ...  # unknown typename


class IrayPlusMaterialEditorBuilderLayerTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IrayPlusMaterialEditorBuilderLayerType():
    """
    Layer types used in iray plus material 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Coatings", "Coating layers"
       "Base", "Base layer"
       "Geometry", "Base Geometry layer"
       "TextureSpace", "Global texture space layer"
       "MaxNumber", "max layer type"
    """
    Coatings = 0  # IrayPlusMaterialEditorBuilderLayerTypeMemberType
    Base = 1  # IrayPlusMaterialEditorBuilderLayerTypeMemberType
    Geometry = 2  # IrayPlusMaterialEditorBuilderLayerTypeMemberType
    TextureSpace = 3  # IrayPlusMaterialEditorBuilderLayerTypeMemberType
    MaxNumber = 4  # IrayPlusMaterialEditorBuilderLayerTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IrayPlusMaterialEditorBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.IrayPlusMaterialEditorBuilder` 
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    The IrayPlusMaterialEditorBuilder used to manipulate specific material for IrayPlus.
    It maintained an IrayPlusMatAttribute based hierarchical structure corresponding to the 
    xml structure of IrayPlus material.
    
    The example of the hierarchical structure for material Varnished Cherry is:
    
    Material-Layers
    -ClearCoat
    -Attribute1
    -Attribute2
    -...
    -Base
    -Attribute1
    -Attribute2
    -...
    -Geometry
    -Attribute1
    -Attribute2
    -...
    -Global Texture Space
    -Attribute1
    -Attribute2
    -...
    Each node in the hierarchy is an IrayPlusMatAttribute object.
    This structure been created when the IrayPlusMaterialEditorBuilder creating process.
    
    Example for general workflow of set parameter show bellow:
    (1)Use GetMaterialLayersInfo() to get names and unique names
    of all the layers and components of the material.
    For the example Varnished Cherry material. 
    It will return 4 names:[ClearCoat,Base,Geometry,Global Texture Space] and 4 unique names:[
    model2_'Varnished Cherry_Layer_198, Matte, BaseGeometry,Box].
    
    (2)Then we can use these name to call GetComponentInfo()
    to get the parameters of each component:
    If we use 'Base' as component name. The attribute number will return 18. The attribute list
    will return array like:[Base-Base Type, Base-Colour-Interface Type,...]
    
    (3)Use GetComponentParameter() to get attribute object of specific attribute name.
    We can use 'Base-Colour-Interface Type' as parameter to call GetComponentParameter().
    It will return the pointer of IrayPlusMatAttribute object of this attribute.User can 
    modify the value of the IrayPlusMatAttribute object.
    
    (4)Use SetComponentParameter() to set the value of attribute.
    After modify IrayPlusMatAttribute object returned by GetComponentParameter().
    We can use 'Base-Colour-Interface Type' and the pointer to IrayPlusMatAttribute object that
    been modified as parameter to call SetComponentParameter() to set the value into hierarchy.
    
    (5)If you did any change of hierarchy. You need to call builder's commit() function to
    make hierarchy apply to IrayPlus Rendeing engine to make all your modification have effect.
    
    NOTE: The detail rule of using each function see comments of specific function.
    
    .. versionadded:: NX11.0.0
    """
    
    class LayerType():
        """
        Layer types used in iray plus material 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Coatings", "Coating layers"
           "Base", "Base layer"
           "Geometry", "Base Geometry layer"
           "TextureSpace", "Global texture space layer"
           "MaxNumber", "max layer type"
        """
        Coatings = 0  # IrayPlusMaterialEditorBuilderLayerTypeMemberType
        Base = 1  # IrayPlusMaterialEditorBuilderLayerTypeMemberType
        Geometry = 2  # IrayPlusMaterialEditorBuilderLayerTypeMemberType
        TextureSpace = 3  # IrayPlusMaterialEditorBuilderLayerTypeMemberType
        MaxNumber = 4  # IrayPlusMaterialEditorBuilderLayerTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetMaterialLayersInfo(self) -> tuple:
        """
        Get all the components unique name and type name of this material.  
        
        The order in list have meanings. The Layers's components are put into the list first.
        So the index of component in list are same of index in Layers.
        Other Base, Global TextureSplace are insert into the list after Layer's components.
        
        Use system material 'Varnished Cherry' as example. Set attribueName paramter to ''Varnished Cherry'.
        It will return 4 items in type_list:[ClearCoat,Base,Geometry,Global Texture Space] 
        and 4 item in unique_name_list:[model2_'Varnished Cherry_Layer_198, Matte, BaseGeometry,Box].
        
        The type_list output the type for sublayer in Layers and name for Base,Geometry,Global Texture Space.
        The unique_name_list output the unique name of each layers and types for Base,Geometry,Global Texture Space.
        
        When user use these name to get or set attribute for the specific components. They should use 
        'Base' 'Geometry' 'Global Texture Space' for fixed components. But for components in Layers. 
        
        NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
        session. 
        User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
        Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
        This is because the unique name for each layers would change between each session.
        
        For example if user want to set or get the attribute of ClearCoat of material ''Varnished Cherry'. They should
        use '0' as the paramter name to call GetComponentParameter or SetComponentParameter.
        
        Signature ``GetMaterialLayersInfo()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (typeList, uniqueNameList). typeList is a list of str. uniqueNameList is a list of str. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def GetComponentInfo(self, componentName: str) -> tuple:
        """
        Get all the attribute name of a component.  
        
        The string attribute name format should be the component
        name. 
        
        Let material ''Varnished Cherry' for example:
        
        If user wants to get component's sub attribute names of 'Base' component. They should input 'Base' as 
        componentName paramter.
        Then the attribueObject output the pointer to the IrayPlusMatAttribute object of 'Base' component in
        the hierarchy. The attrib_list will return array of all the attribute name of the 'Base' component like
        [Base-Base Type, Base-Colour-Interface Type,...]
        
        If user wants to get layer's sub attribute names of 'ClearCoat'. They should use '0' as componentName paramter.
        Then the attribueObject output the pointer to the IrayPlusMatAttribute object of 'ClearCoat' layer in
        the hierarchy. The attrib_list will return array of all the attribute name of the 'ClearCoat' layer like
        [model2_'Varnished Cherry_Layer_198-Layer Type, model2_'Varnished Cherry_Layer_198-Colour-Interface Type,...]
        
        NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
        session. 
        User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
        Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
        This is because the unique name for each layers would change between each session.
        
        Signature ``GetComponentInfo(componentName)`` 
        
        :param componentName: 
        :type componentName: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (attribueObject, attribList). attribueObject is a :py:class:`NXOpen.Display.IrayPlusMaterialAttribute`. attribList is a list of str. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def AddComponent(self, componentType: str) -> tuple:
        """
        Adds a component to layers for specific layer type.  
        
        Let material ''Varnished Cherry' for example:
        
        If user wants to add 'Dir1' layer into Layers. They should use 'Dir1' to componentType paramter.
        Then the added_layer_index output the added layer's new index. It will return 1 for 'Dir1' index 
        .Because the 'ClearCoat' will be index 0. 
        
        componentUniqueName parameter will return the unique name of 'Dir1':
        'model2_'Varnished Cherry_Layer_262'. 
        
        You can also add more than one layers for same type. You can add 'Dir1' into ''Varnished Cherry'
        again. The added_layer_index would return 2. The componentUniqueName parameter will return the 
        unique name of new added 'Dir2' : 'model2_'Varnished Cherry_Layer_281'
        
        Signature ``AddComponent(componentType)`` 
        
        :param componentType: 
        :type componentType: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (componentUniqueName, addedLayerIndex). componentUniqueName is a str. addedLayerIndex is a int. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def RemoveComponent(self, index: int, componentType: str) -> None:
        """
        Removes a component to layers for specific layer index
        
        Let material ''Varnished Cherry' for example:
        If use changed the material has two Layers: Dir1 and ClearCoat.  
        
        Then user wants to remove 'Dir1' layer from Layers. They should use 1 as index paramter.
        
        The parameter componentType should input the layer type of the layer that you want to remove.
        This make the deleting more type safe.
        User should set 'Dir1' as componentType for this example.
        
        Signature ``RemoveComponent(index, componentType)`` 
        
        :param index: 
        :type index: int 
        :param componentType: 
        :type componentType: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def MoveComponent(self, index: int, componentType: str, moveUp: bool) -> None:
        """
        Moves a component of layers up and down of layers stack.  
        
        Let material ''Varnished Cherry' for example:
        If use changed the material has two Layers: Dir1 and ClearCoat.
        Then user wants to move 'Dir1' layer down in Layers. They should use 1 as index paramter.
        
        The parameter componentType should input the layer type of the layer that you want to move.
        This make the deleting more type safe.
        User should set 'Dir1' as componentType for this example.
        
        move_up parameter should be 'false' for this example.
        
        Signature ``MoveComponent(index, componentType, moveUp)`` 
        
        :param index: 
        :type index: int 
        :param componentType: 
        :type componentType: str 
        :param moveUp: 
        :type moveUp: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def GetComponentParameter(self, attribueName: str) -> IrayPlusMaterialAttribute:
        """
        Gets single attribute object for specific fomatted attribute name 
        The string attribute name format should be : 
        "layer name-interface name-attribute name"
        
        Let material ''Varnished Cherry' for example:
        
        If user wants to get 'Base' component's attribueObject of 'Base-Colour-Colour'.  
        
        They should input 
        'Base-Colour-Colour' as componentName paramter.
        Then the attribueObject output the pointer to the IrayPlusMatAttribute object of 'Base-Colour-Colour' 
        component in the hierarchy. 
        
        If user wants to get layer's sub attribute of 'ClearCoat'. They should use index in componentName paramter:
        'Layers-0-ReflectionColour-ColourOffset'
        Then the attribueObject output the pointer to the IrayPlusMatAttribute object of 'ReflectionColour-ColourOffset' 
        attribute of 'ClearCoat' layer in the hierarchy. 
        
        NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
        session. 
        User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
        Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
        This is because the unique name for each layers would change between each session.
        
        Signature ``GetComponentParameter(attribueName)`` 
        
        :param attribueName: 
        :type attribueName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Display.IrayPlusMaterialAttribute` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def GetComponentParameterValue(self, attribueName: str) -> str:
        """
        Gets attribute's value as string for specific fomatted attribute name 
        The string attribute name format should be : 
        "layer name-interface name-attribute name"
        
        Let material ''Varnished Cherry' for example:
        
        If user wants to get 'Base' component's value of 'Base-Colour-Colour'.  
        
        They should input 
        'Base-Colour-Colour' as componentName paramter.
        attribueValue parameter will return  the string for the value of 'Base-Colour-Colour': 
        "0.000000000000000,1.000000000000000,1.000000000000000"
        
        If user wants to get layer's sub attribute of 'ClearCoat'. They should use index in componentName paramter:
        'Layers-0-ReflectionColour-ColourOffset'
        
        attribueValue parameter will return the value of 'ClearCoat''s 'ReflectionColour-ColourOffset' as a string : 
        "1.000000000000000,0.000000000000000,0.000000000000000"
        
        NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
        session. 
        User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
        Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
        This is because the unique name for each layers would change between each session.
        
        Signature ``GetComponentParameterValue(attribueName)`` 
        
        :param attribueName: 
        :type attribueName: str 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def SetComponentParameter(self, attribueName: str, attribueObject: IrayPlusMaterialAttribute) -> 'list[str]':
        """
        Sets attribute object for specific fomatted attribute name 
        The string attribute name format should be : 
        "layer name-interface name-attribute name"
        
        Let material ''Varnished Cherry' for example:
        
        If user wants to set 'Base' component's attribueObject of 'Base-Colour-Colour'.  
        
        They should input 
        'Base-Colour-Colour' as attribueName paramter.
        The attribueObject point to the IrayPlusMatAttribute which should have modified value for Colour.
        
        If user wants to set layer's sub attribute of 'ClearCoat'. They should use index in attribueName paramter:
        'Layers-0-ReflectionColour-ColourOffset'
        The attribueObject point to the IrayPlusMatAttribute which should have modified value for ColourOffset.
        
        The changed_attrib parameter will return all the attributs names effected by current modification.
        then user could use this to figure out what should to requery.
        
        If user use 'Base-Base Type' to change base type to 'Metal'. Then all the attribute name in 'Base' will
        be listed in changed_attrib. Because the interface type change will cause the sub attributes been changed
        either.
        
        NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
        session. 
        User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
        Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
        This is because the unique name for each layers would change between each session.
        
        Signature ``SetComponentParameter(attribueName, attribueObject)`` 
        
        :param attribueName: 
        :type attribueName: str 
        :param attribueObject: 
        :type attribueObject: :py:class:`NXOpen.Display.IrayPlusMaterialAttribute` 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def SetComponentParameterValue(self, attribueName: str, attribueValue: str) -> 'list[str]':
        """
        Sets attribute value for specific fomatted attribute name 
        The string attribute name format should be : 
        "layer name-interface name-attribute name"
        
        Let material ''Varnished Cherry' for example:
        
        If user wants to set 'Base' component's value of 'Base-Colour-Colour'.  
        
        They should input 
        'Base-Colour-Colour' as attribueName paramter.
        attribueValue parameter will return  the string for the value of 'Base-Colour-Colour': 
        "0.000000000000000,1.000000000000000,1.000000000000000"
        
        If user wants to set layer's sub attribute value of 'ClearCoat'. They should use index in attribueName paramter:
        'Layers-0-ReflectionColour-ColourOffset'
        attribueValue parameter will return  the string for the value of 'ReflectionColour-ColourOffset' in 'ClearCoat': 
        "1.000000000000000,0.000000000000000,0.000000000000000"
        
        The changed_attrib parameter will return all the attributs names effected by current modification.
        then user could use this to figure out what should to requery.
        
        If user use 'Base-Base Type' to change base type to 'Metal'. Then all the attribute name in 'Base' will
        be listed in changed_attrib. Because the interface type change will cause the sub attributes been changed
        either.
        
        NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
        session. 
        User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
        Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
        This is because the unique name for each layers would change between each session.
        
        Signature ``SetComponentParameterValue(attribueName, attribueValue)`` 
        
        :param attribueName: 
        :type attribueName: str 
        :param attribueValue: 
        :type attribueValue: str 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def SaveToSystemStudioMaterials(self, saveXmlFileName: str) -> None:
        """
        Saves the material to System Studio Materials which is a directory under 
        ugphoto/IrayPlus_ug_canned_mattex.  
        
        Signature ``SaveToSystemStudioMaterials(saveXmlFileName)`` 
        
        :param saveXmlFileName: 
        :type saveXmlFileName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def ExportToXMLFile(self, exportXmlFileName: str) -> None:
        """
        Exports current material of material editor builder into a XML file.  
        
        Signature ``ExportToXMLFile(exportXmlFileName)`` 
        
        :param exportXmlFileName: 
        :type exportXmlFileName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def GetImageParameterFullPath(self, imageAttribueName: str) -> str:
        """
        To return the absolute path of specific image type parameter.  
        
        The format of imageAttribueName  should be : 
        "layer name-interface name-attribute name"
        
        Let material ''Varnished Cherry' for example:
        
        If user wants to get image's full path of 'Base-Colour-TextureSpace-Image'. User should input 
        'Base-Colour-TextureSpace-Image' as imageAttribueName paramter.
        imageFullPath parameter will return  the string of full path. 
        
        If user wants to get layer's sub attribute of 'ClearCoat'. They should use index in imageAttribueName paramter:
        'Layers-0-TextureSpace-Image'
        
        NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
        session. 
        User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
        Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
        This is because the unique name for each layers would change between each session.
        
        If the 
        
        Signature ``GetImageParameterFullPath(imageAttribueName)`` 
        
        :param imageAttribueName: 
        :type imageAttribueName: str 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    MaterialName: str = ...
    """
    Returns or sets  the current material name of material editor builder.  
    
    NOTE: the returned materialName should be freed via TEXT_free by caller.
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialName`` 
    
    :param materialName: 
    :type materialName: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    PreviewToggle: bool = ...
    """
    Returns or sets  a boolean value that indicate whether the preview toggle is ON.  
    
    If preview toggle is true. 
    then the preview image of the material will be generated.
    
    <hr>
    
    Getter Method
    
    Signature ``PreviewToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``PreviewToggle`` 
    
    :param toggleOn: 
    :type toggleOn: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    Null: IrayPlusMaterialEditorBuilder = ...  # unknown typename


class PointCloudClippingBoxesListItemBuilderClippingSidesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PointCloudClippingBoxesListItemBuilderClippingSides():
    """
    Specifies clipping side options used for defined clipping box. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", "inside"
       "Outside", "outside"
       "NotSet", "none"
    """
    Inside = 0  # PointCloudClippingBoxesListItemBuilderClippingSidesMemberType
    Outside = 1  # PointCloudClippingBoxesListItemBuilderClippingSidesMemberType
    NotSet = 2  # PointCloudClippingBoxesListItemBuilderClippingSidesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PointCloudClippingBoxesListItemBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilder` 
    to create clipping regions for :py:class:`NXOpen.Display.PointCloud`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Display.PointCloudBuilder.CreateClippingBoxesListItemBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    class ClippingSides():
        """
        Specifies clipping side options used for defined clipping box. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", "inside"
           "Outside", "outside"
           "NotSet", "none"
        """
        Inside = 0  # PointCloudClippingBoxesListItemBuilderClippingSidesMemberType
        Outside = 1  # PointCloudClippingBoxesListItemBuilderClippingSidesMemberType
        NotSet = 2  # PointCloudClippingBoxesListItemBuilderClippingSidesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    ClippingEndPoint: NXOpen.Point = ...
    """
    Returns or sets  the end point of the clipping box diagonal 
    
    <hr>
    
    Getter Method
    
    Signature ``ClippingEndPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ClippingEndPoint`` 
    
    :param clippingEndPoint: 
    :type clippingEndPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
    """
    ClippingSide: PointCloudClippingBoxesListItemBuilderClippingSides = ...
    """
    Returns or sets  the clipping side of the defined clipping box 
    
    <hr>
    
    Getter Method
    
    Signature ``ClippingSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilderClippingSides` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ClippingSide`` 
    
    :param clippingSide: 
    :type clippingSide: :py:class:`NXOpen.Display.PointCloudClippingBoxesListItemBuilderClippingSides` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
    """
    ClippingStartPoint: NXOpen.Point = ...
    """
    Returns or sets  the start point of the clipping box diagonal.  
    
    <hr>
    
    Getter Method
    
    Signature ``ClippingStartPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ClippingStartPoint`` 
    
    :param clippingStartPoint: 
    :type clippingStartPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_point_cloud_view ("NX Point Cloud Viewer")
    """
    Orientation: NXOpen.Matrix3x3 = ...
    """
    Returns  the orientation of clipping box 
    
    <hr>
    
    Getter Method
    
    Signature ``Orientation`` 
    
    :returns:  Box orientation  
    :rtype: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: PointCloudClippingBoxesListItemBuilder = ...  # unknown typename


class RasterImage(ImageBase):
    """
    Represents a :py:class:`NXOpen.Display.RasterImage` that provides 
    placing an imported image onto a plane (with controls for orientation, 
    sizing, and display) to use as a reference in the model to create geometry.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Display.RasterImageBuilder`
    
    .. versionadded:: NX9.0.0
    """
    Null: RasterImage = ...  # unknown typename


class Lighting(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.Lighting`
    Lights are used to illuminate the scene in Shaded and Studio rendering
    styles, as well as in High Quality Images.  
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateLighting`
    
    .. versionadded:: NX5.0.0
    """
    
    def GetLightBuilderFromList(self, index: int) -> LightBuilder:
        """
        Returns a light builder, given by the index, in the array of lights assigned to the work view  
        
        Signature ``GetLightBuilderFromList(index)`` 
        
        :param index:  index to the array of light builders  
        :type index: int 
        :returns:  the light builder  
        :rtype: :py:class:`NXOpen.Display.LightBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLightBuilderInList(self, index: int, light: LightBuilder) -> None:
        """
        Sets a light builder in the array at the given index 
        
        Signature ``SetLightBuilderInList(index, light)`` 
        
        :param index:  index to the array of light builders  
        :type index: int 
        :param light:  the light builder  
        :type light: :py:class:`NXOpen.Display.LightBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNumLightBuilders(self) -> int:
        """
        Returns the total number of light builders in the given lighting list  
        
        Signature ``GetNumLightBuilders()`` 
        
        :returns:  total lights in the light builder array  
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Lighting = ...  # unknown typename


class ImageData(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.Display.ImageData` that stores the 
    contents of a previously imported image file in the part.  
    
    :py:meth:`Display.ImageBaseBuilder.GetImagesInPart` provides a
    list of names of the :py:class:`NXOpen.Display.ImageData` saved in the 
    part file.
    Use :py:meth:`Display.ImageBaseBuilder.SetImageFromPart` to set
    a :py:class:`NXOpen.Display.ImageData` object (by name) as the image used
    by the builder.
    
    ImageData objects are not supported in KF.
    
    .. versionadded:: NX9.0.0
    """
    Null: ImageData = ...  # unknown typename


class IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IrayPlusSimpleMaterialEditorBuilderTextureSpace():
    """
    texture spacee type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Box", " - "
       "Planar", " - "
       "Cylindrical", " - "
       "Spherical", " - "
       "UVMap", " - "
    """
    Box = 0  # IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType
    Planar = 1  # IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType
    Cylindrical = 2  # IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType
    Spherical = 3  # IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType
    UVMap = 4  # IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IrayPlusSimpleMaterialEditorBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.IrayPlusSimpleMaterialEditorBuilder` 
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    .. versionadded:: NX10.0.2
    """
    
    class TextureSpace():
        """
        texture spacee type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Box", " - "
           "Planar", " - "
           "Cylindrical", " - "
           "Spherical", " - "
           "UVMap", " - "
        """
        Box = 0  # IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType
        Planar = 1  # IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType
        Cylindrical = 2  # IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType
        Spherical = 3  # IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType
        UVMap = 4  # IrayPlusSimpleMaterialEditorBuilderTextureSpaceMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetColorPicker(self) -> 'list[float]':
        """
        Returns the color picker  
        
        Signature ``GetColorPicker()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX10.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def SetColorPicker(self, colorPicker: 'list[float]') -> None:
        """
        Sets the color picker 
        
        Signature ``SetColorPicker(colorPicker)`` 
        
        :param colorPicker:  Array of 3 RGB values, each between 0 and 1  
        :type colorPicker: list of float 
        
        .. versionadded:: NX10.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def SaveMaterialsButton(self) -> None:
        """
        To save to System Studio Materials 
        
        Signature ``SaveMaterialsButton()`` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    
    def ExportXMLButton(self) -> None:
        """
        To export to a XML file 
        
        Signature ``ExportXMLButton()`` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: studio_render ("UG STUDIO RENDER")
        """
        ...
    
    AspectRatio: float = ...
    """
    Returns or sets  the aspect ratio 
    
    <hr>
    
    Getter Method
    
    Signature ``AspectRatio`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``AspectRatio`` 
    
    :param aspectRatio: 
    :type aspectRatio: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    FileBrowser: str = ...
    """
    Returns or sets  the file browser 
    
    <hr>
    
    Getter Method
    
    Signature ``FileBrowser`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``FileBrowser`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    LatitudeScale: float = ...
    """
    Returns or sets  the latitude scale 
    
    <hr>
    
    Getter Method
    
    Signature ``LatitudeScale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``LatitudeScale`` 
    
    :param latitudeScale: 
    :type latitudeScale: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    LongitudeScale: float = ...
    """
    Returns or sets  the longitude scale 
    
    <hr>
    
    Getter Method
    
    Signature ``LongitudeScale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``LongitudeScale`` 
    
    :param longitudeScale: 
    :type longitudeScale: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    NameString: str = ...
    """
    Returns or sets  the name string 
    
    <hr>
    
    Getter Method
    
    Signature ``NameString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``NameString`` 
    
    :param nameString: 
    :type nameString: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    NormalVector: NXOpen.Direction = ...
    """
    Returns or sets  the normal vector 
    
    <hr>
    
    Getter Method
    
    Signature ``NormalVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``NormalVector`` 
    
    :param normalVector: 
    :type normalVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    Scale: float = ...
    """
    Returns or sets  the scale 
    
    <hr>
    
    Getter Method
    
    Signature ``Scale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``Scale`` 
    
    :param scale: 
    :type scale: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    TextureSpaceEnum: IrayPlusSimpleMaterialEditorBuilderTextureSpace = ...
    """
    Returns or sets  the texture space enum 
    
    <hr>
    
    Getter Method
    
    Signature ``TextureSpaceEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.IrayPlusSimpleMaterialEditorBuilderTextureSpace` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``TextureSpaceEnum`` 
    
    :param textureSpaceEnum: 
    :type textureSpaceEnum: :py:class:`NXOpen.Display.IrayPlusSimpleMaterialEditorBuilderTextureSpace` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    TexturedToggle: bool = ...
    """
    Returns or sets  the textured toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``TexturedToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``TexturedToggle`` 
    
    :param texturedToggle: 
    :type texturedToggle: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    UScale: float = ...
    """
    Returns or sets  the u scale 
    
    <hr>
    
    Getter Method
    
    Signature ``UScale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``UScale`` 
    
    :param uScale: 
    :type uScale: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    UpVector: NXOpen.Direction = ...
    """
    Returns or sets  the up vector 
    
    <hr>
    
    Getter Method
    
    Signature ``UpVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``UpVector`` 
    
    :param upVector: 
    :type upVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    VScale: float = ...
    """
    Returns or sets  the v scale 
    
    <hr>
    
    Getter Method
    
    Signature ``VScale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    
    <hr>
    
    Setter Method
    
    Signature ``VScale`` 
    
    :param vScale: 
    :type vScale: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: studio_render ("UG STUDIO RENDER")
    """
    Null: IrayPlusSimpleMaterialEditorBuilder = ...  # unknown typename


class ImageDataCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Display.ImageData` 
    objects.  
    
    The :py:class:`NXOpen.Display.ImageDataCollection` also provides
    an iterator that iterates through all the :py:class:`NXOpen.Display.ImageData`
    objects in the part.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX9.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> ImageData:
        """
        Finds the :py:class:`NXOpen.Display.ImageData` with the given identifier  
        as recorded in a journal.  
        
        An object may not return the same value as 
        its JournalIdentifier in different versions of the software. However  
        newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In 
        general,this method should not be used in handwritten code and exists 
        to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given 
        journal identifier. 
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  Image data found  
        :rtype: :py:class:`NXOpen.Display.ImageData` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    


class LayerSettingsBuilderLayerOptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LayerSettingsBuilderLayerOptionType():
    """
    Specifies the layer options.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Maintain", "Maintain layer"
       "Original", "Original layer"
       "Work", "Work layer"
       "UserDefined", "User specified layer"
    """
    Maintain = 0  # LayerSettingsBuilderLayerOptionTypeMemberType
    Original = 1  # LayerSettingsBuilderLayerOptionTypeMemberType
    Work = 2  # LayerSettingsBuilderLayerOptionTypeMemberType
    UserDefined = 3  # LayerSettingsBuilderLayerOptionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LayerSettingsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a builder for object layer settings.  
    
    .. versionadded:: NX9.0.0
    """
    
    class LayerOptionType():
        """
        Specifies the layer options.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Maintain", "Maintain layer"
           "Original", "Original layer"
           "Work", "Work layer"
           "UserDefined", "User specified layer"
        """
        Maintain = 0  # LayerSettingsBuilderLayerOptionTypeMemberType
        Original = 1  # LayerSettingsBuilderLayerOptionTypeMemberType
        Work = 2  # LayerSettingsBuilderLayerOptionTypeMemberType
        UserDefined = 3  # LayerSettingsBuilderLayerOptionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def IsValidLayerOption(self, layerOption: LayerSettingsBuilderLayerOptionType) -> bool:
        """
        Determines if the layer option is supported.  
        
        The parent builder determines the validity of the layer options.
        For example, following layer options are not relevant when the layer
        is not being derived from another displayable object.
        
          * :py:class:`Display.LayerSettingsBuilderLayerOptionType.Maintain <Display.LayerSettingsBuilderLayerOptionType>`
          * :py:class:`Display.LayerSettingsBuilderLayerOptionType.Original <Display.LayerSettingsBuilderLayerOptionType>`
        
        Signature ``IsValidLayerOption(layerOption)`` 
        
        :param layerOption: 
        :type layerOption: :py:class:`NXOpen.Display.LayerSettingsBuilderLayerOptionType` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
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
    
    Layer: int = ...
    """
    Returns or sets  the layer.  
    
    Used when the layer option is set to
    :py:class:`Display.LayerSettingsBuilderLayerOptionType.UserDefined
    <Display.LayerSettingsBuilderLayerOptionType>`. See :py:class:`NXOpen.Layer.Constants` for 
    valid layer values.
    
    <hr>
    
    Getter Method
    
    Signature ``Layer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Layer`` 
    
    :param layer: 
    :type layer: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LayerOption: LayerSettingsBuilderLayerOptionType = ...
    """
    Returns or sets  the layer option.  
    
    Note that all layer options may not be supported by the builder.
    Refer :py:meth:`Display.LayerSettingsBuilder.IsValidLayerOption` to determine supported options.
    
    <hr>
    
    Getter Method
    
    Signature ``LayerOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.LayerSettingsBuilderLayerOptionType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayerOption`` 
    
    :param layerOption: 
    :type layerOption: :py:class:`NXOpen.Display.LayerSettingsBuilderLayerOptionType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: LayerSettingsBuilder = ...  # unknown typename


class ImageBasedLightingImagesTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageBasedLightingImagesType():
    """
    images type - environment used for generating image-based lighting 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Background", "Use the background image."
       "Stage", "Use the stage."
       "UserDefined", "Use the image file specified."
       "LightingOnly", "only used for IBL"
    """
    Background = 0  # ImageBasedLightingImagesTypeMemberType
    Stage = 1  # ImageBasedLightingImagesTypeMemberType
    UserDefined = 2  # ImageBasedLightingImagesTypeMemberType
    LightingOnly = 3  # ImageBasedLightingImagesTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageBasedLightingShadowsTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageBasedLightingShadowsType():
    """
    shadow type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No shadows will be produced."
       "SoftEdged", "Soft-edged,approximated shadows will be generated using a shadow mapping algorithm."
       "HardEdged", "Hard-edged, precise shadows will be generated using a ray-tracing algorithm."
       "TranslucentHard", "Hard-edged, precise shadows will be generated using a ray-tracing algorithm. Shadows from translucent objects will also be generated and their color will be determined by the transparent object's color."
    """
    NotSet = 0  # ImageBasedLightingShadowsTypeMemberType
    SoftEdged = 1  # ImageBasedLightingShadowsTypeMemberType
    HardEdged = 2  # ImageBasedLightingShadowsTypeMemberType
    TranslucentHard = 3  # ImageBasedLightingShadowsTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageBasedLightingImageBlurTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageBasedLightingImageBlurType():
    """
    lighting image blurr type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Low", " - "
       "Medium", " - "
       "High", " - "
    """
    NotSet = 0  # ImageBasedLightingImageBlurTypeMemberType
    Low = 1  # ImageBasedLightingImageBlurTypeMemberType
    Medium = 2  # ImageBasedLightingImageBlurTypeMemberType
    High = 3  # ImageBasedLightingImageBlurTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageBasedLightingImageUpVectorTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageBasedLightingImageUpVectorTypes():
    """
    up vector type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AlignWithFloorPlane", " - "
       "UserDefined", " - "
    """
    AlignWithFloorPlane = 0  # ImageBasedLightingImageUpVectorTypesMemberType
    UserDefined = 1  # ImageBasedLightingImageUpVectorTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageBasedLighting(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.ImageBasedLighting`
    Image-based Lighting (IBL) is only performed in High Quality Image 
    renderings.  
    
    IBL replaces the Lights in a scene with lighting effects 
    derived from a given image.
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateImageBasedLighting`
    
    .. versionadded:: NX5.0.0
    """
    
    class ImagesType():
        """
        images type - environment used for generating image-based lighting 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Background", "Use the background image."
           "Stage", "Use the stage."
           "UserDefined", "Use the image file specified."
           "LightingOnly", "only used for IBL"
        """
        Background = 0  # ImageBasedLightingImagesTypeMemberType
        Stage = 1  # ImageBasedLightingImagesTypeMemberType
        UserDefined = 2  # ImageBasedLightingImagesTypeMemberType
        LightingOnly = 3  # ImageBasedLightingImagesTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ShadowsType():
        """
        shadow type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No shadows will be produced."
           "SoftEdged", "Soft-edged,approximated shadows will be generated using a shadow mapping algorithm."
           "HardEdged", "Hard-edged, precise shadows will be generated using a ray-tracing algorithm."
           "TranslucentHard", "Hard-edged, precise shadows will be generated using a ray-tracing algorithm. Shadows from translucent objects will also be generated and their color will be determined by the transparent object's color."
        """
        NotSet = 0  # ImageBasedLightingShadowsTypeMemberType
        SoftEdged = 1  # ImageBasedLightingShadowsTypeMemberType
        HardEdged = 2  # ImageBasedLightingShadowsTypeMemberType
        TranslucentHard = 3  # ImageBasedLightingShadowsTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ImageBlurType():
        """
        lighting image blurr type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Low", " - "
           "Medium", " - "
           "High", " - "
        """
        NotSet = 0  # ImageBasedLightingImageBlurTypeMemberType
        Low = 1  # ImageBasedLightingImageBlurTypeMemberType
        Medium = 2  # ImageBasedLightingImageBlurTypeMemberType
        High = 3  # ImageBasedLightingImageBlurTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ImageUpVectorTypes():
        """
        up vector type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AlignWithFloorPlane", " - "
           "UserDefined", " - "
        """
        AlignWithFloorPlane = 0  # ImageBasedLightingImageUpVectorTypesMemberType
        UserDefined = 1  # ImageBasedLightingImageUpVectorTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CommitAndDisplay(self, view: NXOpen.View, updateDisplay: bool) -> None:
        """
        Saves the attributes and optionally updates the display of image-based lighting 
        
        Signature ``CommitAndDisplay(view, updateDisplay)`` 
        
        :param view:  View of the image-based lighting attributes  
        :type view: :py:class:`NXOpen.View` 
        :param updateDisplay:  True if the display should be updated  
        :type updateDisplay: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Accuracy: float = ...
    """
    Returns or sets  the accuracy of the lighting and shadows produced from the given image 
    
    <hr>
    
    Getter Method
    
    Signature ``Accuracy`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Accuracy`` 
    
    :param accuracy: 
    :type accuracy: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ColorSaturation: float = ...
    """
    Returns or sets  the image-based lighting color saturation 
    
    <hr>
    
    Getter Method
    
    Signature ``ColorSaturation`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColorSaturation`` 
    
    :param colorSaturation: 
    :type colorSaturation: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Image: Image = ...
    """
    Returns or sets  the image-based lighting's image builder 
    
    <hr>
    
    Getter Method
    
    Signature ``Image`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Image`` 
    
    :param imageBuilder: 
    :type imageBuilder: :py:class:`NXOpen.Display.Image` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ImageBlur: ImageBasedLightingImageBlurType = ...
    """
    Returns or sets  the blurr of the lighting image 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageBlur`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBasedLightingImageBlurType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageBlur`` 
    
    :param imageBlurr: 
    :type imageBlurr: :py:class:`NXOpen.Display.ImageBasedLightingImageBlurType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ImageFilename: str = ...
    """
    Returns or sets  the image filename used for image-based lighting 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageFilename`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageFilename`` 
    
    :param imageFileName: 
    :type imageFileName: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ImageRotation: float = ...
    """
    Returns or sets  the image rotation angle (in degrees) 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageRotation`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageRotation`` 
    
    :param imageRotation: 
    :type imageRotation: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ImageType: ImageBasedLightingImagesType = ...
    """
    Returns or sets  the image type 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBasedLightingImagesType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageType`` 
    
    :param imageType: 
    :type imageType: :py:class:`NXOpen.Display.ImageBasedLightingImagesType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ImageUpVector: NXOpen.Direction = ...
    """
    Returns or sets  the image up vector direction, relative to the absolute coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageUpVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageUpVector`` 
    
    :param imageUpVector: 
    :type imageUpVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ImageUpVectorType: ImageBasedLightingImageUpVectorTypes = ...
    """
    Returns or sets  the image up vector define 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageUpVectorType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBasedLightingImageUpVectorTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageUpVectorType`` 
    
    :param imageUpVector: 
    :type imageUpVector: :py:class:`NXOpen.Display.ImageBasedLightingImageUpVectorTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Intensity: float = ...
    """
    Returns or sets  the intensity of the image-based lighting light effects 
    
    <hr>
    
    Getter Method
    
    Signature ``Intensity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Intensity`` 
    
    :param intensity: 
    :type intensity: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    LwrtAngle: float = ...
    """
    Returns or sets  the angle of the lwrt image-based lighting light effects 
    
    <hr>
    
    Getter Method
    
    Signature ``LwrtAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LwrtAngle`` 
    
    :param lwrtAngle: 
    :type lwrtAngle: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    LwrtIntensity: float = ...
    """
    Returns or sets  the intensity of the lwrt image-based lighting light effects 
    
    <hr>
    
    Getter Method
    
    Signature ``LwrtIntensity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LwrtIntensity`` 
    
    :param lwrtIntensity: 
    :type lwrtIntensity: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    LwrtQuality: float = ...
    """
    Returns or sets  the quality of the lwrt image-based lighting light effects 1 to 7 
    
    <hr>
    
    Getter Method
    
    Signature ``LwrtQuality`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LwrtQuality`` 
    
    :param lwrtQuality: 
    :type lwrtQuality: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ShadowSoftness: float = ...
    """
    Returns or sets  the image-based lighting shadow softness 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadowSoftness`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadowSoftness`` 
    
    :param shadowSoftness: 
    :type shadowSoftness: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShadowType: ImageBasedLightingShadowsType = ...
    """
    Returns or sets  the shadow type 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadowType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.ImageBasedLightingShadowsType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadowType`` 
    
    :param shadowType: 
    :type shadowType: :py:class:`NXOpen.Display.ImageBasedLightingShadowsType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    UseImageBasedLighting: bool = ...
    """
    Returns or sets  whether image-based lighting (IBL) is enabled 
    
    <hr>
    
    Getter Method
    
    Signature ``UseImageBasedLighting`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseImageBasedLighting`` 
    
    :param useIBL: 
    :type useIBL: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    UseLightsForShadowCatcherInHqi: bool = ...
    """
    Returns or sets  whether high quality image generation (HQI) uses individual light sources or image-based lighting for shadow catcher 
    
    <hr>
    
    Getter Method
    
    Signature ``UseLightsForShadowCatcherInHqi`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseLightsForShadowCatcherInHqi`` 
    
    :param useLightsForShadowCatcherInHqi: 
    :type useLightsForShadowCatcherInHqi: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    UseLightsForShadowCatcherInLwrt: bool = ...
    """
    Returns or sets  whether Advanced Studio display (lwrt) uses individual light sources or image-based lighting for shadow catcher 
    
    <hr>
    
    Getter Method
    
    Signature ``UseLightsForShadowCatcherInLwrt`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseLightsForShadowCatcherInLwrt`` 
    
    :param useLightsForShadowCatcherInLwrt: 
    :type useLightsForShadowCatcherInLwrt: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    UseLwrtImageBasedLighting: bool = ...
    """
    Returns or sets  whether image-based lighting is enabled in Advanced Studio (lwrt) display 
    
    <hr>
    
    Getter Method
    
    Signature ``UseLwrtImageBasedLighting`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseLwrtImageBasedLighting`` 
    
    :param useLwrtIBL: 
    :type useLwrtIBL: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: ImageBasedLighting = ...  # unknown typename


class FacetSettingsBuilderShadedToleranceSettingMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetSettingsBuilderShadedToleranceSetting():
    """
    Specifies which set of tolerances are to be used for rendering facets
    for display for Shaded views. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Coarse", " - "
       "Standard", " - "
       "Fine", " - "
       "ExtraFine", " - "
       "UltraFine", " - "
       "UserDefined", " - "
    """
    Coarse = 0  # FacetSettingsBuilderShadedToleranceSettingMemberType
    Standard = 1  # FacetSettingsBuilderShadedToleranceSettingMemberType
    Fine = 2  # FacetSettingsBuilderShadedToleranceSettingMemberType
    ExtraFine = 3  # FacetSettingsBuilderShadedToleranceSettingMemberType
    UltraFine = 4  # FacetSettingsBuilderShadedToleranceSettingMemberType
    UserDefined = 5  # FacetSettingsBuilderShadedToleranceSettingMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetSettingsBuilderAdvVisToleranceSettingMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetSettingsBuilderAdvVisToleranceSetting():
    """
    Specifies which set of tolerances are to be used for rendering facets
    for display for Advanced Visualization views. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Coarse", " - "
       "Standard", " - "
       "Fine", " - "
       "ExtraFine", " - "
       "SuperFine", " - "
       "UltraFine", " - "
       "UserDefined", " - "
    """
    Coarse = 0  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
    Standard = 1  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
    Fine = 2  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
    ExtraFine = 3  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
    SuperFine = 4  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
    UltraFine = 5  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
    UserDefined = 6  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetSettingsBuilderFacetUpdateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetSettingsBuilderFacetUpdate():
    """
    Specifies whether an Update Display or Fit operation is to
    regenerate the facets for only visible objects, for all objects or
    for no objects. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "VisibleObjects", " - "
       "AllObjects", " - "
       "NotSet", " - "
    """
    VisibleObjects = 0  # FacetSettingsBuilderFacetUpdateMemberType
    AllObjects = 1  # FacetSettingsBuilderFacetUpdateMemberType
    NotSet = 2  # FacetSettingsBuilderFacetUpdateMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetSettingsBuilderFacetToViewRatioMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetSettingsBuilderFacetToViewRatio():
    """
    Specifies whether the ratio of the view scale to the scale used to
    generate facets is determined automatically by the system (as was
    always done before NX 8) or whether a ratio defined by the user
    (by one of the set_*FacetRatio methods) is to be used as the ratio.   
    
    .. deprecated::  NX9.0.0
       Refer to :py:class:`NXOpen.Display.FacetSettingsBuilderFacetScale` instead
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Automatic", " - "
       "UserDefined", " - "
    """
    Automatic = 0  # FacetSettingsBuilderFacetToViewRatioMemberType
    UserDefined = 1  # FacetSettingsBuilderFacetToViewRatioMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetSettingsBuilderFacetScaleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetSettingsBuilderFacetScale():
    """
    Denotes what type of scaling factor is applied to the corresponding tolerances used to generate facets. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fixed", "Adjusts tolerances by a constant value"
       "Part", "Adjusts tolerances by scale derived from bounding box of objects to facet in part"
       "View", "Adjusts tolerances by view scale"
    """
    Fixed = 0  # FacetSettingsBuilderFacetScaleMemberType
    Part = 1  # FacetSettingsBuilderFacetScaleMemberType
    View = 2  # FacetSettingsBuilderFacetScaleMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetSettingsBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.FacetSettingsBuilder`
    
    Facet Settings are not supported in KF.
    
    .. versionadded:: NX8.0.0
    """
    
    class ShadedToleranceSetting():
        """
        Specifies which set of tolerances are to be used for rendering facets
        for display for Shaded views. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Coarse", " - "
           "Standard", " - "
           "Fine", " - "
           "ExtraFine", " - "
           "UltraFine", " - "
           "UserDefined", " - "
        """
        Coarse = 0  # FacetSettingsBuilderShadedToleranceSettingMemberType
        Standard = 1  # FacetSettingsBuilderShadedToleranceSettingMemberType
        Fine = 2  # FacetSettingsBuilderShadedToleranceSettingMemberType
        ExtraFine = 3  # FacetSettingsBuilderShadedToleranceSettingMemberType
        UltraFine = 4  # FacetSettingsBuilderShadedToleranceSettingMemberType
        UserDefined = 5  # FacetSettingsBuilderShadedToleranceSettingMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class AdvVisToleranceSetting():
        """
        Specifies which set of tolerances are to be used for rendering facets
        for display for Advanced Visualization views. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Coarse", " - "
           "Standard", " - "
           "Fine", " - "
           "ExtraFine", " - "
           "SuperFine", " - "
           "UltraFine", " - "
           "UserDefined", " - "
        """
        Coarse = 0  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
        Standard = 1  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
        Fine = 2  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
        ExtraFine = 3  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
        SuperFine = 4  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
        UltraFine = 5  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
        UserDefined = 6  # FacetSettingsBuilderAdvVisToleranceSettingMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FacetUpdate():
        """
        Specifies whether an Update Display or Fit operation is to
        regenerate the facets for only visible objects, for all objects or
        for no objects. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "VisibleObjects", " - "
           "AllObjects", " - "
           "NotSet", " - "
        """
        VisibleObjects = 0  # FacetSettingsBuilderFacetUpdateMemberType
        AllObjects = 1  # FacetSettingsBuilderFacetUpdateMemberType
        NotSet = 2  # FacetSettingsBuilderFacetUpdateMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FacetToViewRatio():
        """
        Specifies whether the ratio of the view scale to the scale used to
        generate facets is determined automatically by the system (as was
        always done before NX 8) or whether a ratio defined by the user
        (by one of the set_*FacetRatio methods) is to be used as the ratio.   
        
        .. deprecated::  NX9.0.0
           Refer to :py:class:`NXOpen.Display.FacetSettingsBuilderFacetScale` instead
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Automatic", " - "
           "UserDefined", " - "
        """
        Automatic = 0  # FacetSettingsBuilderFacetToViewRatioMemberType
        UserDefined = 1  # FacetSettingsBuilderFacetToViewRatioMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FacetScale():
        """
        Denotes what type of scaling factor is applied to the corresponding tolerances used to generate facets. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Fixed", "Adjusts tolerances by a constant value"
           "Part", "Adjusts tolerances by scale derived from bounding box of objects to facet in part"
           "View", "Adjusts tolerances by view scale"
        """
        Fixed = 0  # FacetSettingsBuilderFacetScaleMemberType
        Part = 1  # FacetSettingsBuilderFacetScaleMemberType
        View = 2  # FacetSettingsBuilderFacetScaleMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetShadedEdgeTol(self, shadedTolerance: FacetSettingsBuilderShadedToleranceSetting) -> float:
        """
        Returns the edge tolerance for a given tolerance set for Shaded Views  
        
        Signature ``GetShadedEdgeTol(shadedTolerance)`` 
        
        :param shadedTolerance: 
        :type shadedTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderShadedToleranceSetting` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetShadedEdgeTol(self, shadedTolerance: FacetSettingsBuilderShadedToleranceSetting, shadedEdgeTol: float) -> None:
        """
        Sets the edge toleramce for a given tolerance set for Shaded Views 
        
        Signature ``SetShadedEdgeTol(shadedTolerance, shadedEdgeTol)`` 
        
        :param shadedTolerance: 
        :type shadedTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderShadedToleranceSetting` 
        :param shadedEdgeTol: 
        :type shadedEdgeTol: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetShadedFaceTol(self, shadedTolerance: FacetSettingsBuilderShadedToleranceSetting) -> float:
        """
        Returns the face tolerance for a given tolerance set for Shaded Views  
        
        Signature ``GetShadedFaceTol(shadedTolerance)`` 
        
        :param shadedTolerance: 
        :type shadedTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderShadedToleranceSetting` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetShadedFaceTol(self, shadedTolerance: FacetSettingsBuilderShadedToleranceSetting, shadedFaceTol: float) -> None:
        """
        Sets the face tolerance for a given tolerance set for Shaded Views 
        
        Signature ``SetShadedFaceTol(shadedTolerance, shadedFaceTol)`` 
        
        :param shadedTolerance: 
        :type shadedTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderShadedToleranceSetting` 
        :param shadedFaceTol: 
        :type shadedFaceTol: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetShadedAngleTol(self, shadedTolerance: FacetSettingsBuilderShadedToleranceSetting) -> float:
        """
        Returns the angle tolerance for a given tolerance set for Shaded Views  
        
        Signature ``GetShadedAngleTol(shadedTolerance)`` 
        
        :param shadedTolerance: 
        :type shadedTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderShadedToleranceSetting` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetShadedAngleTol(self, shadedTolerance: FacetSettingsBuilderShadedToleranceSetting, shadedAngleTol: float) -> None:
        """
        Sets the angle tolerance for a given tolerance set for Shaded Views 
        
        Signature ``SetShadedAngleTol(shadedTolerance, shadedAngleTol)`` 
        
        :param shadedTolerance: 
        :type shadedTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderShadedToleranceSetting` 
        :param shadedAngleTol: 
        :type shadedAngleTol: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAdvVisEdgeTol(self, advVisTolerance: FacetSettingsBuilderAdvVisToleranceSetting) -> float:
        """
        Returns the edge tolerance for a given tolerance set for Advanced Visualization Views  
        
        Signature ``GetAdvVisEdgeTol(advVisTolerance)`` 
        
        :param advVisTolerance: 
        :type advVisTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderAdvVisToleranceSetting` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAdvVisEdgeTol(self, advVisTolerance: FacetSettingsBuilderAdvVisToleranceSetting, advVisEdgeTol: float) -> None:
        """
        Sets the edge tolerance for a given tolerance set for Advanced Visualization Views 
        
        Signature ``SetAdvVisEdgeTol(advVisTolerance, advVisEdgeTol)`` 
        
        :param advVisTolerance: 
        :type advVisTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderAdvVisToleranceSetting` 
        :param advVisEdgeTol: 
        :type advVisEdgeTol: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAdvVisFaceTol(self, advVisTolerance: FacetSettingsBuilderAdvVisToleranceSetting) -> float:
        """
        Returns the face tolerance for a given tolerance set for Advanced Visualization Views  
        
        Signature ``GetAdvVisFaceTol(advVisTolerance)`` 
        
        :param advVisTolerance: 
        :type advVisTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderAdvVisToleranceSetting` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAdvVisFaceTol(self, advVisTolerance: FacetSettingsBuilderAdvVisToleranceSetting, advVisFaceTol: float) -> None:
        """
        Sets the face tolerance for a given tolerance set for Advanced Visualization Views 
        
        Signature ``SetAdvVisFaceTol(advVisTolerance, advVisFaceTol)`` 
        
        :param advVisTolerance: 
        :type advVisTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderAdvVisToleranceSetting` 
        :param advVisFaceTol: 
        :type advVisFaceTol: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAdvVisAngleTol(self, advVisTolerance: FacetSettingsBuilderAdvVisToleranceSetting) -> float:
        """
        Returns the angle tolerance for a given tolerance set for Advanced Visualization Views  
        
        Signature ``GetAdvVisAngleTol(advVisTolerance)`` 
        
        :param advVisTolerance: 
        :type advVisTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderAdvVisToleranceSetting` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAdvVisAngleTol(self, advVisTolerance: FacetSettingsBuilderAdvVisToleranceSetting, advVisAngleTol: float) -> None:
        """
        Sets the angle tolerance for a given tolerance set for Advanced Visualization Views 
        
        Signature ``SetAdvVisAngleTol(advVisTolerance, advVisAngleTol)`` 
        
        :param advVisTolerance: 
        :type advVisTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderAdvVisToleranceSetting` 
        :param advVisAngleTol: 
        :type advVisAngleTol: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAdvVisWidthTol(self, advVisTolerance: FacetSettingsBuilderAdvVisToleranceSetting) -> float:
        """
        Returns the width tolerance for a given tolerance set for Advanced Visualization Views  
        
        Signature ``GetAdvVisWidthTol(advVisTolerance)`` 
        
        :param advVisTolerance: 
        :type advVisTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderAdvVisToleranceSetting` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAdvVisWidthTol(self, advVisTolerance: FacetSettingsBuilderAdvVisToleranceSetting, advVisWidthTol: float) -> None:
        """
        Sets the width tolerance for a given tolerance set for Advanced Visualization Views 
        
        Signature ``SetAdvVisWidthTol(advVisTolerance, advVisWidthTol)`` 
        
        :param advVisTolerance: 
        :type advVisTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderAdvVisToleranceSetting` 
        :param advVisWidthTol: 
        :type advVisWidthTol: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    AdvVisAlignFacets: bool = ...
    """
    Returns or sets  the state of whether facets for advanced visualization views should be aligned along
    common edges.  
    
    Using this option will generally increase the quality of the facets
    but the facet generation will generally take longer.  
    
    <hr>
    
    Getter Method
    
    Signature ``AdvVisAlignFacets`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdvVisAlignFacets`` 
    
    :param advVisAlignFacets: 
    :type advVisAlignFacets: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    AdvVisFacetRatio: float = ...
    """
    Returns or sets  the facet ratio to use for Advanced Visualization Views 
    
    <hr>
    
    Getter Method
    
    Signature ``AdvVisFacetRatio`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX9.0.0
       Refer to :py:meth:`NXOpen.Display.FacetSettingsBuilder.AdvVisRefinementFactor` instead
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdvVisFacetRatio`` 
    
    :param advVisFacetRatio: 
    :type advVisFacetRatio: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX9.0.0
       Refer to :py:meth:`NXOpen.Display.FacetSettingsBuilder.AdvVisRefinementFactor` instead
    
    License requirements: None.
    """
    AdvVisFacetScale: FacetSettingsBuilderFacetScale = ...
    """
    Returns or sets  the facet scale to use for Advanced Visualization Views 
    
    <hr>
    
    Getter Method
    
    Signature ``AdvVisFacetScale`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetScale` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdvVisFacetScale`` 
    
    :param advVisFacetScale: 
    :type advVisFacetScale: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetScale` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    AdvVisFacetToViewRatio: FacetSettingsBuilderFacetToViewRatio = ...
    """
    Returns or sets  the facet to view ratio to use for Advanced Visualization Views 
    
    <hr>
    
    Getter Method
    
    Signature ``AdvVisFacetToViewRatio`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetToViewRatio` 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX9.0.0
       Refer to :py:meth:`NXOpen.Display.FacetSettingsBuilder.AdvVisFacetScale` instead
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdvVisFacetToViewRatio`` 
    
    :param advVisFacetToViewRatio: 
    :type advVisFacetToViewRatio: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetToViewRatio` 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX9.0.0
       Refer to :py:meth:`NXOpen.Display.FacetSettingsBuilder.AdvVisFacetScale` instead
    
    License requirements: None.
    """
    AdvVisRefinementFactor: float = ...
    """
    Returns or sets  the refinement factor to use for Advanced Visualization Views 
    
    <hr>
    
    Getter Method
    
    Signature ``AdvVisRefinementFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdvVisRefinementFactor`` 
    
    :param advVisRefinementFactor: 
    :type advVisRefinementFactor: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    AdvVisTolerance: FacetSettingsBuilderAdvVisToleranceSetting = ...
    """
    Returns or sets  the tolerance setting to use for Advanced Visualization Views 
    
    <hr>
    
    Getter Method
    
    Signature ``AdvVisTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.FacetSettingsBuilderAdvVisToleranceSetting` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdvVisTolerance`` 
    
    :param advVisTolerance: 
    :type advVisTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderAdvVisToleranceSetting` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    AdvVisUpdate: FacetSettingsBuilderFacetUpdate = ...
    """
    Returns or sets  the update mode to use for Advanced Visualization Views 
    
    <hr>
    
    Getter Method
    
    Signature ``AdvVisUpdate`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetUpdate` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdvVisUpdate`` 
    
    :param advVisUpdate: 
    :type advVisUpdate: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetUpdate` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ShadedAlignFacets: bool = ...
    """
    Returns or sets  the state of whether facets for shaded views should be aligned along
    common edges.  
    
    Using this option will generally increase the quality of the facets
    but the facet generation will generally take longer.  
    
    <hr>
    
    Getter Method
    
    Signature ``ShadedAlignFacets`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadedAlignFacets`` 
    
    :param shadedAlignFacets: 
    :type shadedAlignFacets: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShadedFacetRatio: float = ...
    """
    Returns or sets  the facet ratio to use for Shaded Views 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadedFacetRatio`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX9.0.0
       Refer to :py:meth:`NXOpen.Display.FacetSettingsBuilder.ShadedRefinementFactor` instead
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadedFacetRatio`` 
    
    :param shadedFacetRatio: 
    :type shadedFacetRatio: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX9.0.0
       Refer to :py:meth:`NXOpen.Display.FacetSettingsBuilder.ShadedRefinementFactor` instead
    
    License requirements: None.
    """
    ShadedFacetScale: FacetSettingsBuilderFacetScale = ...
    """
    Returns or sets  the facet scale to use for Shaded Views 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadedFacetScale`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetScale` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadedFacetScale`` 
    
    :param shadedFacetScale: 
    :type shadedFacetScale: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetScale` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShadedFacetToViewRatio: FacetSettingsBuilderFacetToViewRatio = ...
    """
    Returns or sets  the facet to view ratio to use for Shaded Views 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadedFacetToViewRatio`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetToViewRatio` 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX9.0.0
       Refer to :py:meth:`NXOpen.Display.FacetSettingsBuilder.ShadedFacetScale` instead
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadedFacetToViewRatio`` 
    
    :param shadedFacetToViewRatio: 
    :type shadedFacetToViewRatio: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetToViewRatio` 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX9.0.0
       Refer to :py:meth:`NXOpen.Display.FacetSettingsBuilder.ShadedFacetScale` instead
    
    License requirements: None.
    """
    ShadedRefinementFactor: float = ...
    """
    Returns or sets  the refinement factor to use for Shaded Views 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadedRefinementFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadedRefinementFactor`` 
    
    :param shadedRefinementFactor: 
    :type shadedRefinementFactor: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShadedTolerance: FacetSettingsBuilderShadedToleranceSetting = ...
    """
    Returns or sets  the tolerance setting to use for Shaded Views 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadedTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.FacetSettingsBuilderShadedToleranceSetting` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadedTolerance`` 
    
    :param shadedTolerance: 
    :type shadedTolerance: :py:class:`NXOpen.Display.FacetSettingsBuilderShadedToleranceSetting` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ShadedUpdate: FacetSettingsBuilderFacetUpdate = ...
    """
    Returns or sets  the update mode to use for Shaded Views 
    
    <hr>
    
    Getter Method
    
    Signature ``ShadedUpdate`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetUpdate` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShadedUpdate`` 
    
    :param shadedUpdate: 
    :type shadedUpdate: :py:class:`NXOpen.Display.FacetSettingsBuilderFacetUpdate` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ShowFacetEdges: bool = ...
    """
    Returns or sets  the state of whether facet edges should be shown for shaded solid and sheet bodies 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFacetEdges`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFacetEdges`` 
    
    :param showFacetEdges: 
    :type showFacetEdges: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: FacetSettingsBuilder = ...  # unknown typename


class Camera(NXOpen.NXObject):
    """
    Represents a camera   
    
    To obtain an instance of this class, use :py:class:`NXOpen.Display.CameraCollection`
    
    .. versionadded:: NX5.0.0
    """
    
    def ApplyToView(self, view: NXOpen.ModelingView) -> None:
        """
        Applies the parameters of a camera to a view 
        
        Signature ``ApplyToView(view)`` 
        
        :param view:  View to which the camera's                                                     parameters are to be applied.  
        :type view: :py:class:`NXOpen.ModelingView` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CopyToClipboard(self) -> None:
        """
        Copies the parameters of a camera to the operating system clipboard 
        
        Signature ``CopyToClipboard()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ListInformation(self) -> None:
        """
        Writes information about a camera to the listing device 
        
        Signature ``ListInformation()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Camera = ...  # unknown typename


class DatumPlaneGrid(BoundedGrid):
    """
    Represents a grid on a datum plane   
    
    Datum plane grids are not supported in KF.
    
    .. versionadded:: NX6.0.0
    """
    Null: DatumPlaneGrid = ...  # unknown typename


class GlobalIlluminationBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Display.GlobalIlluminationBuilder`.  
    
    Global Illumination provides simulation of real-world lighting using 
    image-based lighting.  Image-Based Lighting replaces the Lights in a 
    view with lighting effects derived from a given image.  Global
    Illumination Final Gather settings affect the Ray Traced Studio 
    photo-realistic display of the work view.
    
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ViewCollection.CreateGlobalIlluminationBuilder`
    
    .. versionadded:: NX9.0.0
    """
    IntensityDouble: float = ...
    """
    Returns or sets  the intensity control affects the brightness of the Ray Traced Studio lighting and depends on the global illumination image used 
    
    <hr>
    
    Getter Method
    
    Signature ``IntensityDouble`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IntensityDouble`` 
    
    :param intensityDouble: 
    :type intensityDouble: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    StaticFinalGatherQuality: float = ...
    """
    Returns or sets  the static final gather quality affects Ray Traced Studio static (still) image rendering 
    
    <hr>
    
    Getter Method
    
    Signature ``StaticFinalGatherQuality`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StaticFinalGatherQuality`` 
    
    :param staticFinalGatherQuality: 
    :type staticFinalGatherQuality: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    StationaryFinalGatherQuality: float = ...
    """
    Returns or sets  the stationary final gather quality affects Ray Traced Studio rendering when dynamic operations stop 
    
    <hr>
    
    Getter Method
    
    Signature ``StationaryFinalGatherQuality`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StationaryFinalGatherQuality`` 
    
    :param stationaryFinalGatherQuality: 
    :type stationaryFinalGatherQuality: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: GlobalIlluminationBuilder = ...  # unknown typename


class DynamicSectionBuilder(NXOpen.Builder):
    """
    Represents a Dynamic Section Builder used for creating sections.  
    
    The dynamic sectioning is performed on a displayable part that is
    displayed in the modeling work view.It is possible to specify the view 
    after creating the builder. However, the specified view must be
    modeling work view. This operation is meant to be performed in an 
    interactive mode with visual feedback.
    
    **Builder Creation:</b>
    
    The dynamic section builder can be used to create new dynamic
    section objects OR to edit an existing section object. 
    
    See :py:meth:`Display.DynamicSectionCollection.CreateSectionBuilder` 
    
    When a view is specified during the builder creation, the dynamic
    section object will be activated in the view. When the dynamic
    section object is activated in the view, view clipping and
    capping is enabled. However, it is not necessary to specify the
    view.
    
    There are three different types of sections that are currently
    being supported.
    
      * One Plane Section
      * Two Parallel Planes Section
      * Box Section
    
    User can switch between these types at any time.
    
    **Assembly and Modeling Operations</b>
    
      * Create section curves by intersecting all clipping planes  
    with all bodies in the scene
      * Create a datum plane from the active section plane.
      * Load components that are near or intersecting with the active
    section plane.
    
    All the APIs accept geometric data such as plane origin, plane normal
    in the absolute coordinate system.
    
    **Saving changes</b>
    
    :py:meth:`Builder.Commit` method will activate the section
    object in the modeling view. It returns the dynamic section object tag.
    
    **Section Plane Families:</b>
    
    An important issue with dynamic sectioning is the ability to easily 
    define a group of related cross-section planes. A group of related 
    cross-section planes will be known as a <tt>Plane Family</tt>. An 
    important idea in understanding a plane family is the concept of a 
    defining or a <tt>Base Plane</tt>. The base plane of the plane family 
    is the starting point (i.e. plane) for the plane family. All planes 
    in the family are related by an offset to the base plane. There are 
    two types of plane families: 
    
      * Linear 
      * Axi-Symmetric
    
    <tt>Linear Plane Family</tt>
    
    A linear plane family is defined by an infinite group of parallel 
    planes. All of the planes in a linear family are parallel to its 
    base plane (i.e. along the base plane normal at some linear offset 
    value). This is illustrated below with a base plane and three
    parallel planes to it that are members of the plane family.
    
    Base Plane
    
    |   |   |   | 
    |   |   |   | 
    |   |   |   | ==> Nomal to all planes.
    |   |   |   | 
    |   |   |   | 
    
    <tt>Axi-Symmetric Plane Family</tt>
    
    An axi-symmetric plane family is defined by rotating the base plane about 
    one of the three primary axes. There are an infinite number of planes in 
    an axi-symmetric plane family similar to a linear plane family. This is 
    illustrated below with a base plane and three planes rotated about the 
    z-axis.
    
    \   |   /
    \  |  / 
    \ | /   
    \|/____  Base Plane
    
    **Switching between plane families</b>
    
    Methods defining a new linear family
    
      * :py:meth:`Display.DynamicSectionBuilder.AlternatePlane`
      * :py:meth:`Display.DynamicSectionBuilder.PlaneX`
      * :py:meth:`Display.DynamicSectionBuilder.PlaneY`
      * :py:meth:`Display.DynamicSectionBuilder.PlaneZ`
      * :py:meth:`Display.DynamicSectionBuilder.SetNormal`
      * :py:meth:`Display.DynamicSectionBuilder.SetOffset`
      * :py:meth:`Display.DynamicSectionBuilder.SetOffsetByPoint`
      * :py:meth:`Display.DynamicSectionBuilder.SetOrigin`
      * :py:meth:`Display.DynamicSectionBuilder.SetPlane`
    
    Following methods define a new axi-symmetric family
    
      * :py:meth:`Display.DynamicSectionBuilder.SetRotationAngle`
      * :py:meth:`Display.DynamicSectionBuilder.SetRotationMatrix`       
    
    **Transition between plane families</b>
    
    When a method defining a new linear family is invoked, then if 
    
      * the current plane is in a linear family, it will stay in the family.
      * the current plane is in a axi-symmetric family, it becomes the base 
    plane of the linear family.
    
    The same thing happens when a method defining a new axi-symmetric plane           
    is invoked. 
    
    **Examples:</b>
    
    <tt>1. Linear Family</tt>
    
    Goal: User wants to create a series of sections along X axis.
    
    API sequence:
    
    planeX  - Create a plane with base plane at X = 0 
    See Display.DynamicSectionBuilder.PlaneX:py:meth:`Display.DynamicSectionBuilder.PlaneX`
    SetOffset( 50 ) - Plane at X = 50 
    SetOffset( 100 ) - Plane at X = 100 
    SetOffset( 0 ) - Plane at X = 0 
    
    <tt>2. Axi-symmetric Family</tt>
    
    Goal: User wants to create a series of sections by planes rotated 
    around X axis of the section plane.
    
    API sequence:
    
    SetRotation( X, 45 ) - The current plane becomes base plane. Then 
    the plane rotated around X axis by 45 
    degrees. 
    SetRotation( X, 90 ) - Plane rotated around X axis by 90 degrees. 
    SetRotation( X, 90 ) - Plane rotated around X axis by 0 degrees. 
    Back to original position.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Display.DynamicSectionCollection.CreateSectionBuilder`
    
    Default values.
    
    ==========================  =========
    Property                    Value
    ==========================  =========
    BoxExtentDelayUpdate        false 
    --------------------------  ---------
    CapColorOption              Any 
    --------------------------  ---------
    ClipType                    Section 
    --------------------------  ---------
    CurveColorOption            Any 
    --------------------------  ---------
    LayerSettings.LayerOption   Work 
    --------------------------  ---------
    LockPlanes                  true 
    --------------------------  ---------
    ShowCap                     true 
    --------------------------  ---------
    ShowClip                    true 
    --------------------------  ---------
    ShowCurves (deprecated)     false 
    --------------------------  ---------
    ShowGrid                    false 
    --------------------------  ---------
    ShowInterference            false 
    --------------------------  ---------
    ShowViewer                  false 
    --------------------------  ---------
    Type                        OnePlane 
    ==========================  =========
    
    .. versionadded:: NX5.0.0
    """
    
    def GetActivePlane(self) -> tuple:
        """
        Gets the active plane in the section.  
        
        *  See :py:meth:`Display.DynamicSectionBuilder.SetActivePlane` 
        *  for details.
        
        Signature ``GetActivePlane()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (planeAxis, activePlane). planeAxis is a :py:class:`NXOpen.Display.DynamicSectionTypesAxis`. activePlane is a :py:class:`NXOpen.Display.DynamicSectionTypesActivePlane`. 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetActivePlane(self, planeAxis: DynamicSectionTypesAxis, activePlane: DynamicSectionTypesActivePlane) -> None:
        """
        Sets the active plane in the section 
        
        Single Plane:
        
        :py:class:`Display.DynamicSectionTypesAxis.Z <Display.DynamicSectionTypesAxis>` is the
        active axis. There is no secondary plane. Only primary plane exists.
        
        Two Parallel Plane Section:
        
        :py:class:`Display.DynamicSectionTypesAxis.Z <Display.DynamicSectionTypesAxis>` is the 
        active axis and primary/secondary plane can be activated.
        
        Box Section:
        
        The active plane pair can be selected by specifying the planeAxis
        Given an axis, the primary/secondary planes can be activated.
        
        E.g. To activate primary plane along the local X axis use
        :py:class:`Display.DynamicSectionTypesAxis.X <Display.DynamicSectionTypesAxis>` and 
        :py:class:`Display.DynamicSectionTypesActivePlane.Primary <Display.DynamicSectionTypesActivePlane>`.
        
        Signature ``SetActivePlane(planeAxis, activePlane)`` 
        
        :param planeAxis: 
        :type planeAxis: :py:class:`NXOpen.Display.DynamicSectionTypesAxis` 
        :param activePlane: 
        :type activePlane: :py:class:`NXOpen.Display.DynamicSectionTypesActivePlane` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AlternatePlane(self) -> None:
        """
        Cycle through planes that are 90 degrees aligned to the current section plane.  
        
        For example, for a XY plane with normal along positive Z axis, invoking 
        this method will cycle through the planes in the following order.
        
        - YZ plane with normal along X axis
        - XZ plane with normal along Y axis
        - XY plane with normal along Z axis
        
        The section offset and rotation matrix are updated.                
        
        Signature ``AlternatePlane()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDatumPlane(self) -> NXOpen.DatumPlane:
        """
        Creates a datum plane from the active section plane.  
        
        Signature ``CreateDatumPlane()`` 
        
        :returns:  Datum plane  
        :rtype: :py:class:`NXOpen.DatumPlane` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EditView(self, view: NXOpen.ModelingView) -> None:
        """
        Edits the section object in the modeling view.  
        
        The view being edited must be the modeling view. This is provided
        to handle scenarios when the working view is changed when sectioning
        is in progress. It is the responsibility of user to save pending
        changes using :py:meth:`Builder.Commit` method. Otherwise,
        any existing changes will be lost.
        
        Signature ``EditView(view)`` 
        
        :param view:  Modeling view  
        :type view: :py:class:`NXOpen.ModelingView` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ShowCurvePreview(self, showCurvePreview: bool) -> None:
        """
        Show/hide curve preview.  
        
        When editing a view section, curve preview can be shown
        while the editing is in progress. The preview is removed once 
        the changes are committed on the builder or when the builder 
        is destroyed.      
        
        Hiding preview will remove the section series preview too.
        
        Signature ``ShowCurvePreview(showCurvePreview)`` 
        
        :param showCurvePreview: 
        :type showCurvePreview: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetGridSettings(self) -> PlaneGridBuilder:
        """
        Creates a grid settings builder from the active section plane.  
        
        Signature ``GetGridSettings()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Display.PlaneGridBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetName(self) -> str:
        """
        Gets the section name.  
        
        Caller is expected to free the memory.
        
        Signature ``GetName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetName(self, sectionName: str) -> bool:
        """
        Sets the section name.  
        
        The specified name will be validated. A section is expected to have a
        unique name in a part. The name may be modified to make it unique within
        the part.
        
        Signature ``SetName(sectionName)`` 
        
        :param sectionName:  Section name  
        :type sectionName: str 
        :returns:  If specified name was modified to 
        ensure uniqueness  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNormal(self) -> NXOpen.Vector3d:
        """
        Gets the normal of the section plane  
        
        Signature ``GetNormal()`` 
        
        :returns:  Section plane normal  
        :rtype: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNormal(self, normal: NXOpen.Vector3d) -> None:
        """
        Sets the normal of the section plane 
        
        Section offset and rotation matrix are updated.
        
        Signature ``SetNormal(normal)`` 
        
        :param normal:  Section plane normal  
        :type normal: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOffset(self) -> float:
        """
        Gets the the plane offset.  
        
        Signature ``GetOffset()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOffset(self, offset: float) -> None:
        """
        Sets the the plane offset.  
        
        When there are more than one
        clipping planes in the section, the active clipping plane will be 
        not be allowed to cross-over the non-active clipping plane.
        
        If :py:meth:`Display.DynamicSectionBuilder.LockPlanes``
        is off, section thickness is updated.
        
        Signature ``SetOffset(offset)`` 
        
        :param offset:  Offset  
        :type offset: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOffsetLimits(self) -> tuple:
        """
        Gets minimum and maximum offset limits.  
        
        Offset limits are dependent on the active section plane. They
        are determined based on the model bounding box and location
        of the active section plane. 
        
        :py:meth:`Display.DynamicSectionBuilder.SetOffset`
        can specify offset outside the offset limits. In that case the
        offset limits are extended to include the specified offset.  
        
        Signature ``GetOffsetLimits()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (minimumOffset, maximumOffset). minimumOffset is a float.   Minimum offset maximumOffset is a float.   Minimum offset 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOrigin(self) -> NXOpen.Point3d:
        """
        Gets the section origin.  
        
        Signature ``GetOrigin()`` 
        
        :returns:  Section origin  
        :rtype: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOrigin(self, origin: NXOpen.Point3d) -> None:
        """
        Sets the section origin.  
        
        The section is moved to new location. It obeys the lock flag
        :py:meth:`Display.DynamicSectionBuilder.LockPlanes``.
        if it is a multiple plane section.
        
        Section offset is updated.
        
        Signature ``SetOrigin(origin)`` 
        
        :param origin:  Section origin  
        :type origin: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OffsetOriginInPlane(self, xOffset: float, yOffset: float) -> None:
        """
        Offsets section origin within current section plane.  
        
        The section is moved to new location along in the section plane.
        The offsets are w.r.t. current origin along the X and Y
        axis of the section plane respectively.
        
        Signature ``OffsetOriginInPlane(xOffset, yOffset)`` 
        
        :param xOffset:  Delta X from the current position  
        :type xOffset: float 
        :param yOffset:  Delta Y from the current position  
        :type yOffset: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPlaneThickness(self) -> float:
        """
        Gets the thickness between active plane pair.  
        
        This is valid
        when the section contains more than one clipping plane. When the
        section planes are locked, setting thickness will not alter the 
        current thickness.
        
        Signature ``GetPlaneThickness()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPlaneThickness(self, planeThickness: float) -> None:
        """
        Sets the thickness between active plane pair.  
        
        This property is only available
        when the section contains more than one clipping plane. When the
        section planes are locked, setting thickness will not alter the 
        current thickness.
        
        Signature ``SetPlaneThickness(planeThickness)`` 
        
        :param planeThickness:  Active plane thickness  
        :type planeThickness: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRotationAngle(self, rotationAxis: DynamicSectionTypesAxis) -> float:
        """
        Gets rotation angle for specified axis.  
        
        Signature ``GetRotationAngle(rotationAxis)`` 
        
        :param rotationAxis: 
        :type rotationAxis: :py:class:`NXOpen.Display.DynamicSectionTypesAxis` 
        :returns:  Rotation angle in degrees  
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRotationAngle(self, rotationAxis: DynamicSectionTypesAxis, angle: float) -> None:
        """
        Rotates the section about specified axis by the specified angle.  
        
        If a rotation already exists about the specified axis, then 
        the section is rotated such that the total rotation angle is 
        set to the specified angle. Rotation about only one axis is 
        active at a time.
        
        1. Create plane with normal along Z.
        
        2. Display.DynamicSectionBuilder.SetRotationAngle:py:meth:`Display.DynamicSectionBuilder.SetRotationAngle`( X, 30 )
        Rotates plane around X axis by 30 degrees
        
        3. Display.DynamicSectionBuilder.SetRotationAngle:py:meth:`Display.DynamicSectionBuilder.SetRotationAngle`( X, 45 )
        Incremental rotation of 45 - 30 = 15 degrees.
        
        Section offset and rotation matrix are updated.
        
        Signature ``SetRotationAngle(rotationAxis, angle)`` 
        
        :param rotationAxis: 
        :type rotationAxis: :py:class:`NXOpen.Display.DynamicSectionTypesAxis` 
        :param angle:  Rotation angle in degrees  
        :type angle: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRotationMatrix(self) -> NXOpen.Matrix3x3:
        """
        Gets the section rotation matrix  
        
        Signature ``GetRotationMatrix()`` 
        
        :returns:  Rotation matrix  
        :rtype: :py:class:`NXOpen.Matrix3x3` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRotationMatrix(self, rotationAxis: DynamicSectionTypesAxis, rotationMatrix: NXOpen.Matrix3x3) -> None:
        """
        Sets the section rotation matrix
        
        Specify :py:class:`Display.DynamicSectionTypesAxis.None <Display.DynamicSectionTypesAxis>` 
        if the axis about which rotation was performed is not known.
        
        Section offset and rotation matrix are updated.
        
        Signature ``SetRotationMatrix(rotationAxis, rotationMatrix)`` 
        
        :param rotationAxis: 
        :type rotationAxis: :py:class:`NXOpen.Display.DynamicSectionTypesAxis` 
        :param rotationMatrix:  Rotation matrix  
        :type rotationMatrix: :py:class:`NXOpen.Matrix3x3` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def LoadAllIntersecting(self) -> tuple:
        """
        Loads all components that intersect the current section plane.  
        
        Errors
        are reported by the part load status. Caller is expected to destroy
        the memory used by load status object.
        
        Signature ``LoadAllIntersecting()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (componentsLoaded, loadStatus). componentsLoaded is a bool.   New component loaded flag loadStatus is a :py:class:`NXOpen.PartLoadStatus`.                  Errors occurred during loading of parts. 
        
        .. versionadded:: NX5.0.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    
    
    def LoadNearIntersecting(self) -> tuple:
        """
        Loads components that intersect the current section plane and are  
        near the section plane origin.  
        
        The distance used for which components 
        are "near" the section plane origin is determined internally. Errors 
        are reported by the part load status. Caller is expected to destroy 
        the memory used by load status object.
        
        Signature ``LoadNearIntersecting()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (componentsLoaded, loadStatus). componentsLoaded is a bool.   New component loaded flag loadStatus is a :py:class:`NXOpen.PartLoadStatus`.                  Errors occurred during loading of parts. 
        
        .. versionadded:: NX5.0.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    
    
    def PlaneX(self) -> None:
        """
        Creates a plane along X direction.  
        
        The plane is created with the base plane at the origin with normal 
        along X axis of the coordinate system 
        :py:meth:`Display.DynamicSectionBuilder.CsysType``.
        
        The location of the plane depends on the bounding box of all
        parts displayed in the view. The plane is positioned at the center
        of the bounding box.
        
        Section offset and rotation matrix are updated.
        
        Section thickness is recomputed based on the bounding box.
        
        Signature ``PlaneX()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PlaneY(self) -> None:
        """
        Creates a plane along Y direction.  
        
        The plane is created with the base plane at the origin with normal 
        along Y axis of the coordinate system 
        :py:meth:`Display.DynamicSectionBuilder.CsysType``.
        
        The location of the plane depends on the bounding box of all
        parts displayed in the view. The plane is positioned at the center
        of the bounding box.
        
        Section offset and rotation matrix are updated.
        
        Section thickness is recomputed based on the bounding box. 
        
        Signature ``PlaneY()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PlaneZ(self) -> None:
        """
        Creates a plane along Z direction.  
        
        The plane is created with the base plane at the origin with normal  
        along Z axis of the coordinate system 
        :py:meth:`Display.DynamicSectionBuilder.CsysType``.
        
        The location of the plane depends on the bounding box of all
        parts displayed in the view. The plane is positioned at the center
        of the bounding box.
        
        Section offset and rotation matrix are updated.
        
        Section thickness is recomputed based on the bounding box.     
        
        Signature ``PlaneZ()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RestoreView(self) -> None:
        """
        Restores the section to the saved section in the view database.  
        
        Signature ``RestoreView()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ReverseDirection(self) -> None:
        """
        Reverses the plane direction.  
        
        This will flip the side of the model
        being clipped.
        
        Section rotation matrix is updated.      
        
        Signature ``ReverseDirection()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveCurves(self, groupName: str) -> None:
        """
        Creates curves by intersecting all clipping planes of the section with 
        all visible bodies in the scene and adds them to the group created with the 
        specified name.  
        
        The group is displayed in the part navigator. If the 
        customer default "Load Solids/Sheets when Saving Section Curves" is 
        enabled, then this will load exact solid/sheet bodies for the visible 
        lightweight bodies intersecting the clipping planes. This may increase 
        the time and memory used by the operation, but will ensure exact 
        section curves.
        
        Signature ``SaveCurves(groupName)`` 
        
        :param groupName:  Name of the group containing curves  
        :type groupName: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsDefaultPlane(self) -> bool:
        """
        Indicates whether the section plane is at the default location.  
        
        Section plane is at the default location when builder creates
        a new section using default plane parameters (specified in the
        customer defaults) and/or when the section plane location is reset using
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.SetDefaultPlane`
        or :py:meth:`NXOpen.Display.DynamicSectionBuilder.SetDefaults`.
        Modifying section plane thereafter will reset the default plane
        state.
        
        Signature ``IsDefaultPlane()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultPlane(self) -> None:
        """
        Set current section plane to its default definition.  
        
        This will 
        only modify section plane geometry.
        
        Following properties affect the default section plane geometry.
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.DefaultPlaneAxis``
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.CsysType``
        
        Signature ``SetDefaultPlane()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaults(self) -> None:
        """
        Set current section to the default values.  
        
        This will modify
        all section geometry as well as section attributes.
        
        Following properties affect the default section plane geometry.
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.DefaultPlaneAxis``
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.CsysType``
        
        Signature ``SetDefaults()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOffsetByPoint(self, point: NXOpen.Point3d) -> None:
        """
        This method offsets the active clipping plane such that the plane 
        passes through the specified point.  
        
        When there are more than one
        clipping planes in the section, the active clipping plane will be 
        not be allowed to cross-over the non-active clipping plane.
        
        See :py:meth:`Display.DynamicSectionBuilder.SetOffset`
        
        Signature ``SetOffsetByPoint(point)`` 
        
        :param point:  Point in absolute coordinate system.  
        :type point: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPlane(self, axisOrigin: NXOpen.Point3d, origin: NXOpen.Point3d, rotationMatrix: NXOpen.Matrix3x3) -> None:
        """
        Sets a section plane to be the specified plane 
        The plane is created at the specified origin with the
        specified rotation matrix.  
        
        The axis origin can be same as
        the plane origin. To defind a linear plane family from the
        absolute origin, define axis origin as {0, 0, 0}. The section
        offset will reflect the distance of the plane from the
        axis origin.
        
        Section offset and rotation matrix are updated.
        
        Signature ``SetPlane(axisOrigin, origin, rotationMatrix)`` 
        
        :param axisOrigin:  Axis origin  
        :type axisOrigin: :py:class:`NXOpen.Point3d` 
        :param origin:  Plane origin.  
        :type origin: :py:class:`NXOpen.Point3d` 
        :param rotationMatrix:  Rotation matrix  
        :type rotationMatrix: :py:class:`NXOpen.Matrix3x3` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAssociativePlane(self, planeTag: NXOpen.Plane) -> None:
        """
        Makes dynamic section associative to the specified plane
        The plane must be a smart plane; otherwise an error will be reported.  
        
        Associative plane can be specified only if the builder supports associativity 
        (see :py:meth:`Display.DynamicSectionBuilder.IsAssociativitySupported`).            
        
        Signature ``SetAssociativePlane(planeTag)`` 
        
        :param planeTag:  Plane  
        :type planeTag: :py:class:`NXOpen.Plane` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsAssociativitySupported(self) -> bool:
        """
        Determines if an associative section plane is supported.  
        
        Signature ``IsAssociativitySupported()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ShowSectionCurves(self, showCurves: bool) -> None:
        """
        Shows the section curves in the view associated with the builder.  
        
        If no view is associated with the builder, then the curves are 
        Shown in the current work view.
        
        Signature ``ShowSectionCurves(showCurves)`` 
        
        :param showCurves: 
        :type showCurves: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def UpdateBoxExtents(self) -> None:
        """
        Update box section display by recomputing the box extents if necessary.  
        
        Use :py:meth:`Display.DynamicSectionBuilder.BoxExtentSupported`
        to determine if extent construction is supported before querying or
        setting extent attributes.
        
        Signature ``UpdateBoxExtents()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllPlanesGeometry(self) -> tuple:
        """
        Gets geometry for all planes of the section.  
        
        Numnber of planes depends on :py:meth:`NXOpen.Display.DynamicSectionBuilder.Type``. 
        Z direction of the plane matrix is the plane normal.
        
        Signature ``GetAllPlanesGeometry()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (planeOrigins, planeMetrices). planeOrigins is a list of :py:class:`NXOpen.Point3d`. planeMetrices is a list of :py:class:`NXOpen.Matrix3x3`. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPlaneGeometry(self, axisType: DynamicSectionTypesAxis, planeType: DynamicSectionTypesActivePlane) -> tuple:
        """
        Gets geometry of specified plane of the section.  
        
        Valid values for section axis and active plane depends on 
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.Type``. 
        See :py:meth:`NXOpen.Display.DynamicSectionBuilder.SetActivePlane` 
        for more details on how to specify axis and active plane type. Z direction
        of plane matrix is the plane normal.
        
        Signature ``GetPlaneGeometry(axisType, planeType)`` 
        
        :param axisType: 
        :type axisType: :py:class:`NXOpen.Display.DynamicSectionTypesAxis` 
        :param planeType: 
        :type planeType: :py:class:`NXOpen.Display.DynamicSectionTypesActivePlane` 
        :returns: a tuple 
        :rtype: A tuple consisting of (origin, matrix). origin is a :py:class:`NXOpen.Point3d`.   Plane origin matrix is a :py:class:`NXOpen.Matrix3x3`.   Plane matrix 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAllPlanesGeometry(self, planeOrigins: 'list[NXOpen.Point3d]', planeMetrices: 'list[NXOpen.Matrix3x3]') -> bool:
        """
        Sets geometry for all planes of the section.  
        
        Numnber of planes specified must be consistent with the current 
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.Type``.
        
        Signature ``SetAllPlanesGeometry(planeOrigins, planeMetrices)`` 
        
        :param planeOrigins: 
        :type planeOrigins: list of :py:class:`NXOpen.Point3d` 
        :param planeMetrices: 
        :type planeMetrices: list of :py:class:`NXOpen.Matrix3x3` 
        :returns:  Indicates if section geometry changed.  
        :rtype: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBoundingBox(self) -> tuple:
        """
        Gets bounding box used by the section.  
        
        The bounding box is used to compute offset limits (see
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.GetOffsetLimits`).
        
        It is possible that there is no valid bounding box associated with
        the section. The box is invalid if the X coordinate of min corner 
        point is larger than the X coordinate of max corner point.
        
        Signature ``GetBoundingBox()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (minCornerPt, maxCornerPt). minCornerPt is a :py:class:`NXOpen.Point3d`. maxCornerPt is a :py:class:`NXOpen.Point3d`. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBoundingBox(self, minCornerPt: NXOpen.Point3d, maxCornerPt: NXOpen.Point3d) -> None:
        """
        Sets bounding box for the section.  
        
        The bounding box is used to compute offset limits (see
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.GetOffsetLimits`).
        Specifying bounding box has no effect on current section geometry.
        
        The bounding box impacts construction of default section geometry.            
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.SetDefaultPlane`
        :py:meth:`NXOpen.Display.DynamicSectionBuilder.SetDefaults`
        
        Signature ``SetBoundingBox(minCornerPt, maxCornerPt)`` 
        
        :param minCornerPt: 
        :type minCornerPt: :py:class:`NXOpen.Point3d` 
        :param maxCornerPt: 
        :type maxCornerPt: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    BoxExtentDelayUpdate: bool = ...
    """
    Returns or sets  the delay box extent update.  
    
    This determines if the
    box section extent updates are delayed when selection list is modified
    (see :py:meth:`Display.DynamicSectionBuilder.BoxExtentObjects`).
    
    If true then use :py:meth:`Display.DynamicSectionBuilder.UpdateBoxExtents` 
    to update the box section. If false then update happens immediately.
    
    Use :py:meth:`Display.DynamicSectionBuilder.BoxExtentSupported`
    to determine if extent construction is supported before querying or
    setting extent attributes.
    
    <hr>
    
    Getter Method
    
    Signature ``BoxExtentDelayUpdate`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BoxExtentDelayUpdate`` 
    
    :param delayUpdate: 
    :type delayUpdate: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    BoxExtentMargin: float = ...
    """
    Returns or sets  the margin for box section extents 
    
    Use :py:meth:`Display.DynamicSectionBuilder.BoxExtentSupported`
    to determine if extent construction is supported before querying or
    setting extent attributes.
    
    <hr>
    
    Getter Method
    
    Signature ``BoxExtentMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BoxExtentMargin`` 
    
    :param margin: 
    :type margin: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    BoxExtentObjects: NXOpen.SelectINXObjectList = ...
    """
    Returns  the objects that define the extents for box section.  
    
    Absence of the object list indicates that the extent construction
    is not supported.
    
    <hr>
    
    Getter Method
    
    Signature ``BoxExtentObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectINXObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    BoxExtentSupported: bool = ...
    """
    Returns  the box extent support.  
    
    This is used to determine if the box extent construction is supported. Any
    box extent related APIs will not function when the extent construction
    is not supported.
    
    <hr>
    
    Getter Method
    
    Signature ``BoxExtentSupported`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    CapColor: NXOpen.NXColor = ...
    """
    Returns or sets  the cap color.  
    
    Used when cap color type is 
    :py:class:`Display.DynamicSectionTypesCapColorOption.Any <Display.DynamicSectionTypesCapColorOption>` 
    
    <hr>
    
    Getter Method
    
    Signature ``CapColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CapColor`` 
    
    :param capColor: 
    :type capColor: Id 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CapColorOption: DynamicSectionTypesCapColorOption = ...
    """
    Returns or sets  the cap color option 
    
    <hr>
    
    Getter Method
    
    Signature ``CapColorOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DynamicSectionTypesCapColorOption` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CapColorOption`` 
    
    :param capColorOption: 
    :type capColorOption: :py:class:`NXOpen.Display.DynamicSectionTypesCapColorOption` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ClipType: DynamicSectionTypesClip = ...
    """
    Returns or sets  the clip type 
    
    <hr>
    
    Getter Method
    
    Signature ``ClipType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DynamicSectionTypesClip` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ClipType`` 
    
    :param clipType: 
    :type clipType: :py:class:`NXOpen.Display.DynamicSectionTypesClip` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CsysType: DynamicSectionTypesCoordinateSystem = ...
    """
    Returns or sets  the coordinate system used for creating section plane along
    X, Y or Z principal planes.  
    
    Specifying the coordinate system has no 
    effect on the current section geometry.
    
    This is used in conjunction with
    :py:meth:`NXOpen.Display.DynamicSectionBuilder.DefaultPlaneAxis``
    to determine default plane constructed by following methods.
    :py:meth:`NXOpen.Display.DynamicSectionBuilder.SetDefaultPlane`
    :py:meth:`NXOpen.Display.DynamicSectionBuilder.SetDefaults`
    
    <hr>
    
    Getter Method
    
    Signature ``CsysType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DynamicSectionTypesCoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CsysType`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.Display.DynamicSectionTypesCoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CurveColor: NXOpen.NXColor = ...
    """
    Returns or sets  the curve color.  
    
    Used when the curve color option is set to
    :py:class:`Display.DynamicSectionTypesCurveColorOption.Any <Display.DynamicSectionTypesCurveColorOption>`.
    
    <hr>
    
    Getter Method
    
    Signature ``CurveColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurveColor`` 
    
    :param curveColor: 
    :type curveColor: Id 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CurveColorOption: DynamicSectionTypesCurveColorOption = ...
    """
    Returns or sets  the curve color option 
    
    <hr>
    
    Getter Method
    
    Signature ``CurveColorOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DynamicSectionTypesCurveColorOption` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurveColorOption`` 
    
    :param curveColorOption: 
    :type curveColorOption: :py:class:`NXOpen.Display.DynamicSectionTypesCurveColorOption` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    DefaultPlaneAxis: DynamicSectionTypesAxis = ...
    """
    Returns or sets  the axis indicating the default plane normal.  
    
    :py:class:`Display.DynamicSectionTypes.AxisNone` is 
    invalid. For example; specify 
    :py:class:`Display.DynamicSectionTypes.AxisZ` to use 
    XY plane as the default plane.
    Specifying the default plane has no effect on the current 
    section geometry.
    
    This is used in conjunction with
    :py:meth:`NXOpen.Display.DynamicSectionBuilder.CsysType``
    to determine default plane constructed by following methods.
    :py:meth:`NXOpen.Display.DynamicSectionBuilder.SetDefaultPlane`
    :py:meth:`NXOpen.Display.DynamicSectionBuilder.SetDefaults`
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultPlaneAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DynamicSectionTypesAxis` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultPlaneAxis`` 
    
    :param planeAxis: 
    :type planeAxis: :py:class:`NXOpen.Display.DynamicSectionTypesAxis` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    DeferCurveUpdate: bool = ...
    """
    Returns or sets  the defer curve update property.  
    
    This property can be used to reduce number of
    curve updates when performing a series of attribute changes on the dynamic
    section. After the changes are done, undefer the curve update. Undeferring
    will update the curves, if and only if, curve update is required based on
    the applied changes.
    
    <hr>
    
    Getter Method
    
    Signature ``DeferCurveUpdate`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DeferCurveUpdate`` 
    
    :param deferCurveUpdate: 
    :type deferCurveUpdate: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    InterferenceColor: NXOpen.NXColor = ...
    """
    Returns or sets  the interference color.  
    
    <hr>
    
    Getter Method
    
    Signature ``InterferenceColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterferenceColor`` 
    
    :param interferenceColor: 
    :type interferenceColor: Id 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    LayerSettings: LayerSettingsBuilder = ...
    """
    Returns  the layer settings builder 
    
    <hr>
    
    Getter Method
    
    Signature ``LayerSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.LayerSettingsBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LockPlanes: bool = ...
    """
    Returns or sets  the lock planes flag.  
    
    The planes can be locked in case of Two Parallel
    Planes and Box Section. When locked the planes will move together.
    
    <hr>
    
    Getter Method
    
    Signature ``LockPlanes`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LockPlanes`` 
    
    :param lockPlanes: 
    :type lockPlanes: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    NumberInSeries: int = ...
    """
    Returns or sets  the number of requested section planes in the current section series.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberInSeries`` 
    
    :returns:  Number of section requested  (>= 1). 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberInSeries`` 
    
    :param numberSectionsRequested:  Number of section requested (>= 1).  
    :type numberSectionsRequested: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ReverseSeries: bool = ...
    """
    Returns or sets  the reverse series flag 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseSeries`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseSeries`` 
    
    :param reverseSeries: 
    :type reverseSeries: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SeriesSpacing: float = ...
    """
    Returns or sets  the section plane spacing in the current section series.  
    
    <hr>
    
    Getter Method
    
    Signature ``SeriesSpacing`` 
    
    :returns:  Distance between sections (>= 0.02).  
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeriesSpacing`` 
    
    :param sectionSpacing:  Distance between sections (>= 0.02).  
    :type sectionSpacing: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowCap: bool = ...
    """
    Returns or sets  the cap on off flag 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowCap`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowCap`` 
    
    :param showCap: 
    :type showCap: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ShowClip: bool = ...
    """
    Returns or sets  the clip on off flag 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowClip`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowClip`` 
    
    :param showClip: 
    :type showClip: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ShowCurves: bool = ...
    """
    Returns or sets  the curve on off flag.  
    
    When the dynamic section object is visible in the view, the
    curves from the section object are shown in that view.            
    
    <hr>
    
    Getter Method
    
    Signature ``ShowCurves`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX6.0.0
       Use :py:meth:`ModelingView.IsDynamicSectionVisible` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowCurves`` 
    
    :param showCurves: 
    :type showCurves: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX6.0.0
       Use :py:meth:`ModelingView.SetDynamicSectionVisible` instead.
    
    License requirements: None.
    """
    ShowGrid: bool = ...
    """
    Returns or sets  the show grid display flag 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowGrid`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowGrid`` 
    
    :param showGrid: 
    :type showGrid: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowInterference: bool = ...
    """
    Returns or sets  the interference on off flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``ShowInterference`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowInterference`` 
    
    :param showInterference: 
    :type showInterference: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ShowViewer: bool = ...
    """
    Returns or sets  the 2D viewer display flag 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowViewer`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowViewer`` 
    
    :param showViewer: 
    :type showViewer: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Type: DynamicSectionTypesType = ...
    """
    Returns or sets  the section type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DynamicSectionTypesType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Display.DynamicSectionTypesType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    View: NXOpen.ModelingView = ...
    """
    Returns or sets  the modeling view in which section object edits are being done.  
    
    :py:meth:`Display.DynamicSectionBuilder.View` method is
    present for legacy reasons. 
    
    Use :py:meth:`Display.DynamicSectionBuilder.EditView` instead.
    
    <hr>
    
    Getter Method
    
    Signature ``View`` 
    
    :returns:  Modeling view  
    :rtype: :py:class:`NXOpen.ModelingView` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``View`` 
    
    :param view:  Modeling view  
    :type view: :py:class:`NXOpen.ModelingView` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: DynamicSectionBuilder = ...  # unknown typename


