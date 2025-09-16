# module 'NXOpen.GeometricAnalysis'
#
# Automatically generated 2025-06-09T14:38:46.696429
#
"""Default documentation for NXOpen.GeometricAnalysis."""

import typing

import NXOpen
import NXOpen.Features
import NXOpen.GeometricAnalysis.SectionAnalysis
import NXOpen.GeometricUtilities



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class AnalysisObject(NXOpen.DisplayableObject):
    """
    Represents an Analysis Object     
    
    This is an abstract class, and cannot be instantiated
    
    .. versionadded:: NX5.0.0
    """
    Null: AnalysisObject = ...  # unknown typename


class FaceAnalysis(AnalysisObject):
    """
    Represents a face analysis    
    
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder`
    
    .. versionadded:: NX11.0.0
    """
    Null: FaceAnalysis = ...  # unknown typename


class SectionAnalysisObject(AnalysisObject):
    """
    Represents a Section Analysis object.  
    
    Section Analysis
    generates planar, circular, or isoparametric sections across faces and faceted bodies 
    to help evaluating sectional curvature flow of faces and surface quality and 
    characteristics in general. Section Analysis object update dynamically on geometry 
    changes of the sectioned faces and faceted bodies. 
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: SectionAnalysisObject = ...  # unknown typename


class SlopeAnalysisBuilderDisplayModesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SlopeAnalysisBuilderDisplayModes():
    """
    The display type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fringe", " - "
       "Hedgehog", " - "
       "ContourLines", " - "
    """
    Fringe = 0  # SlopeAnalysisBuilderDisplayModesMemberType
    Hedgehog = 1  # SlopeAnalysisBuilderDisplayModesMemberType
    ContourLines = 2  # SlopeAnalysisBuilderDisplayModesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SlopeAnalysisBuilder(NXOpen.Builder):
    """
    Represents a Slope Analysis builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollectionEx.CreateSlopeAnalysisBuilder`
    
    Default values.
    
    =================================================  ===========================================
    Property                                           Value
    =================================================  ===========================================
    DataRange.IsFixed                                  1 
    -------------------------------------------------  -------------------------------------------
    DataRange.Max                                      0.010000 
    -------------------------------------------------  -------------------------------------------
    DataRange.Middle                                   0.000000 
    -------------------------------------------------  -------------------------------------------
    DataRange.MiddleScale                              0.000000 
    -------------------------------------------------  -------------------------------------------
    DataRange.Min                                      -0.010000 
    -------------------------------------------------  -------------------------------------------
    DataRange.ZoomScale                                8 
    -------------------------------------------------  -------------------------------------------
    DisplayMode                                        Fringe 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.CanShowFacet                       0 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.ColorLegendOption                  Blend 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.AngleTolerance   15.0 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.EdgeTolerance    0.005 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.FaceTolerance    0.005 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.Resolution       Standard 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.WidthTolerance   0.3 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.NumberOfColors                     Seven 
    -------------------------------------------------  -------------------------------------------
    NumberOfContourLines                               8 
    -------------------------------------------------  -------------------------------------------
    SpikeLength                                        25.4 (millimeters part), 1.0 (inches part) 
    =================================================  ===========================================
    
    .. versionadded:: NX11.0.0
    """
    
    class DisplayModes():
        """
        The display type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Fringe", " - "
           "Hedgehog", " - "
           "ContourLines", " - "
        """
        Fringe = 0  # SlopeAnalysisBuilderDisplayModesMemberType
        Hedgehog = 1  # SlopeAnalysisBuilderDisplayModesMemberType
        ContourLines = 2  # SlopeAnalysisBuilderDisplayModesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreatePMILabel(self, location: NXOpen.Point3d, face: NXOpen.DisplayableObject) -> None:
        """
        Create a PMI label.  
        
        Signature ``CreatePMILabel(location, face)`` 
        
        :param location:  the loction on the face to create a PMI label.  
        :type location: :py:class:`NXOpen.Point3d` 
        :param face:  the selected face to create a PMI label.  
        :type face: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def StartSlopeAnalysis(self) -> None:
        """
        Start slope analysis.  
        
        Signature ``StartSlopeAnalysis()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    DataRange: FaceAnalysisDataRangeBuilder = ...
    """
    Returns  the slope analysis data range.  
    
    <hr>
    
    Getter Method
    
    Signature ``DataRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DisplayMode: SlopeAnalysisBuilderDisplayModes = ...
    """
    Returns or sets  the display mode.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SlopeAnalysisBuilderDisplayModes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayMode`` 
    
    :param displayMode: 
    :type displayMode: :py:class:`NXOpen.GeometricAnalysis.SlopeAnalysisBuilderDisplayModes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DisplaySettings: FaceAnalysisDisplayBuilder = ...
    """
    Returns  the slope analysis display settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplaySettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Faces: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the face to apply slope analysis.  
    
    <hr>
    
    Getter Method
    
    Signature ``Faces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Normals: FaceAnalysisNormalsBuilder = ...
    """
    Returns  the slope analysis normals.  
    
    <hr>
    
    Getter Method
    
    Signature ``Normals`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    NumberOfContourLines: int = ...
    """
    Returns or sets  the number of contour lines.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfContourLines`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfContourLines`` 
    
    :param numberOfContourLines: 
    :type numberOfContourLines: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    PmiPoint: NXOpen.SelectNXObjectList = ...
    """
    Returns  the point to draw labels.  
    
    <hr>
    
    Getter Method
    
    Signature ``PmiPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    SpikeLength: float = ...
    """
    Returns or sets  the spike length.  
    
    <hr>
    
    Getter Method
    
    Signature ``SpikeLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpikeLength`` 
    
    :param spikeLength: 
    :type spikeLength: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the reference vector used for slope analysis.  
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vector: 
    :type vector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: SlopeAnalysisBuilder = ...  # unknown typename


class FaceAnalysisDataRangeBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents data range functions used by Face Analysis.  
    
    .. versionadded:: NX11.0.0
    """
    
    def ResetData(self) -> None:
        """
        Resets data range.  
        
        Signature ``ResetData()`` 
        
        .. versionadded:: NX11.0.0
        
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
    
    IsFixed: bool = ...
    """
    Returns or sets  the value indicating the range is fixed or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsFixed`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsFixed`` 
    
    :param isFixed: 
    :type isFixed: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Max: float = ...
    """
    Returns or sets  the maximum data range.  
    
    <hr>
    
    Getter Method
    
    Signature ``Max`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Max`` 
    
    :param max: 
    :type max: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Middle: float = ...
    """
    Returns or sets  the middle data range value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Middle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Middle`` 
    
    :param middle: 
    :type middle: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MiddleScale: float = ...
    """
    Returns or sets  the middle value scale for data range.  
    
    <hr>
    
    Getter Method
    
    Signature ``MiddleScale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MiddleScale`` 
    
    :param middleScale: 
    :type middleScale: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Min: float = ...
    """
    Returns or sets  the minimum data range.  
    
    <hr>
    
    Getter Method
    
    Signature ``Min`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Min`` 
    
    :param min: 
    :type min: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ZoomScale: float = ...
    """
    Returns or sets  the zoom scale.  
    
    <hr>
    
    Getter Method
    
    Signature ``ZoomScale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZoomScale`` 
    
    :param scaleSlider: 
    :type scaleSlider: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: FaceAnalysisDataRangeBuilder = ...  # unknown typename


class GapFlushness(AnalysisObject):
    """
    Gap and Flushness analysis object class   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: GapFlushness = ...  # unknown typename


class DraftAnalysis(AnalysisObject):
    """
    Represents a Draft Analysis builder   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.DraftAnalysisBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: DraftAnalysis = ...  # unknown typename


class HighlightLinesAnalysis(AnalysisObject):
    """
    Represents a Highlight Lines Analysis object.  
    
    Highlight Lines
    Analysis function can produce both reflection lines and projection
    lines which are used to evaluate the surface quality and
    continuity between adjacent surfaces. 
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: HighlightLinesAnalysis = ...  # unknown typename


class GeometricPropertiesEdge_Struct():
    """
    Edge/Curve Geometric Properties .  
    
    Constructor: 
    NXOpen.GeometricAnalysis.GeometricProperties.Edge()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    ParameterPercentage: float = ...
    """
    Curve Parameter Percentage 
    <hr>
    
    Field Value
    Type:float
    """
    Parameter: float = ...
    """
    Curve Parameter
    <hr>
    
    Field Value
    Type:float
    """
    PositionInWcs: NXOpen.Point3d = ...
    """
    XYZ Position in Work Part coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    Position: NXOpen.Point3d = ...
    """
    XYZ Position in Root Part coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    TangentInWcs: NXOpen.Vector3d = ...
    """
    Tangent Vector in Work Part coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    Tangent: NXOpen.Vector3d = ...
    """
    Tangent Vector in Root Part coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    NormalInWcs: NXOpen.Vector3d = ...
    """
    Curve Normal in Work Part coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    Normal: NXOpen.Vector3d = ...
    """
    Curve Normal in Root Part coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    BinormalInWcs: NXOpen.Vector3d = ...
    """
    Curve Binormal in Work Part coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    Binormal: NXOpen.Vector3d = ...
    """
    Curve Binormal in Root Part coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    Torsion: float = ...
    """
    Curve Torsion
    <hr>
    
    Field Value
    Type:float
    """
    Curvature: float = ...
    """
    Curvature of the Curve
    <hr>
    
    Field Value
    Type:float
    """


class SurfaceIntersection(AnalysisObject):
    """
    Represents a SurfaceIntersection builder   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder`
    
    .. versionadded:: NX7.5.0
    """
    Null: SurfaceIntersection = ...  # unknown typename


class DistanceAnalysisBuilderDisplayModesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DistanceAnalysisBuilderDisplayModes():
    """
    The display type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fringe", "Display in fringe."
       "Hedgehog", "Display in hedgehog."
       "ContourLines", "Display in contour lines."
    """
    Fringe = 0  # DistanceAnalysisBuilderDisplayModesMemberType
    Hedgehog = 1  # DistanceAnalysisBuilderDisplayModesMemberType
    ContourLines = 2  # DistanceAnalysisBuilderDisplayModesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DistanceAnalysisBuilder(NXOpen.Builder):
    """
    Represents a Distance Analysis builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollectionEx.CreateDistanceAnalysisBuilder`
    
    Default values.
    
    =================================================  ===========================================
    Property                                           Value
    =================================================  ===========================================
    DataRange.IsFixed                                  1 
    -------------------------------------------------  -------------------------------------------
    DataRange.Max                                      0.010000 
    -------------------------------------------------  -------------------------------------------
    DataRange.Middle                                   0.000000 
    -------------------------------------------------  -------------------------------------------
    DataRange.MiddleScale                              0.000000 
    -------------------------------------------------  -------------------------------------------
    DataRange.Min                                      -0.010000 
    -------------------------------------------------  -------------------------------------------
    DataRange.ZoomScale                                8 
    -------------------------------------------------  -------------------------------------------
    DisplayMode                                        Fringe 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.CanShowFacet                       0 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.ColorLegendOption                  Blend 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.AngleTolerance   15.0 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.EdgeTolerance    0.005 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.FaceTolerance    0.005 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.Resolution       Standard 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.WidthTolerance   0.3 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.NumberOfColors                     Seven 
    -------------------------------------------------  -------------------------------------------
    NumberOfContourLines                               8 
    -------------------------------------------------  -------------------------------------------
    SpikeLength                                        25.4 (millimeters part), 1.0 (inches part) 
    =================================================  ===========================================
    
    .. versionadded:: NX11.0.0
    """
    
    class DisplayModes():
        """
        The display type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Fringe", "Display in fringe."
           "Hedgehog", "Display in hedgehog."
           "ContourLines", "Display in contour lines."
        """
        Fringe = 0  # DistanceAnalysisBuilderDisplayModesMemberType
        Hedgehog = 1  # DistanceAnalysisBuilderDisplayModesMemberType
        ContourLines = 2  # DistanceAnalysisBuilderDisplayModesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def UpdateDisplayOnPlaneChange(self) -> None:
        """
        Update display after plane changes.  
        
        Signature ``UpdateDisplayOnPlaneChange()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def StartDistanceAnalysis(self) -> None:
        """
        Start distance analysis.  
        
        Signature ``StartDistanceAnalysis()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    DataRange: FaceAnalysisDataRangeBuilder = ...
    """
    Returns  the distance analysis data range.  
    
    <hr>
    
    Getter Method
    
    Signature ``DataRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DisplayMode: DistanceAnalysisBuilderDisplayModes = ...
    """
    Returns or sets  the display mode.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DistanceAnalysisBuilderDisplayModes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayMode`` 
    
    :param displayMode: 
    :type displayMode: :py:class:`NXOpen.GeometricAnalysis.DistanceAnalysisBuilderDisplayModes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DisplaySettings: FaceAnalysisDisplayBuilder = ...
    """
    Returns  the distance analysis display settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplaySettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Faces: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the face to apply distance analysis.  
    
    <hr>
    
    Getter Method
    
    Signature ``Faces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Normals: FaceAnalysisNormalsBuilder = ...
    """
    Returns  the distance analysis normals.  
    
    <hr>
    
    Getter Method
    
    Signature ``Normals`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    NumberOfContourLines: int = ...
    """
    Returns or sets  the number of contour lines.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfContourLines`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfContourLines`` 
    
    :param numberOfContourLines: 
    :type numberOfContourLines: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the reference plane for distance analysis.  
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    SpikeLength: float = ...
    """
    Returns or sets  the spike length.  
    
    <hr>
    
    Getter Method
    
    Signature ``SpikeLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpikeLength`` 
    
    :param spikeLength: 
    :type spikeLength: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: DistanceAnalysisBuilder = ...  # unknown typename


class SolidDensityUnitsTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SolidDensityUnitsType():
    """
    Types of units for solid density 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PoundsPerCubicInches", "lbm/in^3"
       "PoundsPerCubicFeet", "lbm/ft^3"
       "GramsPerCubicCentimeters", "g/cm^3"
       "KilogramsPerCubicMeters", "kg/m^3"
    """
    PoundsPerCubicInches = 0  # SolidDensityUnitsTypeMemberType
    PoundsPerCubicFeet = 1  # SolidDensityUnitsTypeMemberType
    GramsPerCubicCentimeters = 2  # SolidDensityUnitsTypeMemberType
    KilogramsPerCubicMeters = 3  # SolidDensityUnitsTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SolidDensity(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.GeometricAnalysis.SolidDensity`
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisManager.CreateSolidDensityObject`
    
    .. versionadded:: NX5.0.0
    """
    
    class UnitsType():
        """
        Types of units for solid density 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PoundsPerCubicInches", "lbm/in^3"
           "PoundsPerCubicFeet", "lbm/ft^3"
           "GramsPerCubicCentimeters", "g/cm^3"
           "KilogramsPerCubicMeters", "kg/m^3"
        """
        PoundsPerCubicInches = 0  # SolidDensityUnitsTypeMemberType
        PoundsPerCubicFeet = 1  # SolidDensityUnitsTypeMemberType
        GramsPerCubicCentimeters = 2  # SolidDensityUnitsTypeMemberType
        KilogramsPerCubicMeters = 3  # SolidDensityUnitsTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Density: float = ...
    """
    Returns or sets  the Solid Density.  
    
    :py:meth:`NXOpen.GeometricAnalysis.SolidDensity.Units` must be specified before
    specifying the density. When :py:meth:`NXOpen.GeometricAnalysis.SolidDensity.Units` is changed, 
    :py:meth:`NXOpen.GeometricAnalysis.SolidDensity.Density` value is recomputed to reflect the change
    in units. Set :py:meth:`NXOpen.GeometricAnalysis.SolidDensity.Units` first, then
    :py:meth:`NXOpen.GeometricAnalysis.SolidDensity.Density` to set specify the density along
    with its units. 
    
    <hr>
    
    Getter Method
    
    Signature ``Density`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Density`` 
    
    :param density: 
    :type density: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Solids: NXOpen.SelectObjectList = ...
    """
    Returns  the solids to set density for 
    
    <hr>
    
    Getter Method
    
    Signature ``Solids`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectObjectList` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Units: SolidDensityUnitsType = ...
    """
    Returns or sets  the density units for :py:class:`NXOpen.GeometricAnalysis.SolidDensity`.  
    
    When :py:meth:`NXOpen.GeometricAnalysis.SolidDensity.Units` is changed, :py:meth:`NXOpen.GeometricAnalysis.SolidDensity.Density`
    value is recomputed to reflect the change in units. Set
    :py:meth:`NXOpen.GeometricAnalysis.SolidDensity.Units` first, then
    :py:meth:`NXOpen.GeometricAnalysis.SolidDensity.Density` to set specify the density with
    units. 
    
    <hr>
    
    Getter Method
    
    Signature ``Units`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SolidDensityUnitsType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Units`` 
    
    :param units:  Type of Units  
    :type units: :py:class:`NXOpen.GeometricAnalysis.SolidDensityUnitsType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: SolidDensity = ...  # unknown typename


class CurveAnalysisInflectionsBuilderDirectionOptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveAnalysisInflectionsBuilderDirectionOptionType():
    """
    Direction option types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "no direction"
       "PlaneOfCurve", "best fit plane"
       "SpecifyVector", "specify vector"
       "WorkView", "work view"
    """
    NotSet = 0  # CurveAnalysisInflectionsBuilderDirectionOptionTypeMemberType
    PlaneOfCurve = 1  # CurveAnalysisInflectionsBuilderDirectionOptionTypeMemberType
    SpecifyVector = 2  # CurveAnalysisInflectionsBuilderDirectionOptionTypeMemberType
    WorkView = 3  # CurveAnalysisInflectionsBuilderDirectionOptionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveAnalysisInflectionsBuilder(NXOpen.Builder):
    """
    This class handles the options setting for the curve analysis information (Inflections) display.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateCurveAnalysisInflectionsBuilder`
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX8.5.0
       Use :py:class:`GeometricAnalysis.CurveCurvatureAnalysisBuilder`.
    """
    
    class DirectionOptionType():
        """
        Direction option types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "no direction"
           "PlaneOfCurve", "best fit plane"
           "SpecifyVector", "specify vector"
           "WorkView", "work view"
        """
        NotSet = 0  # CurveAnalysisInflectionsBuilderDirectionOptionTypeMemberType
        PlaneOfCurve = 1  # CurveAnalysisInflectionsBuilderDirectionOptionTypeMemberType
        SpecifyVector = 2  # CurveAnalysisInflectionsBuilderDirectionOptionTypeMemberType
        WorkView = 3  # CurveAnalysisInflectionsBuilderDirectionOptionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreatePoints(self) -> 'list[NXOpen.Point]':
        """
        Create points at the infections of the curve  
        
        Signature ``CreatePoints()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Point` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    DirectionOption: CurveAnalysisInflectionsBuilderDirectionOptionType = ...
    """
    Returns or sets  the direction option 
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisInflectionsBuilderDirectionOptionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionOption`` 
    
    :param option: 
    :type option: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisInflectionsBuilderDirectionOptionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SelectedCurves: NXOpen.ScCollector = ...
    """
    Returns  the selected curves 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedCurves`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the vector 
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vect: 
    :type vect: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Null: CurveAnalysisInflectionsBuilder = ...  # unknown typename


class GeometricPropertiesFace_Struct():
    """
    Face Geometric Properties .  
    
    Constructor: 
    NXOpen.GeometricAnalysis.GeometricProperties.Face()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    UParamater: float = ...
    """
    U parameter 
    <hr>
    
    Field Value
    Type:float
    """
    VParamater: float = ...
    """
    V parameter 
    <hr>
    
    Field Value
    Type:float
    """
    PositionInWcs: NXOpen.Point3d = ...
    """
    XYZ Position in Work Part coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    UDerivativeInWcs: NXOpen.Vector3d = ...
    """
    Derivative Vector in U direction - Work Part  Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    VDerivativeInWcs: NXOpen.Vector3d = ...
    """
    Derivative Vector in V direction - Work Part  Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    NormalInWcs: NXOpen.Vector3d = ...
    """
    Unitized Face Normal - Work Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    Position: NXOpen.Point3d = ...
    """
    XYZ Position 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    UDerivative: NXOpen.Vector3d = ...
    """
    Derivative Vector in U direction -  Root Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    VDerivative: NXOpen.Vector3d = ...
    """
    Derivative Vector in V direction - Root Part  Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    Normal: NXOpen.Vector3d = ...
    """
    Unitized Face Normal - Root Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    InvOfMinRadiusOfCurvature: float = ...
    """
    Inverse of Minumum  Radius of
    Curvature, 1/(minimum radius of curvature) 
    <hr>
    
    Field Value
    Type:float
    """
    InvOfMaxRadiusOfCurvature: float = ...
    """
    Inverse of Maximum Radius of
    Curvature,  1/(maximum radius of curvature).  
    
    <hr>
    
    Field Value
    Type:float
    """


class ReflectionAnalysisBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReflectionAnalysisBuilderTypes():
    """
    The types of images. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "LineImages", "Line image."
       "SceneImages", "Scene image."
       "ImageFromFile", "Image from file."
    """
    LineImages = 0  # ReflectionAnalysisBuilderTypesMemberType
    SceneImages = 1  # ReflectionAnalysisBuilderTypesMemberType
    ImageFromFile = 2  # ReflectionAnalysisBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ReflectionAnalysisBuilderLineImageTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReflectionAnalysisBuilderLineImageTypes():
    """
    The line image types. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BlackLines", "Black lines."
       "BlackandWhiteLines", "Black and lines."
       "ColoredLines", "Colored lines."
    """
    BlackLines = 0  # ReflectionAnalysisBuilderLineImageTypesMemberType
    BlackandWhiteLines = 1  # ReflectionAnalysisBuilderLineImageTypesMemberType
    ColoredLines = 2  # ReflectionAnalysisBuilderLineImageTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReflectionAnalysisBuilderNumberOfLinesOptions():
    """
    The number of reflection lines. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "One", "1 reflection line."
       "Two", "2 reflection line."
       "Four", "4 reflection line."
       "Eight", "8 reflection line."
       "Sixteen", "16 reflection line."
       "ThirtyTwo", "32 reflection line."
       "SixtyFour", "64 reflection line."
       "OneTwoEight", "128 reflection line."
       "TwoFiveSix", "256 reflection line."
    """
    One = 0  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
    Two = 1  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
    Four = 2  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
    Eight = 3  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
    Sixteen = 4  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
    ThirtyTwo = 5  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
    SixtyFour = 6  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
    OneTwoEight = 7  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
    TwoFiveSix = 8  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ReflectionAnalysisBuilderLineOrientationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReflectionAnalysisBuilderLineOrientationType():
    """
    The reflection line orientation. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Horizontal", "Horizontal."
       "Vertical", "Vertical."
       "Both", "Both horizontal and vertical."
    """
    Horizontal = 0  # ReflectionAnalysisBuilderLineOrientationTypeMemberType
    Vertical = 1  # ReflectionAnalysisBuilderLineOrientationTypeMemberType
    Both = 2  # ReflectionAnalysisBuilderLineOrientationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ReflectionAnalysisBuilderLineThicknessTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReflectionAnalysisBuilderLineThicknessType():
    """
    The reflection line thickness. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Thin", "Thin."
       "Normal", "Normal."
       "Thick", "Thick."
    """
    Thin = 0  # ReflectionAnalysisBuilderLineThicknessTypeMemberType
    Normal = 1  # ReflectionAnalysisBuilderLineThicknessTypeMemberType
    Thick = 2  # ReflectionAnalysisBuilderLineThicknessTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ReflectionAnalysisBuilderSceneImageTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReflectionAnalysisBuilderSceneImageType():
    """
    The reflection scene images. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SimulatedHorizon", "Simulated horizon."
       "PhotoHorizon", "Photo horizon."
       "SphericalRoom", "Spherical room."
       "SphericalLightTubesRoom", "Spherical light tubes room."
       "DaytimeHorizon", "Daytime horizon."
       "MagentaSunset", "Magenta sunset."
       "SphericalHorizon", "Spherical horizon."
       "CylindricalRoom", "Cylindrical room."
       "MonochromeHorizon", "Monochrome horizon."
       "SmoothGrayScale", "Smooth gray scale."
       "SharpGrayScale", "Sharp gray scale."
       "SphericalTubes", "Spherical tubes."
    """
    SimulatedHorizon = 0  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    PhotoHorizon = 1  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    SphericalRoom = 2  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    SphericalLightTubesRoom = 3  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    DaytimeHorizon = 4  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    MagentaSunset = 5  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    SphericalHorizon = 6  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    CylindricalRoom = 7  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    MonochromeHorizon = 8  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    SmoothGrayScale = 9  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    SharpGrayScale = 10  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    SphericalTubes = 11  # ReflectionAnalysisBuilderSceneImageTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ReflectionAnalysisBuilderImageMovementTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReflectionAnalysisBuilderImageMovementTypes():
    """
    The type of image movement. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Horizontal", "Move image in horizonal direction."
       "Vertical", "Move image in vertical direction."
       "Rotate", "Rotate image."
    """
    Horizontal = 0  # ReflectionAnalysisBuilderImageMovementTypesMemberType
    Vertical = 1  # ReflectionAnalysisBuilderImageMovementTypesMemberType
    Rotate = 2  # ReflectionAnalysisBuilderImageMovementTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ReflectionAnalysisBuilderImageSizeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReflectionAnalysisBuilderImageSizeOption():
    """
    The reflection image size option. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "KeepCurrent", "Keep current size."
       "ReduceScale", "Reduce scale size."
    """
    KeepCurrent = 0  # ReflectionAnalysisBuilderImageSizeOptionMemberType
    ReduceScale = 1  # ReflectionAnalysisBuilderImageSizeOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ReflectionAnalysisBuilder(NXOpen.Builder):
    """
    Represents a Reflection Analysis builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollectionEx.CreateReflectionAnalysisBuilder`
    
    Default values.
    
    =================================  ==========
    Property                           Value
    =================================  ==========
    DisplayResolution.AngleTolerance   15.0 
    ---------------------------------  ----------
    DisplayResolution.EdgeTolerance    0.005 
    ---------------------------------  ----------
    DisplayResolution.FaceTolerance    0.005 
    ---------------------------------  ----------
    DisplayResolution.Resolution       Standard 
    ---------------------------------  ----------
    DisplayResolution.WidthTolerance   0.3 
    ---------------------------------  ----------
    FaceReflectivityScale              100 
    ---------------------------------  ----------
    ImagePosition                      0 
    ---------------------------------  ----------
    LineNumber                         ThirtyTwo 
    ---------------------------------  ----------
    ShowFacetEdge                      0 
    =================================  ==========
    
    .. versionadded:: NX11.0.0
    """
    
    class Types():
        """
        The types of images. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "LineImages", "Line image."
           "SceneImages", "Scene image."
           "ImageFromFile", "Image from file."
        """
        LineImages = 0  # ReflectionAnalysisBuilderTypesMemberType
        SceneImages = 1  # ReflectionAnalysisBuilderTypesMemberType
        ImageFromFile = 2  # ReflectionAnalysisBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LineImageTypes():
        """
        The line image types. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BlackLines", "Black lines."
           "BlackandWhiteLines", "Black and lines."
           "ColoredLines", "Colored lines."
        """
        BlackLines = 0  # ReflectionAnalysisBuilderLineImageTypesMemberType
        BlackandWhiteLines = 1  # ReflectionAnalysisBuilderLineImageTypesMemberType
        ColoredLines = 2  # ReflectionAnalysisBuilderLineImageTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class NumberOfLinesOptions():
        """
        The number of reflection lines. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "One", "1 reflection line."
           "Two", "2 reflection line."
           "Four", "4 reflection line."
           "Eight", "8 reflection line."
           "Sixteen", "16 reflection line."
           "ThirtyTwo", "32 reflection line."
           "SixtyFour", "64 reflection line."
           "OneTwoEight", "128 reflection line."
           "TwoFiveSix", "256 reflection line."
        """
        One = 0  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
        Two = 1  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
        Four = 2  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
        Eight = 3  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
        Sixteen = 4  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
        ThirtyTwo = 5  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
        SixtyFour = 6  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
        OneTwoEight = 7  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
        TwoFiveSix = 8  # ReflectionAnalysisBuilderNumberOfLinesOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LineOrientationType():
        """
        The reflection line orientation. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Horizontal", "Horizontal."
           "Vertical", "Vertical."
           "Both", "Both horizontal and vertical."
        """
        Horizontal = 0  # ReflectionAnalysisBuilderLineOrientationTypeMemberType
        Vertical = 1  # ReflectionAnalysisBuilderLineOrientationTypeMemberType
        Both = 2  # ReflectionAnalysisBuilderLineOrientationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LineThicknessType():
        """
        The reflection line thickness. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Thin", "Thin."
           "Normal", "Normal."
           "Thick", "Thick."
        """
        Thin = 0  # ReflectionAnalysisBuilderLineThicknessTypeMemberType
        Normal = 1  # ReflectionAnalysisBuilderLineThicknessTypeMemberType
        Thick = 2  # ReflectionAnalysisBuilderLineThicknessTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SceneImageType():
        """
        The reflection scene images. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SimulatedHorizon", "Simulated horizon."
           "PhotoHorizon", "Photo horizon."
           "SphericalRoom", "Spherical room."
           "SphericalLightTubesRoom", "Spherical light tubes room."
           "DaytimeHorizon", "Daytime horizon."
           "MagentaSunset", "Magenta sunset."
           "SphericalHorizon", "Spherical horizon."
           "CylindricalRoom", "Cylindrical room."
           "MonochromeHorizon", "Monochrome horizon."
           "SmoothGrayScale", "Smooth gray scale."
           "SharpGrayScale", "Sharp gray scale."
           "SphericalTubes", "Spherical tubes."
        """
        SimulatedHorizon = 0  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        PhotoHorizon = 1  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        SphericalRoom = 2  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        SphericalLightTubesRoom = 3  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        DaytimeHorizon = 4  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        MagentaSunset = 5  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        SphericalHorizon = 6  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        CylindricalRoom = 7  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        MonochromeHorizon = 8  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        SmoothGrayScale = 9  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        SharpGrayScale = 10  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        SphericalTubes = 11  # ReflectionAnalysisBuilderSceneImageTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ImageMovementTypes():
        """
        The type of image movement. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Horizontal", "Move image in horizonal direction."
           "Vertical", "Move image in vertical direction."
           "Rotate", "Rotate image."
        """
        Horizontal = 0  # ReflectionAnalysisBuilderImageMovementTypesMemberType
        Vertical = 1  # ReflectionAnalysisBuilderImageMovementTypesMemberType
        Rotate = 2  # ReflectionAnalysisBuilderImageMovementTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ImageSizeOption():
        """
        The reflection image size option. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "KeepCurrent", "Keep current size."
           "ReduceScale", "Reduce scale size."
        """
        KeepCurrent = 0  # ReflectionAnalysisBuilderImageSizeOptionMemberType
        ReduceScale = 1  # ReflectionAnalysisBuilderImageSizeOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def StartReflectionAnalysis(self) -> None:
        """
        Start reflection analysis.  
        
        Signature ``StartReflectionAnalysis()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    DisplayResolution: NXOpen.GeometricUtilities.DisplayResolutionBuilder = ...
    """
    Returns  the display resolution.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayResolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.DisplayResolutionBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    FaceReflectivityScale: int = ...
    """
    Returns or sets  the face reflectivity scale from 0 to 100.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceReflectivityScale`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FaceReflectivityScale`` 
    
    :param faceReflectivityScale: 
    :type faceReflectivityScale: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Faces: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the face to apply reflection analysis.  
    
    <hr>
    
    Getter Method
    
    Signature ``Faces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    FileName: str = ...
    """
    Returns or sets  the file browser.  
    
    <hr>
    
    Getter Method
    
    Signature ``FileName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FileName`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ImageMovementType: ReflectionAnalysisBuilderImageMovementTypes = ...
    """
    Returns or sets  the orientation to move reflection lines.  
    
    <hr>
    
    Getter Method
    
    Signature ``ImageMovementType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderImageMovementTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageMovementType`` 
    
    :param imageMovementType: 
    :type imageMovementType: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderImageMovementTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ImagePosition: int = ...
    """
    Returns or sets  the moving image scale.  
    
    <hr>
    
    Getter Method
    
    Signature ``ImagePosition`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImagePosition`` 
    
    :param imagePosition: 
    :type imagePosition: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ImageSizeSetting: ReflectionAnalysisBuilderImageSizeOption = ...
    """
    Returns or sets  the image size setting.  
    
    <hr>
    
    Getter Method
    
    Signature ``ImageSizeSetting`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderImageSizeOption` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageSizeSetting`` 
    
    :param imageSizeSetting: 
    :type imageSizeSetting: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderImageSizeOption` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LineImageType: ReflectionAnalysisBuilderLineImageTypes = ...
    """
    Returns or sets  the image type.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineImageType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderLineImageTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineImageType`` 
    
    :param lineImageType: 
    :type lineImageType: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderLineImageTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LineNumber: ReflectionAnalysisBuilderNumberOfLinesOptions = ...
    """
    Returns or sets  the reflection line number.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineNumber`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderNumberOfLinesOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineNumber`` 
    
    :param lineNumber: 
    :type lineNumber: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderNumberOfLinesOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LineOrientation: ReflectionAnalysisBuilderLineOrientationType = ...
    """
    Returns or sets  the reflection line orientation.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderLineOrientationType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineOrientation`` 
    
    :param lineOrientation: 
    :type lineOrientation: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderLineOrientationType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LineThickness: ReflectionAnalysisBuilderLineThicknessType = ...
    """
    Returns or sets  the reflection line thickness.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineThickness`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderLineThicknessType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineThickness`` 
    
    :param lineThickness: 
    :type lineThickness: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderLineThicknessType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Normals: FaceAnalysisNormalsBuilder = ...
    """
    Returns  the reflection analysis normals.  
    
    <hr>
    
    Getter Method
    
    Signature ``Normals`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    SceneImageOption: ReflectionAnalysisBuilderSceneImageType = ...
    """
    Returns or sets  the scene image option.  
    
    <hr>
    
    Getter Method
    
    Signature ``SceneImageOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderSceneImageType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SceneImageOption`` 
    
    :param sceneImageOption: 
    :type sceneImageOption: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderSceneImageType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ShowFacetEdge: bool = ...
    """
    Returns or sets  the flag indicating if facet edges should be shown.  
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFacetEdge`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFacetEdge`` 
    
    :param showFacetEdge: 
    :type showFacetEdge: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Type: ReflectionAnalysisBuilderTypes = ...
    """
    Returns or sets  the reflection analysis type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: ReflectionAnalysisBuilder = ...  # unknown typename


class AnalysisManager():
    """
    Represents the collection of analysis commands.  
    
    Inputs to this class can be convergent objects.
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX5.0.0
    """
    
    def CreateExamineGeometryObject(self) -> ExamineGeometry:
        """
        Creates an examine geometry object  
        
        Signature ``CreateExamineGeometryObject()`` 
        
        :returns:  Examine
        Geometry object  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.ExamineGeometry` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateSimpleInterferenceObject(self) -> SimpleInterference:
        """
        Creates a simple interference object  
        
        Signature ``CreateSimpleInterferenceObject()`` 
        
        :returns: 
        Simple Interference object  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.SimpleInterference` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateGeometricPropertiesObject(self) -> GeometricProperties:
        """
        Creates a geometric properties object  
        
        Signature ``CreateGeometricPropertiesObject()`` 
        
        :returns: 
        Geometric
        Properties object  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.GeometricProperties` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateSolidDensityObject(self) -> SolidDensity:
        """
        Creates a solid density object  
        
        Signature ``CreateSolidDensityObject()`` 
        
        :returns:  SolidDensity object 
        :rtype: :py:class:`NXOpen.GeometricAnalysis.SolidDensity` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDeviationCheckingObject(self) -> DeviationChecking:
        """
        Creates a deviation checking object  
        
        Signature ``CreateDeviationCheckingObject()`` 
        
        :returns:  DeviationChecking object 
        :rtype: :py:class:`NXOpen.GeometricAnalysis.DeviationChecking` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    AnalysisObjects: AnalysisObjectCollection = ...
    """
    Returns the AnalysisObjectCollection instance belonging to this part 
    
    Signature ``AnalysisObjects`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.AnalysisObjectCollection`
    """


class GeometricPropertiesCaeCurve_Struct():
    """
    CAE Edge/Curve Geometric Properties .  
    
    Constructor: 
    NXOpen.GeometricAnalysis.GeometricProperties.CaeCurve()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    ArcLengthParameter: float = ...
    """
    ArcLength parametrization
    <hr>
    
    Field Value
    Type:float
    """
    UnitArcLengthParameter: float = ...
    """
    UnitArcLength parametrization
    <hr>
    
    Field Value
    Type:float
    """
    ClosestPointInWcs: NXOpen.Point3d = ...
    """
    closest point on curve in Work Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    NormalInWcs: NXOpen.Vector3d = ...
    """
    normal of closest point in Work Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    TangentInWcs: NXOpen.Vector3d = ...
    """
    tangent of closest point in Work Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    Tangent: NXOpen.Vector3d = ...
    """
    tangent of closest point in Root Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    Normal: NXOpen.Vector3d = ...
    """
    normal of closest point in Root Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    ClosestPoint: NXOpen.Point3d = ...
    """
    closest point on curve in Root Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """


class CurveContinuityBuilderTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveContinuityBuilderType():
    """
    Define curve continuity types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CurvetoObject", "curve to object"
       "Multicurve", "multicurve"
    """
    CurvetoObject = 0  # CurveContinuityBuilderTypeMemberType
    Multicurve = 1  # CurveContinuityBuilderTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveContinuityBuilder(NXOpen.Builder):
    """
    Represents a curve continuity builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateCurveContinuityBuilder`
    
    Default values.
    
    ========================  ===========================================
    Property                  Value
    ========================  ===========================================
    AngularThreshold.Value    15.0 
    ------------------------  -------------------------------------------
    ContinuityType            Multicurve 
    ------------------------  -------------------------------------------
    DistanceThreshold.Value   10.0 (millimeters part), 0.5 (inches part) 
    ------------------------  -------------------------------------------
    EndPointX                 0 
    ------------------------  -------------------------------------------
    EndPointY                 0 
    ------------------------  -------------------------------------------
    EndPointZ                 0 
    ------------------------  -------------------------------------------
    G0Check                   1 
    ------------------------  -------------------------------------------
    G0Check2                  1 
    ------------------------  -------------------------------------------
    G0Tolerance               0.01 
    ------------------------  -------------------------------------------
    G1Check                   0 
    ------------------------  -------------------------------------------
    G1Check2                  0 
    ------------------------  -------------------------------------------
    G1Tolerance               0.5 
    ------------------------  -------------------------------------------
    G2Check                   0 
    ------------------------  -------------------------------------------
    G2Check2                  0 
    ------------------------  -------------------------------------------
    G2Tolerance               0.5 
    ------------------------  -------------------------------------------
    G3Check                   0 
    ------------------------  -------------------------------------------
    G3Check2                  0 
    ------------------------  -------------------------------------------
    G3Tolerance               0.5 
    ------------------------  -------------------------------------------
    ShowDeviation             1 
    ------------------------  -------------------------------------------
    ShowMarkup                1 
    ------------------------  -------------------------------------------
    ShowMaximum               0 
    ------------------------  -------------------------------------------
    ShowMinimum               0 
    ------------------------  -------------------------------------------
    ShowNeedle                1 
    ------------------------  -------------------------------------------
    ShowOutOfTolerance        0 
    ========================  ===========================================
    
    .. versionadded:: NX7.0.0
    """
    
    class Type():
        """
        Define curve continuity types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CurvetoObject", "curve to object"
           "Multicurve", "multicurve"
        """
        CurvetoObject = 0  # CurveContinuityBuilderTypeMemberType
        Multicurve = 1  # CurveContinuityBuilderTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def ResetShowDeviation(self) -> None:
        """
        Prepare to toggle deviation label 
        
        Signature ``ResetShowDeviation()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    AngularThreshold: NXOpen.Expression = ...
    """
    Returns  the angular threshold 
    
    <hr>
    
    Getter Method
    
    Signature ``AngularThreshold`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    ContinuityType: CurveContinuityBuilderType = ...
    """
    Returns or sets  the curve continuity type 
    
    <hr>
    
    Getter Method
    
    Signature ``ContinuityType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveContinuityBuilderType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContinuityType`` 
    
    :param continuityType: 
    :type continuityType: :py:class:`NXOpen.GeometricAnalysis.CurveContinuityBuilderType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    DistanceThreshold: NXOpen.Expression = ...
    """
    Returns  the distance threshold 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceThreshold`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    DynamicLabel: NXOpen.SelectNXObject = ...
    """
    Returns  the location for dynamic label 
    
    <hr>
    
    Getter Method
    
    Signature ``DynamicLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObject` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    EndPointX: float = ...
    """
    Returns or sets  the end point x value 
    
    <hr>
    
    Getter Method
    
    Signature ``EndPointX`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EndPointX`` 
    
    :param endPointX: 
    :type endPointX: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    EndPointY: float = ...
    """
    Returns or sets  the end point y value 
    
    <hr>
    
    Getter Method
    
    Signature ``EndPointY`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EndPointY`` 
    
    :param endPointY: 
    :type endPointY: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    EndPointZ: float = ...
    """
    Returns or sets  the end point z value 
    
    <hr>
    
    Getter Method
    
    Signature ``EndPointZ`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EndPointZ`` 
    
    :param endPointZ: 
    :type endPointZ: float 
    
    .. versionadded:: NX7.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G0Check: bool = ...
    """
    Returns or sets  the G0 check 
    
    <hr>
    
    Getter Method
    
    Signature ``G0Check`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G0Check`` 
    
    :param g0Check: 
    :type g0Check: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G0Check2: bool = ...
    """
    Returns or sets  the G0 check for multicurve 
    
    <hr>
    
    Getter Method
    
    Signature ``G0Check2`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G0Check2`` 
    
    :param g0Check2: 
    :type g0Check2: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    G0Tolerance: float = ...
    """
    Returns or sets  the g0 tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``G0Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G0Tolerance`` 
    
    :param g0Tolerance: 
    :type g0Tolerance: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    G1Check: bool = ...
    """
    Returns or sets  the G1 check 
    
    <hr>
    
    Getter Method
    
    Signature ``G1Check`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G1Check`` 
    
    :param g1Check: 
    :type g1Check: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G1Check2: bool = ...
    """
    Returns or sets  the G1 check for multicurve 
    
    <hr>
    
    Getter Method
    
    Signature ``G1Check2`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G1Check2`` 
    
    :param g1Check2: 
    :type g1Check2: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    G1Tolerance: float = ...
    """
    Returns or sets  the g1 tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``G1Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G1Tolerance`` 
    
    :param g1Tolerance: 
    :type g1Tolerance: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    G2Check: bool = ...
    """
    Returns or sets  the G2 check 
    
    <hr>
    
    Getter Method
    
    Signature ``G2Check`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G2Check`` 
    
    :param g2Check: 
    :type g2Check: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G2Check2: bool = ...
    """
    Returns or sets  the G2 check for multicurve 
    
    <hr>
    
    Getter Method
    
    Signature ``G2Check2`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G2Check2`` 
    
    :param g2Check2: 
    :type g2Check2: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    G2Tolerance: float = ...
    """
    Returns or sets  the g2 tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``G2Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G2Tolerance`` 
    
    :param g2Tolerance: 
    :type g2Tolerance: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    G3Check: bool = ...
    """
    Returns or sets  the G3 check 
    
    <hr>
    
    Getter Method
    
    Signature ``G3Check`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G3Check`` 
    
    :param g3Check: 
    :type g3Check: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G3Check2: bool = ...
    """
    Returns or sets  the G3 check for multicurve 
    
    <hr>
    
    Getter Method
    
    Signature ``G3Check2`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G3Check2`` 
    
    :param g3Check2: 
    :type g3Check2: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    G3Tolerance: float = ...
    """
    Returns or sets  the g3 tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``G3Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G3Tolerance`` 
    
    :param g3Tolerance: 
    :type g3Tolerance: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    MultiCurve: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the multiple curve 
    
    <hr>
    
    Getter Method
    
    Signature ``MultiCurve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    SelectCurve: NXOpen.SelectNXObject = ...
    """
    Returns  the select curve 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectCurve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObject` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    SelectObject: NXOpen.SelectNXObject = ...
    """
    Returns  the select object 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObject` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    ShowDeviation: bool = ...
    """
    Returns or sets  the show deviation label 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowDeviation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowDeviation`` 
    
    :param showDeviation: 
    :type showDeviation: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    ShowMarkup: bool = ...
    """
    Returns or sets  the show tolerance markup 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowMarkup`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowMarkup`` 
    
    :param showMarkup: 
    :type showMarkup: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    ShowMaximum: bool = ...
    """
    Returns or sets  the show maximum label 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowMaximum`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowMaximum`` 
    
    :param showMaximum: 
    :type showMaximum: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    ShowMinimum: bool = ...
    """
    Returns or sets  the show minimum label 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowMinimum`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowMinimum`` 
    
    :param showMinimum: 
    :type showMinimum: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    ShowNeedle: bool = ...
    """
    Returns or sets  the show needle 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowNeedle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowNeedle`` 
    
    :param showNeedle: 
    :type showNeedle: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    ShowOutOfTolerance: bool = ...
    """
    Returns or sets  the show out of tolerance only 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOutOfTolerance`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOutOfTolerance`` 
    
    :param showOutOfTolerance: 
    :type showOutOfTolerance: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: gateway ("UG GATEWAY")
    """
    Null: CurveContinuityBuilder = ...  # unknown typename


class SurfaceContinuityAnalysisBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceContinuityAnalysisBuilderTypes():
    """
    Two possible types for the dialog 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "EdgeToEdge", " - "
       "EdgeToFace", " - "
       "MultiFace", " - "
    """
    EdgeToEdge = 0  # SurfaceContinuityAnalysisBuilderTypesMemberType
    EdgeToFace = 1  # SurfaceContinuityAnalysisBuilderTypesMemberType
    MultiFace = 2  # SurfaceContinuityAnalysisBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceContinuityAnalysisBuilderCurvatureTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceContinuityAnalysisBuilderCurvatureType():
    """
    Curvature types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Sectional", " - "
       "Gaussian", " - "
       "Mean", " - "
       "Absolute", " - "
    """
    Sectional = 0  # SurfaceContinuityAnalysisBuilderCurvatureTypeMemberType
    Gaussian = 1  # SurfaceContinuityAnalysisBuilderCurvatureTypeMemberType
    Mean = 2  # SurfaceContinuityAnalysisBuilderCurvatureTypeMemberType
    Absolute = 3  # SurfaceContinuityAnalysisBuilderCurvatureTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceContinuityAnalysisBuilderReportingTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceContinuityAnalysisBuilderReportingType():
    """
    Reporting types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Analysis", " - "
       "Pair", " - "
    """
    Analysis = 0  # SurfaceContinuityAnalysisBuilderReportingTypeMemberType
    Pair = 1  # SurfaceContinuityAnalysisBuilderReportingTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceContinuityAnalysisBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.GeometricAnalysis.SurfaceContinuityAnalysis` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateSurfaceContinuityAnalysisBuilder`
    
    Default values.
    
    ===============  ==========
    Property         Value
    ===============  ==========
    CurvatureCheck   Sectional 
    ---------------  ----------
    G0               True 
    ---------------  ----------
    G1               False 
    ---------------  ----------
    G2               False 
    ---------------  ----------
    G3               False 
    ===============  ==========
    
    .. versionadded:: NX6.0.0
    """
    
    class Types():
        """
        Two possible types for the dialog 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "EdgeToEdge", " - "
           "EdgeToFace", " - "
           "MultiFace", " - "
        """
        EdgeToEdge = 0  # SurfaceContinuityAnalysisBuilderTypesMemberType
        EdgeToFace = 1  # SurfaceContinuityAnalysisBuilderTypesMemberType
        MultiFace = 2  # SurfaceContinuityAnalysisBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CurvatureType():
        """
        Curvature types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Sectional", " - "
           "Gaussian", " - "
           "Mean", " - "
           "Absolute", " - "
        """
        Sectional = 0  # SurfaceContinuityAnalysisBuilderCurvatureTypeMemberType
        Gaussian = 1  # SurfaceContinuityAnalysisBuilderCurvatureTypeMemberType
        Mean = 2  # SurfaceContinuityAnalysisBuilderCurvatureTypeMemberType
        Absolute = 3  # SurfaceContinuityAnalysisBuilderCurvatureTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ReportingType():
        """
        Reporting types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Analysis", " - "
           "Pair", " - "
        """
        Analysis = 0  # SurfaceContinuityAnalysisBuilderReportingTypeMemberType
        Pair = 1  # SurfaceContinuityAnalysisBuilderReportingTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def UpdateFirstEdgeFace(self, edgeOrFace: NXOpen.DisplayableObject, selectionPoint: NXOpen.Point3d) -> None:
        """
        The user selects or deselects first edge or face, update builder m_edge1, m_face1 
        
        Signature ``UpdateFirstEdgeFace(edgeOrFace, selectionPoint)`` 
        
        :param edgeOrFace:  the parent of Face or Edge  
        :type edgeOrFace: :py:class:`NXOpen.DisplayableObject` 
        :param selectionPoint: 
        :type selectionPoint: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def UpdateSecondEdgeFace(self, edgeOrFace: NXOpen.DisplayableObject, selectionPoint: NXOpen.Point3d) -> None:
        """
        User selects or deselects second edge or face, update builder m_edge2, m_face2 
        
        Signature ``UpdateSecondEdgeFace(edgeOrFace, selectionPoint)`` 
        
        :param edgeOrFace:  the parent of Face or Edge  
        :type edgeOrFace: :py:class:`NXOpen.DisplayableObject` 
        :param selectionPoint: 
        :type selectionPoint: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def UpdateFace(self, face: NXOpen.Face, selectionPoint: NXOpen.Point3d) -> None:
        """
        User selects or deselects face, update builder m_edge2, m_face2 
        
        Signature ``UpdateFace(face, selectionPoint)`` 
        
        :param face: 
        :type face: :py:class:`NXOpen.Face` 
        :param selectionPoint: 
        :type selectionPoint: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def GetFace1Array(self) -> 'list[NXOpen.Face]':
        """
        Returns the edge1 array not used  
        
        Signature ``GetFace1Array()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeselectFirstEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
        Deselection of first edge or face 
        
        Signature ``DeselectFirstEdgeFace(edge, face)`` 
        
        :param edge: 
        :type edge: :py:class:`NXOpen.DisplayableObject` 
        :param face: 
        :type face: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def SelectFirstEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
        Selection of first edge or face 
        
        Signature ``SelectFirstEdgeFace(edge, face)`` 
        
        :param edge: 
        :type edge: :py:class:`NXOpen.DisplayableObject` 
        :param face: 
        :type face: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def DeselectSecondEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
        Deselection of second edge or face 
        
        Signature ``DeselectSecondEdgeFace(edge, face)`` 
        
        :param edge: 
        :type edge: :py:class:`NXOpen.DisplayableObject` 
        :param face: 
        :type face: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def SelectSecondEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
        Selection of second edge or face 
        
        Signature ``SelectSecondEdgeFace(edge, face)`` 
        
        :param edge: 
        :type edge: :py:class:`NXOpen.DisplayableObject` 
        :param face: 
        :type face: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    AngularThreshold: NXOpen.Expression = ...
    """
    Returns  the angular threshold 
    
    <hr>
    
    Getter Method
    
    Signature ``AngularThreshold`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    CombOptions: NXOpen.GeometricUtilities.CombOptionsBuilder = ...
    """
    Returns  the comb display block options 
    
    <hr>
    
    Getter Method
    
    Signature ``CombOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.CombOptionsBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    CurvatureCheck: SurfaceContinuityAnalysisBuilderCurvatureType = ...
    """
    Returns or sets  the curvature check 
    
    <hr>
    
    Getter Method
    
    Signature ``CurvatureCheck`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilderCurvatureType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurvatureCheck`` 
    
    :param curvatureCheck: 
    :type curvatureCheck: :py:class:`NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilderCurvatureType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    DistanceThreshold: NXOpen.Expression = ...
    """
    Returns  the distance threshold 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceThreshold`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DynamicLabel: NXOpen.Features.GeometricConstraintDataManager = ...
    """
    Returns  the constraint manager 
    
    <hr>
    
    Getter Method
    
    Signature ``DynamicLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.GeometricConstraintDataManager` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Face: NXOpen.SelectNXObjectList = ...
    """
    Returns  the (second) faces.  
    
    Used only if the type is EdgeFace 
    
    <hr>
    
    Getter Method
    
    Signature ``Face`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    FirstEdge: NXOpen.SelectNXObjectList = ...
    """
    Returns  the first edges or faces 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    G0: bool = ...
    """
    Returns or sets  the g0 toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``G0`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G0`` 
    
    :param g0: 
    :type g0: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G0Tolerance: float = ...
    """
    Returns or sets  the g0 tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``G0Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G0Tolerance`` 
    
    :param g0Tolerance: 
    :type g0Tolerance: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G1: bool = ...
    """
    Returns or sets  the g1 toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``G1`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G1`` 
    
    :param g1: 
    :type g1: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G1Tolerance: float = ...
    """
    Returns or sets  the g1 tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``G1Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G1Tolerance`` 
    
    :param g1Tolerance: 
    :type g1Tolerance: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G2: bool = ...
    """
    Returns or sets  the g2 toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``G2`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G2`` 
    
    :param g2: 
    :type g2: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G2Tolerance: float = ...
    """
    Returns or sets  the g2 tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``G2Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G2Tolerance`` 
    
    :param g2Tolerance: 
    :type g2Tolerance: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G3: bool = ...
    """
    Returns or sets  the g3 toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``G3`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G3`` 
    
    :param g3: 
    :type g3: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    G3Tolerance: float = ...
    """
    Returns or sets  the g3 tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``G3Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``G3Tolerance`` 
    
    :param g3Tolerance: 
    :type g3Tolerance: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    MultiFace: NXOpen.SelectNXObjectList = ...
    """
    Returns  the objects for multi-face 
    
    <hr>
    
    Getter Method
    
    Signature ``MultiFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ReportPer: int = ...
    """
    Returns or sets  the reporting type 
    
    <hr>
    
    Getter Method
    
    Signature ``ReportPer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportPer`` 
    
    :param reportPer: 
    :type reportPer: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    SecondEdge: NXOpen.SelectNXObjectList = ...
    """
    Returns  the second edges or faces.  
    
    Used only if the type is EdgeEdge 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowOutOfTolerance: bool = ...
    """
    Returns or sets  the out of tolerance only flag 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOutOfTolerance`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOutOfTolerance`` 
    
    :param outTolerance: 
    :type outTolerance: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    ToleranceMarkup: bool = ...
    """
    Returns or sets  the tolerance markup flag 
    
    <hr>
    
    Getter Method
    
    Signature ``ToleranceMarkup`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToleranceMarkup`` 
    
    :param markup: 
    :type markup: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    Type: SurfaceContinuityAnalysisBuilderTypes = ...
    """
    Returns or sets  the type of analysis to perform 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilderTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilderTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    Null: SurfaceContinuityAnalysisBuilder = ...  # unknown typename


class GeometricPropertiesOutputTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GeometricPropertiesOutputType():
    """
    Represents how to output geometric properties.
    :py:class:`GeometricAnalysis.GeometricPropertiesOutputType.Dynamic <GeometricAnalysis.GeometricPropertiesOutputType>`
    displays the properties of an entity under the cursor when NX is
    run interactively. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Dynamic", "Properties of an entity are displayed first on the dialog itself on mouse over. These properties are listed on in the information window upon selection of a point."
       "Static", "Propeties of the selected entities are displayed in the information window."
    """
    Dynamic = 0  # GeometricPropertiesOutputTypeMemberType
    Static = 1  # GeometricPropertiesOutputTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GeometricPropertiesEntityMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GeometricPropertiesEntity():
    """
    Type of input entity for geometric properties. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Face", "Face"
       "Edge", "Either a modeling edge or a curve."
       "CaeFace", "CAE Face"
       "CaeCurve", "CAE Curve"
    """
    Face = 0  # GeometricPropertiesEntityMemberType
    Edge = 1  # GeometricPropertiesEntityMemberType
    CaeFace = 2  # GeometricPropertiesEntityMemberType
    CaeCurve = 3  # GeometricPropertiesEntityMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GeometricPropertiesCaeFace_Struct():
    """
    CAE Face Geometric Properties .  
    
    Constructor: 
    NXOpen.GeometricAnalysis.GeometricProperties.CaeFace()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    ClosestPoint: NXOpen.Vector3d = ...
    """
    closest point on face in Root Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    UParameter: float = ...
    """
    u parameter of the closest point in Root Part Coordinates
    <hr>
    
    Field Value
    Type:float
    """
    VParameter: float = ...
    """
    v parameter of the closest point in Root Part Coordinates
    <hr>
    
    Field Value
    Type:float
    """
    Normal: NXOpen.Vector3d = ...
    """
    normal at the closest point in Root Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    ClosestPointInWcs: NXOpen.Point3d = ...
    """
    closest point in Work Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    NormalInWcs: NXOpen.Vector3d = ...
    """
    normal in Work Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    UDerivative: NXOpen.Vector3d = ...
    """
    Derivative in U, Root Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    VDerivative: NXOpen.Vector3d = ...
    """
    Derivative in V, Root Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    UDerivativeInWcs: NXOpen.Vector3d = ...
    """
    Derivative in U in Work Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    VDerivativeInWcs: NXOpen.Vector3d = ...
    """
    Derivative in V in Work Part Coordinates
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """


class GeometricPropertiesStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GeometricPropertiesStatus():
    """
    Status of computing geometric properties. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Success", "Success"
       "InvalidInput", "Input specified is not valid."
       "Failed", "Failed to find all geometric properties"
    """
    Success = 0  # GeometricPropertiesStatusMemberType
    InvalidInput = 1  # GeometricPropertiesStatusMemberType
    Failed = 2  # GeometricPropertiesStatusMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GeometricProperties(NXOpen.Builder):
    """
    Represents the Geometric Properties class.  
    
    This class can be used to
    find local geometric properties of faces, edges, curves, CAE faces, and CAE
    edges/curves at a given point.
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisManager.CreateGeometricPropertiesObject`
    
    .. versionadded:: NX5.0.0
    """
    
    class OutputType():
        """
        Represents how to output geometric properties.
        :py:class:`GeometricAnalysis.GeometricPropertiesOutputType.Dynamic <GeometricAnalysis.GeometricPropertiesOutputType>`
        displays the properties of an entity under the cursor when NX is
        run interactively. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Dynamic", "Properties of an entity are displayed first on the dialog itself on mouse over. These properties are listed on in the information window upon selection of a point."
           "Static", "Propeties of the selected entities are displayed in the information window."
        """
        Dynamic = 0  # GeometricPropertiesOutputTypeMemberType
        Static = 1  # GeometricPropertiesOutputTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Entity():
        """
        Type of input entity for geometric properties. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Face", "Face"
           "Edge", "Either a modeling edge or a curve."
           "CaeFace", "CAE Face"
           "CaeCurve", "CAE Curve"
        """
        Face = 0  # GeometricPropertiesEntityMemberType
        Edge = 1  # GeometricPropertiesEntityMemberType
        CaeFace = 2  # GeometricPropertiesEntityMemberType
        CaeCurve = 3  # GeometricPropertiesEntityMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Face():
        """
        Face Geometric Properties .  
        
        Constructor: 
        NXOpen.GeometricAnalysis.GeometricProperties.Face()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        UParamater: float = ...
        """
        U parameter 
        <hr>
        
        Field Value
        Type:float
        """
        VParamater: float = ...
        """
        V parameter 
        <hr>
        
        Field Value
        Type:float
        """
        PositionInWcs: NXOpen.Point3d = ...
        """
        XYZ Position in Work Part coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
        UDerivativeInWcs: NXOpen.Vector3d = ...
        """
        Derivative Vector in U direction - Work Part  Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        VDerivativeInWcs: NXOpen.Vector3d = ...
        """
        Derivative Vector in V direction - Work Part  Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        NormalInWcs: NXOpen.Vector3d = ...
        """
        Unitized Face Normal - Work Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        Position: NXOpen.Point3d = ...
        """
        XYZ Position 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
        UDerivative: NXOpen.Vector3d = ...
        """
        Derivative Vector in U direction -  Root Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        VDerivative: NXOpen.Vector3d = ...
        """
        Derivative Vector in V direction - Root Part  Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        Normal: NXOpen.Vector3d = ...
        """
        Unitized Face Normal - Root Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        InvOfMinRadiusOfCurvature: float = ...
        """
        Inverse of Minumum  Radius of
        Curvature, 1/(minimum radius of curvature) 
        <hr>
        
        Field Value
        Type:float
        """
        InvOfMaxRadiusOfCurvature: float = ...
        """
        Inverse of Maximum Radius of
        Curvature,  1/(maximum radius of curvature).  
        
        <hr>
        
        Field Value
        Type:float
        """
    
    
    class Edge():
        """
        Edge/Curve Geometric Properties .  
        
        Constructor: 
        NXOpen.GeometricAnalysis.GeometricProperties.Edge()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        ParameterPercentage: float = ...
        """
        Curve Parameter Percentage 
        <hr>
        
        Field Value
        Type:float
        """
        Parameter: float = ...
        """
        Curve Parameter
        <hr>
        
        Field Value
        Type:float
        """
        PositionInWcs: NXOpen.Point3d = ...
        """
        XYZ Position in Work Part coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
        Position: NXOpen.Point3d = ...
        """
        XYZ Position in Root Part coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
        TangentInWcs: NXOpen.Vector3d = ...
        """
        Tangent Vector in Work Part coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        Tangent: NXOpen.Vector3d = ...
        """
        Tangent Vector in Root Part coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        NormalInWcs: NXOpen.Vector3d = ...
        """
        Curve Normal in Work Part coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        Normal: NXOpen.Vector3d = ...
        """
        Curve Normal in Root Part coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        BinormalInWcs: NXOpen.Vector3d = ...
        """
        Curve Binormal in Work Part coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        Binormal: NXOpen.Vector3d = ...
        """
        Curve Binormal in Root Part coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        Torsion: float = ...
        """
        Curve Torsion
        <hr>
        
        Field Value
        Type:float
        """
        Curvature: float = ...
        """
        Curvature of the Curve
        <hr>
        
        Field Value
        Type:float
        """
    
    
    class CaeFace():
        """
        CAE Face Geometric Properties .  
        
        Constructor: 
        NXOpen.GeometricAnalysis.GeometricProperties.CaeFace()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        ClosestPoint: NXOpen.Vector3d = ...
        """
        closest point on face in Root Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        UParameter: float = ...
        """
        u parameter of the closest point in Root Part Coordinates
        <hr>
        
        Field Value
        Type:float
        """
        VParameter: float = ...
        """
        v parameter of the closest point in Root Part Coordinates
        <hr>
        
        Field Value
        Type:float
        """
        Normal: NXOpen.Vector3d = ...
        """
        normal at the closest point in Root Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        ClosestPointInWcs: NXOpen.Point3d = ...
        """
        closest point in Work Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
        NormalInWcs: NXOpen.Vector3d = ...
        """
        normal in Work Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        UDerivative: NXOpen.Vector3d = ...
        """
        Derivative in U, Root Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        VDerivative: NXOpen.Vector3d = ...
        """
        Derivative in V, Root Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        UDerivativeInWcs: NXOpen.Vector3d = ...
        """
        Derivative in U in Work Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        VDerivativeInWcs: NXOpen.Vector3d = ...
        """
        Derivative in V in Work Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
    
    
    class CaeCurve():
        """
        CAE Edge/Curve Geometric Properties .  
        
        Constructor: 
        NXOpen.GeometricAnalysis.GeometricProperties.CaeCurve()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        ArcLengthParameter: float = ...
        """
        ArcLength parametrization
        <hr>
        
        Field Value
        Type:float
        """
        UnitArcLengthParameter: float = ...
        """
        UnitArcLength parametrization
        <hr>
        
        Field Value
        Type:float
        """
        ClosestPointInWcs: NXOpen.Point3d = ...
        """
        closest point on curve in Work Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
        NormalInWcs: NXOpen.Vector3d = ...
        """
        normal of closest point in Work Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        TangentInWcs: NXOpen.Vector3d = ...
        """
        tangent of closest point in Work Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        Tangent: NXOpen.Vector3d = ...
        """
        tangent of closest point in Root Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        Normal: NXOpen.Vector3d = ...
        """
        normal of closest point in Root Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        ClosestPoint: NXOpen.Point3d = ...
        """
        closest point on curve in Root Part Coordinates
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
    
    
    class Status():
        """
        Status of computing geometric properties. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Success", "Success"
           "InvalidInput", "Input specified is not valid."
           "Failed", "Failed to find all geometric properties"
        """
        Success = 0  # GeometricPropertiesStatusMemberType
        InvalidInput = 1  # GeometricPropertiesStatusMemberType
        Failed = 2  # GeometricPropertiesStatusMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetFaceProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> tuple:
        """
        Returns face local properties at the given point  
        
        Signature ``GetFaceProperties(entityTag, absPoint)`` 
        
        :param entityTag:  NXObject to                                                             obtain the properties for  
        :type entityTag: :py:class:`NXOpen.NXObject` 
        :param absPoint:  Absolute point                                                            co-ordinates of the reference point                                                             to compute the properties  
        :type absPoint: :py:class:`NXOpen.Point3d` 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, face). status is a :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesStatus`.   Return status face is a :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesFace_Struct`.   Face Properties 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetEdgeProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> tuple:
        """
        Returns edge/curve local properties at the given point  
        
        Signature ``GetEdgeProperties(entityTag, absPoint)`` 
        
        :param entityTag:  NXObject to                                                             obtain the properties for  
        :type entityTag: :py:class:`NXOpen.NXObject` 
        :param absPoint:  Absolute point                                                            co-ordinates of the reference point                                                             to compute the properties  
        :type absPoint: :py:class:`NXOpen.Point3d` 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, edge). status is a :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesStatus`.   Return status edge is a :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesEdge_Struct`.   Edge/Curve Properties 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCaeFaceProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> tuple:
        """
        Returns CAE face local properties at the given point  
        
        Signature ``GetCaeFaceProperties(entityTag, absPoint)`` 
        
        :param entityTag:  NXObject to                                                             obtain the properties for  
        :type entityTag: :py:class:`NXOpen.NXObject` 
        :param absPoint:  Absolute point                                                            co-ordinates of the reference point                                                             to compute the properties  
        :type absPoint: :py:class:`NXOpen.Point3d` 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, caeFace). status is a :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesStatus`.   Return status caeFace is a :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesCaeFace_Struct`.   CAE Face Properties 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCaeCurveProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> tuple:
        """
        Returns CAE curve local properties at the given point  
        
        Signature ``GetCaeCurveProperties(entityTag, absPoint)`` 
        
        :param entityTag:  NXObject to                                                             obtain the properties for  
        :type entityTag: :py:class:`NXOpen.NXObject` 
        :param absPoint:  Absolute point                                                            co-ordinates of the reference point                                                             to compute the properties  
        :type absPoint: :py:class:`NXOpen.Point3d` 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, caeCurve). status is a :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesStatus`.   Return status caeCurve is a :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesCaeCurve_Struct`.   CAE Edge/Curve Properties 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def ListProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> GeometricPropertiesStatus:
        """
        Displays the local properties of the specified object at the
        given point in the listing window  
        
        Signature ``ListProperties(entityTag, absPoint)`` 
        
        :param entityTag:  NXObject to                                                             obtain the properties for  
        :type entityTag: :py:class:`NXOpen.NXObject` 
        :param absPoint:  Absolute point                                                            co-ordinates of the reference point                                                             to compute the properties  
        :type absPoint: :py:class:`NXOpen.Point3d` 
        :returns:  Return status  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesStatus` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def ListProperties(self, absPoint: NXOpen.Point3d) -> GeometricPropertiesStatus:
        """
        Displays the local properties of
        :py:meth:`ObjectsForAnalysis` at the given point in 
        the listing window.   
        
        Signature ``ListProperties(absPoint)`` 
        
        :param absPoint:  Absolute point                                                            co-ordinates of the reference point                                                             to compute the properties  
        :type absPoint: :py:class:`NXOpen.Point3d` 
        :returns:  Return status  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesStatus` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Reset(self) -> None:
        """
        Clears all markers showing the local geometric properties in the graphics window 
        
        Signature ``Reset()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ObjectsForAnalysis: NXOpen.SelectObjectList = ...
    """
    Returns  the Objects for analysis 
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectsForAnalysis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectObjectList` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    OutputMethod: GeometricPropertiesOutputType = ...
    """
    Returns or sets  the output method 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesOutputType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputMethod`` 
    
    :param outputMethod: 
    :type outputMethod: :py:class:`NXOpen.GeometricAnalysis.GeometricPropertiesOutputType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: GeometricProperties = ...  # unknown typename


class SimpleInterferenceInterferenceMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SimpleInterferenceInterferenceMethod():
    """
    Specifies interference method, i.e., to highlight interfering
    faces or create interference solid 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "InterferingFaces", "Find interfering faces."
       "InterferenceSolid", "Create interference solid."
    """
    InterferingFaces = 0  # SimpleInterferenceInterferenceMethodMemberType
    InterferenceSolid = 1  # SimpleInterferenceInterferenceMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SimpleInterferenceFaceInterferenceMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SimpleInterferenceFaceInterferenceMethod():
    """
    Specifies to "find only first pair of interfering faces" or "all
    pairs of interfering faces" between the input boides. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FirstPairOnly", "Find first pair of interfering faces"
       "AllPairs", "Find all pairs of interfering faces."
    """
    FirstPairOnly = 0  # SimpleInterferenceFaceInterferenceMethodMemberType
    AllPairs = 1  # SimpleInterferenceFaceInterferenceMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SimpleInterferenceResultMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SimpleInterferenceResult():
    """
    Specifies the result of a simple interference check 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoInterference", "No interference exists between the input bodies."
       "OnlyEdgesOrFacesInterfere", "Only faces or edges interfere and no solid interference exists between the input bodies."
       "InterferenceExists", "Interference exists between the input bodies. Use :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.GetInterferenceResults` to obtain the pairs of faces interfering or interference solid(s) created between the input bodies."
       "CanNotPerformCheck", "An unknown error has occured while performing the interference check. Check could not be performed between the input bodies."
    """
    NoInterference = 0  # SimpleInterferenceResultMemberType
    OnlyEdgesOrFacesInterfere = 1  # SimpleInterferenceResultMemberType
    InterferenceExists = 2  # SimpleInterferenceResultMemberType
    CanNotPerformCheck = 3  # SimpleInterferenceResultMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SimpleInterference(NXOpen.Builder):
    """
    Represents the Simple Interference object.  
    
    A
    :py:class:`NXOpen.GeometricAnalysis.SimpleInterference` object
    takes two solid bodies as inputs and the type of interference results to
    be produced. It can report the first pair of interfering faces between
    two solids or all pairs of interfering faces. It can also
    create the interference solid(s) between two bodies.
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisManager.CreateSimpleInterferenceObject`
    
    .. versionadded:: NX5.0.0
    """
    
    class InterferenceMethod():
        """
        Specifies interference method, i.e., to highlight interfering
        faces or create interference solid 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "InterferingFaces", "Find interfering faces."
           "InterferenceSolid", "Create interference solid."
        """
        InterferingFaces = 0  # SimpleInterferenceInterferenceMethodMemberType
        InterferenceSolid = 1  # SimpleInterferenceInterferenceMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FaceInterferenceMethod():
        """
        Specifies to "find only first pair of interfering faces" or "all
        pairs of interfering faces" between the input boides. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FirstPairOnly", "Find first pair of interfering faces"
           "AllPairs", "Find all pairs of interfering faces."
        """
        FirstPairOnly = 0  # SimpleInterferenceFaceInterferenceMethodMemberType
        AllPairs = 1  # SimpleInterferenceFaceInterferenceMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
        Specifies the result of a simple interference check 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoInterference", "No interference exists between the input bodies."
           "OnlyEdgesOrFacesInterfere", "Only faces or edges interfere and no solid interference exists between the input bodies."
           "InterferenceExists", "Interference exists between the input bodies. Use :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.GetInterferenceResults` to obtain the pairs of faces interfering or interference solid(s) created between the input bodies."
           "CanNotPerformCheck", "An unknown error has occured while performing the interference check. Check could not be performed between the input bodies."
        """
        NoInterference = 0  # SimpleInterferenceResultMemberType
        OnlyEdgesOrFacesInterfere = 1  # SimpleInterferenceResultMemberType
        InterferenceExists = 2  # SimpleInterferenceResultMemberType
        CanNotPerformCheck = 3  # SimpleInterferenceResultMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def PerformCheck(self) -> SimpleInterferenceResult:
        """
        Perform Interference Check.  
        
        :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.PerformCheck`
        should be called after specifiying input bodies to be checked, i.e.,
        :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.FirstBody`
        and :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.SecondBody`. 
        The return value :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceResult` specifies the type of
        interference existing between the input bodies. Use
        :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.GetInterferenceResults` to obtain the interfering faces
        or solid(s) of interference between the input bodis.
        
        Signature ``PerformCheck()`` 
        
        :returns:  Indicates
        the type of interference existing between the input bodies.  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceResult` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def HighlightNextPair(self) -> bool:
        """
        Highlights the pairs of interfering faces after a
        :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.PerformCheck`.  
        
        This method is applicable only
        when :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType`` is set to
        :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod.InterferingFaces <NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod>` and
        :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType`` is set to
        :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod.AllPairs <NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod>`. When
        highlighting the next pair, current pair of faces is
        unhighlighted. Return value is set to true if there are more
        pairs of faces to be highlighted. If the last pair is reached 
        (i.e., the pair being highlighted in this call is the last pair 
        of faces), return value is set to false. 
        
        Signature ``HighlightNextPair()`` 
        
        :returns:  Indicates if there are
        any more pairs left .  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterferenceResults(self) -> 'list[NXOpen.NXObject]':
        """
        Returns the pair(s) of interfering faces or solid(s) of interference
        between the input bodies.  
        
        nObjects will be 0 if there is no face or
        solid interference between the input bodies. If the
        :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType`` is
        :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod.InterferingFaces <NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod>`, pair(s) of
        interfering faces are returned. The first two objects represent the first pair of
        interfering faces, and next two objects represent the second pair
        of interering faces and so on. If the
        :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType`` is
        :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod.FirstPairOnly <NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod>`,
        only the first pair of interfering faces are returned.
        
        Signature ``GetInterferenceResults()`` 
        
        :returns:  Results of Simple Interference  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX6.0.2
        
        License requirements: None.
        """
        ...
    
    
    def Reset(self) -> None:
        """
        Frees up resources/results associated with
        :py:class:`NXOpen.GeometricAnalysis.SimpleInterference` object after a
        call to :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.PerformCheck`.  
        
        :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.PerformCheck` is followed by
        :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.GetInterferenceResults` and the
        :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.Reset`. 
        
        Signature ``Reset()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    FaceInterferenceType: SimpleInterferenceFaceInterferenceMethod = ...
    """
    Returns or sets  the FaceInterferenceType.  
    
    :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType`` is used when 
    :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType`` is set to
    :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod.InterferingFaces <NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod>`, 
    i.e., create pair(s) of interfering faces between two solids. A
    value of :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod.FirstPairOnly <NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod>` 
    for :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType`` reports only the first
    pair of interfering faces and value of
    :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod.AllPairs <NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod>` 
    reports all pairs of interfering faces between two bodies. 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceInterferenceType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FaceInterferenceType`` 
    
    :param faceInterferenceType: 
    :type faceInterferenceType: :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    FirstBody: NXOpen.SelectObject = ...
    """
    Returns  the First Body 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectObject` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    InterferenceType: SimpleInterferenceInterferenceMethod = ...
    """
    Returns or sets  the InterferenceType.  
    
    A value of
    :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod.InterferingFaces <NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod>`  for
    :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType`` reports 
    the pairs of interfering faces between two solids.  You can also
    further specify to report only the first pair of interfering faces or 
    all pairs of interfering faces by 
    :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType``. A value of
    :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod.InterferenceSolid <NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod>` for
    :py:meth:`NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType`` creates the 
    interference solid(s) between the two input bodies. 
    
    <hr>
    
    Getter Method
    
    Signature ``InterferenceType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterferenceType`` 
    
    :param interferenceType: 
    :type interferenceType: :py:class:`NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    SecondBody: NXOpen.SelectObject = ...
    """
    Returns  the Second Body 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectObject` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: SimpleInterference = ...  # unknown typename


