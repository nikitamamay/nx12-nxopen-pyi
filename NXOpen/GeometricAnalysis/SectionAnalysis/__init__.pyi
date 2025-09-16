# module 'NXOpen.GeometricAnalysis.SectionAnalysis'
#
# Automatically generated 2025-06-09T14:38:46.743316
#

import typing

import NXOpen
import NXOpen.GeometricAnalysis
import NXOpen.GeometricUtilities



class XYZPlaneBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the XYZ Plane specification for a :py:class:`GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder`.  
    
    .. versionadded:: NX7.0.0
    """
    
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
    
    AnchorOrigin: NXOpen.Point3d = ...
    """
    Returns or sets  the anchor position 
    
    <hr>
    
    Getter Method
    
    Signature ``AnchorOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnchorOrigin`` 
    
    :param anchorOrigin: 
    :type anchorOrigin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    AnchorXAxis: NXOpen.Vector3d = ...
    """
    Returns or sets  the anchor X axis 
    
    <hr>
    
    Getter Method
    
    Signature ``AnchorXAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnchorXAxis`` 
    
    :param anchorXAxis: 
    :type anchorXAxis: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    AnchorYAxis: NXOpen.Vector3d = ...
    """
    Returns or sets  the anchor Y axis 
    
    <hr>
    
    Getter Method
    
    Signature ``AnchorYAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnchorYAxis`` 
    
    :param anchorYAxis: 
    :type anchorYAxis: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsNumberEnabled: bool = ...
    """
    Returns or sets  a value indicating whether the number is used 
    
    <hr>
    
    Getter Method
    
    Signature ``IsNumberEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsNumberEnabled`` 
    
    :param isNumberEnabled: 
    :type isNumberEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsSpacingEnabled: bool = ...
    """
    Returns or sets  a value indicating whether the spacing is applied 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSpacingEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSpacingEnabled`` 
    
    :param isSpacingEnabled: 
    :type isSpacingEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsXEnabled: bool = ...
    """
    Returns or sets  a value indicating whether X is enabled 
    
    <hr>
    
    Getter Method
    
    Signature ``IsXEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsXEnabled`` 
    
    :param isXEnabled: 
    :type isXEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsYEnabled: bool = ...
    """
    Returns or sets  a value indicating whether Y is enabled 
    
    <hr>
    
    Getter Method
    
    Signature ``IsYEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsYEnabled`` 
    
    :param isYEnabled: 
    :type isYEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsZEnabled: bool = ...
    """
    Returns or sets  a value indicating whether Z is enabled 
    
    <hr>
    
    Getter Method
    
    Signature ``IsZEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsZEnabled`` 
    
    :param isZEnabled: 
    :type isZEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Number: int = ...
    """
    Returns or sets  a value indicating how many sections should be created 
    
    <hr>
    
    Getter Method
    
    Signature ``Number`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Number`` 
    
    :param number: 
    :type number: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Spacing: float = ...
    """
    Returns or sets  a value indicating the space between sections 
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Spacing`` 
    
    :param spacing: 
    :type spacing: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: XYZPlaneBuilder = ...  # unknown typename


class SectionPlaneBuilderPlaneTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionPlaneBuilderPlaneType():
    """
    The type of different section planes 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Xc", "XC plane"
       "Yc", "YC plane"
       "Zc", "ZC plane"
       "View", "View plane"
       "Plane", "A user specifed plane"
    """
    Xc = 0  # SectionPlaneBuilderPlaneTypeMemberType
    Yc = 1  # SectionPlaneBuilderPlaneTypeMemberType
    Zc = 2  # SectionPlaneBuilderPlaneTypeMemberType
    View = 3  # SectionPlaneBuilderPlaneTypeMemberType
    Plane = 4  # SectionPlaneBuilderPlaneTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionPlaneBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a plane which is used to cut sections on faces or facet bodies   
    
    .. versionadded:: NX7.0.0
    """
    
    class PlaneType():
        """
        The type of different section planes 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Xc", "XC plane"
           "Yc", "YC plane"
           "Zc", "ZC plane"
           "View", "View plane"
           "Plane", "A user specifed plane"
        """
        Xc = 0  # SectionPlaneBuilderPlaneTypeMemberType
        Yc = 1  # SectionPlaneBuilderPlaneTypeMemberType
        Zc = 2  # SectionPlaneBuilderPlaneTypeMemberType
        View = 3  # SectionPlaneBuilderPlaneTypeMemberType
        Plane = 4  # SectionPlaneBuilderPlaneTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    Origin: NXOpen.Point3d = ...
    """
    Returns or sets  the plane origin 
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Origin`` 
    
    :param origin: 
    :type origin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Plane: SectionPlaneBuilderPlaneType = ...
    """
    Returns or sets  the plane type 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilderPlaneType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilderPlaneType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    XAxis: NXOpen.Vector3d = ...
    """
    Returns or sets  the plane X axis 
    
    <hr>
    
    Getter Method
    
    Signature ``XAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XAxis`` 
    
    :param xAxis: 
    :type xAxis: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    YAxis: NXOpen.Vector3d = ...
    """
    Returns or sets  the plane Y axis 
    
    <hr>
    
    Getter Method
    
    Signature ``YAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``YAxis`` 
    
    :param yAxis: 
    :type yAxis: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: SectionPlaneBuilder = ...  # unknown typename


class TriangularGridBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the triangular grid section specifications for a SectionAnalysisBuilder.  
    
    Only used when type is :py:class:`GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes.Triangular <GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes>`.
    
    .. versionadded:: NX6.0.0
    """
    
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
    
    Spacing: GridSpacingBuilder = ...
    """
    Returns  the spacing specification for the triangular grid 
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.GridSpacingBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SpecifiedPlane: SectionPlaneBuilder = ...
    """
    Returns  the user specified section plane 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifiedPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TriangularFrame: NXOpen.GeometricUtilities.TriangularFrameBuilder = ...
    """
    Returns  the triangular frame 
    
    <hr>
    
    Getter Method
    
    Signature ``TriangularFrame`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.TriangularFrameBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: TriangularGridBuilder = ...  # unknown typename


class GridSpacingBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the grid spacing for certain types of section specifications for
    the :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder`.  
    
    .. versionadded:: NX6.0.0
    """
    
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
    
    BoundSections1: bool = ...
    """
    Returns or sets  the flag to bound the section to grid in direction 1 
    
    <hr>
    
    Getter Method
    
    Signature ``BoundSections1`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``BoundSections1`` 
    
    :param boundSections1: 
    :type boundSections1: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    BoundSections2: bool = ...
    """
    Returns or sets  the flag to bound the section to grid in direction 2 
    
    <hr>
    
    Getter Method
    
    Signature ``BoundSections2`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``BoundSections2`` 
    
    :param boundSections2: 
    :type boundSections2: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Interval1: float = ...
    """
    Returns or sets  the interval of sections in direction 1 
    
    <hr>
    
    Getter Method
    
    Signature ``Interval1`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``Interval1`` 
    
    :param interval1: 
    :type interval1: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Interval2: float = ...
    """
    Returns or sets  the interval of sections in direction 2 
    
    <hr>
    
    Getter Method
    
    Signature ``Interval2`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``Interval2`` 
    
    :param interval2: 
    :type interval2: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    LockInterval1: bool = ...
    """
    Returns or sets  the flag to lock the section interval in direction 1 
    
    <hr>
    
    Getter Method
    
    Signature ``LockInterval1`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``LockInterval1`` 
    
    :param lockInterval1: 
    :type lockInterval1: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    LockInterval2: bool = ...
    """
    Returns or sets  the flag to lock the section interval in direction 2 
    
    <hr>
    
    Getter Method
    
    Signature ``LockInterval2`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``LockInterval2`` 
    
    :param lockInterval2: 
    :type lockInterval2: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SectionNumber1: int = ...
    """
    Returns or sets  the number of sections in direction 1 
    
    <hr>
    
    Getter Method
    
    Signature ``SectionNumber1`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``SectionNumber1`` 
    
    :param sectionNumber1: 
    :type sectionNumber1: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SectionNumber2: int = ...
    """
    Returns or sets  the number of sections in direction 2 
    
    <hr>
    
    Getter Method
    
    Signature ``SectionNumber2`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``SectionNumber2`` 
    
    :param sectionNumber2: 
    :type sectionNumber2: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: GridSpacingBuilder = ...  # unknown typename


class CircularGridBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the circular grid section specifications for a :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder`.  
    
    Only used when type is :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes.Circular <NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes>`.
    
    .. versionadded:: NX6.0.0
    """
    
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
    
    CircularFrame: NXOpen.GeometricUtilities.CircularFrameBuilder = ...
    """
    Returns  the circular frame 
    
    <hr>
    
    Getter Method
    
    Signature ``CircularFrame`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.CircularFrameBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Spacing: GridSpacingBuilder = ...
    """
    Returns  the spacing specification for the circular grid 
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.GridSpacingBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SpecifiedPlane: SectionPlaneBuilder = ...
    """
    Returns  the user specified section plane 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifiedPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: CircularGridBuilder = ...  # unknown typename


class IsoparametricBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the Isoparametric specification for a :py:class:`GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder`.  
    
    .. versionadded:: NX7.0.0
    """
    
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
    
    IsSpacingEnabled: bool = ...
    """
    Returns or sets  a value indicating whether the spacing is applied 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSpacingEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSpacingEnabled`` 
    
    :param isSpacingEnabled: 
    :type isSpacingEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsUEnabled: bool = ...
    """
    Returns or sets  a value indicating wheter the U direction is enabled 
    
    <hr>
    
    Getter Method
    
    Signature ``IsUEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsUEnabled`` 
    
    :param isUEnabled: 
    :type isUEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsVEnabled: bool = ...
    """
    Returns or sets  a value indicating wheter the V direction is enabled 
    
    <hr>
    
    Getter Method
    
    Signature ``IsVEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsVEnabled`` 
    
    :param isVEnabled: 
    :type isVEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Number: int = ...
    """
    Returns or sets  a value indicating how many sections should be created 
    
    <hr>
    
    Getter Method
    
    Signature ``Number`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Number`` 
    
    :param number: 
    :type number: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Spacing: float = ...
    """
    Returns or sets  a value indicating the space between sections 
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Spacing`` 
    
    :param spacing: 
    :type spacing: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: IsoparametricBuilder = ...  # unknown typename


class InteractiveBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the Interactive specification for a :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder`.  
    
    .. versionadded:: NX7.0.0
    """
    
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
    
    InteractiveSection: NXOpen.GeometricUtilities.InteractiveSectionBuilder = ...
    """
    Returns  the interactive section lines 
    
    <hr>
    
    Getter Method
    
    Signature ``InteractiveSection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.InteractiveSectionBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    IsCutInfiniteEnabled: bool = ...
    """
    Returns or sets  a value indicating whether extending the interactive section lines to infinite 
    
    <hr>
    
    Getter Method
    
    Signature ``IsCutInfiniteEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsCutInfiniteEnabled`` 
    
    :param enabled: 
    :type enabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: InteractiveBuilder = ...  # unknown typename


class CurveAlignedBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the Curve Aligned specification for a :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder`.  
    
    .. versionadded:: NX7.0.0
    """
    
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
    
    Curves: NXOpen.ScCollector = ...
    """
    Returns  the curves 
    
    <hr>
    
    Getter Method
    
    Signature ``Curves`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    IsSpacingEnabled: bool = ...
    """
    Returns or sets  a value indicating whether the spacing is applied 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSpacingEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSpacingEnabled`` 
    
    :param isSpacingEnabled: 
    :type isSpacingEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Number: int = ...
    """
    Returns or sets  a value indicating how many sections should be created 
    
    <hr>
    
    Getter Method
    
    Signature ``Number`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Number`` 
    
    :param number: 
    :type number: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Offset: float = ...
    """
    Returns or sets  a value indicating the distance from the start position 
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Offset`` 
    
    :param offset: 
    :type offset: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Spacing: float = ...
    """
    Returns or sets  a value indicating the space between sections 
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Spacing`` 
    
    :param spacing: 
    :type spacing: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SpecifiedPlane: SectionPlaneBuilder = ...
    """
    Returns  the user specified project plane 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifiedPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    UseProjectedCurve: bool = ...
    """
    Returns or sets  a value indicating whether to project the curve to a plane 
    
    <hr>
    
    Getter Method
    
    Signature ``UseProjectedCurve`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseProjectedCurve`` 
    
    :param useProjectedCurve: 
    :type useProjectedCurve: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: CurveAlignedBuilder = ...  # unknown typename


class QuadrilateralGridBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the quadrilateral grid section specifications for a :py:class:`GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder`.  
    
    Only used when type is :py:class:`GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes.Quadrilateral <GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes>`.
    
    .. versionadded:: NX6.0.0
    """
    
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
    
    QuadrilateralFrame: NXOpen.GeometricUtilities.QuadrilateralFrameBuilder = ...
    """
    Returns  the quadrilateral frame 
    
    <hr>
    
    Getter Method
    
    Signature ``QuadrilateralFrame`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.QuadrilateralFrameBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Spacing: GridSpacingBuilder = ...
    """
    Returns  the spacing specification for the quadrilateral grid 
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.GridSpacingBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SpecifiedPlane: SectionPlaneBuilder = ...
    """
    Returns  the user specified section plane 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifiedPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: QuadrilateralGridBuilder = ...  # unknown typename


class RadialBuilderRotationAxisTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RadialBuilderRotationAxisType():
    """
    The type of the rotation axis
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Xc", "XC axis"
       "Yc", "YC axis"
       "Zc", "ZC axis"
       "View", "View direction"
       "ArbitraryVector", "A user specified vector"
    """
    Xc = 0  # RadialBuilderRotationAxisTypeMemberType
    Yc = 1  # RadialBuilderRotationAxisTypeMemberType
    Zc = 2  # RadialBuilderRotationAxisTypeMemberType
    View = 3  # RadialBuilderRotationAxisTypeMemberType
    ArbitraryVector = 4  # RadialBuilderRotationAxisTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RadialBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the Radial specification for a :py:class:`GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder`.  
    
    .. versionadded:: NX7.0.0
    """
    
    class RotationAxisType():
        """
        The type of the rotation axis
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Xc", "XC axis"
           "Yc", "YC axis"
           "Zc", "ZC axis"
           "View", "View direction"
           "ArbitraryVector", "A user specified vector"
        """
        Xc = 0  # RadialBuilderRotationAxisTypeMemberType
        Yc = 1  # RadialBuilderRotationAxisTypeMemberType
        Zc = 2  # RadialBuilderRotationAxisTypeMemberType
        View = 3  # RadialBuilderRotationAxisTypeMemberType
        ArbitraryVector = 4  # RadialBuilderRotationAxisTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    IsSpacingEnabled: bool = ...
    """
    Returns or sets  a value indicating whether the spacing is applied 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSpacingEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSpacingEnabled`` 
    
    :param isSpacingEnabled: 
    :type isSpacingEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Number: int = ...
    """
    Returns or sets  a value indicating how many sections should created 
    
    <hr>
    
    Getter Method
    
    Signature ``Number`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Number`` 
    
    :param number: 
    :type number: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Offset: float = ...
    """
    Returns or sets  a value indicating the distance from the start position 
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Offset`` 
    
    :param offset: 
    :type offset: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    RotationAxis: RadialBuilderRotationAxisType = ...
    """
    Returns or sets  a value indicating the type of the rotation axis
    
    <hr>
    
    Getter Method
    
    Signature ``RotationAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilderRotationAxisType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RotationAxis`` 
    
    :param rotationAxis: 
    :type rotationAxis: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilderRotationAxisType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    RotationVector: NXOpen.Vector3d = ...
    """
    Returns or sets  the user specified rotation vector 
    
    <hr>
    
    Getter Method
    
    Signature ``RotationVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RotationVector`` 
    
    :param rotationVector: 
    :type rotationVector: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Spacing: float = ...
    """
    Returns or sets  a value indicating the space between sections 
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Spacing`` 
    
    :param spacing: 
    :type spacing: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SpecifiedRotationPoint: NXOpen.Point = ...
    """
    Returns or sets  the rotation point 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifiedRotationPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpecifiedRotationPoint`` 
    
    :param specifiedRotationPoint: 
    :type specifiedRotationPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    StartPosition: NXOpen.SelectPoint = ...
    """
    Returns  the start position 
    
    <hr>
    
    Getter Method
    
    Signature ``StartPosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectPoint` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Null: RadialBuilder = ...  # unknown typename


class SectionAnalysisBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisBuilderTypes():
    """
    Represents the sectioning types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Parallel", "Parallel Planes"
       "Isoparametric", "Isoparametric"
       "AlongCurve", "Along Curve"
       "Quadrilateral", "Quadrilateral"
       "Triangular", "Triangular"
       "Circular", "Circular"
    """
    Parallel = 0  # SectionAnalysisBuilderTypesMemberType
    Isoparametric = 1  # SectionAnalysisBuilderTypesMemberType
    AlongCurve = 2  # SectionAnalysisBuilderTypesMemberType
    Quadrilateral = 3  # SectionAnalysisBuilderTypesMemberType
    Triangular = 4  # SectionAnalysisBuilderTypesMemberType
    Circular = 5  # SectionAnalysisBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisBuilderOutputTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisBuilderOutputType():
    """
    The output options 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AnalysisObject", "Analysis Object"
       "SectionCurves", "section curves"
       "Both", "Both Analysis Object and section curves"
    """
    AnalysisObject = 0  # SectionAnalysisBuilderOutputTypeMemberType
    SectionCurves = 1  # SectionAnalysisBuilderOutputTypeMemberType
    Both = 2  # SectionAnalysisBuilderOutputTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisBuilderNeedleDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisBuilderNeedleDirectionType():
    """
    The needle direction 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", "Inside"
       "Outside", "Outside"
    """
    Inside = 0  # SectionAnalysisBuilderNeedleDirectionTypeMemberType
    Outside = 1  # SectionAnalysisBuilderNeedleDirectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisBuilderCalculationMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisBuilderCalculationMethodType():
    """
    The calculation method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Curvature", "Curvature"
       "RadiusofCurvature", "Radius of curvature"
    """
    Curvature = 0  # SectionAnalysisBuilderCalculationMethodTypeMemberType
    RadiusofCurvature = 1  # SectionAnalysisBuilderCalculationMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisBuilderScalingMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisBuilderScalingMethodType():
    """
    The scaling method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "Linear"
       "Logarithmic", "Logarithmic"
    """
    Linear = 0  # SectionAnalysisBuilderScalingMethodTypeMemberType
    Logarithmic = 1  # SectionAnalysisBuilderScalingMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.GeometricAnalysis.SectionAnalysisObject` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateSectionAnalysisBuilder`
    
    Default values.
    
    ======================================================  ===========================================
    Property                                                Value
    ======================================================  ===========================================
    CalculationMethod                                       Curvature 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.CircularFrame.AnchorAttachment             None 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.CircularFrame.Subtype                      Arbitrary 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.Spacing.BoundSections1                     True 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.Spacing.BoundSections2                     True 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.Spacing.Interval1                          45.0 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.Spacing.Interval2                          50.0 (millimeters part), 2.0 (inches part) 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.Spacing.LockInterval1                      False 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.Spacing.LockInterval2                      False 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.Spacing.SectionNumber1                     5 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.Spacing.SectionNumber2                     5 
    ------------------------------------------------------  -------------------------------------------
    CircularGrid.SpecifiedPlane.Plane                       View 
    ------------------------------------------------------  -------------------------------------------
    NeedleDirection                                         Outside 
    ------------------------------------------------------  -------------------------------------------
    Output                                                  AnalysisObject 
    ------------------------------------------------------  -------------------------------------------
    QuadrilateralGrid.QuadrilateralFrame.AnchorAttachment   None 
    ------------------------------------------------------  -------------------------------------------
    QuadrilateralGrid.QuadrilateralFrame.Subtype            Arbitrary 
    ------------------------------------------------------  -------------------------------------------
    ScalingMethod                                           Linear 
    ------------------------------------------------------  -------------------------------------------
    ShowInflectionPoints                                    False 
    ------------------------------------------------------  -------------------------------------------
    ShowPeakPoints                                          False 
    ------------------------------------------------------  -------------------------------------------
    ShowSectionLength                                       False 
    ------------------------------------------------------  -------------------------------------------
    TriangularGrid.TriangularFrame.AnchorAttachment         None 
    ------------------------------------------------------  -------------------------------------------
    TriangularGrid.TriangularFrame.Subtype                  Arbitrary 
    ------------------------------------------------------  -------------------------------------------
    Type                                                    Parallel 
    ======================================================  ===========================================
    
    .. versionadded:: NX6.0.0
    """
    
    class Types():
        """
        Represents the sectioning types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Parallel", "Parallel Planes"
           "Isoparametric", "Isoparametric"
           "AlongCurve", "Along Curve"
           "Quadrilateral", "Quadrilateral"
           "Triangular", "Triangular"
           "Circular", "Circular"
        """
        Parallel = 0  # SectionAnalysisBuilderTypesMemberType
        Isoparametric = 1  # SectionAnalysisBuilderTypesMemberType
        AlongCurve = 2  # SectionAnalysisBuilderTypesMemberType
        Quadrilateral = 3  # SectionAnalysisBuilderTypesMemberType
        Triangular = 4  # SectionAnalysisBuilderTypesMemberType
        Circular = 5  # SectionAnalysisBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OutputType():
        """
        The output options 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AnalysisObject", "Analysis Object"
           "SectionCurves", "section curves"
           "Both", "Both Analysis Object and section curves"
        """
        AnalysisObject = 0  # SectionAnalysisBuilderOutputTypeMemberType
        SectionCurves = 1  # SectionAnalysisBuilderOutputTypeMemberType
        Both = 2  # SectionAnalysisBuilderOutputTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class NeedleDirectionType():
        """
        The needle direction 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", "Inside"
           "Outside", "Outside"
        """
        Inside = 0  # SectionAnalysisBuilderNeedleDirectionTypeMemberType
        Outside = 1  # SectionAnalysisBuilderNeedleDirectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CalculationMethodType():
        """
        The calculation method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Curvature", "Curvature"
           "RadiusofCurvature", "Radius of curvature"
        """
        Curvature = 0  # SectionAnalysisBuilderCalculationMethodTypeMemberType
        RadiusofCurvature = 1  # SectionAnalysisBuilderCalculationMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ScalingMethodType():
        """
        The scaling method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "Linear"
           "Logarithmic", "Logarithmic"
        """
        Linear = 0  # SectionAnalysisBuilderScalingMethodTypeMemberType
        Logarithmic = 1  # SectionAnalysisBuilderScalingMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    CalculationMethod: SectionAnalysisBuilderCalculationMethodType = ...
    """
    Returns or sets  the calculation method 
    
    <hr>
    
    Getter Method
    
    Signature ``CalculationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderCalculationMethodType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CalculationMethod`` 
    
    :param calculationMethod: 
    :type calculationMethod: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderCalculationMethodType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    CircularGrid: CircularGridBuilder = ...
    """
    Returns  the circular grid.  
    
    Only used when type is :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes.Circular <NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes>` 
    
    <hr>
    
    Getter Method
    
    Signature ``CircularGrid`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.CircularGridBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    CombOptions: NXOpen.GeometricUtilities.CombOptionsBuilder = ...
    """
    Returns  the comb options 
    
    <hr>
    
    Getter Method
    
    Signature ``CombOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.CombOptionsBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    NeedleDirection: SectionAnalysisBuilderNeedleDirectionType = ...
    """
    Returns or sets  the needle direction 
    
    <hr>
    
    Getter Method
    
    Signature ``NeedleDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderNeedleDirectionType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NeedleDirection`` 
    
    :param needleDirection: 
    :type needleDirection: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderNeedleDirectionType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Output: SectionAnalysisBuilderOutputType = ...
    """
    Returns or sets  the output 
    
    <hr>
    
    Getter Method
    
    Signature ``Output`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderOutputType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Output`` 
    
    :param output: 
    :type output: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderOutputType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    QuadrilateralGrid: QuadrilateralGridBuilder = ...
    """
    Returns  the quadrilateral grid.  
    
    Only used when type is :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes.Quadrilateral <NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes>` 
    
    <hr>
    
    Getter Method
    
    Signature ``QuadrilateralGrid`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.QuadrilateralGridBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    References: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the references (faces or faceted bodies) 
    
    <hr>
    
    Getter Method
    
    Signature ``References`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ScalingMethod: SectionAnalysisBuilderScalingMethodType = ...
    """
    Returns or sets  the scaling method 
    
    <hr>
    
    Getter Method
    
    Signature ``ScalingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderScalingMethodType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScalingMethod`` 
    
    :param scalingMethod: 
    :type scalingMethod: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderScalingMethodType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ShowInflectionPoints: bool = ...
    """
    Returns or sets  the flag to show the inflection points of planar sections 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowInflectionPoints`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowInflectionPoints`` 
    
    :param showInflectionPoints: 
    :type showInflectionPoints: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ShowPeakPoints: bool = ...
    """
    Returns or sets  the flag to show the peak points of the sections 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowPeakPoints`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowPeakPoints`` 
    
    :param showPeakPoints: 
    :type showPeakPoints: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ShowSectionLength: bool = ...
    """
    Returns or sets  the flag to show the section length labels 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowSectionLength`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowSectionLength`` 
    
    :param showSectionLength: 
    :type showSectionLength: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    TriangularGrid: TriangularGridBuilder = ...
    """
    Returns  the triangular grid.  
    
    Only used when type is :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes.Triangular <NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes>` 
    
    <hr>
    
    Getter Method
    
    Signature ``TriangularGrid`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.TriangularGridBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Type: SectionAnalysisBuilderTypes = ...
    """
    Returns or sets  the sectioning type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: SectionAnalysisBuilder = ...  # unknown typename


class ParallelPlanesExBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the Parallel Plane specification for a :py:class:`GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder`.  
    
    .. versionadded:: NX7.0.0
    """
    
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
    
    IsNumberEnabled: bool = ...
    """
    Returns or sets  a value indicating whether the number is used 
    
    <hr>
    
    Getter Method
    
    Signature ``IsNumberEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsNumberEnabled`` 
    
    :param isNumberEnabled: 
    :type isNumberEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsSpacingEnabled: bool = ...
    """
    Returns or sets  a value indicating whether the spacing is applied 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSpacingEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSpacingEnabled`` 
    
    :param isSpacingEnabled: 
    :type isSpacingEnabled: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Number: int = ...
    """
    Returns or sets  a value indicating how many sections should be created 
    
    <hr>
    
    Getter Method
    
    Signature ``Number`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Number`` 
    
    :param number: 
    :type number: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Offset: float = ...
    """
    Returns or sets  a value indicating the distance from the start position 
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Offset`` 
    
    :param offset: 
    :type offset: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Spacing: float = ...
    """
    Returns or sets  a value indicating the space between sections 
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Spacing`` 
    
    :param spacing: 
    :type spacing: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SpecifiedPlane: SectionPlaneBuilder = ...
    """
    Returns  the user specified section plane 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifiedPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Null: ParallelPlanesExBuilder = ...  # unknown typename


