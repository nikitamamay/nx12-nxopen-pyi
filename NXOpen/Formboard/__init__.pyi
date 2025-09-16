# module 'NXOpen.Formboard'
#
# Automatically generated 2025-06-09T14:38:46.680766
#
"""Default documentation for NXOpen.Formboard."""

import typing

import NXOpen
import NXOpen.Annotations
import NXOpen.Positioning
import NXOpen.Routing
import NXOpen.Routing.Electrical



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class LayoutLengthOptionsRoundingMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LayoutLengthOptionsRoundingMethod():
    """
    Methods of rounding lengths for Formboard geometry.  The rounding method determines
    the value of the length in the Formboard by modifying the original length
    values from the 3D harness part file. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Exact", "Lengths are unmodified."
       "Nearest", "Lengths are rounded up or down to the nearest increment value."
       "UpToNearest", "Lengths are rounded up to the nearest increment value."
       "DownToNearest", "Lengths are rounded down to the nearest increment value."
    """
    Exact = 0  # LayoutLengthOptionsRoundingMethodMemberType
    Nearest = 1  # LayoutLengthOptionsRoundingMethodMemberType
    UpToNearest = 2  # LayoutLengthOptionsRoundingMethodMemberType
    DownToNearest = 3  # LayoutLengthOptionsRoundingMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LayoutLengthOptions(NXOpen.Builder):
    """
    Defines the various options for determining the rounded lengths of 
    formboard geometry during the layout or update process.  
    
    Created automatically by containing classes.
    
    .. versionadded:: NX7.5.0
    """
    
    class RoundingMethod():
        """
        Methods of rounding lengths for Formboard geometry.  The rounding method determines
        the value of the length in the Formboard by modifying the original length
        values from the 3D harness part file. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Exact", "Lengths are unmodified."
           "Nearest", "Lengths are rounded up or down to the nearest increment value."
           "UpToNearest", "Lengths are rounded up to the nearest increment value."
           "DownToNearest", "Lengths are rounded down to the nearest increment value."
        """
        Exact = 0  # LayoutLengthOptionsRoundingMethodMemberType
        Nearest = 1  # LayoutLengthOptionsRoundingMethodMemberType
        UpToNearest = 2  # LayoutLengthOptionsRoundingMethodMemberType
        DownToNearest = 3  # LayoutLengthOptionsRoundingMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    NetlistLengthIncrement: NXOpen.Expression = ...
    """
    Returns  the connection list length increment.  
    
    Only used when the  
    :py:meth:`Formboard.LayoutLengthOptions.NetlistRoundingMethod`` 
    is :py:class:`Formboard.LayoutLengthOptionsRoundingMethod.UpToNearest <Formboard.LayoutLengthOptionsRoundingMethod>` or
    :py:class:`Formboard.LayoutLengthOptionsRoundingMethod.DownToNearest <Formboard.LayoutLengthOptionsRoundingMethod>`.
    
    <hr>
    
    Getter Method
    
    Signature ``NetlistLengthIncrement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    NetlistRoundingMethod: LayoutLengthOptionsRoundingMethod = ...
    """
    Returns or sets  the rounding method to apply to Connection List lengths.  
    
    <hr>
    
    Getter Method
    
    Signature ``NetlistRoundingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.LayoutLengthOptionsRoundingMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``NetlistRoundingMethod`` 
    
    :param netlistRoundingMethod: 
    :type netlistRoundingMethod: :py:class:`NXOpen.Formboard.LayoutLengthOptionsRoundingMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    OverstockLengthIncrement: NXOpen.Expression = ...
    """
    Returns  the overstock length increment.  
    
    Only used when the 
    :py:meth:`Formboard.LayoutLengthOptions.OverstockRoundingMethod`` 
    is :py:class:`Formboard.LayoutLengthOptionsRoundingMethod.UpToNearest <Formboard.LayoutLengthOptionsRoundingMethod>` or
    :py:class:`Formboard.LayoutLengthOptionsRoundingMethod.DownToNearest <Formboard.LayoutLengthOptionsRoundingMethod>`.
    
    <hr>
    
    Getter Method
    
    Signature ``OverstockLengthIncrement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    OverstockRoundingMethod: LayoutLengthOptionsRoundingMethod = ...
    """
    Returns or sets  the rounding method to apply to overstock wrapped lengths.  
    
    <hr>
    
    Getter Method
    
    Signature ``OverstockRoundingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.LayoutLengthOptionsRoundingMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``OverstockRoundingMethod`` 
    
    :param overstockRoundingMethod: 
    :type overstockRoundingMethod: :py:class:`NXOpen.Formboard.LayoutLengthOptionsRoundingMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    SegmentLengthIncrement: NXOpen.Expression = ...
    """
    Returns  the segment length increment.  
    
    Only used when the
    :py:meth:`Formboard.LayoutLengthOptions.SegmentRoundingMethod`` 
    is :py:class:`Formboard.LayoutLengthOptionsRoundingMethod.UpToNearest <Formboard.LayoutLengthOptionsRoundingMethod>` or
    :py:class:`Formboard.LayoutLengthOptionsRoundingMethod.DownToNearest <Formboard.LayoutLengthOptionsRoundingMethod>`.
    
    <hr>
    
    Getter Method
    
    Signature ``SegmentLengthIncrement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    SegmentRoundingMethod: LayoutLengthOptionsRoundingMethod = ...
    """
    Returns or sets  the rounding method to apply to segment lengths.  
    
    <hr>
    
    Getter Method
    
    Signature ``SegmentRoundingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.LayoutLengthOptionsRoundingMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``SegmentRoundingMethod`` 
    
    :param segmentRoundingMethod: 
    :type segmentRoundingMethod: :py:class:`NXOpen.Formboard.LayoutLengthOptionsRoundingMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Null: LayoutLengthOptions = ...  # unknown typename


class FaceAnnotationBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FaceAnnotationBuilderTypes():
    """
    Enum which defines the type to import CGM/Pattern file
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ComponentAttribute", "Import CGM file by selecting a component"
       "CgmFileSelection", "Import CGM file by browsing a CGM file"
       "PatternFileSelection", "Import a pattern file"
    """
    ComponentAttribute = 0  # FaceAnnotationBuilderTypesMemberType
    CgmFileSelection = 1  # FaceAnnotationBuilderTypesMemberType
    PatternFileSelection = 2  # FaceAnnotationBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FaceAnnotationBuilderDrwDestinationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FaceAnnotationBuilderDrwDestination():
    """
    Enum which defines where the geometry is to be placed. The geometry
    can be placed either in model or drawing sheet.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DrawingSheet", "Place geometry in drawing sheet"
       "Model", "Place geometry in model"
    """
    DrawingSheet = 0  # FaceAnnotationBuilderDrwDestinationMemberType
    Model = 1  # FaceAnnotationBuilderDrwDestinationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FaceAnnotationBuilder(NXOpen.Builder):
    """
    Builder for Face Annotation functionality used in formboard.  
    
    It allows 
    importing CGM or Pattern file geometry and placing it on a drawing sheet
    or model view. As a result of this a group of dumb geometry is placed such
    that defined origin is located at the lower left hand of the bounding box 
    containing the group of geometry.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Formboard.FormboardManager.CreateFaceAnnotationBuilder`
    
    Default values.
    
    =========  =============
    Property   Value
    =========  =============
    DestEnum   DrawingSheet 
    ---------  -------------
    TogBlank   0 
    =========  =============
    
    .. versionadded:: NX7.5.0
    """
    
    class Types():
        """
        Enum which defines the type to import CGM/Pattern file
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ComponentAttribute", "Import CGM file by selecting a component"
           "CgmFileSelection", "Import CGM file by browsing a CGM file"
           "PatternFileSelection", "Import a pattern file"
        """
        ComponentAttribute = 0  # FaceAnnotationBuilderTypesMemberType
        CgmFileSelection = 1  # FaceAnnotationBuilderTypesMemberType
        PatternFileSelection = 2  # FaceAnnotationBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DrwDestination():
        """
        Enum which defines where the geometry is to be placed. The geometry
        can be placed either in model or drawing sheet.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DrawingSheet", "Place geometry in drawing sheet"
           "Model", "Place geometry in model"
        """
        DrawingSheet = 0  # FaceAnnotationBuilderDrwDestinationMemberType
        Model = 1  # FaceAnnotationBuilderDrwDestinationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    CgmflBrsr: str = ...
    """
    Returns or sets  the browser which enables selection of CGM file when :py:class:`Formboard.FaceAnnotationBuilderTypes` is :py:class:`
    Formboard.FaceAnnotationBuilderTypes.CgmFileSelection  <
    Formboard.FaceAnnotationBuilderTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``CgmflBrsr`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``CgmflBrsr`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    CompSel: NXOpen.SelectNXObject = ...
    """
    Returns  the user selected component which has a CGM_FILE or PATTERN_FILE attribute defined.  
    
    <hr>
    
    Getter Method
    
    Signature ``CompSel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObject` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    DestEnum: FaceAnnotationBuilderDrwDestination = ...
    """
    Returns or sets  the :py:class:`NXOpen.Formboard.FaceAnnotationBuilderDrwDestination` selected by
    user to place the geometry 
    
    <hr>
    
    Getter Method
    
    Signature ``DestEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.FaceAnnotationBuilderDrwDestination` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``DestEnum`` 
    
    :param destEnum: 
    :type destEnum: :py:class:`NXOpen.Formboard.FaceAnnotationBuilderDrwDestination` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    PntOrigin: NXOpen.Point = ...
    """
    Returns or sets  the user selected point where geometry will be placed 
    
    <hr>
    
    Getter Method
    
    Signature ``PntOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``PntOrigin`` 
    
    :param pntOrigin: 
    :type pntOrigin: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    StrAnnot: str = ...
    """
    Returns or sets  the string to display the name of Pattern file name selected by user.  
    
    <hr>
    
    Getter Method
    
    Signature ``StrAnnot`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``StrAnnot`` 
    
    :param strAnnot: 
    :type strAnnot: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    StrAnnotFileName: str = ...
    """
    Returns or sets  the string to display the name of CGM name selected by user.  
    
    <hr>
    
    Getter Method
    
    Signature ``StrAnnotFileName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``StrAnnotFileName`` 
    
    :param strAnnot: 
    :type strAnnot: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    TogBlank: bool = ...
    """
    Returns or sets  the toggle which defines whether the selected component is to be blanked or not 
    
    <hr>
    
    Getter Method
    
    Signature ``TogBlank`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``TogBlank`` 
    
    :param togBlank: 
    :type togBlank: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Type: FaceAnnotationBuilderTypes = ...
    """
    Returns or sets  the :py:class:`NXOpen.Formboard.FaceAnnotationBuilderTypes`
    selected by user 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.FaceAnnotationBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Formboard.FaceAnnotationBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Null: FaceAnnotationBuilder = ...  # unknown typename


class ShapeSegmentBuilder(NXOpen.Builder):
    """
    Builder for Face Annotation functionality used in formboard.  
    
    It allows 
    importing CGM or Pattern file geometry and placing it on a drawing sheet
    or model view. As a result of this a group of dumb geometry is placed such
    that defined origin is located at the lower left hand of the bounding box 
    containing the group of geometry.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Formboard.FormboardManager.CreateShapeSegmentBuilder`
    
    .. versionadded:: NX7.5.0
    """
    
    def ChangeType(self, newType: int) -> None:
        """
        Signature ``ChangeType(newType)`` 
        
        :param newType: 
        :type newType: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def NewSegment(self, newSegment: NXOpen.Routing.ISegment) -> None:
        """
        Signature ``NewSegment(newSegment)`` 
        
        :param newSegment: 
        :type newSegment: :py:class:`NXOpen.Routing.ISegment` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def UpdateLineAngleVec(self, newDir: NXOpen.Vector3d) -> None:
        """
        Signature ``UpdateLineAngleVec(newDir)`` 
        
        :param newDir: 
        :type newDir: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def GetLineData(self) -> tuple:
        """
        Signature ``GetLineData()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (anchorSeg, anchorRcp, angle). anchorSeg is a :py:class:`NXOpen.Routing.ISegment`. anchorRcp is a :py:class:`NXOpen.Routing.ControlPoint`. angle is a float. 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateNewRadialBend(self, firstPivot: NXOpen.Point3d, firstBendMethod: int, firstBendValue: float, secondPivot: NXOpen.Point3d, secondBendMethod: int, secondBendValue: float) -> None:
        """
        Signature ``CreateNewRadialBend(firstPivot, firstBendMethod, firstBendValue, secondPivot, secondBendMethod, secondBendValue)`` 
        
        :param firstPivot: 
        :type firstPivot: :py:class:`NXOpen.Point3d` 
        :param firstBendMethod: 
        :type firstBendMethod: int 
        :param firstBendValue: 
        :type firstBendValue: float 
        :param secondPivot: 
        :type secondPivot: :py:class:`NXOpen.Point3d` 
        :param secondBendMethod: 
        :type secondBendMethod: int 
        :param secondBendValue: 
        :type secondBendValue: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def AddRadialPivot(self, pivotLocation: NXOpen.Point3d, bendMethod: int, bendValue: float) -> None:
        """
        Signature ``AddRadialPivot(pivotLocation, bendMethod, bendValue)`` 
        
        :param pivotLocation: 
        :type pivotLocation: :py:class:`NXOpen.Point3d` 
        :param bendMethod: 
        :type bendMethod: int 
        :param bendValue: 
        :type bendValue: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def RemoveRadialPivot(self, pivotIndex: int) -> None:
        """
        Signature ``RemoveRadialPivot(pivotIndex)`` 
        
        :param pivotIndex: 
        :type pivotIndex: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def UpdateRadialPivot(self, pivotIndex: int, newLocation: NXOpen.Point3d, newBendMethod: int, newBendValue: float) -> None:
        """
        Signature ``UpdateRadialPivot(pivotIndex, newLocation, newBendMethod, newBendValue)`` 
        
        :param pivotIndex: 
        :type pivotIndex: int 
        :param newLocation: 
        :type newLocation: :py:class:`NXOpen.Point3d` 
        :param newBendMethod: 
        :type newBendMethod: int 
        :param newBendValue: 
        :type newBendValue: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateNewSpline(self, anchorLocation: NXOpen.Point3d, firstPoint: NXOpen.Point3d, secondPoint: NXOpen.Point3d) -> None:
        """
        Signature ``CreateNewSpline(anchorLocation, firstPoint, secondPoint)`` 
        
        :param anchorLocation: 
        :type anchorLocation: :py:class:`NXOpen.Point3d` 
        :param firstPoint: 
        :type firstPoint: :py:class:`NXOpen.Point3d` 
        :param secondPoint: 
        :type secondPoint: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def RemoveSplinePoint(self, pointIndex: int) -> None:
        """
        Signature ``RemoveSplinePoint(pointIndex)`` 
        
        :param pointIndex: 
        :type pointIndex: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def AddSplinePoint(self, pointLocation: NXOpen.Point3d) -> int:
        """
        Adds a point to the existing spline.  
        
        Signature ``AddSplinePoint(pointLocation)`` 
        
        :param pointLocation: 
        :type pointLocation: :py:class:`NXOpen.Point3d` 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def UpdateSplinePoint(self, pointIndex: int, pointLocation: NXOpen.Point3d, inDrag: bool) -> None:
        """
        Signature ``UpdateSplinePoint(pointIndex, pointLocation, inDrag)`` 
        
        :param pointIndex: 
        :type pointIndex: int 
        :param pointLocation: 
        :type pointLocation: :py:class:`NXOpen.Point3d` 
        :param inDrag: 
        :type inDrag: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CommitCurrentOperation(self) -> None:
        """
        Signature ``CommitCurrentOperation()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def SwapAnchorEnd(self) -> None:
        """
        Signature ``SwapAnchorEnd()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def SetActiveView(self, view: NXOpen.TaggedObject) -> None:
        """
        Sets the active view for the shape operation.  
        
        Signature ``SetActiveView(view)`` 
        
        :param view: 
        :type view: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    Null: ShapeSegmentBuilder = ...  # unknown typename


class FormboardManager():
    """
    Contains information about flattened harness drawing and drafting data for
    harness manufacturing drawings (Formboard Drawings).  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX7.5.0
    """
    
    def IsFormboard(self) -> bool:
        """
        Returns whether or not the part containing this :py:class:`NXOpen.Formboard.FormboardManager` is
        actually a Formboard Drawing part file.  
        
        Signature ``IsFormboard()`` 
        
        :returns:  whether or not the part is a formboard.  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def StoreHarnessesToFlatten(self, harnesses: 'list[NXOpen.Routing.Electrical.HarnessDevice]') -> None:
        """
        Examines the input list of harnesses and stores information from the harnesses into the part containing
        this :py:class:`NXOpen.Formboard.FormboardManager`.  
        
        The harnesses must from a sub-component of
        this part.  The harnesses must form a fully-connected set of geometry.   This method does not actually
        flatten or copy the harness geometry. 
        
        Signature ``StoreHarnessesToFlatten(harnesses)`` 
        
        :param harnesses:  Harnesses to flatten into this part.  
        :type harnesses: list of :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def AddPartAs3dHarness(self, harnessPart: NXOpen.Part) -> None:
        """
        Sets the input part as the part containing the potential harnesses to flatten.  
        
        This method will add the input part as a new component of this assembly if there
        is not already an instance of the input part in the work part assembly.  This
        method is only necessary if the reference between the formboard and it's parent
        3D harness assembly has been removed.  
        
        Passing in None for the harness part will sever the link between
        the formboard and it's current 3D harness part file.
        
        Signature ``AddPartAs3dHarness(harnessPart)`` 
        
        :param harnessPart:  Part containing the harnesses to flatten into this part.  
        :type harnessPart: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateLayoutBuilder(self) -> FormboardLayoutBuilder:
        """
        Creates a :py:class:`NXOpen.Formboard.FormboardLayoutBuilder` that can flatten and layout
        new formboard geometry, or modify the layout of existing formboard geometry.  
        
        Signature ``CreateLayoutBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Formboard.FormboardLayoutBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateOrientBranchBuilder(self) -> OrientBranchBuilder:
        """
        Creates a :py:class:`NXOpen.Formboard.OrientBranchBuilder` object for rotating
        branches in formboard about Z axis.  
        
        Signature ``CreateOrientBranchBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Formboard.OrientBranchBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateFlipComponentBuilder(self) -> FlipComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Formboard.FlipComponentBuilder` object for
        flipping of formboard component about an axis orthogonal to Z axis to ensure that
        after flipping component lies in XY plane.  
        
        Signature ``CreateFlipComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Formboard.FlipComponentBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateShapeSegmentBuilder(self, segment: NXOpen.Routing.ISegment) -> ShapeSegmentBuilder:
        """
        Creates a :py:class:`NXOpen.Formboard.ShapeSegmentBuilder` that can shape formboard segments.  
        
        Signature ``CreateShapeSegmentBuilder(segment)`` 
        
        :param segment:  The routing segment to shape.  
        :type segment: :py:class:`NXOpen.Routing.ISegment` 
        :returns: 
        :rtype: :py:class:`NXOpen.Formboard.ShapeSegmentBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateFaceAnnotationBuilder(self) -> FaceAnnotationBuilder:
        """
        Creates a :py:class:`NXOpen.Formboard.FaceAnnotationBuilder` object for importing
        CGM or Pattern file geometry and placing it on a drawing sheet or model view.  
        
        Signature ``CreateFaceAnnotationBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Formboard.FaceAnnotationBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateObjectAttributeReferenceBuilder(self) -> ObjectAttributeReferenceBuilder:
        """
        Creates a :py:class:`NXOpen.Formboard.ObjectAttributeReferenceBuilder` that creates a tabular note
        object which reads values from the single object selected by the user.  
        
        It also creates leader for the
        annotation associated with the object selected by user.
        
        Signature ``CreateObjectAttributeReferenceBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Formboard.ObjectAttributeReferenceBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreatePathLengthAnnotationBuilder(self, annotation: NXOpen.Annotations.Annotation) -> PathLengthAnnotationBuilder:
        """
        Creates a :py:class:`NXOpen.Formboard.PathLengthAnnotationBuilder`  
        
        Signature ``CreatePathLengthAnnotationBuilder(annotation)`` 
        
        :param annotation:  The Formboard Path Length annotation.  
        
        :type annotation: :py:class:`NXOpen.Annotations.Annotation` 
        :returns: 
        :rtype: :py:class:`NXOpen.Formboard.PathLengthAnnotationBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateUpdateFormboardBuilder(self) -> UpdateFormboardBuilder:
        """
        Creates a :py:class:`NXOpen.Formboard.UpdateFormboardBuilder` that compares and
        updates formboard geometry to match a modified master 3D harness.  
        
        Signature ``CreateUpdateFormboardBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Formboard.UpdateFormboardBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def GetFmbdPlaneConstraints(self, fmbdPlane: NXOpen.NXObject) -> 'list[NXOpen.Positioning.ComponentConstraint]':
        """
        Gets :py:class:`NXOpen.Positioning.ComponentConstraint` which are associated to the formboard plane.  
        
        Signature ``GetFmbdPlaneConstraints(fmbdPlane)`` 
        
        :param fmbdPlane: 
        :type fmbdPlane: :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Positioning.ComponentConstraint` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def ShowFormboardConstraints(self) -> None:
        """
        Shows all of the hidden formboard constraints.  
        
        Signature ``ShowFormboardConstraints()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def HideFormboardConstraints(self) -> None:
        """
        Hides the formboard constraints.  
        
        Signature ``HideFormboardConstraints()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    


class FormboardLayoutBuilderMainRunTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FormboardLayoutBuilderMainRunType():
    """
    Selection method for the set of segments that define the main
    run of the formboard geometry. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Longest", "Path of longest wire."
       "Thickest", "Path of longest wire contained within the thickest bundle."
       "UserSelection", "Manual selection of path."
    """
    Longest = 0  # FormboardLayoutBuilderMainRunTypeMemberType
    Thickest = 1  # FormboardLayoutBuilderMainRunTypeMemberType
    UserSelection = 2  # FormboardLayoutBuilderMainRunTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FormboardLayoutBuilderBranchAngleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FormboardLayoutBuilderBranchAngle():
    """
    Methods for determining which angles to apply at each branch of the Formboard. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AsDesigned", "Use the angle equal to the 3D angle of the branch in the 3D harness."
       "StandardAngles", "Apply a standard angle to the branch, the level of the branch determines which angle to apply."
       "MaximumAngles", "Apply the largest possible angle values at every branch to force the harness to spread out."
       "RandomAngles", "Randomly choose an angle for each branch."
    """
    AsDesigned = 0  # FormboardLayoutBuilderBranchAngleMemberType
    StandardAngles = 1  # FormboardLayoutBuilderBranchAngleMemberType
    MaximumAngles = 2  # FormboardLayoutBuilderBranchAngleMemberType
    RandomAngles = 3  # FormboardLayoutBuilderBranchAngleMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FormboardLayoutBuilderBranchShapeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FormboardLayoutBuilderBranchShape():
    """
    Shape option for the branches. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Straight", "Each branch forms a straight line."
       "Angled", "Branch becomes angled at each location that forms a new branch."
    """
    Straight = 0  # FormboardLayoutBuilderBranchShapeMemberType
    Angled = 1  # FormboardLayoutBuilderBranchShapeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FormboardLayoutBuilder(NXOpen.Builder):
    """
    Class that performs the "layout" of Formboard geometry.  
    
    Creates all geometry
    chosen by the user to flatten into a drawing and orients the geometry to
    match the criteria specified in this builder class.   This builder must only
    be instantiated and used after the harnesses have been specified and stored
    using the :py:meth:`NXOpen.Formboard.FormboardManager.StoreHarnessesToFlatten` method. 
    To create a new instance of this class, use :py:meth:`NXOpen.Formboard.FormboardManager.CreateLayoutBuilder`
    
    .. versionadded:: NX7.5.0
    """
    
    class MainRunType():
        """
        Selection method for the set of segments that define the main
        run of the formboard geometry. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Longest", "Path of longest wire."
           "Thickest", "Path of longest wire contained within the thickest bundle."
           "UserSelection", "Manual selection of path."
        """
        Longest = 0  # FormboardLayoutBuilderMainRunTypeMemberType
        Thickest = 1  # FormboardLayoutBuilderMainRunTypeMemberType
        UserSelection = 2  # FormboardLayoutBuilderMainRunTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BranchAngle():
        """
        Methods for determining which angles to apply at each branch of the Formboard. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AsDesigned", "Use the angle equal to the 3D angle of the branch in the 3D harness."
           "StandardAngles", "Apply a standard angle to the branch, the level of the branch determines which angle to apply."
           "MaximumAngles", "Apply the largest possible angle values at every branch to force the harness to spread out."
           "RandomAngles", "Randomly choose an angle for each branch."
        """
        AsDesigned = 0  # FormboardLayoutBuilderBranchAngleMemberType
        StandardAngles = 1  # FormboardLayoutBuilderBranchAngleMemberType
        MaximumAngles = 2  # FormboardLayoutBuilderBranchAngleMemberType
        RandomAngles = 3  # FormboardLayoutBuilderBranchAngleMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BranchShape():
        """
        Shape option for the branches. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Straight", "Each branch forms a straight line."
           "Angled", "Branch becomes angled at each location that forms a new branch."
        """
        Straight = 0  # FormboardLayoutBuilderBranchShapeMemberType
        Angled = 1  # FormboardLayoutBuilderBranchShapeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreateDefaultGeometry(self) -> None:
        """
        Creates the initial set of formboard geometry using the current 
        default values stored in the builder.  
        
        This geometry is necessary for the
        UI to allow the user to see and select formboard geometry, for example to define
        a Main Run.   Does nothing if the work part already contains formboard
        geometry.  
        
        Signature ``CreateDefaultGeometry()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def UpdateLayout(self) -> None:
        """
        Updates the orientation and placement of the formboard geometry to match
        the current set of layout options stored within the builder.  
        
        Signature ``UpdateLayout()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def TranslateToNewOrigin(self) -> None:
        """
        Translates the formboard geometry so that it matches the new main run origin, this is a more
        lightweight operation than the full UpdateLayout operation.  
        
        The assumption here
        is that the only change to the builder is with the main run origin. 
        
        Signature ``TranslateToNewOrigin()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    BranchAngleMethod: FormboardLayoutBuilderBranchAngle = ...
    """
    Returns or sets  the branch angle type.  
    
    Specifies how the layout algorithm determines the angle
    between each child branch and its parent branch.  
    
    <hr>
    
    Getter Method
    
    Signature ``BranchAngleMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``BranchAngleMethod`` 
    
    :param branchAngle: 
    :type branchAngle: :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    BranchShapeType: FormboardLayoutBuilderBranchShape = ...
    """
    Returns or sets  the branch shape type.  
    
    <hr>
    
    Getter Method
    
    Signature ``BranchShapeType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchShape` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``BranchShapeType`` 
    
    :param branchShape: 
    :type branchShape: :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchShape` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    LengthOptions: LayoutLengthOptions = ...
    """
    Returns  the length options for the layout operation.  
    
    The length options only have
    any effect if this is the first time that the Formboard geometry is being
    created in the drawing. 
    
    <hr>
    
    Getter Method
    
    Signature ``LengthOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.LayoutLengthOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    MainRunEndSelection: NXOpen.Routing.SelectControlPoint = ...
    """
    Returns  the end of the main run.  
    
    Contains the ending control point 
    that defines the main run of the Formboard if the 
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderMainRunType` is 
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderMainRunType.UserSelection <NXOpen.Formboard.FormboardLayoutBuilderMainRunType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``MainRunEndSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.SelectControlPoint` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    MainRunMethod: FormboardLayoutBuilderMainRunType = ...
    """
    Returns or sets  the main run method.  
    
    <hr>
    
    Getter Method
    
    Signature ``MainRunMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.FormboardLayoutBuilderMainRunType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``MainRunMethod`` 
    
    :param mainRunType: 
    :type mainRunType: :py:class:`NXOpen.Formboard.FormboardLayoutBuilderMainRunType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    MainRunOrigin: NXOpen.Point = ...
    """
    Returns or sets  the main run origin.  
    
    The location in modeling space of the start 
    of the main run. The layout operation translates the main run such 
    that it start RCP is located at this location. 
    
    <hr>
    
    Getter Method
    
    Signature ``MainRunOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``MainRunOrigin`` 
    
    :param mainRunOrigin: 
    :type mainRunOrigin: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    MainRunStartSelection: NXOpen.Routing.SelectControlPoint = ...
    """
    Returns  the start of the main run.  
    
    Contains the starting control point 
    that defines the main run of the Formboard if the 
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderMainRunType` is 
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderMainRunType.UserSelection <NXOpen.Formboard.FormboardLayoutBuilderMainRunType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``MainRunStartSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.SelectControlPoint` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    MaximumRandomAngle: NXOpen.Expression = ...
    """
    Returns  the maximum random angle.  
    
    Used when
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle` is
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle.RandomAngles <NXOpen.Formboard.FormboardLayoutBuilderBranchAngle>`.
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumRandomAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    MinimumRandomAngle: NXOpen.Expression = ...
    """
    Returns  the minimum random angle.  
    
    Used when 
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle` is
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle.RandomAngles <NXOpen.Formboard.FormboardLayoutBuilderBranchAngle>`.
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumRandomAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    PrimaryStandardAngle: NXOpen.Expression = ...
    """
    Returns  the primary standard angle.  
    
    The layout algorithm snaps the angle of the
    branch to a multiple of this angle.  
    Only used when the 
    :py:meth:`NXOpen.Formboard.FormboardLayoutBuilder.BranchAngleMethod` is
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle.StandardAngles <NXOpen.Formboard.FormboardLayoutBuilderBranchAngle>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``PrimaryStandardAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    ReverseMainRun: bool = ...
    """
    Returns or sets  the flag that determines whether the main run is "reversed" or not.  
    
    If true then
    the direction and order of the main run path is reversed.   The end of the main
    run becomes the start and vice-versa.  The list of path segments is not
    modified or re-ordered, only the order in which the path segments is evaluated
    when laying out the geometry. 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseMainRun`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseMainRun`` 
    
    :param reverseMainRun: 
    :type reverseMainRun: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    SecondaryStandardAngle: NXOpen.Expression = ...
    """
    Returns  the secondary standard angle.  
    
    The layout algorithm snaps the angle of the
    branch to a multiple of this angle when all multiples of the primary angle
    have been used.  
    
    Only used when the 
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle` is
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle.StandardAngles <NXOpen.Formboard.FormboardLayoutBuilderBranchAngle>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryStandardAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    TertiaryStandardAngle: NXOpen.Expression = ...
    """
    Returns  the tertiary standard angle.  
    
    The layout algorithm snaps the angle of the
    branch to a multiple of this angle when all multiples of the primary and secondary 
    angles have been used.  
    
    Only used when the 
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle` is
    :py:class:`NXOpen.Formboard.FormboardLayoutBuilderBranchAngle.StandardAngles <NXOpen.Formboard.FormboardLayoutBuilderBranchAngle>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``TertiaryStandardAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Null: FormboardLayoutBuilder = ...  # unknown typename


class OrientBranchBuilderBranchAngleMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OrientBranchBuilderBranchAngleMethod():
    """
    Enum to define the type of method to orient branch. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AnglefromReferenceVector", "method to rotate branch with respect to selected vectors"
       "Angle", "method to rotate branch by angle"
       "AlignAxisToVector", "method to rotate branch by an angle between two vectors"
       "TwoPoints", "method to rotate branch by and angle between two points"
    """
    AnglefromReferenceVector = 0  # OrientBranchBuilderBranchAngleMethodMemberType
    Angle = 1  # OrientBranchBuilderBranchAngleMethodMemberType
    AlignAxisToVector = 2  # OrientBranchBuilderBranchAngleMethodMemberType
    TwoPoints = 3  # OrientBranchBuilderBranchAngleMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OrientBranchBuilder(NXOpen.Builder):
    """
    Builder for "Orient Branch" operation used in formboard.  
    
    Allows user to orient the branch by different methods.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Formboard.FormboardManager.CreateOrientBranchBuilder`
    
    Default values.
    
    ====================  =========================
    Property              Value
    ====================  =========================
    BranchAngleType       AnglefromReferenceVector 
    --------------------  -------------------------
    RotationAngle.Value   0 
    ====================  =========================
    
    .. versionadded:: NX7.5.0
    """
    
    class BranchAngleMethod():
        """
        Enum to define the type of method to orient branch. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AnglefromReferenceVector", "method to rotate branch with respect to selected vectors"
           "Angle", "method to rotate branch by angle"
           "AlignAxisToVector", "method to rotate branch by an angle between two vectors"
           "TwoPoints", "method to rotate branch by and angle between two points"
        """
        AnglefromReferenceVector = 0  # OrientBranchBuilderBranchAngleMethodMemberType
        Angle = 1  # OrientBranchBuilderBranchAngleMethodMemberType
        AlignAxisToVector = 2  # OrientBranchBuilderBranchAngleMethodMemberType
        TwoPoints = 3  # OrientBranchBuilderBranchAngleMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def UpdateRotationAngle(self, angle: float) -> None:
        """
        Rotates the branch by an appropriate rotation and transformation
        which depends on the :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod`
        selected by user.  
        
        Signature ``UpdateRotationAngle(angle)`` 
        
        :param angle:  angle for rotation  
        :type angle: float 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX9.0.1
           This method is no longer required.
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def StartDrag(self) -> None:
        """
        Starts the drag operation of selected object.  
        
        Does nothing if drag has
        already been started.
        
        Signature ``StartDrag()`` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX9.0.1
           This method is no longer required.
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def StopDrag(self) -> None:
        """
        Stop the drag operation of selected object.  
        
        Does nothing if drag has
        not been started.
        
        Signature ``StopDrag()`` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX9.0.1
           This method is no longer required.
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def InitializeFromSegment(self) -> None:
        """
        Initializes or resets ( start or stop ) drag operation based on the 
        input branch segment.  
        
        Signature ``InitializeFromSegment()`` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX9.0.1
           This method is no longer required.
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def SetBranchSeedObject(self, segmentTag: NXOpen.Routing.ISegment) -> None:
        """
        Sets the selected branch :py:class:`NXOpen.Routing.ISegment` when
        a branch is selected by branch method by Routing Object Collector.  
        
        Signature ``SetBranchSeedObject(segmentTag)`` 
        
        :param segmentTag:  selected seed object  
        :type segmentTag: :py:class:`NXOpen.Routing.ISegment` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def UnSuppressConstraints(self) -> None:
        """
        Suppress the :py:class:`NXOpen.Positioning.Constraint` associated with selected branch :py:class:`NXOpen.Routing.ISegment`
        when a branch is selected by branch method by Routing Object Collector.  
        
        Signature ``UnSuppressConstraints()`` 
        
        .. versionadded:: NX7.5.3
        
        .. deprecated::  NX7.5.3
           This method is no longer relevant and calls to this can be safely removed.
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    BranchAngleType: OrientBranchBuilderBranchAngleMethod = ...
    """
    Returns or sets  the user selected :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod` 
    
    <hr>
    
    Getter Method
    
    Signature ``BranchAngleType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``BranchAngleType`` 
    
    :param branchAngleType: 
    :type branchAngleType: :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    FromPoint: NXOpen.Point = ...
    """
    Returns or sets  the user selected from point when :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod` is 
    :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.TwoPoints  < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``FromPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX8.5.0
       This :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.TwoPoints  < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>` is no longer supported.
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``FromPoint`` 
    
    :param fromPoint: 
    :type fromPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX8.5.0
       This :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.TwoPoints  < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>` is no longer supported.
    
    License requirements: routing_harness ("Routing Harness")
    """
    FromVector: NXOpen.Direction = ...
    """
    Returns or sets  the user selected from vector when :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod` is 
    :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.AlignAxisToVector  < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``FromVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX8.5.0
       This builder attribute is no longer required.
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``FromVector`` 
    
    :param fromVector: 
    :type fromVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX8.5.0
       This builder attribute is no longer required.
    
    License requirements: routing_harness ("Routing Harness")
    """
    RefRotationAngle: NXOpen.Expression = ...
    """
    Returns  the angle for the rotation of branch when :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod` is 
    :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.AnglefromReferenceVector  < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``RefRotationAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    ReferenceVector: NXOpen.Direction = ...
    """
    Returns or sets  the user selected reference vector when :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod` is 
    :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.AnglefromReferenceVector  < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceVector`` 
    
    :param referenceVector: 
    :type referenceVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    RotationAngle: NXOpen.Expression = ...
    """
    Returns  the angle for the rotation of branch when :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod` is 
    :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.Angle < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``RotationAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    SelectBranch: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the user selected branch :py:class:`NXOpen.Routing.ISegment`
    for rotation.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectBranch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    ToPoint: NXOpen.Point = ...
    """
    Returns or sets  the user selected to point when :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod` is 
    :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.TwoPoints  < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ToPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX8.5.0
       This :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.TwoPoints  < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>` is no longer supported.
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``ToPoint`` 
    
    :param toPoint: 
    :type toPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX8.5.0
       This :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.TwoPoints  < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>` is no longer supported.
    
    License requirements: routing_harness ("Routing Harness")
    """
    ToVector: NXOpen.Direction = ...
    """
    Returns or sets  the user selected to vector when :py:class:`NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod` is 
    :py:class:` NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod.AlignAxisToVector  < NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ToVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``ToVector`` 
    
    :param toVector: 
    :type toVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Null: OrientBranchBuilder = ...  # unknown typename


class FlipComponentBuilderAxisTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlipComponentBuilderAxisType():
    """
    Enum for the selection of axis type for flipping formboard component
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PathLocations", "Flip component by path locations"
       "Custom", "Flip component by user defined custom axis"
    """
    PathLocations = 0  # FlipComponentBuilderAxisTypeMemberType
    Custom = 1  # FlipComponentBuilderAxisTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlipComponentBuilder(NXOpen.Builder):
    """
    Builder for flip component operation used in formboard.  
    
    Allows user to flip the component by 180 degrees about an axis which is
    orthogonal to Z axis so that after flipping , the component lies in XY plane.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Formboard.FormboardManager.CreateFlipComponentBuilder`
    
    Default values.
    
    =============  ==============
    Property       Value
    =============  ==============
    AxisTypeEnum   PathLocations 
    =============  ==============
    
    .. versionadded:: NX7.5.0
    """
    
    class AxisType():
        """
        Enum for the selection of axis type for flipping formboard component
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PathLocations", "Flip component by path locations"
           "Custom", "Flip component by user defined custom axis"
        """
        PathLocations = 0  # FlipComponentBuilderAxisTypeMemberType
        Custom = 1  # FlipComponentBuilderAxisTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def StartDrag(self) -> None:
        """
        Starts the drag operation of selected object.  
        
        Does nothing if drag has
        already been started.
        
        Signature ``StartDrag()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def StopDrag(self) -> None:
        """
        Stop the drag operation of selected object.  
        
        Does nothing if drag has
        not been started.
        
        Signature ``StopDrag()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def InitializeFromComponent(self) -> None:
        """
        Initializes or resets ( start or stop ) drag operation based on the 
        component selected for flipping operation.  
        
        Signature ``InitializeFromComponent()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def FlipComponent(self) -> None:
        """
        Flips the selected formboard component by rotation angle 
        about selected axis.  
        
        Signature ``FlipComponent()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateDatumAxis(self) -> 'list[NXOpen.NXObject]':
        """
        Creates datums axis at locations where selected formboard component 
        is connected to path.  
        
        Signature ``CreateDatumAxis()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def SetRotationAngle(self, angle: float) -> None:
        """
        Set the angle to rotate the component.  
        
        Signature ``SetRotationAngle(angle)`` 
        
        :param angle:  Rotation angle 
        :type angle: float 
        
        .. versionadded:: NX7.5.3
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    AxisTypeEnum: FlipComponentBuilderAxisType = ...
    """
    Returns or sets  the user selected :py:class:`NXOpen.Formboard.FlipComponentBuilderAxisType` method 
    
    <hr>
    
    Getter Method
    
    Signature ``AxisTypeEnum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.FlipComponentBuilderAxisType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``AxisTypeEnum`` 
    
    :param axisTypeEnum: 
    :type axisTypeEnum: :py:class:`NXOpen.Formboard.FlipComponentBuilderAxisType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    CompSel: NXOpen.SelectNXObject = ...
    """
    Returns  the formboard component selected by user for flipping operation 
    
    <hr>
    
    Getter Method
    
    Signature ``CompSel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObject` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    CustomAxis: NXOpen.Axis = ...
    """
    Returns or sets  the custom axis which is created when 
    :py:class:`NXOpen.Formboard.FlipComponentBuilderAxisType` is
    :py:class:`NXOpen.Formboard.FlipComponentBuilderAxisType.Custom <NXOpen.Formboard.FlipComponentBuilderAxisType>`
    
    <hr>
    
    Getter Method
    
    Signature ``CustomAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Axis` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``CustomAxis`` 
    
    :param customAxis: 
    :type customAxis: :py:class:`NXOpen.Axis` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    PathAxisSel: NXOpen.SelectNXObject = ...
    """
    Returns  the axis selected by user about which selected formboard component 
    will be flipped.  
    
    <hr>
    
    Getter Method
    
    Signature ``PathAxisSel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObject` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Null: FlipComponentBuilder = ...  # unknown typename


class ObjectAttributeReferenceBuilderLeaderTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ObjectAttributeReferenceBuilderLeaderType():
    """
    Enum which defines types of leader user wants to associate with the annotation.
    User can either create no leader or one or two leader for the annotation when picking 
    the associated object.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No leader for annotation of selected object."
       "SingleLocation", "Single leader for the annotation of selected object."
       "StartandEndLocations", "Two leaders for annotation with start and end location."
    """
    NotSet = 0  # ObjectAttributeReferenceBuilderLeaderTypeMemberType
    SingleLocation = 1  # ObjectAttributeReferenceBuilderLeaderTypeMemberType
    StartandEndLocations = 2  # ObjectAttributeReferenceBuilderLeaderTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ObjectAttributeReferenceBuilder(NXOpen.Builder):
    """
    Builder for "object attribute" used in formboard which enbles user to create
    annotation in drafting functionality.  
    
    It creates a tabular note and displays
    object attributes of a single object selected by user.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Formboard.FormboardManager.CreateObjectAttributeReferenceBuilder`
    
    Default values.
    
    =========  =====
    Property   Value
    =========  =====
    EnumType   None 
    =========  =====
    
    .. versionadded:: NX7.5.0
    """
    
    class LeaderType():
        """
        Enum which defines types of leader user wants to associate with the annotation.
        User can either create no leader or one or two leader for the annotation when picking 
        the associated object.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No leader for annotation of selected object."
           "SingleLocation", "Single leader for the annotation of selected object."
           "StartandEndLocations", "Two leaders for annotation with start and end location."
        """
        NotSet = 0  # ObjectAttributeReferenceBuilderLeaderTypeMemberType
        SingleLocation = 1  # ObjectAttributeReferenceBuilderLeaderTypeMemberType
        StartandEndLocations = 2  # ObjectAttributeReferenceBuilderLeaderTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AnnotLeader: NXOpen.Annotations.LeaderBuilder = ...
    """
    Returns  the :py:class:`Annotations.LeaderBuilder` for the annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``AnnotLeader`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.LeaderBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    CompOrigin: NXOpen.Annotations.OriginBuilder = ...
    """
    Returns  the comp origin 
    
    <hr>
    
    Getter Method
    
    Signature ``CompOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.OriginBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    EnumType: ObjectAttributeReferenceBuilderLeaderType = ...
    """
    Returns or sets  the enum type 
    
    <hr>
    
    Getter Method
    
    Signature ``EnumType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.ObjectAttributeReferenceBuilderLeaderType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``EnumType`` 
    
    :param enumType: 
    :type enumType: :py:class:`NXOpen.Formboard.ObjectAttributeReferenceBuilderLeaderType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    ObjectSelection: NXOpen.SelectNXObject = ...
    """
    Returns  the object selected by user to associated annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObject` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Null: ObjectAttributeReferenceBuilder = ...  # unknown typename