class FaceAnalysisDisplayBuilderColorLegendOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FaceAnalysisDisplayBuilderColorLegendOptions():
    """
    Represents color legend type in display. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Blend", "Blended color display."
       "Sharp", "Sharp color display."
    """
    Blend = 0  # FaceAnalysisDisplayBuilderColorLegendOptionsMemberType
    Sharp = 1  # FaceAnalysisDisplayBuilderColorLegendOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FaceAnalysisDisplayBuilderColorsOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FaceAnalysisDisplayBuilderColorsOptions():
    """
    The option indicating number of colors to be used for display. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Two", "Display in 2 colors."
       "Three", "Display in 3 colors."
       "Four", "Display in 4 colors."
       "Five", "Display in 5 colors."
       "Six", "Display in 6 colors."
       "Seven", "Display in 7 colors."
       "Eight", "Display in 8 colors."
       "Nine", "Display in 9 colors."
       "Ten", "Display in 10 colors."
       "Eleven", "Display in 11 colors."
       "Twelve", "Display in 12 colors."
    """
    Two = 0  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    Three = 1  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    Four = 2  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    Five = 3  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    Six = 4  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    Seven = 5  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    Eight = 6  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    Nine = 7  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    Ten = 8  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    Eleven = 9  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    Twelve = 10  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FaceAnalysisDisplayBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a set of display settings used by Face Analysis.  
    
    .. versionadded:: NX11.0.0
    """
    
    class ColorLegendOptions():
        """
        Represents color legend type in display. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Blend", "Blended color display."
           "Sharp", "Sharp color display."
        """
        Blend = 0  # FaceAnalysisDisplayBuilderColorLegendOptionsMemberType
        Sharp = 1  # FaceAnalysisDisplayBuilderColorLegendOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ColorsOptions():
        """
        The option indicating number of colors to be used for display. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Two", "Display in 2 colors."
           "Three", "Display in 3 colors."
           "Four", "Display in 4 colors."
           "Five", "Display in 5 colors."
           "Six", "Display in 6 colors."
           "Seven", "Display in 7 colors."
           "Eight", "Display in 8 colors."
           "Nine", "Display in 9 colors."
           "Ten", "Display in 10 colors."
           "Eleven", "Display in 11 colors."
           "Twelve", "Display in 12 colors."
        """
        Two = 0  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        Three = 1  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        Four = 2  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        Five = 3  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        Six = 4  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        Seven = 5  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        Eight = 6  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        Nine = 7  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        Ten = 8  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        Eleven = 9  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        Twelve = 10  # FaceAnalysisDisplayBuilderColorsOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    CanShowFacet: bool = ...
    """
    Returns or sets  the flag indicating if facets should be shown.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanShowFacet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanShowFacet`` 
    
    :param canShowFacet: 
    :type canShowFacet: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ColorLegendOption: FaceAnalysisDisplayBuilderColorLegendOptions = ...
    """
    Returns or sets  the color legend option.  
    
    <hr>
    
    Getter Method
    
    Signature ``ColorLegendOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilderColorLegendOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColorLegendOption`` 
    
    :param colorLegendOption: 
    :type colorLegendOption: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilderColorLegendOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DisplayResolution: NXOpen.GeometricUtilities.DisplayResolutionBuilder = ...
    """
    Returns  the display resolution.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayResolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.DisplayResolutionBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    NumberOfColors: FaceAnalysisDisplayBuilderColorsOptions = ...
    """
    Returns or sets  the number of colors.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfColors`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilderColorsOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfColors`` 
    
    :param numberOfColors: 
    :type numberOfColors: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilderColorsOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: FaceAnalysisDisplayBuilder = ...  # unknown typename


class RadiusAnalysisBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RadiusAnalysisBuilderTypes():
    """
    Represents the radius type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Gaussian", "Gaussian radius."
       "Minimum", "Minimum radius."
       "Maximum", "Maximum radius."
       "Mean", "Mean radius."
       "Normal", "Normal radius."
       "Sectional", "Sectional radius."
       "U", "Radius in U direction."
       "V", "Radius in V direction."
    """
    Gaussian = 0  # RadiusAnalysisBuilderTypesMemberType
    Minimum = 1  # RadiusAnalysisBuilderTypesMemberType
    Maximum = 2  # RadiusAnalysisBuilderTypesMemberType
    Mean = 3  # RadiusAnalysisBuilderTypesMemberType
    Normal = 4  # RadiusAnalysisBuilderTypesMemberType
    Sectional = 5  # RadiusAnalysisBuilderTypesMemberType
    U = 6  # RadiusAnalysisBuilderTypesMemberType
    V = 7  # RadiusAnalysisBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RadiusAnalysisBuilderDisplayModesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RadiusAnalysisBuilderDisplayModes():
    """
    The display type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fringe", "Display in fringe."
       "Hedgehog", "Display in hedgehog."
       "ContourLines", "Display in contour lines."
    """
    Fringe = 0  # RadiusAnalysisBuilderDisplayModesMemberType
    Hedgehog = 1  # RadiusAnalysisBuilderDisplayModesMemberType
    ContourLines = 2  # RadiusAnalysisBuilderDisplayModesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RadiusAnalysisBuilder(NXOpen.Builder):
    """
    Represents a Radius Analysis builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollectionEx.CreateRadiusAnalysisBuilder`
    
    Default values.
    
    =================================================  ===========================================
    Property                                           Value
    =================================================  ===========================================
    DataRange.IsFixed                                  1 
    -------------------------------------------------  -------------------------------------------
    DataRange.Max                                      0.01 
    -------------------------------------------------  -------------------------------------------
    DataRange.Middle                                   0.00001 
    -------------------------------------------------  -------------------------------------------
    DataRange.MiddleScale                              999999 
    -------------------------------------------------  -------------------------------------------
    DataRange.Min                                      -0.01 
    -------------------------------------------------  -------------------------------------------
    DataRange.ZoomScale                                8 
    -------------------------------------------------  -------------------------------------------
    DisplayMode                                        Fringe 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.CanShowFacet                       0 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.ColorLegendOption                  Blend 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.AngleTolerance   15.0 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.EdgeTolerance    0.005 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.FaceTolerance    0.005 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.Resolution       Standard 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.DisplayResolution.WidthTolerance   0.3 
    -------------------------------------------------  -------------------------------------------
    DisplaySettings.NumberOfColors                     Seven 
    -------------------------------------------------  -------------------------------------------
    NumberOfContourLines                               8 
    -------------------------------------------------  -------------------------------------------
    SpikeLength                                        25.4 (millimeters part), 1.0 (inches part) 
    =================================================  ===========================================
    
    .. versionadded:: NX11.0.0
    """
    
    class Types():
        """
        Represents the radius type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Gaussian", "Gaussian radius."
           "Minimum", "Minimum radius."
           "Maximum", "Maximum radius."
           "Mean", "Mean radius."
           "Normal", "Normal radius."
           "Sectional", "Sectional radius."
           "U", "Radius in U direction."
           "V", "Radius in V direction."
        """
        Gaussian = 0  # RadiusAnalysisBuilderTypesMemberType
        Minimum = 1  # RadiusAnalysisBuilderTypesMemberType
        Maximum = 2  # RadiusAnalysisBuilderTypesMemberType
        Mean = 3  # RadiusAnalysisBuilderTypesMemberType
        Normal = 4  # RadiusAnalysisBuilderTypesMemberType
        Sectional = 5  # RadiusAnalysisBuilderTypesMemberType
        U = 6  # RadiusAnalysisBuilderTypesMemberType
        V = 7  # RadiusAnalysisBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DisplayModes():
        """
        The display type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Fringe", "Display in fringe."
           "Hedgehog", "Display in hedgehog."
           "ContourLines", "Display in contour lines."
        """
        Fringe = 0  # RadiusAnalysisBuilderDisplayModesMemberType
        Hedgehog = 1  # RadiusAnalysisBuilderDisplayModesMemberType
        ContourLines = 2  # RadiusAnalysisBuilderDisplayModesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def UpdateDisplayOnPlaneChange(self) -> None:
        """
        Update display after plane changes.  
        
        Signature ``UpdateDisplayOnPlaneChange()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def StartRadiusAnalysis(self) -> None:
        """
        Start radius analysis.  
        
        Signature ``StartRadiusAnalysis()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    DataRange: FaceAnalysisDataRangeBuilder = ...
    """
    Returns  the radius analysis data range.  
    
    <hr>
    
    Getter Method
    
    Signature ``DataRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DisplayMode: RadiusAnalysisBuilderDisplayModes = ...
    """
    Returns or sets  the display mode.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.RadiusAnalysisBuilderDisplayModes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayMode`` 
    
    :param displayMode: 
    :type displayMode: :py:class:`NXOpen.GeometricAnalysis.RadiusAnalysisBuilderDisplayModes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DisplaySettings: FaceAnalysisDisplayBuilder = ...
    """
    Returns  the radius analysis display settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplaySettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Faces: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the face to apply radius analysis.  
    
    <hr>
    
    Getter Method
    
    Signature ``Faces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Normals: FaceAnalysisNormalsBuilder = ...
    """
    Returns  the radius analysis normals.  
    
    <hr>
    
    Getter Method
    
    Signature ``Normals`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    NumberOfContourLines: int = ...
    """
    Returns or sets  the number of contour lines.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfContourLines`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfContourLines`` 
    
    :param numberOfContourLines: 
    :type numberOfContourLines: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the reference plane used for :py:class:`NXOpen.GeometricAnalysis.RadiusAnalysisBuilderTypes.Sectional <NXOpen.GeometricAnalysis.RadiusAnalysisBuilderTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    SpikeLength: float = ...
    """
    Returns or sets  the spike length.  
    
    <hr>
    
    Getter Method
    
    Signature ``SpikeLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpikeLength`` 
    
    :param spikeLength: 
    :type spikeLength: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Type: RadiusAnalysisBuilderTypes = ...
    """
    Returns or sets  the radius type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.RadiusAnalysisBuilderTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.GeometricAnalysis.RadiusAnalysisBuilderTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the reference vector for :py:class:`NXOpen.GeometricAnalysis.RadiusAnalysisBuilderTypes.Normal <NXOpen.GeometricAnalysis.RadiusAnalysisBuilderTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vector: 
    :type vector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: RadiusAnalysisBuilder = ...  # unknown typename