class SectionAnalysisExObject(NXOpen.GeometricAnalysis.AnalysisObject):
    """
    Represents a Section Analysis Object of the new version.  
    
    Section Analysis
    generates planar or isoparametric sections across faces and faceted bodies 
    to help evaluating sectional curvature flow of faces and surface quality and 
    characteristics in general. Section Analysis object update dynamically on geometry 
    changes of the sectioned faces and faceted bodies. 
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder`
    
    .. versionadded:: NX7.5.0
    """
    Null: SectionAnalysisExObject = ...  # unknown typename


class SectionAnalysisExBuilderPlacementTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisExBuilderPlacementType():
    """
    The types of the section placement
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Uniform", "Uniformly distributed"
       "ThroughPoints", "Through the specified points"
       "BetweenPoints", "Distributed between two specified points"
       "Interactive", "Interactively specified"
    """
    Uniform = 0  # SectionAnalysisExBuilderPlacementTypeMemberType
    ThroughPoints = 1  # SectionAnalysisExBuilderPlacementTypeMemberType
    BetweenPoints = 2  # SectionAnalysisExBuilderPlacementTypeMemberType
    Interactive = 3  # SectionAnalysisExBuilderPlacementTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisExBuilderAlignmentTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisExBuilderAlignmentType():
    """
    The section alignment type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "XYZPlane", "The cutting planes are perpendicular to X, Y or Z plane"
       "ParallelPlanes", "The cutting planes are parallel to a specified plane"
       "CurveAligned", "The cutting planes are perpendicular to specified curves"
       "Isoparametric", "The sections are along isoparametric lines"
       "Radial", "The cutting planes are distributed along a circle"
    """
    XYZPlane = 0  # SectionAnalysisExBuilderAlignmentTypeMemberType
    ParallelPlanes = 1  # SectionAnalysisExBuilderAlignmentTypeMemberType
    CurveAligned = 2  # SectionAnalysisExBuilderAlignmentTypeMemberType
    Isoparametric = 3  # SectionAnalysisExBuilderAlignmentTypeMemberType
    Radial = 4  # SectionAnalysisExBuilderAlignmentTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisExBuilderOutputTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisExBuilderOutputType():
    """
    The output options 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AnalysisObject", "Analysis Object"
       "SectionCurves", "section curves"
       "Both", "Both Analysis Object and section curves"
    """
    AnalysisObject = 0  # SectionAnalysisExBuilderOutputTypeMemberType
    SectionCurves = 1  # SectionAnalysisExBuilderOutputTypeMemberType
    Both = 2  # SectionAnalysisExBuilderOutputTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisExBuilderNeedleDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisExBuilderNeedleDirectionType():
    """
    The needle direction 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", "Inside"
       "Outside", "Outside"
    """
    Inside = 0  # SectionAnalysisExBuilderNeedleDirectionTypeMemberType
    Outside = 1  # SectionAnalysisExBuilderNeedleDirectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisExBuilderCalculationMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisExBuilderCalculationMethodType():
    """
    The calculation method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Curvature", "Curvature"
       "RadiusofCurvature", "Radius of curvature"
    """
    Curvature = 0  # SectionAnalysisExBuilderCalculationMethodTypeMemberType
    RadiusofCurvature = 1  # SectionAnalysisExBuilderCalculationMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisExBuilderScalingMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SectionAnalysisExBuilderScalingMethodType():
    """
    The scaling method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "Linear"
       "Logarithmic", "Logarithmic"
    """
    Linear = 0  # SectionAnalysisExBuilderScalingMethodTypeMemberType
    Logarithmic = 1  # SectionAnalysisExBuilderScalingMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SectionAnalysisExBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExObject` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateSectionAnalysisExBuilder`
    
    Default values.
    
    ==================================  =======================================
    Property                            Value
    ==================================  =======================================
    Alignment                           XYZPlane 
    ----------------------------------  ---------------------------------------
    CalculationMethod                   Curvature 
    ----------------------------------  ---------------------------------------
    CurveAligned.IsSpacingEnabled       0 
    ----------------------------------  ---------------------------------------
    CurveAligned.Number                 5 
    ----------------------------------  ---------------------------------------
    CurveAligned.Offset                 0 
    ----------------------------------  ---------------------------------------
    CurveAligned.Spacing                25 
    ----------------------------------  ---------------------------------------
    CurveAligned.SpecifiedPlane.Plane   View 
    ----------------------------------  ---------------------------------------
    CurveAligned.UseProjectedCurve      0 
    ----------------------------------  ---------------------------------------
    Interactive.IsCutInfiniteEnabled    0 
    ----------------------------------  ---------------------------------------
    IsShowInflectionPointsEnabled       0 
    ----------------------------------  ---------------------------------------
    IsShowLengthEnabled                 0 
    ----------------------------------  ---------------------------------------
    IsShowPeakPointsEnabled             0 
    ----------------------------------  ---------------------------------------
    Isoparametric.IsSpacingEnabled      0 
    ----------------------------------  ---------------------------------------
    Isoparametric.IsUEnabled            1 
    ----------------------------------  ---------------------------------------
    Isoparametric.IsVEnabled            1 
    ----------------------------------  ---------------------------------------
    Isoparametric.Number                5 
    ----------------------------------  ---------------------------------------
    Isoparametric.Spacing               25 
    ----------------------------------  ---------------------------------------
    NeedleDirection                     Outside 
    ----------------------------------  ---------------------------------------
    Output                              AnalysisObject 
    ----------------------------------  ---------------------------------------
    ParallelPlanes.IsNumberEnabled      0 
    ----------------------------------  ---------------------------------------
    ParallelPlanes.IsSpacingEnabled     0 
    ----------------------------------  ---------------------------------------
    ParallelPlanes.Number               5 
    ----------------------------------  ---------------------------------------
    ParallelPlanes.Offset               0 
    ----------------------------------  ---------------------------------------
    ParallelPlanes.Spacing              50 (millimeters part), 2 (inches part) 
    ----------------------------------  ---------------------------------------
    Placement                           Uniform 
    ----------------------------------  ---------------------------------------
    Radial.IsSpacingEnabled             0 
    ----------------------------------  ---------------------------------------
    Radial.Number                       5 
    ----------------------------------  ---------------------------------------
    Radial.Offset                       0 
    ----------------------------------  ---------------------------------------
    Radial.RotationAxis                 View 
    ----------------------------------  ---------------------------------------
    Radial.Spacing                      72 
    ----------------------------------  ---------------------------------------
    ScalingMethod                       Linear 
    ----------------------------------  ---------------------------------------
    XYZPlane.IsNumberEnabled            0 
    ----------------------------------  ---------------------------------------
    XYZPlane.IsSpacingEnabled           0 
    ----------------------------------  ---------------------------------------
    XYZPlane.IsXEnabled                 1 
    ----------------------------------  ---------------------------------------
    XYZPlane.IsYEnabled                 1 
    ----------------------------------  ---------------------------------------
    XYZPlane.IsZEnabled                 1 
    ----------------------------------  ---------------------------------------
    XYZPlane.Number                     5 
    ----------------------------------  ---------------------------------------
    XYZPlane.Spacing                    50 (millimeters part), 2 (inches part) 
    ==================================  =======================================
    
    .. versionadded:: NX7.0.0
    """
    
    class PlacementType():
        """
        The types of the section placement
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Uniform", "Uniformly distributed"
           "ThroughPoints", "Through the specified points"
           "BetweenPoints", "Distributed between two specified points"
           "Interactive", "Interactively specified"
        """
        Uniform = 0  # SectionAnalysisExBuilderPlacementTypeMemberType
        ThroughPoints = 1  # SectionAnalysisExBuilderPlacementTypeMemberType
        BetweenPoints = 2  # SectionAnalysisExBuilderPlacementTypeMemberType
        Interactive = 3  # SectionAnalysisExBuilderPlacementTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class AlignmentType():
        """
        The section alignment type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "XYZPlane", "The cutting planes are perpendicular to X, Y or Z plane"
           "ParallelPlanes", "The cutting planes are parallel to a specified plane"
           "CurveAligned", "The cutting planes are perpendicular to specified curves"
           "Isoparametric", "The sections are along isoparametric lines"
           "Radial", "The cutting planes are distributed along a circle"
        """
        XYZPlane = 0  # SectionAnalysisExBuilderAlignmentTypeMemberType
        ParallelPlanes = 1  # SectionAnalysisExBuilderAlignmentTypeMemberType
        CurveAligned = 2  # SectionAnalysisExBuilderAlignmentTypeMemberType
        Isoparametric = 3  # SectionAnalysisExBuilderAlignmentTypeMemberType
        Radial = 4  # SectionAnalysisExBuilderAlignmentTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OutputType():
        """
        The output options 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AnalysisObject", "Analysis Object"
           "SectionCurves", "section curves"
           "Both", "Both Analysis Object and section curves"
        """
        AnalysisObject = 0  # SectionAnalysisExBuilderOutputTypeMemberType
        SectionCurves = 1  # SectionAnalysisExBuilderOutputTypeMemberType
        Both = 2  # SectionAnalysisExBuilderOutputTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class NeedleDirectionType():
        """
        The needle direction 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", "Inside"
           "Outside", "Outside"
        """
        Inside = 0  # SectionAnalysisExBuilderNeedleDirectionTypeMemberType
        Outside = 1  # SectionAnalysisExBuilderNeedleDirectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CalculationMethodType():
        """
        The calculation method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Curvature", "Curvature"
           "RadiusofCurvature", "Radius of curvature"
        """
        Curvature = 0  # SectionAnalysisExBuilderCalculationMethodTypeMemberType
        RadiusofCurvature = 1  # SectionAnalysisExBuilderCalculationMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ScalingMethodType():
        """
        The scaling method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "Linear"
           "Logarithmic", "Logarithmic"
        """
        Linear = 0  # SectionAnalysisExBuilderScalingMethodTypeMemberType
        Logarithmic = 1  # SectionAnalysisExBuilderScalingMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Alignment: SectionAnalysisExBuilderAlignmentType = ...
    """
    Returns or sets  the alignment type 
    
    <hr>
    
    Getter Method
    
    Signature ``Alignment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Alignment`` 
    
    :param alignment: 
    :type alignment: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    CalculationMethod: SectionAnalysisExBuilderCalculationMethodType = ...
    """
    Returns or sets  the calculation method 
    
    <hr>
    
    Getter Method
    
    Signature ``CalculationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderCalculationMethodType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CalculationMethod`` 
    
    :param calculationMethod: 
    :type calculationMethod: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderCalculationMethodType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    CombOptions: NXOpen.GeometricUtilities.CombOptionsBuilder = ...
    """
    Returns  the comb options specification
    
    <hr>
    
    Getter Method
    
    Signature ``CombOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.CombOptionsBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    CurveAligned: CurveAlignedBuilder = ...
    """
    Returns  the Curve Aligned section specification.  
    
    Only used when type is :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType.CurveAligned <NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``CurveAligned`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.CurveAlignedBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Interactive: InteractiveBuilder = ...
    """
    Returns  the Interactive placement specification.  
    
    Only used when type is :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderPlacementType.Interactive <NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderPlacementType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``Interactive`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.InteractiveBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    IsShowInflectionPointsEnabled: bool = ...
    """
    Returns or sets  a value indicating whether to show the inflection points 
    
    <hr>
    
    Getter Method
    
    Signature ``IsShowInflectionPointsEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsShowInflectionPointsEnabled`` 
    
    :param inflection: 
    :type inflection: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsShowLengthEnabled: bool = ...
    """
    Returns or sets  a value indicating whether to show the length of each section curve 
    
    <hr>
    
    Getter Method
    
    Signature ``IsShowLengthEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsShowLengthEnabled`` 
    
    :param length: 
    :type length: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsShowPeakPointsEnabled: bool = ...
    """
    Returns or sets  a value indicating whether to show the peak points 
    
    <hr>
    
    Getter Method
    
    Signature ``IsShowPeakPointsEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsShowPeakPointsEnabled`` 
    
    :param peak: 
    :type peak: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Isoparametric: IsoparametricBuilder = ...
    """
    Returns  the Isoparametric section specification.  
    
    Only used when type is :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType.Isoparametric <NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``Isoparametric`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.IsoparametricBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    NeedleDirection: SectionAnalysisExBuilderNeedleDirectionType = ...
    """
    Returns or sets  the needle direction 
    
    <hr>
    
    Getter Method
    
    Signature ``NeedleDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderNeedleDirectionType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NeedleDirection`` 
    
    :param needleDirection: 
    :type needleDirection: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderNeedleDirectionType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Output: SectionAnalysisExBuilderOutputType = ...
    """
    Returns or sets  the output 
    
    <hr>
    
    Getter Method
    
    Signature ``Output`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderOutputType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Output`` 
    
    :param output: 
    :type output: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderOutputType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ParallelPlanes: ParallelPlanesExBuilder = ...
    """
    Returns  the Parallel Planes section specification.  
    
    Only used when type is :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType.ParallelPlanes <NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``ParallelPlanes`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.ParallelPlanesExBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Placement: SectionAnalysisExBuilderPlacementType = ...
    """
    Returns or sets  the placement 
    
    <hr>
    
    Getter Method
    
    Signature ``Placement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderPlacementType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Placement`` 
    
    :param placement: 
    :type placement: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderPlacementType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Radial: RadialBuilder = ...
    """
    Returns  the Radial section specification.  
    
    Only used when type is :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType.CurveAligned <NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``Radial`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    ScalingMethod: SectionAnalysisExBuilderScalingMethodType = ...
    """
    Returns or sets  the scaling method 
    
    <hr>
    
    Getter Method
    
    Signature ``ScalingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderScalingMethodType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScalingMethod`` 
    
    :param scalingMethod: 
    :type scalingMethod: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderScalingMethodType` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SelectObject: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    SpecifyPoint: NXOpen.SelectPointList = ...
    """
    Returns  the specified points 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifyPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectPointList` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    XYZPlane: XYZPlaneBuilder = ...
    """
    Returns  the XYZ Planes section specification.  
    
    Only used when type is :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType.XYZPlane <NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``XYZPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.XYZPlaneBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Null: SectionAnalysisExBuilder = ...  # unknown typename