class UpdateFormboardBuilder(NXOpen.Builder):
    """
    Class that performs the "update" of Formboard geometry.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Formboard.FormboardManager.CreateUpdateFormboardBuilder`
    
    .. versionadded:: NX7.5.0
    """
    
    def GetHarnessPart(self) -> NXOpen.Part:
        """
        Gets the 3D harness part file to compare the formboard against.  
        
        Signature ``GetHarnessPart()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def SetHarnessPart(self, harnessPart: NXOpen.Part) -> None:
        """
        Sets the 3D harness part file to compare the formboard against.  
        
        This clears
        any discrepancies that have been discovered against the previous harness
        part.  
        
        Signature ``SetHarnessPart(harnessPart)`` 
        
        :param harnessPart: 
        :type harnessPart: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def SetHarnesses(self, harnesses: 'list[NXOpen.Routing.Electrical.HarnessDevice]') -> None:
        """
        Sets the harnesses within the harness part that the formboard must be 
        compared with.  
        
        Signature ``SetHarnesses(harnesses)`` 
        
        :param harnesses:  Harnesses to compare against.  
        :type harnesses: list of :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def FindMapping(self) -> None:
        """
        Compute the mapping between the data in the formboard and the data in the
        3D harness.  
        
        This method can take a very long time to execute. 
        
        Signature ``FindMapping()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def DetermineDiscrepancies(self) -> None:
        """
        Once the mapping has been determined, this method can find any discrepancies
        between the 3D harness and the formboard.  
        
        Signature ``DetermineDiscrepancies()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def GetNumberOfDiscrepancies(self) -> int:
        """
        Returns the number of discrepancies discovered by the 
        :py:meth:`Formboard.UpdateFormboardBuilder.DetermineDiscrepancies`.  
        
        Signature ``GetNumberOfDiscrepancies()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def GetDiscrepancy(self, index: int) -> UpdateDiscrepancy:
        """
        Returns the discrepancy at the given index.  
        
        The index must be
        0 to :py:meth:`Formboard.UpdateFormboardBuilder.GetNumberOfDiscrepancies`.
        
        Signature ``GetDiscrepancy(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Formboard.UpdateDiscrepancy` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def RemoveBendsOfRadialBends(self) -> None:
        """
        Removes bends in all radial bends and replaces them with a linear segment
        going from the anchor to the free RCP of each radial bend.  
        
        This is done before
        fixing discrepancies because presence of bends in radial bend causes problems.
        The bends of radial bends are recreated after the discrepancies have been fixed
        using CreateBendsOfRadialBends
        
        Signature ``RemoveBendsOfRadialBends()`` 
        
        .. versionadded:: NX7.5.5
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreateBendsOfRadialBends(self) -> None:
        """
        Creates bends for radial bends after all discrepanices have been fixed.  
        
        This routine
        should be called in conjunction with RemoveBendsOfRadialBends.
        
        Signature ``CreateBendsOfRadialBends()`` 
        
        .. versionadded:: NX7.5.5
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    LengthOptions: LayoutLengthOptions = ...
    """
    Returns  the length options for the update operation.  
    
    <hr>
    
    Getter Method
    
    Signature ``LengthOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.LayoutLengthOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Null: UpdateFormboardBuilder = ...  # unknown typename


class UpdateDiscrepancyTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UpdateDiscrepancyType():
    """
    The general type of the discrepancy. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", "Unknown type, not valid."
       "Missing", "Object exits in the 3D harness but is missing from the formboard."
       "Extra", "Object is in the formboard but not in the 3D harness."
       "Modified", "Object exists in both 3D and the formboard but is modified in some way."
    """
    Unknown = 0  # UpdateDiscrepancyTypeMemberType
    Missing = 1  # UpdateDiscrepancyTypeMemberType
    Extra = 2  # UpdateDiscrepancyTypeMemberType
    Modified = 3  # UpdateDiscrepancyTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UpdateDiscrepancyObjectTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UpdateDiscrepancyObjectType():
    """
    Specifies the type of objects involved in the discrepancy. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", "Unknown type."
       "Rcp", "Routing Control Point."
       "Segment", "Routing Segment."
       "Clip", "A component not assigned as a electrical connector."
       "Component", "A component assigned as a electrical connector or device."
       "Harness", "Harness."
       "Wire", "Wire connection."
       "Cable", "Cable connection."
       "Shield", "Shield connection."
       "Connector", "ConnectorDevice object which has a type of connector."
       "Device", "ConnectorDevice object which has a type of device."
       "Overstock", "Overstock."
       "Fillerstock", "Filler stock."
       "FittingOverstock", "Overstock applied to fittings."
    """
    Unknown = 0  # UpdateDiscrepancyObjectTypeMemberType
    Rcp = 1  # UpdateDiscrepancyObjectTypeMemberType
    Segment = 2  # UpdateDiscrepancyObjectTypeMemberType
    Clip = 3  # UpdateDiscrepancyObjectTypeMemberType
    Component = 4  # UpdateDiscrepancyObjectTypeMemberType
    Harness = 5  # UpdateDiscrepancyObjectTypeMemberType
    Wire = 6  # UpdateDiscrepancyObjectTypeMemberType
    Cable = 7  # UpdateDiscrepancyObjectTypeMemberType
    Shield = 8  # UpdateDiscrepancyObjectTypeMemberType
    Connector = 9  # UpdateDiscrepancyObjectTypeMemberType
    Device = 10  # UpdateDiscrepancyObjectTypeMemberType
    Overstock = 11  # UpdateDiscrepancyObjectTypeMemberType
    Fillerstock = 12  # UpdateDiscrepancyObjectTypeMemberType
    FittingOverstock = 13  # UpdateDiscrepancyObjectTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UpdateDiscrepancy(NXOpen.TransientObject):
    """
    Defines a discrepancy object which contains information about a specific
    difference between the formboard drawing and the 3D harness model.  
    
    .. versionadded:: NX7.5.0
    """
    
    class Type():
        """
        The general type of the discrepancy. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unknown", "Unknown type, not valid."
           "Missing", "Object exits in the 3D harness but is missing from the formboard."
           "Extra", "Object is in the formboard but not in the 3D harness."
           "Modified", "Object exists in both 3D and the formboard but is modified in some way."
        """
        Unknown = 0  # UpdateDiscrepancyTypeMemberType
        Missing = 1  # UpdateDiscrepancyTypeMemberType
        Extra = 2  # UpdateDiscrepancyTypeMemberType
        Modified = 3  # UpdateDiscrepancyTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ObjectType():
        """
        Specifies the type of objects involved in the discrepancy. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unknown", "Unknown type."
           "Rcp", "Routing Control Point."
           "Segment", "Routing Segment."
           "Clip", "A component not assigned as a electrical connector."
           "Component", "A component assigned as a electrical connector or device."
           "Harness", "Harness."
           "Wire", "Wire connection."
           "Cable", "Cable connection."
           "Shield", "Shield connection."
           "Connector", "ConnectorDevice object which has a type of connector."
           "Device", "ConnectorDevice object which has a type of device."
           "Overstock", "Overstock."
           "Fillerstock", "Filler stock."
           "FittingOverstock", "Overstock applied to fittings."
        """
        Unknown = 0  # UpdateDiscrepancyObjectTypeMemberType
        Rcp = 1  # UpdateDiscrepancyObjectTypeMemberType
        Segment = 2  # UpdateDiscrepancyObjectTypeMemberType
        Clip = 3  # UpdateDiscrepancyObjectTypeMemberType
        Component = 4  # UpdateDiscrepancyObjectTypeMemberType
        Harness = 5  # UpdateDiscrepancyObjectTypeMemberType
        Wire = 6  # UpdateDiscrepancyObjectTypeMemberType
        Cable = 7  # UpdateDiscrepancyObjectTypeMemberType
        Shield = 8  # UpdateDiscrepancyObjectTypeMemberType
        Connector = 9  # UpdateDiscrepancyObjectTypeMemberType
        Device = 10  # UpdateDiscrepancyObjectTypeMemberType
        Overstock = 11  # UpdateDiscrepancyObjectTypeMemberType
        Fillerstock = 12  # UpdateDiscrepancyObjectTypeMemberType
        FittingOverstock = 13  # UpdateDiscrepancyObjectTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
        Frees the memory associated with this object.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    Description: str = ...
    """
    Returns  the description string of the discrepancy.  
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    DiscrepancyObjectType: UpdateDiscrepancyObjectType = ...
    """
    Returns  the type of object referenced by the discrepancy.  
    
    <hr>
    
    Getter Method
    
    Signature ``DiscrepancyObjectType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.UpdateDiscrepancyObjectType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    DiscrepancyType: UpdateDiscrepancyType = ...
    """
    Returns  the general type of the discrepancy.  
    
    <hr>
    
    Getter Method
    
    Signature ``DiscrepancyType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.UpdateDiscrepancyType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    FormboardObject: NXOpen.NXObject = ...
    """
    Returns  the object in the 2D formboard referenced by the discrepancy.  
    
    This may
    be None depending on the type of the discrepancy.
    
    <hr>
    
    Getter Method
    
    Signature ``FormboardObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    HarnessObject: NXOpen.NXObject = ...
    """
    Returns  the object in the 3D harness referenced by the discrepancy.  
    
    This may
    be None depending on the type of the discrepancy.
    
    <hr>
    
    Getter Method
    
    Signature ``HarnessObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """


class PathLengthAnnotationBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PathLengthAnnotationBuilderTypes():
    """
    TODO: Document the whole type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PointsOnCurves", "TODO"
       "RoutingPathLength", "TODO"
    """
    PointsOnCurves = 0  # PathLengthAnnotationBuilderTypesMemberType
    RoutingPathLength = 1  # PathLengthAnnotationBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PathLengthAnnotationBuilder(NXOpen.Builder):
    """
    TODO Class documentation   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Formboard.FormboardManager.CreatePathLengthAnnotationBuilder`
    
    Default values.
    
    =================================  ===========================================
    Property                           Value
    =================================  ===========================================
    ShowLeadersToggle                  0 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.CustomSymbolScale   1.0 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolAspectRatio   1.0 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolHeight        25.4 (millimeters part), 1.0 (inches part) 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolLength        25.4 (millimeters part), 1.0 (inches part) 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolPreferences   UseCurrent 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolScale         1.0 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolSizeMethod    ScaleAndAspectRatio 
    =================================  ===========================================
    
    .. versionadded:: NX7.5.0
    """
    
    class Types():
        """
        TODO: Document the whole type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PointsOnCurves", "TODO"
           "RoutingPathLength", "TODO"
        """
        PointsOnCurves = 0  # PathLengthAnnotationBuilderTypesMemberType
        RoutingPathLength = 1  # PathLengthAnnotationBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetPathLengthAnnotationEndPoints(self, firstEndPoint: NXOpen.Point, secondEndPoint: NXOpen.Point) -> None:
        """
        Create and initialize the Path Length Annotation 
        
        Signature ``SetPathLengthAnnotationEndPoints(firstEndPoint, secondEndPoint)`` 
        
        :param firstEndPoint:  First end point for the path length annotation  
        :type firstEndPoint: :py:class:`NXOpen.Point` 
        :param secondEndPoint:  Second end point for the path length annotation  
        :type secondEndPoint: :py:class:`NXOpen.Point` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    
    def CreatePointsAtRcps(self, firstEndRcp: NXOpen.Routing.ControlPoint, secondEndRcp: NXOpen.Routing.ControlPoint) -> None:
        """
        Create builder end points at the RCP locations
        
        Signature ``CreatePointsAtRcps(firstEndRcp, secondEndRcp)`` 
        
        :param firstEndRcp:  First Routing control point  
        :type firstEndRcp: :py:class:`NXOpen.Routing.ControlPoint` 
        :param secondEndRcp:  Second Routing control point  
        :type secondEndRcp: :py:class:`NXOpen.Routing.ControlPoint` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_harness ("Routing Harness")
        """
        ...
    
    ExpressionName: str = ...
    """
    Returns  the expression name 
    
    <hr>
    
    Getter Method
    
    Signature ``ExpressionName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    FirstEndPoint: NXOpen.Point = ...
    """
    Returns or sets  the first end point 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstEndPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``FirstEndPoint`` 
    
    :param firstEndPoint: 
    :type firstEndPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Leader: NXOpen.Annotations.LeaderBuilder = ...
    """
    Returns  the leader 
    
    <hr>
    
    Getter Method
    
    Signature ``Leader`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.LeaderBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Origin: NXOpen.Annotations.OriginBuilder = ...
    """
    Returns  the origin 
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.OriginBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    RouteObjectCollector: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the route object collector 
    
    <hr>
    
    Getter Method
    
    Signature ``RouteObjectCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    SecondEndPoint: NXOpen.Point = ...
    """
    Returns or sets  the second end point 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondEndPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``SecondEndPoint`` 
    
    :param secondEndPoint: 
    :type secondEndPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    ShowLeadersToggle: bool = ...
    """
    Returns or sets  the show leaders toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowLeadersToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowLeadersToggle`` 
    
    :param showLeadersToggle: 
    :type showLeadersToggle: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Style: NXOpen.Annotations.StyleBuilder = ...
    """
    Returns  the style 
    
    <hr>
    
    Getter Method
    
    Signature ``Style`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.StyleBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Text: NXOpen.Annotations.TextWithEditControlsBuilder = ...
    """
    Returns  the u icomp text with symbols0 
    
    <hr>
    
    Getter Method
    
    Signature ``Text`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.TextWithEditControlsBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Type: PathLengthAnnotationBuilderTypes = ...
    """
    Returns or sets  the type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Formboard.PathLengthAnnotationBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Formboard.PathLengthAnnotationBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_harness ("Routing Harness")
    """
    Null: PathLengthAnnotationBuilder = ...  # unknown typename