class FaceCurvatureAnalysis(AnalysisObject):
    """
    Represents a Face Curvature Analysis builder   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: FaceCurvatureAnalysis = ...  # unknown typename


class SurfaceIntersectionBuilderProjectionTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceIntersectionBuilderProjectionTypes():
    """
    Projection  types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "no projection"
       "Normal", "face normal"
       "Vector", "specify vector"
       "View", "view plane"
       "Xyz", "specify x,y,z plane"
    """
    NotSet = 0  # SurfaceIntersectionBuilderProjectionTypesMemberType
    Normal = 1  # SurfaceIntersectionBuilderProjectionTypesMemberType
    Vector = 2  # SurfaceIntersectionBuilderProjectionTypesMemberType
    View = 3  # SurfaceIntersectionBuilderProjectionTypesMemberType
    Xyz = 4  # SurfaceIntersectionBuilderProjectionTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceIntersectionBuilderXyzTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceIntersectionBuilderXyzTypes():
    """
    Enumeration for X, Y or Z projection plane 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", "x-axis plane"
       "Y", "y-axis plane"
       "Z", "z-axis plane"
    """
    X = 0  # SurfaceIntersectionBuilderXyzTypesMemberType
    Y = 1  # SurfaceIntersectionBuilderXyzTypesMemberType
    Z = 2  # SurfaceIntersectionBuilderXyzTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceIntersectionBuilderNormalTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceIntersectionBuilderNormalTypes():
    """
    Enumeration for face normal 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FaceSet1", "linear needle"
       "FaceSet2", "logarithmic needle"
    """
    FaceSet1 = 0  # SurfaceIntersectionBuilderNormalTypesMemberType
    FaceSet2 = 1  # SurfaceIntersectionBuilderNormalTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceIntersectionBuilderLabelValuesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceIntersectionBuilderLabelValues():
    """
    Enumeration for label computation method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Curvature", "label showing curvature value"
       "RadiusOfCurvature", "label showing radius of curvature value"
    """
    Curvature = 0  # SurfaceIntersectionBuilderLabelValuesMemberType
    RadiusOfCurvature = 1  # SurfaceIntersectionBuilderLabelValuesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceIntersectionBuilderDirectionTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceIntersectionBuilderDirectionTypes():
    """
    Enumeration for needle direction type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", "needle pointing inside"
       "Outside", "needle pointing outside"
    """
    Inside = 0  # SurfaceIntersectionBuilderDirectionTypesMemberType
    Outside = 1  # SurfaceIntersectionBuilderDirectionTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceIntersectionBuilderCalculationTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceIntersectionBuilderCalculationTypes():
    """
    Enumeration for needle calculation method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Curvature", "needle of curvature value"
       "RadiusofCurvature", "needle of radius of curvature value"
    """
    Curvature = 0  # SurfaceIntersectionBuilderCalculationTypesMemberType
    RadiusofCurvature = 1  # SurfaceIntersectionBuilderCalculationTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceIntersectionBuilderScalingTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceIntersectionBuilderScalingTypes():
    """
    Enumeration for needle display type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "linear needle"
       "Logarithmic", "logarithmic needle"
    """
    Linear = 0  # SurfaceIntersectionBuilderScalingTypesMemberType
    Logarithmic = 1  # SurfaceIntersectionBuilderScalingTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceIntersectionBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersection` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateSurfaceIntersectionBuilder`
    
    Default values.
    
    =====================  ==========
    Property               Value
    =====================  ==========
    CalculationMethod      Curvature 
    ---------------------  ----------
    DynamicProjection      1 
    ---------------------  ----------
    NeedleDirection        Outside 
    ---------------------  ----------
    ProjectionNormalFace   FaceSet1 
    ---------------------  ----------
    ProjectionOption       None 
    ---------------------  ----------
    ProjectionXYZ          X 
    ---------------------  ----------
    ScalingMethod          Linear 
    =====================  ==========
    
    .. versionadded:: NX7.5.0
    """
    
    class ProjectionTypes():
        """
        Projection  types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "no projection"
           "Normal", "face normal"
           "Vector", "specify vector"
           "View", "view plane"
           "Xyz", "specify x,y,z plane"
        """
        NotSet = 0  # SurfaceIntersectionBuilderProjectionTypesMemberType
        Normal = 1  # SurfaceIntersectionBuilderProjectionTypesMemberType
        Vector = 2  # SurfaceIntersectionBuilderProjectionTypesMemberType
        View = 3  # SurfaceIntersectionBuilderProjectionTypesMemberType
        Xyz = 4  # SurfaceIntersectionBuilderProjectionTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class XyzTypes():
        """
        Enumeration for X, Y or Z projection plane 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "X", "x-axis plane"
           "Y", "y-axis plane"
           "Z", "z-axis plane"
        """
        X = 0  # SurfaceIntersectionBuilderXyzTypesMemberType
        Y = 1  # SurfaceIntersectionBuilderXyzTypesMemberType
        Z = 2  # SurfaceIntersectionBuilderXyzTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class NormalTypes():
        """
        Enumeration for face normal 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FaceSet1", "linear needle"
           "FaceSet2", "logarithmic needle"
        """
        FaceSet1 = 0  # SurfaceIntersectionBuilderNormalTypesMemberType
        FaceSet2 = 1  # SurfaceIntersectionBuilderNormalTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LabelValues():
        """
        Enumeration for label computation method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Curvature", "label showing curvature value"
           "RadiusOfCurvature", "label showing radius of curvature value"
        """
        Curvature = 0  # SurfaceIntersectionBuilderLabelValuesMemberType
        RadiusOfCurvature = 1  # SurfaceIntersectionBuilderLabelValuesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DirectionTypes():
        """
        Enumeration for needle direction type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", "needle pointing inside"
           "Outside", "needle pointing outside"
        """
        Inside = 0  # SurfaceIntersectionBuilderDirectionTypesMemberType
        Outside = 1  # SurfaceIntersectionBuilderDirectionTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CalculationTypes():
        """
        Enumeration for needle calculation method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Curvature", "needle of curvature value"
           "RadiusofCurvature", "needle of radius of curvature value"
        """
        Curvature = 0  # SurfaceIntersectionBuilderCalculationTypesMemberType
        RadiusofCurvature = 1  # SurfaceIntersectionBuilderCalculationTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ScalingTypes():
        """
        Enumeration for needle display type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "linear needle"
           "Logarithmic", "logarithmic needle"
        """
        Linear = 0  # SurfaceIntersectionBuilderScalingTypesMemberType
        Logarithmic = 1  # SurfaceIntersectionBuilderScalingTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def UpdateWorkView(self) -> None:
        """
        Update work view with a given view matrix 
        
        Signature ``UpdateWorkView()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    CalculationMethod: SurfaceIntersectionBuilderCalculationTypes = ...
    """
    Returns or sets  the calculation method 
    
    <hr>
    
    Getter Method
    
    Signature ``CalculationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderCalculationTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CalculationMethod`` 
    
    :param calculationMethod: 
    :type calculationMethod: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderCalculationTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    CombOptions: NXOpen.GeometricUtilities.CombOptionsBuilder = ...
    """
    Returns  the comb display block options 
    
    <hr>
    
    Getter Method
    
    Signature ``CombOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.CombOptionsBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    DynamicProjection: bool = ...
    """
    Returns or sets  the dynamic projection 
    
    <hr>
    
    Getter Method
    
    Signature ``DynamicProjection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DynamicProjection`` 
    
    :param dynamicProjection: 
    :type dynamicProjection: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    FirstFaceSet: NXOpen.ScCollector = ...
    """
    Returns  the first selected face set 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstFaceSet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    NeedleDirection: SurfaceIntersectionBuilderDirectionTypes = ...
    """
    Returns or sets  the needle direction 
    
    <hr>
    
    Getter Method
    
    Signature ``NeedleDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderDirectionTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NeedleDirection`` 
    
    :param needleDirection: 
    :type needleDirection: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderDirectionTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ProjectionNormalFace: SurfaceIntersectionBuilderNormalTypes = ...
    """
    Returns or sets  the face normal projection 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectionNormalFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderNormalTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectionNormalFace`` 
    
    :param normalFace: 
    :type normalFace: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderNormalTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ProjectionOption: SurfaceIntersectionBuilderProjectionTypes = ...
    """
    Returns or sets  the projection option
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderProjectionTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectionOption`` 
    
    :param projectionOption: 
    :type projectionOption: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderProjectionTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ProjectionXYZ: SurfaceIntersectionBuilderXyzTypes = ...
    """
    Returns or sets  the xyz projection 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectionXYZ`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderXyzTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectionXYZ`` 
    
    :param projectionXYZ: 
    :type projectionXYZ: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderXyzTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ScalingMethod: SurfaceIntersectionBuilderScalingTypes = ...
    """
    Returns or sets  the scaling method 
    
    <hr>
    
    Getter Method
    
    Signature ``ScalingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderScalingTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScalingMethod`` 
    
    :param scalingMethod: 
    :type scalingMethod: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderScalingTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SecondFaceSet: NXOpen.ScCollector = ...
    """
    Returns  the second selected face set 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondFaceSet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the vector 
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vector: 
    :type vector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: SurfaceIntersectionBuilder = ...  # unknown typename


class DeviationCheckingDeviationOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DeviationCheckingDeviationOptions():
    """
    the deviation type to be shown 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoDeviations", "show no deviations"
       "AllDeviations", "show all deviations"
       "MaximumDistance", "show maximum distance deviation"
       "MinimumDistance", "show minimum distance deviation"
       "MaximumAngle", "show maximum angle deviation"
       "MinimumAngle", "show minimum angle deviation"
    """
    NoDeviations = 0  # DeviationCheckingDeviationOptionsMemberType
    AllDeviations = 1  # DeviationCheckingDeviationOptionsMemberType
    MaximumDistance = 2  # DeviationCheckingDeviationOptionsMemberType
    MinimumDistance = 3  # DeviationCheckingDeviationOptionsMemberType
    MaximumAngle = 4  # DeviationCheckingDeviationOptionsMemberType
    MinimumAngle = 5  # DeviationCheckingDeviationOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DeviationCheckingTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DeviationCheckingTypes():
    """
    the type of deviation checking to be performed 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CurveToCurve", "check curve/edge to curve/edge deviation"
       "CurveToFace", "check curve/edge to face deviation"
       "EdgeToFace", "check edge to face deviation"
       "FaceToFace", "check face to face deviation"
       "EdgeToEdge", "check edge to edge deviation"
    """
    CurveToCurve = 0  # DeviationCheckingTypesMemberType
    CurveToFace = 1  # DeviationCheckingTypesMemberType
    EdgeToFace = 2  # DeviationCheckingTypesMemberType
    FaceToFace = 3  # DeviationCheckingTypesMemberType
    EdgeToEdge = 4  # DeviationCheckingTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DeviationChecking(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.GeometricAnalysis.DeviationChecking`
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisManager.CreateDeviationCheckingObject`
    
    .. versionadded:: NX6.0.0
    """
    
    class DeviationOptions():
        """
        the deviation type to be shown 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoDeviations", "show no deviations"
           "AllDeviations", "show all deviations"
           "MaximumDistance", "show maximum distance deviation"
           "MinimumDistance", "show minimum distance deviation"
           "MaximumAngle", "show maximum angle deviation"
           "MinimumAngle", "show minimum angle deviation"
        """
        NoDeviations = 0  # DeviationCheckingDeviationOptionsMemberType
        AllDeviations = 1  # DeviationCheckingDeviationOptionsMemberType
        MaximumDistance = 2  # DeviationCheckingDeviationOptionsMemberType
        MinimumDistance = 3  # DeviationCheckingDeviationOptionsMemberType
        MaximumAngle = 4  # DeviationCheckingDeviationOptionsMemberType
        MinimumAngle = 5  # DeviationCheckingDeviationOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Types():
        """
        the type of deviation checking to be performed 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CurveToCurve", "check curve/edge to curve/edge deviation"
           "CurveToFace", "check curve/edge to face deviation"
           "EdgeToFace", "check edge to face deviation"
           "FaceToFace", "check face to face deviation"
           "EdgeToEdge", "check edge to edge deviation"
        """
        CurveToCurve = 0  # DeviationCheckingTypesMemberType
        CurveToFace = 1  # DeviationCheckingTypesMemberType
        EdgeToFace = 2  # DeviationCheckingTypesMemberType
        FaceToFace = 3  # DeviationCheckingTypesMemberType
        EdgeToEdge = 4  # DeviationCheckingTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Check(self) -> None:
        """
        Performs deviation checking.  
        
        Before calling this method, set
        property :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` to specify the type of 
        deviation checking, and the two objects (curve/face/edge) to be used the deviation
        checking. The type of the objects required
        depends on :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` set above. Also set the
        number check points to be displayed or u and v check points, the
        distance tolerance, and the angle tolerance before calling the
        method :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Check`. 
        :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Check` displays the
        deviation as per the specification above in the graphics and lists
        in the information window of NX.
        
        Signature ``Check()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    AngleTolerance: float = ...
    """
    Returns or sets  the angle tolerance to be used for the deviation checking 
    
    <hr>
    
    Getter Method
    
    Signature ``AngleTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AngleTolerance`` 
    
    :param angleTolerance: 
    :type angleTolerance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Curve: NXOpen.SelectIBaseCurve = ...
    """
    Returns  the curve  - required for the deviation checking when
    :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.CurveToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``Curve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectIBaseCurve` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    DeviationOption: DeviationCheckingDeviationOptions = ...
    """
    Returns or sets  the number or type of deviations to be shown for the deviation checking 
    
    <hr>
    
    Getter Method
    
    Signature ``DeviationOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingDeviationOptions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DeviationOption`` 
    
    :param deviationOption: 
    :type deviationOption: :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingDeviationOptions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance to be used for the deviation checking 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    FaceOfFirstEdge: NXOpen.SelectIParameterizedSurface = ...
    """
    Returns  the face associated with the first edge or edge  - required for the deviation checking when
    :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.EdgeToEdge <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`
    or
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.EdgeToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceOfFirstEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectIParameterizedSurface` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    FaceOfSecondEdge: NXOpen.SelectIParameterizedSurface = ...
    """
    Returns  the face associated with the second edge  - required for the deviation checking when
    :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.EdgeToEdge <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceOfSecondEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectIParameterizedSurface` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    FirstCurve: NXOpen.SelectIBaseCurve = ...
    """
    Returns  the first curve or edge - required for the deviation checking when
    :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.CurveToCurve <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``FirstCurve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectIBaseCurve` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    FirstEdge: NXOpen.SelectIBaseCurve = ...
    """
    Returns  the first edge or edge  - required for the deviation checking when
    :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.EdgeToEdge <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`
    or
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.EdgeToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``FirstEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectIBaseCurve` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    FirstFace: NXOpen.SelectIParameterizedSurface = ...
    """
    Returns  the first face - required for the deviation checking when
    :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.FaceToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``FirstFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectIParameterizedSurface` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    NumberCheckPoints: int = ...
    """
    Returns or sets  the number of check points to be shown for the deviation checking  -
    required when :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.CurveToCurve <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`
    or
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.CurveToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`
    or
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.EdgeToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`
    or
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.EdgeToEdge <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberCheckPoints`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberCheckPoints`` 
    
    :param numberCheckPoints: 
    :type numberCheckPoints: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    NumberUcheckPoints: int = ...
    """
    Returns or sets  the number of u check points to be shown for the deviation checking
    - required when :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.FaceToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`
    
    <hr>
    
    Getter Method
    
    Signature ``NumberUcheckPoints`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberUcheckPoints`` 
    
    :param numberUCheckPoints: 
    :type numberUCheckPoints: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    NumberVcheckPoints: int = ...
    """
    Returns or sets  the number of v check points to be shown for the deviation checking
    - required when :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.FaceToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`
    
    <hr>
    
    Getter Method
    
    Signature ``NumberVcheckPoints`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberVcheckPoints`` 
    
    :param numberVCheckPoints: 
    :type numberVCheckPoints: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SecondCurve: NXOpen.SelectIBaseCurve = ...
    """
    Returns  the second curve or edge - required for the deviation checking when
    :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.CurveToCurve <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``SecondCurve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectIBaseCurve` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SecondEdge: NXOpen.SelectIBaseCurve = ...
    """
    Returns  the second edge - required for the deviation checking when
    :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.EdgeToEdge <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``SecondEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectIBaseCurve` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SecondFace: NXOpen.SelectIParameterizedSurface = ...
    """
    Returns  the second face - required for the deviation checking when
    :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.FaceToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`
    or the face  - required for the deviation checking when :py:meth:`NXOpen.GeometricAnalysis.DeviationChecking.Type`` is set to
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.CurveToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`
    or
    :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes.EdgeToFace <NXOpen.GeometricAnalysis.DeviationCheckingTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``SecondFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectIParameterizedSurface` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Type: DeviationCheckingTypes = ...
    """
    Returns or sets  the deviation checking type.  
    
    Depending on the value of the deviation
    checking type, different inputs are required. See the
    documentation for each of the inputs. 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.GeometricAnalysis.DeviationCheckingTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: DeviationChecking = ...  # unknown typename


class ExamineGeometryCheckMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ExamineGeometryCheck():
    """
    Types of checks 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ObjectTiny", "ObjectTiny"
       "ObjectMisaligned", "ObjectMisaligned"
       "BodyDataStructures", "BodyDataStructures"
       "BodyConsistency", "BodyConsistency"
       "BodyFaceIntersections", "BodyFaceIntersections"
       "BodySheetBoundaries", "BodySheetBoundaries"
       "FaceSmoothness", "FaceSmoothness"
       "FaceSelfIntersection", "FaceSelfIntersection"
       "FaceSpikesCuts", "FaceSpikesCuts"
       "EdgeSmoothness", "EdgeSmoothness"
       "EdgeTolerances", "EdgeTolerances"
       "NumChecks", "Number of Checks"
    """
    ObjectTiny = 0  # ExamineGeometryCheckMemberType
    ObjectMisaligned = 1  # ExamineGeometryCheckMemberType
    BodyDataStructures = 2  # ExamineGeometryCheckMemberType
    BodyConsistency = 3  # ExamineGeometryCheckMemberType
    BodyFaceIntersections = 4  # ExamineGeometryCheckMemberType
    BodySheetBoundaries = 5  # ExamineGeometryCheckMemberType
    FaceSmoothness = 6  # ExamineGeometryCheckMemberType
    FaceSelfIntersection = 7  # ExamineGeometryCheckMemberType
    FaceSpikesCuts = 8  # ExamineGeometryCheckMemberType
    EdgeSmoothness = 9  # ExamineGeometryCheckMemberType
    EdgeTolerances = 10  # ExamineGeometryCheckMemberType
    NumChecks = 11  # ExamineGeometryCheckMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ExamineGeometry(NXOpen.Builder):
    """
    Represents the Examine Geometry class
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisManager.CreateExamineGeometryObject`
    
    .. versionadded:: NX5.0.0
    """
    
    class Check():
        """
        Types of checks 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ObjectTiny", "ObjectTiny"
           "ObjectMisaligned", "ObjectMisaligned"
           "BodyDataStructures", "BodyDataStructures"
           "BodyConsistency", "BodyConsistency"
           "BodyFaceIntersections", "BodyFaceIntersections"
           "BodySheetBoundaries", "BodySheetBoundaries"
           "FaceSmoothness", "FaceSmoothness"
           "FaceSelfIntersection", "FaceSelfIntersection"
           "FaceSpikesCuts", "FaceSpikesCuts"
           "EdgeSmoothness", "EdgeSmoothness"
           "EdgeTolerances", "EdgeTolerances"
           "NumChecks", "Number of Checks"
        """
        ObjectTiny = 0  # ExamineGeometryCheckMemberType
        ObjectMisaligned = 1  # ExamineGeometryCheckMemberType
        BodyDataStructures = 2  # ExamineGeometryCheckMemberType
        BodyConsistency = 3  # ExamineGeometryCheckMemberType
        BodyFaceIntersections = 4  # ExamineGeometryCheckMemberType
        BodySheetBoundaries = 5  # ExamineGeometryCheckMemberType
        FaceSmoothness = 6  # ExamineGeometryCheckMemberType
        FaceSelfIntersection = 7  # ExamineGeometryCheckMemberType
        FaceSpikesCuts = 8  # ExamineGeometryCheckMemberType
        EdgeSmoothness = 9  # ExamineGeometryCheckMemberType
        EdgeTolerances = 10  # ExamineGeometryCheckMemberType
        NumChecks = 11  # ExamineGeometryCheckMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetAllChecks(self) -> None:
        """
        Set all types of checks to examine 
        
        Signature ``SetAllChecks()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearAllChecks(self) -> None:
        """
        Clear or unset all types of checks 
        
        Signature ``ClearAllChecks()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCheck(self, check: ExamineGeometryCheck) -> None:
        """
        Set a specified type of check for examine geometry 
        
        Signature ``SetCheck(check)`` 
        
        :param check:  Type of Check  
        :type check: :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearCheck(self, check: ExamineGeometryCheck) -> None:
        """
        Clear or unset a specified type of check 
        
        Signature ``ClearCheck(check)`` 
        
        :param check:  Type of Check  
        :type check: :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Examine(self) -> None:
        """
        Examines the geometry.  
        
        Before calling this method, use 
        :py:meth:`NXOpen.GeometricAnalysis.ExamineGeometry.SetCheck` and :py:meth:`NXOpen.GeometricAnalysis.ExamineGeometry.ClearCheck` 
        to specify which checks to perform and use :py:meth:`NXOpen.GeometricAnalysis.ExamineGeometry.ObjectsToExamine` 
        to specify which objects to examine.  After calling this method, 
        use :py:meth:`NXOpen.GeometricAnalysis.ExamineGeometry.GetResults` and 
        :py:meth:`NXOpen.GeometricAnalysis.ExamineGeometry.GetFailedObjects` to get the results. 
        
        Signature ``Examine()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetResults(self) -> 'list[int]':
        """
        Returns an array containing the number of objects that failed each check.  
        
        You should call :py:meth:`NXOpen.GeometricAnalysis.ExamineGeometry.Examine` before calling this 
        method.    The array contains an entry for each check in the
        :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` enumeration.  The nth item in the array corresponds to
        the nth check in the :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` enumeration.  For example, the 
        first item in the array is the number of objects that failed the 
        :py:class:`GeometricAnalysis.ExamineGeometryCheck.ObjectTiny <GeometricAnalysis.ExamineGeometryCheck>` check.  
        The corresponding entry in the array will be as follows:
        
          *  **-1</b>    errors
          *  **0</b>    Check not performed as check is not selected
          *  **-2</b>    a type of :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` is selected, no objects relevant to that type 
        of :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` are selected. For example, no bodies are selected yet the 
        :py:class:`GeometricAnalysis.ExamineGeometryCheck.BodyDataStructures <GeometricAnalysis.ExamineGeometryCheck>` check is
        set or selected. 
          *  **-3</b>    :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` not performed as other relevant :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` failed. This occurs when 
        :py:class:`GeometricAnalysis.ExamineGeometryCheck.BodyConsistency <GeometricAnalysis.ExamineGeometryCheck>`
        and/or :py:class:`GeometricAnalysis.ExamineGeometryCheck.BodyFaceIntersections <GeometricAnalysis.ExamineGeometryCheck>` check is set along with 
        :py:class:`GeometricAnalysis.ExamineGeometryCheck.BodyDataStructures <GeometricAnalysis.ExamineGeometryCheck>` check.
        If :py:class:`GeometricAnalysis.ExamineGeometryCheck.BodyDataStructures <GeometricAnalysis.ExamineGeometryCheck>` check
        failed, :py:class:`GeometricAnalysis.ExamineGeometryCheck.BodyConsistency <GeometricAnalysis.ExamineGeometryCheck>`
        and/or
        :py:class:`GeometricAnalysis.ExamineGeometryCheck.BodyFaceIntersections <GeometricAnalysis.ExamineGeometryCheck>` will
        not be performed.  
        
        Signature ``GetResults()`` 
        
        :returns:  Results of Examine Geometry  
        :rtype: list of int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFailedObjects(self, check: ExamineGeometryCheck) -> 'list[NXOpen.NXObject]':
        """
        Returns the objects that failed a given type of check.  
        
        You should 
        call :py:meth:`NXOpen.GeometricAnalysis.ExamineGeometry.Examine` before calling this method.    
        
        Signature ``GetFailedObjects(check)`` 
        
        :param check:  Type of Check  
        :type check: :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` 
        :returns:  Objects that
        failed above check during Examine Geometry  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def HighlightResult(self, check: ExamineGeometryCheck) -> bool:
        """
        Highlights results of a specified type of check.  
        
        If the
        highlighting fails for some of the entities, it returns True, otherwise
        False.  Highlighting can fail when the entities are corrupt or missing
        the information needed to display properly. Remaining entities are highlighted 
        when highlighting fails for some entities.  
        
        Signature ``HighlightResult(check)`` 
        
        :param check:  Type of Check  
        :type check: :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` 
        :returns:  Return status of the method.
        If return values equals
        false, display was successful. 
        if return value is true,
        display of some objects
        failed.  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UnhighlightResult(self, check: ExamineGeometryCheck) -> None:
        """
        Unhighlight results of a specified type of check
        
        Signature ``UnhighlightResult(check)`` 
        
        :param check:  Type of Check  
        :type check: :py:class:`NXOpen.GeometricAnalysis.ExamineGeometryCheck` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UnhighlightAllResults(self) -> None:
        """
        Unhighlight all results 
        
        Signature ``UnhighlightAllResults()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayResultsAsInfo(self) -> None:
        """
        Displays the results in the information window 
        
        Signature ``DisplayResultsAsInfo()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    CheckCriteriaAngle: float = ...
    """
    Returns or sets  the Check Criteria Angle 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckCriteriaAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckCriteriaAngle`` 
    
    :param angle: 
    :type angle: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CheckCriteriaDistance: float = ...
    """
    Returns or sets  the Check Criteria Distance 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckCriteriaDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckCriteriaDistance`` 
    
    :param distance: 
    :type distance: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ObjectsToExamine: NXOpen.SelectObjectList = ...
    """
    Returns  the Objects to examine 
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectsToExamine`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectObjectList` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: ExamineGeometry = ...  # unknown typename


class CurveAnalysisCombsBuilderDirectionOptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveAnalysisCombsBuilderDirectionOptionType():
    """
    Direction option types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "no direction"
       "PlaneOfCurve", "best fit plane"
       "SpecifyVector", "specify vector"
       "WorkView", "work view"
    """
    NotSet = 0  # CurveAnalysisCombsBuilderDirectionOptionTypeMemberType
    PlaneOfCurve = 1  # CurveAnalysisCombsBuilderDirectionOptionTypeMemberType
    SpecifyVector = 2  # CurveAnalysisCombsBuilderDirectionOptionTypeMemberType
    WorkView = 3  # CurveAnalysisCombsBuilderDirectionOptionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveAnalysisCombsBuilder(NXOpen.Builder):
    """
    This class handles the options setting for the curve analysis information (Curvature Combs) display.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateCurveAnalysisCombsBuilder`
    
    Default values.
    
    ==========================  ======
    Property                    Value
    ==========================  ======
    CurveRange.AnchorPosition   Start 
    ==========================  ======
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX8.5.0
       Use :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysis`.
    """
    
    class DirectionOptionType():
        """
        Direction option types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "no direction"
           "PlaneOfCurve", "best fit plane"
           "SpecifyVector", "specify vector"
           "WorkView", "work view"
        """
        NotSet = 0  # CurveAnalysisCombsBuilderDirectionOptionTypeMemberType
        PlaneOfCurve = 1  # CurveAnalysisCombsBuilderDirectionOptionTypeMemberType
        SpecifyVector = 2  # CurveAnalysisCombsBuilderDirectionOptionTypeMemberType
        WorkView = 3  # CurveAnalysisCombsBuilderDirectionOptionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def UpdateCurves(self) -> None:
        """
        This method should be called after the selected curves have changed 
        
        Signature ``UpdateCurves()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    CombOptions: NXOpen.GeometricUtilities.CombOptionsBuilder = ...
    """
    Returns  the comb options 
    
    <hr>
    
    Getter Method
    
    Signature ``CombOptions`` 
    
    :returns:  comb options  
    :rtype: :py:class:`NXOpen.GeometricUtilities.CombOptionsBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    CurveRange: NXOpen.GeometricUtilities.CurveRangeBuilder = ...
    """
    Returns  the curve range 
    
    <hr>
    
    Getter Method
    
    Signature ``CurveRange`` 
    
    :returns:  curve range  
    :rtype: :py:class:`NXOpen.GeometricUtilities.CurveRangeBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    DirectionOption: CurveAnalysisCombsBuilderDirectionOptionType = ...
    """
    Returns or sets  the direction option 
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisCombsBuilderDirectionOptionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionOption`` 
    
    :param option: 
    :type option: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisCombsBuilderDirectionOptionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SelectedCurves: NXOpen.ScCollector = ...
    """
    Returns  the selected curves 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedCurves`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the vector 
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vect: 
    :type vect: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Null: CurveAnalysisCombsBuilder = ...  # unknown typename


class DraftAnalysisBuilderDrawDirectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DraftAnalysisBuilderDrawDirection():
    """
    define draw direction items 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Vector", "vector;"
       "Orientation", "orientation;"
    """
    Vector = 0  # DraftAnalysisBuilderDrawDirectionMemberType
    Orientation = 1  # DraftAnalysisBuilderDrawDirectionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DraftAnalysisBuilderSelectOutputMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DraftAnalysisBuilderSelectOutput():
    """
    define output options 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AnalysisObject", "analysis object;"
       "Isoclines", "isoclines;"
       "Both", "analysis object and isoclines;"
    """
    AnalysisObject = 0  # DraftAnalysisBuilderSelectOutputMemberType
    Isoclines = 1  # DraftAnalysisBuilderSelectOutputMemberType
    Both = 2  # DraftAnalysisBuilderSelectOutputMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DraftAnalysisBuilder(NXOpen.Builder):
    """
    Represents a Draft Analysis builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateDraftAnalysisBuilder`
    
    Default values.
    
    ============================  ===============
    Property                      Value
    ============================  ===============
    CoupleLimit                   1 
    ----------------------------  ---------------
    CreateCSYS                    0 
    ----------------------------  ---------------
    DrawOption                    Orientation 
    ----------------------------  ---------------
    JoinIsocline                  0 
    ----------------------------  ---------------
    LimitAngleNegative            -5 
    ----------------------------  ---------------
    LimitAnglePositive            5 
    ----------------------------  ---------------
    OutputOption                  AnalysisObject 
    ----------------------------  ---------------
    Resolution.AngleTolerance     15.0 
    ----------------------------  ---------------
    Resolution.EdgeTolerance      0.005 
    ----------------------------  ---------------
    Resolution.FaceTolerance      0.005 
    ----------------------------  ---------------
    Resolution.Resolution         Standard 
    ----------------------------  ---------------
    Resolution.WidthTolerance     0.3 
    ----------------------------  ---------------
    ShowIsoclineNegative          0 
    ----------------------------  ---------------
    ShowIsoclinePositive          0 
    ----------------------------  ---------------
    ShowPartingLine               0 
    ----------------------------  ---------------
    TranslucencyInsideNegative    0 
    ----------------------------  ---------------
    TranslucencyInsidePositive    0 
    ----------------------------  ---------------
    TranslucencyOutsideNegative   0 
    ----------------------------  ---------------
    TranslucencyOutsidePositive   0 
    ============================  ===============
    
    .. versionadded:: NX8.0.0
    """
    
    class DrawDirection():
        """
        define draw direction items 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Vector", "vector;"
           "Orientation", "orientation;"
        """
        Vector = 0  # DraftAnalysisBuilderDrawDirectionMemberType
        Orientation = 1  # DraftAnalysisBuilderDrawDirectionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SelectOutput():
        """
        define output options 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AnalysisObject", "analysis object;"
           "Isoclines", "isoclines;"
           "Both", "analysis object and isoclines;"
        """
        AnalysisObject = 0  # DraftAnalysisBuilderSelectOutputMemberType
        Isoclines = 1  # DraftAnalysisBuilderSelectOutputMemberType
        Both = 2  # DraftAnalysisBuilderSelectOutputMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def ReverseAllNormals(self) -> None:
        """
        Reverses all normals 
        
        Signature ``ReverseAllNormals()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def GetColorOutsidePositive(self) -> 'list[float]':
        """
        Returns the positive outside color  
        
        Signature ``GetColorOutsidePositive()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColorOutsidePositive(self, colorOutsidePos: 'list[float]') -> None:
        """
        Sets the positive outside color 
        
        Signature ``SetColorOutsidePositive(colorOutsidePos)`` 
        
        :param colorOutsidePos:  Array of 3 RGB values, each between 0 and 1  
        :type colorOutsidePos: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def GetColorInsidePositive(self) -> 'list[float]':
        """
        Returns the positive inside color  
        
        Signature ``GetColorInsidePositive()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColorInsidePositive(self, colorInsidePos: 'list[float]') -> None:
        """
        Sets the positive inside color 
        
        Signature ``SetColorInsidePositive(colorInsidePos)`` 
        
        :param colorInsidePos:  Array of 3 RGB values, each between 0 and 1  
        :type colorInsidePos: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def GetColorOutsideNegative(self) -> 'list[float]':
        """
        Returns the negative outside color  
        
        Signature ``GetColorOutsideNegative()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColorOutsideNegative(self, colorOutsideNeg: 'list[float]') -> None:
        """
        Sets the negative outside color 
        
        Signature ``SetColorOutsideNegative(colorOutsideNeg)`` 
        
        :param colorOutsideNeg:  Array of 3 RGB values, each between 0 and 1  
        :type colorOutsideNeg: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def GetColorInsideNegative(self) -> 'list[float]':
        """
        Returns the negative inside color  
        
        Signature ``GetColorInsideNegative()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColorInsideNegative(self, colorInsideNeg: 'list[float]') -> None:
        """
        Sets the negative inside color 
        
        Signature ``SetColorInsideNegative(colorInsideNeg)`` 
        
        :param colorInsideNeg:  Array of 3 RGB values, each between 0 and 1  
        :type colorInsideNeg: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def AddDynamicPoints(self) -> None:
        """
        Adds dynamic points to the draft analysis object 
        
        Signature ``AddDynamicPoints()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def SetTotalDynamicNormals(self, total: int) -> None:
        """
        Sets number of dynamic normals 
        
        Signature ``SetTotalDynamicNormals(total)`` 
        
        :param total: 
        :type total: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def SetDynamicNormal(self, index: int, normal: NXOpen.Vector3d) -> None:
        """
        Sets dynamic normal 
        
        Signature ``SetDynamicNormal(index, normal)`` 
        
        :param index: 
        :type index: int 
        :param normal: 
        :type normal: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def SetDynamicParent(self, index: int, parent: NXOpen.DisplayableObject) -> None:
        """
        Sets dynamic parent 
        
        Signature ``SetDynamicParent(index, parent)`` 
        
        :param index: 
        :type index: int 
        :param parent: 
        :type parent: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def ReverseNormal(self, face: NXOpen.DisplayableObject) -> None:
        """
        Reverses individual face normal 
        
        Signature ``ReverseNormal(face)`` 
        
        :param face: 
        :type face: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def DeselectFaces(self, faces: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Deselects faces 
        
        Signature ``DeselectFaces(faces)`` 
        
        :param faces: 
        :type faces: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def UpdateReverseMap(self) -> None:
        """
        Updates reverse map 
        
        Signature ``UpdateReverseMap()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def RemoveLabelParents(self, parents: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Removes dynamic label parents 
        
        Signature ``RemoveLabelParents(parents)`` 
        
        :param parents: 
        :type parents: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def DeleteDynamicLabels(self, deletedLabels: 'list[bool]') -> None:
        """
        Deletes dynamic labels whose corresponding positions are set to true in the array 
        
        Signature ``DeleteDynamicLabels(deletedLabels)`` 
        
        :param deletedLabels: 
        :type deletedLabels: list of bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    CoupleLimit: bool = ...
    """
    Returns or sets  the coupling limit 
    
    <hr>
    
    Getter Method
    
    Signature ``CoupleLimit`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CoupleLimit`` 
    
    :param coupleLimit: 
    :type coupleLimit: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    CreateCSYS: bool = ...
    """
    Returns or sets  the datum CSYS creation 
    
    <hr>
    
    Getter Method
    
    Signature ``CreateCSYS`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateCSYS`` 
    
    :param createCSYS: 
    :type createCSYS: bool 
    
    .. versionadded:: NX8.0.1
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    DrawOption: DraftAnalysisBuilderDrawDirection = ...
    """
    Returns or sets  the draw option 
    
    <hr>
    
    Getter Method
    
    Signature ``DrawOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DraftAnalysisBuilderDrawDirection` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DrawOption`` 
    
    :param drawOption: 
    :type drawOption: :py:class:`NXOpen.GeometricAnalysis.DraftAnalysisBuilderDrawDirection` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    DrawOrientation: NXOpen.Matrix3x3 = ...
    """
    Returns or sets  the draw orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``DrawOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DrawOrientation`` 
    
    :param drawOrientation: 
    :type drawOrientation: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    DrawOrigin: NXOpen.Point3d = ...
    """
    Returns or sets  the draw origin 
    
    <hr>
    
    Getter Method
    
    Signature ``DrawOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DrawOrigin`` 
    
    :param drawOrigin: 
    :type drawOrigin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    DrawVector: NXOpen.Direction = ...
    """
    Returns or sets  the draw vector 
    
    <hr>
    
    Getter Method
    
    Signature ``DrawVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DrawVector`` 
    
    :param drawVector: 
    :type drawVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    DynamicLabel: NXOpen.Features.GeometricConstraintDataManager = ...
    """
    Returns  the constraint manager 
    
    <hr>
    
    Getter Method
    
    Signature ``DynamicLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.GeometricConstraintDataManager` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    JoinIsocline: bool = ...
    """
    Returns or sets  the joining isocline 
    
    <hr>
    
    Getter Method
    
    Signature ``JoinIsocline`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``JoinIsocline`` 
    
    :param joinIsocline: 
    :type joinIsocline: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    LimitAngleNegative: float = ...
    """
    Returns or sets  the negative limit angle 
    
    <hr>
    
    Getter Method
    
    Signature ``LimitAngleNegative`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LimitAngleNegative`` 
    
    :param limitAngleNeg: 
    :type limitAngleNeg: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    LimitAnglePositive: float = ...
    """
    Returns or sets  the positive limit angle 
    
    <hr>
    
    Getter Method
    
    Signature ``LimitAnglePositive`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LimitAnglePositive`` 
    
    :param limitAnglePos: 
    :type limitAnglePos: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    OutputOption: DraftAnalysisBuilderSelectOutput = ...
    """
    Returns or sets  the output option 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DraftAnalysisBuilderSelectOutput` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputOption`` 
    
    :param outputOption: 
    :type outputOption: :py:class:`NXOpen.GeometricAnalysis.DraftAnalysisBuilderSelectOutput` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Resolution: NXOpen.GeometricUtilities.DisplayResolutionBuilder = ...
    """
    Returns  the display resolution 
    
    <hr>
    
    Getter Method
    
    Signature ``Resolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.DisplayResolutionBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ReverseIndividual: NXOpen.SelectDisplayableObject = ...
    """
    Returns  the individual face normal
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseIndividual`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObject` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SelectObject: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the faces or facet bodies 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ShowIsoclineNegative: bool = ...
    """
    Returns or sets  the negative isocline 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowIsoclineNegative`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowIsoclineNegative`` 
    
    :param showIsoclineNeg: 
    :type showIsoclineNeg: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ShowIsoclinePositive: bool = ...
    """
    Returns or sets  the positive isocline 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowIsoclinePositive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowIsoclinePositive`` 
    
    :param showIsoclinePos: 
    :type showIsoclinePos: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ShowPartingLine: bool = ...
    """
    Returns or sets  the show parting line 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowPartingLine`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowPartingLine`` 
    
    :param showPartingLine: 
    :type showPartingLine: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    TranslucencyInsideNegative: int = ...
    """
    Returns or sets  the negative inside translucency 
    
    <hr>
    
    Getter Method
    
    Signature ``TranslucencyInsideNegative`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TranslucencyInsideNegative`` 
    
    :param translucencyInsideNeg: 
    :type translucencyInsideNeg: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    TranslucencyInsidePositive: int = ...
    """
    Returns or sets  the positive inside translucency 
    
    <hr>
    
    Getter Method
    
    Signature ``TranslucencyInsidePositive`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TranslucencyInsidePositive`` 
    
    :param translucencyInsidePos: 
    :type translucencyInsidePos: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    TranslucencyOutsideNegative: int = ...
    """
    Returns or sets  the negative outside tanslucency 
    
    <hr>
    
    Getter Method
    
    Signature ``TranslucencyOutsideNegative`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TranslucencyOutsideNegative`` 
    
    :param translucencyOutsideNeg: 
    :type translucencyOutsideNeg: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    TranslucencyOutsidePositive: int = ...
    """
    Returns or sets  the positive outside translucenty 
    
    <hr>
    
    Getter Method
    
    Signature ``TranslucencyOutsidePositive`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TranslucencyOutsidePositive`` 
    
    :param translucencyOutsidePos: 
    :type translucencyOutsidePos: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: DraftAnalysisBuilder = ...  # unknown typename


class SurfaceAnalysisDisplayShowFlagTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceAnalysisDisplayShowFlagType():
    """
    Show flag types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Pole", "show pole"
       "Knot", "show knot"
    """
    Pole = 0  # SurfaceAnalysisDisplayShowFlagTypeMemberType
    Knot = 1  # SurfaceAnalysisDisplayShowFlagTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SurfaceAnalysisDisplay():
    """
    Represents a tool control whether to show a surface's poles and knots   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.GeometricAnalysis.AnalysisObjectCollection`
    
    .. versionadded:: NX6.0.0
    """
    
    class ShowFlagType():
        """
        Show flag types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Pole", "show pole"
           "Knot", "show knot"
        """
        Pole = 0  # SurfaceAnalysisDisplayShowFlagTypeMemberType
        Knot = 1  # SurfaceAnalysisDisplayShowFlagTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetShowFlag(self, surface: NXOpen.DisplayableObject, choice: SurfaceAnalysisDisplayShowFlagType, on: bool) -> None:
        """
        Sets show flags 
        
        Signature ``SetShowFlag(surface, choice, on)`` 
        
        :param surface:  surface  
        :type surface: :py:class:`NXOpen.DisplayableObject` 
        :param choice:  pole/knot  
        :type choice: :py:class:`NXOpen.GeometricAnalysis.SurfaceAnalysisDisplayShowFlagType` 
        :param on:  true/false to show flags  
        :type on: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    


class FaceCurvatureAnalysisBuilderCurvatureTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FaceCurvatureAnalysisBuilderCurvatureTypes():
    """
    Represents the face curvature types. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Gaussian", "Gausssian"
       "Absolute", "Absolute"
       "Minimum", "Minimum"
       "Maximum", "Maximum"
       "Mean", "Mean"
       "Normal", "Normal"
       "Sectional", "Sectional"
       "U", "U"
       "V", "V"
    """
    Gaussian = 0  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
    Absolute = 1  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
    Minimum = 2  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
    Maximum = 3  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
    Mean = 4  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
    Normal = 5  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
    Sectional = 6  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
    U = 7  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
    V = 8  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FaceCurvatureAnalysisBuilderDisplayTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FaceCurvatureAnalysisBuilderDisplayTypes():
    """
    Represents the display types. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Colormap", "Color Map only"
       "Contours", "Contours"
       "ColormapAndContours", "Color Map and Contours"
    """
    Colormap = 0  # FaceCurvatureAnalysisBuilderDisplayTypesMemberType
    Contours = 1  # FaceCurvatureAnalysisBuilderDisplayTypesMemberType
    ColormapAndContours = 2  # FaceCurvatureAnalysisBuilderDisplayTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FaceCurvatureAnalysisBuilderScaleTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FaceCurvatureAnalysisBuilderScaleTypes():
    """
    Represents the scaling types for curvature values.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "Linear Scaling (No Scaling)"
       "Log", "Log Scaling"
       "Area", "Equalized by Area"
    """
    Linear = 0  # FaceCurvatureAnalysisBuilderScaleTypesMemberType
    Log = 1  # FaceCurvatureAnalysisBuilderScaleTypesMemberType
    Area = 2  # FaceCurvatureAnalysisBuilderScaleTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FaceCurvatureAnalysisBuilderDirectionTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FaceCurvatureAnalysisBuilderDirectionTypes():
    """
    Methods of specifiying the direction for normal and section curvatures.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Primitive", "vector or plane"
       "Manipulator", "orientation maninpulator"
    """
    Primitive = 0  # FaceCurvatureAnalysisBuilderDirectionTypesMemberType
    Manipulator = 1  # FaceCurvatureAnalysisBuilderDirectionTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FaceCurvatureAnalysisBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder` builder.  
    
    Use :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder` to compute different
    types of curvature analysis for selected faces.  The result of the curvature analysis is
    displayed as color maps and contour lines on the faces.  For more details see the NX
    documentation for Face Curvature Analysis.
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateFaceCurvatureAnalysisBuilder`
    
    Default values.
    
    ==========================  ============
    Property                    Value
    ==========================  ============
    ContourRefinement           0 
    --------------------------  ------------
    ContourShift                0 
    --------------------------  ------------
    DisplayType                 Colormap 
    --------------------------  ------------
    MapCenter                   50 
    --------------------------  ------------
    MapRange                    100 
    --------------------------  ------------
    NormalOption                Manipulator 
    --------------------------  ------------
    NumberOfContours            10 
    --------------------------  ------------
    Resolution.AngleTolerance   15.0 
    --------------------------  ------------
    Resolution.EdgeTolerance    0.005 
    --------------------------  ------------
    Resolution.FaceTolerance    0.005 
    --------------------------  ------------
    Resolution.Resolution       Standard 
    --------------------------  ------------
    Resolution.WidthTolerance   0.3 
    --------------------------  ------------
    SectionOption               Manipulator 
    --------------------------  ------------
    ShowZeroContour             0 
    ==========================  ============
    
    .. versionadded:: NX9.0.0
    """
    
    class CurvatureTypes():
        """
        Represents the face curvature types. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Gaussian", "Gausssian"
           "Absolute", "Absolute"
           "Minimum", "Minimum"
           "Maximum", "Maximum"
           "Mean", "Mean"
           "Normal", "Normal"
           "Sectional", "Sectional"
           "U", "U"
           "V", "V"
        """
        Gaussian = 0  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
        Absolute = 1  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
        Minimum = 2  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
        Maximum = 3  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
        Mean = 4  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
        Normal = 5  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
        Sectional = 6  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
        U = 7  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
        V = 8  # FaceCurvatureAnalysisBuilderCurvatureTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DisplayTypes():
        """
        Represents the display types. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Colormap", "Color Map only"
           "Contours", "Contours"
           "ColormapAndContours", "Color Map and Contours"
        """
        Colormap = 0  # FaceCurvatureAnalysisBuilderDisplayTypesMemberType
        Contours = 1  # FaceCurvatureAnalysisBuilderDisplayTypesMemberType
        ColormapAndContours = 2  # FaceCurvatureAnalysisBuilderDisplayTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ScaleTypes():
        """
        Represents the scaling types for curvature values.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "Linear Scaling (No Scaling)"
           "Log", "Log Scaling"
           "Area", "Equalized by Area"
        """
        Linear = 0  # FaceCurvatureAnalysisBuilderScaleTypesMemberType
        Log = 1  # FaceCurvatureAnalysisBuilderScaleTypesMemberType
        Area = 2  # FaceCurvatureAnalysisBuilderScaleTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DirectionTypes():
        """
        Methods of specifiying the direction for normal and section curvatures.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Primitive", "vector or plane"
           "Manipulator", "orientation maninpulator"
        """
        Primitive = 0  # FaceCurvatureAnalysisBuilderDirectionTypesMemberType
        Manipulator = 1  # FaceCurvatureAnalysisBuilderDirectionTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def ReverseAllNormals(self) -> None:
        """
        Reverses all normals.  
        
        Signature ``ReverseAllNormals()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def ReverseIndividualNormal(self, face: NXOpen.DisplayableObject) -> None:
        """
        Reverses an individual face normal.  
        
        Signature ``ReverseIndividualNormal(face)`` 
        
        :param face: 
        :type face: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def UpdateReverseMap(self) -> None:
        """
        Updates reverse map.  
        
        Signature ``UpdateReverseMap()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def DeselectFaces(self, faces: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Deselects faces 
        
        Signature ``DeselectFaces(faces)`` 
        
        :param faces: 
        :type faces: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    ContourRefinement: int = ...
    """
    Returns or sets  the contour refinement level, in the range 0-6.  
    
    Increasing values compute more detailed and 
    accurate contour lines on the face. 
    
    <hr>
    
    Getter Method
    
    Signature ``ContourRefinement`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContourRefinement`` 
    
    :param contourRefinement: 
    :type contourRefinement: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    ContourShift: float = ...
    """
    Returns or sets  the starting contour shift or bias value, as % of the standard contour interval.  
    
    Valid values are -100 to 100. 
    
    <hr>
    
    Getter Method
    
    Signature ``ContourShift`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContourShift`` 
    
    :param contourShift: 
    :type contourShift: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    CurvatureSectionPlane: NXOpen.Plane = ...
    """
    Returns or sets  the section curvature plane when sectional curvature values are to be computed and displayed.  
    
    <hr>
    
    Getter Method
    
    Signature ``CurvatureSectionPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurvatureSectionPlane`` 
    
    :param curvatureSectionPlane: 
    :type curvatureSectionPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    CurvatureType: FaceCurvatureAnalysisBuilderCurvatureTypes = ...
    """
    Returns or sets  the curvature type to compute and display.  
    
    <hr>
    
    Getter Method
    
    Signature ``CurvatureType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderCurvatureTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurvatureType`` 
    
    :param curvatureType: 
    :type curvatureType: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderCurvatureTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    DisplayType: FaceCurvatureAnalysisBuilderDisplayTypes = ...
    """
    Returns or sets  the display type for curvature values.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderDisplayTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayType`` 
    
    :param displayType: 
    :type displayType: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderDisplayTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    MapCenter: float = ...
    """
    Returns or sets  the center point of the color mapping and contouring, as % of the full range of
    curvature values present in the data.  
    
    <hr>
    
    Getter Method
    
    Signature ``MapCenter`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MapCenter`` 
    
    :param mapCenter: 
    :type mapCenter: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    MapRange: float = ...
    """
    Returns or sets  the color map and contour range, as % of the full range of curvature values present in the data.  
    
    <hr>
    
    Getter Method
    
    Signature ``MapRange`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MapRange`` 
    
    :param mapRange: 
    :type mapRange: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    NormalOption: FaceCurvatureAnalysisBuilderDirectionTypes = ...
    """
    Returns or sets  the normal for the case of normal curvature type.  
    
    <hr>
    
    Getter Method
    
    Signature ``NormalOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderDirectionTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NormalOption`` 
    
    :param normalOption: 
    :type normalOption: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderDirectionTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    NormalOrientation: NXOpen.Matrix3x3 = ...
    """
    Returns or sets  the normal orientation when the normal curvature values are to be computed and displayed.  
    
    <hr>
    
    Getter Method
    
    Signature ``NormalOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NormalOrientation`` 
    
    :param normalOrientation: 
    :type normalOrientation: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    NormalOrigin: NXOpen.Point3d = ...
    """
    Returns or sets  the normal origin when normal curvature values are to be computed and displayed.  
    
    <hr>
    
    Getter Method
    
    Signature ``NormalOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NormalOrigin`` 
    
    :param normalOrigin: 
    :type normalOrigin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    NormalVector: NXOpen.Direction = ...
    """
    Returns or sets  the normal vector for the case when normal curvature values are to be computed and displayed.  
    
    <hr>
    
    Getter Method
    
    Signature ``NormalVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NormalVector`` 
    
    :param normalVector: 
    :type normalVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    NumberOfContours: int = ...
    """
    Returns or sets  the number of contour lines to compute and display.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfContours`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfContours`` 
    
    :param numberOfContours: 
    :type numberOfContours: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Resolution: NXOpen.GeometricUtilities.DisplayResolutionBuilder = ...
    """
    Returns  the tesselation resolution to use for curvature color map and contours.  
    
    <hr>
    
    Getter Method
    
    Signature ``Resolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.DisplayResolutionBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ReverseIndividual: NXOpen.SelectDisplayableObject = ...
    """
    Returns  the individual face normal.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseIndividual`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObject` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ScaleType: FaceCurvatureAnalysisBuilderScaleTypes = ...
    """
    Returns or sets  the scaling type of curvature values.  
    
    <hr>
    
    Getter Method
    
    Signature ``ScaleType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderScaleTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScaleType`` 
    
    :param scaleType: 
    :type scaleType: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderScaleTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SectionOption: FaceCurvatureAnalysisBuilderDirectionTypes = ...
    """
    Returns or sets  whether to use a section plane or maninpulator for sectional curvatures.  
    
    <hr>
    
    Getter Method
    
    Signature ``SectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderDirectionTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SectionOption`` 
    
    :param sectionOption: 
    :type sectionOption: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderDirectionTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SectionOrientation: NXOpen.Matrix3x3 = ...
    """
    Returns or sets  the section orientation for sectional curvatures.  
    
    <hr>
    
    Getter Method
    
    Signature ``SectionOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SectionOrientation`` 
    
    :param sectionOrientation: 
    :type sectionOrientation: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SectionOrigin: NXOpen.Point3d = ...
    """
    Returns or sets  the section origin for sectional curvatures.  
    
    <hr>
    
    Getter Method
    
    Signature ``SectionOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SectionOrigin`` 
    
    :param sectionOrigin: 
    :type sectionOrigin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    SelectObject: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the faces on which to perform curvature analysis.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowZeroContour: bool = ...
    """
    Returns or sets  the option to show zero curvature contour line.  
    
    <hr>
    
    Getter Method
    
    Signature ``ShowZeroContour`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowZeroContour`` 
    
    :param showContour: 
    :type showContour: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: FaceCurvatureAnalysisBuilder = ...  # unknown typename


class CurveAnalysisRecordDirectionOptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveAnalysisRecordDirectionOptionType():
    """
    Direction option types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "no direction"
       "PlaneOfCurve", "best fit plane"
       "SpecifyVector", "specify vector"
       "WorkView", "work view"
    """
    NotSet = 0  # CurveAnalysisRecordDirectionOptionTypeMemberType
    PlaneOfCurve = 1  # CurveAnalysisRecordDirectionOptionTypeMemberType
    SpecifyVector = 2  # CurveAnalysisRecordDirectionOptionTypeMemberType
    WorkView = 3  # CurveAnalysisRecordDirectionOptionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveAnalysisRecord(NXOpen.TransientObject):
    """
    Represents the information regarding how to display a curve's poles, knots, combs, peaks and inflections   
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX8.5.0
       Use :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisDisplay`.
    """
    
    class DirectionOptionType():
        """
        Direction option types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "no direction"
           "PlaneOfCurve", "best fit plane"
           "SpecifyVector", "specify vector"
           "WorkView", "work view"
        """
        NotSet = 0  # CurveAnalysisRecordDirectionOptionTypeMemberType
        PlaneOfCurve = 1  # CurveAnalysisRecordDirectionOptionTypeMemberType
        SpecifyVector = 2  # CurveAnalysisRecordDirectionOptionTypeMemberType
        WorkView = 3  # CurveAnalysisRecordDirectionOptionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
        Free resources associated with the instance.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    CombDensity: int = ...
    """
    Returns or sets  the comb density 
    
    <hr>
    
    Getter Method
    
    Signature ``CombDensity`` 
    
    :returns:  comb density  
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CombDensity`` 
    
    :param density:  comb density  
    :type density: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    CombInterneedleDensity: int = ...
    """
    Returns or sets  the comb interneedle density 
    
    <hr>
    
    Getter Method
    
    Signature ``CombInterneedleDensity`` 
    
    :returns:  comb interneedle density  
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CombInterneedleDensity`` 
    
    :param interneedleDensity:  comb interneedle density  
    :type interneedleDensity: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    CombMaxLength: float = ...
    """
    Returns or sets  the comb maximum length 
    
    <hr>
    
    Getter Method
    
    Signature ``CombMaxLength`` 
    
    :returns:  max length  
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CombMaxLength`` 
    
    :param maxLength:  max length  
    :type maxLength: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    CombScaleFactor: float = ...
    """
    Returns or sets  the comb scale factor 
    
    <hr>
    
    Getter Method
    
    Signature ``CombScaleFactor`` 
    
    :returns:  comb scale factor  
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CombScaleFactor`` 
    
    :param factor:  comb scale factor  
    :type factor: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Direction: NXOpen.Vector3d = ...
    """
    Returns or sets  the diection 
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns:  direction  
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction:  direction  
    :type direction: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    DirectionOption: CurveAnalysisRecordDirectionOptionType = ...
    """
    Returns or sets  the direction option 
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionOption`` 
    
    :returns:  direction option  
    :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisRecordDirectionOptionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionOption`` 
    
    :param directionOption:  direction option  
    :type directionOption: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisRecordDirectionOptionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    End: float = ...
    """
    Returns or sets  the end parameter 
    
    <hr>
    
    Getter Method
    
    Signature ``End`` 
    
    :returns:  end paramter  
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``End`` 
    
    :param end:  end parameter  
    :type end: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowComb: bool = ...
    """
    Returns or sets  the flag to show comb 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowComb`` 
    
    :returns:  true to show comb  
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowComb`` 
    
    :param on:  true to show comb  
    :type on: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowInflection: bool = ...
    """
    Returns or sets  the flag to show inflection 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowInflection`` 
    
    :returns:  true to show inflection  
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowInflection`` 
    
    :param on:  true to show inflection  
    :type on: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowKnot: bool = ...
    """
    Returns or sets  the flag to show knot 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowKnot`` 
    
    :returns:  true to show knot  
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowKnot`` 
    
    :param on:  true to show knot  
    :type on: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowPeak: bool = ...
    """
    Returns or sets  the flag to show peak 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowPeak`` 
    
    :returns:  true to show peak  
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowPeak`` 
    
    :param on:  true to show peak  
    :type on: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ShowPole: bool = ...
    """
    Returns or sets  the flag to show pole 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowPole`` 
    
    :returns:  true to show pole  
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowPole`` 
    
    :param on:  true to show pole  
    :type on: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Start: float = ...
    """
    Returns or sets  the start parameter, range from 0 to 100 
    
    <hr>
    
    Getter Method
    
    Signature ``Start`` 
    
    :returns:  start paramter  
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Start`` 
    
    :param start:  start parameter  
    :type start: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    UseMaxLength: bool = ...
    """
    Returns or sets  the flag to limit the maximum length of the comb 
    
    <hr>
    
    Getter Method
    
    Signature ``UseMaxLength`` 
    
    :returns:  true to use the max length to limit comb  
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseMaxLength`` 
    
    :param on:  true to use the max length to limit comb  
    :type on: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """


class SurfaceContinuityAnalysis(AnalysisObject):
    """
    Represents a SurfaceContinuityAnalysis builder   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: SurfaceContinuityAnalysis = ...  # unknown typename


class HighlightLinesAnalysisBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HighlightLinesAnalysisBuilderTypes():
    """
    three types of light methods   
    
    .. deprecated::  NX8.0.0
       Use :py:meth:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlacements` instead.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Uniform", "Uniform: Lights are placed uniformly on light plane"
       "ThroughPoints", "Through Points: A highlight line is guaranteed to pass through a surface point."
       "BetweenPoints", "Between Points: Two highlight lines are guaranteed to pass through two given surface points. More highlight lines are created between these two highlight lines when light number is more than two."
    """
    Uniform = 0  # HighlightLinesAnalysisBuilderTypesMemberType
    ThroughPoints = 1  # HighlightLinesAnalysisBuilderTypesMemberType
    BetweenPoints = 2  # HighlightLinesAnalysisBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HighlightLinesAnalysisBuilderTypes2MemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HighlightLinesAnalysisBuilderTypes2():
    """
    four types of display methods 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Reflection", "Create reflection lines"
       "Projection", "Create projection lines"
       "Isoclines", "Create isoclines"
       "Zebra", "Create zebra contour lines"
    """
    Reflection = 0  # HighlightLinesAnalysisBuilderTypes2MemberType
    Projection = 1  # HighlightLinesAnalysisBuilderTypes2MemberType
    Isoclines = 2  # HighlightLinesAnalysisBuilderTypes2MemberType
    Zebra = 3  # HighlightLinesAnalysisBuilderTypes2MemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HighlightLinesAnalysisBuilderResolutionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HighlightLinesAnalysisBuilderResolutions():
    """
    resolution options 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Coarse", "Coarse"
       "Standard", "Standard"
       "Fine", "Fine"
       "ExtraFine", "Extra Fine"
       "SuperFine", "Super Fine"
       "UltraFine", "Ultra Fine"
    """
    Coarse = 0  # HighlightLinesAnalysisBuilderResolutionsMemberType
    Standard = 1  # HighlightLinesAnalysisBuilderResolutionsMemberType
    Fine = 2  # HighlightLinesAnalysisBuilderResolutionsMemberType
    ExtraFine = 3  # HighlightLinesAnalysisBuilderResolutionsMemberType
    SuperFine = 4  # HighlightLinesAnalysisBuilderResolutionsMemberType
    UltraFine = 5  # HighlightLinesAnalysisBuilderResolutionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HighlightLinesAnalysisBuilderDisplayMethodsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HighlightLinesAnalysisBuilderDisplayMethods():
    """
    display methods   
    
    .. deprecated::  NX8.0.0
       Use :py:meth:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types2` instead.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Reflection", "Create reflection lines"
       "Projection", "Create projection lines"
    """
    Reflection = 0  # HighlightLinesAnalysisBuilderDisplayMethodsMemberType
    Projection = 1  # HighlightLinesAnalysisBuilderDisplayMethodsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HighlightLinesAnalysisBuilderLightPlacementsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HighlightLinesAnalysisBuilderLightPlacements():
    """
    light placement 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Uniform", "Uniform: Lights are placed uniformly on light plane"
       "ThroughPoints", "Through Points: A highlight line is guaranteed to pass through a surface point."
       "BetweenPoints", "Between Points: Two highlight lines are guaranteed to pass through two given surface points. More highlight lines are created between these two highlight lines when light number is more than two."
    """
    Uniform = 0  # HighlightLinesAnalysisBuilderLightPlacementsMemberType
    ThroughPoints = 1  # HighlightLinesAnalysisBuilderLightPlacementsMemberType
    BetweenPoints = 2  # HighlightLinesAnalysisBuilderLightPlacementsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HighlightLinesAnalysisBuilderLightPlaneOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HighlightLinesAnalysisBuilderLightPlaneOptions():
    """
    light plane options
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "YZ", "Uses YC-ZC plane as light plane"
       "ZX", "Uses XC-ZC plane as light plane"
       "XY", "Uses XC-YC plane as light plane"
       "Arbitrary", "Uses an arbitrary plane as light plane"
    """
    YZ = 0  # HighlightLinesAnalysisBuilderLightPlaneOptionsMemberType
    ZX = 1  # HighlightLinesAnalysisBuilderLightPlaneOptionsMemberType
    XY = 2  # HighlightLinesAnalysisBuilderLightPlaneOptionsMemberType
    Arbitrary = 3  # HighlightLinesAnalysisBuilderLightPlaneOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HighlightLinesAnalysisBuilder(NXOpen.Builder):
    """
    Represents a
    :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysis`
    builder.  
    
    Highlight Lines Analysis function can produce both reflection lines and projection
    lines which are used to evaluate the surface quality and continuity between adjacent surfaces.
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateHighlightLinesAnalysisBuilder`
    
    Default values.
    
    ====================  ===========================================
    Property              Value
    ====================  ===========================================
    EndIsoAngle.Value     90 
    --------------------  -------------------------------------------
    LightNumber           10 
    --------------------  -------------------------------------------
    LightSpacing          50.0 (millimeters part), 2.0 (inches part) 
    --------------------  -------------------------------------------
    Resolution            Fine 
    --------------------  -------------------------------------------
    StartIsoAngle.Value   -90 
    ====================  ===========================================
    
    .. versionadded:: NX6.0.0
    """
    
    class Types():
        """
        three types of light methods   
        
        .. deprecated::  NX8.0.0
           Use :py:meth:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlacements` instead.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Uniform", "Uniform: Lights are placed uniformly on light plane"
           "ThroughPoints", "Through Points: A highlight line is guaranteed to pass through a surface point."
           "BetweenPoints", "Between Points: Two highlight lines are guaranteed to pass through two given surface points. More highlight lines are created between these two highlight lines when light number is more than two."
        """
        Uniform = 0  # HighlightLinesAnalysisBuilderTypesMemberType
        ThroughPoints = 1  # HighlightLinesAnalysisBuilderTypesMemberType
        BetweenPoints = 2  # HighlightLinesAnalysisBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Types2():
        """
        four types of display methods 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Reflection", "Create reflection lines"
           "Projection", "Create projection lines"
           "Isoclines", "Create isoclines"
           "Zebra", "Create zebra contour lines"
        """
        Reflection = 0  # HighlightLinesAnalysisBuilderTypes2MemberType
        Projection = 1  # HighlightLinesAnalysisBuilderTypes2MemberType
        Isoclines = 2  # HighlightLinesAnalysisBuilderTypes2MemberType
        Zebra = 3  # HighlightLinesAnalysisBuilderTypes2MemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Resolutions():
        """
        resolution options 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Coarse", "Coarse"
           "Standard", "Standard"
           "Fine", "Fine"
           "ExtraFine", "Extra Fine"
           "SuperFine", "Super Fine"
           "UltraFine", "Ultra Fine"
        """
        Coarse = 0  # HighlightLinesAnalysisBuilderResolutionsMemberType
        Standard = 1  # HighlightLinesAnalysisBuilderResolutionsMemberType
        Fine = 2  # HighlightLinesAnalysisBuilderResolutionsMemberType
        ExtraFine = 3  # HighlightLinesAnalysisBuilderResolutionsMemberType
        SuperFine = 4  # HighlightLinesAnalysisBuilderResolutionsMemberType
        UltraFine = 5  # HighlightLinesAnalysisBuilderResolutionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DisplayMethods():
        """
        display methods   
        
        .. deprecated::  NX8.0.0
           Use :py:meth:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types2` instead.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Reflection", "Create reflection lines"
           "Projection", "Create projection lines"
        """
        Reflection = 0  # HighlightLinesAnalysisBuilderDisplayMethodsMemberType
        Projection = 1  # HighlightLinesAnalysisBuilderDisplayMethodsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LightPlacements():
        """
        light placement 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Uniform", "Uniform: Lights are placed uniformly on light plane"
           "ThroughPoints", "Through Points: A highlight line is guaranteed to pass through a surface point."
           "BetweenPoints", "Between Points: Two highlight lines are guaranteed to pass through two given surface points. More highlight lines are created between these two highlight lines when light number is more than two."
        """
        Uniform = 0  # HighlightLinesAnalysisBuilderLightPlacementsMemberType
        ThroughPoints = 1  # HighlightLinesAnalysisBuilderLightPlacementsMemberType
        BetweenPoints = 2  # HighlightLinesAnalysisBuilderLightPlacementsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LightPlaneOptions():
        """
        light plane options
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "YZ", "Uses YC-ZC plane as light plane"
           "ZX", "Uses XC-ZC plane as light plane"
           "XY", "Uses XC-YC plane as light plane"
           "Arbitrary", "Uses an arbitrary plane as light plane"
        """
        YZ = 0  # HighlightLinesAnalysisBuilderLightPlaneOptionsMemberType
        ZX = 1  # HighlightLinesAnalysisBuilderLightPlaneOptionsMemberType
        XY = 2  # HighlightLinesAnalysisBuilderLightPlaneOptionsMemberType
        Arbitrary = 3  # HighlightLinesAnalysisBuilderLightPlaneOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetDarkColor(self) -> 'list[float]':
        """
        Gets the color of the dark (unlit) areas of reflection contours  
        
        Signature ``GetDarkColor()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDarkColor(self, darkColor: 'list[float]') -> None:
        """
        Sets the color of the dark (unlit) areas of reflection contours 
        
        Signature ``SetDarkColor(darkColor)`` 
        
        :param darkColor:  Array of 3 RGB values, each between 0 and 1  
        :type darkColor: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def GetBrightColor(self) -> 'list[float]':
        """
        Gets the color of the bright (lit) areas of reflection contours  
        
        Signature ``GetBrightColor()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBrightColor(self, brightColor: 'list[float]') -> None:
        """
        Sets the color of the bright (lit) areas of reflection contours 
        
        Signature ``SetBrightColor(brightColor)`` 
        
        :param brightColor:  Array of 3 RGB values, each between 0 and 1  
        :type brightColor: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def ReinitializePlane(self) -> None:
        """
        Reinitialize light plane based on the selected faces.  
        
        If
        more faces are selected, you may need to change
        light plane, so the light plane could be better centered. 
        
        Signature ``ReinitializePlane()`` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX8.0.0
           This call currently does not do anything.  Calls to this method can be safely removed.
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def SetLightPlaneOrigin(self, origin: NXOpen.Point3d) -> None:
        """
        Sets the origin of the light plane.  
        
        Signature ``SetLightPlaneOrigin(origin)`` 
        
        :param origin:  coordinates of origin  
        :type origin: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def SetLightPlaneXAxis(self, xAxis: NXOpen.Vector3d) -> None:
        """
        Sets the x-axis of the light plane.  
        
        Signature ``SetLightPlaneXAxis(xAxis)`` 
        
        :param xAxis:  x-axis vector  
        :type xAxis: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def SetLightPlaneYAxis(self, yAxis: NXOpen.Vector3d) -> None:
        """
        Sets the y-axis of the light plane.  
        
        Signature ``SetLightPlaneYAxis(yAxis)`` 
        
        :param yAxis:  y-axis vector  
        :type yAxis: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    BetweenPoints: NXOpen.SelectPointList = ...
    """
    Returns  the between points 
    
    <hr>
    
    Getter Method
    
    Signature ``BetweenPoints`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectPointList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    DisplayMethod: HighlightLinesAnalysisBuilderDisplayMethods = ...
    """
    Returns or sets  the display method 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderDisplayMethods` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX8.0.0
       Use :py:meth:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Type2`` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayMethod`` 
    
    :param displayMethod: 
    :type displayMethod: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderDisplayMethods` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX8.0.0
       Use :py:meth:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Type2`` instead.
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    EndIsoAngle: NXOpen.Expression = ...
    """
    Returns  the end angle for isoclines (uniform) 
    
    <hr>
    
    Getter Method
    
    Signature ``EndIsoAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Faces: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the face list 
    
    <hr>
    
    Getter Method
    
    Signature ``Faces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    IsReflectionLocked: bool = ...
    """
    Returns or sets  the lock reflection.  
    
    When the lock is on, the reflection lines will be freezed
    while the view is changing. Otherwise, the reflection lines
    will be updated continuously while view is changing. 
    
    <hr>
    
    Getter Method
    
    Signature ``IsReflectionLocked`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsReflectionLocked`` 
    
    :param isReflectionLocked: 
    :type isReflectionLocked: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    IsoclineVector: NXOpen.Direction = ...
    """
    Returns or sets  the vector to define isoclines 
    
    <hr>
    
    Getter Method
    
    Signature ``IsoclineVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsoclineVector`` 
    
    :param isoclineVector: 
    :type isoclineVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    LightDiffuseness: float = ...
    """
    Returns or sets  the ratio of blended texels to all light texels.  
    
    It is used by reflection contours 
    
    <hr>
    
    Getter Method
    
    Signature ``LightDiffuseness`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LightDiffuseness`` 
    
    :param lightDiffuseness: 
    :type lightDiffuseness: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    LightNumber: int = ...
    """
    Returns or sets  the number of lights.  
    
    It's used by Uniform type and Between Points type. 
    
    <hr>
    
    Getter Method
    
    Signature ``LightNumber`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LightNumber`` 
    
    :param lightNumber: 
    :type lightNumber: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    LightPlacement: HighlightLinesAnalysisBuilderLightPlacements = ...
    """
    Returns or sets  the light placement 
    
    <hr>
    
    Getter Method
    
    Signature ``LightPlacement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderLightPlacements` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LightPlacement`` 
    
    :param placement: 
    :type placement: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderLightPlacements` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    LightPlaneOrigin: NXOpen.Point3d = ...
    """
    Returns  the origin of the light plane 
    
    <hr>
    
    Getter Method
    
    Signature ``LightPlaneOrigin`` 
    
    :returns:  coordinates of origin  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    LightPlaneXAxis: NXOpen.Vector3d = ...
    """
    Returns  the x-axis of the light plane 
    
    <hr>
    
    Getter Method
    
    Signature ``LightPlaneXAxis`` 
    
    :returns:  x-axis vector  
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    LightPlaneYAxis: NXOpen.Vector3d = ...
    """
    Returns  the y-axis of the light plane 
    
    <hr>
    
    Getter Method
    
    Signature ``LightPlaneYAxis`` 
    
    :returns:  y-axis vector  
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    LightSpacing: float = ...
    """
    Returns or sets  the light spacing between two adjacent lights.  
    
    It's used by Uniform type 
    
    <hr>
    
    Getter Method
    
    Signature ``LightSpacing`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LightSpacing`` 
    
    :param lightSpacing: 
    :type lightSpacing: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    LightWidth: float = ...
    """
    Returns or sets  the ratio of light size to light spacing.  
    
    It is used by reflection contours 
    
    <hr>
    
    Getter Method
    
    Signature ``LightWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LightWidth`` 
    
    :param lightWidth: 
    :type lightWidth: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Resolution: HighlightLinesAnalysisBuilderResolutions = ...
    """
    Returns or sets  the resolution.  
    
    <hr>
    
    Getter Method
    
    Signature ``Resolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderResolutions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Resolution`` 
    
    :param resolution: 
    :type resolution: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderResolutions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    StartIsoAngle: NXOpen.Expression = ...
    """
    Returns  the start angle for isoclines (uniform) 
    
    <hr>
    
    Getter Method
    
    Signature ``StartIsoAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ThroughPoints: NXOpen.SelectPointList = ...
    """
    Returns  the through points 
    
    <hr>
    
    Getter Method
    
    Signature ``ThroughPoints`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectPointList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Type: HighlightLinesAnalysisBuilderTypes = ...
    """
    Returns or sets  the type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderTypes` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX8.0.0
       Use :py:meth:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlacement`` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderTypes` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX8.0.0
       Use :py:meth:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlacement`` instead.
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Type2: HighlightLinesAnalysisBuilderTypes2 = ...
    """
    Returns or sets  the display type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderTypes2` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type2`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderTypes2` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_analyze ("STUDIO ANALYZE")
    """
    Null: HighlightLinesAnalysisBuilder = ...  # unknown typename


class CurveAnalysisDisplayShowFlagTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveAnalysisDisplayShowFlagType():
    """
    Show flag types   
    
    .. deprecated::  NX8.5.0
       Use :py:meth:`NXOpen.GeometricAnalysis.CurveAnalysisDisplay.SetShowPole`, :py:meth:`NXOpen.GeometricAnalysis.CurveAnalysisDisplay.SetShowKnot`, :py:meth:`NXOpen.GeometricAnalysis.CurveAnalysisDisplay.SetShowEndPoints` methods.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Pole", "show pole"
       "Comb", "show comb"
       "Inflection", "show inflection"
       "Peak", "show peak"
       "Knot", "show knot"
       "Endpoint", "show endpoint"
    """
    Pole = 0  # CurveAnalysisDisplayShowFlagTypeMemberType
    Comb = 1  # CurveAnalysisDisplayShowFlagTypeMemberType
    Inflection = 2  # CurveAnalysisDisplayShowFlagTypeMemberType
    Peak = 3  # CurveAnalysisDisplayShowFlagTypeMemberType
    Knot = 4  # CurveAnalysisDisplayShowFlagTypeMemberType
    Endpoint = 5  # CurveAnalysisDisplayShowFlagTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveAnalysisDisplay():
    """
    Represents a tool to control whether to show a curve's poles,knots,combs,peaks and inflections   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.GeometricAnalysis.AnalysisObjectCollection`
    
    .. versionadded:: NX6.0.0
    """
    
    class ShowFlagType():
        """
        Show flag types   
        
        .. deprecated::  NX8.5.0
           Use :py:meth:`NXOpen.GeometricAnalysis.CurveAnalysisDisplay.SetShowPole`, :py:meth:`NXOpen.GeometricAnalysis.CurveAnalysisDisplay.SetShowKnot`, :py:meth:`NXOpen.GeometricAnalysis.CurveAnalysisDisplay.SetShowEndPoints` methods.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Pole", "show pole"
           "Comb", "show comb"
           "Inflection", "show inflection"
           "Peak", "show peak"
           "Knot", "show knot"
           "Endpoint", "show endpoint"
        """
        Pole = 0  # CurveAnalysisDisplayShowFlagTypeMemberType
        Comb = 1  # CurveAnalysisDisplayShowFlagTypeMemberType
        Inflection = 2  # CurveAnalysisDisplayShowFlagTypeMemberType
        Peak = 3  # CurveAnalysisDisplayShowFlagTypeMemberType
        Knot = 4  # CurveAnalysisDisplayShowFlagTypeMemberType
        Endpoint = 5  # CurveAnalysisDisplayShowFlagTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetAnalysisRecord(self, curve: NXOpen.Curve, record: CurveAnalysisRecord) -> None:
        """
        Sets analysis record 
        
        Signature ``SetAnalysisRecord(curve, record)`` 
        
        :param curve:  curve  
        :type curve: :py:class:`NXOpen.Curve` 
        :param record:  curve analysis record  
        :type record: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisRecord` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX8.5.0
           Use :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysis`.
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetAnalysisRecord(self, curve: NXOpen.Curve) -> CurveAnalysisRecord:
        """
        Gets analysis record  
        
        Signature ``GetAnalysisRecord(curve)`` 
        
        :param curve:  curve  
        :type curve: :py:class:`NXOpen.Curve` 
        :returns:  curve analysis record  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisRecord` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX8.5.0
           Use :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysis`.
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def NewRecord(self) -> CurveAnalysisRecord:
        """
        Creats a curve analysis record  
        
        Signature ``NewRecord()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisRecord` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX8.5.0
           Use :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysis`.
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def SetShowFlag(self, curve: NXOpen.Curve, choice: CurveAnalysisDisplayShowFlagType, on: bool) -> None:
        """
        Sets show flags 
        
        Signature ``SetShowFlag(curve, choice, on)`` 
        
        :param curve:  curve  
        :type curve: :py:class:`NXOpen.Curve` 
        :param choice:  pole/comb/inflection/peak/knot  
        :type choice: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisDisplayShowFlagType` 
        :param on:  true/false to show flags  
        :type on: bool 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX8.5.0
           Use :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysis`.
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def SetShowPole(self, curve: NXOpen.Curve, show: bool) -> None:
        """
        Sets a flag representing poles display state of a b-spline curve 
        
        Signature ``SetShowPole(curve, show)`` 
        
        :param curve:  curve  
        :type curve: :py:class:`NXOpen.Curve` 
        :param show: 
        :type show: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetShowPole(self, curve: NXOpen.Curve) -> bool:
        """
        Gets a flag representing poles display state of a b-spline curve 
        
        Signature ``GetShowPole(curve)`` 
        
        :param curve:  curve  
        :type curve: :py:class:`NXOpen.Curve` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def SetShowKnot(self, curve: NXOpen.Curve, show: bool) -> None:
        """
        Sets a flag representing knots display state of a b-spline curve
        
        Signature ``SetShowKnot(curve, show)`` 
        
        :param curve:  curve  
        :type curve: :py:class:`NXOpen.Curve` 
        :param show: 
        :type show: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetShowKnot(self, curve: NXOpen.Curve) -> bool:
        """
        Gets a flag representing knots display state of a b-spline curve 
        
        Signature ``GetShowKnot(curve)`` 
        
        :param curve:  curve  
        :type curve: :py:class:`NXOpen.Curve` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def SetShowEndPoints(self, curve: NXOpen.Curve, show: bool) -> None:
        """
        Sets a flag representing end points display state of a curve
        
        Signature ``SetShowEndPoints(curve, show)`` 
        
        :param curve:  curve  
        :type curve: :py:class:`NXOpen.Curve` 
        :param show: 
        :type show: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetShowEndPoints(self, curve: NXOpen.Curve) -> bool:
        """
        Gets a flag representing end points display state of a curve 
        
        Signature ``GetShowEndPoints(curve)`` 
        
        :param curve:  curve  
        :type curve: :py:class:`NXOpen.Curve` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    


class DeviationGaugeBuilderMeasurementMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DeviationGaugeBuilderMeasurementMethodType():
    """
    This enum represents the Deviation Gauge  Analysis Object evaluation types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ThreeDim", "3D"
       "XyzDirection", "XYZ direction"
       "WorkView", "Work view"
       "VectorComponent", "Vector component"
       "Plane", "Plane"
       "AlongVector", "Along vector"
    """
    ThreeDim = 0  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
    XyzDirection = 1  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
    WorkView = 2  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
    VectorComponent = 3  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
    Plane = 4  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
    AlongVector = 5  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DeviationGaugeBuilderXyzDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DeviationGaugeBuilderXyzDirectionType():
    """
    This enum represents the Deviation Gauge Analysis Object X, Y, Z direction options 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", "X direction"
       "Y", "Y direction"
       "Z", "Z direction"
    """
    X = 0  # DeviationGaugeBuilderXyzDirectionTypeMemberType
    Y = 1  # DeviationGaugeBuilderXyzDirectionTypeMemberType
    Z = 2  # DeviationGaugeBuilderXyzDirectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DeviationGaugeBuilderAdditionalValuesLabelTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DeviationGaugeBuilderAdditionalValuesLabelType():
    """
    This enum represents the Deviation Gauge  Analysis Object additional values label type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UserDefined", "User Defined"
       "Intermediate", "Intermediate"
       "All", "All"
       "NotSet", "None"
    """
    UserDefined = 0  # DeviationGaugeBuilderAdditionalValuesLabelTypeMemberType
    Intermediate = 1  # DeviationGaugeBuilderAdditionalValuesLabelTypeMemberType
    All = 2  # DeviationGaugeBuilderAdditionalValuesLabelTypeMemberType
    NotSet = 3  # DeviationGaugeBuilderAdditionalValuesLabelTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DeviationGaugeBuilderMinMaxTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DeviationGaugeBuilderMinMaxType():
    """
    This enum represents the Deviation Gauge  Analysis Object min max type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Minmax", "Minimum/Maximum"
       "Minimum", "Minimum"
       "Maximum", "Maximum"
       "NotSet", "None"
    """
    Minmax = 0  # DeviationGaugeBuilderMinMaxTypeMemberType
    Minimum = 1  # DeviationGaugeBuilderMinMaxTypeMemberType
    Maximum = 2  # DeviationGaugeBuilderMinMaxTypeMemberType
    NotSet = 3  # DeviationGaugeBuilderMinMaxTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DeviationGaugeBuilderColorPlotTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DeviationGaugeBuilderColorPlotTypes():
    """
    This enum represents the Deviation Gauge  Analysis Object color plot types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Blend", "Blend"
       "Stepped", "Stepped"
       "NotSet", "None"
    """
    Blend = 0  # DeviationGaugeBuilderColorPlotTypesMemberType
    Stepped = 1  # DeviationGaugeBuilderColorPlotTypesMemberType
    NotSet = 2  # DeviationGaugeBuilderColorPlotTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DeviationGaugeBuilderReportingPerTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DeviationGaugeBuilderReportingPerTypes():
    """
    This enum represents the Deviation Gauge  Analysis Object reporting per setting 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AnalysisObject", "Per Analysis Object"
       "Target", "Per Target Object"
       "Reference", "Per Reference Object"
    """
    AnalysisObject = 0  # DeviationGaugeBuilderReportingPerTypesMemberType
    Target = 1  # DeviationGaugeBuilderReportingPerTypesMemberType
    Reference = 2  # DeviationGaugeBuilderReportingPerTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DeviationGaugeBuilder(NXOpen.Builder):
    """
    DeviationGaugeBuilder class    
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateDeviationGaugeBuilder`
    
    Default values.
    
    ===================================  ========================================
    Property                             Value
    ===================================  ========================================
    ColorPlotType                        Blend 
    -----------------------------------  ----------------------------------------
    CurveRangeControl.AnchorPosition     Start 
    -----------------------------------  ----------------------------------------
    DeviationIntervals                   5 
    -----------------------------------  ----------------------------------------
    HasAbsoluteColorPlot                 0 
    -----------------------------------  ----------------------------------------
    HasAdditionalValuesLabel             None 
    -----------------------------------  ----------------------------------------
    HasMaximumValueLabel                 1 
    -----------------------------------  ----------------------------------------
    HasMinimumValueLabel                 0 
    -----------------------------------  ----------------------------------------
    InnerTolerance                       0.1 
    -----------------------------------  ----------------------------------------
    IsLabelDisplayed                     0 
    -----------------------------------  ----------------------------------------
    IsMarkerDisplayed                    0 
    -----------------------------------  ----------------------------------------
    IsNeedlePlotDisplayed                1 
    -----------------------------------  ----------------------------------------
    MaxCheckingAngle                     5 
    -----------------------------------  ----------------------------------------
    MaxCheckingDistance                  1 (millimeters part), 0.5 (inches part) 
    -----------------------------------  ----------------------------------------
    MeasurementMethod                    ThreeDim 
    -----------------------------------  ----------------------------------------
    MeasurementSamples                   20 
    -----------------------------------  ----------------------------------------
    MinMaxOption                         Minmax 
    -----------------------------------  ----------------------------------------
    NeedleScale                          1.0 
    -----------------------------------  ----------------------------------------
    NegativeInnerTolerance               -0.001 
    -----------------------------------  ----------------------------------------
    NegativeOuterTolerance               -0.001 
    -----------------------------------  ----------------------------------------
    OuterTolerance                       0.1 
    -----------------------------------  ----------------------------------------
    PositiveInnerTolerance               0.001 
    -----------------------------------  ----------------------------------------
    PositiveOuterTolerance               0.001 
    -----------------------------------  ----------------------------------------
    ReportingPerType                     AnalysisObject 
    -----------------------------------  ----------------------------------------
    SpatialResolution                    0.1 
    -----------------------------------  ----------------------------------------
    SurfaceRangeControl.AnchorPosition   Vertex1 
    -----------------------------------  ----------------------------------------
    XyzDirection                         X 
    ===================================  ========================================
    
    .. versionadded:: NX6.0.0
    """
    
    class MeasurementMethodType():
        """
        This enum represents the Deviation Gauge  Analysis Object evaluation types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ThreeDim", "3D"
           "XyzDirection", "XYZ direction"
           "WorkView", "Work view"
           "VectorComponent", "Vector component"
           "Plane", "Plane"
           "AlongVector", "Along vector"
        """
        ThreeDim = 0  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
        XyzDirection = 1  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
        WorkView = 2  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
        VectorComponent = 3  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
        Plane = 4  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
        AlongVector = 5  # DeviationGaugeBuilderMeasurementMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class XyzDirectionType():
        """
        This enum represents the Deviation Gauge Analysis Object X, Y, Z direction options 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "X", "X direction"
           "Y", "Y direction"
           "Z", "Z direction"
        """
        X = 0  # DeviationGaugeBuilderXyzDirectionTypeMemberType
        Y = 1  # DeviationGaugeBuilderXyzDirectionTypeMemberType
        Z = 2  # DeviationGaugeBuilderXyzDirectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class AdditionalValuesLabelType():
        """
        This enum represents the Deviation Gauge  Analysis Object additional values label type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "UserDefined", "User Defined"
           "Intermediate", "Intermediate"
           "All", "All"
           "NotSet", "None"
        """
        UserDefined = 0  # DeviationGaugeBuilderAdditionalValuesLabelTypeMemberType
        Intermediate = 1  # DeviationGaugeBuilderAdditionalValuesLabelTypeMemberType
        All = 2  # DeviationGaugeBuilderAdditionalValuesLabelTypeMemberType
        NotSet = 3  # DeviationGaugeBuilderAdditionalValuesLabelTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class MinMaxType():
        """
        This enum represents the Deviation Gauge  Analysis Object min max type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Minmax", "Minimum/Maximum"
           "Minimum", "Minimum"
           "Maximum", "Maximum"
           "NotSet", "None"
        """
        Minmax = 0  # DeviationGaugeBuilderMinMaxTypeMemberType
        Minimum = 1  # DeviationGaugeBuilderMinMaxTypeMemberType
        Maximum = 2  # DeviationGaugeBuilderMinMaxTypeMemberType
        NotSet = 3  # DeviationGaugeBuilderMinMaxTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ColorPlotTypes():
        """
        This enum represents the Deviation Gauge  Analysis Object color plot types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Blend", "Blend"
           "Stepped", "Stepped"
           "NotSet", "None"
        """
        Blend = 0  # DeviationGaugeBuilderColorPlotTypesMemberType
        Stepped = 1  # DeviationGaugeBuilderColorPlotTypesMemberType
        NotSet = 2  # DeviationGaugeBuilderColorPlotTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ReportingPerTypes():
        """
        This enum represents the Deviation Gauge  Analysis Object reporting per setting 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AnalysisObject", "Per Analysis Object"
           "Target", "Per Target Object"
           "Reference", "Per Reference Object"
        """
        AnalysisObject = 0  # DeviationGaugeBuilderReportingPerTypesMemberType
        Target = 1  # DeviationGaugeBuilderReportingPerTypesMemberType
        Reference = 2  # DeviationGaugeBuilderReportingPerTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def AddDynamicPoints(self) -> None:
        """
        Adds dynamic points to the Deviation Gauge.  
        
        Signature ``AddDynamicPoints()`` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def AddPMILabel(self, snappedObject: NXOpen.NXObject) -> None:
        """
        Add a PMI label in specified position to represent the deviation value.  
        
        Signature ``AddPMILabel(snappedObject)`` 
        
        :param snappedObject:  The face or curve which the PMI label pointed to.  
        :type snappedObject: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    ColorPlotType: DeviationGaugeBuilderColorPlotTypes = ...
    """
    Returns or sets  the color plot type 
    
    <hr>
    
    Getter Method
    
    Signature ``ColorPlotType`` 
    
    :returns:     
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderColorPlotTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``ColorPlotType`` 
    
    :param colorPlotType:     
    :type colorPlotType: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderColorPlotTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    ConstraintManager: NXOpen.Features.GeometricConstraintDataManager = ...
    """
    Returns  the constraint manager 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintManager`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.GeometricConstraintDataManager` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    CurveRangeControl: NXOpen.GeometricUtilities.CurveRangeBuilder = ...
    """
    Returns  the curve range   
    
    <hr>
    
    Getter Method
    
    Signature ``CurveRangeControl`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.CurveRangeBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    DeviationIntervals: int = ...
    """
    Returns or sets  the number of deviation intervals 
    
    <hr>
    
    Getter Method
    
    Signature ``DeviationIntervals`` 
    
    :returns:     
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``DeviationIntervals`` 
    
    :param deviationIntervals:     
    :type deviationIntervals: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    HasAbsoluteColorPlot: bool = ...
    """
    Returns or sets  a value indicating whether to plot using absolute value   
    
    <hr>
    
    Getter Method
    
    Signature ``HasAbsoluteColorPlot`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``HasAbsoluteColorPlot`` 
    
    :param absoluteColorPlot:     
    :type absoluteColorPlot: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    HasAdditionalValuesLabel: DeviationGaugeBuilderAdditionalValuesLabelType = ...
    """
    Returns or sets  a value indicating whether to add additional values label 
    
    <hr>
    
    Getter Method
    
    Signature ``HasAdditionalValuesLabel`` 
    
    :returns:     
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderAdditionalValuesLabelType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``HasAdditionalValuesLabel`` 
    
    :param additionalValuesLabel:     
    :type additionalValuesLabel: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderAdditionalValuesLabelType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    HasCrossCurveDeviationLabel: bool = ...
    """
    Returns or sets  a value indicating whether to display cross_curve deviation label 
    
    <hr>
    
    Getter Method
    
    Signature ``HasCrossCurveDeviationLabel`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``HasCrossCurveDeviationLabel`` 
    
    :param crossCurveDeviationLabel:     
    :type crossCurveDeviationLabel: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    HasInfoLabel: bool = ...
    """
    Returns or sets  a value indicating whether to enable floating info label 
    
    <hr>
    
    Getter Method
    
    Signature ``HasInfoLabel`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``HasInfoLabel`` 
    
    :param infoLabel:     
    :type infoLabel: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    HasInnerToleranceLabel: bool = ...
    """
    Returns or sets  a value indicating whether to display inner tolerance label 
    
    <hr>
    
    Getter Method
    
    Signature ``HasInnerToleranceLabel`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``HasInnerToleranceLabel`` 
    
    :param innerToleranceLabel:     
    :type innerToleranceLabel: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    HasMaximumValueLabel: bool = ...
    """
    Returns or sets  a value indicating whether to display maximum value label 
    
    <hr>
    
    Getter Method
    
    Signature ``HasMaximumValueLabel`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``HasMaximumValueLabel`` 
    
    :param maximumValueLabel:     
    :type maximumValueLabel: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    HasMinimumValueLabel: bool = ...
    """
    Returns or sets  a value indicating whether to display minimum value label 
    
    <hr>
    
    Getter Method
    
    Signature ``HasMinimumValueLabel`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``HasMinimumValueLabel`` 
    
    :param minimumValueLabel:     
    :type minimumValueLabel: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    InnerTolerance: float = ...
    """
    Returns or sets  the inner tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``InnerTolerance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``InnerTolerance`` 
    
    :param innerTolerance:     
    :type innerTolerance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsColorMapDisplayed: bool = ...
    """
    Returns or sets  a value indicating whether to display color map  
    
    <hr>
    
    Getter Method
    
    Signature ``IsColorMapDisplayed`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``IsColorMapDisplayed`` 
    
    :param isColorMapDisplayed:     
    :type isColorMapDisplayed: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsDirectionReversed: bool = ...
    """
    Returns or sets  a value indicating whether to reverse the direction 
    
    <hr>
    
    Getter Method
    
    Signature ``IsDirectionReversed`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``IsDirectionReversed`` 
    
    :param reverseDirection:     
    :type reverseDirection: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsLabelDisplayed: bool = ...
    """
    Returns or sets   a value indicating whether to display label   
    
    <hr>
    
    Getter Method
    
    Signature ``IsLabelDisplayed`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``IsLabelDisplayed`` 
    
    :param labelDisplayed:     
    :type labelDisplayed: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsMarkerDisplayed: bool = ...
    """
    Returns or sets  a value indicating whether to display marker  
    
    <hr>
    
    Getter Method
    
    Signature ``IsMarkerDisplayed`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``IsMarkerDisplayed`` 
    
    :param isMarkerDisplayed:     
    :type isMarkerDisplayed: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsNeedlePlotDisplayed: bool = ...
    """
    Returns or sets  a value indicating whether to display needle plot  
    
    <hr>
    
    Getter Method
    
    Signature ``IsNeedlePlotDisplayed`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``IsNeedlePlotDisplayed`` 
    
    :param isNeedlePlotDisplayed:     
    :type isNeedlePlotDisplayed: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MaxCheckingAngle: float = ...
    """
    Returns or sets  the maximum checking angle 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxCheckingAngle`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``MaxCheckingAngle`` 
    
    :param maxCheckingAngle:     
    :type maxCheckingAngle: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MaxCheckingDistance: float = ...
    """
    Returns or sets  the maximum checking distance 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxCheckingDistance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``MaxCheckingDistance`` 
    
    :param maxCheckingDistance:     
    :type maxCheckingDistance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MeasurementMethod: DeviationGaugeBuilderMeasurementMethodType = ...
    """
    Returns or sets  the measurement method 
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementMethod`` 
    
    :returns:     
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderMeasurementMethodType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementMethod`` 
    
    :param measurementMethod:     
    :type measurementMethod: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderMeasurementMethodType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MeasurementSamples: int = ...
    """
    Returns or sets  the number of measurement samples 
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementSamples`` 
    
    :returns:     
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementSamples`` 
    
    :param measurementSamples:     
    :type measurementSamples: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MinMaxOption: DeviationGaugeBuilderMinMaxType = ...
    """
    Returns or sets  the min_max type 
    
    <hr>
    
    Getter Method
    
    Signature ``MinMaxOption`` 
    
    :returns:     
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderMinMaxType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``MinMaxOption`` 
    
    :param minMax:     
    :type minMax: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderMinMaxType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    NeedleScale: float = ...
    """
    Returns or sets  the needle scale 
    
    <hr>
    
    Getter Method
    
    Signature ``NeedleScale`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``NeedleScale`` 
    
    :param needleScale:     
    :type needleScale: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    NegativeInnerTolerance: float = ...
    """
    Returns or sets  the negative inner tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``NegativeInnerTolerance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``NegativeInnerTolerance`` 
    
    :param negativennerTolerance:     
    :type negativennerTolerance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    NegativeOuterTolerance: float = ...
    """
    Returns or sets  the negative outer tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``NegativeOuterTolerance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``NegativeOuterTolerance`` 
    
    :param negativeOuterTolerance:     
    :type negativeOuterTolerance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    OuterTolerance: float = ...
    """
    Returns or sets  the outer tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``OuterTolerance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``OuterTolerance`` 
    
    :param outerTolerance:     
    :type outerTolerance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the plane for measurement direction 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    PositiveInnerTolerance: float = ...
    """
    Returns or sets  the positive inner tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``PositiveInnerTolerance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``PositiveInnerTolerance`` 
    
    :param positiveInnerTolerance:     
    :type positiveInnerTolerance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    PositiveOuterTolerance: float = ...
    """
    Returns or sets  the positive outer tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``PositiveOuterTolerance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``PositiveOuterTolerance`` 
    
    :param positiveOuterTolerance:     
    :type positiveOuterTolerance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    ReferenceObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the reference object 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    ReportingPerType: DeviationGaugeBuilderReportingPerTypes = ...
    """
    Returns or sets  the reporting per option 
    
    <hr>
    
    Getter Method
    
    Signature ``ReportingPerType`` 
    
    :returns:     
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderReportingPerTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``ReportingPerType`` 
    
    :param reportingPerType:     
    :type reportingPerType: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderReportingPerTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    SpatialResolution: float = ...
    """
    Returns or sets  the maximum checking angle 
    
    <hr>
    
    Getter Method
    
    Signature ``SpatialResolution`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``SpatialResolution`` 
    
    :param spatialResolution:     
    :type spatialResolution: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    SuggestScaleFactor: bool = ...
    """
    Returns or sets  a value indicating whether to use automatic scale factor 
    
    <hr>
    
    Getter Method
    
    Signature ``SuggestScaleFactor`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``SuggestScaleFactor`` 
    
    :param suggestScaleFactor:     
    :type suggestScaleFactor: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    SurfaceRangeControl: NXOpen.GeometricUtilities.SurfaceRangeBuilder = ...
    """
    Returns  the surface range   
    
    <hr>
    
    Getter Method
    
    Signature ``SurfaceRangeControl`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.SurfaceRangeBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    TargetObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the target object 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    UseDefiningPoints: bool = ...
    """
    Returns or sets   a value indicating whether to use defining points.  
    
    Available only if target is curve with defining points   
    
    <hr>
    
    Getter Method
    
    Signature ``UseDefiningPoints`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``UseDefiningPoints`` 
    
    :param useDefiningPoints:     
    :type useDefiningPoints: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    VectorComponentDirection: NXOpen.Direction = ...
    """
    Returns or sets  the direction vector.  
    
    Not used if the measurement method is ThreeDim or Plane 
    
    <hr>
    
    Getter Method
    
    Signature ``VectorComponentDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``VectorComponentDirection`` 
    
    :param vectorComponentDirection: 
    :type vectorComponentDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    XyzDirection: DeviationGaugeBuilderXyzDirectionType = ...
    """
    Returns or sets  the xyz direction 
    
    <hr>
    
    Getter Method
    
    Signature ``XyzDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderXyzDirectionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``XyzDirection`` 
    
    :param xyzDirection: 
    :type xyzDirection: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilderXyzDirectionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: DeviationGaugeBuilder = ...  # unknown typename


class CurveCurvatureAnalysisBuilderProjectionTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveCurvatureAnalysisBuilderProjectionTypes():
    """
    Projection plane types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "no projection"
       "CurvePlane", "best fit plane"
       "Vector", "specify vector"
       "View", "view plane"
       "Xyz", "specify x,y,z plane"
    """
    NotSet = 0  # CurveCurvatureAnalysisBuilderProjectionTypesMemberType
    CurvePlane = 1  # CurveCurvatureAnalysisBuilderProjectionTypesMemberType
    Vector = 2  # CurveCurvatureAnalysisBuilderProjectionTypesMemberType
    View = 3  # CurveCurvatureAnalysisBuilderProjectionTypesMemberType
    Xyz = 4  # CurveCurvatureAnalysisBuilderProjectionTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveCurvatureAnalysisBuilderXyzTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveCurvatureAnalysisBuilderXyzTypes():
    """
    Enumeration for X, Y or Z projection plane 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", "x-axis plane"
       "Y", "y-axis plane"
       "Z", "z-axis plane"
    """
    X = 0  # CurveCurvatureAnalysisBuilderXyzTypesMemberType
    Y = 1  # CurveCurvatureAnalysisBuilderXyzTypesMemberType
    Z = 2  # CurveCurvatureAnalysisBuilderXyzTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveCurvatureAnalysisBuilderLabelValuesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveCurvatureAnalysisBuilderLabelValues():
    """
    Enumeration for label computation method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Curvature", "label showing curvature value"
       "RadiusofCurvature", "label showing radius of curvature value"
    """
    Curvature = 0  # CurveCurvatureAnalysisBuilderLabelValuesMemberType
    RadiusofCurvature = 1  # CurveCurvatureAnalysisBuilderLabelValuesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveCurvatureAnalysisBuilderNeedleDirectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveCurvatureAnalysisBuilderNeedleDirection():
    """
    Enumeration for needle direction type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", "needle pointing inside"
       "Outside", "needle pointing outside"
    """
    Inside = 0  # CurveCurvatureAnalysisBuilderNeedleDirectionMemberType
    Outside = 1  # CurveCurvatureAnalysisBuilderNeedleDirectionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveCurvatureAnalysisBuilderCalculationMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveCurvatureAnalysisBuilderCalculationMethod():
    """
    Enumeration for needle calculation method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Curvature", "needle of curvature value"
       "RadiusofCurvature", "needle of radius of curvature value"
    """
    Curvature = 0  # CurveCurvatureAnalysisBuilderCalculationMethodMemberType
    RadiusofCurvature = 1  # CurveCurvatureAnalysisBuilderCalculationMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveCurvatureAnalysisBuilderDisplayStyleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveCurvatureAnalysisBuilderDisplayStyle():
    """
    Enumeration for needle display type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "linear needle"
       "Logarithmic", "logarithmic needle"
    """
    Linear = 0  # CurveCurvatureAnalysisBuilderDisplayStyleMemberType
    Logarithmic = 1  # CurveCurvatureAnalysisBuilderDisplayStyleMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveCurvatureAnalysisBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysis` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateCurveCurvatureAnalysisBuilder`
    
    Default values.
    
    =========================  ==========
    Property                   Value
    =========================  ==========
    CombRange.AnchorPosition   Start 
    -------------------------  ----------
    DynamicProjection          1 
    -------------------------  ----------
    Method                     Curvature 
    -------------------------  ----------
    Projection                 None 
    -------------------------  ----------
    ReverseDirection           0 
    -------------------------  ----------
    ShowInflections            0 
    -------------------------  ----------
    ShowPeaks                  0 
    -------------------------  ----------
    Style                      Linear 
    -------------------------  ----------
    Xyz                        X 
    =========================  ==========
    
    .. versionadded:: NX7.0.0
    """
    
    class ProjectionTypes():
        """
        Projection plane types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "no projection"
           "CurvePlane", "best fit plane"
           "Vector", "specify vector"
           "View", "view plane"
           "Xyz", "specify x,y,z plane"
        """
        NotSet = 0  # CurveCurvatureAnalysisBuilderProjectionTypesMemberType
        CurvePlane = 1  # CurveCurvatureAnalysisBuilderProjectionTypesMemberType
        Vector = 2  # CurveCurvatureAnalysisBuilderProjectionTypesMemberType
        View = 3  # CurveCurvatureAnalysisBuilderProjectionTypesMemberType
        Xyz = 4  # CurveCurvatureAnalysisBuilderProjectionTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class XyzTypes():
        """
        Enumeration for X, Y or Z projection plane 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "X", "x-axis plane"
           "Y", "y-axis plane"
           "Z", "z-axis plane"
        """
        X = 0  # CurveCurvatureAnalysisBuilderXyzTypesMemberType
        Y = 1  # CurveCurvatureAnalysisBuilderXyzTypesMemberType
        Z = 2  # CurveCurvatureAnalysisBuilderXyzTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LabelValues():
        """
        Enumeration for label computation method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Curvature", "label showing curvature value"
           "RadiusofCurvature", "label showing radius of curvature value"
        """
        Curvature = 0  # CurveCurvatureAnalysisBuilderLabelValuesMemberType
        RadiusofCurvature = 1  # CurveCurvatureAnalysisBuilderLabelValuesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class NeedleDirection():
        """
        Enumeration for needle direction type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", "needle pointing inside"
           "Outside", "needle pointing outside"
        """
        Inside = 0  # CurveCurvatureAnalysisBuilderNeedleDirectionMemberType
        Outside = 1  # CurveCurvatureAnalysisBuilderNeedleDirectionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CalculationMethod():
        """
        Enumeration for needle calculation method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Curvature", "needle of curvature value"
           "RadiusofCurvature", "needle of radius of curvature value"
        """
        Curvature = 0  # CurveCurvatureAnalysisBuilderCalculationMethodMemberType
        RadiusofCurvature = 1  # CurveCurvatureAnalysisBuilderCalculationMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DisplayStyle():
        """
        Enumeration for needle display type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "linear needle"
           "Logarithmic", "logarithmic needle"
        """
        Linear = 0  # CurveCurvatureAnalysisBuilderDisplayStyleMemberType
        Logarithmic = 1  # CurveCurvatureAnalysisBuilderDisplayStyleMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def UpdateWorkView(self) -> None:
        """
        Update work view with a given view matrix 
        
        Signature ``UpdateWorkView()`` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDumbPeakPoints(self) -> 'list[NXOpen.Point]':
        """
        Create peak points  
        
        Signature ``CreateDumbPeakPoints()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Point` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDumbInflectionPoints(self) -> 'list[NXOpen.Point]':
        """
        Create inflection points  
        
        Signature ``CreateDumbInflectionPoints()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Point` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCurveRange(self, index: int) -> NXOpen.GeometricUtilities.CurveRangeBuilder:
        """
        Returns the :py:class:`NXOpen.GeometricUtilities.CurveRangeBuilder` object at a given index from the list  
        
        Signature ``GetCurveRange(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.GeometricUtilities.CurveRangeBuilder` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetCurveRangeListLength(self) -> int:
        """
        Get the number of :py:class:`NXOpen.GeometricUtilities.CurveRangeBuilder` objects in the list 
        
        Signature ``GetCurveRangeListLength()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX8.0.1
        
        License requirements: None.
        """
        ...
    
    CombOptions: NXOpen.GeometricUtilities.CombOptionsBuilder = ...
    """
    Returns  the comb display block options 
    
    <hr>
    
    Getter Method
    
    Signature ``CombOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.CombOptionsBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    CombRange: NXOpen.GeometricUtilities.CurveRangeBuilder = ...
    """
    Returns  the comb range 
    
    <hr>
    
    Getter Method
    
    Signature ``CombRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.CurveRangeBuilder` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    DynamicProjection: bool = ...
    """
    Returns or sets  the dynamic projection 
    
    <hr>
    
    Getter Method
    
    Signature ``DynamicProjection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DynamicProjection`` 
    
    :param dynamicProjection: 
    :type dynamicProjection: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Method: CurveCurvatureAnalysisBuilderCalculationMethod = ...
    """
    Returns or sets  the method 
    
    <hr>
    
    Getter Method
    
    Signature ``Method`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderCalculationMethod` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Method`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderCalculationMethod` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Projection: CurveCurvatureAnalysisBuilderProjectionTypes = ...
    """
    Returns or sets  the projection 
    
    <hr>
    
    Getter Method
    
    Signature ``Projection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderProjectionTypes` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Projection`` 
    
    :param projection: 
    :type projection: :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderProjectionTypes` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    ReverseDirection: int = ...
    """
    Returns or sets  the reverse direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseDirection`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseDirection`` 
    
    :param reverseDirection: 
    :type reverseDirection: int 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    SelectedCurves: NXOpen.ScCollector = ...
    """
    Returns  the selected curves and/or edges 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedCurves`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    ShowCombs: bool = ...
    """
    Returns or sets  the show combs 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowCombs`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowCombs`` 
    
    :param showCombs: 
    :type showCombs: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    ShowInflections: bool = ...
    """
    Returns or sets  the show inflections 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowInflections`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowInflections`` 
    
    :param showInflections: 
    :type showInflections: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    ShowMaxLabels: bool = ...
    """
    Returns or sets  the show max labels 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowMaxLabels`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowMaxLabels`` 
    
    :param showMaxLabels: 
    :type showMaxLabels: bool 
    
    .. versionadded:: NX7.0.1
    
    License requirements: None.
    """
    ShowMinLabels: bool = ...
    """
    Returns or sets  the show min labels 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowMinLabels`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowMinLabels`` 
    
    :param showMinLabels: 
    :type showMinLabels: bool 
    
    .. versionadded:: NX7.0.1
    
    License requirements: None.
    """
    ShowPeaks: bool = ...
    """
    Returns or sets  the show peaks 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowPeaks`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowPeaks`` 
    
    :param showPeaks: 
    :type showPeaks: bool 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Style: CurveCurvatureAnalysisBuilderDisplayStyle = ...
    """
    Returns or sets  the style 
    
    <hr>
    
    Getter Method
    
    Signature ``Style`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderDisplayStyle` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Style`` 
    
    :param style: 
    :type style: :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderDisplayStyle` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the vector 
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vector: 
    :type vector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Xyz: CurveCurvatureAnalysisBuilderXyzTypes = ...
    """
    Returns or sets  the xyz 
    
    <hr>
    
    Getter Method
    
    Signature ``Xyz`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderXyzTypes` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Xyz`` 
    
    :param xyz: 
    :type xyz: :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderXyzTypes` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Null: CurveCurvatureAnalysisBuilder = ...  # unknown typename


class LocalRadiusAnalysisBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.GeometricAnalysis.LocalRadiusAnalysis` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateLocalRadiusAnalysisBuilder`
    
    Default values.
    
    ==============================  =====
    Property                        Value
    ==============================  =====
    VisibilityCoordinates           0 
    ------------------------------  -----
    VisibilityMaxRadius             0 
    ------------------------------  -----
    VisibilityMinMaxRadiusTangent   0 
    ------------------------------  -----
    VisibilityMinRadius             1 
    ------------------------------  -----
    VisibilityRadius                1 
    ------------------------------  -----
    VisibilityURadius               0 
    ------------------------------  -----
    VisibilityUV                    0 
    ------------------------------  -----
    VisibilityUVTangent             0 
    ------------------------------  -----
    VisibilityVRadius               0 
    ==============================  =====
    
    .. versionadded:: NX8.5.0
    """
    
    def ButtonOpenInformationWindow(self) -> None:
        """
        TODO: fill in a description for this 
        
        Signature ``ButtonOpenInformationWindow()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    SelectionPoint: NXOpen.Features.GeometricConstraintDataManager = ...
    """
    Returns  the selection point 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.GeometricConstraintDataManager` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    VisibilityCoordinates: bool = ...
    """
    Returns or sets  the toggle coordinates 
    
    <hr>
    
    Getter Method
    
    Signature ``VisibilityCoordinates`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibilityCoordinates`` 
    
    :param visibilityCoordinates: 
    :type visibilityCoordinates: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    VisibilityMaxRadius: bool = ...
    """
    Returns or sets  the toggle max radius show 
    
    <hr>
    
    Getter Method
    
    Signature ``VisibilityMaxRadius`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibilityMaxRadius`` 
    
    :param visibilityMaxRadius: 
    :type visibilityMaxRadius: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    VisibilityMinMaxRadiusTangent: bool = ...
    """
    Returns or sets  the toggle min radius tangent 
    
    <hr>
    
    Getter Method
    
    Signature ``VisibilityMinMaxRadiusTangent`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibilityMinMaxRadiusTangent`` 
    
    :param visibilityMinMaxRadiusTangent: 
    :type visibilityMinMaxRadiusTangent: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    VisibilityMinRadius: bool = ...
    """
    Returns or sets  the toggle min radius show 
    
    <hr>
    
    Getter Method
    
    Signature ``VisibilityMinRadius`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibilityMinRadius`` 
    
    :param visibilityMinRadius: 
    :type visibilityMinRadius: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    VisibilityRadius: bool = ...
    """
    Returns or sets  the toggle radius show 
    
    <hr>
    
    Getter Method
    
    Signature ``VisibilityRadius`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibilityRadius`` 
    
    :param visibilityRadius: 
    :type visibilityRadius: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    VisibilityURadius: bool = ...
    """
    Returns or sets  the toggle uradius show 
    
    <hr>
    
    Getter Method
    
    Signature ``VisibilityURadius`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibilityURadius`` 
    
    :param visibilityURadius: 
    :type visibilityURadius: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    VisibilityUV: bool = ...
    """
    Returns or sets  the toggle uv 
    
    <hr>
    
    Getter Method
    
    Signature ``VisibilityUV`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibilityUV`` 
    
    :param visibilityUV: 
    :type visibilityUV: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    VisibilityUVTangent: bool = ...
    """
    Returns or sets  the toggle max radius tangent 
    
    <hr>
    
    Getter Method
    
    Signature ``VisibilityUVTangent`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibilityUVTangent`` 
    
    :param visibilityUVTangent: 
    :type visibilityUVTangent: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    VisibilityVRadius: bool = ...
    """
    Returns or sets  the toggle vradius show 
    
    <hr>
    
    Getter Method
    
    Signature ``VisibilityVRadius`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibilityVRadius`` 
    
    :param visibilityVRadius: 
    :type visibilityVRadius: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: LocalRadiusAnalysisBuilder = ...  # unknown typename


class LocalRadiusAnalysis(AnalysisObject):
    """
    Builder for Local Radius Analysis (formerly Dynamic Radius)   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.LocalRadiusAnalysisBuilder`
    
    .. versionadded:: NX8.5.0
    """
    Null: LocalRadiusAnalysis = ...  # unknown typename


class AnalysisObjectCollectionEx():
    """
    Collection of analysis objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.GeometricAnalysis.AnalysisObjectCollection`
    
    .. versionadded:: NX11.0.0
    """
    
    def CreateRadiusAnalysisBuilder(self, radiusAO: NXOpen.DisplayableObject) -> RadiusAnalysisBuilder:
        """
        Creates a radius analysis builder.  
        
        Signature ``CreateRadiusAnalysisBuilder(radiusAO)`` 
        
        :param radiusAO:  RadiusAO  
        :type radiusAO: :py:class:`NXOpen.DisplayableObject` 
        :returns:  radius analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.RadiusAnalysisBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def CreateSlopeAnalysisBuilder(self, slopeAO: NXOpen.DisplayableObject) -> SlopeAnalysisBuilder:
        """
        Creates a slope analysis builder.  
        
        Signature ``CreateSlopeAnalysisBuilder(slopeAO)`` 
        
        :param slopeAO:  SlopeAO  
        :type slopeAO: :py:class:`NXOpen.DisplayableObject` 
        :returns:  slope analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.SlopeAnalysisBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def CreateDistanceAnalysisBuilder(self, distanceAO: NXOpen.DisplayableObject) -> DistanceAnalysisBuilder:
        """
        Creates a distance analysis builder.  
        
        Signature ``CreateDistanceAnalysisBuilder(distanceAO)`` 
        
        :param distanceAO:  DistanceAO  
        :type distanceAO: :py:class:`NXOpen.DisplayableObject` 
        :returns:  distance analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.DistanceAnalysisBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def CreateReflectionAnalysisBuilder(self, reflectionAO: NXOpen.DisplayableObject) -> ReflectionAnalysisBuilder:
        """
        Creates a reflection analysis builder.  
        
        Signature ``CreateReflectionAnalysisBuilder(reflectionAO)`` 
        
        :param reflectionAO:  ReflectionAO  
        :type reflectionAO: :py:class:`NXOpen.DisplayableObject` 
        :returns:  reflection analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    


class CurveAnalysisPeaksBuilderDirectionOptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CurveAnalysisPeaksBuilderDirectionOptionType():
    """
    Direction option types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "no direction"
       "PlaneOfCurve", "best fit plane"
       "SpecifyVector", "specify vector"
       "WorkView", "work view"
    """
    NotSet = 0  # CurveAnalysisPeaksBuilderDirectionOptionTypeMemberType
    PlaneOfCurve = 1  # CurveAnalysisPeaksBuilderDirectionOptionTypeMemberType
    SpecifyVector = 2  # CurveAnalysisPeaksBuilderDirectionOptionTypeMemberType
    WorkView = 3  # CurveAnalysisPeaksBuilderDirectionOptionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CurveAnalysisPeaksBuilder(NXOpen.Builder):
    """
    This class handles the options setting for the curve analysis information (Peaks) display.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateCurveAnalysisPeaksBuilder`
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX8.5.0
       Use :py:class:`GeometricAnalysis.CurveCurvatureAnalysis`.
    """
    
    class DirectionOptionType():
        """
        Direction option types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "no direction"
           "PlaneOfCurve", "best fit plane"
           "SpecifyVector", "specify vector"
           "WorkView", "work view"
        """
        NotSet = 0  # CurveAnalysisPeaksBuilderDirectionOptionTypeMemberType
        PlaneOfCurve = 1  # CurveAnalysisPeaksBuilderDirectionOptionTypeMemberType
        SpecifyVector = 2  # CurveAnalysisPeaksBuilderDirectionOptionTypeMemberType
        WorkView = 3  # CurveAnalysisPeaksBuilderDirectionOptionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreatePoints(self) -> 'list[NXOpen.Point]':
        """
        Create points at the peaks of the curve 
        
        Signature ``CreatePoints()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Point` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    DirectionOption: CurveAnalysisPeaksBuilderDirectionOptionType = ...
    """
    Returns or sets  the direction option 
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisPeaksBuilderDirectionOptionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionOption`` 
    
    :param option: 
    :type option: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisPeaksBuilderDirectionOptionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SelectedCurves: NXOpen.ScCollector = ...
    """
    Returns  the selected curves 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedCurves`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the vector 
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vect: 
    :type vect: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Null: CurveAnalysisPeaksBuilder = ...  # unknown typename


class FaceAnalysisNormalsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents reverse normal functions used by Face Analysis.  
    
    .. versionadded:: NX11.0.0
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
    
    FaceToReverseNormal: NXOpen.SelectNXObject = ...
    """
    Returns  the face to reverse normal 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceToReverseNormal`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Point: NXOpen.Point = ...
    """
    Returns or sets  the point to redirect normals
    
    <hr>
    
    Getter Method
    
    Signature ``Point`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Point`` 
    
    :param point: 
    :type point: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: FaceAnalysisNormalsBuilder = ...  # unknown typename


class CurveContinuity(AnalysisObject):
    """
    Represents a Curve Continuity Analysis builder   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.CurveContinuityBuilder`
    
    .. versionadded:: NX7.0.0
    """
    Null: CurveContinuity = ...  # unknown typename


class AnalysisObjectCollection(NXOpen.TaggedObjectCollection):
    """
    Create a AnalysisObjectCollection   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.GeometricAnalysis.AnalysisManager`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateGapFlushnessBuilder(self, gfaoObject: GapFlushness) -> GapFlushnessBuilder:
        """
        Creates a gap and flushness builder  
        
        Signature ``CreateGapFlushnessBuilder(gfaoObject)`` 
        
        :param gfaoObject:  Gap and Flushness   
        :type gfaoObject: :py:class:`NXOpen.GeometricAnalysis.GapFlushness` 
        :returns:  Gap and Flushness builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def CreateSurfaceContinuityAnalysisBuilder(self, scaoObject: NXOpen.DisplayableObject) -> SurfaceContinuityAnalysisBuilder:
        """
        Creates a surface continuity analysis builder  
        
        Signature ``CreateSurfaceContinuityAnalysisBuilder(scaoObject)`` 
        
        :param scaoObject:  Surface Continuity Analysis  
        :type scaoObject: :py:class:`NXOpen.DisplayableObject` 
        :returns:  Surface Continuity Analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def CreateCurveCurvatureAnalysisBuilder(self, caaoObject: NXOpen.DisplayableObject) -> CurveCurvatureAnalysisBuilder:
        """
        Creates a curve curvature analysis builder  
        
        Signature ``CreateCurveCurvatureAnalysisBuilder(caaoObject)`` 
        
        :param caaoObject: Curve Curvature Analysis  
        :type caaoObject: :py:class:`NXOpen.DisplayableObject` 
        :returns:  Curve Curvature Analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def CreateCurveAnalysisCombsBuilder(self) -> CurveAnalysisCombsBuilder:
        """
        Creates a curve analysis combs builder  
        
        Signature ``CreateCurveAnalysisCombsBuilder()`` 
        
        :returns:  Curve analysis Combs Builder 
        :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisCombsBuilder` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX8.5.0
           Use :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysis`.
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def CreateCurveAnalysisInflectionsBuilder(self) -> CurveAnalysisInflectionsBuilder:
        """
        Creates a curve analysis inflections builder  
        
        Signature ``CreateCurveAnalysisInflectionsBuilder()`` 
        
        :returns:  Curve analysis Inflections Builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisInflectionsBuilder` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX8.5.0
           Use :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysis`.
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def CreateCurveAnalysisPeaksBuilder(self) -> CurveAnalysisPeaksBuilder:
        """
        Creates a curve analysis peaks builder  
        
        Signature ``CreateCurveAnalysisPeaksBuilder()`` 
        
        :returns:  Curve analysis Peaks Builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisPeaksBuilder` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX8.5.0
           Use :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysis`.
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def CreateHighlightLinesAnalysisBuilder(self, hpaoObject: NXOpen.DisplayableObject) -> HighlightLinesAnalysisBuilder:
        """
        Creates a Highlight Lines Analysis builder  
        
        Signature ``CreateHighlightLinesAnalysisBuilder(hpaoObject)`` 
        
        :param hpaoObject:  Highlight Lines Analysis object  
        :type hpaoObject: :py:class:`NXOpen.DisplayableObject` 
        :returns:  Highlight Lines Analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def CreateSectionAnalysisBuilder(self, msaoObject: SectionAnalysisObject) -> NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder:
        """
        Creates a Section Analysis object builder  
        
        Signature ``CreateSectionAnalysisBuilder(msaoObject)`` 
        
        :param msaoObject:  Section Analysis object  
        :type msaoObject: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysisObject` 
        :returns:  Section Analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def CreateSectionAnalysisExBuilder(self, csaoObject: NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExObject) -> NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder:
        """
        Creates a Section Analysis builder of a new version 
        
        Signature ``CreateSectionAnalysisExBuilder(csaoObject)`` 
        
        :param csaoObject:  Section Analysis object  
        :type csaoObject: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExObject` 
        :returns:  Section Analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def CreateDeviationGaugeBuilder(self, ddaoObject: NXOpen.DisplayableObject) -> DeviationGaugeBuilder:
        """
        Creates a  Deviation Gauge Builder  
        
        Signature ``CreateDeviationGaugeBuilder(ddaoObject)`` 
        
        :param ddaoObject:  DDAO   
        :type ddaoObject: :py:class:`NXOpen.DisplayableObject` 
        :returns:  DeviationGauge builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def CreateCurveContinuityBuilder(self, ccaoObject: NXOpen.DisplayableObject) -> CurveContinuityBuilder:
        """
        Creates a Curve Continuity Builder  
        
        Signature ``CreateCurveContinuityBuilder(ccaoObject)`` 
        
        :param ccaoObject:  CCAO  
        :type ccaoObject: :py:class:`NXOpen.DisplayableObject` 
        :returns:  Curve Continuity AO builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveContinuityBuilder` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def CreateSurfaceIntersectionBuilder(self, siaoObject: NXOpen.DisplayableObject) -> SurfaceIntersectionBuilder:
        """
        Creates a surface intersection  builder  
        
        Signature ``CreateSurfaceIntersectionBuilder(siaoObject)`` 
        
        :param siaoObject: surface intersection  
        :type siaoObject: :py:class:`NXOpen.DisplayableObject` 
        :returns:  surface intersection builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def CreateDraftAnalysisBuilder(self, daoObject: NXOpen.DisplayableObject) -> DraftAnalysisBuilder:
        """
        Creates a draft analysis builder  
        
        Signature ``CreateDraftAnalysisBuilder(daoObject)`` 
        
        :param daoObject:  DAO  
        :type daoObject: :py:class:`NXOpen.DisplayableObject` 
        :returns:  draft analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.DraftAnalysisBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    
    def CreateLocalRadiusAnalysisBuilder(self, lrao: LocalRadiusAnalysis) -> LocalRadiusAnalysisBuilder:
        """
        Creates a :py:class:`NXOpen.GeometricAnalysis.LocalRadiusAnalysisBuilder`  
        
        Signature ``CreateLocalRadiusAnalysisBuilder(lrao)`` 
        
        :param lrao: 
        :type lrao: :py:class:`NXOpen.GeometricAnalysis.LocalRadiusAnalysis` 
        :returns: 
        :rtype: :py:class:`NXOpen.GeometricAnalysis.LocalRadiusAnalysisBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateFaceCurvatureAnalysisBuilder(self, fcaoObject: NXOpen.DisplayableObject) -> FaceCurvatureAnalysisBuilder:
        """
        Creates a face curvature analysis builder  
        
        Signature ``CreateFaceCurvatureAnalysisBuilder(fcaoObject)`` 
        
        :param fcaoObject:  FCAO  
        :type fcaoObject: :py:class:`NXOpen.DisplayableObject` 
        :returns:  face curvature analysis builder  
        :rtype: :py:class:`NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_analyze ("STUDIO ANALYZE")
        """
        ...
    
    CurveAnalysisDisplayObject: CurveAnalysisDisplay = ...
    """
    Returns object for displaying curve analysis information 
    
    Signature ``CurveAnalysisDisplayObject`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.CurveAnalysisDisplay`
    """
    SurfaceAnalysisDisplayObject: SurfaceAnalysisDisplay = ...
    """
    Returns object for displaying surface analysis information 
    
    Signature ``SurfaceAnalysisDisplayObject`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.SurfaceAnalysisDisplay`
    """
    AnalysisObjectsEx: AnalysisObjectCollectionEx = ...
    """
    Returns the AnalysisObjectCollectionEx instance belonging to this part 
    
    Signature ``AnalysisObjectsEx`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.AnalysisObjectCollectionEx`
    """


class DupinBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    The Dupin Indicatrix is a tool to geometrically display the surface curvature at a specified point on a surface.  
    
    .. versionadded:: NX8.0.0
    """
    
    def ResetAnalysisPoint(self) -> None:
        """
        Reset the analysis point to accept dynamic input.  
        
        Signature ``ResetAnalysisPoint()`` 
        
        .. versionadded:: NX8.0.0
        
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
    
    AnalysisPoint: NXOpen.Point = ...
    """
    Returns or sets  the point location defining where the analysis should be done.  
    
    <hr>
    
    Getter Method
    
    Signature ``AnalysisPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnalysisPoint`` 
    
    :param analysisPoint: 
    :type analysisPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Angle: float = ...
    """
    Returns or sets  the deviation in degrees from the minimum curvature.  
    
    This value is used to rotate the normal curvature about the specified point. 
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Angle`` 
    
    :param angle: 
    :type angle: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    FlatnessTolerance: float = ...
    """
    Returns or sets  the tolerance that defines at the specified point if an area is flat.  
    
    <hr>
    
    Getter Method
    
    Signature ``FlatnessTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FlatnessTolerance`` 
    
    :param flatnessTolerance: 
    :type flatnessTolerance: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Scale: float = ...
    """
    Returns or sets  the scale factor to apply to the display of the dupin indicatrix.  
    
    <hr>
    
    Getter Method
    
    Signature ``Scale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Scale`` 
    
    :param scale: 
    :type scale: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: DupinBuilder = ...  # unknown typename


class DeviationGauge(AnalysisObject):
    """
    Deviation Gauge analysis object class   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.DeviationGaugeBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: DeviationGauge = ...  # unknown typename


class CurveCurvatureAnalysis(AnalysisObject):
    """
    Represents a CurveCurvatureAnalysis builder   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder`
    
    .. versionadded:: NX7.0.0
    """
    Null: CurveCurvatureAnalysis = ...  # unknown typename


class GapFlushnessBuilderEvaluationTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GapFlushnessBuilderEvaluationTypes():
    """
    This enum represents the Gap and Flushness Analysis Object evaluation types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Absolute", "absolute"
       "Visual", "visual"
    """
    Absolute = 0  # GapFlushnessBuilderEvaluationTypesMemberType
    Visual = 1  # GapFlushnessBuilderEvaluationTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GapFlushnessBuilderEvaluationModesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GapFlushnessBuilderEvaluationModes():
    """
    This enum represents evaluation mode  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Point", "at point"
       "CurveNumber", "along curve and number"
       "Curve", "along curve and distance"
    """
    Point = 0  # GapFlushnessBuilderEvaluationModesMemberType
    CurveNumber = 1  # GapFlushnessBuilderEvaluationModesMemberType
    Curve = 2  # GapFlushnessBuilderEvaluationModesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GapFlushnessBuilderSectionAlignmentsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GapFlushnessBuilderSectionAlignments():
    """
    This enum represents cross-section alignment type  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Curve", "curve"
       "CurveView", "curve in view"
       "SpecifiedDirection", "specified direction"
    """
    Curve = 0  # GapFlushnessBuilderSectionAlignmentsMemberType
    CurveView = 1  # GapFlushnessBuilderSectionAlignmentsMemberType
    SpecifiedDirection = 2  # GapFlushnessBuilderSectionAlignmentsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GapFlushnessBuilderDisplayOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GapFlushnessBuilderDisplayOptions():
    """
    This enum represents Label Display Option type  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "GapOnly", "gap only"
       "FlushnessOnly", "flushness only"
       "Both", "both"
    """
    GapOnly = 0  # GapFlushnessBuilderDisplayOptionsMemberType
    FlushnessOnly = 1  # GapFlushnessBuilderDisplayOptionsMemberType
    Both = 2  # GapFlushnessBuilderDisplayOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GapFlushnessBuilderSectionCurveOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GapFlushnessBuilderSectionCurveOptions():
    """
    This enum represents Cross Section Curves Options  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ContactCurve", "use contact curve"
       "UserDefined", "use user defined curve"
    """
    ContactCurve = 0  # GapFlushnessBuilderSectionCurveOptionsMemberType
    UserDefined = 1  # GapFlushnessBuilderSectionCurveOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GapFlushnessBuilderPanelTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GapFlushnessBuilderPanelTypes():
    """
    This enum represents panel type  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Hem", "type hem"
       "Flange", "type flange"
       "Wall", "type wall"
    """
    Hem = 0  # GapFlushnessBuilderPanelTypesMemberType
    Flange = 1  # GapFlushnessBuilderPanelTypesMemberType
    Wall = 2  # GapFlushnessBuilderPanelTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GapFlushnessBuilder(NXOpen.Builder):
    """
    GapFlushnessBuilder class    
    
    To create a new instance of this class, use :py:meth:`NXOpen.GeometricAnalysis.AnalysisObjectCollection.CreateGapFlushnessBuilder`
    
    Default values.
    
    =============  =====
    Property       Value
    =============  =====
    SampleNumber   10 
    =============  =====
    
    .. versionadded:: NX5.0.0
    """
    
    class EvaluationTypes():
        """
        This enum represents the Gap and Flushness Analysis Object evaluation types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Absolute", "absolute"
           "Visual", "visual"
        """
        Absolute = 0  # GapFlushnessBuilderEvaluationTypesMemberType
        Visual = 1  # GapFlushnessBuilderEvaluationTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class EvaluationModes():
        """
        This enum represents evaluation mode  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Point", "at point"
           "CurveNumber", "along curve and number"
           "Curve", "along curve and distance"
        """
        Point = 0  # GapFlushnessBuilderEvaluationModesMemberType
        CurveNumber = 1  # GapFlushnessBuilderEvaluationModesMemberType
        Curve = 2  # GapFlushnessBuilderEvaluationModesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SectionAlignments():
        """
        This enum represents cross-section alignment type  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Curve", "curve"
           "CurveView", "curve in view"
           "SpecifiedDirection", "specified direction"
        """
        Curve = 0  # GapFlushnessBuilderSectionAlignmentsMemberType
        CurveView = 1  # GapFlushnessBuilderSectionAlignmentsMemberType
        SpecifiedDirection = 2  # GapFlushnessBuilderSectionAlignmentsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DisplayOptions():
        """
        This enum represents Label Display Option type  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "GapOnly", "gap only"
           "FlushnessOnly", "flushness only"
           "Both", "both"
        """
        GapOnly = 0  # GapFlushnessBuilderDisplayOptionsMemberType
        FlushnessOnly = 1  # GapFlushnessBuilderDisplayOptionsMemberType
        Both = 2  # GapFlushnessBuilderDisplayOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SectionCurveOptions():
        """
        This enum represents Cross Section Curves Options  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ContactCurve", "use contact curve"
           "UserDefined", "use user defined curve"
        """
        ContactCurve = 0  # GapFlushnessBuilderSectionCurveOptionsMemberType
        UserDefined = 1  # GapFlushnessBuilderSectionCurveOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class PanelTypes():
        """
        This enum represents panel type  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Hem", "type hem"
           "Flange", "type flange"
           "Wall", "type wall"
        """
        Hem = 0  # GapFlushnessBuilderPanelTypesMemberType
        Flange = 1  # GapFlushnessBuilderPanelTypesMemberType
        Wall = 2  # GapFlushnessBuilderPanelTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    BasePanelFaces: NXOpen.ScCollector = ...
    """
    Returns  the Base Panel face selection    
    
    <hr>
    
    Getter Method
    
    Signature ``BasePanelFaces`` 
    
    :returns:   Face  collector  
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    BasePanelInnerContactCurves: NXOpen.Section = ...
    """
    Returns  the Base Panel inner contact section 
    
    <hr>
    
    Getter Method
    
    Signature ``BasePanelInnerContactCurves`` 
    
    :returns:   curve/edge collector  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    BasePanelOuterContactCurves: NXOpen.Section = ...
    """
    Returns  the Base Panel outer contact section  
    
    <hr>
    
    Getter Method
    
    Signature ``BasePanelOuterContactCurves`` 
    
    :returns:   curve/edge collector  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    BasePanelType: GapFlushnessBuilderPanelTypes = ...
    """
    Returns or sets  the Base Panel type   
    
    <hr>
    
    Getter Method
    
    Signature ``BasePanelType`` 
    
    :returns:     
    :rtype: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderPanelTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``BasePanelType`` 
    
    :param panelType:     
    :type panelType: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderPanelTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    CrossSectionCurveOption: GapFlushnessBuilderSectionCurveOptions = ...
    """
    Returns or sets  the cross section curve option     
    
    <hr>
    
    Getter Method
    
    Signature ``CrossSectionCurveOption`` 
    
    :returns:       
    :rtype: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderSectionCurveOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``CrossSectionCurveOption`` 
    
    :param sectionCurveOption:       
    :type sectionCurveOption: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderSectionCurveOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    CrossSectionCurves: NXOpen.Section = ...
    """
    Returns  the Cross Section Curves 
    
    <hr>
    
    Getter Method
    
    Signature ``CrossSectionCurves`` 
    
    :returns:   curve/edge collector  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    EvaluationMode: GapFlushnessBuilderEvaluationModes = ...
    """
    Returns or sets  the evaluation Method    
    
    <hr>
    
    Getter Method
    
    Signature ``EvaluationMode`` 
    
    :returns:     
    :rtype: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderEvaluationModes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``EvaluationMode`` 
    
    :param evaluationMode:     
    :type evaluationMode: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderEvaluationModes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    EvaluationPoint: NXOpen.Point = ...
    """
    Returns or sets  the evaluation point     
    
    <hr>
    
    Getter Method
    
    Signature ``EvaluationPoint`` 
    
    :returns:  Evaluation point  
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``EvaluationPoint`` 
    
    :param evaluationPoint:  Evaluation point  
    :type evaluationPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    EvaluationType: GapFlushnessBuilderEvaluationTypes = ...
    """
    Returns or sets  the evaluation type 
    
    <hr>
    
    Getter Method
    
    Signature ``EvaluationType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderEvaluationTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``EvaluationType`` 
    
    :param evaluationType: 
    :type evaluationType: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderEvaluationTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    IsNegativeToleranceLabelDisplayed: bool = ...
    """
    Returns or sets  the Label Display negative tolerance     
    
    <hr>
    
    Getter Method
    
    Signature ``IsNegativeToleranceLabelDisplayed`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``IsNegativeToleranceLabelDisplayed`` 
    
    :param showlabelNegative:     
    :type showlabelNegative: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    IsNominalLabelDisplayed: bool = ...
    """
    Returns or sets  the Label Display Nominal     
    
    <hr>
    
    Getter Method
    
    Signature ``IsNominalLabelDisplayed`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``IsNominalLabelDisplayed`` 
    
    :param showlabelNominal:     
    :type showlabelNominal: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    IsPositiveToleranceLabelDisplayed: bool = ...
    """
    Returns or sets  the Label Display positive tolerance    
    
    <hr>
    
    Getter Method
    
    Signature ``IsPositiveToleranceLabelDisplayed`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``IsPositiveToleranceLabelDisplayed`` 
    
    :param showlabelPositive:     
    :type showlabelPositive: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    LabelDisplayOption: GapFlushnessBuilderDisplayOptions = ...
    """
    Returns or sets  the display option type    
    
    <hr>
    
    Getter Method
    
    Signature ``LabelDisplayOption`` 
    
    :returns:       
    :rtype: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderDisplayOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``LabelDisplayOption`` 
    
    :param displayOption:       
    :type displayOption: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderDisplayOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    NegativeFlushnessTolerance: float = ...
    """
    Returns or sets  the negative tolerance for flushness      
    
    <hr>
    
    Getter Method
    
    Signature ``NegativeFlushnessTolerance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``NegativeFlushnessTolerance`` 
    
    :param negativeTolFlush:     
    :type negativeTolFlush: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    NegativeGapTolerance: float = ...
    """
    Returns or sets  the negative tolerance for gap     
    
    <hr>
    
    Getter Method
    
    Signature ``NegativeGapTolerance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``NegativeGapTolerance`` 
    
    :param negativeTolGap:     
    :type negativeTolGap: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    NominalFlushness: float = ...
    """
    Returns or sets  the nominal value  for flushness      
    
    <hr>
    
    Getter Method
    
    Signature ``NominalFlushness`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``NominalFlushness`` 
    
    :param nominalFlush:     
    :type nominalFlush: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    NominalGap: float = ...
    """
    Returns or sets  the nominal value  for gap       
    
    <hr>
    
    Getter Method
    
    Signature ``NominalGap`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``NominalGap`` 
    
    :param nominalGap:     
    :type nominalGap: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    PositiveFlushnessTolerance: float = ...
    """
    Returns or sets  the positive tolerance for flushness  
    
    <hr>
    
    Getter Method
    
    Signature ``PositiveFlushnessTolerance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``PositiveFlushnessTolerance`` 
    
    :param positiveTolFlush:     
    :type positiveTolFlush: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    PositiveGapTolerance: float = ...
    """
    Returns or sets  the positive tolerance for gap      
    
    <hr>
    
    Getter Method
    
    Signature ``PositiveGapTolerance`` 
    
    :returns:     
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``PositiveGapTolerance`` 
    
    :param positiveTolGap:     
    :type positiveTolGap: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    PreviewOption: bool = ...
    """
    Returns or sets  the preview option 
    
    <hr>
    
    Getter Method
    
    Signature ``PreviewOption`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``PreviewOption`` 
    
    :param previewOption:     
    :type previewOption: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SampleDistance: NXOpen.Expression = ...
    """
    Returns  the Sample Distance      
    
    <hr>
    
    Getter Method
    
    Signature ``SampleDistance`` 
    
    :returns:   Sample distance   
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SampleNumber: int = ...
    """
    Returns or sets  the sample number 
    
    <hr>
    
    Getter Method
    
    Signature ``SampleNumber`` 
    
    :returns:     
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``SampleNumber`` 
    
    :param sampleNumber:     
    :type sampleNumber: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SecondPanelFaces: NXOpen.ScCollector = ...
    """
    Returns  the Second Panel face selection      
    
    <hr>
    
    Getter Method
    
    Signature ``SecondPanelFaces`` 
    
    :returns:   Face collector  
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SecondPanelInnerContactCurves: NXOpen.Section = ...
    """
    Returns  the Second Panel inner contact section  
    
    <hr>
    
    Getter Method
    
    Signature ``SecondPanelInnerContactCurves`` 
    
    :returns:   curve/edge collector  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SecondPanelOuterContactCurves: NXOpen.Section = ...
    """
    Returns  the Second Panel outer contact section 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondPanelOuterContactCurves`` 
    
    :returns:   curve/edge collector  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SecondPanelType: GapFlushnessBuilderPanelTypes = ...
    """
    Returns or sets  the Second Panel type   
    
    <hr>
    
    Getter Method
    
    Signature ``SecondPanelType`` 
    
    :returns:     
    :rtype: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderPanelTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``SecondPanelType`` 
    
    :param panelType:     
    :type panelType: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderPanelTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SectionAlignment: GapFlushnessBuilderSectionAlignments = ...
    """
    Returns or sets  the Section Alignment     
    
    <hr>
    
    Getter Method
    
    Signature ``SectionAlignment`` 
    
    :returns:       
    :rtype: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderSectionAlignments` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``SectionAlignment`` 
    
    :param sectionAlignment:       
    :type sectionAlignment: :py:class:`NXOpen.GeometricAnalysis.GapFlushnessBuilderSectionAlignments` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SectionAlignmentDirection: NXOpen.Direction = ...
    """
    Returns or sets  the section alignment vector     
    
    <hr>
    
    Getter Method
    
    Signature ``SectionAlignmentDirection`` 
    
    :returns:  Section Alignment Direction vector  
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``SectionAlignmentDirection`` 
    
    :param sectionAlignmentDirection:  Section Alignment Direction vector  
    :type sectionAlignmentDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    ShowOutRangeLabels: bool = ...
    """
    Returns or sets  the show out of range labels 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOutRangeLabels`` 
    
    :returns:     
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOutRangeLabels`` 
    
    :param showOutRangeLabels:     
    :type showOutRangeLabels: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Null: GapFlushnessBuilder = ...  # unknown typename


