# module 'NXOpen.Facet'
#
# Automatically generated 2025-06-09T14:38:45.714768
#
"""Default documentation for NXOpen.Facet."""

import typing

import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class MultiPatchAlignmentBuilderResolutionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MultiPatchAlignmentBuilderResolutionType():
    """
    Determines the number of facets used in the alignment. 
    If you are importing an .AC file with image information, this option will 
    control how many image pixels are used in the alignment. If the imported 
    facet data does not have image information, the number of points being used 
    for the alignment will be controlled. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "High", "Uses a high number of facets for the alignment."
       "Medium", "Uses a medium number of facets for the alignment."
       "Low", "Uses a low number of facets for the alignment."
    """
    High = 0  # MultiPatchAlignmentBuilderResolutionTypeMemberType
    Medium = 1  # MultiPatchAlignmentBuilderResolutionTypeMemberType
    Low = 2  # MultiPatchAlignmentBuilderResolutionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MultiPatchAlignmentBuilder(NXOpen.Builder):
    """
    Aligns multiple facet bodies to one another without using reference points.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateMultiPatchAlignmentBuilder`
    
    Default values.
    
    ========================  =============================================
    Property                  Value
    ========================  =============================================
    Iteration                 10 
    ------------------------  ---------------------------------------------
    MaximumCheckingDistance   10.0 (millimeters part), 0.5 (inches part) 
    ------------------------  ---------------------------------------------
    Resolution                High 
    ------------------------  ---------------------------------------------
    Tolerance                 0.01 (millimeters part), 0.005 (inches part) 
    ========================  =============================================
    
    .. versionadded:: NX7.5.0
    """
    
    class ResolutionType():
        """
        Determines the number of facets used in the alignment. 
        If you are importing an .AC file with image information, this option will 
        control how many image pixels are used in the alignment. If the imported 
        facet data does not have image information, the number of points being used 
        for the alignment will be controlled. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "High", "Uses a high number of facets for the alignment."
           "Medium", "Uses a medium number of facets for the alignment."
           "Low", "Uses a low number of facets for the alignment."
        """
        High = 0  # MultiPatchAlignmentBuilderResolutionTypeMemberType
        Medium = 1  # MultiPatchAlignmentBuilderResolutionTypeMemberType
        Low = 2  # MultiPatchAlignmentBuilderResolutionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AlignmentBodies: SelectFacetedBodyList = ...
    """
    Returns  the facet bodies to be aligned.  
    
    <hr>
    
    Getter Method
    
    Signature ``AlignmentBodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBodyList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Iteration: int = ...
    """
    Returns or sets  the value indicating the number of times the alignment algorithm is applied.  
    
    Many iterations improve alignment accuracy but take longer. 
    
    <hr>
    
    Getter Method
    
    Signature ``Iteration`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Iteration`` 
    
    :param iteration: 
    :type iteration: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MaximumCheckingDistance: float = ...
    """
    Returns or sets  the distance facets may be from one another in order to be used 
    in the alignment.  
    
    Larger numbers slow the alignment process. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumCheckingDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumCheckingDistance`` 
    
    :param maximumCheckingDistance: 
    :type maximumCheckingDistance: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    ReferencePatches: SelectFacetedBodyList = ...
    """
    Returns  an optional reference facet body with a location and orientation that will 
    remain fixed, causing all of the other selected facet bodies to align with 
    it.  
    
    If you do not select a reference body, all of the selected facet bodies 
    will align to each other, without a fixed location. 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferencePatches`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBodyList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Resolution: MultiPatchAlignmentBuilderResolutionType = ...
    """
    Returns or sets  the type indicating number of facets to be used  in the alignment.  
    
    <hr>
    
    Getter Method
    
    Signature ``Resolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.MultiPatchAlignmentBuilderResolutionType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Resolution`` 
    
    :param resolution: 
    :type resolution: :py:class:`NXOpen.Facet.MultiPatchAlignmentBuilderResolutionType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Tolerance: float = ...
    """
    Returns or sets  the precision of the alignment.  
    
    Alignment will complete when tolerance is met or the number of iterations has been reached. 
    
    <hr>
    
    Getter Method
    
    Signature ``Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Tolerance`` 
    
    :param tolerance: 
    :type tolerance: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: MultiPatchAlignmentBuilder = ...  # unknown typename


class MergeFacetFacesBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`Facet.MergeFacetFacesBuilder` builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateMergeFacetFacesBuilder`
    
    Default values.
    
    ===========  =====
    Property     Value
    ===========  =====
    IsEditCopy   0 
    ===========  =====
    
    .. versionadded:: NX12.0.0
    """
    FaceCollector: NXOpen.ScCollector = ...
    """
    Returns  the face collector 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IsEditCopy: bool = ...
    """
    Returns or sets  the value indicating if a copy of the facet body to be used for Merge facet faces without altering the original 
    
    <hr>
    
    Getter Method
    
    Signature ``IsEditCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsEditCopy`` 
    
    :param isEditCopy: 
    :type isEditCopy: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    Null: MergeFacetFacesBuilder = ...  # unknown typename


class PolygonModelingBuilderConvertTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PolygonModelingBuilderConvertTypes():
    """
    the conversion type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Convergent", " - "
       "Facet", " - "
    """
    Convergent = 0  # PolygonModelingBuilderConvertTypesMemberType
    Facet = 1  # PolygonModelingBuilderConvertTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PolygonModelingBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.PolygonModelingBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreatePolygonModelingBuilder`
    
    Default values.
    
    ============  ===========
    Property      Value
    ============  ===========
    ConvertType   Convergent 
    ============  ===========
    
    .. versionadded:: NX12.0.0
    """
    
    class ConvertTypes():
        """
        the conversion type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Convergent", " - "
           "Facet", " - "
        """
        Convergent = 0  # PolygonModelingBuilderConvertTypesMemberType
        Facet = 1  # PolygonModelingBuilderConvertTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def RemoveParameterOfBody(self, bodyTag: NXOpen.Body) -> None:
        """
        Removes the parameters of the input body
        
        Signature ``RemoveParameterOfBody(bodyTag)`` 
        
        :param bodyTag: 
        :type bodyTag: :py:class:`NXOpen.Body` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_polygon_modeling (" NX Polygon Modeling")
        """
        ...
    
    
    def MergeAllFaces(self, bodyTag: NXOpen.Body) -> None:
        """
        Merges all faces of the input body
        
        Signature ``MergeAllFaces(bodyTag)`` 
        
        :param bodyTag: 
        :type bodyTag: :py:class:`NXOpen.Body` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_polygon_modeling (" NX Polygon Modeling")
        """
        ...
    
    ConvertType: PolygonModelingBuilderConvertTypes = ...
    """
    Returns or sets  the convert type 
    
    <hr>
    
    Getter Method
    
    Signature ``ConvertType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.PolygonModelingBuilderConvertTypes` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConvertType`` 
    
    :param convertType: 
    :type convertType: :py:class:`NXOpen.Facet.PolygonModelingBuilderConvertTypes` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    SelectFacetBodies: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the selected bodies 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectFacetBodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: PolygonModelingBuilder = ...  # unknown typename


class BestFitAlignBuilderConstraintOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BestFitAlignBuilderConstraintOptions():
    """
    Represents the constraint options 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Free", "No constraint"
       "OnlyTranslation", "Only translation"
       "TranslationInPlane", "Translation in the plane"
       "TranslationAlongDirection", "Translation along direction"
       "OnlyRotation", "Only rotation"
       "RotationAroundPoint", "Rotation around specific point"
       "RotationAroundLine", "Rotation around specific line"
       "HoldToPlane", "Moving in the plane"
       "HoldToLine", "Moving along the line"
    """
    Free = 0  # BestFitAlignBuilderConstraintOptionsMemberType
    OnlyTranslation = 1  # BestFitAlignBuilderConstraintOptionsMemberType
    TranslationInPlane = 2  # BestFitAlignBuilderConstraintOptionsMemberType
    TranslationAlongDirection = 3  # BestFitAlignBuilderConstraintOptionsMemberType
    OnlyRotation = 4  # BestFitAlignBuilderConstraintOptionsMemberType
    RotationAroundPoint = 5  # BestFitAlignBuilderConstraintOptionsMemberType
    RotationAroundLine = 6  # BestFitAlignBuilderConstraintOptionsMemberType
    HoldToPlane = 7  # BestFitAlignBuilderConstraintOptionsMemberType
    HoldToLine = 8  # BestFitAlignBuilderConstraintOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BestFitAlignBuilder(NXOpen.Builder):
    """
    This class performs the best fit alignment between objects   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateBestFitAlignBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    class ConstraintOptions():
        """
        Represents the constraint options 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Free", "No constraint"
           "OnlyTranslation", "Only translation"
           "TranslationInPlane", "Translation in the plane"
           "TranslationAlongDirection", "Translation along direction"
           "OnlyRotation", "Only rotation"
           "RotationAroundPoint", "Rotation around specific point"
           "RotationAroundLine", "Rotation around specific line"
           "HoldToPlane", "Moving in the plane"
           "HoldToLine", "Moving along the line"
        """
        Free = 0  # BestFitAlignBuilderConstraintOptionsMemberType
        OnlyTranslation = 1  # BestFitAlignBuilderConstraintOptionsMemberType
        TranslationInPlane = 2  # BestFitAlignBuilderConstraintOptionsMemberType
        TranslationAlongDirection = 3  # BestFitAlignBuilderConstraintOptionsMemberType
        OnlyRotation = 4  # BestFitAlignBuilderConstraintOptionsMemberType
        RotationAroundPoint = 5  # BestFitAlignBuilderConstraintOptionsMemberType
        RotationAroundLine = 6  # BestFitAlignBuilderConstraintOptionsMemberType
        HoldToPlane = 7  # BestFitAlignBuilderConstraintOptionsMemberType
        HoldToLine = 8  # BestFitAlignBuilderConstraintOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    DestinationObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the destination objects 
    
    <hr>
    
    Getter Method
    
    Signature ``DestinationObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Direction: NXOpen.Direction = ...
    """
    Returns or sets  the plane or line direction 
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    FitConstraints: BestFitAlignBuilderConstraintOptions = ...
    """
    Returns or sets  the fit constraint 
    
    <hr>
    
    Getter Method
    
    Signature ``FitConstraints`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.BestFitAlignBuilderConstraintOptions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FitConstraints`` 
    
    :param fitConstraints: 
    :type fitConstraints: :py:class:`NXOpen.Facet.BestFitAlignBuilderConstraintOptions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    GlobalSearch: bool = ...
    """
    Returns or sets  a value indicating whether to do a global search 
    
    <hr>
    
    Getter Method
    
    Signature ``GlobalSearch`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GlobalSearch`` 
    
    :param globalSearch: 
    :type globalSearch: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MobileObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the mobile objects 
    
    <hr>
    
    Getter Method
    
    Signature ``MobileObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    RotateCenter: NXOpen.Point = ...
    """
    Returns or sets  the rotation center 
    
    <hr>
    
    Getter Method
    
    Signature ``RotateCenter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RotateCenter`` 
    
    :param rotateCenter: 
    :type rotateCenter: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    SourceObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the source objects 
    
    <hr>
    
    Getter Method
    
    Signature ``SourceObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: BestFitAlignBuilder = ...  # unknown typename


class BridgeFacetBodyBuilderSmoothTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BridgeFacetBodyBuilderSmoothTypes():
    """
    Represents the smoothness type for the inserted new facets 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "Insert new facets with linear smoothness"
       "TangentBased", "Insert new facets with tangent smoothness"
    """
    Linear = 0  # BridgeFacetBodyBuilderSmoothTypesMemberType
    TangentBased = 1  # BridgeFacetBodyBuilderSmoothTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BridgeFacetBodyBuilderInputMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BridgeFacetBodyBuilderInput():
    """
    Represents the option for keeping, deleting or hiding input two facet bodies after builder committing 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Keep", "Keep the input facet body after builder committing"
       "Delete", "Delete the input facet body after builder committing"
       "Hide", "Hide the input facet body after builder committing"
    """
    Keep = 0  # BridgeFacetBodyBuilderInputMemberType
    Delete = 1  # BridgeFacetBodyBuilderInputMemberType
    Hide = 2  # BridgeFacetBodyBuilderInputMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BridgeFacetBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.BridgeFacetBodyBuilder`
    It bridges two disjoint NX facet bodies.  
    
    User need to specify the range for each input facet body.
    It returns a new megered NX facet Body. The two input bodies can be kept, deleted or hidden.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateBridgeFacetBodyBuilder`
    
    Default values.
    
    ============  =======
    Property      Value
    ============  =======
    InputStatus   Keep 
    ------------  -------
    Smoothness    Linear 
    ============  =======
    
    .. versionadded:: NX9.0.0
    """
    
    class SmoothTypes():
        """
        Represents the smoothness type for the inserted new facets 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "Insert new facets with linear smoothness"
           "TangentBased", "Insert new facets with tangent smoothness"
        """
        Linear = 0  # BridgeFacetBodyBuilderSmoothTypesMemberType
        TangentBased = 1  # BridgeFacetBodyBuilderSmoothTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Input():
        """
        Represents the option for keeping, deleting or hiding input two facet bodies after builder committing 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Keep", "Keep the input facet body after builder committing"
           "Delete", "Delete the input facet body after builder committing"
           "Hide", "Hide the input facet body after builder committing"
        """
        Keep = 0  # BridgeFacetBodyBuilderInputMemberType
        Delete = 1  # BridgeFacetBodyBuilderInputMemberType
        Hide = 2  # BridgeFacetBodyBuilderInputMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def FlipRange1(self) -> None:
        """
        Flip the range between the first and second vertex on the first facet body 
        
        Signature ``FlipRange1()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FlipRange2(self) -> None:
        """
        Flip the range between the first and second vertex on the second facet body 
        
        Signature ``FlipRange2()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance used in the bridge facet body feature 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    """
    FacetBodyOne: SelectFacetedBody = ...
    """
    Returns  the first NX facet body to be bridged 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodyOne`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBody` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FacetBodyTwo: SelectFacetedBody = ...
    """
    Returns  the second NX facet body to be bridged 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodyTwo`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBody` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    InputStatus: BridgeFacetBodyBuilderInput = ...
    """
    Returns or sets  the option to specify how to deal with the input two facet bodies: keep, delete or hide 
    
    <hr>
    
    Getter Method
    
    Signature ``InputStatus`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.BridgeFacetBodyBuilderInput` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputStatus`` 
    
    :param inputStatus: 
    :type inputStatus: :py:class:`NXOpen.Facet.BridgeFacetBodyBuilderInput` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Smoothness: BridgeFacetBodyBuilderSmoothTypes = ...
    """
    Returns or sets  the inserted facet smooth type 
    
    <hr>
    
    Getter Method
    
    Signature ``Smoothness`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.BridgeFacetBodyBuilderSmoothTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Smoothness`` 
    
    :param smoothType: 
    :type smoothType: :py:class:`NXOpen.Facet.BridgeFacetBodyBuilderSmoothTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Vertex1Range1: NXOpen.Point = ...
    """
    Returns or sets  the first vertex used to define the range on the the first facet body 
    
    <hr>
    
    Getter Method
    
    Signature ``Vertex1Range1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vertex1Range1`` 
    
    :param vertex1Range1: 
    :type vertex1Range1: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Vertex1Range2: NXOpen.Point = ...
    """
    Returns or sets  the first vertex used to defind the range on the second facet body 
    
    <hr>
    
    Getter Method
    
    Signature ``Vertex1Range2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vertex1Range2`` 
    
    :param vertex1Range2: 
    :type vertex1Range2: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Vertex2Range1: NXOpen.Point = ...
    """
    Returns or sets  the second vertex used to define the range on the first facet body 
    
    <hr>
    
    Getter Method
    
    Signature ``Vertex2Range1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vertex2Range1`` 
    
    :param vertex2Range1: 
    :type vertex2Range1: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Vertex2Range2: NXOpen.Point = ...
    """
    Returns or sets  the second vertex used to defind the range on the second facet body 
    
    <hr>
    
    Getter Method
    
    Signature ``Vertex2Range2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vertex2Range2`` 
    
    :param vertex2Range2: 
    :type vertex2Range2: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: BridgeFacetBodyBuilder = ...  # unknown typename


class SewFacetBodyBuilderInputMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SewFacetBodyBuilderInput():
    """
    Represents the option for keeping, deleting or hiding input two facet bodies after builder committing 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Keep", "Keep the input facet body after builder committing"
       "Delete", "Delete the input facet body after builder committing"
       "Hide", "Hide the input facet body after builder committing"
    """
    Keep = 0  # SewFacetBodyBuilderInputMemberType
    Delete = 1  # SewFacetBodyBuilderInputMemberType
    Hide = 2  # SewFacetBodyBuilderInputMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SewFacetBodyBuilderVertexIndexMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SewFacetBodyBuilderVertexIndex():
    """
    Index of the vertex 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "First", "Index of the first vertex"
       "Second", "Index of the second vertex"
    """
    First = 0  # SewFacetBodyBuilderVertexIndexMemberType
    Second = 1  # SewFacetBodyBuilderVertexIndexMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SewFacetBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.SewFacetBodyBuilder`
    It sews two touching NX facet bodies.  
    
    User need to specify the range on one of input body.
    The range on the other body is calculated automatically by choosing the closest vertex.
    It retruns a new mergered NX facet body. The two input bodies can be kept, deleted or hidden.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateSewFacetBodyBuilder`
    
    Default values.
    
    =====================  ===========================================
    Property               Value
    =====================  ===========================================
    DeformDistance.Value   0.5 (millimeters part), 0.05 (inches part) 
    ---------------------  -------------------------------------------
    InputStatus            Keep 
    =====================  ===========================================
    
    .. versionadded:: NX9.0.0
    """
    
    class Input():
        """
        Represents the option for keeping, deleting or hiding input two facet bodies after builder committing 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Keep", "Keep the input facet body after builder committing"
           "Delete", "Delete the input facet body after builder committing"
           "Hide", "Hide the input facet body after builder committing"
        """
        Keep = 0  # SewFacetBodyBuilderInputMemberType
        Delete = 1  # SewFacetBodyBuilderInputMemberType
        Hide = 2  # SewFacetBodyBuilderInputMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class VertexIndex():
        """
        Index of the vertex 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "First", "Index of the first vertex"
           "Second", "Index of the second vertex"
        """
        First = 0  # SewFacetBodyBuilderVertexIndexMemberType
        Second = 1  # SewFacetBodyBuilderVertexIndexMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def FlipRange(self) -> None:
        """
        Flip the range between the first and second vertex 
        
        Signature ``FlipRange()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    DeformBody: SelectFacetedBody = ...
    """
    Returns  the deform body to be sewed 
    
    <hr>
    
    Getter Method
    
    Signature ``DeformBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBody` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    DeformDistance: NXOpen.Expression = ...
    """
    Returns  the distance to control the deform area on the deform body 
    
    <hr>
    
    Getter Method
    
    Signature ``DeformDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance used in the merge touching facet body feature 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    """
    InputStatus: SewFacetBodyBuilderInput = ...
    """
    Returns or sets  the option to specify how to deal with the input two facet bodies: keep, delete or hide 
    
    <hr>
    
    Getter Method
    
    Signature ``InputStatus`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SewFacetBodyBuilderInput` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputStatus`` 
    
    :param inputStatus: 
    :type inputStatus: :py:class:`NXOpen.Facet.SewFacetBodyBuilderInput` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    """
    TargetBody: SelectFacetedBody = ...
    """
    Returns  the target body to be sewed 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBody` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Vertex1: NXOpen.Point = ...
    """
    Returns or sets  the first vertex used to define the range 
    
    <hr>
    
    Getter Method
    
    Signature ``Vertex1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vertex1`` 
    
    :param vertexPoint1: 
    :type vertexPoint1: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    """
    Vertex2: NXOpen.Point = ...
    """
    Returns or sets  the second vertex used to define the range 
    
    <hr>
    
    Getter Method
    
    Signature ``Vertex2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vertex2`` 
    
    :param vertexPoint2: 
    :type vertexPoint2: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    """
    Null: SewFacetBodyBuilder = ...  # unknown typename


class DecimateFacetBodyBuilderDecimateMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DecimateFacetBodyBuilderDecimateMethodType():
    """
    Decimate Method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ChordalDeviation", "Chordal deviation reduces the number of facets by removing facets which do not effect the overall accuracy of the mesh."
       "SmallestFacet", "Smallest facet removes all facets smaller than the defined area, thus removing facets deemed to be redundant by the designer."
       "Percentage", "Percentage option allows the user to reduce the facet count by overall percentage."
    """
    ChordalDeviation = 0  # DecimateFacetBodyBuilderDecimateMethodTypeMemberType
    SmallestFacet = 1  # DecimateFacetBodyBuilderDecimateMethodTypeMemberType
    Percentage = 2  # DecimateFacetBodyBuilderDecimateMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DecimateFacetBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.DecimateFacetBodyBuilder`.  
    
    Decimate Body Builder is a function to facilitate the reduction of data by reducing the density of facets while keeping the general shape in tact.
    Three different methods are provided to reduce the data. 
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateDecimateFacetBodyBuilder`
    
    Default values.
    
    ===============  =================
    Property         Value
    ===============  =================
    AngleThreshold   15 
    ---------------  -----------------
    DecimateMethod   ChordalDeviation 
    ---------------  -----------------
    IsEditCopy       0 
    ---------------  -----------------
    IsLockBoundary   0 
    ---------------  -----------------
    MinimumArea      1 
    ---------------  -----------------
    Percentage       10 
    ---------------  -----------------
    Tolerance        0.25 
    ===============  =================
    
    .. versionadded:: NX7.5.0
    """
    
    class DecimateMethodType():
        """
        Decimate Method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ChordalDeviation", "Chordal deviation reduces the number of facets by removing facets which do not effect the overall accuracy of the mesh."
           "SmallestFacet", "Smallest facet removes all facets smaller than the defined area, thus removing facets deemed to be redundant by the designer."
           "Percentage", "Percentage option allows the user to reduce the facet count by overall percentage."
        """
        ChordalDeviation = 0  # DecimateFacetBodyBuilderDecimateMethodTypeMemberType
        SmallestFacet = 1  # DecimateFacetBodyBuilderDecimateMethodTypeMemberType
        Percentage = 2  # DecimateFacetBodyBuilderDecimateMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AngleThreshold: float = ...
    """
    Returns or sets  the value indicating maximum angle, where any facets with a larger relative angle are not reduced.  
    
    This allows sharp edges to be retained. 
    
    <hr>
    
    Getter Method
    
    Signature ``AngleThreshold`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AngleThreshold`` 
    
    :param angleThreshold: 
    :type angleThreshold: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Bodies: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the facet bodies to be decimated.  
    
    Inputs to this command can be convergent objects.
    
    <hr>
    
    Getter Method
    
    Signature ``Bodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.Facet.SubdivideFacetBodyBuilder.FacetCollector` instead.
    
    License requirements: None.
    """
    DecimateMethod: DecimateFacetBodyBuilderDecimateMethodType = ...
    """
    Returns or sets  the decimation method 
    
    <hr>
    
    Getter Method
    
    Signature ``DecimateMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DecimateMethod`` 
    
    :param decimateMethod: 
    :type decimateMethod: :py:class:`NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    FacetBodies: SelectFacetedBodyList = ...
    """
    Returns  the facet bodies to be decimated 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBodyList` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX11.0.0
       Use :py:meth:`NXOpen.Facet.DecimateFacetBodyBuilder.Bodies` instead.
    
    License requirements: None.
    """
    FacetCollector: NXOpen.FacetCollector = ...
    """
    Returns or sets  a collector of facets on the facet bodies to be decimated.  
    
    <hr>
    
    Getter Method
    
    Signature ``FacetCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FacetCollector`` 
    
    :param collector: 
    :type collector: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsEditCopy: bool = ...
    """
    Returns or sets  the value indicating if a copy of the facet body to be decimated without altering the original 
    
    <hr>
    
    Getter Method
    
    Signature ``IsEditCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsEditCopy`` 
    
    :param isEditCopy: 
    :type isEditCopy: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsLockBoundary: bool = ...
    """
    Returns or sets  the value indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact 
    
    <hr>
    
    Getter Method
    
    Signature ``IsLockBoundary`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsLockBoundary`` 
    
    :param isLockBoundary: 
    :type isLockBoundary: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MinimumArea: float = ...
    """
    Returns or sets  the value indicating area of the smallest facet that is to be retained.  
    
    All the facets
    smaller than the minimum area are removed. This value is used when
    :py:class:`NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType` is
    :py:class:`NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType.SmallestFacet <NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumArea`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumArea`` 
    
    :param minimumArea: 
    :type minimumArea: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Percentage: float = ...
    """
    Returns or sets  the value indicating percentage by which facet count is to be reduced.  
    
    This value is used when
    :py:class:`NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType` is
    :py:class:`NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType.Percentage <NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``Percentage`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Percentage`` 
    
    :param percentage: 
    :type percentage: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    RegionList: NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList = ...
    """
    Returns  an optional list of regions on the facet bodies to be decimated.  
    
    <hr>
    
    Getter Method
    
    Signature ``RegionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.Facet.SubdivideFacetBodyBuilder.FacetCollector` instead.
    
    License requirements: None.
    """
    Tolerance: float = ...
    """
    Returns or sets  the value indicating maximum chordal deviation from the original facet body.  
    
    The value is used
    when :py:class:`NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType` is
    :py:class:`NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType.ChordalDeviation <NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``Tolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Tolerance`` 
    
    :param tolerance: 
    :type tolerance: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: DecimateFacetBodyBuilder = ...  # unknown typename


class CreateTransitionBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CreateTransitionBuilderTypes():
    """
    the transition type. The round type creates fillet type transition. The flat type creates chamfer type transition. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Round", " - "
       "Flat", " - "
    """
    Round = 0  # CreateTransitionBuilderTypesMemberType
    Flat = 1  # CreateTransitionBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CreateTransitionBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.CreateTransitionBuilder` builder.  
    
    This class creates the blend/chamfer of a facet body.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateCreateTransitionBuilder`
    
    Default values.
    
    ===============  ========================================
    Property         Value
    ===============  ========================================
    Distance.Value   5 (millimeters part), 0.2 (inches part) 
    ---------------  ----------------------------------------
    IsClosed         0 
    ---------------  ----------------------------------------
    IsEditCopy       0 
    ---------------  ----------------------------------------
    Radius.Value     5 (millimeters part), 0.2 (inches part) 
    ===============  ========================================
    
    .. versionadded:: NX12.0.0
    """
    
    class Types():
        """
        the transition type. The round type creates fillet type transition. The flat type creates chamfer type transition. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Round", " - "
           "Flat", " - "
        """
        Round = 0  # CreateTransitionBuilderTypesMemberType
        Flat = 1  # CreateTransitionBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Distance: NXOpen.Expression = ...
    """
    Returns  the distance.  
    
    This value is for chamfer operation. 
    
    <hr>
    
    Getter Method
    
    Signature ``Distance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IsClosed: bool = ...
    """
    Returns or sets  the is closed.  
    
    The flag indicate if the edge is closed or not. 
    
    <hr>
    
    Getter Method
    
    Signature ``IsClosed`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsClosed`` 
    
    :param isClosed: 
    :type isClosed: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    IsEditCopy: bool = ...
    """
    Returns or sets  the flag indicating if the transition is created on the copy of the input facet body.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsEditCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsEditCopy`` 
    
    :param isEditCopy: 
    :type isEditCopy: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    Radius: NXOpen.Expression = ...
    """
    Returns  the radius.  
    
    This value is for blend operation. 
    
    <hr>
    
    Getter Method
    
    Signature ``Radius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SelectedBody: NXOpen.DisplayableObject = ...
    """
    Returns or sets  the selected facet body.  
    
    It could be a convergent object. 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObject` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectedBody`` 
    
    :param selectedBody: 
    :type selectedBody: :py:class:`NXOpen.DisplayableObject` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    SelectedPoints: NXOpen.Features.GeometricConstraintDataManager = ...
    """
    Returns  the selected points.  
    
    The points will define the edge which needs blend/chamfer. 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedPoints`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.GeometricConstraintDataManager` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Type: CreateTransitionBuilderTypes = ...
    """
    Returns or sets  the type.  
    
    This value defines the transition type. 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.CreateTransitionBuilderTypes` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Facet.CreateTransitionBuilderTypes` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    Null: CreateTransitionBuilder = ...  # unknown typename


class FacetedFaceFacetedfaceTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetedFaceFacetedfaceType():
    """
    Facet Face type  
    
    .. versionadded:: NX8.5.1
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Undefined", "Undefined body type"
       "Planar", "Planar face"
       "Cylindrical", "Cylindrical face"
       "Conical", "Conical face"
       "Spherical", "Spherical face"
       "Toroidal", "Face from toroid"
       "Parametric", "Parametric face"
    """
    Undefined = 0  # FacetedFaceFacetedfaceTypeMemberType
    Planar = 1  # FacetedFaceFacetedfaceTypeMemberType
    Cylindrical = 2  # FacetedFaceFacetedfaceTypeMemberType
    Conical = 3  # FacetedFaceFacetedfaceTypeMemberType
    Spherical = 4  # FacetedFaceFacetedfaceTypeMemberType
    Toroidal = 5  # FacetedFaceFacetedfaceTypeMemberType
    Parametric = 6  # FacetedFaceFacetedfaceTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetedFace(NXOpen.DisplayableObject, NXOpen.IParameterizedSurface):
    """
    Represents a faceted face.  
    
    Instances of this class may be
    generated when recording a journal, but they cannot be created
    directly. 
    
    .. versionadded:: NX5.0.0
    """
    
    class FacetedfaceType():
        """
        Facet Face type  
        
        .. versionadded:: NX8.5.1
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Undefined", "Undefined body type"
           "Planar", "Planar face"
           "Cylindrical", "Cylindrical face"
           "Conical", "Conical face"
           "Spherical", "Spherical face"
           "Toroidal", "Face from toroid"
           "Parametric", "Parametric face"
        """
        Undefined = 0  # FacetedFaceFacetedfaceTypeMemberType
        Planar = 1  # FacetedFaceFacetedfaceTypeMemberType
        Cylindrical = 2  # FacetedFaceFacetedfaceTypeMemberType
        Conical = 3  # FacetedFaceFacetedfaceTypeMemberType
        Spherical = 4  # FacetedFaceFacetedfaceTypeMemberType
        Toroidal = 5  # FacetedFaceFacetedfaceTypeMemberType
        Parametric = 6  # FacetedFaceFacetedfaceTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetNumberOfEdges(self) -> int:
        """
        Returns the number of edges in the faceted face  
        
        Signature ``GetNumberOfEdges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def GetEdges(self) -> 'list[FacetedEdge]':
        """
        Returns the edges connected to the face  
        
        Signature ``GetEdges()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Facet.FacetedEdge` 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def GetBody(self) -> FacetedBody:
        """
        Returns the facet body containing this facet face  
        
        Signature ``GetBody()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def GetSurfaceData(self) -> tuple:
        """
        Returns the surface information for this face 
        
        tag_t    faceted_face     : The input edge tag for which face information is required.  
        
        PNT3_p_t position         : Plane: Position on Plane
        Origin for other
        PNT3_p_t dir              : Plane: Normal direction
        Axis for others.
        double   *radius          : Not applicable for planes
        Cylinder: Radius of Cylinder, 
        Sphere: Radius of Sphere
        Cone: Radius of Circle on the cone and in the plane passing through the position.
        double   *radius_or_angle : Cone: Half Angle. 
        logical  *sense           : Indicates the sense of normal
        
        Signature ``GetSurfaceData()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (position, dir, radius, radiusOrAngle, sense). position is a :py:class:`NXOpen.Point3d`. dir is a :py:class:`NXOpen.Point3d`. radius is a float. radiusOrAngle is a float. sense is a bool. 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    FaceType: FacetedFaceFacetedfaceType = ...
    """
    Returns  the type of the face 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.FacetedFaceFacetedfaceType` 
    
    .. versionadded:: NX8.5.1
    
    License requirements: None.
    """
    Null: FacetedFace = ...  # unknown typename


class FacetedBodyFacetedbodyTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetedBodyFacetedbodyType():
    """
    Body type  
    
    .. versionadded:: NX8.5.1
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Undefined", "Undefined body type"
       "SolidBody", " - "
       "SheetBody", " - "
    """
    Undefined = 0  # FacetedBodyFacetedbodyTypeMemberType
    SolidBody = 1  # FacetedBodyFacetedbodyTypeMemberType
    SheetBody = 2  # FacetedBodyFacetedbodyTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetedBody(NXOpen.DisplayableObject):
    """
    Represents a faceted body.  
    
    Instances of this class cannot be created directly by the user, but can
    be created using the methods of FacetedBodyCollection.
    
    .. versionadded:: NX5.0.0
    """
    
    class FacetedbodyType():
        """
        Body type  
        
        .. versionadded:: NX8.5.1
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Undefined", "Undefined body type"
           "SolidBody", " - "
           "SheetBody", " - "
        """
        Undefined = 0  # FacetedBodyFacetedbodyTypeMemberType
        SolidBody = 1  # FacetedBodyFacetedbodyTypeMemberType
        SheetBody = 2  # FacetedBodyFacetedbodyTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetNumberOfFacets(self, levelOfDetail: int) -> int:
        """
        Get the number of facets in the given level of detail.  
        
        Signature ``GetNumberOfFacets(levelOfDetail)`` 
        
        :param levelOfDetail:  level of detail to query  
        :type levelOfDetail: int 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFaces(self) -> 'list[FacetedFace]':
        """
        Returns the faces in the faceted body.  
        
        This only works for JT Facets.
        
        Signature ``GetFaces()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Facet.FacetedFace` 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def GetNumberOfEdges(self) -> int:
        """
        Returns the number of edges in the faceted body.  
        
        This only works for JT Facets.
        
        Signature ``GetNumberOfEdges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def GetEdges(self) -> 'list[FacetedEdge]':
        """
        Returns the edges in the faceted body.  
        
        This only works for JT Facets.
        
        Signature ``GetEdges()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Facet.FacetedEdge` 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def HasTopologyInformation(self) -> bool:
        """
        Returns whether the FACET has topology information.  
        
        This only works for JT Facets.
        
        Signature ``HasTopologyInformation()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def HasLightWeightAnalytics(self) -> bool:
        """
        Returns whether the FACET has analytical information.  
        
        This only works for JT Facets.
        
        Signature ``HasLightWeightAnalytics()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def GetParameters(self) -> FacetingParameters:
        """
        Get the faceted body parameters
        
        Signature ``GetParameters()`` 
        
        :returns:  faceting parameters for this body  
        :rtype: :py:class:`NXOpen.Facet.FacetingParameters` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetParameters(self, parameters: FacetingParameters) -> None:
        """
        Set the faceted body parameters, it will retessellate the body with the new parameters
        
        Signature ``SetParameters(parameters)`` 
        
        :param parameters:  new facetting faceting parameters to set for this body  
        :type parameters: :py:class:`NXOpen.Facet.FacetingParameters` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DestroyOwnedFacets(self) -> None:
        """
        Destroys all :py:class:`IFacet` objects owned by this body.
        
        Please note that this method does not geometrically delete a facet from its surface mesh leaving a hole. 
        It only deletes the tagged object created to represent the individual facet.
        
        Signature ``DestroyOwnedFacets()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    AssociatedBody: NXOpen.Body = ...
    """
    Returns 
    the solid body associated with this facet body.  
    
    <hr>
    
    Getter Method
    
    Signature ``AssociatedBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Body` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    BodyType: FacetedBodyFacetedbodyType = ...
    """
    Returns  the type of the body.  
    
    This only works for JT Facets.
    
    <hr>
    
    Getter Method
    
    Signature ``BodyType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.FacetedBodyFacetedbodyType` 
    
    .. versionadded:: NX8.5.1
    
    License requirements: None.
    """
    IsAssemblyLevel: bool = ...
    """
    Returns 
    a flag indicating this is an assembly level representation.  
    
    That is
    this facet body is associated with an occurrence of a solid body. 
    
    <hr>
    
    Getter Method
    
    Signature ``IsAssemblyLevel`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    IsAssociatedBodyLoaded: bool = ...
    """
    Returns 
    the load state of the solid body associated with this facet body.  
    
    False if there is no associated body.
    
    <hr>
    
    Getter Method
    
    Signature ``IsAssociatedBodyLoaded`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    IsSheetBody: bool = ...
    """
    Returns  true if the body is a sheet body 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSheetBody`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX8.5.1
       Use :py:meth:`NXOpen.Facet.FacetedBody.BodyType` instead
    
    License requirements: None.
    """
    IsSolidBody: bool = ...
    """
    Returns  true if the body is a solid body 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSolidBody`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX8.5.1
       Use :py:meth:`NXOpen.Facet.FacetedBody.BodyType` instead.
    
    License requirements: None.
    """
    NumberOfFaces: int = ...
    """
    Returns 
    the number of faces in this faceted body in the highest level of detail.  
    
    Typically only useful if the model has been derived from a solid model. 
    For models constructed directly, the output will be number of facets/triangles, since there would be no faces. 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfFaces`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    NumberOfLevelsOfDetail: int = ...
    """
    Returns 
    the number of levels of detail in this faceted body.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfLevelsOfDetail`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    SurfaceArea: float = ...
    """
    Returns 
    the surface area of the faceted body in part units for its
    highest level of detail.  
    
    <hr>
    
    Getter Method
    
    Signature ``SurfaceArea`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Volume: float = ...
    """
    Returns 
    the volume of the faceted body in part units for its
    highest level of detail.  
    
    <hr>
    
    Getter Method
    
    Signature ``Volume`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: FacetedBody = ...  # unknown typename


class AdjustMinimumRadiusBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.AdjustMinimumRadiusBuilder`.  
    
    It smooths the input bodies such that their minimum radius of curvature is larger than the prescribed radius of curvature.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateFacetAdjustMinimumRadiusBuilder`
    
    .. versionadded:: NX12.0.0
    """
    FacetBodies: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the input facet body list.  
    
    Inputs to this command can be convergent objects. 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    MinimumRadius: float = ...
    """
    Returns or sets  the minimum radius of curvature 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumRadius`` 
    
    :param radius: 
    :type radius: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    SelectedFacet: NXOpen.FacetCollector = ...
    """
    Returns  the input facet body list.  
    
    Inputs to this command can be convergent objects. 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedFacet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: AdjustMinimumRadiusBuilder = ...  # unknown typename


class STLImportBuilderAngularToleranceTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class STLImportBuilderAngularToleranceTypes():
    """
    The angular tolerance types
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Coarse", " - "
       "Medium", " - "
       "Fine", " - "
    """
    Coarse = 0  # STLImportBuilderAngularToleranceTypesMemberType
    Medium = 1  # STLImportBuilderAngularToleranceTypesMemberType
    Fine = 2  # STLImportBuilderAngularToleranceTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class STLImportBuilderSTLFileUnitsTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class STLImportBuilderSTLFileUnitsTypes():
    """
    The STL file units types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Meters", " - "
       "Millimeters", " - "
       "Inches", " - "
    """
    Meters = 0  # STLImportBuilderSTLFileUnitsTypesMemberType
    Millimeters = 1  # STLImportBuilderSTLFileUnitsTypesMemberType
    Inches = 2  # STLImportBuilderSTLFileUnitsTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class STLImportBuilderFacetBodyTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class STLImportBuilderFacetBodyTypes():
    """
    These represent the type of body that will get created on importing the STL file 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Psm", "Import to Facet Brep format"
       "Nx", "Import To NX Facet Format"
       "Jt", "Import to JT format"
    """
    Psm = 0  # STLImportBuilderFacetBodyTypesMemberType
    Nx = 1  # STLImportBuilderFacetBodyTypesMemberType
    Jt = 2  # STLImportBuilderFacetBodyTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class STLImportBuilder(NXOpen.Builder):
    """
    The STL file import builder.  
    
    Inputs to this class can be convergent objects.
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateSTLImportBuilder`
    
    Default values.
    
    =========================  ============
    Property                   Value
    =========================  ============
    AngularTolerance           Medium 
    -------------------------  ------------
    FacetBodyType              Psm 
    -------------------------  ------------
    HideSmoothEdges            1 
    -------------------------  ------------
    MinimumAngleFoldedFacets   15.0 
    -------------------------  ------------
    MinimumFacetNumber         100 
    -------------------------  ------------
    STLFileUnits               Millimeters 
    -------------------------  ------------
    ShowInformationWindow      0 
    =========================  ============
    
    .. versionadded:: NX6.0.0
    """
    
    class AngularToleranceTypes():
        """
        The angular tolerance types
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Coarse", " - "
           "Medium", " - "
           "Fine", " - "
        """
        Coarse = 0  # STLImportBuilderAngularToleranceTypesMemberType
        Medium = 1  # STLImportBuilderAngularToleranceTypesMemberType
        Fine = 2  # STLImportBuilderAngularToleranceTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class STLFileUnitsTypes():
        """
        The STL file units types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Meters", " - "
           "Millimeters", " - "
           "Inches", " - "
        """
        Meters = 0  # STLImportBuilderSTLFileUnitsTypesMemberType
        Millimeters = 1  # STLImportBuilderSTLFileUnitsTypesMemberType
        Inches = 2  # STLImportBuilderSTLFileUnitsTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FacetBodyTypes():
        """
        These represent the type of body that will get created on importing the STL file 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Psm", "Import to Facet Brep format"
           "Nx", "Import To NX Facet Format"
           "Jt", "Import to JT format"
        """
        Psm = 0  # STLImportBuilderFacetBodyTypesMemberType
        Nx = 1  # STLImportBuilderFacetBodyTypesMemberType
        Jt = 2  # STLImportBuilderFacetBodyTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AngularTolerance: STLImportBuilderAngularToleranceTypes = ...
    """
    Returns or sets  the angular tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``AngularTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.STLImportBuilderAngularToleranceTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``AngularTolerance`` 
    
    :param angularTolerance: 
    :type angularTolerance: :py:class:`NXOpen.Facet.STLImportBuilderAngularToleranceTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    """
    CleanUp: bool = ...
    """
    Returns or sets  the option to clean up all mesh defects on import 
    
    <hr>
    
    Getter Method
    
    Signature ``CleanUp`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``CleanUp`` 
    
    :param cleanUp: 
    :type cleanUp: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    """
    FacetBodyType: STLImportBuilderFacetBodyTypes = ...
    """
    Returns or sets  the facet body type 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodyType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.STLImportBuilderFacetBodyTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``FacetBodyType`` 
    
    :param facetBodyType: 
    :type facetBodyType: :py:class:`NXOpen.Facet.STLImportBuilderFacetBodyTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    """
    File: str = ...
    """
    Returns or sets  the STL file  
    
    <hr>
    
    Getter Method
    
    Signature ``File`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``File`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling")
    """
    HideSmoothEdges: bool = ...
    """
    Returns or sets  the indicator for whether to hide smooth edges 
    
    <hr>
    
    Getter Method
    
    Signature ``HideSmoothEdges`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``HideSmoothEdges`` 
    
    :param hideSmoothEdges: 
    :type hideSmoothEdges: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    """
    MinimumAngleFoldedFacets: float = ...
    """
    Returns or sets  the value for minimum angle between adjacent facets to define folded facets.  
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumAngleFoldedFacets`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumAngleFoldedFacets`` 
    
    :param minimumAngleFoldedFacets: 
    :type minimumAngleFoldedFacets: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    """
    MinimumFacetNumber: int = ...
    """
    Returns or sets  the value for minimum number of facets for a STL file to be imported 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumFacetNumber`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumFacetNumber`` 
    
    :param minimumFacetNumber: 
    :type minimumFacetNumber: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    """
    STLFileUnits: STLImportBuilderSTLFileUnitsTypes = ...
    """
    Returns or sets  the STL file units 
    
    <hr>
    
    Getter Method
    
    Signature ``STLFileUnits`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.STLImportBuilderSTLFileUnitsTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``STLFileUnits`` 
    
    :param stlFileUnits: 
    :type stlFileUnits: :py:class:`NXOpen.Facet.STLImportBuilderSTLFileUnitsTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    """
    ShowInformationWindow: bool = ...
    """
    Returns or sets  the indicator for whether to show information window 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowInformationWindow`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowInformationWindow`` 
    
    :param showInformationWindow: 
    :type showInformationWindow: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM")
    """
    Null: STLImportBuilder = ...  # unknown typename


class PaintFacetBodyBuilder(NXOpen.Builder):
    """
    This class manages the color painting on a facet body.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreatePaintFacetBodyBuilder`
    
    Default values.
    
    ==================================  ===========================================
    Property                            Value
    ==================================  ===========================================
    PaintBrushSize.Value (deprecated)   20.0 (millimeters part), 1.0 (inches part) 
    ==================================  ===========================================
    
    .. versionadded:: NX10.0.0
    """
    
    def GetPaintBrushColor(self) -> 'list[float]':
        """
        Returns the paint brush color  
        
        Signature ``GetPaintBrushColor()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPaintBrushColor(self, paintBrushColor: 'list[float]') -> None:
        """
        Sets the paint brush color 
        
        Signature ``SetPaintBrushColor(paintBrushColor)`` 
        
        :param paintBrushColor:  Array of 3 RGB values, each between 0 and 1  
        :type paintBrushColor: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetupBodyColorData(self, bodies: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Setup color data.  
        
        Inputs to this command can be convergent objects. 
        
        Signature ``SetupBodyColorData(bodies)`` 
        
        :param bodies:  Bodies that need color data for edit  
        :type bodies: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetupColorData(self, facets: 'list[FacetedBody]') -> None:
        """
        Setup color data 
        
        Signature ``SetupColorData(facets)`` 
        
        :param facets:  Facets that need color data for edit  
        :type facets: list of :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.Facet.PaintFacetBodyBuilder.SetupBodyColorData` instead.
        
        License requirements: None.
        """
        ...
    
    
    def PaintBodiesBackgroundColor(self, bodies: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Paints facets background color.  
        
        Inputs to this command can be convergent objects.
        
        Signature ``PaintBodiesBackgroundColor(bodies)`` 
        
        :param bodies:  Bodies to be painted with background color  
        :type bodies: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PaintFacetsBackGroundColor(self, facets: 'list[FacetedBody]') -> None:
        """
        Paints facets background color 
        
        Signature ``PaintFacetsBackGroundColor(facets)`` 
        
        :param facets:  Facets to be painted with background color  
        :type facets: list of :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.Facet.PaintFacetBodyBuilder.PaintBodiesBackgroundColor` instead.
        
        License requirements: None.
        """
        ...
    
    
    def PaintSelectedFacets(self) -> None:
        """
        Paints selected facets.  
        
        Signature ``PaintSelectedFacets()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    FacetCollector: NXOpen.FacetCollector = ...
    """
    Returns  a collector of facets on the facet bodies to be to be tested.  
    
    <hr>
    
    Getter Method
    
    Signature ``FacetCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    InheritBodyColorPick: NXOpen.SelectDisplayableObject = ...
    """
    Returns  the inherit color pick.  
    
    Inputs to this command can be convergent objects. 
    
    <hr>
    
    Getter Method
    
    Signature ``InheritBodyColorPick`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    InheritColorPick: SelectFacetedBody = ...
    """
    Returns  the inherit color pick 
    
    <hr>
    
    Getter Method
    
    Signature ``InheritColorPick`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBody` 
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX11.0.0
       Use :py:meth:`NXOpen.Facet.PaintFacetBodyBuilder.InheritBodyColorPick` instead.
    
    License requirements: None.
    """
    PaintBrush: PaintBrushBuilder = ...
    """
    Returns  the paint brush 
    
    <hr>
    
    Getter Method
    
    Signature ``PaintBrush`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.PaintBrushBuilder` 
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.Facet.PaintFacetBodyBuilder.FacetCollector`` instead.
    
    License requirements: None.
    """
    PaintBrushSize: NXOpen.Expression = ...
    """
    Returns  the paint brush size 
    
    <hr>
    
    Getter Method
    
    Signature ``PaintBrushSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.Facet.PaintFacetBodyBuilder.FacetCollector`` instead.
    
    License requirements: None.
    """
    Null: PaintFacetBodyBuilder = ...  # unknown typename


class ExtrudeFacetBodyBuilderLimitTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ExtrudeFacetBodyBuilderLimitType():
    """
    Represents the extrude limit type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Distance", "Specify the limit by direction and distance. Direction and Distance need to be specified."
       "ToPlane", "Specify the limit by plane object. Plane needes to be specified."
    """
    Distance = 0  # ExtrudeFacetBodyBuilderLimitTypeMemberType
    ToPlane = 1  # ExtrudeFacetBodyBuilderLimitTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ExtrudeFacetBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.ExtrudeFacetBodyBuilder`
    It extrudes a NX Facet Body.  
    
    The limit of extrusion can be specified by direction and distance
    or plane object. It returns the extruded NX Facet Body.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateExtrudeFacetBodyBuilder`
    
    Default values.
    
    ===============  =======================================
    Property         Value
    ===============  =======================================
    Distance.Value   10 (millimeters part), 1 (inches part) 
    ---------------  ---------------------------------------
    Offset.Value     0 (millimeters part), 0 (inches part) 
    ---------------  ---------------------------------------
    Type             Distance 
    ===============  =======================================
    
    .. versionadded:: NX9.0.0
    """
    
    class LimitType():
        """
        Represents the extrude limit type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Distance", "Specify the limit by direction and distance. Direction and Distance need to be specified."
           "ToPlane", "Specify the limit by plane object. Plane needes to be specified."
        """
        Distance = 0  # ExtrudeFacetBodyBuilderLimitTypeMemberType
        ToPlane = 1  # ExtrudeFacetBodyBuilderLimitTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Direction: NXOpen.Direction = ...
    """
    Returns or sets  the direction used when limit type is :py:class:`NXOpen.Facet.ExtrudeFacetBodyBuilderLimitType.Distance <NXOpen.Facet.ExtrudeFacetBodyBuilderLimitType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    """
    Distance: NXOpen.Expression = ...
    """
    Returns  the distance used when limit type is :py:class:`NXOpen.Facet.ExtrudeFacetBodyBuilderLimitType.Distance <NXOpen.Facet.ExtrudeFacetBodyBuilderLimitType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``Distance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance used in the extrude facet body feature 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX9.0.1
    
    License requirements: None.
    """
    FacetBody: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the facet/sheet bodies to be extruded 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Offset: NXOpen.Expression = ...
    """
    Returns  the offset value used to offset the extruded body 
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the plane used when limit type is :py:class:`NXOpen.Facet.ExtrudeFacetBodyBuilderLimitType.ToPlane <NXOpen.Facet.ExtrudeFacetBodyBuilderLimitType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    """
    Type: ExtrudeFacetBodyBuilderLimitType = ...
    """
    Returns or sets  the limit type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.ExtrudeFacetBodyBuilderLimitType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Facet.ExtrudeFacetBodyBuilderLimitType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    """
    Null: ExtrudeFacetBodyBuilder = ...  # unknown typename


class FacetBodyFromBodyBuilderOutputTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetBodyFromBodyBuilderOutputTypes():
    """
    These options represent the type of output body 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ConvergentBody", "Convert To Convergent bodies"
       "NXFacetBody", "Convert to NX Facet Bodies"
       "JTFacetBody", "Convert To JT Facet bodies"
    """
    ConvergentBody = 0  # FacetBodyFromBodyBuilderOutputTypesMemberType
    NXFacetBody = 1  # FacetBodyFromBodyBuilderOutputTypesMemberType
    JTFacetBody = 2  # FacetBodyFromBodyBuilderOutputTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetBodyFromBodyBuilderOriginalBodyOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetBodyFromBodyBuilderOriginalBodyOptions():
    """
    These options represent the options for handling original body: Keep, Hide, Delete  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Keep", "Keep original body"
       "Hide", "Hide original body"
       "Delete", "Delete original body"
    """
    Keep = 0  # FacetBodyFromBodyBuilderOriginalBodyOptionsMemberType
    Hide = 1  # FacetBodyFromBodyBuilderOriginalBodyOptionsMemberType
    Delete = 2  # FacetBodyFromBodyBuilderOriginalBodyOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetBodyFromBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.FacetBodyFromBodyBuilder` builder.  
    
    It converts the selected analytic bodies to NX convergent bodies bodies. 
    The original inputs are deleted.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateFacetBodyFromBodyBuilder`
    
    Default values.
    
    ===================  ============================================
    Property             Value
    ===================  ============================================
    Associative          False 
    -------------------  --------------------------------------------
    MaximumDeviation     0.1 (millimeters part), 0.005 (inches part) 
    -------------------  --------------------------------------------
    OriginalBodyOption   Hide 
    -------------------  --------------------------------------------
    OutputType           ConvergentBody 
    ===================  ============================================
    
    .. versionadded:: NX10.0.0
    """
    
    class OutputTypes():
        """
        These options represent the type of output body 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ConvergentBody", "Convert To Convergent bodies"
           "NXFacetBody", "Convert to NX Facet Bodies"
           "JTFacetBody", "Convert To JT Facet bodies"
        """
        ConvergentBody = 0  # FacetBodyFromBodyBuilderOutputTypesMemberType
        NXFacetBody = 1  # FacetBodyFromBodyBuilderOutputTypesMemberType
        JTFacetBody = 2  # FacetBodyFromBodyBuilderOutputTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OriginalBodyOptions():
        """
        These options represent the options for handling original body: Keep, Hide, Delete  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Keep", "Keep original body"
           "Hide", "Hide original body"
           "Delete", "Delete original body"
        """
        Keep = 0  # FacetBodyFromBodyBuilderOriginalBodyOptionsMemberType
        Hide = 1  # FacetBodyFromBodyBuilderOriginalBodyOptionsMemberType
        Delete = 2  # FacetBodyFromBodyBuilderOriginalBodyOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Associative: bool = ...
    """
    Returns or sets  the option that specifies whether the facet body from body operation is associative 
    
    <hr>
    
    Getter Method
    
    Signature ``Associative`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Associative`` 
    
    :param associative: 
    :type associative: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MaximumDeviation: float = ...
    """
    Returns or sets  the maximum deviation 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumDeviation`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumDeviation`` 
    
    :param maximumDeviation: 
    :type maximumDeviation: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    NonFacetedBodiesToConvert: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the input non-faceted bodies to convert 
    
    <hr>
    
    Getter Method
    
    Signature ``NonFacetedBodiesToConvert`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    OriginalBodyOption: FacetBodyFromBodyBuilderOriginalBodyOptions = ...
    """
    Returns or sets  the original body option of enum 
    
    <hr>
    
    Getter Method
    
    Signature ``OriginalBodyOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.FacetBodyFromBodyBuilderOriginalBodyOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OriginalBodyOption`` 
    
    :param enumOriginalBodyOption: 
    :type enumOriginalBodyOption: :py:class:`NXOpen.Facet.FacetBodyFromBodyBuilderOriginalBodyOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    OutputType: FacetBodyFromBodyBuilderOutputTypes = ...
    """
    Returns or sets  the output of the type of enum 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.FacetBodyFromBodyBuilderOutputTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputType`` 
    
    :param enumOutputType: 
    :type enumOutputType: :py:class:`NXOpen.Facet.FacetBodyFromBodyBuilderOutputTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: FacetBodyFromBodyBuilder = ...  # unknown typename


class SnipFacetBodyBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SnipFacetBodyBuilderTypes():
    """
    Snip method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SnipByBoundary", "Snip by boundary"
       "SnipByRegion", "Snip by region"
       "SnipWithCurves", "Snip with curves"
       "SnipAtPlane", "Snip at plane"
    """
    SnipByBoundary = 0  # SnipFacetBodyBuilderTypesMemberType
    SnipByRegion = 1  # SnipFacetBodyBuilderTypesMemberType
    SnipWithCurves = 2  # SnipFacetBodyBuilderTypesMemberType
    SnipAtPlane = 3  # SnipFacetBodyBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SnipFacetBodyBuilderDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SnipFacetBodyBuilderDirectionType():
    """
    Snipping direction when snipping type "by profiles"  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ViewDirection", "Snip along view direction"
       "FacetNormal", "Snip along facet normal"
       "AlongVector", "Snip along specified vector"
    """
    ViewDirection = 0  # SnipFacetBodyBuilderDirectionTypeMemberType
    FacetNormal = 1  # SnipFacetBodyBuilderDirectionTypeMemberType
    AlongVector = 2  # SnipFacetBodyBuilderDirectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SnipFacetBodyBuilderBoundaryFacetTreatmentMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SnipFacetBodyBuilderBoundaryFacetTreatmentMethod():
    """
    Boundary facet treatment type: 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SnipFacets", "Snip scarred facets by the border"
       "RemoveFacets", "Remove scarred facets"
    """
    SnipFacets = 0  # SnipFacetBodyBuilderBoundaryFacetTreatmentMethodMemberType
    RemoveFacets = 1  # SnipFacetBodyBuilderBoundaryFacetTreatmentMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SnipFacetBodyBuilder(NXOpen.Builder):
    """
    Represents a SnipFacetBody builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateSnipFacetBodyBuilder`
    
    Default values.
    
    ===========================  ==============
    Property                     Value
    ===========================  ==============
    AlongDirection               ViewDirection 
    ---------------------------  --------------
    BoundaryFacetTreatmentType   SnipFacets 
    ---------------------------  --------------
    CanDivide                    0 
    ---------------------------  --------------
    IsEditCopy                   0 
    ---------------------------  --------------
    IsSnipNearFacets             0 
    ===========================  ==============
    
    .. versionadded:: NX7.5.0
    """
    
    class Types():
        """
        Snip method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SnipByBoundary", "Snip by boundary"
           "SnipByRegion", "Snip by region"
           "SnipWithCurves", "Snip with curves"
           "SnipAtPlane", "Snip at plane"
        """
        SnipByBoundary = 0  # SnipFacetBodyBuilderTypesMemberType
        SnipByRegion = 1  # SnipFacetBodyBuilderTypesMemberType
        SnipWithCurves = 2  # SnipFacetBodyBuilderTypesMemberType
        SnipAtPlane = 3  # SnipFacetBodyBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DirectionType():
        """
        Snipping direction when snipping type "by profiles"  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ViewDirection", "Snip along view direction"
           "FacetNormal", "Snip along facet normal"
           "AlongVector", "Snip along specified vector"
        """
        ViewDirection = 0  # SnipFacetBodyBuilderDirectionTypeMemberType
        FacetNormal = 1  # SnipFacetBodyBuilderDirectionTypeMemberType
        AlongVector = 2  # SnipFacetBodyBuilderDirectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BoundaryFacetTreatmentMethod():
        """
        Boundary facet treatment type: 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SnipFacets", "Snip scarred facets by the border"
           "RemoveFacets", "Remove scarred facets"
        """
        SnipFacets = 0  # SnipFacetBodyBuilderBoundaryFacetTreatmentMethodMemberType
        RemoveFacets = 1  # SnipFacetBodyBuilderBoundaryFacetTreatmentMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SwitchRegion(self) -> None:
        """
        Switch the region to be snipped indicated by the region point.  
        
        Signature ``SwitchRegion()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    AlongDirection: SnipFacetBodyBuilderDirectionType = ...
    """
    Returns or sets  the direction in which snipping profiles are projected on the facet bodies  
    
    <hr>
    
    Getter Method
    
    Signature ``AlongDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SnipFacetBodyBuilderDirectionType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AlongDirection`` 
    
    :param alongDirection: 
    :type alongDirection: :py:class:`NXOpen.Facet.SnipFacetBodyBuilderDirectionType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Bodies: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the facet bodies to snip.  
    
    Inputs to this command can be convergent objects. 
    
    <hr>
    
    Getter Method
    
    Signature ``Bodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    BoundaryFacetTreatmentType: SnipFacetBodyBuilderBoundaryFacetTreatmentMethod = ...
    """
    Returns or sets  the boundary facet treatment type 
    
    <hr>
    
    Getter Method
    
    Signature ``BoundaryFacetTreatmentType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SnipFacetBodyBuilderBoundaryFacetTreatmentMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BoundaryFacetTreatmentType`` 
    
    :param boundaryFacetTreatmentType: 
    :type boundaryFacetTreatmentType: :py:class:`NXOpen.Facet.SnipFacetBodyBuilderBoundaryFacetTreatmentMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    CanDivide: bool = ...
    """
    Returns or sets  the value indicating if facet body is to be divided 
    
    <hr>
    
    Getter Method
    
    Signature ``CanDivide`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanDivide`` 
    
    :param canDivide: 
    :type canDivide: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    FacetBodies: SelectFacetedBodyList = ...
    """
    Returns  the facet bodies to snip 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBodyList` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX11.0.0
       Use :py:meth:`NXOpen.Facet.SnipFacetBodyBuilder.Bodies` instead.
    
    License requirements: None.
    """
    FacetCollector: NXOpen.FacetCollector = ...
    """
    Returns or sets  the collector of facets to be snipped.  
    
    <hr>
    
    Getter Method
    
    Signature ``FacetCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FacetCollector`` 
    
    :param collector: 
    :type collector: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsEditCopy: bool = ...
    """
    Returns or sets  the value indicating if a copy of the facet body to be snipped without altering the original 
    
    <hr>
    
    Getter Method
    
    Signature ``IsEditCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsEditCopy`` 
    
    :param isEditCopy: 
    :type isEditCopy: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsSnipNearFacets: bool = ...
    """
    Returns or sets  the value indicating if only facets near to the viewer to be snipped 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSnipNearFacets`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSnipNearFacets`` 
    
    :param isSnipNearFacets: 
    :type isSnipNearFacets: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the snipping plane 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    ProfileList: NXOpen.SectionList = ...
    """
    Returns  the list of snipping profiles 
    
    <hr>
    
    Getter Method
    
    Signature ``ProfileList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SectionList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ProjectionVector: NXOpen.Direction = ...
    """
    Returns or sets  the projection vector 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectionVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectionVector`` 
    
    :param projectionVector: 
    :type projectionVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    RegionList: NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList = ...
    """
    Returns  the list of regions to snip 
    
    <hr>
    
    Getter Method
    
    Signature ``RegionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    RegionPoint: NXOpen.SelectPointList = ...
    """
    Returns  the point indicating the portion of the facet body with respect to specified region to be snipped.  
    
    <hr>
    
    Getter Method
    
    Signature ``RegionPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectPointList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Type: SnipFacetBodyBuilderTypes = ...
    """
    Returns or sets  the snipping method accessor
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SnipFacetBodyBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Facet.SnipFacetBodyBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    ViewDirection: NXOpen.Vector3d = ...
    """
    Returns or sets  the view direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ViewDirection`` 
    
    :param viewDirection: 
    :type viewDirection: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: SnipFacetBodyBuilder = ...  # unknown typename


class FacetedEdgeFacetededgeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetedEdgeFacetededgeType():
    """
    Facet Edge type  
    
    .. versionadded:: NX8.5.1
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Undefined", " - "
       "Linear", "Linear edge"
       "Circular", "Circular edge"
       "Elliptical", "Elliptical edge"
       "Intersection", "Intersection edge"
       "Spline", "Spline edge"
    """
    Undefined = 0  # FacetedEdgeFacetededgeTypeMemberType
    Linear = 1  # FacetedEdgeFacetededgeTypeMemberType
    Circular = 2  # FacetedEdgeFacetededgeTypeMemberType
    Elliptical = 3  # FacetedEdgeFacetededgeTypeMemberType
    Intersection = 4  # FacetedEdgeFacetededgeTypeMemberType
    Spline = 5  # FacetedEdgeFacetededgeTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetedEdge(NXOpen.DisplayableObject, NXOpen.IBaseCurve):
    """
    Represents a faceted edge.  
    
    Instances of this class may be
    generated when recording a journal, but they cannot be created
    directly. 
    
    .. versionadded:: NX5.0.0
    """
    
    class FacetededgeType():
        """
        Facet Edge type  
        
        .. versionadded:: NX8.5.1
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Undefined", " - "
           "Linear", "Linear edge"
           "Circular", "Circular edge"
           "Elliptical", "Elliptical edge"
           "Intersection", "Intersection edge"
           "Spline", "Spline edge"
        """
        Undefined = 0  # FacetedEdgeFacetededgeTypeMemberType
        Linear = 1  # FacetedEdgeFacetededgeTypeMemberType
        Circular = 2  # FacetedEdgeFacetededgeTypeMemberType
        Elliptical = 3  # FacetedEdgeFacetededgeTypeMemberType
        Intersection = 4  # FacetedEdgeFacetededgeTypeMemberType
        Spline = 5  # FacetedEdgeFacetededgeTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetFaces(self) -> 'list[FacetedFace]':
        """
        Returns the faces connected to the edge  
        
        Signature ``GetFaces()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Facet.FacetedFace` 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def GetVertices(self) -> tuple:
        """
        Returns the vertices of the edge.  
        
        If the edge is closed, the second vertex is the same as the first. 
        
        Signature ``GetVertices()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (vertex1, vertex2). vertex1 is a :py:class:`NXOpen.Point3d`.   First vertex in the edge vertex2 is a :py:class:`NXOpen.Point3d`.   Second vertex in the edge 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def GetBody(self) -> FacetedBody:
        """
        Returns the body containing this edge  
        
        Signature ``GetBody()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def GetCurveData(self) -> tuple:
        """
        Returns the curve information for the facet edge
        
        Parameter description
        faceted_edge           : The input edge tag for which curve information is required.
        PNT3_p_t position      : Line: Position on Line 
        Circle/Ellipse: Center Point
        Spline/Intersection-Curve: Start Point of Curve.
        PNT3_p_t dir_or_end_pt : Line : Direction of the Line
        Circle: Normal to Plane Axis.
        Ellipse: Major Axis
        Spline/Intersection-Curve: End Point.
        PNT3_p_t x_axis         : Circle: Axis from Center to Start Point,
        Ellipse: Minor Axis
        Not valid for other types.
        
        double* radius         : Circle: Radius
        Ellipse: Major Radius
        Not valid for other types.
        
        double* minor_radius   : Ellipse: Minor Radius
        Not valid for other types.
        
        Signature ``GetCurveData()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (position, dirOrEndPt, xAxis, radius, minorRadius). position is a :py:class:`NXOpen.Point3d`. dirOrEndPt is a :py:class:`NXOpen.Point3d`. xAxis is a :py:class:`NXOpen.Point3d`. radius is a float. minorRadius is a float. 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def GetLength(self) -> float:
        """
        Returns the length of the object  
        
        Signature ``GetLength()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    EdgeType: FacetedEdgeFacetededgeType = ...
    """
    Returns  the type of the facet edge 
    
    <hr>
    
    Getter Method
    
    Signature ``EdgeType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.FacetedEdgeFacetededgeType` 
    
    .. versionadded:: NX8.5.1
    
    License requirements: None.
    """
    IsReference: bool = ...
    """
    Returns  the reference state of a curve 
    
    <hr>
    
    Getter Method
    
    Signature ``IsReference`` 
    
    :returns:  True - Reference; False - Not Reference  
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: FacetedEdge = ...  # unknown typename


class CombineFacetBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.CombineFacetBodyBuilder` builder.  
    
    It combines the facet bodies to one facet body. The original inputs are deleted.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateCombineFacetBodyBuilder`
    
    .. versionadded:: NX10.0.0
    """
    FacetedBodiesToCombine: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the faceted bodies to combine 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetedBodiesToCombine`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: CombineFacetBodyBuilder = ...  # unknown typename


class DivideFacetFaceBuilderDivideFacetTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DivideFacetFaceBuilderDivideFacetTypes():
    """
    Divide Facet Face type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ByRegion", "Divide Facet face based on selected regional facets"
       "ByColor", "Divide Facet face based on colored facets"
    """
    ByRegion = 0  # DivideFacetFaceBuilderDivideFacetTypesMemberType
    ByColor = 1  # DivideFacetFaceBuilderDivideFacetTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DivideFacetFaceBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.DivideFacetFaceBuilder`.  
    
    Divide Facet Face Builder is a function to facilitate dividing of selected facet out of original facet face. 
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateDivideFacetFaceBuilder`
    
    Default values.
    
    ===========  =====
    Property     Value
    ===========  =====
    Degree       3 
    -----------  -----
    IsEditCopy   0 
    -----------  -----
    Segments     50 
    ===========  =====
    
    .. versionadded:: NX12.0.0
    """
    
    class DivideFacetTypes():
        """
        Divide Facet Face type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ByRegion", "Divide Facet face based on selected regional facets"
           "ByColor", "Divide Facet face based on colored facets"
        """
        ByRegion = 0  # DivideFacetFaceBuilderDivideFacetTypesMemberType
        ByColor = 1  # DivideFacetFaceBuilderDivideFacetTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Degree: int = ...
    """
    Returns or sets  the polynomial degree (one unit less than the order).  
    
    <hr>
    
    Getter Method
    
    Signature ``Degree`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Degree`` 
    
    :param degree: 
    :type degree: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    FacetBodyCollector: NXOpen.ScCollector = ...
    """
    Returns  the collector for specifying facet bodies to be divided based on colored regions.  
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodyCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FacetCollector: NXOpen.FacetCollector = ...
    """
    Returns  the collector for specifying facet regions
    
    <hr>
    
    Getter Method
    
    Signature ``FacetCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IsEditCopy: bool = ...
    """
    Returns or sets  the value indicating if a copy of the facet body to be used for Divide facet face without altering the original 
    
    <hr>
    
    Getter Method
    
    Signature ``IsEditCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsEditCopy`` 
    
    :param isEditCopy: 
    :type isEditCopy: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    Segments: int = ...
    """
    Returns or sets the number of segments used for advanced fitting
    
    <hr>
    
    Getter Method
    
    Signature ``Segments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Segments`` 
    
    :param segments: 
    :type segments: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    Type: DivideFacetFaceBuilderDivideFacetTypes = ...
    """
    Returns or sets  the type of enum which decides method for dividing facet faces
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.DivideFacetFaceBuilderDivideFacetTypes` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Facet.DivideFacetFaceBuilderDivideFacetTypes` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    Null: DivideFacetFaceBuilder = ...  # unknown typename


class FacetingParameters():
    """
    The structure of JA faceting parameters .  
    
    Constructor: 
    NXOpen.Facet.FacetingParameters()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    MaximumFacetEdges: int = ...
    """
    The maximum number of edges allowed
    in the facets that are to be generated 
    (this does not apply to JT).  
    
    <hr>
    
    Field Value
    Type:int
    """
    SpecifySurfaceTolerance: bool = ...
    """
    If this value is true, then
    values must be specified for
    surfaceDistanceTolerance
    and surfaceAngularTolerance.  
    
    If
    this value is false then values for
    surfaceDistanceTolerance and
    surfaceAngularTolerance will be
    determined by the system based on the
    body box or face box of the solid entity
    being faceted.
    
    <hr>
    
    Field Value
    Type:bool
    """
    SurfaceDistanceTolerance: float = ...
    """
    This is the maximum distance from
    the surface to the facet.  
    
    <hr>
    
    Field Value
    Type:float
    """
    SurfaceAngularTolerance: float = ...
    """
    This is the maximum angular variation
    in radians of the surface normal
    over the facet.  
    
    A value of zero
    indicates no constraint.
    
    <hr>
    
    Field Value
    Type:float
    """
    SpecifyCurveTolerance: bool = ...
    """
    This indicates that values are to be
    specified for curveDistanceTolerance
    and curveAngularTolerance and
    curve_max_length.  
    
    If this value is false
    then values for curveDistanceTolerance
    and curveAngularTolerance will be
    determined by the system based on the
    body box or face box of the solid
    entity being faceted, and no restriction
    will be placed on the maximum length
    of curve that can be represented
    by a single facet edge.
    
    <hr>
    
    Field Value
    Type:bool
    """
    CurveDistanceTolerance: float = ...
    """
    This is the maximum distance between
    the facet edge and the curve segment
    represented by the facet edge.  
    
    This
    applies only to those facet edges lying
    along solid edges.
    
    <hr>
    
    Field Value
    Type:float
    """
    CurveAngularTolerance: float = ...
    """
    This is the maximum angular variation
    in radians of the curve tangent along
    the curve segment represented by the
    facet edge.  
    
    This applies only to those
    facet edges lying along solid edges.
    A value of zero indicates no constraint.
    
    <hr>
    
    Field Value
    Type:float
    """
    CurveMaximumLength: float = ...
    """
    The maximum length of a curve, default is 1000.  
    
    0 
    <hr>
    
    Field Value
    Type:float
    """
    SpecifyConvexFacets: bool = ...
    """
    This indicates that the facets
    generated by the faceter should all be
    convex (this does not apply to JT).  
    
    <hr>
    
    Field Value
    Type:bool
    """
    SpecifyMaximumFacetSize: bool = ...
    """
    This indicates that a maximum width of
    facet is to be specified using
    maximumFacetSize.  
    
    If this field is false
    then no maximum facet size is imposed.
    
    <hr>
    
    Field Value
    Type:bool
    """
    MaximumFacetSize: float = ...
    """
    This is the maximum width of a facet.  
    
    This is only used if
    specifyMaximumFacetSize is true.
    
    <hr>
    
    Field Value
    Type:float
    """
    SpecifyParameters: bool = ...
    """
    This indicates that the model will be
    created with the parametric information
    for each vertex.  
    
    Should parameters at
    the vertices be obtained for the facets
    of the model (this does not apply to JT).
    
    <hr>
    
    Field Value
    Type:bool
    """
    NumberStorageType: int = ...
    """
    This indicates whether the real
    numbers for facet vertices and facet
    normals should be stored as floats
    (UF_FACET_TYPE_FLOAT) or as doubles
    (UF_FACET_TYPE_DOUBLE).  
    
    Note that this
    option applies only when a faceted model
    is being created, and is ignored when the
    model is updated. This option is not applicable
    to JT creation or update.
    
    <hr>
    
    Field Value
    Type:int
    """
    SpecifyViewDirection: bool = ...
    """
    Should we use a viewing direction
    for denser faceting around
    silhouettes.  
    
    The denser faceting will
    honor the tolerance specified by
    silhouetteChordTolerance in the silhouette
    with respect to the view direction
    specified by silhouetteViewDirection vector.
    If this is false, there is no special
    consideration for any silhouette area
    (this does not apply to JT).
    
    <hr>
    
    Field Value
    Type:bool
    """
    SilhouetteViewDirection: NXOpen.Vector3d = ...
    """
    If specifyViewDirection is specified,
    then this is the view direction to use
    (this does not apply to JT).  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    SilhouetteChordTolerance: float = ...
    """
    If specifyViewDirection is specified
    then this is the tolerance which will be
    used as a tighter surface tolerance
    in the silhouette area specified
    by the view direction (this does not apply to JT).  
    
    <hr>
    
    Field Value
    Type:float
    """
    StoreFaceTag: bool = ...
    """
    Should this FACET body record face tags or not 
    (this does not apply to JT).  
    
    <hr>
    
    Field Value
    Type:bool
    """
    WithLODS: bool = ...
    """
    When creating a JT facet body whether to create LODs or not 
    (this does not apply to NX).  
    
    <hr>
    
    Field Value
    Type:bool
    """


class ConvertFacetBodyBuilderOutputTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConvertFacetBodyBuilderOutputTypes():
    """
    These options represent the type of output facet body 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ConvergentBody", "Convert To Convergent bodies"
       "NXFacetBody", "Convert to NX Facet bodies"
       "JTFacetBody", "Convert To JT Facet bodies"
    """
    ConvergentBody = 0  # ConvertFacetBodyBuilderOutputTypesMemberType
    NXFacetBody = 1  # ConvertFacetBodyBuilderOutputTypesMemberType
    JTFacetBody = 2  # ConvertFacetBodyBuilderOutputTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ConvertFacetBodyBuilderOriginalBodyOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConvertFacetBodyBuilderOriginalBodyOptions():
    """
    These represent the options for handling the input facet bodies  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Keep", "Keep original body"
       "Hide", "Hide original body"
       "Delete", "Delete original body"
    """
    Keep = 0  # ConvertFacetBodyBuilderOriginalBodyOptionsMemberType
    Hide = 1  # ConvertFacetBodyBuilderOriginalBodyOptionsMemberType
    Delete = 2  # ConvertFacetBodyBuilderOriginalBodyOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ConvertFacetBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.ConvertFacetBodyBuilder` builder.  
    
    It converts the selected NX facet bodies to Convergent bodies or JT bodies, and converts JT facet bodies 
    to Convergent bodies or NX facets bodies. The original inputs can be deleted, kept, or hidden.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateConvertFacetBodyBuilder`
    
    Default values.
    
    =========================  ===============
    Property                   Value
    =========================  ===============
    MinimumAngleFoldedFacets   15.0 
    -------------------------  ---------------
    OriginalBodyOption         Delete 
    -------------------------  ---------------
    OutputType                 ConvergentBody 
    =========================  ===============
    
    .. versionadded:: NX10.0.0
    """
    
    class OutputTypes():
        """
        These options represent the type of output facet body 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ConvergentBody", "Convert To Convergent bodies"
           "NXFacetBody", "Convert to NX Facet bodies"
           "JTFacetBody", "Convert To JT Facet bodies"
        """
        ConvergentBody = 0  # ConvertFacetBodyBuilderOutputTypesMemberType
        NXFacetBody = 1  # ConvertFacetBodyBuilderOutputTypesMemberType
        JTFacetBody = 2  # ConvertFacetBodyBuilderOutputTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OriginalBodyOptions():
        """
        These represent the options for handling the input facet bodies  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Keep", "Keep original body"
           "Hide", "Hide original body"
           "Delete", "Delete original body"
        """
        Keep = 0  # ConvertFacetBodyBuilderOriginalBodyOptionsMemberType
        Hide = 1  # ConvertFacetBodyBuilderOriginalBodyOptionsMemberType
        Delete = 2  # ConvertFacetBodyBuilderOriginalBodyOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    CleanUp: bool = ...
    """
    Returns or sets  an option for automatically repairing the converted PSM mesh 
    
    <hr>
    
    Getter Method
    
    Signature ``CleanUp`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CleanUp`` 
    
    :param cleanUp: 
    :type cleanUp: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    FacetedBodiesToConvert: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the input facet bodies to convert 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetedBodiesToConvert`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    MinimumAngleFoldedFacets: float = ...
    """
    Returns or sets  the minimum angle between adjacent facets to define folded facets.  
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumAngleFoldedFacets`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumAngleFoldedFacets`` 
    
    :param minimumAngleFoldedFacets: 
    :type minimumAngleFoldedFacets: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    OriginalBodyOption: ConvertFacetBodyBuilderOriginalBodyOptions = ...
    """
    Returns or sets  the option for handling the input facet bodies 
    
    <hr>
    
    Getter Method
    
    Signature ``OriginalBodyOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.ConvertFacetBodyBuilderOriginalBodyOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OriginalBodyOption`` 
    
    :param enumOriginalBodyOption: 
    :type enumOriginalBodyOption: :py:class:`NXOpen.Facet.ConvertFacetBodyBuilderOriginalBodyOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    OutputType: ConvertFacetBodyBuilderOutputTypes = ...
    """
    Returns or sets  the output type of converted facet body 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.ConvertFacetBodyBuilderOutputTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputType`` 
    
    :param enumOutputType: 
    :type enumOutputType: :py:class:`NXOpen.Facet.ConvertFacetBodyBuilderOutputTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: ConvertFacetBodyBuilder = ...  # unknown typename


class FacetModelingCollection():
    """
    Collection of freeform facet operations.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Facet.FacetedBodyCollection`
    
    .. versionadded:: NX10.0.0
    """
    
    def CreateConvertFacetBodyBuilder(self) -> ConvertFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.ConvertFacetBodyBuilder`  
        
        Signature ``CreateConvertFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.ConvertFacetBodyBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def CreateCleanupFacetBodyBuilder(self) -> CleanupFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.CleanupFacetBodyBuilder`  
        
        Signature ``CreateCleanupFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def CreateCombineFacetBodyBuilder(self) -> CombineFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.CombineFacetBodyBuilder`  
        
        Signature ``CreateCombineFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.CombineFacetBodyBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def CreateFacetBodyFromBodyBuilder(self) -> FacetBodyFromBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.FacetBodyFromBodyBuilder`  
        
        Signature ``CreateFacetBodyFromBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.FacetBodyFromBodyBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def CreateDetectPrimitivesBuilder(self) -> DetectPrimitivesBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.DetectPrimitivesBuilder` object.  
        
        Signature ``CreateDetectPrimitivesBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.DetectPrimitivesBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreatePaintFacetBodyBuilder(self) -> PaintFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.PaintFacetBodyBuilder` object.  
        
        Signature ``CreatePaintFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.PaintFacetBodyBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreatePaintBrushBuilder(self) -> PaintBrushBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.PaintBrushBuilder` object.  
        
        Signature ``CreatePaintBrushBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.PaintBrushBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateRemoveUndercutsBuilder(self) -> RemoveUndercutsBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.RemoveUndercutsBuilder` object  
        
        Signature ``CreateRemoveUndercutsBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.RemoveUndercutsBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_polygon_modeling (" NX Polygon Modeling")
        """
        ...
    
    
    def CreateCreateTransitionBuilder(self) -> CreateTransitionBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.CreateTransitionBuilder` object  
        
        Signature ``CreateCreateTransitionBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.CreateTransitionBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_polygon_modeling (" NX Polygon Modeling")
        """
        ...
    
    
    def CreateLocalOffsetBuilder(self) -> LocalOffsetBuilder:
        """
        Creates a :py:class:`Facet.LocalOffsetBuilder`  
        
        Signature ``CreateLocalOffsetBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.LocalOffsetBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_polygon_modeling (" NX Polygon Modeling")
        """
        ...
    
    
    def CreateMergeFacetFacesBuilder(self) -> MergeFacetFacesBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.MergeFacetFacesBuilder`  
        
        Signature ``CreateMergeFacetFacesBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.MergeFacetFacesBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_polygon_modeling (" NX Polygon Modeling")
        """
        ...
    
    
    def CreateFacetAdjustMinimumRadiusBuilder(self) -> AdjustMinimumRadiusBuilder:
        """
        Create a :py:class:`NXOpen.Facet.AdjustMinimumRadiusBuilder` object.  
        
        Signature ``CreateFacetAdjustMinimumRadiusBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.AdjustMinimumRadiusBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDivideFacetFaceBuilder(self) -> DivideFacetFaceBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.DivideFacetFaceBuilder`  
        
        Signature ``CreateDivideFacetFaceBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.DivideFacetFaceBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_polygon_modeling (" NX Polygon Modeling")
        """
        ...
    
    
    def CreatePolygonModelingBuilder(self) -> PolygonModelingBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.PolygonModelingBuilder`  
        
        Signature ``CreatePolygonModelingBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.PolygonModelingBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_polygon_modeling (" NX Polygon Modeling")
        """
        ...
    


class MergeFacetBodyBuilderInputMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MergeFacetBodyBuilderInput():
    """
    Represents the option for keeping, deleting or hiding input two facet bodies after builder committing 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Keep", "Keep the input facet body after builder committing"
       "Delete", "Delete the input facet body after builder committing"
       "Hide", "Hide the input facet body after builder committing"
    """
    Keep = 0  # MergeFacetBodyBuilderInputMemberType
    Delete = 1  # MergeFacetBodyBuilderInputMemberType
    Hide = 2  # MergeFacetBodyBuilderInputMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MergeFacetBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.MergeFacetBodyBuilder`
    It merges two overlapping NX facet bodies.  
    
    It returns a new mergered NX facet body. The two input bodies
    can be kept, deleted or hidden.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateMergeFacetBodyBuilder`
    
    Default values.
    
    ==================  =============================================
    Property            Value
    ==================  =============================================
    ChordHeight.Value   0.05 (millimeters part), 0.005 (inches part) 
    ------------------  ---------------------------------------------
    EdgeLength.Value    1 (millimeters part), 0.1 (inches part) 
    ------------------  ---------------------------------------------
    InputStatus         Keep 
    ==================  =============================================
    
    .. versionadded:: NX9.0.0
    """
    
    class Input():
        """
        Represents the option for keeping, deleting or hiding input two facet bodies after builder committing 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Keep", "Keep the input facet body after builder committing"
           "Delete", "Delete the input facet body after builder committing"
           "Hide", "Hide the input facet body after builder committing"
        """
        Keep = 0  # MergeFacetBodyBuilderInputMemberType
        Delete = 1  # MergeFacetBodyBuilderInputMemberType
        Hide = 2  # MergeFacetBodyBuilderInputMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AngleTolerance: float = ...
    """
    Returns or sets  the angle tolerance used in the merge facet body feature 
    
    <hr>
    
    Getter Method
    
    Signature ``AngleTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AngleTolerance`` 
    
    :param angleTolerance: 
    :type angleTolerance: float 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    """
    ChordHeight: NXOpen.Expression = ...
    """
    Returns  the chord height to control the size of new facets 
    
    <hr>
    
    Getter Method
    
    Signature ``ChordHeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance used in the merge facet body feature 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    """
    EdgeLength: NXOpen.Expression = ...
    """
    Returns  the edge length to control the size of new facets 
    
    <hr>
    
    Getter Method
    
    Signature ``EdgeLength`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FacetBodyOne: SelectFacetedBody = ...
    """
    Returns  the first NX facet body to be merged 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodyOne`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBody` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FacetBodyTwo: SelectFacetedBody = ...
    """
    Returns  the second NX facet body to be merged 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodyTwo`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBody` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    InputStatus: MergeFacetBodyBuilderInput = ...
    """
    Returns or sets  the option to specify how to deal with the input two facet bodies: keep, delete or hide 
    
    <hr>
    
    Getter Method
    
    Signature ``InputStatus`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.MergeFacetBodyBuilderInput` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputStatus`` 
    
    :param inputStatus: 
    :type inputStatus: :py:class:`NXOpen.Facet.MergeFacetBodyBuilderInput` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    """
    Null: MergeFacetBodyBuilder = ...  # unknown typename


class FeatureExtractionBuilderInputActionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FeatureExtractionBuilderInputActions():
    """
    Specifies how to handle the input facet bodies. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Blank", "Blank the input facet bodies"
       "Retain", "Retain the input facet bodies"
       "Delete", "Delete the input facet bodies"
    """
    Blank = 0  # FeatureExtractionBuilderInputActionsMemberType
    Retain = 1  # FeatureExtractionBuilderInputActionsMemberType
    Delete = 2  # FeatureExtractionBuilderInputActionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FeatureExtractionBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.FeatureExtractionBuilder`
    It extracts feature lines or separates regions of different curvature
    from a facet body based on the curvature map.  
    
    For facet body curvature, please see :py:class:`NXOpen.Facet.CurvatureBuilder`.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateFacetFeatureExtractionBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class InputActions():
        """
        Specifies how to handle the input facet bodies. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Blank", "Blank the input facet bodies"
           "Retain", "Retain the input facet bodies"
           "Delete", "Delete the input facet bodies"
        """
        Blank = 0  # FeatureExtractionBuilderInputActionsMemberType
        Retain = 1  # FeatureExtractionBuilderInputActionsMemberType
        Delete = 2  # FeatureExtractionBuilderInputActionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetExtractedRegions(self) -> 'list[FacetedBody]':
        """
        Gets the extracted facet bodies.  
        
        Call :py:meth:`Builder.Commit` before calling this method.  
        
        Signature ``GetExtractedRegions()`` 
        
        :returns:  The extracted facet bodies  
        :rtype: list of :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def GetExtractedBorders(self) -> 'list[NXOpen.Spline]':
        """
        Gets the extracted curves.  
        
        Call :py:meth:`Builder.Commit` before calling this method.  
        
        Signature ``GetExtractedBorders()`` 
        
        :returns:  The extracted curves 
        :rtype: list of :py:class:`NXOpen.Spline` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    AreBordersEnabled: bool = ...
    """
    Returns or sets  the extracting borders option 
    
    <hr>
    
    Getter Method
    
    Signature ``AreBordersEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AreBordersEnabled`` 
    
    :param bordersEnabled: 
    :type bordersEnabled: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    AreRegionsEnabled: bool = ...
    """
    Returns or sets   the extracting regions option 
    
    <hr>
    
    Getter Method
    
    Signature ``AreRegionsEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AreRegionsEnabled`` 
    
    :param regionsEnabled: 
    :type regionsEnabled: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    FacetBodies: SelectFacetedBodyList = ...
    """
    Returns  the input facet body selection list 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBodyList` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    InputAction: FeatureExtractionBuilderInputActions = ...
    """
    Returns or sets  the input facet body action 
    
    <hr>
    
    Getter Method
    
    Signature ``InputAction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.FeatureExtractionBuilderInputActions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputAction`` 
    
    :param inputAction: 
    :type inputAction: :py:class:`NXOpen.Facet.FeatureExtractionBuilderInputActions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsSmoothingEnabled: bool = ...
    """
    Returns or sets  the smoothing option 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSmoothingEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSmoothingEnabled`` 
    
    :param smoothingEanbled: 
    :type smoothingEanbled: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MinimumBorderLength: float = ...
    """
    Returns or sets  the minimum border length 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumBorderLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumBorderLength`` 
    
    :param minimumBorderLength: 
    :type minimumBorderLength: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    SmoothingFactor: float = ...
    """
    Returns or sets  the smoothing factor 
    
    <hr>
    
    Getter Method
    
    Signature ``SmoothingFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SmoothingFactor`` 
    
    :param smoothingFactor: 
    :type smoothingFactor: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: FeatureExtractionBuilder = ...  # unknown typename


class SelectFacetedBody(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a single object selection.  
    
    .. versionadded:: NX5.0.0
    """
    
    @typing.overload
    def SetValue(self) -> None:
        """Returns or sets  the object being selected"""
        ...
    
    @typing.overload
    def SetValue(self, selection: FacetedBody) -> None:
        """
        Getter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: FacetedBody) -> None:
        """
        Setter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: FacetedBody, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
        The object being selected with the object's view and object's point
        
        Signature ``SetValue(selection, view, point)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Facet.FacetedBody` 
        :param view:  selected object view 
        :type view: :py:class:`NXOpen.View` 
        :param point:  selected object point 
        :type point: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, snapType: NXOpen.InferSnapTypeSnapType, selection1: FacetedBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: FacetedBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
        The object being selected with the objects view and objects point and snap information.
        
        Signature ``SetValue(snapType, selection1, view1, point1, selection2, view2, point2)`` 
        
        :param snapType:   snap point type 
        :type snapType: :py:class:`NXOpen.InferSnapTypeSnapType` 
        :param selection1:  first selected object  
        :type selection1: :py:class:`NXOpen.Facet.FacetedBody` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1:  first selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Facet.FacetedBody` 
        :param view2:  second selected object view 
        :type view2: :py:class:`NXOpen.View` 
        :param point2:  second selected object point 
        :type point2: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: FacetedBody, caeSubType: NXOpen.CaeObjectTypeCaeSubType, caeSubId: int) -> None:
        """
        The object being selected with CAE set object information.
        
        Signature ``SetValue(selection, caeSubType, caeSubId)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Facet.FacetedBody` 
        :param caeSubType:  CAE set object sub type 
        :type caeSubType: :py:class:`NXOpen.CaeObjectTypeCaeSubType` 
        :param caeSubId:  CAE set object sub id 
        :type caeSubId: int 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObject.SetValue`.
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetValue(self) -> None:
        """Returns or sets  the object being selected"""
        ...
    
    @typing.overload
    def GetValue(self) -> FacetedBody:
        """
        Getter Method
        
        Signature ``Value`` 
        
        :returns:  selected object  
        :rtype: :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self, selection: FacetedBody) -> None:
        """
        Setter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with the object's view and point.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (selection, view, point). selection is a :py:class:`NXOpen.Facet.FacetedBody`.   selected object view is a :py:class:`NXOpen.View`.   selected object viewpoint is a :py:class:`NXOpen.Point3d`.   selected object point
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with the objects view and point and snap information.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (snapType, selection1, view1, point1, selection2, view2, point2). snapType is a :py:class:`NXOpen.InferSnapTypeSnapType`.    snap point typeselection1 is a :py:class:`NXOpen.Facet.FacetedBody`.   first selected object view1 is a :py:class:`NXOpen.View`.   first selected object viewpoint1 is a :py:class:`NXOpen.Point3d`.   first selected object pointselection2 is a :py:class:`NXOpen.Facet.FacetedBody`.   second selected object view2 is a :py:class:`NXOpen.View`.   second selected object viewpoint2 is a :py:class:`NXOpen.Point3d`.   second selected object point
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with CAE set object information.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (selection, caeSubType, caeSubId). selection is a :py:class:`NXOpen.Facet.FacetedBody`.   selected object caeSubType is a :py:class:`NXOpen.CaeObjectTypeCaeSubType`.   CAE set object sub typecaeSubId is a int.   CAE set object sub id
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObject.GetValue`.
        
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
    
    Value: FacetedBody = ...
    """
    Returns or sets  the object being selected
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns:  selected object  
    :rtype: :py:class:`NXOpen.Facet.FacetedBody` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param selection:  selected object  
    :type selection: :py:class:`NXOpen.Facet.FacetedBody` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: SelectFacetedBody = ...  # unknown typename


class ExtrudeProfileBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.ExtrudeProfileBuilder`
    It extrudes 3D closed profile between planes.  
    
    The two planes are defined 
    by direction and distance. It returns the extruded NX Facet Body.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateExtrudeProfileBuilder`
    
    Default values.
    
    =====================  =============================================
    Property               Value
    =====================  =============================================
    FirstDistance.Value    0 (millimeters part), 0 (inches part) 
    ---------------------  ---------------------------------------------
    Offset.Value           0 (millimeters part), 0 (inches part) 
    ---------------------  ---------------------------------------------
    SecondDistance.Value   0 (millimeters part), 0 (inches part) 
    ---------------------  ---------------------------------------------
    Tolerance.Value        0.01 (millimeters part), 0.001 (inches part) 
    =====================  =============================================
    
    .. versionadded:: NX9.0.0
    """
    Direction: NXOpen.Direction = ...
    """
    Returns or sets  the extrude direction 
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    """
    FirstDistance: NXOpen.Expression = ...
    """
    Returns  the first distance to extrude 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Offset: NXOpen.Expression = ...
    """
    Returns  the offset used to offset the extruded body 
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Profile: NXOpen.Section = ...
    """
    Returns  the 3D profile to be extruded 
    
    <hr>
    
    Getter Method
    
    Signature ``Profile`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    SecondDistance: NXOpen.Expression = ...
    """
    Returns  the second distance to extrude 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Tolerance: NXOpen.Expression = ...
    """
    Returns  the tolerance used to create the polyline 
    
    <hr>
    
    Getter Method
    
    Signature ``Tolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: ExtrudeProfileBuilder = ...  # unknown typename


class DetectPrimitivesBuilder(NXOpen.Builder):
    """
    This class manages the primitive shape detection for a facet body.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateDetectPrimitivesBuilder`
    
    Default values.
    
    =====================  =====
    Property               Value
    =====================  =====
    CurvatureSensitivity   20 
    =====================  =====
    
    .. versionadded:: NX10.0.0
    """
    
    def GetPlaneColor(self) -> 'list[float]':
        """
        Returns the plane color  
        
        Signature ``GetPlaneColor()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPlaneColor(self, planeColor: 'list[float]') -> None:
        """
        Sets the plane color 
        
        Signature ``SetPlaneColor(planeColor)`` 
        
        :param planeColor:  Array of 3 RGB values, each between 0 and 1  
        :type planeColor: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSphereColor(self) -> 'list[float]':
        """
        Returns the sphere color  
        
        Signature ``GetSphereColor()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSphereColor(self, sphereColor: 'list[float]') -> None:
        """
        Sets the sphere color 
        
        Signature ``SetSphereColor(sphereColor)`` 
        
        :param sphereColor:  Array of 3 RGB values, each between 0 and 1  
        :type sphereColor: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCylinderColor(self) -> 'list[float]':
        """
        Returns the cylinder color  
        
        Signature ``GetCylinderColor()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCylinderColor(self, cylinderColor: 'list[float]') -> None:
        """
        Sets the cylinder color 
        
        Signature ``SetCylinderColor(cylinderColor)`` 
        
        :param cylinderColor:  Array of 3 RGB values, each between 0 and 1  
        :type cylinderColor: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetConeColor(self) -> 'list[float]':
        """
        Returns the cone color  
        
        Signature ``GetConeColor()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetConeColor(self, coneColor: 'list[float]') -> None:
        """
        Sets the cone color 
        
        Signature ``SetConeColor(coneColor)`` 
        
        :param coneColor:  Array of 3 RGB values, each between 0 and 1  
        :type coneColor: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBlendColor(self) -> 'list[float]':
        """
        Returns the blend color  
        
        Signature ``GetBlendColor()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBlendColor(self, blendColor: 'list[float]') -> None:
        """
        Sets the blend color 
        
        Signature ``SetBlendColor(blendColor)`` 
        
        :param blendColor:  Array of 3 RGB values, each between 0 and 1  
        :type blendColor: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOtherColor(self) -> 'list[float]':
        """
        Returns Other type of color.  
        
        All non-primitive shapes are classfied as Other type  
        
        Signature ``GetOtherColor()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOtherColor(self, otherColor: 'list[float]') -> None:
        """
        Sets the other color 
        
        Signature ``SetOtherColor(otherColor)`` 
        
        :param otherColor:  Array of 3 RGB values, each between 0 and 1  
        :type otherColor: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AdjustShapeBoundary(self) -> None:
        """
        Adjust shape detection result with selectivity angle 
        
        Signature ``AdjustShapeBoundary()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    BlendFactor: NXOpen.Expression = ...
    """
    Returns  the blend factor 
    
    <hr>
    
    Getter Method
    
    Signature ``BlendFactor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    CurvatureSensitivity: int = ...
    """
    Returns or sets  the curvature sensitivity 
    
    <hr>
    
    Getter Method
    
    Signature ``CurvatureSensitivity`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurvatureSensitivity`` 
    
    :param curvatureSensitivity: 
    :type curvatureSensitivity: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    FacetSelection: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the facet selection.  
    
    Inputs to this command can be convergent objects.
    
    <hr>
    
    Getter Method
    
    Signature ``FacetSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: DetectPrimitivesBuilder = ...  # unknown typename


class FacetedBodyCollectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FacetedBodyCollectionType():
    """
    Specifies the type of facets created when copying or converting faceted bodies 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Nx", "NX facet"
       "Jt", "JT facet"
    """
    Nx = 0  # FacetedBodyCollectionTypeMemberType
    Jt = 1  # FacetedBodyCollectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FacetedBodyCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of faceted bodies in a part   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX5.0.0
    """
    
    class Type():
        """
        Specifies the type of facets created when copying or converting faceted bodies 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Nx", "NX facet"
           "Jt", "JT facet"
        """
        Nx = 0  # FacetedBodyCollectionTypeMemberType
        Jt = 1  # FacetedBodyCollectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    
    def FindObject(self, journalIdentifier: str) -> FacetedBody:
        """
        Finds the :py:class:`NXOpen.Facet.FacetedBody` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier of the faceted body you want  
        :type journalIdentifier: str 
        :returns:  Faceted body with this identifier  
        :rtype: :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateFacetCurvatureBuilder(self) -> CurvatureBuilder:
        """
        Create a :py:class:`NXOpen.Facet.CurvatureBuilder` object.  
        
        Signature ``CreateFacetCurvatureBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.CurvatureBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateFacetFeatureExtractionBuilder(self) -> FeatureExtractionBuilder:
        """
        Create a :py:class:`NXOpen.Facet.FeatureExtractionBuilder` object.  
        
        Signature ``CreateFacetFeatureExtractionBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.FeatureExtractionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def Convert(self, fromBody: FacetedBody, toFacetType: FacetedBodyCollectionType) -> None:
        """
        Converts the internal representation of this faceted body to the specified type.  
        
        This does not create a new body 
        
        Signature ``Convert(fromBody, toFacetType)`` 
        
        :param fromBody:  The faceted body to convert  
        :type fromBody: :py:class:`NXOpen.Facet.FacetedBody` 
        :param toFacetType:  To facet type  
        :type toFacetType: :py:class:`NXOpen.Facet.FacetedBodyCollectionType` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Copy(self, fromBody: FacetedBody, toPart: NXOpen.Part, toFacetType: FacetedBodyCollectionType) -> FacetedBody:
        """
        Copies a faceted body and optionally changes the internal representation to the given type
        (This is only valid for JT to NX copy) 
        
        Signature ``Copy(fromBody, toPart, toFacetType)`` 
        
        :param fromBody:  The faceted body to copy  
        :type fromBody: :py:class:`NXOpen.Facet.FacetedBody` 
        :param toPart:  Part to create the copy in  
        :type toPart: :py:class:`NXOpen.Part` 
        :param toFacetType:  To facet type  
        :type toFacetType: :py:class:`NXOpen.Facet.FacetedBodyCollectionType` 
        :returns:  New body  
        :rtype: :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAssociatedFacetedBodies(self, solidBody: NXOpen.Body) -> tuple:
        """
        Returns the loaded solid bodies associated with the argument faceted body.  
        
        Also returns the number of unloaded associated faceted bodies.
        
        Signature ``GetAssociatedFacetedBodies(solidBody)`` 
        
        :param solidBody:  The body for which to get associated faceted bodies  
        :type solidBody: :py:class:`NXOpen.Body` 
        :returns: a tuple 
        :rtype: A tuple consisting of (associatedFacetedBodies, numberOfUnloadedFacetedBodies). associatedFacetedBodies is a list of :py:class:`NXOpen.Facet.FacetedBody`.   Array of loaded associated faceted bodies numberOfUnloadedFacetedBodies is a int.   The number of unloaded associated faceted bodies for this solids body 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteTemporaryFacesAndEdges(self) -> None:
        """
        Delete any temporary faces and edges on faceted bodies that may have been created 
        in the specified part.  
        
        Please note that this call will invoke an Update operation.
        
        Signature ``DeleteTemporaryFacesAndEdges()`` 
        
        .. versionadded:: NX5.0.2
        
        License requirements: None.
        """
        ...
    
    
    def CreateBestFitAlignBuilder(self) -> BestFitAlignBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.BestFitAlignBuilder`  
        
        Signature ``CreateBestFitAlignBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.BestFitAlignBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling")
        """
        ...
    
    
    def CreateFillHoleBuilder(self) -> FillHoleBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.FillHoleBuilder`  
        
        Signature ``CreateFillHoleBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.FillHoleBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def CreateSTLImportBuilder(self) -> STLImportBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.STLImportBuilder`  
        
        Signature ``CreateSTLImportBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.STLImportBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling")
        """
        ...
    
    
    def CreateDecimateFacetBodyBuilder(self) -> DecimateFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.DecimateFacetBodyBuilder`  
        
        Signature ``CreateDecimateFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.DecimateFacetBodyBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def CreateMultiPatchAlignmentBuilder(self) -> MultiPatchAlignmentBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.MultiPatchAlignmentBuilder`  
        
        Signature ``CreateMultiPatchAlignmentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.MultiPatchAlignmentBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def CreateSubdivideFacetBodyBuilder(self) -> SubdivideFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.SubdivideFacetBodyBuilder`  
        
        Signature ``CreateSubdivideFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.SubdivideFacetBodyBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def CreateSmoothFacetBodyBuilder(self) -> SmoothFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.SmoothFacetBodyBuilder`  
        
        Signature ``CreateSmoothFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.SmoothFacetBodyBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def CreateSnipFacetBodyBuilder(self) -> SnipFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.SnipFacetBodyBuilder`  
        
        Signature ``CreateSnipFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.SnipFacetBodyBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def CreateFacetBody(self, solidBodies: 'list[NXOpen.Body]') -> tuple:
        """
        Creates a JT :py:class:`NXOpen.Facet.FacetedBody` using the default faceting tolerances.  
        
        The output facetBodies and errorTable arrays are the same size as the input nSolidBodies. 
        The errorTable array provides information about any errors encountered when faceting bodies. 
        Note that it is possible that faceted bodies with 0 facets are created (and returned in the facetBodies parameter). 
        For this case, the errorTable will contain the UF_FACET_err_zero_facets_produced error. 
        If there is an existing facet body it will get refaceted with the previous tolerance used to tessellate it .
        See :py:meth:`NXOpen.Body.GetFacetedBody` for ways to check for this situation.
        
        Signature ``CreateFacetBody(solidBodies)`` 
        
        :param solidBodies: 
        :type solidBodies: list of :py:class:`NXOpen.Body` 
        :returns: a tuple 
        :rtype: A tuple consisting of (facetBodies, errorTable). facetBodies is a list of :py:class:`NXOpen.Facet.FacetedBody`. errorTable is a list of int. 
        
        .. versionadded:: NX7.5.5
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    
    
    def CreateFacetBodyFromFaces(self, solidFaces: 'list[NXOpen.Face]') -> tuple:
        """
        Creates a JT :py:class:`NXOpen.Facet.FacetedBody` using the default faceting tolerances.  
        
        The output facetBodies and errorTable arrays are the same size as the input nSolidFaces. 
        The errorTable array provides information about any errors encountered when faceting bodies. 
        Note that it is possible that faceted bodies with 0 facets are created (and returned in the facetBodies parameter). 
        For this case, the errorTable will contain the UF_FACET_err_zero_facets_produced error. 
        If there is an existing facet body it will get refaceted with the previous tolerance used to tessellate it .
        See :py:meth:`NXOpen.Body.GetFacetedBody` for ways to check for this situation.
        
        Signature ``CreateFacetBodyFromFaces(solidFaces)`` 
        
        :param solidFaces: 
        :type solidFaces: list of :py:class:`NXOpen.Face` 
        :returns: a tuple 
        :rtype: A tuple consisting of (facetBodies, errorTable). facetBodies is a list of :py:class:`NXOpen.Facet.FacetedBody`. errorTable is a list of int. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    
    
    def CreateExtrudeFacetBodyBuilder(self) -> ExtrudeFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.ExtrudeFacetBodyBuilder`  
        
        Signature ``CreateExtrudeFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.ExtrudeFacetBodyBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
        """
        ...
    
    
    def CreateExtrudeProfileBuilder(self) -> ExtrudeProfileBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.ExtrudeProfileBuilder`  
        
        Signature ``CreateExtrudeProfileBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.ExtrudeProfileBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
        """
        ...
    
    
    def CreateMergeFacetBodyBuilder(self) -> MergeFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.MergeFacetBodyBuilder`  
        
        Signature ``CreateMergeFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.MergeFacetBodyBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
        """
        ...
    
    
    def CreateBridgeFacetBodyBuilder(self) -> BridgeFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.BridgeFacetBodyBuilder`  
        
        Signature ``CreateBridgeFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.BridgeFacetBodyBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
        """
        ...
    
    
    def CreateSewFacetBodyBuilder(self) -> SewFacetBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Facet.SewFacetBodyBuilder`  
        
        Signature ``CreateSewFacetBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Facet.SewFacetBodyBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
        """
        ...
    
    FacetModelingCollection: FacetModelingCollection = ...
    """
    Returns the FacetModelingCollection instance belonging to this part 
    
    Signature ``FacetModelingCollection`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.FacetModelingCollection`
    """


class SmoothFacetBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.SmoothFacetBodyBuilder`.  
    
    Smooth Facet Body Builder is a function to facilitate the removal of noise from facet bodies while keeping the general shape in tact. 
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateSmoothFacetBodyBuilder`
    
    Default values.
    
    ===============  =====
    Property         Value
    ===============  =====
    IsEditCopy       0 
    ---------------  -----
    IsLockBoundary   0 
    ---------------  -----
    ModifyPercent    100 
    ---------------  -----
    SmoothFactor     1 
    ===============  =====
    
    .. versionadded:: NX7.5.0
    """
    Bodies: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the facet bodies to be smoothed.  
    
    Inputs to this command can be convergent objects. 
    
    <hr>
    
    Getter Method
    
    Signature ``Bodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.Facet.SmoothFacetBodyBuilder.FacetCollector` instead.
    
    License requirements: None.
    """
    FacetBodies: SelectFacetedBodyList = ...
    """
    Returns  the facet bodies to be smoothed 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBodyList` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX11.0.0
       Use :py:meth:`NXOpen.Facet.SmoothFacetBodyBuilder.Bodies` instead.
    
    License requirements: None.
    """
    FacetCollector: NXOpen.FacetCollector = ...
    """
    Returns or sets  a collector of facets on the facet bodies to be to be smoothed.  
    
    <hr>
    
    Getter Method
    
    Signature ``FacetCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FacetCollector`` 
    
    :param collector: 
    :type collector: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsEditCopy: bool = ...
    """
    Returns or sets  the option indicating if a copy of the facet body will be smoothed without altering the original 
    
    <hr>
    
    Getter Method
    
    Signature ``IsEditCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsEditCopy`` 
    
    :param isEditCopy: 
    :type isEditCopy: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsLockBoundary: bool = ...
    """
    Returns or sets  the option indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact 
    
    <hr>
    
    Getter Method
    
    Signature ``IsLockBoundary`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsLockBoundary`` 
    
    :param isLockBoundary: 
    :type isLockBoundary: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    ModifyPercent: int = ...
    """
    Returns or sets  the modification percentage 
    
    <hr>
    
    Getter Method
    
    Signature ``ModifyPercent`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ModifyPercent`` 
    
    :param modifyPercent: 
    :type modifyPercent: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    RegionList: NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList = ...
    """
    Returns  an optional list of regions on the facet bodies to be smoothed 
    
    <hr>
    
    Getter Method
    
    Signature ``RegionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.Facet.SmoothFacetBodyBuilder.FacetCollector` instead.
    
    License requirements: None.
    """
    SmoothFactor: int = ...
    """
    Returns or sets  the smoothing factor 
    
    <hr>
    
    Getter Method
    
    Signature ``SmoothFactor`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SmoothFactor`` 
    
    :param smoothFactor: 
    :type smoothFactor: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: SmoothFacetBodyBuilder = ...  # unknown typename


class CurvatureBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.CurvatureBuilder`.  
    
    It calculates the maximum absolute principal curvature on facet
    bodies and creates a color map of these values.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateFacetCurvatureBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def DeleteCurvature(self) -> None:
        """
        Deletes the curvature data associated with the input facet bodies.  
        
        Call this method in order to save memory if the curvature data are not needed any more.
        
        Signature ``DeleteCurvature()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    Bodies: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the input facet body list.  
    
    Inputs to this command can be convergent objects. 
    
    <hr>
    
    Getter Method
    
    Signature ``Bodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ConcaveRadius: float = ...
    """
    Returns or sets  the concave radius threshold 
    
    <hr>
    
    Getter Method
    
    Signature ``ConcaveRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConcaveRadius`` 
    
    :param concaveRadius: 
    :type concaveRadius: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    ConvexRadius: float = ...
    """
    Returns or sets  the convex radius threshold 
    
    <hr>
    
    Getter Method
    
    Signature ``ConvexRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConvexRadius`` 
    
    :param convexRadius: 
    :type convexRadius: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    FacetBodies: SelectFacetedBodyList = ...
    """
    Returns  the input facet body list 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBodyList` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX11.0.0
       Use :py:meth:`NXOpen.Facet.CurvatureBuilder.Bodies` instead.
    
    License requirements: None.
    """
    IsDirectionReversed: bool = ...
    """
    Returns or sets  the reverse direction option 
    
    <hr>
    
    Getter Method
    
    Signature ``IsDirectionReversed`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsDirectionReversed`` 
    
    :param directionReversed: 
    :type directionReversed: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    SmoothingFactor: float = ...
    """
    Returns or sets  the smoothing factor 
    
    <hr>
    
    Getter Method
    
    Signature ``SmoothingFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SmoothingFactor`` 
    
    :param smoothingFactor: 
    :type smoothingFactor: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: CurvatureBuilder = ...  # unknown typename


class SelectFacetedBodyList(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a list of objects on a selection list.  
    
    .. versionadded:: NX5.0.0
    """
    
    @typing.overload
    def Add(self, object: FacetedBody) -> bool:
        """
        Adds an object to the list
        
        Signature ``Add(object)`` 
        
        :param object:  object to add  
        :type object: :py:class:`NXOpen.Facet.FacetedBody` 
        :returns:  True if succesully added to list;
        False if the object was already a member
        of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, objects: 'list[FacetedBody]') -> bool:
        """
        Adds a set of objects to the list
        
        Signature ``Add(objects)`` 
        
        :param objects:  objects to add  
        :type objects: list of :py:class:`NXOpen.Facet.FacetedBody` 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, inputSelectionMethod: NXOpen.SelectionMethod) -> bool:
        """
        Adds the objects from a SelectionMethod to the list
        
        Signature ``Add(inputSelectionMethod)`` 
        
        :param inputSelectionMethod:  selection method containing objects to add  
        :type inputSelectionMethod: :py:class:`NXOpen.SelectionMethod` 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, selection: FacetedBody, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
        Adds the object with the objects view and objects point
        
        Signature ``Add(selection, view, point)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Facet.FacetedBody` 
        :param view:  selected object view 
        :type view: :py:class:`NXOpen.View` 
        :param point:  selected object point 
        :type point: :py:class:`NXOpen.Point3d` 
        :returns:  True if succesully added to list;
        False if the object was already a member
        of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, snapType: NXOpen.InferSnapTypeSnapType, selection1: FacetedBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: FacetedBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
        The object being selected with the objects view and objects point and snap information.
        
        Signature ``Add(snapType, selection1, view1, point1, selection2, view2, point2)`` 
        
        :param snapType:   snap point type 
        :type snapType: :py:class:`NXOpen.InferSnapTypeSnapType` 
        :param selection1:  first selected object  
        :type selection1: :py:class:`NXOpen.Facet.FacetedBody` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1: first  selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Facet.FacetedBody` 
        :param view2: second  selected object view 
        :type view2: :py:class:`NXOpen.View` 
        :param point2:  second selected object point 
        :type point2: :py:class:`NXOpen.Point3d` 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, selection: FacetedBody, caeSubType: NXOpen.CaeObjectTypeCaeSubType, caeSubId: int) -> bool:
        """
        The object being selected with CAE set object information.
        
        Signature ``Add(selection, caeSubType, caeSubId)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Facet.FacetedBody` 
        :param caeSubType:  CAE set object sub type 
        :type caeSubType: :py:class:`NXOpen.CaeObjectTypeCaeSubType` 
        :param caeSubId:  CAE set object sub id 
        :type caeSubId: int 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObjectList.Add`.
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Remove(self, object: FacetedBody) -> bool:
        """
        Remove specified object from list.
        
        Signature ``Remove(object)`` 
        
        :param object:  Object to remove  
        :type object: :py:class:`NXOpen.Facet.FacetedBody` 
        :returns:  True if succesully removed from list;
        False if the object was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Remove(self, object: FacetedBody, view: NXOpen.View) -> bool:
        """
        Remove specified object from list.
        
        Signature ``Remove(object, view)`` 
        
        :param object:  Object to remove  
        :type object: :py:class:`NXOpen.Facet.FacetedBody` 
        :param view:  with this view 
        :type view: :py:class:`NXOpen.View` 
        :returns:  True if succesully removed from list;
        False if the object / view was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Remove(self, snapType: NXOpen.InferSnapTypeSnapType, selection1: FacetedBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: FacetedBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
        Remove specified object from list.
        
        Signature ``Remove(snapType, selection1, view1, point1, selection2, view2, point2)`` 
        
        :param snapType:   snap point type 
        :type snapType: :py:class:`NXOpen.InferSnapTypeSnapType` 
        :param selection1:  first selected object  
        :type selection1: :py:class:`NXOpen.Facet.FacetedBody` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1: first  selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Facet.FacetedBody` 
        :param view2: second  selected object view 
        :type view2: :py:class:`NXOpen.View` 
        :param point2:  second selected object point 
        :type point2: :py:class:`NXOpen.Point3d` 
        :returns:  True if succesully removed from list;
        False if the object was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Remove(self, inputSelectionMethod: NXOpen.SelectionMethod) -> bool:
        """
        Removes the objects from a SelectionMethod from the list
        
        Signature ``Remove(inputSelectionMethod)`` 
        
        :param inputSelectionMethod:  selection method containing objects to add  
        :type inputSelectionMethod: :py:class:`NXOpen.SelectionMethod` 
        :returns:  True if succesully removed all objects from the list;
        False if there was at least one object that was not a
        member of the list  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveArray(self, objects: 'list[FacetedBody]') -> bool:
        """
        Remove specified objects from list.  
        
        Signature ``RemoveArray(objects)`` 
        
        :param objects:  Objects to remove  
        :type objects: list of :py:class:`NXOpen.Facet.FacetedBody` 
        :returns:  True if succesully removed from list;
        False if the object was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Clear(self) -> None:
        """
        Removes all items from the list.  
        
        Signature ``Clear()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Contains(self, object: FacetedBody) -> bool:
        """
        Returns whether the specified object is already in the list or not.  
        
        Signature ``Contains(object)`` 
        
        :param object:  object to check  
        :type object: :py:class:`NXOpen.Facet.FacetedBody` 
        :returns:  true if object is in the list, false otherwise  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetArray(self, objects: 'list[FacetedBody]') -> None:
        """
        Overloaded method SetArray
        
        * ``SetArray(objects)`` 
        * ``SetArray(vars)`` 
        
        <hr>
        
        Sets the list of objects in the selection list. This will clear any existing
        items in the list.
        
        Signature ``SetArray(objects)`` 
        
        :param objects:  items to put in the list 
        :type objects: list of :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        
        <hr>
        """
        ...
    
    
    def GetArray(self) -> 'list[FacetedBody]':
        """
        Overloaded method GetArray
        
        * ``GetArray()`` 
        * ``GetArray()`` 
        
        <hr>
        
        Returns the list of objects in the selection list.
        
        Signature ``GetArray()`` 
        
        :returns:  items in list  
        :rtype: list of :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        
        <hr>
        """
        ...
    
    
    def GetSelectObjectArray(self) -> 'list[NXOpen.SelectObject]':
        """
        Returns the list of SelectObjects in the selection list.  
        
        Signature ``GetSelectObjectArray()`` 
        
        :returns:  items in list  
        :rtype: list of :py:class:`NXOpen.SelectObject` 
        
        .. versionadded:: NX5.0.0
        
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
    
    DuplicatesAllowed: bool = ...
    """
    Returns  whether duplicate objects are allowed in the selection list.  
    
    <hr>
    
    Getter Method
    
    Signature ``DuplicatesAllowed`` 
    
    :returns:  Whether duplicate objects are allowed  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Size: int = ...
    """
    Returns  the number of objects in the list.  
    
    <hr>
    
    Getter Method
    
    Signature ``Size`` 
    
    :returns:  number of objects in the list  
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: SelectFacetedBodyList = ...  # unknown typename


class SubdivideFacetBodyBuilderSubdivisionMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivideFacetBodyBuilderSubdivisionMethodType():
    """
    Subdivision methods 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SubdivideIntoFour", "Subdivides the polygons into four sub triangles. The original mesh structure remains."
       "SubdividebyEdgeLength", "Subdivides the polygons to a specified edge length. The original mesh structure disappears."
    """
    SubdivideIntoFour = 0  # SubdivideFacetBodyBuilderSubdivisionMethodTypeMemberType
    SubdividebyEdgeLength = 1  # SubdivideFacetBodyBuilderSubdivisionMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SubdivideFacetBodyBuilderInterpolationMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivideFacetBodyBuilderInterpolationMethodType():
    """
    Subdivision interpolation methods 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "In the linear option the sub-triangles are coplanar to the original triangle. Shape resolution remains untouched."
       "Cubic", "In the cubic option the sub-triangles are fitted cubic to the surrounding triangles. Shape resolution increases."
    """
    Linear = 0  # SubdivideFacetBodyBuilderInterpolationMethodTypeMemberType
    Cubic = 1  # SubdivideFacetBodyBuilderInterpolationMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SubdivideFacetBodyBuilder(NXOpen.Builder):
    """
    This class provides functionality to subdivide the polygons to increase the density of the facet bodies.  
    
    Subdividing Polygons creates a smoother representation.
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateSubdivideFacetBodyBuilder`
    
    Default values.
    
    ====================  ==================
    Property              Value
    ====================  ==================
    AngleThreshold        30 
    --------------------  ------------------
    EdgeLength            1 
    --------------------  ------------------
    InterpolationMethod   Cubic 
    --------------------  ------------------
    IsEditCopy            0 
    --------------------  ------------------
    IsOptimize            0 
    --------------------  ------------------
    SubdivisionMethod     SubdivideIntoFour 
    ====================  ==================
    
    .. versionadded:: NX7.5.0
    """
    
    class SubdivisionMethodType():
        """
        Subdivision methods 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SubdivideIntoFour", "Subdivides the polygons into four sub triangles. The original mesh structure remains."
           "SubdividebyEdgeLength", "Subdivides the polygons to a specified edge length. The original mesh structure disappears."
        """
        SubdivideIntoFour = 0  # SubdivideFacetBodyBuilderSubdivisionMethodTypeMemberType
        SubdividebyEdgeLength = 1  # SubdivideFacetBodyBuilderSubdivisionMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class InterpolationMethodType():
        """
        Subdivision interpolation methods 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "In the linear option the sub-triangles are coplanar to the original triangle. Shape resolution remains untouched."
           "Cubic", "In the cubic option the sub-triangles are fitted cubic to the surrounding triangles. Shape resolution increases."
        """
        Linear = 0  # SubdivideFacetBodyBuilderInterpolationMethodTypeMemberType
        Cubic = 1  # SubdivideFacetBodyBuilderInterpolationMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AngleThreshold: float = ...
    """
    Returns or sets  the angular tolerance to detect sharp edges to be kept.  
    
    Cubic interpolation can not interpolate over an edge of two triangles whose normals differ more than the specified value. Same applies to re-meshing. 
    
    <hr>
    
    Getter Method
    
    Signature ``AngleThreshold`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AngleThreshold`` 
    
    :param angleThreshold: 
    :type angleThreshold: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Bodies: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the facet bodies to be subdivided.  
    
    Inputs to this command can be convergent objects. 
    
    <hr>
    
    Getter Method
    
    Signature ``Bodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.Facet.SubdivideFacetBodyBuilder.FacetCollector` instead.
    
    License requirements: None.
    """
    EdgeLength: float = ...
    """
    Returns or sets  the value indicating length of the edge of the polygons to be subdivided.  
    
    <hr>
    
    Getter Method
    
    Signature ``EdgeLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EdgeLength`` 
    
    :param edgeLength: 
    :type edgeLength: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    FacetBodies: SelectFacetedBodyList = ...
    """
    Returns  the facet bodies to be subdivided
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBodyList` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX11.0.0
       Use :py:meth:`NXOpen.Facet.SubdivideFacetBodyBuilder.Bodies` instead.
    
    License requirements: None.
    """
    FacetCollector: NXOpen.FacetCollector = ...
    """
    Returns or sets  a collector of facets on the facet bodies to be subdivided.  
    
    <hr>
    
    Getter Method
    
    Signature ``FacetCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FacetCollector`` 
    
    :param collector: 
    :type collector: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    InterpolationMethod: SubdivideFacetBodyBuilderInterpolationMethodType = ...
    """
    Returns or sets  the interpolation method 
    
    <hr>
    
    Getter Method
    
    Signature ``InterpolationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SubdivideFacetBodyBuilderInterpolationMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpolationMethod`` 
    
    :param interpolationMethod: 
    :type interpolationMethod: :py:class:`NXOpen.Facet.SubdivideFacetBodyBuilderInterpolationMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsEditCopy: bool = ...
    """
    Returns or sets  the value indicating if a copy of the facet body to be subdivided without altering the original.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsEditCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsEditCopy`` 
    
    :param isEditCopy: 
    :type isEditCopy: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    IsOptimize: bool = ...
    """
    Returns or sets  the value indicating whether to perform a decimation step after the subdivision.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsOptimize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsOptimize`` 
    
    :param isOptimize: 
    :type isOptimize: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    RegionList: NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList = ...
    """
    Returns  an optional list of regions on the facet bodies to be subdivided.  
    
    <hr>
    
    Getter Method
    
    Signature ``RegionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList` 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX12.0.0
       Use :py:meth:`NXOpen.Facet.SubdivideFacetBodyBuilder.FacetCollector` instead.
    
    License requirements: None.
    """
    SubdivisionMethod: SubdivideFacetBodyBuilderSubdivisionMethodType = ...
    """
    Returns or sets  the subdivision method 
    
    <hr>
    
    Getter Method
    
    Signature ``SubdivisionMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SubdivideFacetBodyBuilderSubdivisionMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SubdivisionMethod`` 
    
    :param subdivisionMethod: 
    :type subdivisionMethod: :py:class:`NXOpen.Facet.SubdivideFacetBodyBuilderSubdivisionMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: SubdivideFacetBodyBuilder = ...  # unknown typename


class CleanupFacetBodyBuilderCleanupOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CleanupFacetBodyBuilderCleanupOptions():
    """
    These represent the options for each facet defect 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Don't perform Analysis or Repair"
       "Analyze", "Perform Analysis"
       "Repair", "Perform Repair"
    """
    NotSet = 0  # CleanupFacetBodyBuilderCleanupOptionsMemberType
    Analyze = 1  # CleanupFacetBodyBuilderCleanupOptionsMemberType
    Repair = 2  # CleanupFacetBodyBuilderCleanupOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CleanupFacetBodyBuilderOriginalBodyOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CleanupFacetBodyBuilderOriginalBodyOptions():
    """
    These represent the options for handling the input bodies  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Keep", "Keep original body"
       "Hide", "Hide original body"
       "Delete", "Delete original body"
    """
    Keep = 0  # CleanupFacetBodyBuilderOriginalBodyOptionsMemberType
    Hide = 1  # CleanupFacetBodyBuilderOriginalBodyOptionsMemberType
    Delete = 2  # CleanupFacetBodyBuilderOriginalBodyOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CleanupFacetBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.CleanupFacetBodyBuilder` builder.  
    
    It removes defects that are present in the surfaces of the bodies selected. 
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateCleanupFacetBodyBuilder`
    
    Default values.
    
    =====================  ========
    Property               Value
    =====================  ========
    FoldedEdges            Analyze 
    ---------------------  --------
    InconsistentNormals    Analyze 
    ---------------------  --------
    LaminarSlits           Analyze 
    ---------------------  --------
    LongFacets             Analyze 
    ---------------------  --------
    MaxRatioLongFacets     10 
    ---------------------  --------
    MinAngleFoldedFacets   15 
    ---------------------  --------
    OriginalBodyOption     Delete 
    ---------------------  --------
    SelfIntersections      Analyze 
    ---------------------  --------
    ShowInfo               0 
    ---------------------  --------
    ThinFacets             Analyze 
    =====================  ========
    
    .. versionadded:: NX10.0.0
    """
    
    class CleanupOptions():
        """
        These represent the options for each facet defect 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Don't perform Analysis or Repair"
           "Analyze", "Perform Analysis"
           "Repair", "Perform Repair"
        """
        NotSet = 0  # CleanupFacetBodyBuilderCleanupOptionsMemberType
        Analyze = 1  # CleanupFacetBodyBuilderCleanupOptionsMemberType
        Repair = 2  # CleanupFacetBodyBuilderCleanupOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OriginalBodyOptions():
        """
        These represent the options for handling the input bodies  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Keep", "Keep original body"
           "Hide", "Hide original body"
           "Delete", "Delete original body"
        """
        Keep = 0  # CleanupFacetBodyBuilderOriginalBodyOptionsMemberType
        Hide = 1  # CleanupFacetBodyBuilderOriginalBodyOptionsMemberType
        Delete = 2  # CleanupFacetBodyBuilderOriginalBodyOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetAllOptionsToNone(self) -> None:
        """
        Sets all cleanup options to :py:class:`Facet.CleanupFacetBodyBuilderCleanupOptions.None <Facet.CleanupFacetBodyBuilderCleanupOptions>`, which means to do nothing 
        
        Signature ``SetAllOptionsToNone()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def SetAllOptionsToAnalyze(self) -> None:
        """
        Sets all cleanup options to :py:class:`Facet.CleanupFacetBodyBuilderCleanupOptions.Analyze <Facet.CleanupFacetBodyBuilderCleanupOptions>`, which means to identify the defects only for the input bodies 
        
        Signature ``SetAllOptionsToAnalyze()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def SetAllOptionsToRepair(self) -> None:
        """
        Sets all cleanup options to :py:class:`Facet.CleanupFacetBodyBuilderCleanupOptions.Repair <Facet.CleanupFacetBodyBuilderCleanupOptions>`, which means to identify as well as repair the defects for the input bodies 
        
        Signature ``SetAllOptionsToRepair()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: studio_free_form ("STUDIO FREE FORM")
        """
        ...
    
    
    def DisplayCleanupReportInListWindow(self) -> None:
        """
        Displays the :py:class:`NXOpen.ListingWindow` with numbers of various type of defects identified or repaired.  
        
        If we call this method externally without UI, it displays 
        the information on standard output device. The listing 
        window output can be sent to the Information window or to a 
        file, or to both. See :py:meth:`NXOpen.ListingWindow.SelectDevice`
        for more information.
        
        Signature ``DisplayCleanupReportInListWindow()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    DistanceTolerance: float = ...
    """
    Returns or sets  the tolerance value use to detect the faults in facet body and fix the same 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param disTolerance: 
    :type disTolerance: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    FoldedEdges: CleanupFacetBodyBuilderCleanupOptions = ...
    """
    Returns or sets  the option to identify or repair facets having an angle with adjacent facets less than a specified minimum value 
    
    <hr>
    
    Getter Method
    
    Signature ``FoldedEdges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FoldedEdges`` 
    
    :param foldedEdges: 
    :type foldedEdges: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    InconsistentNormals: CleanupFacetBodyBuilderCleanupOptions = ...
    """
    Returns or sets  the option to identify or repair normals of neighboring facets or vertices that do not have the right orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``InconsistentNormals`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InconsistentNormals`` 
    
    :param inconsistentNormals: 
    :type inconsistentNormals: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    InputBodies: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the input facet bodies to be analyzed or repaired 
    
    <hr>
    
    Getter Method
    
    Signature ``InputBodies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LaminarSlits: CleanupFacetBodyBuilderCleanupOptions = ...
    """
    Returns or sets  the option to identify or repair thin holes or slits in the mesh caused by facets not being aligned 
    
    <hr>
    
    Getter Method
    
    Signature ``LaminarSlits`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LaminarSlits`` 
    
    :param laminarSlits: 
    :type laminarSlits: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    LongFacets: CleanupFacetBodyBuilderCleanupOptions = ...
    """
    Returns or sets  the option to identify or repair facets with a ratio of longest to shortest side exceeding a specified value 
    
    <hr>
    
    Getter Method
    
    Signature ``LongFacets`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LongFacets`` 
    
    :param longFacets: 
    :type longFacets: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MaxRatioLongFacets: float = ...
    """
    Returns or sets  the specified value used to define long facets 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxRatioLongFacets`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxRatioLongFacets`` 
    
    :param maxRatioLongFacets: 
    :type maxRatioLongFacets: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MinAngleFoldedFacets: float = ...
    """
    Returns or sets  the minimum angle between adjacent facets to define folded facets 
    
    <hr>
    
    Getter Method
    
    Signature ``MinAngleFoldedFacets`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinAngleFoldedFacets`` 
    
    :param minAngleFoldedFacets: 
    :type minAngleFoldedFacets: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    OriginalBodyOption: CleanupFacetBodyBuilderOriginalBodyOptions = ...
    """
    Returns or sets  the option for handling the input facet bodies 
    
    <hr>
    
    Getter Method
    
    Signature ``OriginalBodyOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderOriginalBodyOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OriginalBodyOption`` 
    
    :param enumOriginalBodyOption: 
    :type enumOriginalBodyOption: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderOriginalBodyOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    SelfIntersections: CleanupFacetBodyBuilderCleanupOptions = ...
    """
    Returns or sets  the option to identify or repair facets of the same mesh intersecting each other 
    
    <hr>
    
    Getter Method
    
    Signature ``SelfIntersections`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelfIntersections`` 
    
    :param selfIntersections: 
    :type selfIntersections: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    ShowInfo: bool = ...
    """
    Returns or sets  
    the option to display numbers of various type of defects identified or repaired in the :py:class:`NXOpen.ListingWindow`.  
    
    If this option is true, but the program is running externally without UI, display would go to
    a standard output devicethe.  The listing window output can be sent to the Information window or to a 
    file, or to both. See :py:meth:`NXOpen.ListingWindow.SelectDevice`
    for more information.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowInfo`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowInfo`` 
    
    :param showInfo: 
    :type showInfo: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    ThinFacets: CleanupFacetBodyBuilderCleanupOptions = ...
    """
    Returns or sets  the option to identify or repair facets with with one long edge and two edges with more or the less the same length and a ratio of length to width exceeding a specified value 
    
    <hr>
    
    Getter Method
    
    Signature ``ThinFacets`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ThinFacets`` 
    
    :param thinFacets: 
    :type thinFacets: :py:class:`NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: CleanupFacetBodyBuilder = ...  # unknown typename


class LocalOffsetBuilderTransitionMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LocalOffsetBuilderTransitionMethodType():
    """
    Transition Region Definition 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None creates an offset without a transition region."
       "ByConstantOffset", "Constant offset creates a transition region of constant distance."
       "ByRegionSelection", "Region selection allows the user to select transtion regions."
    """
    NotSet = 0  # LocalOffsetBuilderTransitionMethodTypeMemberType
    ByConstantOffset = 1  # LocalOffsetBuilderTransitionMethodTypeMemberType
    ByRegionSelection = 2  # LocalOffsetBuilderTransitionMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LocalOffsetBuilderShapeMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LocalOffsetBuilderShapeMethodType():
    """
    Continuity Method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Sharp", "Sharp specifies a transition region without smoothing."
       "Smooth", "Smooth specifies a transition region with smoothing."
    """
    Sharp = 0  # LocalOffsetBuilderShapeMethodTypeMemberType
    Smooth = 1  # LocalOffsetBuilderShapeMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LocalOffsetBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Facet.LocalOffsetBuilder`.  
    
    This class adds or removes material on facet bodies by creating local offsets.
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateLocalOffsetBuilder`
    
    Default values.
    
    =====================  =========================================
    Property               Value
    =====================  =========================================
    IsEditCopy             0 
    ---------------------  -----------------------------------------
    IsSmoothEdge           1 
    ---------------------  -----------------------------------------
    OffsetDistance.Value   5 (millimeters part), 0.2 (inches part) 
    ---------------------  -----------------------------------------
    RegionDistance.Value   10 (millimeters part), 0.4 (inches part) 
    ---------------------  -----------------------------------------
    ShapeMethod            Smooth 
    ---------------------  -----------------------------------------
    TransitionMethod       None 
    =====================  =========================================
    
    .. versionadded:: NX12.0.0
    """
    
    class TransitionMethodType():
        """
        Transition Region Definition 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None creates an offset without a transition region."
           "ByConstantOffset", "Constant offset creates a transition region of constant distance."
           "ByRegionSelection", "Region selection allows the user to select transtion regions."
        """
        NotSet = 0  # LocalOffsetBuilderTransitionMethodTypeMemberType
        ByConstantOffset = 1  # LocalOffsetBuilderTransitionMethodTypeMemberType
        ByRegionSelection = 2  # LocalOffsetBuilderTransitionMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ShapeMethodType():
        """
        Continuity Method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Sharp", "Sharp specifies a transition region without smoothing."
           "Smooth", "Smooth specifies a transition region with smoothing."
        """
        Sharp = 0  # LocalOffsetBuilderShapeMethodTypeMemberType
        Smooth = 1  # LocalOffsetBuilderShapeMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    FacetRegion: NXOpen.FacetCollector = ...
    """
    Returns  the facets to be offset 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetRegion`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FacetTransitionRegions: NXOpen.FacetCollector = ...
    """
    Returns  the user-selected transition regions 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetTransitionRegions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IsEditCopy: bool = ...
    """
    Returns or sets  the option to create a non-associative copy of the selected body and edit that copy 
    
    <hr>
    
    Getter Method
    
    Signature ``IsEditCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsEditCopy`` 
    
    :param isEditCopy: 
    :type isEditCopy: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    IsRegenerateOffsetMesh: bool = ...
    """
    Returns or sets  the option to rebuild the mesh structure of the offset output 
    
    <hr>
    
    Getter Method
    
    Signature ``IsRegenerateOffsetMesh`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsRegenerateOffsetMesh`` 
    
    :param isRegenerateOffsetMesh: 
    :type isRegenerateOffsetMesh: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    IsReverseDirection: bool = ...
    """
    Returns or sets  the method to reverse the direction of the offset.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsReverseDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsReverseDirection`` 
    
    :param isReverseDirection: 
    :type isReverseDirection: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    IsSmoothEdge: bool = ...
    """
    Returns or sets  the option to add smoothing to the edge of the offset region 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSmoothEdge`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSmoothEdge`` 
    
    :param isSmoothEdge: 
    :type isSmoothEdge: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    OffsetDistance: NXOpen.Expression = ...
    """
    Returns  the linear distance of the created local offset, which may be a positive or negative distance 
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RegionDistance: NXOpen.Expression = ...
    """
    Returns  the distance of the transition region with the constant offset option 
    
    <hr>
    
    Getter Method
    
    Signature ``RegionDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ShapeMethod: LocalOffsetBuilderShapeMethodType = ...
    """
    Returns or sets  the method to define the shape of the transition region 
    
    <hr>
    
    Getter Method
    
    Signature ``ShapeMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.LocalOffsetBuilderShapeMethodType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShapeMethod`` 
    
    :param shapeMethod: 
    :type shapeMethod: :py:class:`NXOpen.Facet.LocalOffsetBuilderShapeMethodType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    TransitionMethod: LocalOffsetBuilderTransitionMethodType = ...
    """
    Returns or sets  the type of transition region 
    
    <hr>
    
    Getter Method
    
    Signature ``TransitionMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.LocalOffsetBuilderTransitionMethodType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TransitionMethod`` 
    
    :param transitionMethod: 
    :type transitionMethod: :py:class:`NXOpen.Facet.LocalOffsetBuilderTransitionMethodType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    Null: LocalOffsetBuilder = ...  # unknown typename


class FillHoleBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FillHoleBuilderTypes():
    """
    Hole filling type options. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FillHole", "Fills individual hole(s)."
       "FillIsland", "Fills a hole defined by inner island and outer facet body."
       "BridgeGap", "Bridges some open boundary edges with a linear fill."
    """
    FillHole = 0  # FillHoleBuilderTypesMemberType
    FillIsland = 1  # FillHoleBuilderTypesMemberType
    BridgeGap = 2  # FillHoleBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FillHoleBuilderTargetTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FillHoleBuilderTargetTypes():
    """
    Options defining how to target holes for filling. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UserDefined", "Fills user-defined target holes."
       "ByNumberOfEdges", "Automatically target holes based on number of edges."
    """
    UserDefined = 0  # FillHoleBuilderTargetTypesMemberType
    ByNumberOfEdges = 1  # FillHoleBuilderTargetTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FillHoleBuilderSmoothTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FillHoleBuilderSmoothTypes():
    """
    Smoothness and boundary continuity options. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "Linear (triangulated) fill."
       "Refined", "Smooth internal fill."
       "TangentBased", "Smooth fill, boundary is based on facet body tangent."
       "CurvatureBased", "Smooth fill, boundary is based on facet body curvature."
    """
    Linear = 0  # FillHoleBuilderSmoothTypesMemberType
    Refined = 1  # FillHoleBuilderSmoothTypesMemberType
    TangentBased = 2  # FillHoleBuilderSmoothTypesMemberType
    CurvatureBased = 3  # FillHoleBuilderSmoothTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FillHoleBuilder(NXOpen.Builder):
    """
    This class finds and fills holes to a prescribed boundary smoothness condition.  
    
    Inputs to this class can be convergent objects. 
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetedBodyCollection.CreateFillHoleBuilder`
    
    Default values.
    
    ===========  ============
    Property     Value
    ===========  ============
    IsEditCopy   0 
    -----------  ------------
    MaxEdges     0 
    -----------  ------------
    SmoothType   Linear 
    -----------  ------------
    TargetType   UserDefined 
    ===========  ============
    
    .. versionadded:: NX6.0.0
    """
    
    class Types():
        """
        Hole filling type options. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FillHole", "Fills individual hole(s)."
           "FillIsland", "Fills a hole defined by inner island and outer facet body."
           "BridgeGap", "Bridges some open boundary edges with a linear fill."
        """
        FillHole = 0  # FillHoleBuilderTypesMemberType
        FillIsland = 1  # FillHoleBuilderTypesMemberType
        BridgeGap = 2  # FillHoleBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TargetTypes():
        """
        Options defining how to target holes for filling. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "UserDefined", "Fills user-defined target holes."
           "ByNumberOfEdges", "Automatically target holes based on number of edges."
        """
        UserDefined = 0  # FillHoleBuilderTargetTypesMemberType
        ByNumberOfEdges = 1  # FillHoleBuilderTargetTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SmoothTypes():
        """
        Smoothness and boundary continuity options. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "Linear (triangulated) fill."
           "Refined", "Smooth internal fill."
           "TangentBased", "Smooth fill, boundary is based on facet body tangent."
           "CurvatureBased", "Smooth fill, boundary is based on facet body curvature."
        """
        Linear = 0  # FillHoleBuilderSmoothTypesMemberType
        Refined = 1  # FillHoleBuilderSmoothTypesMemberType
        TangentBased = 2  # FillHoleBuilderSmoothTypesMemberType
        CurvatureBased = 3  # FillHoleBuilderSmoothTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def ClearHoles(self) -> None:
        """
        Removes all holes, deletes associated hole polylines.  
        
        Signature ``ClearHoles()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindHoles(self) -> None:
        """
        Locates holes in the mesh and creates polylines around them.  
        
        Signature ``FindHoles()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearHoleFills(self) -> None:
        """
        Cleans up local meshes associated with each fill.  
        
        Signature ``ClearHoleFills()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FillHoles(self, globalUpdate: bool) -> NXOpen.DisplayableObject:
        """
        Fills targeted holes.  
        
        Signature ``FillHoles(globalUpdate)`` 
        
        :param globalUpdate:  If true, update the entire input facet body.  If                                  false, GetHoleFillsOnly() may be used to get a facet body                                  that contains only the new facets of the filled holes.  
        :type globalUpdate: bool 
        :returns:  updated input facet body  
        :rtype: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SwitchHoleFillType(self) -> None:
        """
        Switches boundary edge mapping based on the filling type (holes, island, bridge)
        When filling holes or islands, each hole is defined by a polyline.  
        
        When bridging holes,
        each individual open edge has its own polyline.
        
        Signature ``SwitchHoleFillType()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetHoleFillsOnly(self) -> NXOpen.DisplayableObject:
        """
        Builds a facet body that contains only the facets of the filled holes.  
        
        Signature ``GetHoleFillsOnly()`` 
        
        :returns:  the fill facet body  
        :rtype: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllHoles(self) -> 'list[NXOpen.DisplayableObject]':
        """
        Gets a list of all holes (represented by polylines).  
        
        Signature ``GetAllHoles()`` 
        
        :returns:  Hole polylines.  
        :rtype: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNumberOfHoles(self) -> int:
        """
        Gets the number of holes in the target facet body.  
        
        Signature ``GetNumberOfHoles()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetHoleByIndex(self, index: int) -> NXOpen.ICurve:
        """
        Gets a hole given an index into the list of holes.  
        
        Signature ``GetHoleByIndex(index)`` 
        
        :param index:  Index into the list of all holes  
        :type index: int 
        :returns:  Equals None if not found  
        :rtype: :py:class:`NXOpen.ICurve` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTargetHolesByEdgeNumber(self, numMaxEdges: int) -> 'list[NXOpen.DisplayableObject]':
        """
        Gets a list of targeted holes (represented by polylines) based on number of edges.  
        
        Signature ``GetTargetHolesByEdgeNumber(numMaxEdges)`` 
        
        :param numMaxEdges:  Targets polylines that have this many edges or less.  
        :type numMaxEdges: int 
        :returns:  Hole polylines.  
        :rtype: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    BridgeEdges1: NXOpen.SelectICurveList = ...
    """
    Returns  the first list of edges when bridging holes.  
    
    <hr>
    
    Getter Method
    
    Signature ``BridgeEdges1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectICurveList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    BridgeEdges2: NXOpen.SelectICurveList = ...
    """
    Returns  the second list of edges when bridging holes.  
    
    <hr>
    
    Getter Method
    
    Signature ``BridgeEdges2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectICurveList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    InnerHole: NXOpen.SelectICurveList = ...
    """
    Returns  the Inner Hole in island filling.  
    
    <hr>
    
    Getter Method
    
    Signature ``InnerHole`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectICurveList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    IsEditCopy: bool = ...
    """
    Returns or sets  the flag indicating if the hole filling is on the copy of the input facet body.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsEditCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsEditCopy`` 
    
    :param isEditCopy: 
    :type isEditCopy: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    MaxEdges: int = ...
    """
    Returns or sets  the maximum number of edges that a targeted hole can have.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaxEdges`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxEdges`` 
    
    :param maxEdges: 
    :type maxEdges: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    OuterHole: NXOpen.SelectICurveList = ...
    """
    Returns  the Outer Hole in island filling.  
    
    <hr>
    
    Getter Method
    
    Signature ``OuterHole`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectICurveList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    SmoothType: FillHoleBuilderSmoothTypes = ...
    """
    Returns or sets  the boundary smoothness.  
    
    <hr>
    
    Getter Method
    
    Signature ``SmoothType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.FillHoleBuilderSmoothTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SmoothType`` 
    
    :param smoothType: 
    :type smoothType: :py:class:`NXOpen.Facet.FillHoleBuilderSmoothTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    TargetBody: NXOpen.SelectDisplayableObject = ...
    """
    Returns  the facet body we will be filling.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    TargetFacetBody: SelectFacetedBody = ...
    """
    Returns  the facet body we will be filling.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetFacetBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.SelectFacetedBody` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX11.0.0
       Use :py:meth:`NXOpen.Facet.FillHoleBuilder.TargetBody` instead.
    
    License requirements: None.
    """
    TargetHole: NXOpen.SelectICurveList = ...
    """
    Returns  the hole curves using Fill Hole, User Defined.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetHole`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectICurveList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    TargetType: FillHoleBuilderTargetTypes = ...
    """
    Returns or sets  the hole target type when filling holes.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.FillHoleBuilderTargetTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetType`` 
    
    :param targetType: 
    :type targetType: :py:class:`NXOpen.Facet.FillHoleBuilderTargetTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Type: FillHoleBuilderTypes = ...
    """
    Returns or sets  the hole filling type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Facet.FillHoleBuilderTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Facet.FillHoleBuilderTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: studio_free_form ("STUDIO FREE FORM")
    """
    Null: FillHoleBuilder = ...  # unknown typename


class RemoveUndercutsBuilder(NXOpen.Builder):
    """
    This class handles the removal of undercut regions of a facet body.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreateRemoveUndercutsBuilder`
    
    Default values.
    
    =================  =====
    Property           Value
    =================  =====
    DraftAngle.Value   0 
    -----------------  -----
    IsEditCopy         0 
    =================  =====
    
    .. versionadded:: NX12.0.0
    """
    
    def GenerateIsoclines(self) -> None:
        """
        The generation of isoclines.  
        
        Create isocline curves on the input facet body. 
        
        Signature ``GenerateIsoclines()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_polygon_modeling (" NX Polygon Modeling")
        """
        ...
    
    DraftAngle: NXOpen.Expression = ...
    """
    Returns  the draft angle 
    
    <hr>
    
    Getter Method
    
    Signature ``DraftAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DrawDirection: NXOpen.Direction = ...
    """
    Returns or sets  the draft vector 
    
    <hr>
    
    Getter Method
    
    Signature ``DrawDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DrawDirection`` 
    
    :param drawDirection: 
    :type drawDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FacetBody: NXOpen.SelectDisplayableObject = ...
    """
    Returns  the facet body.  
    
    Inputs to this command can be convergent objects 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObject` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    IsEditCopy: bool = ...
    """
    Returns or sets  the flag indicating if the fixing undercuts is on the copy of the input facet body.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsEditCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsEditCopy`` 
    
    :param isEditCopy: 
    :type isEditCopy: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    MatchFace: bool = ...
    """
    Returns or sets  the match tangent to face.  
    
    Math the shorter face by bridging the input face to the edge of the longer face at the parting objet. 
    
    <hr>
    
    Getter Method
    
    Signature ``MatchFace`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MatchFace`` 
    
    :param matchFace: 
    :type matchFace: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    """
    PartingObject: NXOpen.SelectDisplayableObject = ...
    """
    Returns  the parting object 
    
    <hr>
    
    Getter Method
    
    Signature ``PartingObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObject` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SelectedCurve: NXOpen.ScCollector = ...
    """
    Returns  the selected isocline curve.  
    
    The undercut related to the selected isocline curve will be removed. 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedCurve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: RemoveUndercutsBuilder = ...  # unknown typename


class PaintBrushBuilder(NXOpen.Builder):
    """
    This class manages the paint brush utility for a facet body.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Facet.FacetModelingCollection.CreatePaintBrushBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def GetPaintBrushColor(self) -> 'list[float]':
        """
        Returns the paint brush color  
        
        Signature ``GetPaintBrushColor()`` 
        
        :returns:  Array of 3 RGB values, each between 0 and 1  
        :rtype: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPaintBrushColor(self, paintBrushColor: 'list[float]') -> None:
        """
        Sets the paint brush color 
        
        Signature ``SetPaintBrushColor(paintBrushColor)`` 
        
        :param paintBrushColor:  Array of 3 RGB values, each between 0 and 1  
        :type paintBrushColor: list of float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFacetBeingPainted(self, facet: FacetedBody) -> None:
        """
        Sets facet body being painted.  
        
        Signature ``SetFacetBeingPainted(facet)`` 
        
        :param facet:  Facet body being painted.  
        :type facet: :py:class:`NXOpen.Facet.FacetedBody` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.Facet.PaintBrushBuilder.SetBodyBeingPainted` instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetBodyBeingPainted(self, body: NXOpen.DisplayableObject) -> None:
        """
        Sets facet body being painted.  
        
        Inputs to this command can be convergent objects. 
        
        Signature ``SetBodyBeingPainted(body)`` 
        
        :param body:  Body being painted.  
        :type body: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PaintVertexColor(self, position: NXOpen.Point3d) -> None:
        """
        Paints facet body vertex color 
        
        Signature ``PaintVertexColor(position)`` 
        
        :param position:  Vertex position  
        :type position: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearThePaintPath(self) -> None:
        """
        Clears the paint path 
        
        Signature ``ClearThePaintPath()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetupPaintFacetBody(self) -> None:
        """
        Setup the paint facet body 
        
        Signature ``SetupPaintFacetBody()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTemporaryFacetDisplay(self, tempDisplay: bool) -> None:
        """
        Flag to use temporary facet display 
        
        Signature ``SetTemporaryFacetDisplay(tempDisplay)`` 
        
        :param tempDisplay:  Temporary display flag  
        :type tempDisplay: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: PaintBrushBuilder = ...  # unknown typename


