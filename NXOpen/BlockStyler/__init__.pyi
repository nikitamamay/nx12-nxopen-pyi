# module 'NXOpen.BlockStyler'
#
# Automatically generated 2025-06-09T14:38:43.652384
#
"""Default documentation for NXOpen.BlockStyler."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class UIBlock(NXOpen.TaggedObject):
    """
    Represents a UI Block  
    
    .. versionadded:: NX6.0.0
    """
    
    def GetProperties(self) -> PropertyList:
        """
        Returns the properties of the block  
        
        Signature ``GetProperties()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.BlockStyler.PropertyList` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Focus(self) -> None:
        """
        Focuses on the block.  
        
        Use this method for both focus and keyboard focus.
        
        Signature ``Focus()`` 
        
        .. versionadded:: NX6.0.2
        
        License requirements: None.
        """
        ...
    
    Enable: bool = ...
    """
    Returns or sets  the Enable.  
    
    If true, the block is sensitive.
    
    <hr>
    
    Getter Method
    
    Signature ``Enable`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Enable`` 
    
    :param enable: 
    :type enable: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Expanded: bool = ...
    """
    Returns or sets  the Expanded
    
    <hr>
    
    Getter Method
    
    Signature ``Expanded`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Expanded`` 
    
    :param expanded: 
    :type expanded: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Group: bool = ...
    """
    Returns or sets  the Group
    
    <hr>
    
    Getter Method
    
    Signature ``Group`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Group`` 
    
    :param group: 
    :type group: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Label: str = ...
    """
    Returns or sets  the Label
    
    <hr>
    
    Getter Method
    
    Signature ``Label`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Label`` 
    
    :param label: 
    :type label: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Name: str = ...
    """
    Returns  the name of the block or BlockID
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  Block Name.  
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Show: bool = ...
    """
    Returns or sets  the Visibility of block.  
    
    If true, the block is visible. Otherwise invisible.
    This is readonly property for dialog and will be always true for dialog.
    
    <hr>
    
    Getter Method
    
    Signature ``Show`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Show`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Type: str = ...
    """
    Returns  the type of block 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns:  Block Type. E.g., Integer, Double, etc.  
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: UIBlock = ...  # unknown typename


class FaceCollector(UIBlock):
    """
    Represents a Face Collector  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectModeMembers(self) -> 'list[str]':
        """
        Gets the SelectMode members 
        
        Signature ``GetSelectModeMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDefaultFaceRulesMembers(self) -> 'list[str]':
        """
        Gets the DefaultFaceRules members 
        
        Signature ``GetDefaultFaceRulesMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AllowConvergentObject: bool = ...
    """
    Returns or sets  the AllowConvergentObject
    
    <hr>
    
    Getter Method
    
    Signature ``AllowConvergentObject`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowConvergentObject`` 
    
    :param allowConvergentObject: 
    :type allowConvergentObject: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression.  
    
    If true, focus automatically progresses to the next selection block.
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BlendVirtualCurveOverlay: bool = ...
    """
    Returns or sets  the BlendVirtualCurveOverlay
    
    <hr>
    
    Getter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :param blendCurve: 
    :type blendCurve: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DefaultFaceRulesAsString: str = ...
    """
    Returns or sets  the DefaultFaceRules as string
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultFaceRulesAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultFaceRulesAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EntityType: int = ...
    """
    Returns or sets  the EntityType
    
    <hr>
    
    Getter Method
    
    Signature ``EntityType`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EntityType`` 
    
    :param entityType: 
    :type entityType: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    FaceRules: int = ...
    """
    Returns or sets  the FaceRules
    
    <hr>
    
    Getter Method
    
    Signature ``FaceRules`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FaceRules`` 
    
    :param faceRules: 
    :type faceRules: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumScopeAsString: str = ...
    """
    Returns or sets  the MaximumScope
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumScopeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumScopeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    PopupMenuEnabled: bool = ...
    """
    Returns or sets  the PopupMenuEnabled
    
    <hr>
    
    Getter Method
    
    Signature ``PopupMenuEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PopupMenuEnabled`` 
    
    :param enabled: 
    :type enabled: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectModeAsString: str = ...
    """
    Returns or sets  the SelectMode as string
    
    <hr>
    
    Getter Method
    
    Signature ``SelectModeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectModeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ToolTip: str = ...
    """
    Returns or sets  the ToolTip
    
    <hr>
    
    Getter Method
    
    Signature ``ToolTip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolTip`` 
    
    :param toolTip: 
    :type toolTip: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: FaceCollector = ...  # unknown typename


class AngularDimension(UIBlock):
    """
    Represents a Angular Dimension block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout member  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AdaptiveScaleLimits: bool = ...
    """
    Returns or sets the AdaptiveScaleLimits.  
    
    If true, indicates that the scale should be adaptive. Only available when WithScale is set to true.
    
    <hr>
    
    Getter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :param scaleLimits: 
    :type scaleLimits: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ExpressionObject: NXOpen.TaggedObject = ...
    """
    Returns or sets  the ExpressionObject
    
    <hr>
    
    Getter Method
    
    Signature ``ExpressionObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpressionObject`` 
    
    :param expressionObj: 
    :type expressionObj: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Formula: str = ...
    """
    Returns or sets  the Formula
    
    <hr>
    
    Getter Method
    
    Signature ``Formula`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Formula`` 
    
    :param formula: 
    :type formula: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HandleFixedSizeFlag: bool = ...
    """
    Returns or sets  the HandleFixedSizeFlag
    
    <hr>
    
    Getter Method
    
    Signature ``HandleFixedSizeFlag`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HandleFixedSizeFlag`` 
    
    :param handleFlag: 
    :type handleFlag: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HandleOrigin: NXOpen.Point3d = ...
    """
    Returns or sets  the HandleOrigin
    
    <hr>
    
    Getter Method
    
    Signature ``HandleOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HandleOrigin`` 
    
    :param handleOrogin: 
    :type handleOrogin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HandleRadius: float = ...
    """
    Returns or sets  the HandleRadius
    
    <hr>
    
    Getter Method
    
    Signature ``HandleRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HandleRadius`` 
    
    :param handleRadius: 
    :type handleRadius: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HandleRadiusOffset: float = ...
    """
    Returns or sets  the HandleRadiusOffset
    
    <hr>
    
    Getter Method
    
    Signature ``HandleRadiusOffset`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HandleRadiusOffset`` 
    
    :param radiusOffset: 
    :type radiusOffset: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HandleXAxis: NXOpen.Vector3d = ...
    """
    Returns or sets  the HandleXAxis
    
    <hr>
    
    Getter Method
    
    Signature ``HandleXAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HandleXAxis`` 
    
    :param handleXAxis: 
    :type handleXAxis: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HandleZAxis: NXOpen.Vector3d = ...
    """
    Returns or sets  the HandleZAxis
    
    <hr>
    
    Getter Method
    
    Signature ``HandleZAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HandleZAxis`` 
    
    :param handleZAxis: 
    :type handleZAxis: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LineIncrement: float = ...
    """
    Returns or sets the LineIncrement value.  
    
    Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    Only available when WithScale is set to true.
    
    <hr>
    
    Getter Method
    
    Signature ``LineIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineIncrement`` 
    
    :param lineIncrement: 
    :type lineIncrement: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    MaxInclusive: bool = ...
    """
    Returns or sets  the MaxInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MaxInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxInclusive`` 
    
    :param maxInclusive: 
    :type maxInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumValue: float = ...
    """
    Returns or sets  the MaximumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumValue`` 
    
    :param maxValue: 
    :type maxValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinInclusive: bool = ...
    """
    Returns or sets  the MinInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MinInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinInclusive`` 
    
    :param minInclusive: 
    :type minInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinRadius: float = ...
    """
    Returns or sets  the MinRadius
    
    <hr>
    
    Getter Method
    
    Signature ``MinRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinRadius`` 
    
    :param minRadius: 
    :type minRadius: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    MinimumValue: float = ...
    """
    Returns or sets  the MinimumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumValue`` 
    
    :param minValue: 
    :type minValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PageIncrement: float = ...
    """
    Returns or sets the PageIncrement value.  
    
    Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    Only available when WithScale is set to true.
    
    <hr>
    
    Getter Method
    
    Signature ``PageIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PageIncrement`` 
    
    :param pageIncrement: 
    :type pageIncrement: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowFocusHandle: bool = ...
    """
    Returns or sets  the ShowFocusHandle
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFocusHandle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFocusHandle`` 
    
    :param showFocus: 
    :type showFocus: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowHandle: bool = ...
    """
    Returns or sets  the ShowHandle
    
    <hr>
    
    Getter Method
    
    Signature ``ShowHandle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowHandle`` 
    
    :param showHandle: 
    :type showHandle: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       This call can be safely removed as this is now a no-op.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param pointType: 
    :type pointType: int 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       This call can be safely removed as this is now a no-op.
    
    License requirements: None.
    """
    Units: NXOpen.TaggedObject = ...
    """
    Returns or sets  the Units
    
    <hr>
    
    Getter Method
    
    Signature ``Units`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Units`` 
    
    :param units: 
    :type units: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Value: float = ...
    """
    Returns or sets  the Value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param dimensionValue: 
    :type dimensionValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WithScale: bool = ...
    """
    Returns or sets  the WithScale
    
    <hr>
    
    Getter Method
    
    Signature ``WithScale`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WithScale`` 
    
    :param withScale: 
    :type withScale: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: AngularDimension = ...  # unknown typename


class SelectNode(UIBlock):
    """
    Represents a Select Node block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectModeMembers(self) -> 'list[str]':
        """
        Gets the SelectMode members 
        
        Signature ``GetSelectModeMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectModeAsString: str = ...
    """
    Returns or sets  the SelectMode as string
    
    <hr>
    
    Getter Method
    
    Signature ``SelectModeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectModeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowSelection: bool = ...
    """
    Returns or sets  the Show Selection.  
    
    If true,the graphical selection part of this block is shown.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX11.0.0
       
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowSelection`` 
    
    :param showSelection: 
    :type showSelection: bool 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX11.0.0
       
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SelectNode = ...  # unknown typename


class SelectPartFromList(UIBlock):
    """
    Represents a Select Part From List block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    Null: SelectPartFromList = ...  # unknown typename


class SectionBuilder(UIBlock):
    """
    Represents a Section Builder  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDefaultCurveRulesMembers(self) -> 'list[str]':
        """
        Gets the DefaultCurveRules members 
        
        Signature ``GetDefaultCurveRulesMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AllowConvergentObject: bool = ...
    """
    Returns or sets  the AllowConvergentObject
    
    <hr>
    
    Getter Method
    
    Signature ``AllowConvergentObject`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowConvergentObject`` 
    
    :param allowConvergentObject: 
    :type allowConvergentObject: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    AllowInferredCurveSelection: bool = ...
    """
    Returns or sets  the AllowInferredCurveSelection
    
    <hr>
    
    Getter Method
    
    Signature ``AllowInferredCurveSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowInferredCurveSelection`` 
    
    :param allow: 
    :type allow: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    AllowStopAtIntersectionFollowFillet: bool = ...
    """
    Returns or sets  the AllowStopAtIntersectionFollowFillet
    
    <hr>
    
    Getter Method
    
    Signature ``AllowStopAtIntersectionFollowFillet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowStopAtIntersectionFollowFillet`` 
    
    :param allow: 
    :type allow: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    AngularTolerance: float = ...
    """
    Returns or sets  the AngularTolerance
    
    <hr>
    
    Getter Method
    
    Signature ``AngularTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AngularTolerance`` 
    
    :param tolerance: 
    :type tolerance: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression.  
    
    If true, focus automatically progresses to the next selection block.
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BlendVirtualCurveOverlay: bool = ...
    """
    Returns or sets  the BlendVirtualCurveOverlay
    
    <hr>
    
    Getter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :param blendCurve: 
    :type blendCurve: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ChainWithinFeature: bool = ...
    """
    Returns or sets  the ChainWithinFeature
    
    <hr>
    
    Getter Method
    
    Signature ``ChainWithinFeature`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ChainWithinFeature`` 
    
    :param chainWithinFeature: 
    :type chainWithinFeature: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CurveRules: int = ...
    """
    Returns or sets  the CurveRules
    
    <hr>
    
    Getter Method
    
    Signature ``CurveRules`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurveRules`` 
    
    :param curveRules: 
    :type curveRules: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DefaultCurveRulesAsString: str = ...
    """
    Returns or sets  the DefaultCurveRules as string
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultCurveRulesAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultCurveRulesAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EntityType: int = ...
    """
    Returns or sets  the EntityType
    
    <hr>
    
    Getter Method
    
    Signature ``EntityType`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EntityType`` 
    
    :param entityType: 
    :type entityType: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    FollowFillet: bool = ...
    """
    Returns or sets  the FollowFillet
    
    <hr>
    
    Getter Method
    
    Signature ``FollowFillet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FollowFillet`` 
    
    :param followFillet: 
    :type followFillet: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InferredCurveSelection: bool = ...
    """
    Returns or sets  the InferredCurveSelection
    
    <hr>
    
    Getter Method
    
    Signature ``InferredCurveSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InferredCurveSelection`` 
    
    :param selectInferredCurve: 
    :type selectInferredCurve: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PointOverlay: bool = ...
    """
    Returns or sets  the PointOverlay
    
    <hr>
    
    Getter Method
    
    Signature ``PointOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointOverlay`` 
    
    :param overlay: 
    :type overlay: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowFlowDirectionAndOriginCurve: bool = ...
    """
    Returns or sets  the ShowFlowDirectionAndOriginCurve
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFlowDirectionAndOriginCurve`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFlowDirectionAndOriginCurve`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SmartUpdateOptionAsString: str = ...
    """
    Returns or sets  the update option for points created by the point overlay.  
    
    Acceptable values are:
    
      *  **Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).
      *  **After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.
      *  **After Parent Body</b> The smart object will always update after the last feature on the parent body.
      *  **Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.
    
    <hr>
    
    Getter Method
    
    Signature ``SmartUpdateOptionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SmartUpdateOptionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.1
    
    License requirements: None.
    """
    SnapPointTypesEnabled: int = ...
    """
    Returns or sets  the SnapPointTypesEnabled
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesEnabled`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesEnabled`` 
    
    :param snapPointType: 
    :type snapPointType: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param defaultSnapPointType: 
    :type defaultSnapPointType: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StopAtIntersection: bool = ...
    """
    Returns or sets  the StopAtIntersection
    
    <hr>
    
    Getter Method
    
    Signature ``StopAtIntersection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StopAtIntersection`` 
    
    :param stop: 
    :type stop: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ToolTip: str = ...
    """
    Returns or sets  the ToolTip
    
    <hr>
    
    Getter Method
    
    Signature ``ToolTip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolTip`` 
    
    :param toolTip: 
    :type toolTip: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SectionBuilder = ...  # unknown typename


class FolderSelection(UIBlock):
    """
    Represents Folder Selection With Browse block  
    
    .. versionadded:: NX8.5.0
    """
    Path: str = ...
    """
    Returns or sets  the Path
    
    <hr>
    
    Getter Method
    
    Signature ``Path`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Path`` 
    
    :param path: 
    :type path: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainStringValue: bool = ...
    """
    Returns or sets  the RetainStringValue
    
    <hr>
    
    Getter Method
    
    Signature ``RetainStringValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainStringValue`` 
    
    :param retainStringValue: 
    :type retainStringValue: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: FolderSelection = ...  # unknown typename


class SpecifyPoint(UIBlock):
    """
    Represents a Specify Point block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EnableFacetSelection: bool = ...
    """
    Returns or sets  the EnableFacetSelection
    
    <hr>
    
    Getter Method
    
    Signature ``EnableFacetSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnableFacetSelection`` 
    
    :param enableSelection: 
    :type enableSelection: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Point: NXOpen.Point3d = ...
    """
    Returns or sets  the Point
    
    <hr>
    
    Getter Method
    
    Signature ``Point`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Point`` 
    
    :param point: 
    :type point: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowShortcuts: bool = ...
    """
    Returns or sets  the ShowShortcuts
    
    <hr>
    
    Getter Method
    
    Signature ``ShowShortcuts`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowShortcuts`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesEnabled: int = ...
    """
    Returns or sets  the SnapPointTypesEnabled
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesEnabled`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesEnabled`` 
    
    :param snapTypes: 
    :type snapTypes: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param snapTypesByDefault: 
    :type snapTypesByDefault: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SpecifyPoint = ...  # unknown typename


class SpecifyPlane(UIBlock):
    """
    Represents a Specify Plane block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    CurrentStepStatusAsString: str = ...
    """
    Returns  the string specifying current StepStatus 
    
    <hr>
    
    Getter Method
    
    Signature ``CurrentStepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowShortcuts: bool = ...
    """
    Returns or sets  the ShowShortcuts
    
    <hr>
    
    Getter Method
    
    Signature ``ShowShortcuts`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowShortcuts`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the string specifying the default StepStatus 
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SpecifyPlane = ...  # unknown typename


class SpecifyCSYS(UIBlock):
    """
    Represents a Specify CSYS block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOutputTypeMembers(self) -> 'list[str]':
        """
        Gets the OutputType members 
        
        Signature ``GetOutputTypeMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSmartUpdteOptionMembers(self) -> 'list[str]':
        """
        Gets the SmartUpdateOption members 
        
        Signature ``GetSmartUpdteOptionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        .. deprecated::  NX9.0.1
           Use :py:meth:`BlockStyler.SpecifyCSYS.GetSmartUpdateOptionMembers` instead
        
        License requirements: None.
        """
        ...
    
    
    def GetSmartUpdateOptionMembers(self) -> 'list[str]':
        """
        Gets the SmartUpdateOption members 
        
        Signature ``GetSmartUpdateOptionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    OutputTypeAsString: str = ...
    """
    Returns or sets  the OutputType as string
    
    <hr>
    
    Getter Method
    
    Signature ``OutputTypeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputTypeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowShortcuts: bool = ...
    """
    Returns or sets  the ShowShortcuts
    
    <hr>
    
    Getter Method
    
    Signature ``ShowShortcuts`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowShortcuts`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    SmartUpdateOptionAsString: str = ...
    """
    Returns or sets  the SmartUpdateOption as string
    
    <hr>
    
    Getter Method
    
    Signature ``SmartUpdateOptionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SmartUpdateOptionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX9.0.1
    
    License requirements: None.
    """
    SmartUpdteOptionAsString: str = ...
    """
    Returns or sets  the SmartUpdateOption as string
    
    <hr>
    
    Getter Method
    
    Signature ``SmartUpdteOptionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.1
       Use :py:meth:`BlockStyler.SpecifyCSYS.SmartUpdateOptionAsString` instead
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SmartUpdteOptionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.1
       Use :py:meth:`BlockStyler.SpecifyCSYS.SmartUpdateOptionAsString` instead
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SpecifyCSYS = ...  # unknown typename


class RadiusDimension(UIBlock):
    """
    Represents a Radius Dimension block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout member  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Values to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AdaptiveScaleLimits: bool = ...
    """
    Returns or sets the AdaptiveScaleLimits.  
    
    If true, indicates that the scale should be adaptive.
    
    <hr>
    
    Getter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :param scaleLimits: 
    :type scaleLimits: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ExpressionObject: NXOpen.TaggedObject = ...
    """
    Returns or sets  the ExpressionObject
    
    <hr>
    
    Getter Method
    
    Signature ``ExpressionObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpressionObject`` 
    
    :param expressionObj: 
    :type expressionObj: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Formula: str = ...
    """
    Returns or sets  the Formula
    
    <hr>
    
    Getter Method
    
    Signature ``Formula`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Formula`` 
    
    :param formula: 
    :type formula: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HandleOrientation: NXOpen.Vector3d = ...
    """
    Returns or sets  the HandleOrientation
    
    <hr>
    
    Getter Method
    
    Signature ``HandleOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HandleOrientation`` 
    
    :param orientation: 
    :type orientation: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HandleOrigin: NXOpen.Point3d = ...
    """
    Returns or sets  the HandleOrigin
    
    <hr>
    
    Getter Method
    
    Signature ``HandleOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HandleOrigin`` 
    
    :param handleOrogin: 
    :type handleOrogin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LineIncrement: float = ...
    """
    Returns or sets the LineIncrement value.  
    
    Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
    
    <hr>
    
    Getter Method
    
    Signature ``LineIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineIncrement`` 
    
    :param lineIncrement: 
    :type lineIncrement: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    MaxInclusive: bool = ...
    """
    Returns or sets  the MaxInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MaxInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxInclusive`` 
    
    :param maxInclusive: 
    :type maxInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumValue: float = ...
    """
    Returns or sets  the MaximumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumValue`` 
    
    :param maxValue: 
    :type maxValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinInclusive: bool = ...
    """
    Returns or sets  the MinInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MinInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinInclusive`` 
    
    :param minInclusive: 
    :type minInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinimumValue: float = ...
    """
    Returns or sets  the MinimumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumValue`` 
    
    :param minValue: 
    :type minValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PageIncrement: float = ...
    """
    Returns or sets the PageIncrement value.  
    
    Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
    
    <hr>
    
    Getter Method
    
    Signature ``PageIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PageIncrement`` 
    
    :param pageIncrement: 
    :type pageIncrement: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowFocusHandle: bool = ...
    """
    Returns or sets  the ShowFocusHandle
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFocusHandle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFocusHandle`` 
    
    :param showFocus: 
    :type showFocus: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowHandle: bool = ...
    """
    Returns or sets  the ShowHandle
    
    <hr>
    
    Getter Method
    
    Signature ``ShowHandle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowHandle`` 
    
    :param showHandle: 
    :type showHandle: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       This call can be safely removed as this is now a no-op.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param pointType: 
    :type pointType: int 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       This call can be safely removed as this is now a no-op.
    
    License requirements: None.
    """
    Units: NXOpen.TaggedObject = ...
    """
    Returns or sets  the Units
    
    <hr>
    
    Getter Method
    
    Signature ``Units`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Units`` 
    
    :param units: 
    :type units: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Value: float = ...
    """
    Returns or sets  the Value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param dimensionValue: 
    :type dimensionValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WithScale: bool = ...
    """
    Returns or sets  the WithScale
    
    <hr>
    
    Getter Method
    
    Signature ``WithScale`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WithScale`` 
    
    :param withScale: 
    :type withScale: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: RadiusDimension = ...  # unknown typename


class SuperPoint(UIBlock):
    """
    Represents a Super Point block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDefaultCurveRulesMembers(self) -> 'list[str]':
        """
        Gets the DefaultCurveRules members 
        
        Signature ``GetDefaultCurveRulesMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    AllowConvergentObject: bool = ...
    """
    Returns or sets  the AllowConvergentObject
    
    <hr>
    
    Getter Method
    
    Signature ``AllowConvergentObject`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowConvergentObject`` 
    
    :param allowConvergentObject: 
    :type allowConvergentObject: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BlendVirtualCurveOverlay: bool = ...
    """
    Returns or sets  the BlendVirtualCurveOverlay.  
    
    If true, virtual curve is displayed during preselection.
    
    <hr>
    
    Getter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :param blendCurve: 
    :type blendCurve: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    CurveRules: int = ...
    """
    Returns or sets  the CurveRules
    
    <hr>
    
    Getter Method
    
    Signature ``CurveRules`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurveRules`` 
    
    :param curveRules: 
    :type curveRules: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    DefaultCurveRulesAsString: str = ...
    """
    Returns or sets  the DefaultCurveRules as string
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultCurveRulesAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultCurveRulesAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    EntityType: int = ...
    """
    Returns or sets  the EntityType
    
    <hr>
    
    Getter Method
    
    Signature ``EntityType`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EntityType`` 
    
    :param entityType: 
    :type entityType: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    PointOverlay: bool = ...
    """
    Returns or sets  the PointOverlay
    
    <hr>
    
    Getter Method
    
    Signature ``PointOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointOverlay`` 
    
    :param overlay: 
    :type overlay: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowFlowDirectionAndOriginCurve: bool = ...
    """
    Returns or sets  the ShowFlowDirectionAndOriginCurve
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFlowDirectionAndOriginCurve`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFlowDirectionAndOriginCurve`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    SketchOnPath: bool = ...
    """
    Returns or sets  the SketchOnPath
    
    <hr>
    
    Getter Method
    
    Signature ``SketchOnPath`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SketchOnPath`` 
    
    :param sketchOnPath: 
    :type sketchOnPath: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    SnapPointTypesEnabled: int = ...
    """
    Returns or sets  the SnapPointTypesEnabled
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesEnabled`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesEnabled`` 
    
    :param snapPointType: 
    :type snapPointType: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param defaultSnapPointType: 
    :type defaultSnapPointType: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ToolTip: str = ...
    """
    Returns or sets  the ToolTip
    
    <hr>
    
    Getter Method
    
    Signature ``ToolTip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolTip`` 
    
    :param toolTip: 
    :type toolTip: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SuperPoint = ...  # unknown typename


class Table(UIBlock):
    """
    Represents a Table layout  
    
    .. versionadded:: NX8.5.0
    """
    HasColumnLabels: bool = ...
    """
    Returns or sets  the HasColumnLabels
    
    <hr>
    
    Getter Method
    
    Signature ``HasColumnLabels`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HasColumnLabels`` 
    
    :param hasLables: 
    :type hasLables: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HighQualityBitmap: bool = ...
    """
    Returns or sets  the HighQualityBitmap
    
    <hr>
    
    Getter Method
    
    Signature ``HighQualityBitmap`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HighQualityBitmap`` 
    
    :param highQuality: 
    :type highQuality: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Members: PropertyList = ...
    """
    Returns  the Members
    
    <hr>
    
    Getter Method
    
    Signature ``Members`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BlockStyler.PropertyList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    NumberOfColumns: int = ...
    """
    Returns or sets  the NumberOfColumns
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfColumns`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfColumns`` 
    
    :param numColumn: 
    :type numColumn: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue.  
    
    If true, the block's value will be saved in dialog memory upon OK, Apply or Close.
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: Table = ...  # unknown typename


class PropertyListPropertyTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PropertyListPropertyType():
    """
    Represents the property types.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "String", "String"
       "Double", "Double"
       "Logical", "Logical"
       "Integer", "Integer"
       "Enum", "Enum"
       "Strings", "Strings"
       "UIBlock", "UIBlock"
       "Point", "Point"
       "Vector", "Vector"
       "Bits", "Bits"
       "TaggedObject", "Tagged Object"
       "Array", "Array"
       "IntegerMatrix2d", "Integer 2d-Matrix"
       "DoubleMatrix2d", "Double 2d-Matrix"
       "TaggedObjectMatrix2d", "Tagged Object 2d-Matrix"
       "IntegerVector", "Integer Vector"
       "DoubleVector", "Double Vector"
       "TaggedObjectVector", "Tagged Object Vector"
       "File", "File"
       "SelectionFilter", "Selection Filter"
       "Undefined", "Undefined"
    """
    String = 0  # PropertyListPropertyTypeMemberType
    Double = 1  # PropertyListPropertyTypeMemberType
    Logical = 2  # PropertyListPropertyTypeMemberType
    Integer = 3  # PropertyListPropertyTypeMemberType
    Enum = 4  # PropertyListPropertyTypeMemberType
    Strings = 5  # PropertyListPropertyTypeMemberType
    UIBlock = 6  # PropertyListPropertyTypeMemberType
    Point = 7  # PropertyListPropertyTypeMemberType
    Vector = 8  # PropertyListPropertyTypeMemberType
    Bits = 9  # PropertyListPropertyTypeMemberType
    TaggedObject = 10  # PropertyListPropertyTypeMemberType
    Array = 11  # PropertyListPropertyTypeMemberType
    IntegerMatrix2d = 12  # PropertyListPropertyTypeMemberType
    DoubleMatrix2d = 13  # PropertyListPropertyTypeMemberType
    TaggedObjectMatrix2d = 14  # PropertyListPropertyTypeMemberType
    IntegerVector = 15  # PropertyListPropertyTypeMemberType
    DoubleVector = 16  # PropertyListPropertyTypeMemberType
    TaggedObjectVector = 17  # PropertyListPropertyTypeMemberType
    File = 18  # PropertyListPropertyTypeMemberType
    SelectionFilter = 19  # PropertyListPropertyTypeMemberType
    Undefined = 20  # PropertyListPropertyTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PropertyListListModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PropertyListListMode():
    """
    Indicates whether the properties in the list are named.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Indexed", "The properties are not named and must be indexed through an integer index"
       "Named", "The properties are named"
    """
    Indexed = 0  # PropertyListListModeMemberType
    Named = 1  # PropertyListListModeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PropertyList(NXOpen.TransientObject):
    """
    Represents a list of properties   
    
    .. versionadded:: NX6.0.0
    """
    
    class PropertyType():
        """
        Represents the property types.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "String", "String"
           "Double", "Double"
           "Logical", "Logical"
           "Integer", "Integer"
           "Enum", "Enum"
           "Strings", "Strings"
           "UIBlock", "UIBlock"
           "Point", "Point"
           "Vector", "Vector"
           "Bits", "Bits"
           "TaggedObject", "Tagged Object"
           "Array", "Array"
           "IntegerMatrix2d", "Integer 2d-Matrix"
           "DoubleMatrix2d", "Double 2d-Matrix"
           "TaggedObjectMatrix2d", "Tagged Object 2d-Matrix"
           "IntegerVector", "Integer Vector"
           "DoubleVector", "Double Vector"
           "TaggedObjectVector", "Tagged Object Vector"
           "File", "File"
           "SelectionFilter", "Selection Filter"
           "Undefined", "Undefined"
        """
        String = 0  # PropertyListPropertyTypeMemberType
        Double = 1  # PropertyListPropertyTypeMemberType
        Logical = 2  # PropertyListPropertyTypeMemberType
        Integer = 3  # PropertyListPropertyTypeMemberType
        Enum = 4  # PropertyListPropertyTypeMemberType
        Strings = 5  # PropertyListPropertyTypeMemberType
        UIBlock = 6  # PropertyListPropertyTypeMemberType
        Point = 7  # PropertyListPropertyTypeMemberType
        Vector = 8  # PropertyListPropertyTypeMemberType
        Bits = 9  # PropertyListPropertyTypeMemberType
        TaggedObject = 10  # PropertyListPropertyTypeMemberType
        Array = 11  # PropertyListPropertyTypeMemberType
        IntegerMatrix2d = 12  # PropertyListPropertyTypeMemberType
        DoubleMatrix2d = 13  # PropertyListPropertyTypeMemberType
        TaggedObjectMatrix2d = 14  # PropertyListPropertyTypeMemberType
        IntegerVector = 15  # PropertyListPropertyTypeMemberType
        DoubleVector = 16  # PropertyListPropertyTypeMemberType
        TaggedObjectVector = 17  # PropertyListPropertyTypeMemberType
        File = 18  # PropertyListPropertyTypeMemberType
        SelectionFilter = 19  # PropertyListPropertyTypeMemberType
        Undefined = 20  # PropertyListPropertyTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ListMode():
        """
        Indicates whether the properties in the list are named.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Indexed", "The properties are not named and must be indexed through an integer index"
           "Named", "The properties are named"
        """
        Indexed = 0  # PropertyListListModeMemberType
        Named = 1  # PropertyListListModeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPropertyNames(self) -> 'list[str]':
        """
        Returns a list of all the property names  
        
        Signature ``GetPropertyNames()`` 
        
        :returns: Property names  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetPropertyType(self, propertyName: str) -> PropertyListPropertyType:
        """
        Returns the property type for given property name  
        
        Signature ``GetPropertyType(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Property type.  
        :rtype: :py:class:`NXOpen.BlockStyler.PropertyListPropertyType` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetPropertyType(self, propertyIndex: int) -> PropertyListPropertyType:
        """
        Returns the property type for the Indexed property list. Don't use this method on Named property list  
        
        Signature ``GetPropertyType(propertyIndex)`` 
        
        :param propertyIndex: Index 
        :type propertyIndex: int 
        :returns: Property type.  
        :rtype: :py:class:`NXOpen.BlockStyler.PropertyListPropertyType` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInteger(self, propertyName: str, value: int) -> None:
        """
        Sets the integer value for the given property name.  
        
        Exception will be raised if invalid property name is used.
        
        Signature ``SetInteger(propertyName, value)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param value:  Value to set for given property name 
        :type value: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetInteger(self, propertyName: str) -> int:
        """
        Gets the integer value for the given property name. Exception will be raised if invalid property name is used  
        
        Signature ``GetInteger(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name  
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetInteger(self, propertyIndex: int) -> int:
        """
        Gets the integer value for the given index. Exception will be raised if invalid index is used  
        
        Signature ``GetInteger(propertyIndex)`` 
        
        :param propertyIndex: Index 
        :type propertyIndex: int 
        :returns: Value to get for given index  
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLogical(self, propertyName: str, value: bool) -> None:
        """
        Sets the logical value for the given property name.  
        
        Exception will be raised if invalid property name is used.
        
        Signature ``SetLogical(propertyName, value)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param value: Value to set for given property name.  
        :type value: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetLogical(self, propertyName: str) -> bool:
        """
        Gets the logical value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetLogical(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name. 
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetLogical(self, propertyIndex: int) -> bool:
        """
        Gets the logical value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetLogical(propertyIndex)`` 
        
        :param propertyIndex:  Index  
        :type propertyIndex: int 
        :returns: Value to get for given index. 
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDouble(self, propertyName: str, value: float) -> None:
        """
        Sets the double value for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetDouble(propertyName, value)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param value: Value to set for given property name. 
        :type value: float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetDouble(self, propertyName: str) -> float:
        """
        Gets the double value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetDouble(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name. 
        :rtype: float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetDouble(self, propertyIndex: int) -> float:
        """
        Gets the double value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetDouble(propertyIndex)`` 
        
        :param propertyIndex:  Index 
        :type propertyIndex: int 
        :returns: Value to get for given index. 
        :rtype: float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetString(self, propertyName: str, value: str) -> None:
        """
        Sets the string value for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetString(propertyName, value)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param value: Value to set for given property name.  
        :type value: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetString(self, propertyName: str) -> str:
        """
        Gets the string value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetString(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetString(self, propertyIndex: int) -> str:
        """
        Gets the string value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetString(propertyIndex)`` 
        
        :param propertyIndex:  Index 
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEnumAsString(self, propertyName: str, value: str) -> None:
        """
        Sets the value for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetEnumAsString(propertyName, value)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param value: Value to set for given property name.  
        :type value: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetEnumAsString(self, propertyName: str) -> str:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetEnumAsString(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetEnumAsString(self, propertyIndex: int) -> str:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetEnumAsString(propertyIndex)`` 
        
        :param propertyIndex:  index  
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEnum(self, propertyName: str, value: int) -> None:
        """
        Sets the value for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetEnum(propertyName, value)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param value: Value to set for given property name.  
        :type value: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetEnum(self, propertyName: str) -> int:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetEnum(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetEnum(self, propertyIndex: int) -> int:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetEnum(propertyIndex)`` 
        
        :param propertyIndex:  Index  
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEnumMembers(self, propertyName: str, stringArray: 'list[str]') -> None:
        """
        Sets the enum members for the given property of type enum.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetEnumMembers(propertyName, stringArray)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param stringArray: Value to set for given property name.  
        :type stringArray: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetEnumMembers(self, propertyName: str) -> 'list[str]':
        """
        Gets the enum members for the given property of type enum. Exception will be raised if invalid property name is used.  
        
        Signature ``GetEnumMembers(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetEnumMembers(self, propertyIndex: int) -> 'list[str]':
        """
        Gets the enum members for the given property index. Exception will be raised if invalid property name is used.  
        
        Signature ``GetEnumMembers(propertyIndex)`` 
        
        :param propertyIndex:  Index  
        :type propertyIndex: int 
        :returns: Value to get for given property index.  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetStrings(self, propertyName: str, stringArray: 'list[str]') -> None:
        """
        Sets the strings value for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetStrings(propertyName, stringArray)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param stringArray: Value to set for given property name.  
        :type stringArray: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetStrings(self, propertyName: str) -> 'list[str]':
        """
        Gets the strings value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetStrings(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetStrings(self, propertyIndex: int) -> 'list[str]':
        """
        Gets the strings value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetStrings(propertyIndex)`` 
        
        :param propertyIndex:  Index  
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetUIBlock(self, propertyName: str) -> UIBlock:
        """
        Gets the UI Block for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetUIBlock(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetUIBlock(self, propertyIndex: int) -> UIBlock:
        """
        Gets the UI Block for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetUIBlock(propertyIndex)`` 
        
        :param propertyIndex:  Index  
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPoint(self, propertyName: str, pointSc: NXOpen.Point3d) -> None:
        """
        Sets the point value for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetPoint(propertyName, pointSc)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param pointSc: Value to set for given property name.  
        :type pointSc: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetPoint(self, propertyName: str) -> NXOpen.Point3d:
        """
        Gets the point value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetPoint(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetPoint(self, propertyIndex: int) -> NXOpen.Point3d:
        """
        Gets the point value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetPoint(propertyIndex)`` 
        
        :param propertyIndex: Index  
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetVector(self, propertyName: str, vector: NXOpen.Vector3d) -> None:
        """
        Sets the vector value for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetVector(propertyName, vector)`` 
        
        :param propertyName: Name of the property 
        :type propertyName: str 
        :param vector: Value to set for given property name.   
        :type vector: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetVector(self, propertyName: str) -> NXOpen.Vector3d:
        """
        Gets the vector value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetVector(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetVector(self, propertyIndex: int) -> NXOpen.Vector3d:
        """
        Gets the vector value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetVector(propertyIndex)`` 
        
        :param propertyIndex: Index  
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBits(self, propertyName: str, bitsSc: int) -> None:
        """
        Sets the bits value for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetBits(propertyName, bitsSc)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param bitsSc: Value to set for given property name. 
        :type bitsSc: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetBits(self, propertyName: str) -> int:
        """
        Gets the bits value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetBits(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.   
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetBits(self, propertyIndex: int) -> int:
        """
        Gets the bits value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetBits(propertyIndex)`` 
        
        :param propertyIndex: index  
        :type propertyIndex: int 
        :returns: Value to get for given index.   
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTaggedObject(self, propertyName: str, taggedSc: NXOpen.TaggedObject) -> None:
        """
        Sets the tagged object for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetTaggedObject(propertyName, taggedSc)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param taggedSc: Value to set for given property name.  
        :type taggedSc: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetTaggedObject(self, propertyName: str) -> NXOpen.TaggedObject:
        """
        Gets the tagged object for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetTaggedObject(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetTaggedObject(self, propertyIndex: int) -> NXOpen.TaggedObject:
        """
        Gets the tagged object for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetTaggedObject(propertyIndex)`` 
        
        :param propertyIndex: Index 
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetIntegerVector(self, propertyName: str) -> 'list[int]':
        """
        Gets the integer vector for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetIntegerVector(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: list of int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetIntegerVector(self, propertyIndex: int) -> 'list[int]':
        """
        Gets the integer vector for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetIntegerVector(propertyIndex)`` 
        
        :param propertyIndex: Index 
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: list of int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetIntegerVector(self, propertyName: str, intVector: 'list[int]') -> None:
        """
        Sets the integer vector for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetIntegerVector(propertyName, intVector)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param intVector: Value to set for given property name.  
        :type intVector: list of int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetDoubleVector(self, propertyName: str) -> 'list[float]':
        """
        Gets the double vector for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetDoubleVector(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetDoubleVector(self, propertyIndex: int) -> 'list[float]':
        """
        Gets the double vector for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetDoubleVector(propertyIndex)`` 
        
        :param propertyIndex:  Index 
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDoubleVector(self, propertyName: str, doubleVector: 'list[float]') -> None:
        """
        Sets the double vector for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetDoubleVector(propertyName, doubleVector)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param doubleVector: Value to set for given property name.  
        :type doubleVector: list of float 
        
        .. versionadded:: NX7.5.3
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetTaggedObjectVector(self, propertyName: str) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the tagged object vector for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetTaggedObjectVector(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetTaggedObjectVector(self, propertyIndex: int) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the tagged object vector for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetTaggedObjectVector(propertyIndex)`` 
        
        :param propertyIndex:  Index 
        :type propertyIndex: int 
        :returns: Value to get for given property name.  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTaggedObjectVector(self, propertyName: str, tagVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the tagged object vector for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetTaggedObjectVector(propertyName, tagVector)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param tagVector: Value to set for given property name.  
        :type tagVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetIntegerMatrix(self, propertyName: str) -> tuple:
        """
        Gets the integer matrix for the given property name. Exception will be raised if invalid property name is used.
        This is a two dimensional array encoded into a single array.  
        
        Signature ``GetIntegerMatrix(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (matrixValue, nRows, nColumns). matrixValue is a list of int.  Value to get for given property name. nRows is a int.   Number of Rows in the 2D matrix nColumns is a int.   Number of Columns in the 2D matrix 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetIntegerMatrix(self, propertyIndex: int) -> tuple:
        """
        Gets the integer matrix for the given index. Exception will be raised if invalid index is used.
        This is a two dimensional array encoded into a single array.  
        
        Signature ``GetIntegerMatrix(propertyIndex)`` 
        
        :param propertyIndex:  Index  
        :type propertyIndex: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (matrixValue, nRows, nColumns). matrixValue is a list of int.  Value to get for given index. nRows is a int.   Number of Rows in the 2D matrix nColumns is a int.   Number of Columns in the 2D matrix 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetIntegerMatrix(self, propertyName: str, nRows: int, nColumns: int, matrixValue: 'list[int]') -> None:
        """
        Sets the integer matrix for the given property name.  
        
        Exception will be raised if invalid property name is used.
        This is a two dimensional array encoded into a single array. 
        
        Signature ``SetIntegerMatrix(propertyName, nRows, nColumns, matrixValue)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param nRows:  Number of Rows in the 2D matrix  
        :type nRows: int 
        :param nColumns:  Number of Columns in the 2D matrix  
        :type nColumns: int 
        :param matrixValue: Value to set for given property name.  
        :type matrixValue: list of int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetDoubleMatrix(self, propertyName: str) -> tuple:
        """
        Gets the double matrix for the given property name. Exception will be raised if invalid property name is used.
        This is a two dimensional array encoded into a single array.  
        
        Signature ``GetDoubleMatrix(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (matrixValue, nRows, nColumns). matrixValue is a list of float.  Value to get for given property name. nRows is a int.   Number of Rows in the 2D matrix nColumns is a int.   Number of Columns in the 2D matrix 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetDoubleMatrix(self, propertyIndex: int) -> tuple:
        """
        Gets the double matrix for the given index. Exception will be raised if invalid index is used.
        This is a two dimensional array encoded into a single array.  
        
        Signature ``GetDoubleMatrix(propertyIndex)`` 
        
        :param propertyIndex:  Index  
        :type propertyIndex: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (matrixValue, nRows, nColumns). matrixValue is a list of float.  Value to get for given index. nRows is a int.   Number of Rows in the 2D matrix nColumns is a int.   Number of Columns in the 2D matrix 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDoubleMatrix(self, propertyName: str, nRows: int, nColumns: int, matrixValue: 'list[float]') -> None:
        """
        Sets the double matrix for the given property name.  
        
        Exception will be raised if invalid property name is used.
        This is a two dimensional array encoded into a single array. 
        
        Signature ``SetDoubleMatrix(propertyName, nRows, nColumns, matrixValue)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param nRows:  Number of Rows in the 2D matrix  
        :type nRows: int 
        :param nColumns:  Number of Columns in the 2D matrix  
        :type nColumns: int 
        :param matrixValue: Value to set for given property name.  
        :type matrixValue: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetFile(self, propertyName: str) -> str:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetFile(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetFile(self, propertyIndex: int) -> str:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetFile(propertyIndex)`` 
        
        :param propertyIndex:  Index  
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFile(self, propertyName: str, value: str) -> None:
        """
        Sets the value for the given property name.  
        
        Exception will be raised if invalid property name is used. 
        
        Signature ``SetFile(propertyName, value)`` 
        
        :param propertyName:  Name of the property  
        :type propertyName: str 
        :param value: Value to set for given property name.  
        :type value: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetArray(self, propertyName: str) -> PropertyList:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used.  
        
        Signature ``GetArray(propertyName)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :returns: Value to get for given property name.  
        :rtype: :py:class:`NXOpen.BlockStyler.PropertyList` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetArray(self, propertyIndex: int) -> PropertyList:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used.  
        
        Signature ``GetArray(propertyIndex)`` 
        
        :param propertyIndex:  Index  
        :type propertyIndex: int 
        :returns: Value to get for given index.  
        :rtype: :py:class:`NXOpen.BlockStyler.PropertyList` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectionFilter(self, propertyName: str, maskAction: NXOpen.SelectionSelectionAction, maskTriples: 'list[NXOpen.SelectionMaskTriple_Struct]') -> None:
        """
        Sets the filter for the given property name.  
        
        Signature ``SetSelectionFilter(propertyName, maskAction, maskTriples)`` 
        
        :param propertyName: Name of the property  
        :type propertyName: str 
        :param maskAction:  Mask action  
        :type maskAction: :py:class:`NXOpen.SelectionSelectionAction` 
        :param maskTriples:  Mask triples  
        :type maskTriples: list of :py:class:`NXOpen.SelectionMaskTriple_Struct` 
        
        .. versionadded:: NX6.0.0
        
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
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Mode: PropertyListListMode = ...
    """
    Returns  the mode of the list.  
    
    <hr>
    
    Getter Method
    
    Signature ``Mode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BlockStyler.PropertyListListMode` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """


class Label(UIBlock):
    """
    Represents a Label  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Values to get from the property  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param tooltipText: 
    :type tooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DisplayBitmapLabel: bool = ...
    """
    Returns or sets  the DisplayBitmapLabel
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayBitmapLabel`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayBitmapLabel`` 
    
    :param display: 
    :type display: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HighQualityBitmap: bool = ...
    """
    Returns or sets  the HighQualityBitmap
    
    <hr>
    
    Getter Method
    
    Signature ``HighQualityBitmap`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HighQualityBitmap`` 
    
    :param highQuality: 
    :type highQuality: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize.  
    
    If true, translates the Label string into the current locale language.
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Tooltip: str = ...
    """
    Returns or sets  the Tooltip
    
    <hr>
    
    Getter Method
    
    Signature ``Tooltip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Tooltip`` 
    
    :param tooltipString: 
    :type tooltipString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WordWrap: bool = ...
    """
    Returns or sets  the WordWrap
    
    <hr>
    
    Getter Method
    
    Signature ``WordWrap`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WordWrap`` 
    
    :param wordwrap: 
    :type wordwrap: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: Label = ...  # unknown typename


class MultilineString(UIBlock):
    """
    Represents a Multiline String block   
    
    .. versionadded:: NX6.0.0
    """
    
    def GetValue(self) -> 'list[str]':
        """
        Gets the Value 
        
        Signature ``GetValue()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValue(self, valueString: 'list[str]') -> None:
        """
        Sets the Value
        
        Signature ``SetValue(valueString)`` 
        
        :param valueString: 
        :type valueString: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    Height: int = ...
    """
    Returns or sets  the Height
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Height`` 
    
    :param height: 
    :type height: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize.  
    
    If true, the Label is translated to current locale language
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumCharactersAccepted: int = ...
    """
    Returns or sets  the MaximumCharactersAccepted
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumCharactersAccepted`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumCharactersAccepted`` 
    
    :param maxChar: 
    :type maxChar: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumHeight: int = ...
    """
    Returns or sets  the MaximumHeight
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumHeight`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumHeight`` 
    
    :param maxHeight: 
    :type maxHeight: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinimumHeight: int = ...
    """
    Returns or sets  the MinimumHeight
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumHeight`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumHeight`` 
    
    :param minHeight: 
    :type minHeight: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ResizeHeightWithDialog: bool = ...
    """
    Returns or sets  the ResizeHeightWithDialog.  
    
    If true, height of block will dynamically change when the dialog is resized.
    
    <hr>
    
    Getter Method
    
    Signature ``ResizeHeightWithDialog`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ResizeHeightWithDialog`` 
    
    :param resize: 
    :type resize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ValuesConcatenated: str = ...
    """
    Returns or sets  the ValuesConcatenated.  
    
    Represents single string with values in block concatenated with new-line characters.
    
    <hr>
    
    Getter Method
    
    Signature ``ValuesConcatenated`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValuesConcatenated`` 
    
    :param valueString: 
    :type valueString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Width: int = ...
    """
    Returns or sets  the Width
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param width: 
    :type width: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: MultilineString = ...  # unknown typename


class Enumeration(UIBlock):
    """
    Represents an Enumeration block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipImages(self) -> 'list[str]':
        """
        Gets the BalloonTooltipImages 
        
        Signature ``GetBalloonTooltipImages()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBalloonTooltipImages(self, imageStrings: 'list[str]') -> None:
        """
        Sets the BalloonTooltipImages
        
        Signature ``SetBalloonTooltipImages(imageStrings)`` 
        
        :param imageStrings: 
        :type imageStrings: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBalloonTooltipTexts(self) -> 'list[str]':
        """
        Gets the BalloonTooltipTexts 
        
        Signature ``GetBalloonTooltipTexts()`` 
        
        :returns: Value to get from the property  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBalloonTooltipTexts(self, tooltipTextArray: 'list[str]') -> None:
        """
        Sets the BalloonTooltipTexts
        
        Signature ``SetBalloonTooltipTexts(tooltipTextArray)`` 
        
        :param tooltipTextArray: Value to set for the property.  
        :type tooltipTextArray: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBitmaps(self) -> 'list[str]':
        """
        Gets the Bitmaps 
        
        Signature ``GetBitmaps()`` 
        
        :returns: Value to get for the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBitmaps(self, bitmapsStrings: 'list[str]') -> None:
        """
        Sets the Bitmaps
        
        Signature ``SetBitmaps(bitmapsStrings)`` 
        
        :param bitmapsStrings: Value to set for the property.  
        :type bitmapsStrings: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetEnumSensitivity(self) -> 'list[int]':
        """
        Gets EnumSensitivity 
        
        Signature ``GetEnumSensitivity()`` 
        
        :returns:  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is sensitive otherwise it is insensitive.  
        :rtype: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEnumSensitivity(self, valueVector: 'list[int]') -> None:
        """
        Sets EnumSensitivity
        
        Signature ``SetEnumSensitivity(valueVector)`` 
        
        :param valueVector:  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is sensitive otherwise it is insensitive.  
        :type valueVector: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetEnumVisibility(self) -> 'list[int]':
        """
        Gets EnumVisibility 
        
        Signature ``GetEnumVisibility()`` 
        
        :returns:  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is visible otherwise it is hidden.  
        :rtype: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEnumVisibility(self, valueVector: 'list[int]') -> None:
        """
        Sets EnumVisibility
        
        Signature ``SetEnumVisibility(valueVector)`` 
        
        :param valueVector:  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is visible otherwise it is hidden.  
        :type valueVector: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInitialShortcuts(self) -> 'list[int]':
        """
        Gets InitialShortcuts.  
        
        Specifies the set of shortcuts that are displayed when the dialog is initially shown. Valid only if AllowShortcuts property is true.  
        
        Signature ``GetInitialShortcuts()`` 
        
        :returns:  Array of integers with length between 0 and N-1, where N is the number of enumeration options  
        :rtype: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInitialShortcuts(self, valueVector: 'list[int]') -> None:
        """
        Sets InitialShortcuts.  
        
        Specifies the set of shortcuts that are displayed when the dialog is initially shown. Valid only if AllowShortcuts property is true.
        
        Signature ``SetInitialShortcuts(valueVector)`` 
        
        :param valueVector:  Array of integers with length between 0 and N-1, where N is the number of enumeration options  
        :type valueVector: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLayoutMembers(self) -> 'list[str]':
        """
        Gets the Layout members  
        
        Signature ``GetLayoutMembers()`` 
        
        :returns: Value to get from the property  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPresentationStyleMembers(self) -> 'list[str]':
        """
        Gets the PresentationStyle members  
        
        Signature ``GetPresentationStyleMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetEnumMembers(self) -> 'list[str]':
        """
        Gets the Enum members.  
        
        Signature ``GetEnumMembers()`` 
        
        :returns: Array of member names 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEnumMembers(self, memberStrings: 'list[str]') -> None:
        """
        Sets the Enum members.  
        
        Signature ``SetEnumMembers(memberStrings)`` 
        
        :param memberStrings: Array of member names 
        :type memberStrings: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AllowShortcuts: bool = ...
    """
    Returns or sets  the AllowShortcuts.  
    
    If true, the 'Show Shortcuts' option is available.
    
    <hr>
    
    Getter Method
    
    Signature ``AllowShortcuts`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowShortcuts`` 
    
    :param allow: 
    :type allow: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BorderVisibility: bool = ...
    """
    Returns or sets  the BorderVisibility
    
    <hr>
    
    Getter Method
    
    Signature ``BorderVisibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BorderVisibility`` 
    
    :param visibility: 
    :type visibility: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HighQualityBitmap: bool = ...
    """
    Returns or sets  the HighQualityBitmap
    
    <hr>
    
    Getter Method
    
    Signature ``HighQualityBitmap`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HighQualityBitmap`` 
    
    :param highQuality: 
    :type highQuality: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IconsOnly: bool = ...
    """
    Returns or sets  the IconsOnly.  
    
    If true, the enumeration options are shown as bitmaps only 
    
    <hr>
    
    Getter Method
    
    Signature ``IconsOnly`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IconsOnly`` 
    
    :param iconsOnly: 
    :type iconsOnly: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelVisibility: bool = ...
    """
    Returns or sets  the LabelVisibility
    
    <hr>
    
    Getter Method
    
    Signature ``LabelVisibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelVisibility`` 
    
    :param visibility: 
    :type visibility: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LayoutAsString: str = ...
    """
    Returns or sets  the Layout as string
    
    <hr>
    
    Getter Method
    
    Signature ``LayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize.  
    
    If true, the Label is translated to current locale language.
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    NumberOfColumns: int = ...
    """
    Returns or sets  the NumberOfColumns
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfColumns`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfColumns`` 
    
    :param numColumn: 
    :type numColumn: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PackedColumns: bool = ...
    """
    Returns or sets  the PackedColumns.  
    
    If true, each column takes up as much space as required for labels in that column. If false,
    the longest label amongst all options dictates the width of all columns.
    
    <hr>
    
    Getter Method
    
    Signature ``PackedColumns`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PackedColumns`` 
    
    :param packedColumns: 
    :type packedColumns: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PresentationStyleAsString: str = ...
    """
    Returns or sets  the PresentationStyle as string
    
    <hr>
    
    Getter Method
    
    Signature ``PresentationStyleAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PresentationStyleAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ValueAsString: str = ...
    """
    Returns or sets  the Value as string.  
    
    Represents the currently selected option of enum.
    
    <hr>
    
    Getter Method
    
    Signature ``ValueAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValueAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: Enumeration = ...  # unknown typename


class RGBColorPicker(UIBlock):
    """
    Represents a RGB Color Picker block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout member  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Values to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param tooltipText: 
    :type tooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize.  
    
    If true, the Label is translated to current locale language.
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue.  
    
    If true, the block's value will be saved in dialog memory upon OK, Apply or Close.
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Value: int = ...
    """
    Returns or sets  the Value
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param rgbValue: 
    :type rgbValue: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: RGBColorPicker = ...  # unknown typename


class DoubleTable(UIBlock):
    """
    Represents a Double Table block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetMaximumValues(self) -> tuple:
        """
        Gets the MaximumValues 
        
        Signature ``GetMaximumValues()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (matrixValue, nRows, nColumns). matrixValue is a list of float.  Value to get from the property. nRows is a int.   Number of Rows in the 2D matrix nColumns is a int.   Number of Columns in the 2D matrix 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMaximumValues(self, nRows: int, nColumns: int, matrixValue: 'list[float]') -> None:
        """
        Sets the MaximumValues
        
        Signature ``SetMaximumValues(nRows, nColumns, matrixValue)`` 
        
        :param nRows:  Number of Rows in the 2D matrix  
        :type nRows: int 
        :param nColumns:  Number of Columns in the 2D matrix  
        :type nColumns: int 
        :param matrixValue: Value to set to the property  
        :type matrixValue: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetMinimumValues(self) -> tuple:
        """
        Gets the MinimumValues 
        
        Signature ``GetMinimumValues()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (matrixValue, nRows, nColumns). matrixValue is a list of float.  Value to get from the property nRows is a int.   Number of Rows in the 2D matrix nColumns is a int.   Number of Columns in the 2D matrix 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMinimumValues(self, nRows: int, nColumns: int, matrixValue: 'list[float]') -> None:
        """
        Sets the MinimumValues
        
        Signature ``SetMinimumValues(nRows, nColumns, matrixValue)`` 
        
        :param nRows:  Number of Rows in the 2D matrix  
        :type nRows: int 
        :param nColumns:  Number of Columns in the 2D matrix  
        :type nColumns: int 
        :param matrixValue: Value to set for given property.  
        :type matrixValue: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetValues(self) -> tuple:
        """
        Gets the Values in table 
        
        Signature ``GetValues()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (matrixValue, nRows, nColumns). matrixValue is a list of float.  Value to get from the property. nRows is a int.   Number of Rows in the 2D matrix nColumns is a int.   Number of Columns in the 2D matrix 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValues(self, nRows: int, nColumns: int, matrixValue: 'list[float]') -> None:
        """
        Sets the Values in table
        
        Signature ``SetValues(nRows, nColumns, matrixValue)`` 
        
        :param nRows:  Number of Rows in the 2D matrix  
        :type nRows: int 
        :param nColumns:  Number of Columns in the 2D matrix  
        :type nColumns: int 
        :param matrixValue: Value to set for the property.  
        :type matrixValue: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRowTitles(self) -> 'list[str]':
        """
        Gets the titles of rows in table 
        
        Signature ``GetRowTitles()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRowTitles(self, rowTitle: 'list[str]') -> None:
        """
        Sets the titles of rows in table
        
        Signature ``SetRowTitles(rowTitle)`` 
        
        :param rowTitle: Value to set for the property.  
        :type rowTitle: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    CellWidth: int = ...
    """
    Returns or sets  the CellWidth
    
    <hr>
    
    Getter Method
    
    Signature ``CellWidth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CellWidth`` 
    
    :param cellWidth: 
    :type cellWidth: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ColumnTitles: str = ...
    """
    Returns or sets  the ColumnTitles
    
    <hr>
    
    Getter Method
    
    Signature ``ColumnTitles`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColumnTitles`` 
    
    :param title: 
    :type title: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Increment: float = ...
    """
    Returns or sets  the Increment.  
    
    Use this property only when Spin is true
    
    <hr>
    
    Getter Method
    
    Signature ``Increment`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Increment`` 
    
    :param increment: 
    :type increment: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue.  
    
    If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close. 
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Spin: bool = ...
    """
    Returns or sets  the Spin
    
    <hr>
    
    Getter Method
    
    Signature ``Spin`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Spin`` 
    
    :param spin: 
    :type spin: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WrapSpin: bool = ...
    """
    Returns or sets  the WrapSpin.  
    
    Use this property only when Spin is true
    
    <hr>
    
    Getter Method
    
    Signature ``WrapSpin`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WrapSpin`` 
    
    :param wrapSpin: 
    :type wrapSpin: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: DoubleTable = ...  # unknown typename


class CompositeBlock(UIBlock):
    """
    A composite block is a block that contains other blocks   
    
    .. versionadded:: NX6.0.0
    """
    
    def FindBlock(self, blockName: str) -> UIBlock:
        """
        Finds a block contained in the composite block.  
        
        Throws an exception if block not present 
        
        Signature ``FindBlock(blockName)`` 
        
        :param blockName:  Block name  
        :type blockName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBlocks(self) -> 'list[UIBlock]':
        """
        Gets all the blocks available in the composite block  
        
        Signature ``GetBlocks()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDialogSizingMembers(self) -> 'list[str]':
        """
        Gets the Dialog Sizing members 
        
        Signature ``GetDialogSizingMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNavigationStyleMembers(self) -> 'list[str]':
        """
        Gets the Navigation Style members 
        
        Signature ``GetNavigationStyleMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DialogSizing: int = ...
    """
    Returns or sets  the Dialog Sizing
    
    <hr>
    
    Getter Method
    
    Signature ``DialogSizing`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DialogSizing`` 
    
    :param enumIndex: 
    :type enumIndex: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DialogSizingAsString: str = ...
    """
    Returns or sets  the Dialog Sizing as string
    
    <hr>
    
    Getter Method
    
    Signature ``DialogSizingAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DialogSizingAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LastUpdated: UIBlock = ...
    """
    Returns  the block contained in the composite block that was last updated.  
    
    For example, if the CompositeBlock is an item contained in a SetList and
    your update handler is notified that the CompositeBlock has been updated,
    this method returns which block inside the CompositeBlock has been updated. 
    
    <hr>
    
    Getter Method
    
    Signature ``LastUpdated`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BlockStyler.UIBlock` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    NavigationStyle: int = ...
    """
    Returns  the Navigation Style
    
    <hr>
    
    Getter Method
    
    Signature ``NavigationStyle`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    NavigationStyleAsString: str = ...
    """
    Returns  the Navigation Style as string
    
    <hr>
    
    Getter Method
    
    Signature ``NavigationStyleAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: CompositeBlock = ...  # unknown typename


class TabControl(UIBlock):
    """
    Represents a Tab Control layout  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetHiddenTabPages(self) -> 'list[int]':
        """
        Gets the HiddenTabPages.  
        
        This method returns an integer array of the HiddenTabPages.
        If the number of Tab Pages defined is 5 for a Tab Control, they will be indexed 0 to 4. If the first
        and third Tab Pages are hidden, the result returned will be [ 0, -1, 2, -1, -1 ]. Any negative integer
        value will show the Tab Page, using -1 simply to demonstrate. 
        
        Signature ``GetHiddenTabPages()`` 
        
        :returns: 
        :rtype: list of int 
        
        .. versionadded:: NX10.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetHiddenTabPages(self, hiddenTabs: 'list[int]') -> None:
        """
        Sets the HiddenTabPages entered.  
        
        If the number of Tab Pages defined is 5 for a Tab Control,
        they will be indexed 0 to 4. Entering an array of [ 0, -1, 2, -1, -1 ] will result in the first and third
        Tab Pages being hidden. Any negative integer value will show the Tab Page, using -1 simply to demonstrate.
        
        Signature ``SetHiddenTabPages(hiddenTabs)`` 
        
        :param hiddenTabs: Array of Tab Pages defined. To hide a Tab Page, value entered has to map directly to the index being set. 
        :type hiddenTabs: list of int 
        
        .. versionadded:: NX10.0.1
        
        License requirements: None.
        """
        ...
    
    ActivePage: int = ...
    """
    Returns or sets  the ActivePage
    
    <hr>
    
    Getter Method
    
    Signature ``ActivePage`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ActivePage`` 
    
    :param pageIndex: 
    :type pageIndex: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HighQualityBitmap: bool = ...
    """
    Returns or sets  the HighQualityBitmap
    
    <hr>
    
    Getter Method
    
    Signature ``HighQualityBitmap`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HighQualityBitmap`` 
    
    :param highQuality: 
    :type highQuality: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Members: PropertyList = ...
    """
    Returns  the Members
    
    <hr>
    
    Getter Method
    
    Signature ``Members`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BlockStyler.PropertyList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    TabsPerRow: int = ...
    """
    Returns or sets  the TabsPerRow
    
    <hr>
    
    Getter Method
    
    Signature ``TabsPerRow`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TabsPerRow`` 
    
    :param numTabs: 
    :type numTabs: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: TabControl = ...  # unknown typename


class FileSelection(UIBlock):
    """
    Represents File Selection With Browse block  
    
    .. versionadded:: NX8.5.0
    """
    Filter: str = ...
    """
    Returns or sets  the Filter
    Format of the filter string, for a group of related filter extensions will be "Group 1(*.  
    
    xxx;*.yyy;*.zzz),Group 2(*.aaa;*.bbb)" e.g."EPLAN files(*.emp;*.ema;*.ems),Simulation Files(*.sim;*.fem)".
    For the individual filter extensions ".xxx,.yyy,.zzz" e.g. ".prt,.fem,.sim" will appear as "prt File (*.prt)","sim File (*.sim)" and "fem File (*.fem)" respectively in the "Files of type" of file open dialog.
    
    <hr>
    
    Getter Method
    
    Signature ``Filter`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Filter`` 
    
    :param filterString: 
    :type filterString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Path: str = ...
    """
    Returns or sets  the Path
    
    <hr>
    
    Getter Method
    
    Signature ``Path`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Path`` 
    
    :param path: 
    :type path: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainStringValue: bool = ...
    """
    Returns or sets  the RetainStringValue
    
    <hr>
    
    Getter Method
    
    Signature ``RetainStringValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainStringValue`` 
    
    :param retainStringValue: 
    :type retainStringValue: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: FileSelection = ...  # unknown typename


class Separator(UIBlock):
    """
    Represents a Separator block  
    
    .. versionadded:: NX8.5.0
    """
    Null: Separator = ...  # unknown typename


class SelectFacetRegion(UIBlock):
    """
    Represents a Select Region Selection block  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedFacetRegions 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedFacetRegions
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLastDeselectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the LastDeselectedFacetRegions 
        
        Signature ``GetLastDeselectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLastSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the LastSelectedFacetRegions 
        
        Signature ``GetLastSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    EnabledFacetCollectionRules: int = ...
    """
    Returns or sets 
    these are the selection intent rules enabled for the facet selection region block 
    
    It returns the following bit values,
    
      #.  0x1 if only Single Facet rule is enabled,
      #.  0x2 if only Face Facets rule is enabled,
      #.  0x3 if only Flood Fill rule is enabled,
      #.  0x4 if only Color Region rule is enabled
    
    <hr>
    
    Getter Method
    
    Signature ``EnabledFacetCollectionRules`` 
    
    :returns: bit value specifying enabled facet selection rules  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnabledFacetCollectionRules`` 
    
    :param rulesEnabled: bit value specifying enabled facet selection rules  
    :type rulesEnabled: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FacetCollector: NXOpen.FacetCollector = ...
    """
    Returns or sets 
    the owning facet collector is an object of class :py:class:`FacetCollector` that holds collected facets of the block
    
    <hr>
    
    Getter Method
    
    Signature ``FacetCollector`` 
    
    :returns:  the facet collector object holding collection of the block  
    :rtype: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FacetCollector`` 
    
    :param facetCollector:  the facet collector object holding collection of the block  
    :type facetCollector: :py:class:`NXOpen.FacetCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SelectedFacetCollectionRule: int = ...
    """
    Returns or sets  the active facet collection rule
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedFacetCollectionRule`` 
    
    :returns: value specifying selected facet selection rule  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectedFacetCollectionRule`` 
    
    :param selectedRule: bit value specifying selected facet selection rule  
    :type selectedRule: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SupportedFacetTypes: int = ...
    """
    Returns or sets 
    these are type of facets enabled in filters for select facet region block 
    
    It returns following bits,
    
      #.  0x1 if only convergent facets are enabled,
      #.  0x2 if only NX facets are enabled,
      #.  0x3 if both convergent as well as NX facets are enabled.
    
    <hr>
    
    Getter Method
    
    Signature ``SupportedFacetTypes`` 
    
    :returns: bit value specifying the desired types of facets to enable in filter  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SupportedFacetTypes`` 
    
    :param typesEnabled: bit value specifying the desired types of facets to enable in filter  
    :type typesEnabled: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ToolTip: str = ...
    """
    Returns or sets  the ToolTip
    
    <hr>
    
    Getter Method
    
    Signature ``ToolTip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolTip`` 
    
    :param toolTip: 
    :type toolTip: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: SelectFacetRegion = ...  # unknown typename


class DrawingArea(UIBlock):
    """
    Represents a Drawing Area block  
    
    .. versionadded:: NX8.5.0
    """
    Height: int = ...
    """
    Returns or sets  the Height
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Height`` 
    
    :param height: 
    :type height: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Image: str = ...
    """
    Returns or sets  the Image
    
    <hr>
    
    Getter Method
    
    Signature ``Image`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Image`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Width: int = ...
    """
    Returns or sets  the Width
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param width: 
    :type width: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: DrawingArea = ...  # unknown typename


class ExpressionBlock(UIBlock):
    """
    Represents an Expression block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property. 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDimensionalityMembers(self) -> 'list[str]':
        """
        Gets the members of Dimensionality enum.  
        
        Signature ``GetDimensionalityMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AdaptiveScaleLimits: bool = ...
    """
    Returns or sets the AdaptiveScaleLimits.  
    
    If true, indicates that the scale should be adaptive.
    
    <hr>
    
    Getter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :param scaleLimits: 
    :type scaleLimits: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DimensionalityAsString: str = ...
    """
    Returns or sets  the  Dimensionality as string.  
    
    It specifies the type of quantity that the expression represents.
    
    <hr>
    
    Getter Method
    
    Signature ``DimensionalityAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DimensionalityAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ExpressionObject: NXOpen.TaggedObject = ...
    """
    Returns or sets  the ExpressionObject
    
    <hr>
    
    Getter Method
    
    Signature ``ExpressionObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpressionObject`` 
    
    :param expressionObject: 
    :type expressionObject: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Formula: str = ...
    """
    Returns or sets  the Formula for the expression
    
    <hr>
    
    Getter Method
    
    Signature ``Formula`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Formula`` 
    
    :param formulaString: 
    :type formulaString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HasUnitsMenu: bool = ...
    """
    Returns or sets  the HasUnitsMenu.  
    
    If true, indicates that a menu will be displayed allowing the user to change units.
    This property is relevant only when the Dimensionality property is set to a value that is not without units.
    
    <hr>
    
    Getter Method
    
    Signature ``HasUnitsMenu`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HasUnitsMenu`` 
    
    :param hasMenu: 
    :type hasMenu: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LineIncrement: float = ...
    """
    Returns or sets the LineIncrement value.  
    
    Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
    
    <hr>
    
    Getter Method
    
    Signature ``LineIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineIncrement`` 
    
    :param lineIncrement: 
    :type lineIncrement: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    MaxInclusive: bool = ...
    """
    Returns or sets  the MaxInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MaxInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxInclusive`` 
    
    :param maxInclusive: 
    :type maxInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumValue: float = ...
    """
    Returns or sets  the MaximumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumValue`` 
    
    :param maxValue: 
    :type maxValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinInclusive: bool = ...
    """
    Returns or sets  the MinInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MinInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinInclusive`` 
    
    :param minInclusive: 
    :type minInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinimumValue: float = ...
    """
    Returns or sets  the MinimumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumValue`` 
    
    :param minValue: 
    :type minValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PageIncrement: float = ...
    """
    Returns or sets the PageIncrement value.  
    
    Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
    
    <hr>
    
    Getter Method
    
    Signature ``PageIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PageIncrement`` 
    
    :param pageIncrement: 
    :type pageIncrement: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue.  
    
    If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close. 
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Units: NXOpen.TaggedObject = ...
    """
    Returns or sets  the Units for the expression 
    
    <hr>
    
    Getter Method
    
    Signature ``Units`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Units`` 
    
    :param units: 
    :type units: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Value: float = ...
    """
    Returns or sets  the Value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param expressionValue: 
    :type expressionValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WithScale: bool = ...
    """
    Returns or sets  the WithScale.  
    
    If true, the slider bar is shown.
    
    <hr>
    
    Getter Method
    
    Signature ``WithScale`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WithScale`` 
    
    :param withScale: 
    :type withScale: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: ExpressionBlock = ...  # unknown typename


class BlockDialogDialogModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BlockDialogDialogMode():
    """
    Datatype containing options for showing the dialog 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Create", "When the user presses Ok or Apply on the dialog, the user's inputs are saved in dialog memory and the next time that the dialog is shown in Create mode, the dialog is initialized using the user's previous inputs."
       "Edit", "The Apply button is not shown. The user's inputs are not saved in dialog memory and the dialog is not initialized with the user's previous inputs."
    """
    Create = 0  # BlockDialogDialogModeMemberType
    Edit = 1  # BlockDialogDialogModeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BlockDialog(NXOpen.TransientObject):
    """
    Represents a Dialog   
    
    .. versionadded:: NX6.0.0
    """
    
    class DialogMode():
        """
        Datatype containing options for showing the dialog 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Create", "When the user presses Ok or Apply on the dialog, the user's inputs are saved in dialog memory and the next time that the dialog is shown in Create mode, the dialog is initialized using the user's previous inputs."
           "Edit", "The Apply button is not shown. The user's inputs are not saved in dialog memory and the dialog is not initialized with the user's previous inputs."
        """
        Create = 0  # BlockDialogDialogModeMemberType
        Edit = 1  # BlockDialogDialogModeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def AddUpdateHandler(self, cb: typing.Callable) -> None:
        """
        Adds Update callback handler to the dialog.  
        
        Signature ``AddUpdateHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddEnableOKButtonHandler(self, cb: typing.Callable) -> None:
        """
        Adds enable-ok-button callback handler to the dialog.  
        
        Signature ``AddEnableOKButtonHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.3
        
        License requirements: None.
        """
        ...
    
    
    def AddFilterHandler(self, cb: typing.Callable) -> None:
        """
        Adds Filter callback handler to the dialog.  
        
        Signature ``AddFilterHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddOkHandler(self, okCb: typing.Callable) -> None:
        """
        Adds Ok callback handler to the dialog.  
        
        Signature ``AddOkHandler(okCb)`` 
        
        :param okCb: 
        :type okCb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddApplyHandler(self, applyCb: typing.Callable) -> None:
        """
        Adds Apply callback handler to the dialog.  
        
        Signature ``AddApplyHandler(applyCb)`` 
        
        :param applyCb: 
        :type applyCb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddCancelHandler(self, cancelCb: typing.Callable) -> None:
        """
        Adds Cancel callback handler to the dialog.  
        
        Signature ``AddCancelHandler(cancelCb)`` 
        
        :param cancelCb: 
        :type cancelCb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddCloseHandler(self, closeCb: typing.Callable) -> None:
        """
        Adds Close callback handler to the dialog.  
        
        Signature ``AddCloseHandler(closeCb)`` 
        
        :param closeCb: 
        :type closeCb: CallableObject 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AddInitializeHandler(self, cb: typing.Callable) -> None:
        """
        Adds Initialize callback handler to the dialog.  
        
        The callback function is called while the dialog is being initialized.  The callback is called before applying any user inputs saved in dialog memory.
        
        Signature ``AddInitializeHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddDialogShownHandler(self, cb: typing.Callable) -> None:
        """
        Adds Dialog Shown callback handler to the dialog.  
        
        The callback function is called before the dialog is shown.  The callback can be used to overwrite 
        changes that are made during dialog initialization when user inputs saved in dialog memory are applied to the dialog.
        
        Signature ``AddDialogShownHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Show(self) -> NXOpen.SelectionResponse:
        """
        Shows the dialog in :py:class:`BlockStyler.BlockDialogDialogMode.Create <BlockStyler.BlockDialogDialogMode>` mode.  This method will not return until the dialog is closed, 
        which typically is when the dialog's OK or Cancel button is pressed. 
        
        Signature ``Show()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.SelectionResponse` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Show(self, dialogMode: BlockDialogDialogMode) -> NXOpen.SelectionResponse:
        """
        Shows the dialog based upon the mode specified in 
        :py:class:`BlockStyler.BlockDialogDialogMode`.
        This method will not return until the dialog is closed, which typically is when the dialog's OK or Cancel button is pressed.  
        
        Signature ``Show(dialogMode)`` 
        
        :param dialogMode: Dialog mode as Create or Edit. :py:class:`BlockStyler.BlockDialogDialogMode`  
        :type dialogMode: :py:class:`NXOpen.BlockStyler.BlockDialogDialogMode` 
        :returns: 
        :rtype: :py:class:`NXOpen.SelectionResponse` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PerformApply(self) -> None:
        """
        Performs an Apply and restarts the dialog.  
        
        This invokes the apply callback on the dialog.  This method is meant to be called
        when the dialog is shown and while inside the update callback.
        
        Signature ``PerformApply()`` 
        
        .. versionadded:: NX6.0.0
        
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
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddFocusNotifyHandler(self, cb: typing.Callable) -> None:
        """
        Adds focus notify callback handler to the dialog.  
        
        Signature ``AddFocusNotifyHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.2
        
        License requirements: None.
        """
        ...
    
    
    def AddKeyboardFocusNotifyHandler(self, cb: typing.Callable) -> None:
        """
        Adds keyboard focus notify callback handler to the dialog.  
        
        Signature ``AddKeyboardFocusNotifyHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def RegisterUserDefinedUIBlock(self, blockDialog: BlockDialog, blockId: str) -> None:
        """
        Registers the reusable block with the dialog 
        
        Signature ``RegisterUserDefinedUIBlock(blockDialog, blockId)`` 
        
        :param blockDialog:  Dialog which contains the reusable block   
        :type blockDialog: :py:class:`NXOpen.BlockStyler.BlockDialog` 
        :param blockId:  "Block ID" of reusable block  
        :type blockId: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBlockProperties(self, blockName: str) -> PropertyList:
        """
        Gets the properties of a block  
        
        Signature ``GetBlockProperties(blockName)`` 
        
        :param blockName: BlockID of the block 
        :type blockName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.BlockStyler.PropertyList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    TopBlock: CompositeBlock = ...
    """
    Returns  a composite block that contains all the blocks in the dialog 
    
    <hr>
    
    Getter Method
    
    Signature ``TopBlock`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BlockStyler.CompositeBlock` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """


class LinearDimension(UIBlock):
    """
    Represents a Linear Dimension block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Values to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AdaptiveScaleLimits: bool = ...
    """
    Returns or sets the AdaptiveScaleLimits.  
    
    If true, indicates that the scale should be adaptive.
    
    <hr>
    
    Getter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :param scaleLimits: 
    :type scaleLimits: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    AutoReverseDuringDrag: bool = ...
    """
    Returns or sets  the AutoReverseDuringDrag.  
    
    If true, the linear dimension handle reverses its direction when it is dragged through the 0 value.
    
    <hr>
    
    Getter Method
    
    Signature ``AutoReverseDuringDrag`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutoReverseDuringDrag`` 
    
    :param autoReverse: 
    :type autoReverse: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ExpressionObject: NXOpen.TaggedObject = ...
    """
    Returns or sets  the ExpressionObject
    
    <hr>
    
    Getter Method
    
    Signature ``ExpressionObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpressionObject`` 
    
    :param expressionObj: 
    :type expressionObj: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Formula: str = ...
    """
    Returns or sets  the Formula
    
    <hr>
    
    Getter Method
    
    Signature ``Formula`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Formula`` 
    
    :param formula: 
    :type formula: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HandleOrientation: NXOpen.Vector3d = ...
    """
    Returns or sets  the HandleOrientation
    
    <hr>
    
    Getter Method
    
    Signature ``HandleOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HandleOrientation`` 
    
    :param orientation: 
    :type orientation: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HandleOrigin: NXOpen.Point3d = ...
    """
    Returns or sets  the HandleOrigin
    
    <hr>
    
    Getter Method
    
    Signature ``HandleOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HandleOrigin`` 
    
    :param handleOrogin: 
    :type handleOrogin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LineIncrement: float = ...
    """
    Returns or sets the LineIncrement value.  
    
    Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
    
    <hr>
    
    Getter Method
    
    Signature ``LineIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineIncrement`` 
    
    :param lineIncrement: 
    :type lineIncrement: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    MaxInclusive: bool = ...
    """
    Returns or sets  the MaxInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MaxInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxInclusive`` 
    
    :param maxInclusive: 
    :type maxInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumValue: float = ...
    """
    Returns or sets  the MaximumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumValue`` 
    
    :param maxValue: 
    :type maxValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinInclusive: bool = ...
    """
    Returns or sets  the MinInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MinInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinInclusive`` 
    
    :param minInclusive: 
    :type minInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinimumValue: float = ...
    """
    Returns or sets  the MinimumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumValue`` 
    
    :param minValue: 
    :type minValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PageIncrement: float = ...
    """
    Returns or sets the PageIncrement value.  
    
    Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
    
    <hr>
    
    Getter Method
    
    Signature ``PageIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PageIncrement`` 
    
    :param pageIncrement: 
    :type pageIncrement: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowFocusHandle: bool = ...
    """
    Returns or sets  the ShowFocusHandle
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFocusHandle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFocusHandle`` 
    
    :param showFocus: 
    :type showFocus: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowHandle: bool = ...
    """
    Returns or sets  the ShowHandle.  
    
    If true, linear dimension handle is visible
    
    <hr>
    
    Getter Method
    
    Signature ``ShowHandle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowHandle`` 
    
    :param showHandle: 
    :type showHandle: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       This call can be safely removed as this is now a no-op.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param pointType: 
    :type pointType: int 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       This call can be safely removed as this is now a no-op.
    
    License requirements: None.
    """
    Units: NXOpen.TaggedObject = ...
    """
    Returns or sets  the Units
    
    <hr>
    
    Getter Method
    
    Signature ``Units`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Units`` 
    
    :param units: 
    :type units: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Value: float = ...
    """
    Returns or sets  the Value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param dimensionValue: 
    :type dimensionValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WithScale: bool = ...
    """
    Returns or sets  the WithScale.  
    
    If true, the slider bar is shown.
    
    <hr>
    
    Getter Method
    
    Signature ``WithScale`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WithScale`` 
    
    :param withScale: 
    :type withScale: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: LinearDimension = ...  # unknown typename


class SuperSection(UIBlock):
    """
    Represents a Super Section block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDefaultCurveRulesMembers(self) -> 'list[str]':
        """
        Gets the DefaultCurveRules members 
        
        Signature ``GetDefaultCurveRulesMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AllowConvergentObject: bool = ...
    """
    Returns or sets  the AllowConvergentObject
    
    <hr>
    
    Getter Method
    
    Signature ``AllowConvergentObject`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowConvergentObject`` 
    
    :param allowConvergentObject: 
    :type allowConvergentObject: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    AllowInferredCurveSelection: bool = ...
    """
    Returns or sets  the AllowInferredCurveSelection
    
    <hr>
    
    Getter Method
    
    Signature ``AllowInferredCurveSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowInferredCurveSelection`` 
    
    :param allow: 
    :type allow: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    AllowStopAtIntersectionFollowFillet: bool = ...
    """
    Returns or sets  the AllowStopAtIntersectionFollowFillet
    
    <hr>
    
    Getter Method
    
    Signature ``AllowStopAtIntersectionFollowFillet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowStopAtIntersectionFollowFillet`` 
    
    :param allow: 
    :type allow: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    AngularTolerance: float = ...
    """
    Returns or sets  the AngularTolerance
    
    <hr>
    
    Getter Method
    
    Signature ``AngularTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AngularTolerance`` 
    
    :param tolerance: 
    :type tolerance: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BlendVirtualCurveOverlay: bool = ...
    """
    Returns or sets  the BlendVirtualCurveOverlay.  
    
    If true, virtual curve is displayed during preselection.
    
    <hr>
    
    Getter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :param blendCurve: 
    :type blendCurve: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ChainWithinFeature: bool = ...
    """
    Returns or sets  the ChainWithinFeature
    
    <hr>
    
    Getter Method
    
    Signature ``ChainWithinFeature`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ChainWithinFeature`` 
    
    :param chainWithinFeature: 
    :type chainWithinFeature: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CurveRules: int = ...
    """
    Returns or sets  the CurveRules
    
    <hr>
    
    Getter Method
    
    Signature ``CurveRules`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurveRules`` 
    
    :param curveRules: 
    :type curveRules: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DefaultCurveRulesAsString: str = ...
    """
    Returns or sets  the DefaultCurveRules as string
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultCurveRulesAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultCurveRulesAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EntityType: int = ...
    """
    Returns or sets  the EntityType
    
    <hr>
    
    Getter Method
    
    Signature ``EntityType`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EntityType`` 
    
    :param entityType: 
    :type entityType: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    FollowFillet: bool = ...
    """
    Returns or sets  the FollowFillet
    
    <hr>
    
    Getter Method
    
    Signature ``FollowFillet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FollowFillet`` 
    
    :param followFillet: 
    :type followFillet: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InferredCurveSelection: bool = ...
    """
    Returns or sets  the InferredCurveSelection
    
    <hr>
    
    Getter Method
    
    Signature ``InferredCurveSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InferredCurveSelection`` 
    
    :param selectInferredCurve: 
    :type selectInferredCurve: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PointOverlay: bool = ...
    """
    Returns or sets  the PointOverlay
    
    <hr>
    
    Getter Method
    
    Signature ``PointOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointOverlay`` 
    
    :param overlay: 
    :type overlay: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowFlowDirectionAndOriginCurve: bool = ...
    """
    Returns or sets  the ShowFlowDirectionAndOriginCurve
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFlowDirectionAndOriginCurve`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFlowDirectionAndOriginCurve`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SketchOnPath: bool = ...
    """
    Returns or sets  the SketchOnPath
    
    <hr>
    
    Getter Method
    
    Signature ``SketchOnPath`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SketchOnPath`` 
    
    :param sketchOnPath: 
    :type sketchOnPath: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SmartUpdateOptionAsString: str = ...
    """
    Returns or sets  the update option for points created by the point overlay.  
    
    Acceptable values are:
    
      *  **Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).
      *  **After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.
      *  **After Parent Body</b> The smart object will always update after the last feature on the parent body.
      *  **Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.
    
    <hr>
    
    Getter Method
    
    Signature ``SmartUpdateOptionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SmartUpdateOptionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.1
    
    License requirements: None.
    """
    SnapPointTypesEnabled: int = ...
    """
    Returns or sets  the SnapPointTypesEnabled
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesEnabled`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesEnabled`` 
    
    :param snapPointType: 
    :type snapPointType: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param defaultSnapPointType: 
    :type defaultSnapPointType: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StopAtIntersection: bool = ...
    """
    Returns or sets  the StopAtIntersection
    
    <hr>
    
    Getter Method
    
    Signature ``StopAtIntersection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StopAtIntersection`` 
    
    :param stop: 
    :type stop: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ToolTip: str = ...
    """
    Returns or sets  the ToolTip
    
    <hr>
    
    Getter Method
    
    Signature ``ToolTip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolTip`` 
    
    :param toolTip: 
    :type toolTip: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SuperSection = ...  # unknown typename


class SpecifyLocation(UIBlock):
    """
    Represents a Specify Location block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CursorLocation: NXOpen.Point3d = ...
    """
    Returns or sets  the CursorLocation
    
    <hr>
    
    Getter Method
    
    Signature ``CursorLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CursorLocation`` 
    
    :param cursorLocation: 
    :type cursorLocation: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DisplayTemporaryPoint: bool = ...
    """
    Returns or sets  the DisplayTemporaryPoint
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayTemporaryPoint`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayTemporaryPoint`` 
    
    :param display: 
    :type display: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SpecifyLocation = ...  # unknown typename


class TreeNodeInsertOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TreeNodeInsertOption():
    """
    Represents the node insert option which is used while inserting the node in tree.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "First", "Node is placed first in the hierarchy in which it is inserted."
       "Last", "Node is placed last in the hierarchy in which it is inserted."
       "Sort", "Node is sorted according to display text and placed accordingly in the hierarchy in which it is inserted"
       "AlwaysFirst", "Node is placed first in the hierarchy in which it is inserted. This is same as :py:class:`BlockStyler.TreeNodeInsertOption.First <BlockStyler.TreeNodeInsertOption>`, except that it remains first after a column sort. If there is more than one node beneath a single parent with this option then they will be sorted relative to each other."
       "AlwaysLast", "Node is placed last in the hierarchy in which it is inserted. This is same as :py:class:`BlockStyler.TreeNodeInsertOption.Last <BlockStyler.TreeNodeInsertOption>`, except that it remains last after a column sort. If there is more than one node beneath a single parent with this option then they will be sorted relative to each other."
    """
    First = 0  # TreeNodeInsertOptionMemberType
    Last = 1  # TreeNodeInsertOptionMemberType
    Sort = 2  # TreeNodeInsertOptionMemberType
    AlwaysFirst = 3  # TreeNodeInsertOptionMemberType
    AlwaysLast = 4  # TreeNodeInsertOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TreeColumnSortOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TreeColumnSortOption():
    """
    Represents the column sort option.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unsorted", "Unsorted"
       "Ascending", "Ascending"
       "Descending", "Descending"
    """
    Unsorted = 0  # TreeColumnSortOptionMemberType
    Ascending = 1  # TreeColumnSortOptionMemberType
    Descending = 2  # TreeColumnSortOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TreeColumnResizePolicyMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TreeColumnResizePolicy():
    """
    Represents column resize policy.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ConstantWidth", "Constant width"
       "ResizeWithContents", "Width resized with contents."
       "ResizeWithTree", "Width resize with tree window resize."
    """
    ConstantWidth = 0  # TreeColumnResizePolicyMemberType
    ResizeWithContents = 1  # TreeColumnResizePolicyMemberType
    ResizeWithTree = 2  # TreeColumnResizePolicyMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TreeColumnDisplayMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TreeColumnDisplay():
    """
    Represents the column display type. If the type is :py:class:`BlockStyler.TreeColumnDisplay.Icon  <BlockStyler.TreeColumnDisplay>`
    then the provided text is interpreted as icon.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Text", "Text"
       "Icon", "Icon"
    """
    Text = 0  # TreeColumnDisplayMemberType
    Icon = 1  # TreeColumnDisplayMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TreeBeginLabelEditStateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TreeBeginLabelEditState():
    """
    Represents the state to allow/disallow the node label edit. Use these options in callback BlockStyler.Tree.OnBeginLabelEditCallback.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Allow", "Use this option to allow label edit."
       "Disallow", "Use this option to disallow label edit."
    """
    Allow = 0  # TreeBeginLabelEditStateMemberType
    Disallow = 1  # TreeBeginLabelEditStateMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TreeEndLabelEditStateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TreeEndLabelEditState():
    """
    Represents the state to accept/reject the edited label of node. Use these options in callback BlockStyler.Tree.OnEndLabelEditCallback.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AcceptText", "Use this option to accept the edited text."
       "RejectText", "Use this option to reject the edited text and retain the previous one."
    """
    AcceptText = 0  # TreeEndLabelEditStateMemberType
    RejectText = 1  # TreeEndLabelEditStateMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TreeEditControlOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TreeEditControlOption():
    """
    Represents the options to accept or reject the changed value.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Accept", "Use this option to allow edit."
       "Reject", "Use this option to disallow edit."
    """
    Accept = 0  # TreeEditControlOptionMemberType
    Reject = 1  # TreeEditControlOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TreeControlTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TreeControlType():
    """
    Represents the type of edit options. Use these options in edit control callback
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "ComboBox", "Combo box."
       "ListBox", "List box."
    """
    NotSet = 0  # TreeControlTypeMemberType
    ComboBox = 1  # TreeControlTypeMemberType
    ListBox = 2  # TreeControlTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Tree(UIBlock):
    """
    Represents the Tree block in block styler automation.  
    
    To start utilizing the tree use
    methods such as :py:meth:`BlockStyler.Tree.InsertColumn`, :py:meth:`BlockStyler.Tree.CreateNode`, :py:meth:`BlockStyler.Tree.InsertNode` etc.
    It is must to insert the column on the tree before inserting any node. Node can be created but cannot be inserted without the column available on the tree. 
    Note that some of the methods of this class such as :py:meth:`BlockStyler.Tree.InsertColumn` must be used in or after the BlockStyler.BlockDialog.DialogShown callback after 
    which tree is fully constructed and ready for use.
    
    .. versionadded:: NX7.5.0
    """
    
    class NodeInsertOption():
        """
        Represents the node insert option which is used while inserting the node in tree.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "First", "Node is placed first in the hierarchy in which it is inserted."
           "Last", "Node is placed last in the hierarchy in which it is inserted."
           "Sort", "Node is sorted according to display text and placed accordingly in the hierarchy in which it is inserted"
           "AlwaysFirst", "Node is placed first in the hierarchy in which it is inserted. This is same as :py:class:`BlockStyler.TreeNodeInsertOption.First <BlockStyler.TreeNodeInsertOption>`, except that it remains first after a column sort. If there is more than one node beneath a single parent with this option then they will be sorted relative to each other."
           "AlwaysLast", "Node is placed last in the hierarchy in which it is inserted. This is same as :py:class:`BlockStyler.TreeNodeInsertOption.Last <BlockStyler.TreeNodeInsertOption>`, except that it remains last after a column sort. If there is more than one node beneath a single parent with this option then they will be sorted relative to each other."
        """
        First = 0  # TreeNodeInsertOptionMemberType
        Last = 1  # TreeNodeInsertOptionMemberType
        Sort = 2  # TreeNodeInsertOptionMemberType
        AlwaysFirst = 3  # TreeNodeInsertOptionMemberType
        AlwaysLast = 4  # TreeNodeInsertOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ColumnSortOption():
        """
        Represents the column sort option.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unsorted", "Unsorted"
           "Ascending", "Ascending"
           "Descending", "Descending"
        """
        Unsorted = 0  # TreeColumnSortOptionMemberType
        Ascending = 1  # TreeColumnSortOptionMemberType
        Descending = 2  # TreeColumnSortOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ColumnResizePolicy():
        """
        Represents column resize policy.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ConstantWidth", "Constant width"
           "ResizeWithContents", "Width resized with contents."
           "ResizeWithTree", "Width resize with tree window resize."
        """
        ConstantWidth = 0  # TreeColumnResizePolicyMemberType
        ResizeWithContents = 1  # TreeColumnResizePolicyMemberType
        ResizeWithTree = 2  # TreeColumnResizePolicyMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ColumnDisplay():
        """
        Represents the column display type. If the type is :py:class:`BlockStyler.TreeColumnDisplay.Icon  <BlockStyler.TreeColumnDisplay>`
        then the provided text is interpreted as icon.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Text", "Text"
           "Icon", "Icon"
        """
        Text = 0  # TreeColumnDisplayMemberType
        Icon = 1  # TreeColumnDisplayMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BeginLabelEditState():
        """
        Represents the state to allow/disallow the node label edit. Use these options in callback BlockStyler.Tree.OnBeginLabelEditCallback.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Allow", "Use this option to allow label edit."
           "Disallow", "Use this option to disallow label edit."
        """
        Allow = 0  # TreeBeginLabelEditStateMemberType
        Disallow = 1  # TreeBeginLabelEditStateMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class EndLabelEditState():
        """
        Represents the state to accept/reject the edited label of node. Use these options in callback BlockStyler.Tree.OnEndLabelEditCallback.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AcceptText", "Use this option to accept the edited text."
           "RejectText", "Use this option to reject the edited text and retain the previous one."
        """
        AcceptText = 0  # TreeEndLabelEditStateMemberType
        RejectText = 1  # TreeEndLabelEditStateMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class EditControlOption():
        """
        Represents the options to accept or reject the changed value.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Accept", "Use this option to allow edit."
           "Reject", "Use this option to disallow edit."
        """
        Accept = 0  # TreeEditControlOptionMemberType
        Reject = 1  # TreeEditControlOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ControlType():
        """
        Represents the type of edit options. Use these options in edit control callback
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None"
           "ComboBox", "Combo box."
           "ListBox", "List box."
        """
        NotSet = 0  # TreeControlTypeMemberType
        ComboBox = 1  # TreeControlTypeMemberType
        ListBox = 2  # TreeControlTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreateNode(self, displayText: str) -> Node:
        """
        Creates the node but does not insert it.  
        
        Use :py:meth:`BlockStyler.Tree.InsertNode` to insert 
        the node. 
        
        Signature ``CreateNode(displayText)`` 
        
        :param displayText: Specifies the display text of the node. 
        :type displayText: str 
        :returns: Node 
        :rtype: :py:class:`NXOpen.BlockStyler.Node` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def InsertNode(self, newNode: Node, parentNode: Node, afterNode: Node, nodeInsertOption: TreeNodeInsertOption) -> None:
        """
        Inserts the node.  
        
        Subsequently BlockStyler.Tree.OnInsertNodeCallback is called. 
        Reinserting the node in same or different tree is not allowed.
        
        Signature ``InsertNode(newNode, parentNode, afterNode, nodeInsertOption)`` 
        
        :param newNode: New Node. 
        :type newNode: :py:class:`NXOpen.BlockStyler.Node` 
        :param parentNode: Parent node under which new node is supposed to be placed. 
        :type parentNode: :py:class:`NXOpen.BlockStyler.Node` 
        :param afterNode: New node placed after this node. If there is mismatch between parent-node and after-node then former is honoured. 
        :type afterNode: :py:class:`NXOpen.BlockStyler.Node` 
        :param nodeInsertOption: Node insert option. Provide the value if after node is None.                                                             This value is not considered if a valid after-node is supplied. 
        :type nodeInsertOption: :py:class:`NXOpen.BlockStyler.TreeNodeInsertOption` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteNode(self, node: Node) -> None:
        """
        Deletes the node from tree.  
        
        Further usage of deleted node is illegal. The last place where node can be used is in 
        BlockStyler.Tree.OnDeleteNodeCallaback callback which gets called when node is deleted.
        
        Signature ``DeleteNode(node)`` 
        
        :param node: Node to delete 
        :type node: :py:class:`NXOpen.BlockStyler.Node` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SelectNode(self, node: Node, isSelect: bool, isOtherNodeAffected: bool) -> None:
        """
        Selects the provided node.  
        
        Signature ``SelectNode(node, isSelect, isOtherNodeAffected)`` 
        
        :param node: Node to be selected 
        :type node: :py:class:`NXOpen.BlockStyler.Node` 
        :param isSelect: Select/Deselect flag. If true, the provided node is selected, else deselected. 
        :type isSelect: bool 
        :param isOtherNodeAffected: Flag indicating whether selection of other nodes is affected. If true,                                               all the previous selected nodes are deselected, else unaffected. 
        :type isOtherNodeAffected: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SelectNodes(self, node: 'list[Node]', isSelect: bool, isOtherNodeAffected: bool) -> None:
        """
        Selects the provided nodes.  
        
        Signature ``SelectNodes(node, isSelect, isOtherNodeAffected)`` 
        
        :param node: Nodes to be selected 
        :type node: list of :py:class:`NXOpen.BlockStyler.Node` 
        :param isSelect: Select/Deselect flag. If true, the provided nodes are selected, else deselected. 
        :type isSelect: bool 
        :param isOtherNodeAffected: Flag indicating whether selection of other nodes is affected. If true,                                               all the previous selected nodes are deselected, else remain so. 
        :type isOtherNodeAffected: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def InsertColumn(self, columnID: int, columnTitle: str, columnWidth: int) -> int:
        """
        Inserts a column.  
        
        Inserts a column with following defaults: 
        
          * :py:class:`BlockStyler.TreeColumnSortOption` as :py:class:`BlockStyler.TreeColumnSortOption.Ascending <BlockStyler.TreeColumnSortOption>`
          * Column sortable as True
          * Column visible as True
          * :py:class:`BlockStyler.TreeColumnDisplay` as :py:class:`BlockStyler.TreeColumnDisplay.Text <BlockStyler.TreeColumnDisplay>`
          * :py:class:`BlockStyler.TreeColumnResizePolicy` as :py:class:`BlockStyler.TreeColumnResizePolicy.ConstantWidth <BlockStyler.TreeColumnResizePolicy>`
        
        The new column is placed after the last available column. If no column is available then the inserted one becomes the first column of the tree.
        
        Signature ``InsertColumn(columnID, columnTitle, columnWidth)`` 
        
        :param columnID: Unique column Id associated with the column. Any further interaction with the column is done with this column Id. 
        :type columnID: int 
        :param columnTitle: Column header title. 
        :type columnTitle: str 
        :param columnWidth: Providing value less than zero will set the default width of 0 for the column. 
        :type columnWidth: int 
        :returns: Absolute column position. 
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnTitle(self, columnID: int) -> str:
        """
        Gets the column title.  
        
        Signature ``GetColumnTitle(columnID)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :returns: Column header title. 
        :rtype: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnTitle(self, columnID: int, columnHeaderTitle: str) -> None:
        """
        Sets the column title.  
        
        Signature ``SetColumnTitle(columnID, columnHeaderTitle)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :param columnHeaderTitle: Column header title. 
        :type columnHeaderTitle: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnId(self, columnPosition: int) -> int:
        """
        Gets the column Id for the provided column position.  
        
        Signature ``GetColumnId(columnPosition)`` 
        
        :param columnPosition: Column position. 
        :type columnPosition: int 
        :returns: Unique column Id associated with the column. 
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnPosition(self, columnID: int) -> int:
        """
        Gets column position.  
        
        Returns -1 if no column is associated with the provided column Id. 
        
        Signature ``GetColumnPosition(columnID)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :returns: Column position. 
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnWidth(self, columnID: int) -> int:
        """
        Gets column width 
        
        Signature ``GetColumnWidth(columnID)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :returns: Column width. 
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnWidth(self, columnID: int, columnWidth: int) -> None:
        """
        Sets the column width
        
        Signature ``SetColumnWidth(columnID, columnWidth)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :param columnWidth: Column width. 
        :type columnWidth: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnSortOption(self, columnID: int) -> TreeColumnSortOption:
        """
        Gets the column sort option.  
        
        Signature ``GetColumnSortOption(columnID)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :returns: Column sort option. 
        :rtype: :py:class:`NXOpen.BlockStyler.TreeColumnSortOption` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnSortOption(self, columnID: int, sortOption: TreeColumnSortOption) -> None:
        """
        Sets the column sort option.  
        
        Signature ``SetColumnSortOption(columnID, sortOption)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :param sortOption: Column sort option. 
        :type sortOption: :py:class:`NXOpen.BlockStyler.TreeColumnSortOption` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnSortable(self, columnID: int) -> bool:
        """
        Gets the flag indicating whether the column is sortable.  
        
        Signature ``GetColumnSortable(columnID)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :returns: Flag indicating whether the column is sortable. 
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnSortable(self, columnID: int, isSortable: bool) -> None:
        """
        Sets the flag indicating whether the column is sortable.  
        
        Signature ``SetColumnSortable(columnID, isSortable)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :param isSortable: Flag indicating whether the column is sortable. 
        :type isSortable: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnVisible(self, columnID: int) -> bool:
        """
        Gets the flag indicating whether the column is visible.  
        
        Signature ``GetColumnVisible(columnID)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :returns: Flag indicating whether the column is visible. 
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnVisible(self, columnID: int, isVisible: bool) -> None:
        """
        Sets the flag indicating whether the column is visible
        
        Signature ``SetColumnVisible(columnID, isVisible)`` 
        
        :param columnID: Unique column Id associated with the column 
        :type columnID: int 
        :param isVisible: Flag indicating whether the column is visible 
        :type isVisible: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnDisplayType(self, columnID: int) -> TreeColumnDisplay:
        """
        Gets the display type of the column.  
        
        Signature ``GetColumnDisplayType(columnID)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :returns: Display type. 
        :rtype: :py:class:`NXOpen.BlockStyler.TreeColumnDisplay` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnDisplayType(self, columnID: int, displayType: TreeColumnDisplay) -> None:
        """
        Sets the display type of the column.  
        
        Signature ``SetColumnDisplayType(columnID, displayType)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :param displayType: Display type. 
        :type displayType: :py:class:`NXOpen.BlockStyler.TreeColumnDisplay` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnResizePolicy(self, columnID: int) -> TreeColumnResizePolicy:
        """
        Gets the column resize policy.  
        
        Signature ``GetColumnResizePolicy(columnID)`` 
        
        :param columnID: Unique column Id associated with the column. 
        :type columnID: int 
        :returns: Resize policy. 
        :rtype: :py:class:`NXOpen.BlockStyler.TreeColumnResizePolicy` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnResizePolicy(self, columnID: int, resizePolicy: TreeColumnResizePolicy) -> None:
        """
        Sets the column resize policy.  
        
        Signature ``SetColumnResizePolicy(columnID, resizePolicy)`` 
        
        :param columnID: Unique column Id associated with the column 
        :type columnID: int 
        :param resizePolicy: Resize policy 
        :type resizePolicy: :py:class:`NXOpen.BlockStyler.TreeColumnResizePolicy` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPreSelectionTimeOut(self, timeOut: float) -> None:
        """
        Sets the pre selection time out.  
        
        BlockStyler.Tree.OnPreSelectCallback is called based on this value.
        
        Signature ``SetPreSelectionTimeOut(timeOut)`` 
        
        :param timeOut: Time in millisecond 
        :type timeOut: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedNodes(self) -> 'list[Node]':
        """
        Gets the selected nodes.  
        
        Signature ``GetSelectedNodes()`` 
        
        :returns: Selected nodes. 
        :rtype: list of :py:class:`NXOpen.BlockStyler.Node` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def Redraw(self, redraw: bool) -> None:
        """
        Freezes the tree if the value is set to False which implies that no changes would occur 
        in the tree after this point.  
        
        The tree remains in that state until the value is set to True, 
        after which the tree completely updates itself with the changes performed on it in between 
        the two calls. Use this method to efficiently utilize the tree when it is subjected to enourmous changes.
        
        Signature ``Redraw(redraw)`` 
        
        :param redraw: Flag corresponds to freeze/unfreeze of tree changes. 
        :type redraw: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnExpandHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on expand callback to the tree.  
        
        Signature ``SetOnExpandHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnInsertColumnHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on insert column callback to the tree.  
        
        Signature ``SetOnInsertColumnHandler(cb)`` 
        
        :param cb: Callback. 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetStateIconNameHandler(self, cb: typing.Callable) -> None:
        """
        Sets the state icon name callback.  
        
        Signature ``SetStateIconNameHandler(cb)`` 
        
        :param cb: Callback. 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnInsertNodeHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on insert node callback.  
        
        Signature ``SetOnInsertNodeHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnPreSelectHandler(self, cb: typing.Callable) -> None:
        """
        Sets on pre select callback 
        
        Signature ``SetOnPreSelectHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnDeleteNodeHandler(self, cb: typing.Callable) -> None:
        """
        Sets on delete node callback 
        
        Signature ``SetOnDeleteNodeHandler(cb)`` 
        
        :param cb: Callback. 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnSelectHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on select node callback 
        
        Signature ``SetOnSelectHandler(cb)`` 
        
        :param cb: Callback. 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnStateChangeHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on state change callback.  
        
        Signature ``SetOnStateChangeHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetToolTipTextHandler(self, cb: typing.Callable) -> None:
        """
        Sets the tool tip callback.  
        
        Signature ``SetToolTipTextHandler(cb)`` 
        
        :param cb: Callback. 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnSortHandler(self, cb: typing.Callable) -> None:
        """
        Sets the column sort callback.  
        
        Signature ``SetColumnSortHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnBeginLabelEditHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on-begin-label-edit callback
        
        Signature ``SetOnBeginLabelEditHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnEndLabelEditHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on-end-label-edit callback
        
        Signature ``SetOnEndLabelEditHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAskEditControlHandler(self, cb: typing.Callable) -> None:
        """
        Sets the node-edit-control callback
        
        Signature ``SetAskEditControlHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEditOptions(self, stringArray: 'list[str]', defaultIndex: int) -> None:
        """
        Sets the options in edit-control. This method must be used
        in BlockStyler.Tree.AskEditControlCallback to make available the options in edit-control.
        
        Signature ``SetEditOptions(stringArray, defaultIndex)`` 
        
        :param stringArray: Options to be made availabe in edit-control 
        :type stringArray: list of str 
        :param defaultIndex:  Index for default selection. This is zero based, for instance if it is set to 1 then 2nd option is selected by default during edit operation. 
        :type defaultIndex: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnEditOptionSelectedHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on-end-label-edit callback
        
        Signature ``SetOnEditOptionSelectedHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnMenuHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on menu callback 
        
        Signature ``SetOnMenuHandler(cb)`` 
        
        :param cb: Callback. 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnMenuSelectionHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on menu selection callback 
        
        Signature ``SetOnMenuSelectionHandler(cb)`` 
        
        :param cb: Callback. 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetIsDragAllowedHandler(self, cb: typing.Callable) -> None:
        """
        Sets the callback handler for node drag
        
        Signature ``SetIsDragAllowedHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetIsDropAllowedHandler(self, cb: typing.Callable) -> None:
        """
        Sets the callback handler for node drop
        
        Signature ``SetIsDropAllowedHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnDropHandler(self, cb: typing.Callable) -> None:
        """
        Sets the callback handler for node drop
        
        Signature ``SetOnDropHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnDropMenuHandler(self, cb: typing.Callable) -> None:
        """
        Sets the callback handler for on drop menu.  
        
        Signature ``SetOnDropMenuHandler(cb)`` 
        
        :param cb: Callback 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnDefaultActionHandler(self, cb: typing.Callable) -> None:
        """
        Sets the on select node callback 
        
        Signature ``SetOnDefaultActionHandler(cb)`` 
        
        :param cb: Callback. 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.2
        
        License requirements: None.
        """
        ...
    
    
    def CreateMenu(self) -> TreeListMenu:
        """
        Creates the menu.  
        
        Use :py:meth:`BlockStyler.Tree.SetMenu` to set the created menu. 
        
        Signature ``CreateMenu()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.BlockStyler.TreeListMenu` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMenu(self, menu: TreeListMenu) -> None:
        """
        Sets the menu, resulting the menu to appear on the screen.  
        
        This method must be used in callback which is intended to create
        menu, such as BlockStyler.Tree.OnMenuCallback
        
        Signature ``SetMenu(menu)`` 
        
        :param menu: Menu. 
        :type menu: :py:class:`NXOpen.BlockStyler.TreeListMenu` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CopyNode(self, sourceNode: Node) -> Node:
        """
        Copies the existing :py:class:`BlockStyler.Node`.  
        
        The tree can copy either its own node or the node of another tree. 
        The copied node can only be inserted into the tree which has copied that node. The column texts are not passed to the copied node. 
        
        Signature ``CopyNode(sourceNode)`` 
        
        :param sourceNode: Source node. Can be node of other tree. 
        :type sourceNode: :py:class:`NXOpen.BlockStyler.Node` 
        :returns: Copied node. 
        :rtype: :py:class:`NXOpen.BlockStyler.Node` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectionModeMembers(self) -> 'list[str]':
        """
        Gets the SelectionMode 
        
        Signature ``GetSelectionModeMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    CanStretchHeight: bool = ...
    """
    Returns or sets  the CanStretchHeight.  
    
    If true, height of list box will change.
    
    <hr>
    
    Getter Method
    
    Signature ``CanStretchHeight`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanStretchHeight`` 
    
    :param stretchHeight: 
    :type stretchHeight: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CanStretchWidth: bool = ...
    """
    Returns or sets  the CanStretchWidth.  
    
    If true, width of TreeList block will change.
    
    <hr>
    
    Getter Method
    
    Signature ``CanStretchWidth`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanStretchWidth`` 
    
    :param stretchWidth: 
    :type stretchWidth: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    FirstSelectedNode: Node = ...
    """
    Returns  the first selected node among the available selected nodes.  
    
    Returns None if no node is selected.
    
    <hr>
    
    Getter Method
    
    Signature ``FirstSelectedNode`` 
    
    :returns: First selected node in the whole hierarchy 
    :rtype: :py:class:`NXOpen.BlockStyler.Node` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Height: int = ...
    """
    Returns or sets  the Height
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Height`` 
    
    :param height: 
    :type height: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumHeight: int = ...
    """
    Returns or sets  the MaximumHeight
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumHeight`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumHeight`` 
    
    :param maxHeight: 
    :type maxHeight: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumWidth: int = ...
    """
    Returns or sets  the MaximumWidth
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumWidth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumWidth`` 
    
    :param maxWidth: 
    :type maxWidth: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MinimumHeight: int = ...
    """
    Returns or sets  the MinimumHeight
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumHeight`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumHeight`` 
    
    :param minHeight: 
    :type minHeight: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinimumWidth: int = ...
    """
    Returns or sets  the MinimumWidth
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumWidth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumWidth`` 
    
    :param minWidth: 
    :type minWidth: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    NumberOfColumns: int = ...
    """
    Returns  the number of column inserted in the tree.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfColumns`` 
    
    :returns: Total number of column. 
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    RootNode: Node = ...
    """
    Returns  the root node.  
    
    If more than one root node is available in top hierarchy 
    then the first root node is returned.
    
    <hr>
    
    Getter Method
    
    Signature ``RootNode`` 
    
    :returns: Root node. 
    :rtype: :py:class:`NXOpen.BlockStyler.Node` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ScrollFrozenColumn: int = ...
    """
    Returns or sets  the ScrollFrozenColumn.  
    
    It specifies the number of columns to freeze while scrolling.
    
    <hr>
    
    Getter Method
    
    Signature ``ScrollFrozenColumn`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScrollFrozenColumn`` 
    
    :param scrollFrozenColumn: 
    :type scrollFrozenColumn: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ScrollLineNumber: int = ...
    """
    Returns or sets  the ScrollLineNumber.  
    
    It specifies the number of lines to scroll when the mouse wheel rotates.
    
    <hr>
    
    Getter Method
    
    Signature ``ScrollLineNumber`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScrollLineNumber`` 
    
    :param scrollLineNumber: 
    :type scrollLineNumber: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectionModeAsString: str = ...
    """
    Returns or sets  the SelectionMode
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionModeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectionModeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowExpandCollapseMarker: bool = ...
    """
    Returns or sets  the ShowExpandCollapseMarker.  
    
    If true, displays a sign as a marker alongside first node of the tree indicating if it is expanded or collapsed.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowExpandCollapseMarker`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowExpandCollapseMarker`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowHeader: bool = ...
    """
    Returns or sets  the ShowHeader
    
    <hr>
    
    Getter Method
    
    Signature ``ShowHeader`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowHeader`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowMultipleColumns: bool = ...
    """
    Returns or sets  the ShowMultipleColumns
    
    <hr>
    
    Getter Method
    
    Signature ``ShowMultipleColumns`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowMultipleColumns`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowToolTips: bool = ...
    """
    Returns or sets  the ShowToolTips
    
    <hr>
    
    Getter Method
    
    Signature ``ShowToolTips`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowToolTips`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SortRootNodes: bool = ...
    """
    Returns or sets  the SortRootNodes.  
    
    If true, sorting of root nodes is allowed.
    
    <hr>
    
    Getter Method
    
    Signature ``SortRootNodes`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SortRootNodes`` 
    
    :param sort: 
    :type sort: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Width: int = ...
    """
    Returns or sets  the Width
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param width: 
    :type width: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: Tree = ...  # unknown typename


class IntegerBlock(UIBlock):
    """
    Represents a Integer block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetComboOptions(self) -> 'list[int]':
        """
        Gets the ComboOptions 
        
        Signature ``GetComboOptions()`` 
        
        :returns: 
        :rtype: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetComboOptions(self, optionValue: 'list[int]') -> None:
        """
        Sets the ComboOptions
        
        Signature ``SetComboOptions(optionValue)`` 
        
        :param optionValue: 
        :type optionValue: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPresentationStyleMembers(self) -> 'list[str]':
        """
        Gets the PresentationStyle member  
        
        Signature ``GetPresentationStyleMembers()`` 
        
        :returns: Value to get for the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AdaptiveScaleLimits: bool = ...
    """
    Returns or sets  the AdaptiveScaleLimits
    
    <hr>
    
    Getter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :param scaleLimits: 
    :type scaleLimits: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Increment: float = ...
    """
    Returns or sets  the Increment
    
    <hr>
    
    Getter Method
    
    Signature ``Increment`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Increment`` 
    
    :param increment: 
    :type increment: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LineIncrement: float = ...
    """
    Returns or sets  the LineIncrement
    
    <hr>
    
    Getter Method
    
    Signature ``LineIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineIncrement`` 
    
    :param lineIncrement: 
    :type lineIncrement: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaxInclusive: bool = ...
    """
    Returns or sets  the MaxInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MaxInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxInclusive`` 
    
    :param maxInclusive: 
    :type maxInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumValue: int = ...
    """
    Returns or sets  the MaximumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumValue`` 
    
    :param maxValue: 
    :type maxValue: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinInclusive: bool = ...
    """
    Returns or sets  the MinInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MinInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinInclusive`` 
    
    :param minInclusive: 
    :type minInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinimumValue: int = ...
    """
    Returns or sets  the MinimumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumValue`` 
    
    :param minValue: 
    :type minValue: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PageIncrement: float = ...
    """
    Returns or sets  the PageIncrement
    
    <hr>
    
    Getter Method
    
    Signature ``PageIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PageIncrement`` 
    
    :param pageIncrement: 
    :type pageIncrement: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PresentationStyleAsString: str = ...
    """
    Returns or sets  the PresentationStyle as string
    
    <hr>
    
    Getter Method
    
    Signature ``PresentationStyleAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PresentationStyleAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ReadOnlyValue: bool = ...
    """
    Returns or sets  the ReadOnlyValue
    
    <hr>
    
    Getter Method
    
    Signature ``ReadOnlyValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReadOnlyValue`` 
    
    :param readOnly: 
    :type readOnly: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ScaleLimits: bool = ...
    """
    Returns or sets  the ScaleLimits
    
    <hr>
    
    Getter Method
    
    Signature ``ScaleLimits`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScaleLimits`` 
    
    :param scaleLimits: 
    :type scaleLimits: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ScaleMaxLimitLabel: str = ...
    """
    Returns or sets  the ScaleMaxLimitLabel
    
    <hr>
    
    Getter Method
    
    Signature ``ScaleMaxLimitLabel`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScaleMaxLimitLabel`` 
    
    :param maxLimitLabel: 
    :type maxLimitLabel: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ScaleMinLimitLabel: str = ...
    """
    Returns or sets  the ScaleMinLimitLabel
    
    <hr>
    
    Getter Method
    
    Signature ``ScaleMinLimitLabel`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScaleMinLimitLabel`` 
    
    :param minLimitLabel: 
    :type minLimitLabel: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowScaleValue: bool = ...
    """
    Returns or sets  the ShowScaleValue
    
    <hr>
    
    Getter Method
    
    Signature ``ShowScaleValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowScaleValue`` 
    
    :param showValue: 
    :type showValue: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    TitleVisibility: bool = ...
    """
    Returns or sets  the TitleVisibility
    
    <hr>
    
    Getter Method
    
    Signature ``TitleVisibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TitleVisibility`` 
    
    :param visibility: 
    :type visibility: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Value: int = ...
    """
    Returns or sets  the Value
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param inetegerValue: 
    :type inetegerValue: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WrapSpin: bool = ...
    """
    Returns or sets  the WrapSpin
    
    <hr>
    
    Getter Method
    
    Signature ``WrapSpin`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WrapSpin`` 
    
    :param wrapSpin: 
    :type wrapSpin: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: IntegerBlock = ...  # unknown typename


class StringBlock(UIBlock):
    """
    Represents a String block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Values to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBalloonTooltipImages(self) -> 'list[str]':
        """
        Gets the BalloonTooltipImages 
        
        Signature ``GetBalloonTooltipImages()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBalloonTooltipImages(self, imageStrings: 'list[str]') -> None:
        """
        Sets the BalloonTooltipImages
        
        Signature ``SetBalloonTooltipImages(imageStrings)`` 
        
        :param imageStrings: 
        :type imageStrings: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBalloonTooltipTexts(self) -> 'list[str]':
        """
        Gets the BalloonTooltipTexts 
        
        Signature ``GetBalloonTooltipTexts()`` 
        
        :returns: Values to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBalloonTooltipTexts(self, tooltipTextArray: 'list[str]') -> None:
        """
        Sets the BalloonTooltipTexts
        
        Signature ``SetBalloonTooltipTexts(tooltipTextArray)`` 
        
        :param tooltipTextArray: Value to set for the property.  
        :type tooltipTextArray: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetListItems(self) -> 'list[str]':
        """
        Gets the ListItems 
        
        Signature ``GetListItems()`` 
        
        :returns: Values to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetListItems(self, itemStrings: 'list[str]') -> None:
        """
        Sets the ListItems
        
        Signature ``SetListItems(itemStrings)`` 
        
        :param itemStrings: Value to set to the property 
        :type itemStrings: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPresentationStyleMembers(self) -> 'list[str]':
        """
        Gets the PresentationStyle members  
        
        Signature ``GetPresentationStyleMembers()`` 
        
        :returns: Values to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetWidthMembers(self) -> 'list[str]':
        """
        Gets the Width members  
        
        Signature ``GetWidthMembers()`` 
        
        :returns: Values to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AllowInternationalTextInput: bool = ...
    """
    Returns or sets  the AllowInternationalTextInput
    
    <hr>
    
    Getter Method
    
    Signature ``AllowInternationalTextInput`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX12.0.0
       Not required from NX10 onwards. Internationalization is available by default.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowInternationalTextInput`` 
    
    :param allow: 
    :type allow: bool 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX12.0.0
       Not required from NX10 onwards. Internationalization is available by default.
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IsPassword: bool = ...
    """
    Returns or sets  the IsPassword.  
    
    If true, characters will not be readable. They will be displayed as *.
    
    <hr>
    
    Getter Method
    
    Signature ``IsPassword`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsPassword`` 
    
    :param passwrod: 
    :type passwrod: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaxTextLength: int = ...
    """
    Returns or sets  the MaxTextLength
    
    <hr>
    
    Getter Method
    
    Signature ``MaxTextLength`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxTextLength`` 
    
    :param textLength: 
    :type textLength: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PresentationStyleAsString: str = ...
    """
    Returns or sets  the PresentationStyle as string
    
    <hr>
    
    Getter Method
    
    Signature ``PresentationStyleAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PresentationStyleAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ReadOnlyString: bool = ...
    """
    Returns or sets  the ReadOnlyString
    
    <hr>
    
    Getter Method
    
    Signature ``ReadOnlyString`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReadOnlyString`` 
    
    :param readonly: 
    :type readonly: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Tooltip: str = ...
    """
    Returns or sets  the Tooltip
    
    <hr>
    
    Getter Method
    
    Signature ``Tooltip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Tooltip`` 
    
    :param tooltipString: 
    :type tooltipString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Value: str = ...
    """
    Returns or sets  the Value
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param valueString: 
    :type valueString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WideValue: str = ...
    """
    Returns or sets  the WideValue.  
    
    Specifies the International text. This property accepts international characters supported by NX.
    
    <hr>
    
    Getter Method
    
    Signature ``WideValue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX12.0.0
       Use 'Value' instead which supports Internationalization.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WideValue`` 
    
    :param wideValueString: 
    :type wideValueString: str 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX12.0.0
       Use 'Value' instead which supports Internationalization.
    
    License requirements: None.
    """
    WidthAsString: str = ...
    """
    Returns or sets  the Width as string
    
    <hr>
    
    Getter Method
    
    Signature ``WidthAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WidthAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: StringBlock = ...  # unknown typename


class SpecifyVector(UIBlock):
    """
    Represents Specify Vector block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DoubleSide: bool = ...
    """
    Returns or sets  the DoubleSide
    
    <hr>
    
    Getter Method
    
    Signature ``DoubleSide`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DoubleSide`` 
    
    :param doubleSide: 
    :type doubleSide: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EnableFacetSelection: bool = ...
    """
    Returns or sets  the EnableFacetSelection
    
    <hr>
    
    Getter Method
    
    Signature ``EnableFacetSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnableFacetSelection`` 
    
    :param enableSelection: 
    :type enableSelection: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EnableReverseDirection: bool = ...
    """
    Returns or sets  the EnableReverseDirection
    
    <hr>
    
    Getter Method
    
    Signature ``EnableReverseDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnableReverseDirection`` 
    
    :param enableReverse: 
    :type enableReverse: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Is2DMode: bool = ...
    """
    Returns or sets  the Is2DMode.  
    
    If true, vector is created in 2D space.
    
    <hr>
    
    Getter Method
    
    Signature ``Is2DMode`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Is2DMode`` 
    
    :param is2DMode: 
    :type is2DMode: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Point: NXOpen.Point3d = ...
    """
    Returns or sets  the Point
    
    <hr>
    
    Getter Method
    
    Signature ``Point`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Point`` 
    
    :param point: 
    :type point: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowShortcuts: bool = ...
    """
    Returns or sets  the ShowShortcuts
    
    <hr>
    
    Getter Method
    
    Signature ``ShowShortcuts`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowShortcuts`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param snapTypesByDefault: 
    :type snapTypesByDefault: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Vector: NXOpen.Vector3d = ...
    """
    Returns or sets  the Vector
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vector: 
    :type vector: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SpecifyVector = ...  # unknown typename


class Group(UIBlock):
    """
    Represents a Group Block  
    
    .. versionadded:: NX8.5.0
    """
    Column: int = ...
    """
    Returns or sets  the Column
    
    <hr>
    
    Getter Method
    
    Signature ``Column`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Column`` 
    
    :param numColumn: 
    :type numColumn: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Members: PropertyList = ...
    """
    Returns  the Members
    
    <hr>
    
    Getter Method
    
    Signature ``Members`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BlockStyler.PropertyList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: Group = ...  # unknown typename


class NodeExpandOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodeExpandOption():
    """
    Represents the Expand/Collapse option
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Collapse", "Use this option to collapse the node."
       "Expand", "Use this option to expand the node. The child node state is unaltered."
       "Toggle", "Use this option to collapse the expanded node or expand the collapsed node."
    """
    Collapse = 0  # NodeExpandOptionMemberType
    Expand = 1  # NodeExpandOptionMemberType
    Toggle = 2  # NodeExpandOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NodeScrollMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodeScroll():
    """
    Represents the scroll position to be applied on node. 
    Use one of these options to make the node appear in tree window.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Center", "Scrolls the tree to bring the node at the center of the tree window"
       "LeastScroll", "Scrolls the tree to minimal to make the node appear in tree window"
       "MostScroll", "Scrolls the tree to maximum to make the node appear in tree window"
    """
    Center = 0  # NodeScrollMemberType
    LeastScroll = 1  # NodeScrollMemberType
    MostScroll = 2  # NodeScrollMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NodeDragTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodeDragType():
    """
    Represents the drag type
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No drag"
       "All", "Drag allowed to any level in the same tree"
    """
    NotSet = 0  # NodeDragTypeMemberType
    All = 1  # NodeDragTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NodeDropTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodeDropType():
    """
    Represents the drop type
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Drop not permitted"
       "On", "Drop permitted on the target node"
       "Before", "Drop permitted before the target node"
       "After", "Drop permitted after the target node"
       "BeforeAndAfter", "Drop permitted before and after the target node"
    """
    NotSet = 0  # NodeDropTypeMemberType
    On = 1  # NodeDropTypeMemberType
    Before = 2  # NodeDropTypeMemberType
    After = 3  # NodeDropTypeMemberType
    BeforeAndAfter = 4  # NodeDropTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Node(NXOpen.TaggedObject):
    """
    Represents the node created and utilized by :py:class:`BlockStyler.Tree`.  
    
    The node represents the single row of the tree.
    
    .. versionadded:: NX7.5.0
    """
    
    class ExpandOption():
        """
        Represents the Expand/Collapse option
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Collapse", "Use this option to collapse the node."
           "Expand", "Use this option to expand the node. The child node state is unaltered."
           "Toggle", "Use this option to collapse the expanded node or expand the collapsed node."
        """
        Collapse = 0  # NodeExpandOptionMemberType
        Expand = 1  # NodeExpandOptionMemberType
        Toggle = 2  # NodeExpandOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Scroll():
        """
        Represents the scroll position to be applied on node. 
        Use one of these options to make the node appear in tree window.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Center", "Scrolls the tree to bring the node at the center of the tree window"
           "LeastScroll", "Scrolls the tree to minimal to make the node appear in tree window"
           "MostScroll", "Scrolls the tree to maximum to make the node appear in tree window"
        """
        Center = 0  # NodeScrollMemberType
        LeastScroll = 1  # NodeScrollMemberType
        MostScroll = 2  # NodeScrollMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DragType():
        """
        Represents the drag type
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No drag"
           "All", "Drag allowed to any level in the same tree"
        """
        NotSet = 0  # NodeDragTypeMemberType
        All = 1  # NodeDragTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DropType():
        """
        Represents the drop type
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Drop not permitted"
           "On", "Drop permitted on the target node"
           "Before", "Drop permitted before the target node"
           "After", "Drop permitted after the target node"
           "BeforeAndAfter", "Drop permitted before and after the target node"
        """
        NotSet = 0  # NodeDropTypeMemberType
        On = 1  # NodeDropTypeMemberType
        Before = 2  # NodeDropTypeMemberType
        After = 3  # NodeDropTypeMemberType
        BeforeAndAfter = 4  # NodeDropTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def ScrollTo(self, columnID: int, visibleOption: NodeScroll) -> None:
        """
        Scrolls horizontally and vertically to make the specific column of 
        node appear on the tree window.  
        
        Signature ``ScrollTo(columnID, visibleOption)`` 
        
        :param columnID: ColumnId of the column to which tree window scrolls horizontally. 
        :type columnID: int 
        :param visibleOption: Option to scroll the tree window vertically. 
        :type visibleOption: :py:class:`NXOpen.BlockStyler.NodeScroll` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def Expand(self, expandOption: NodeExpandOption) -> None:
        """
        Expands/collapses the node
        
        Signature ``Expand(expandOption)`` 
        
        :param expandOption: Expand option 
        :type expandOption: :py:class:`NXOpen.BlockStyler.NodeExpandOption` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetState(self) -> int:
        """
        Gets the node state associated with node state icon.  
        
        Node state is an iconic 
        representation, e.g., checked/unchecked icons for corresponding state. Node state 
        value 1 and 2 represents the standard checked and unchecked state respectively. 
        
        Signature ``GetState()`` 
        
        :returns: Node state 
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetState(self, state: int) -> None:
        """
        Sets the node state which is associated with node state icon.  
        
        Node state is an iconic 
        representation, e.g., checked/unchecked state. Setting node state to value other 
        than 1 and 2 calls BlockStyler.Tree.StateIconName callback to fetch
        the icon name. Node state can be set only after the node has been added to TreeList.
        
        Signature ``SetState(state)`` 
        
        :param state: Node state 
        :type state: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnDisplayText(self, columnID: int) -> str:
        """
        Gets the column text for the given columnId.  
        
        The text is interpreted as icon if the column display type is  
        :py:class:`BlockStyler.TreeColumnDisplay.Icon <BlockStyler.TreeColumnDisplay>`. 
        
        Signature ``GetColumnDisplayText(columnID)`` 
        
        :param columnID: Unique column id of the column. 
        :type columnID: int 
        :returns: Text associated with column. 
        :rtype: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnDisplayText(self, columnID: int, columnDisplayText: str) -> None:
        """
        Sets the text in the column which corresponds to given columnId.  
        
        The text is interpreted as icon if the column display type is  
        :py:class:`BlockStyler.TreeColumnDisplay.Icon <BlockStyler.TreeColumnDisplay>`.
        
        Signature ``SetColumnDisplayText(columnID, columnDisplayText)`` 
        
        :param columnID: Unique coulmn id of the column. 
        :type columnID: int 
        :param columnDisplayText: Text associated with column 
        :type columnDisplayText: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNodeData(self) -> NXOpen.DataContainer:
        """
        Gets node data which contains the data in the form of unique name-value pairs. 
        In this context unique name is termed as property name. There 
        could me more than one such property name - value pair, but the property name of the primary data 
        should be named "Data" (case-sensitive). For instance, if a :py:class:`BlockStyler.Node` represents a 
        feature object then property name should be "Data" and the value should be feature object. The primary data is used by NX 
        for some operations such cross selection. 
        
        Initialy the container or list is empty and it is expected that data 
        would be added to it. Additional property name - value pair can be added to the container or list, but it should be made sure that
        there is no dublicate property name exists in the container or list. The additional data can be seen as 
        book keeping information for node. At any point the node data can be fetched and value can be extracted
        using the corresponding property name. Refer to :py:class:`NXOpen.DataContainer` on how property name-value pair is added
        to the container or list.
        
        Signature ``GetNodeData()`` 
        
        :returns: Node data which is list of property name - value pair. New property name - value pair can be added to it and existing value can be fetched using corresponding property name. 
        :rtype: :py:class:`NXOpen.DataContainer` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    CrossSelection: bool = ...
    """
    Returns or sets the flag indicating whether cross section is allowed.  
    
    It is useful when the node contains :py:class:`NXOpen.DisplayableObject` as 
    data. If the flag is true then the :py:class:`NXOpen.DisplayableObject` is 
    highlighted, else not. The default value is True
    
    <hr>
    
    Getter Method
    
    Signature ``CrossSelection`` 
    
    :returns: Flag indicating whether cross selection is allowed. 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CrossSelection`` 
    
    :param crossSelection: Flag indicating whether cross selection is allowed. 
    :type crossSelection: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    DisplayIcon: str = ...
    """
    Returns or sets the display icon.  
    
    This is normal icon positioned before the node text and is 
    displayed when the node is in unselected state.
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayIcon`` 
    
    :returns: Icon. 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayIcon`` 
    
    :param icon: Icon. 
    :type icon: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    DisplayText: str = ...
    """
    Returns or sets  the display text of node.  
    
    This is same as 0th column text of this node. 
    Use :py:meth:`BlockStyler.Node.SetColumnDisplayText` to fetch the text of other column of the same node. 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayText`` 
    
    :returns: Display text 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayText`` 
    
    :param displayTest: Display text 
    :type displayTest: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    FirstChildNode: Node = ...
    """
    Returns the first child node.  
    
    Returns None if child node is not present.
    
    <hr>
    
    Getter Method
    
    Signature ``FirstChildNode`` 
    
    :returns: First child node. 
    :rtype: :py:class:`NXOpen.BlockStyler.Node` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ForegroundColor: int = ...
    """
    Returns or sets the text color of the node.  
    
    The color is applicable for whole row.
    
    <hr>
    
    Getter Method
    
    Signature ``ForegroundColor`` 
    
    :returns: Foreground color 
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ForegroundColor`` 
    
    :param nodeForgroundColor: Foreground color. 
    :type nodeForgroundColor: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    IsExpanded: bool = ...
    """
    Returns  the flag indicating whether the node is in expanded state
    
    <hr>
    
    Getter Method
    
    Signature ``IsExpanded`` 
    
    :returns: Flag indicating whether node is expanded. 
    :rtype: bool 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    IsInserted: bool = ...
    """
    Returns  the flag indicating whether the node is inserted in :py:class:`BlockStyler.Tree`
    
    <hr>
    
    Getter Method
    
    Signature ``IsInserted`` 
    
    :returns: Flag indicating whether node is inserted.  
    
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    IsSelected: bool = ...
    """
    Returns  the flag indicating whether the node is in selected state
    
    <hr>
    
    Getter Method
    
    Signature ``IsSelected`` 
    
    :returns: Flag indicating whether the node is in selected state. 
    :rtype: bool 
    
    .. versionadded:: NX7.5.3
    
    License requirements: None.
    """
    NextNode: Node = ...
    """
    Returns the next node which might not belong to the same hierarchy.  
    
    The next node either is a sibling node or belongs to other root node. 
    Returns None if next node is not present
    
    <hr>
    
    Getter Method
    
    Signature ``NextNode`` 
    
    :returns: Next node. 
    :rtype: :py:class:`NXOpen.BlockStyler.Node` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    NextSelectedNode: Node = ...
    """
    Returns the next selected node in the whole tree hierarchy.  
    
    The node on which this method is called does not have to be selected. Returns None if none of the next nodes are selected.
    
    <hr>
    
    Getter Method
    
    Signature ``NextSelectedNode`` 
    
    :returns: Selected node following the provided node. 
    :rtype: :py:class:`NXOpen.BlockStyler.Node` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    NextSiblingNode: Node = ...
    """
    Returns  the next node which belongs to the same hierarchy.  
    
    Returns None null if next sibling node is not present.
    
    <hr>
    
    Getter Method
    
    Signature ``NextSiblingNode`` 
    
    :returns: Next sibling node. 
    :rtype: :py:class:`NXOpen.BlockStyler.Node` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ParentNode: Node = ...
    """
    Returns the parent node.  
    
    Returns None if parent node is not present
    
    <hr>
    
    Getter Method
    
    Signature ``ParentNode`` 
    
    :returns: Parent node. 
    :rtype: :py:class:`NXOpen.BlockStyler.Node` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PreviousNode: Node = ...
    """
    Returns the previous node which might not belong to the same hierarchy.  
    
    Returns None null if previous node is not present
    
    <hr>
    
    Getter Method
    
    Signature ``PreviousNode`` 
    
    :returns: Previous node. 
    :rtype: :py:class:`NXOpen.BlockStyler.Node` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PreviousSelectedNode: Node = ...
    """
    Returns the previous selected node in the whole tree hierarchy.  
    
    The node on which this method is called does not have to be selected.
    Returns None if none of the previous nodes are selected.
    
    <hr>
    
    Getter Method
    
    Signature ``PreviousSelectedNode`` 
    
    :returns: Previous selected node. 
    :rtype: :py:class:`NXOpen.BlockStyler.Node` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PreviousSiblingNode: Node = ...
    """
    Returns the previous node which belongs to the same hierarchy.  
    
    Returns None if previous sibling node is not present.
    
    <hr>
    
    Getter Method
    
    Signature ``PreviousSiblingNode`` 
    
    :returns: Previous sibling node. 
    :rtype: :py:class:`NXOpen.BlockStyler.Node` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SelectedIcon: str = ...
    """
    Returns or sets the selected icon.  
    
    This icon appears on node selection and is positioned before the node text
    replacing the :py:meth:`BlockStyler.Node.DisplayIcon``.
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedIcon`` 
    
    :returns: Icon 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectedIcon`` 
    
    :param icon: Icon. 
    :type icon: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: Node = ...  # unknown typename


class SelectObjectFilterTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SelectObjectFilterType():
    """
    Indicates the general filter type for selection. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Features", "Filter to select all feature types"
       "Faces", "Filter to select all face types"
       "Edges", "Filter to select all edge types"
       "CurvesAndEdges", "Filter to select all curve and edge types"
       "Components", "Filter to select all components"
       "SolidBodies", "Filter to select all solid bodies"
       "SheetBodies", "Filter to select all sheet bodies"
    """
    Features = 1  # SelectObjectFilterTypeMemberType
    Faces = 2  # SelectObjectFilterTypeMemberType
    Edges = 4  # SelectObjectFilterTypeMemberType
    CurvesAndEdges = 8  # SelectObjectFilterTypeMemberType
    Components = 16  # SelectObjectFilterTypeMemberType
    SolidBodies = 32  # SelectObjectFilterTypeMemberType
    SheetBodies = 64  # SelectObjectFilterTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SelectObject(UIBlock):
    """
    Represents a Select Object block  
    
    .. versionadded:: NX8.5.0
    """
    
    class FilterType():
        """
        Indicates the general filter type for selection. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Features", "Filter to select all feature types"
           "Faces", "Filter to select all face types"
           "Edges", "Filter to select all edge types"
           "CurvesAndEdges", "Filter to select all curve and edge types"
           "Components", "Filter to select all components"
           "SolidBodies", "Filter to select all solid bodies"
           "SheetBodies", "Filter to select all sheet bodies"
        """
        Features = 1  # SelectObjectFilterTypeMemberType
        Faces = 2  # SelectObjectFilterTypeMemberType
        Edges = 4  # SelectObjectFilterTypeMemberType
        CurvesAndEdges = 8  # SelectObjectFilterTypeMemberType
        Components = 16  # SelectObjectFilterTypeMemberType
        SolidBodies = 32  # SelectObjectFilterTypeMemberType
        SheetBodies = 64  # SelectObjectFilterTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectModeMembers(self) -> 'list[str]':
        """
        Gets the SelectMode members 
        
        Signature ``GetSelectModeMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLastDeselectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the LastDeselectedObjects 
        
        Signature ``GetLastDeselectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLastSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the LastSelectedObjects 
        
        Signature ``GetLastSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetMaximumScopeMembers(self) -> 'list[str]':
        """
        Gets the MaximumScope members  
        
        Signature ``GetMaximumScopeMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectionFilter(self, maskAction: NXOpen.SelectionSelectionAction, maskTriples: 'list[NXOpen.SelectionMaskTriple_Struct]') -> None:
        """
        Sets the SelectionFilter
        
        Signature ``SetSelectionFilter(maskAction, maskTriples)`` 
        
        :param maskAction:  Mask action  
        :type maskAction: :py:class:`NXOpen.SelectionSelectionAction` 
        :param maskTriples:  Mask triples  
        :type maskTriples: list of :py:class:`NXOpen.SelectionMaskTriple_Struct` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def AddFilter(self, filterTypes: int) -> None:
        """
        Adds the filters for select object block
        
        This method takes the integer value of the desired enum values from 
        :py:class:`NXOpen.BlockStyler.SelectObjectFilterType`.
        
        Signature ``AddFilter(filterTypes)`` 
        
        :param filterTypes: Values from :py:class:`SelectObjectFilterType` for specifying filters  
        :type filterTypes: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def AddFilter(self, filterTypes: SelectObjectFilterType) -> None:
        """
        <summary>
        Adds the filters for select object block 
        </summary>
        
        This method takes the desired enumeration value from
        :py:class:`NXOpen.BlockStyler.SelectObjectFilterType`.
        
        Signature ``AddFilter(filterTypes)`` 
        
        :param filterTypes: Values from :py:class:`SelectObjectFilterType` for specifying filters  
        :type filterTypes: :py:class:`NXOpen.BlockStyler.SelectObjectFilterType` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def AddFilter(self, type: int, subType: int, solidBodyType: int) -> None:
        """
        Adds the filter for select object block using type, subtype and solidBodyType 
        
        Signature ``AddFilter(type, subType, solidBodyType)`` 
        
        :param type:  Object type. This can be one of the object types that are listed in                                         uf_object_types.h. For example, for point,                                         use UF_point_type in C++ and                                        NXOpen.UF.UFConstants.UF_point_type in .NET.  
        :type type: int 
        :param subType:  Object subtype. This can either be -1 (UF_all_subtype) for any subtype, or a                                        subtype of the selected type.                                        The subtypes are listed in uf_object_types.h.  
        :type subType: int 
        :param solidBodyType:  Solid body subtype. This is only meaningful when the type is                                          UF_solid_type.  In that case, this should be set to                                         one of the solid type constants listed in uf_ui_types.h                                          under "Constants for selection solid_type".                                          When this is used, subtype does not matter.                                         For example, to select any face, use UF_UI_SEL_FEATURE_ANY_FACE in C++ and                                          NXOpen.UF.UFConstants.UF_UI_SEL_FEATURE_ANY_FACE in .NET  
        :type solidBodyType: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetFilter(self) -> None:
        """
        Resets the filter for select object block 
        
        Signature ``ResetFilter()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AllowConvergentObject: bool = ...
    """
    Returns or sets  the AllowConvergentObject
    
    <hr>
    
    Getter Method
    
    Signature ``AllowConvergentObject`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowConvergentObject`` 
    
    :param allowConvergentObject: 
    :type allowConvergentObject: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BlendVirtualCurveOverlay: bool = ...
    """
    Returns or sets  the BlendVirtualCurveOverlay.  
    
    If true, virtual curve is displayed during preselection.
    
    <hr>
    
    Getter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :param blendCurve: 
    :type blendCurve: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumScopeAsString: str = ...
    """
    Returns or sets  the MaximumScope as string
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumScopeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumScopeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PickPoint: NXOpen.Point3d = ...
    """
    Returns  the PickPoint
    
    <hr>
    
    Getter Method
    
    Signature ``PickPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PointOverlay: bool = ...
    """
    Returns or sets  the PointOverlay.  
    
    If true,on the fly point creation is allowed.
    
    <hr>
    
    Getter Method
    
    Signature ``PointOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PointOverlay`` 
    
    :param pointOverlay: 
    :type pointOverlay: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectModeAsString: str = ...
    """
    Returns or sets  the SelectMode as string
    
    <hr>
    
    Getter Method
    
    Signature ``SelectModeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectModeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SmartUpdateOptionAsString: str = ...
    """
    Returns or sets  the update option for points created by the point overlay.  
    
    Acceptable values are:
    
      *  **Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).
      *  **After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.
      *  **After Parent Body</b> The smart object will always update after the last feature on the parent body.
      *  **Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.
    
    <hr>
    
    Getter Method
    
    Signature ``SmartUpdateOptionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SmartUpdateOptionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.1
    
    License requirements: None.
    """
    SnapPointTypesEnabled: int = ...
    """
    Returns or sets  the SnapPointTypesEnabled
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesEnabled`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesEnabled`` 
    
    :param typesEnabled: 
    :type typesEnabled: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param typesByDefault: 
    :type typesByDefault: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ToolTip: str = ...
    """
    Returns or sets  the ToolTip
    
    <hr>
    
    Getter Method
    
    Signature ``ToolTip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolTip`` 
    
    :param toolTip: 
    :type toolTip: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SelectObject = ...  # unknown typename


class TextColorFontWidth(UIBlock):
    """
    Represents a Line Width block  
    
    .. versionadded:: NX9.0.0
    """
    
    def GetColorValue(self) -> 'list[int]':
        """
        Gets text color values 
        
        Signature ``GetColorValue()`` 
        
        :returns: color values to get from the property 
        :rtype: list of int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColorValue(self, colorValueVector: 'list[int]') -> None:
        """
        Sets text color values
        
        Signature ``SetColorValue(colorValueVector)`` 
        
        :param colorValueVector: color values to set for the property.  
        :type colorValueVector: list of int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsNxFont(self) -> bool:
        """
        Returns the whether selected font is nx font or standard font.  
        
        Signature ``IsNxFont()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    AvailableFontTypesAsString: str = ...
    """
    Returns or sets  the available font types.  
    
    <hr>
    
    Getter Method
    
    Signature ``AvailableFontTypesAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AvailableFontTypesAsString`` 
    
    :param availableFontTypes: 
    :type availableFontTypes: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FontValue: str = ...
    """
    Returns or sets  the font value
    
    <hr>
    
    Getter Method
    
    Signature ``FontValue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FontValue`` 
    
    :param fontValue: 
    :type fontValue: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LayoutAsString: str = ...
    """
    Returns or sets  the layout.  
    
    <hr>
    
    Getter Method
    
    Signature ``LayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayoutAsString`` 
    
    :param layoutString: 
    :type layoutString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    StandardFontStyle: str = ...
    """
    Returns or sets  the standard font style.  
    
    <hr>
    
    Getter Method
    
    Signature ``StandardFontStyle`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StandardFontStyle`` 
    
    :param fontStyle: 
    :type fontStyle: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    WidthValueAsString: str = ...
    """
    Returns or sets  the width value.  
    
    <hr>
    
    Getter Method
    
    Signature ``WidthValueAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WidthValueAsString`` 
    
    :param widthValueString: 
    :type widthValueString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: TextColorFontWidth = ...  # unknown typename


class WizardTaskNavigatorItemMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WizardTaskNavigatorItem():
    """
    Specifies an item in the Task Navigator.  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Step", " - "
       "SubNode", " - "
       "Background", " - "
    """
    Step = 0  # WizardTaskNavigatorItemMemberType
    SubNode = 1  # WizardTaskNavigatorItemMemberType
    Background = 2  # WizardTaskNavigatorItemMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class WizardSubNodeActionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WizardSubNodeAction():
    """
    Specifies the type of action performed on a sub-node in the Wizard Task Navigator.
    The action is passed into the callback BlockStyler.Wizard.OnSubNodeCallback. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Select", "Sub-node has been selected."
       "Deselect", "Sub-node has been deselected."
       "Check", "Sub-node has been checked if a checkbox was specified."
       "Uncheck", "Sub-node has been unchecked if a checkbox was specified."
    """
    Select = 0  # WizardSubNodeActionMemberType
    Deselect = 1  # WizardSubNodeActionMemberType
    Check = 2  # WizardSubNodeActionMemberType
    Uncheck = 3  # WizardSubNodeActionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Wizard(UIBlock):
    """
    Represents a Wizard block   
    
    .. versionadded:: NX7.5.0
    """
    
    class TaskNavigatorItem():
        """
        Specifies an item in the Task Navigator.  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Step", " - "
           "SubNode", " - "
           "Background", " - "
        """
        Step = 0  # WizardTaskNavigatorItemMemberType
        SubNode = 1  # WizardTaskNavigatorItemMemberType
        Background = 2  # WizardTaskNavigatorItemMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SubNodeAction():
        """
        Specifies the type of action performed on a sub-node in the Wizard Task Navigator.
        The action is passed into the callback BlockStyler.Wizard.OnSubNodeCallback. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Select", "Sub-node has been selected."
           "Deselect", "Sub-node has been deselected."
           "Check", "Sub-node has been checked if a checkbox was specified."
           "Uncheck", "Sub-node has been unchecked if a checkbox was specified."
        """
        Select = 0  # WizardSubNodeActionMemberType
        Deselect = 1  # WizardSubNodeActionMemberType
        Check = 2  # WizardSubNodeActionMemberType
        Uncheck = 3  # WizardSubNodeActionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreateStepSubNode(self, step: int, text: str, bitmap: str, showCheckBox: bool, checkBoxChecked: bool) -> int:
        """
        Create a sub-node for a step in the Task Navigator.  
        
        Signature ``CreateStepSubNode(step, text, bitmap, showCheckBox, checkBoxChecked)`` 
        
        :param step:  The step to add a sub-node.  
        :type step: int 
        :param text:  Text for the sub-node.  
        :type text: str 
        :param bitmap:  Optional bitmap for the sub-node.  
        :type bitmap: str 
        :param showCheckBox:  Associate an optional check box with the sub-node  
        :type showCheckBox: bool 
        :param checkBoxChecked:  The initial state of the check box.  
        :type checkBoxChecked: bool 
        :returns:  Unique id for the sub-node.  
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveStepSubNode(self, subNodeId: int) -> None:
        """
        Remove a sub-node in the Task Navigator.  
        
        Signature ``RemoveStepSubNode(subNodeId)`` 
        
        :param subNodeId:  The sub-node id.  
        :type subNodeId: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateMenu(self) -> TreeListMenu:
        """
        Creates a popup menu.  
        
        Use :py:meth:`BlockStyler.Wizard.SetMenu` to set
        the created menu.  See the :py:class:`BlockStyler.TreeListMenu` for
        information on creating a menu.   
        
        Signature ``CreateMenu()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.BlockStyler.TreeListMenu` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMenu(self, menu: TreeListMenu) -> None:
        """
        Set the menu items for the popup menu for a step, sub-node or the background
        in the Task Navigator.  
        
        See the :py:class:`BlockStyler.TreeListMenu` for
        information on creating a menu.
        
        Signature ``SetMenu(menu)`` 
        
        :param menu: 
        :type menu: :py:class:`NXOpen.BlockStyler.TreeListMenu` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetStepNotifyPreHandler(self, cb: typing.Callable) -> None:
        """
        Sets the StepNotifyPre handler.  
        
        Signature ``SetStepNotifyPreHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetStepNotifyPostHandler(self, cb: typing.Callable) -> None:
        """
        Sets the StepNotifyPost handler.  
        
        Signature ``SetStepNotifyPostHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetIsStepOkayHandler(self, cb: typing.Callable) -> None:
        """
        Sets the IsStepOkay handler.  
        
        Signature ``SetIsStepOkayHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnSubNodeHandler(self, cb: typing.Callable) -> None:
        """
        Sets the OnSubNode handler.  
        
        Signature ``SetOnSubNodeHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnMenuHandler(self, cb: typing.Callable) -> None:
        """
        Sets the OnMenu handler.  
        
        Signature ``SetOnMenuHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOnMenuSelectionHandler(self, cb: typing.Callable) -> None:
        """
        Sets the OnMenuSelection handler.  
        
        Signature ``SetOnMenuSelectionHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepBannerBitmaps(self) -> 'list[str]':
        """
        Gets the StepBannerBitmaps.  
        
        Gets the list of bitmaps for the step bitmaps in the banner area. 
        
        Signature ``GetStepBannerBitmaps()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetStepBannerBitmaps(self, bitmaps: 'list[str]') -> None:
        """
        Sets the StepBannerBitmaps.  
        
        Sets the list of bitmaps for the step bitmaps in the banner area.
        
        Signature ``SetStepBannerBitmaps(bitmaps)`` 
        
        :param bitmaps: 
        :type bitmaps: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepBitmaps(self) -> 'list[str]':
        """
        Gets the StepBitmaps.  
        
        Gets the list of bitmaps for the node bitmaps in the Task Navigator. 
        
        Signature ``GetStepBitmaps()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetStepBitmaps(self, bitmaps: 'list[str]') -> None:
        """
        Sets the StepBitmaps.  
        
        Sets the list of bitmaps for the node bitmaps in the Task Navigator.
        
        Signature ``SetStepBitmaps(bitmaps)`` 
        
        :param bitmaps: 
        :type bitmaps: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepCues(self) -> 'list[str]':
        """
        Gets the StepCues.  
        
        Gets the list of cue lines for the wizard steps. 
        
        Signature ``GetStepCues()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetStepCues(self, cues: 'list[str]') -> None:
        """
        Sets the StepCues.  
        
        Sets the list of cue lines for the wizard steps.
        
        Signature ``SetStepCues(cues)`` 
        
        :param cues: 
        :type cues: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepText(self) -> 'list[str]':
        """
        Gets the StepText.  
        
        Gets the list of step descriptions for the banner area. 
        
        Signature ``GetStepText()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetStepText(self, text: 'list[str]') -> None:
        """
        Sets the StepText.  
        
        Sets the list of step descriptions for the banner area.
        
        Signature ``SetStepText(text)`` 
        
        :param text: 
        :type text: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    CurrentStep: int = ...
    """
    Returns or sets  the CurrentStep.  
    
    <hr>
    
    Getter Method
    
    Signature ``CurrentStep`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurrentStep`` 
    
    :param currentStep: 
    :type currentStep: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HighQualityBitmap: bool = ...
    """
    Returns or sets  the HighQualityBitmap.  
    
    <hr>
    
    Getter Method
    
    Signature ``HighQualityBitmap`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HighQualityBitmap`` 
    
    :param highQuality: 
    :type highQuality: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize.  
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Members: PropertyList = ...
    """
    Returns  the Members
    
    <hr>
    
    Getter Method
    
    Signature ``Members`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BlockStyler.PropertyList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowTaskNavigator: bool = ...
    """
    Returns or sets  the ShowTaskNavigator.  
    
    <hr>
    
    Getter Method
    
    Signature ``ShowTaskNavigator`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowTaskNavigator`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: Wizard = ...  # unknown typename


class TreeListMenu(NXOpen.TransientObject):
    """
    Represents a menu class utilized by :py:class:`BlockStyler.Tree`.  
    
    Refer to :py:meth:`BlockStyler.Tree.CreateMenu` to create the menu.
    
    .. versionadded:: NX7.5.0
    """
    
    @typing.overload
    def AddMenuItem(self, menuItemID: int, menuItemText: str) -> None:
        """
        Adds single menu item 
        
        Signature ``AddMenuItem(menuItemID, menuItemText)`` 
        
        :param menuItemID:  Unique identifier for the menu item being added  
        :type menuItemID: int 
        :param menuItemText:  Display text for menu item being added 
        :type menuItemText: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def AddMenuItem(self, menuItemID: int, menuItemText: str, icon: str) -> None:
        """
        Adds single menu item 
        
        Signature ``AddMenuItem(menuItemID, menuItemText, icon)`` 
        
        :param menuItemID:  Unique identifier for the menu item being added  
        :type menuItemID: int 
        :param menuItemText:  Display text for menu item being added 
        :type menuItemText: str 
        :param icon:  Icon for menu item being added 
        :type icon: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AddSeperator(self) -> None:
        """
        Adds a separator 
        
        Signature ``AddSeperator()`` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`BlockStyler.TreeListMenu.AddSeparator` instead.
        
        License requirements: None.
        """
        ...
    
    
    def AddSeparator(self) -> None:
        """
        Adds a separator 
        
        Signature ``AddSeparator()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSubMenu(self, menuItemID: int, subMenu: TreeListMenu) -> None:
        """
        Sets a submenu.  
        
        Submenu can be created using :py:meth:`BlockStyler.Tree.CreateMenu` method
        
        Signature ``SetSubMenu(menuItemID, subMenu)`` 
        
        :param menuItemID:  Menu Item ID of menu item on which submenu is supposed to be set. 
        :type menuItemID: int 
        :param subMenu:  Menu to be added as submenu  
        :type subMenu: :py:class:`NXOpen.BlockStyler.TreeListMenu` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemChecked(self, menuItemID: int) -> bool:
        """
        Gets the checked status for given menu item  
        
        Signature ``GetItemChecked(menuItemID)`` 
        
        :param menuItemID:  Menu-item ID   
        :type menuItemID: int 
        :returns:  Status  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItemChecked(self, menuItemID: int, checkedStatusStatus: bool) -> None:
        """
        Sets the checked status for given menu item 
        
        Signature ``SetItemChecked(menuItemID, checkedStatusStatus)`` 
        
        :param menuItemID:  Menu-item ID   
        :type menuItemID: int 
        :param checkedStatusStatus:  Status  
        :type checkedStatusStatus: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemDisable(self, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is disabled  
        
        Signature ``GetItemDisable(menuItemID)`` 
        
        :param menuItemID:  Menu-item ID   
        :type menuItemID: int 
        :returns:  Status  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItemDisable(self, menuItemID: int, disableStatus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is disabled 
        
        Signature ``SetItemDisable(menuItemID, disableStatus)`` 
        
        :param menuItemID:  Menu-item ID   
        :type menuItemID: int 
        :param disableStatus:  Status  
        :type disableStatus: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemDefault(self, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is default  
        
        Signature ``GetItemDefault(menuItemID)`` 
        
        :param menuItemID:  Menu-item ID   
        :type menuItemID: int 
        :returns:  Status  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItemDefault(self, menuItemID: int, defaultStatus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is default 
        
        Signature ``SetItemDefault(menuItemID, defaultStatus)`` 
        
        :param menuItemID:  Menu-item ID   
        :type menuItemID: int 
        :param defaultStatus:  Status  
        :type defaultStatus: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemHidden(self, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is hidden  
        
        Signature ``GetItemHidden(menuItemID)`` 
        
        :param menuItemID:  Menu-item ID   
        :type menuItemID: int 
        :returns:  Status  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItemHidden(self, menuItemID: int, hiddenStatus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is hidden 
        
        Signature ``SetItemHidden(menuItemID, hiddenStatus)`` 
        
        :param menuItemID:  Menu-item ID   
        :type menuItemID: int 
        :param hiddenStatus:  Status  
        :type hiddenStatus: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemDialogLaunching(self, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is dialog lanching  
        
        Signature ``GetItemDialogLaunching(menuItemID)`` 
        
        :param menuItemID:  Menu-item ID   
        :type menuItemID: int 
        :returns:  Status  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItemDialogLaunching(self, menuItemID: int, dialogLaunchingStaus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is dialog lanching 
        
        Signature ``SetItemDialogLaunching(menuItemID, dialogLaunchingStaus)`` 
        
        :param menuItemID:  Menu-item ID   
        :type menuItemID: int 
        :param dialogLaunchingStaus:  Status  
        :type dialogLaunchingStaus: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemIcon(self, menuItemID: int) -> str:
        """
        Gets the icon for given menu item  
        
        Signature ``GetItemIcon(menuItemID)`` 
        
        :param menuItemID:  Menu-item ID  
        :type menuItemID: int 
        :returns:  Display text  
        :rtype: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItemIcon(self, menuItemID: int, icon: str) -> None:
        """
        Sets the icon for given menu item 
        
        Signature ``SetItemIcon(menuItemID, icon)`` 
        
        :param menuItemID:  Menu-item ID  
        :type menuItemID: int 
        :param icon:  Display text  
        :type icon: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemText(self, menuItemID: int) -> str:
        """
        Gets the display text for given menu item  
        
        Signature ``GetItemText(menuItemID)`` 
        
        :param menuItemID:  Menu-item ID  
        :type menuItemID: int 
        :returns:  Display text  
        :rtype: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItemText(self, menuItemID: int, text: str) -> None:
        """
        Sets the display text for given menu item 
        
        Signature ``SetItemText(menuItemID, text)`` 
        
        :param menuItemID:  Menu-item ID  
        :type menuItemID: int 
        :param text:  Display text  
        :type text: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    


class Toggle(UIBlock):
    """
    Represents a Toggle block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout member 
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipOffImage: str = ...
    """
    Returns or sets  the BalloonTooltipOffImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipOffImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipOffImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipOffText: str = ...
    """
    Returns or sets  the BalloonTooltipOffText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipOffText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipOffText`` 
    
    :param tooltipString: 
    :type tooltipString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipOnImage: str = ...
    """
    Returns or sets  the BalloonTooltipOnImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipOnImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipOnImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipOnText: str = ...
    """
    Returns or sets  the BalloonTooltipOnText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipOnText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipOnText`` 
    
    :param tooltipString: 
    :type tooltipString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BitmapOnly: bool = ...
    """
    Returns or sets  the BitmapOnly
    
    <hr>
    
    Getter Method
    
    Signature ``BitmapOnly`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BitmapOnly`` 
    
    :param bitmapOnly: 
    :type bitmapOnly: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Value: bool = ...
    """
    Returns or sets  the Value
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param valueProperty: 
    :type valueProperty: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: Toggle = ...  # unknown typename


class SpecifyAxis(UIBlock):
    """
    Represents a Specify Axis block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipPointImage: str = ...
    """
    Returns or sets  the BalloonTooltipPointImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipPointImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipPointImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipPointText: str = ...
    """
    Returns or sets  the BalloonTooltipPointText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipPointText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipPointText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipVectorImage: str = ...
    """
    Returns or sets  the BalloonTooltipVectorImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipVectorImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipVectorImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipVectorText: str = ...
    """
    Returns or sets  the BalloonTooltipVectorText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipVectorText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipVectorText`` 
    
    :param tooltipText: 
    :type tooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SpecifyAxis = ...  # unknown typename


class SelectFeature(UIBlock):
    """
    Represents a Select Feature block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectModeMembers(self) -> 'list[str]':
        """
        Gets the SelectMode members 
        
        Signature ``GetSelectModeMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BlendVirtualCurveOverlay: bool = ...
    """
    Returns or sets  the BlendVirtualCurveOverlay.  
    
    If true, virtual curve is displayed during pre-selection.
    
    <hr>
    
    Getter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :param blendCurve: 
    :type blendCurve: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectModeAsString: str = ...
    """
    Returns or sets  the SelectMode as string
    
    <hr>
    
    Getter Method
    
    Signature ``SelectModeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectModeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ToolTip: str = ...
    """
    Returns or sets  the ToolTip
    
    <hr>
    
    Getter Method
    
    Signature ``ToolTip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolTip`` 
    
    :param toolTip: 
    :type toolTip: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SelectFeature = ...  # unknown typename


class LineWidth(UIBlock):
    """
    Represents a Line Width block  
    
    .. versionadded:: NX8.5.0
    """
    AllowDefaultWidth: bool = ...
    """
    Returns  the AllowDefaultWidth
    
    <hr>
    
    Getter Method
    
    Signature ``AllowDefaultWidth`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    AllowNoChangeWidth: bool = ...
    """
    Returns  the AllowNoChangeWidth.  
    
    If true, no change in width is allowed.
    
    <hr>
    
    Getter Method
    
    Signature ``AllowNoChangeWidth`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelVisibility: bool = ...
    """
    Returns or sets  the LabelVisibility
    
    <hr>
    
    Getter Method
    
    Signature ``LabelVisibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelVisibility`` 
    
    :param visible: 
    :type visible: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LineWidthValue: int = ...
    """
    Returns or sets  the LineWidthValue
    
    <hr>
    
    Getter Method
    
    Signature ``LineWidthValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineWidthValue`` 
    
    :param widthValue: 
    :type widthValue: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowDefaultAsOriginal: bool = ...
    """
    Returns  the ShowDefaultAsOriginal.  
    
    If true, default entry is shown as original.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowDefaultAsOriginal`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: LineWidth = ...  # unknown typename


class OnPathDimension(UIBlock):
    """
    Represents a On Path Dimension block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Values to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLocationOptionMembers(self) -> 'list[str]':
        """
        Gets the LocationOption members 
        
        Signature ``GetLocationOptionMembers()`` 
        
        :returns:  Values to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AdaptiveScaleLimits: bool = ...
    """
    Returns or sets the AdaptiveScaleLimits.  
    
    If true, indicates that the scale should be adaptive.
    
    <hr>
    
    Getter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :param scaleLimits: 
    :type scaleLimits: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ExpressionObject: NXOpen.TaggedObject = ...
    """
    Returns or sets  the ExpressionObject
    
    <hr>
    
    Getter Method
    
    Signature ``ExpressionObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpressionObject`` 
    
    :param expressionObj: 
    :type expressionObj: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Formula: str = ...
    """
    Returns or sets  the Formula
    
    <hr>
    
    Getter Method
    
    Signature ``Formula`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Formula`` 
    
    :param formula: 
    :type formula: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LineIncrement: float = ...
    """
    Returns or sets the LineIncrement value.  
    
    Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
    
    <hr>
    
    Getter Method
    
    Signature ``LineIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineIncrement`` 
    
    :param lineIncrement: 
    :type lineIncrement: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LocationOptionAsString: str = ...
    """
    Returns or sets  the LocationOption as string
    
    <hr>
    
    Getter Method
    
    Signature ``LocationOptionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LocationOptionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaxInclusive: bool = ...
    """
    Returns or sets  the MaxInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MaxInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxInclusive`` 
    
    :param maxInclusive: 
    :type maxInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumValue: float = ...
    """
    Returns or sets  the MaximumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumValue`` 
    
    :param maxValue: 
    :type maxValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinInclusive: bool = ...
    """
    Returns or sets  the MinInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MinInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinInclusive`` 
    
    :param minInclusive: 
    :type minInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinimumValue: float = ...
    """
    Returns or sets  the MinimumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumValue`` 
    
    :param minValue: 
    :type minValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    OptionMask: int = ...
    """
    Returns or sets  the OptionMask
    
    <hr>
    
    Getter Method
    
    Signature ``OptionMask`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OptionMask`` 
    
    :param maskVal: 
    :type maskVal: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    OptionMenuTitle: str = ...
    """
    Returns or sets  the OptionMenuTitle
    
    <hr>
    
    Getter Method
    
    Signature ``OptionMenuTitle`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OptionMenuTitle`` 
    
    :param menuTitleText: 
    :type menuTitleText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PageIncrement: float = ...
    """
    Returns or sets the PageIncrement value.  
    
    Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    Only available when PresentationStyle  is set to Scale or ScaleKeyin.
    
    <hr>
    
    Getter Method
    
    Signature ``PageIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PageIncrement`` 
    
    :param pageIncrement: 
    :type pageIncrement: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Path: NXOpen.TaggedObject = ...
    """
    Returns or sets  the Path
    
    <hr>
    
    Getter Method
    
    Signature ``Path`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Path`` 
    
    :param path: 
    :type path: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowFocusHandle: bool = ...
    """
    Returns or sets  the ShowFocusHandle
    
    <hr>
    
    Getter Method
    
    Signature ``ShowFocusHandle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowFocusHandle`` 
    
    :param showFocus: 
    :type showFocus: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       This call can be safely removed as this is now a no-op.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param pointType: 
    :type pointType: int 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       This call can be safely removed as this is now a no-op.
    
    License requirements: None.
    """
    Units: NXOpen.TaggedObject = ...
    """
    Returns or sets  the Units
    
    <hr>
    
    Getter Method
    
    Signature ``Units`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Units`` 
    
    :param units: 
    :type units: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Value: float = ...
    """
    Returns or sets  the Value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param dimensionValue: 
    :type dimensionValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WithScale: bool = ...
    """
    Returns or sets  the WithScale.  
    
    If true,the slider bar is shown.
    
    <hr>
    
    Getter Method
    
    Signature ``WithScale`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WithScale`` 
    
    :param withScale: 
    :type withScale: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: OnPathDimension = ...  # unknown typename


class Explorer(UIBlock):
    """
    Represents an Explorer block.  
    
    The Explorer block allows for collecting a large number of inputs into a single dialog.
    The inputs are organized into nodes and sub-nodes on a tree to allow for quick and easy navigation.  The Explorer
    block provides the ability to have up to 3 levels of nodes in the Navigation Tree.  Each node contains groups and
    individual inputs that are laid out like standard NX dialogs.  When selecting level 1 and level 2 nodes that do not
    contain any groups and only contain sub-nodes the first sub-node containing groups is highlighted and its content shown.
    
    .. versionadded:: NX9.0.0
    """
    
    def SetChildMembers(self, parentMember: UIBlock, childMembers: 'list[UIBlock]') -> None:
        """
        Sets the parent member for the child members in the Explorer Navigation Tree.  
        
        The maximum
        Navigation Tree depth is 3 levels.  An exception is thrown if the parent member depth is
        already at the maximum allowed depth. 
        
        Signature ``SetChildMembers(parentMember, childMembers)`` 
        
        :param parentMember:  Parent member for the child members.  
        :type parentMember: :py:class:`NXOpen.BlockStyler.UIBlock` 
        :param childMembers:  Child members for the parent member.  
        :type childMembers: list of :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNotifyNodeSelectedPreHandler(self, cb: typing.Callable) -> None:
        """
        Sets the NotifyNodeSelectedPre handler.  
        
        Signature ``SetNotifyNodeSelectedPreHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNotifyNodeSelectedPostHandler(self, cb: typing.Callable) -> None:
        """
        Sets the NotifyNodeSelectedPost handler.  
        
        Signature ``SetNotifyNodeSelectedPostHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    CurrentNode: int = ...
    """
    Returns or sets  the CurrentNode selected in the Navigation Tree.  
    
    <hr>
    
    Getter Method
    
    Signature ``CurrentNode`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurrentNode`` 
    
    :param currentNode: 
    :type currentNode: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the localization of the block label.  
    
    If the label matches an English string in the NX string
    localization databse and the Localize property is set to true, then the Label is translated
    to the current locale language. 
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Members: PropertyList = ...
    """
    Returns  the members.  
    
    <hr>
    
    Getter Method
    
    Signature ``Members`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BlockStyler.PropertyList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TreeWidth: int = ...
    """
    Returns or sets  the TreeWidth for the Navigation Tree.  
    
    <hr>
    
    Getter Method
    
    Signature ``TreeWidth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TreeWidth`` 
    
    :param treeWidth: 
    :type treeWidth: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: Explorer = ...  # unknown typename


class LineFont(UIBlock):
    """
    Represents a Line Width block  
    
    .. versionadded:: NX9.0.0
    """
    AvailableOptions: int = ...
    """
    Returns or sets  the Available Options
    
    <hr>
    
    Getter Method
    
    Signature ``AvailableOptions`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AvailableOptions`` 
    
    :param availableOptions: 
    :type availableOptions: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowOptionLabels: bool = ...
    """
    Returns or sets  the show option labels
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOptionLabels`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOptionLabels`` 
    
    :param showOptionLabels: 
    :type showOptionLabels: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ValueAsString: str = ...
    """
    Returns or sets  the value
    
    <hr>
    
    Getter Method
    
    Signature ``ValueAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValueAsString`` 
    
    :param fontValueString: 
    :type fontValueString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: LineFont = ...  # unknown typename


class LayerBlock(UIBlock):
    """
    Represents a Layer block  
    
    .. versionadded:: NX10.0.0
    """
    LayerOption: int = ...
    """
    Returns or sets  the Layer Option
    
    <hr>
    
    Getter Method
    
    Signature ``LayerOption`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayerOption`` 
    
    :param integerLayerOption: 
    :type integerLayerOption: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LayerValue: int = ...
    """
    Returns or sets  the Layer Value
    
    <hr>
    
    Getter Method
    
    Signature ``LayerValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayerValue`` 
    
    :param inetegerLayerValue: 
    :type inetegerLayerValue: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ShowMaintainLayerOption: bool = ...
    """
    Returns or sets  the Show Maintain Layer Option
    If set to true, Maintain option is displayed in layer options
    
    <hr>
    
    Getter Method
    
    Signature ``ShowMaintainLayerOption`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowMaintainLayerOption`` 
    
    :param showMaintainLayerOption: 
    :type showMaintainLayerOption: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ShowOriginalLayerOption: bool = ...
    """
    Returns or sets  the Show Original Layer Option
    If set to true, Original option is displayed in layer options
    
    <hr>
    
    Getter Method
    
    Signature ``ShowOriginalLayerOption`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowOriginalLayerOption`` 
    
    :param showOriginalLayerOption: 
    :type showOriginalLayerOption: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ShowUserDefinedLayerOption: bool = ...
    """
    Returns or sets  the Show User Defined Layer Option
    If set to true, User Defined option is displayed in layer options
    
    <hr>
    
    Getter Method
    
    Signature ``ShowUserDefinedLayerOption`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowUserDefinedLayerOption`` 
    
    :param showUserDefinedLayerOption: 
    :type showUserDefinedLayerOption: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ShowWorkLayerOption: bool = ...
    """
    Returns or sets  the Show Work Layer Option
    If set to true, Work option is displayed in layer options
    
    <hr>
    
    Getter Method
    
    Signature ``ShowWorkLayerOption`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowWorkLayerOption`` 
    
    :param showWorkLayerOption: 
    :type showWorkLayerOption: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: LayerBlock = ...  # unknown typename


class LineColorFontWidth(UIBlock):
    """
    Represents a Line Width block  
    
    .. versionadded:: NX9.0.0
    """
    
    def GetColorValue(self) -> 'list[int]':
        """
        Gets line color values 
        
        Signature ``GetColorValue()`` 
        
        :returns: color values to get from the property 
        :rtype: list of int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColorValue(self, colorValueVector: 'list[int]') -> None:
        """
        Sets line color values
        
        Signature ``SetColorValue(colorValueVector)`` 
        
        :param colorValueVector: color values to set for the property.  
        :type colorValueVector: list of int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    HideSubBlocksAsString: str = ...
    """
    Returns or sets  the hide sub block.  
    
    <hr>
    
    Getter Method
    
    Signature ``HideSubBlocksAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HideSubBlocksAsString`` 
    
    :param hideSubBlocksString: 
    :type hideSubBlocksString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the Label String in horizontal layout.  
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LayoutAsString: str = ...
    """
    Returns or sets  the layout.  
    
    <hr>
    
    Getter Method
    
    Signature ``LayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayoutAsString`` 
    
    :param layoutString: 
    :type layoutString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LineFontAvailableOptions: int = ...
    """
    Returns or sets  the Line Font Available Options
    
    <hr>
    
    Getter Method
    
    Signature ``LineFontAvailableOptions`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineFontAvailableOptions`` 
    
    :param lineFontAvailableOptions: 
    :type lineFontAvailableOptions: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LineFontValueAsString: str = ...
    """
    Returns or sets  the Line Font Value.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineFontValueAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineFontValueAsString`` 
    
    :param fontValueString: 
    :type fontValueString: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LineWidthShowDefault: bool = ...
    """
    Returns or sets  the Line width Show Default
    
    <hr>
    
    Getter Method
    
    Signature ``LineWidthShowDefault`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineWidthShowDefault`` 
    
    :param lineWidthShowDefault: 
    :type lineWidthShowDefault: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LineWidthShowDefaultAsOriginal: bool = ...
    """
    Returns or sets  the Line Width Show Default as Original
    
    <hr>
    
    Getter Method
    
    Signature ``LineWidthShowDefaultAsOriginal`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineWidthShowDefaultAsOriginal`` 
    
    :param lineWidthShowDefaultAsOriginal: 
    :type lineWidthShowDefaultAsOriginal: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LineWidthShowNoChange: bool = ...
    """
    Returns or sets  the Line Width Show No Change
    
    <hr>
    
    Getter Method
    
    Signature ``LineWidthShowNoChange`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineWidthShowNoChange`` 
    
    :param lineWidthShowNoChange: 
    :type lineWidthShowNoChange: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LineWidthUseWideLines: bool = ...
    """
    Returns or sets  the Line Width Use Wide Lines
    
    <hr>
    
    Getter Method
    
    Signature ``LineWidthUseWideLines`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineWidthUseWideLines`` 
    
    :param lineWidthUseWideLines: 
    :type lineWidthUseWideLines: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ShowLabel: bool = ...
    """
    Returns or sets  the Show Label flag.  
    
    If true, the block label is shown in horizontal layout.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowLabel`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowLabel`` 
    
    :param showLabel: 
    :type showLabel: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: LineColorFontWidth = ...  # unknown typename


class ReverseDirection(UIBlock):
    """
    Represents Reverse Direction block  
    
    .. versionadded:: NX8.5.0
    """
    Direction: NXOpen.Vector3d = ...
    """
    Returns or sets  the Direction.  
    
    It specifies the orientation of direction handle.
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Flip: bool = ...
    """
    Returns or sets  the Flip.  
    
    If true, the handle is flipped opposite of the direction.
    
    <hr>
    
    Getter Method
    
    Signature ``Flip`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Flip`` 
    
    :param flip: 
    :type flip: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Origin: NXOpen.Point3d = ...
    """
    Returns or sets  the Origin.  
    
    It specifies the origin of direction handle.
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Origin`` 
    
    :param origin: 
    :type origin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: ReverseDirection = ...  # unknown typename


class Microposition(UIBlock):
    """
    Represents a Microposition block  
    
    .. versionadded:: NX8.5.0
    """
    Null: Microposition = ...  # unknown typename


class Button(UIBlock):
    """
    Represents a button  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout member  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get for given name.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HighQualityBitmap: bool = ...
    """
    Returns or sets  the HighQualityBitmap
    
    <hr>
    
    Getter Method
    
    Signature ``HighQualityBitmap`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HighQualityBitmap`` 
    
    :param hishQuality: 
    :type hishQuality: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Tooltip: str = ...
    """
    Returns or sets  the Tooltip
    
    <hr>
    
    Getter Method
    
    Signature ``Tooltip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Tooltip`` 
    
    :param tooltipString: 
    :type tooltipString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: Button = ...  # unknown typename


class SpecifyOrientation(UIBlock):
    """
    Represents Specify Orientation block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EnableDoubleClickFlip: bool = ...
    """
    Returns or sets  the EnableDoubleClickFlip.  
    
    If true, flipping is allowed when direction handle is double clicked.
    
    <hr>
    
    Getter Method
    
    Signature ``EnableDoubleClickFlip`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnableDoubleClickFlip`` 
    
    :param enableFlip: 
    :type enableFlip: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EnableFacetSelection: bool = ...
    """
    Returns or sets  the EnableFacetSelection
    
    <hr>
    
    Getter Method
    
    Signature ``EnableFacetSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnableFacetSelection`` 
    
    :param enableSelection: 
    :type enableSelection: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    HasOriginGwif: bool = ...
    """
    Returns or sets  the HasOriginGwif
    
    <hr>
    
    Getter Method
    
    Signature ``HasOriginGwif`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HasOriginGwif`` 
    
    :param originGwif: 
    :type originGwif: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IsOriginSpecified: bool = ...
    """
    Returns or sets  the IsOriginSpecified
    
    <hr>
    
    Getter Method
    
    Signature ``IsOriginSpecified`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsOriginSpecified`` 
    
    :param originSpecified: 
    :type originSpecified: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IsWCSCoordinates: bool = ...
    """
    Returns or sets  the IsWCSCoordinates
    
    <hr>
    
    Getter Method
    
    Signature ``IsWCSCoordinates`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsWCSCoordinates`` 
    
    :param wcsCoordinates: 
    :type wcsCoordinates: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Origin: NXOpen.Point3d = ...
    """
    Returns or sets  the Origin
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Origin`` 
    
    :param origin: 
    :type origin: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointTypesOnByDefault: int = ...
    """
    Returns or sets  the SnapPointTypesOnByDefault
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointTypesOnByDefault`` 
    
    :param snapPointTypes: 
    :type snapPointTypes: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    VisibleManipulatorHandles: int = ...
    """
    Returns or sets  the VisibleManipulatorHandles.  
    
    It specifies the options to display the handles available on triad. The translation, rotation and origin handles are available.
    
    <hr>
    
    Getter Method
    
    Signature ``VisibleManipulatorHandles`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibleManipulatorHandles`` 
    
    :param handles: 
    :type handles: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    XAxis: NXOpen.Vector3d = ...
    """
    Returns or sets  the XAxis
    
    <hr>
    
    Getter Method
    
    Signature ``XAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XAxis`` 
    
    :param xAxis: 
    :type xAxis: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    YAxis: NXOpen.Vector3d = ...
    """
    Returns or sets  the YAxis
    
    <hr>
    
    Getter Method
    
    Signature ``YAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``YAxis`` 
    
    :param yAxis: 
    :type yAxis: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SpecifyOrientation = ...  # unknown typename


class SelectElement(UIBlock):
    """
    Represents a Select Elements block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjectsSubIDs(self) -> 'list[int]':
        """
        Gets the SelectedObjectSubIDs 
        
        Signature ``GetSelectedObjectsSubIDs()`` 
        
        :returns: Value to get from the property 
        :rtype: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjectsSubIDs(self, idVector: 'list[int]') -> None:
        """
        Sets the SelectedObjectSubIDs
        
        Signature ``SetSelectedObjectsSubIDs(idVector)`` 
        
        :param idVector: Value to set for the property 
        :type idVector: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectModeMembers(self) -> 'list[str]':
        """
        Gets the SelectMode members 
        
        Signature ``GetSelectModeMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectSubTypeMembers(self) -> 'list[str]':
        """
        Gets the SelectSubType members 
        
        Signature ``GetSelectSubTypeMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression.  
    
    If true, focus automatically progresses to next selection block.
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectModeAsString: str = ...
    """
    Returns or sets  the SelectMode as string
    
    <hr>
    
    Getter Method
    
    Signature ``SelectModeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectModeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectSubTypeAsString: str = ...
    """
    Returns or sets  the SelectSubType as string
    
    <hr>
    
    Getter Method
    
    Signature ``SelectSubTypeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectSubTypeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowSelection: bool = ...
    """
    Returns or sets  the Show Selection.  
    
    If true, the graphical selection part of this block is shown.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX11.0.0
       
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowSelection`` 
    
    :param showSelection: 
    :type showSelection: bool 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX11.0.0
       
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SelectElement = ...  # unknown typename


class ListBox(UIBlock):
    """
    Represents a ListBox block   
    
    .. versionadded:: NX6.0.0
    """
    
    def SetAddHandler(self, cb: typing.Callable) -> None:
        """
        Sets the Add handler.  
        
        This handler is called when the Add button is pressed.
        The handler is responsible for adding an item to the list.  Nothing will be added to the list unless the handler
        adds it. 
        
        Signature ``SetAddHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDeleteHandler(self, cb: typing.Callable) -> None:
        """
        Sets the Delete handler.  
        
        If you set this handler, the handler will be
        called when the Delete button is pressed.  The handler does not need to implement code
        to delete the item.  The list will delete the selected items if and only if the handler returns 0. 
        
        Signature ``SetDeleteHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetListItems(self) -> 'list[str]':
        """
        Gets the ListItems 
        
        Signature ``GetListItems()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetListItems(self, items: 'list[str]') -> None:
        """
        Sets the ListItems
        
        Signature ``SetListItems(items)`` 
        
        :param items: 
        :type items: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedItems(self) -> 'list[int]':
        """
        Gets SelectedItems 
        
        Signature ``GetSelectedItems()`` 
        
        :returns:  selected items 
        :rtype: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedItems(self, selectedItems: 'list[int]') -> None:
        """
        Sets SelectedItems
        
        Signature ``SetSelectedItems(selectedItems)`` 
        
        :param selectedItems:  selected items 
        :type selectedItems: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedItemStrings(self) -> 'list[str]':
        """
        Gets the SelectedItemStrings 
        
        Signature ``GetSelectedItemStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedItemStrings(self, strings: 'list[str]') -> None:
        """
        Sets the SelectedItemStrings.  
        
        Selects the list items based on input array of strings.
        
        Signature ``SetSelectedItemStrings(strings)`` 
        
        :param strings: 
        :type strings: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedItemBooleans(self) -> 'list[int]':
        """
        Gets the SelectedItemBooleans.  
        
        This method returns an integer array of boolen values populated with 0 and 1 
        
        Signature ``GetSelectedItemBooleans()`` 
        
        :returns: 
        :rtype: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedItemBooleans(self, items: 'list[int]') -> None:
        """
        Sets the SelectedItemStrings.  
        
        Selects the list items based on input boolean array. Item is deselcted if value is 0 and selected otherwise.
        
        Signature ``SetSelectedItemBooleans(items)`` 
        
        :param items: 
        :type items: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AllowDeselectForSingleSelect: bool = ...
    """
    Returns or sets  the AllowDeselectForSingleSelect.  
    
    Allows deselection of item using Ctrl+MB1 when single select is true.
    
    <hr>
    
    Getter Method
    
    Signature ``AllowDeselectForSingleSelect`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowDeselectForSingleSelect`` 
    
    :param allow: 
    :type allow: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Height: int = ...
    """
    Returns or sets  the Height
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Height`` 
    
    :param height: 
    :type height: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IsAddButtonSensitive: bool = ...
    """
    Returns or sets  the IsAddButtonSensitive
    
    <hr>
    
    Getter Method
    
    Signature ``IsAddButtonSensitive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsAddButtonSensitive`` 
    
    :param sensitive: 
    :type sensitive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IsDeleteButtonSensitive: bool = ...
    """
    Returns or sets  the IsDeleteButtonSensitive
    
    <hr>
    
    Getter Method
    
    Signature ``IsDeleteButtonSensitive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsDeleteButtonSensitive`` 
    
    :param sesitive: 
    :type sesitive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize.  
    
    If true, translates the Label string into the language of the current locale.
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumHeight: int = ...
    """
    Returns or sets  the MaximumHeight
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumHeight`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumHeight`` 
    
    :param maxHeight: 
    :type maxHeight: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumStringLength: int = ...
    """
    Returns or sets  the MaximumStringLength
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumStringLength`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumStringLength`` 
    
    :param maxLength: 
    :type maxLength: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinimumHeight: int = ...
    """
    Returns or sets  the MinimumHeight
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumHeight`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumHeight`` 
    
    :param minHeight: 
    :type minHeight: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ResizeHeightWithDialog: bool = ...
    """
    Returns or sets  the ResizeHeightWithDialog
    
    <hr>
    
    Getter Method
    
    Signature ``ResizeHeightWithDialog`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ResizeHeightWithDialog`` 
    
    :param resize: 
    :type resize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectedItemIndex: int = ...
    """
    Returns or sets  the SelectedItemIndex.  
    
    Valid only if SingleSelect is true. Otherwise -1 is returned.
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedItemIndex`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectedItemIndex`` 
    
    :param index: 
    :type index: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectedItemString: str = ...
    """
    Returns or sets  the SelectedItemString.  
    
    Valid only if SingleSelect is true. Otherwise empty string is returned.
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedItemString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectedItemString`` 
    
    :param string: 
    :type string: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowAddButton: bool = ...
    """
    Returns or sets  the ShowAddButton.  
    
    If true, Add button is shown.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowAddButton`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowAddButton`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowDeleteButton: bool = ...
    """
    Returns or sets  the ShowDeleteButton.  
    
    If true, Delete button is shown.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowDeleteButton`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowDeleteButton`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowMoveUpDownButtons: bool = ...
    """
    Returns or sets  the ShowMoveUpDownButtons.  
    
    If true, MoveUp and MoveDown buttons are shown.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowMoveUpDownButtons`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowMoveUpDownButtons`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SingleSelect: bool = ...
    """
    Returns or sets  the SingleSelect.  
    
    If true, only single item can be selected.
    
    <hr>
    
    Getter Method
    
    Signature ``SingleSelect`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SingleSelect`` 
    
    :param sinleSelect: 
    :type sinleSelect: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: ListBox = ...  # unknown typename


class CurveCollector(UIBlock):
    """
    Represents a Curve Collector  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectModeMembers(self) -> 'list[str]':
        """
        Gets the SelectMode members 
        
        Signature ``GetSelectModeMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDefaultCurveRulesMembers(self) -> 'list[str]':
        """
        Gets the DefaultCurveRules members 
        
        Signature ``GetDefaultCurveRulesMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AllowConvergentObject: bool = ...
    """
    Returns or sets  the AllowConvergentObject
    
    <hr>
    
    Getter Method
    
    Signature ``AllowConvergentObject`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowConvergentObject`` 
    
    :param allowConvergentObject: 
    :type allowConvergentObject: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    AllowInferredCurveSelection: bool = ...
    """
    Returns or sets  the AllowInferredCurveSelection
    
    <hr>
    
    Getter Method
    
    Signature ``AllowInferredCurveSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowInferredCurveSelection`` 
    
    :param allow: 
    :type allow: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BlendVirtualCurveOverlay: bool = ...
    """
    Returns or sets  the BlendVirtualCurveOverlay
    
    <hr>
    
    Getter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :param blendCurve: 
    :type blendCurve: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CurveRules: int = ...
    """
    Returns or sets  the CurveRules
    
    <hr>
    
    Getter Method
    
    Signature ``CurveRules`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurveRules`` 
    
    :param curveRules: 
    :type curveRules: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DefaultCurveRulesAsString: str = ...
    """
    Returns or sets  the DefaultCurveRules as string
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultCurveRulesAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultCurveRulesAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EntityType: int = ...
    """
    Returns or sets  the EntityType
    
    <hr>
    
    Getter Method
    
    Signature ``EntityType`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EntityType`` 
    
    :param entityType: 
    :type entityType: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InferredCurveSelection: bool = ...
    """
    Returns or sets  the InferredCurveSelection
    
    <hr>
    
    Getter Method
    
    Signature ``InferredCurveSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InferredCurveSelection`` 
    
    :param selectInferredCurve: 
    :type selectInferredCurve: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumScopeAsString: str = ...
    """
    Returns or sets  the MaximumScope
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumScopeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumScopeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    PopupMenuEnabled: bool = ...
    """
    Returns or sets  the PopupMenuEnabled
    
    <hr>
    
    Getter Method
    
    Signature ``PopupMenuEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PopupMenuEnabled`` 
    
    :param enabled: 
    :type enabled: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectModeAsString: str = ...
    """
    Returns or sets  the SelectMode as string
    
    <hr>
    
    Getter Method
    
    Signature ``SelectModeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectModeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ToolTip: str = ...
    """
    Returns or sets  the ToolTip
    
    <hr>
    
    Getter Method
    
    Signature ``ToolTip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolTip`` 
    
    :param toolTip: 
    :type toolTip: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: CurveCollector = ...  # unknown typename


class ObjectColorPicker(UIBlock):
    """
    Represents an Object Color Picker Block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets theBalloonTooltipLayout members  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Values to get from the property  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetValue(self) -> 'list[int]':
        """
        Gets the Value 
        
        Signature ``GetValue()`` 
        
        :returns: Values to get from the property 
        :rtype: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValue(self, valueVector: 'list[int]') -> None:
        """
        Sets the Value
        
        Signature ``SetValue(valueVector)`` 
        
        :param valueVector: Values to set for the property.  
        :type valueVector: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param tooltipText: 
    :type tooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize.  
    
    If true, translates the Label string into the language of the current locale.
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    NumberSelectable: int = ...
    """
    Returns or sets  the NumberSelectable.  
    
    Represents number of colors that can be selected
    
    <hr>
    
    Getter Method
    
    Signature ``NumberSelectable`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberSelectable`` 
    
    :param number: 
    :type number: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue.  
    
    If true, block's value will be stored in dialog memory upon OK, Apply or Close.
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: ObjectColorPicker = ...  # unknown typename


class BodyCollector(UIBlock):
    """
    Represents a Body Collector block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout member  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterpartSelectionMembers(self) -> 'list[str]':
        """
        Gets the InterpartSelection members 
        
        Signature ``GetInterpartSelectionMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the SelectedObjects 
        
        Signature ``GetSelectedObjects()`` 
        
        :returns: Value to get from the property 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedObjects(self, objectVector: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the SelectedObjects
        
        Signature ``SetSelectedObjects(objectVector)`` 
        
        :param objectVector: Value to set for the property 
        :type objectVector: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectModeMembers(self) -> 'list[str]':
        """
        Gets the SelectMode members 
        
        Signature ``GetSelectModeMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStepStatusMembers(self) -> 'list[str]':
        """
        Gets the StepStatus members 
        
        Signature ``GetStepStatusMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDefaultBodyRulesMembers(self) -> 'list[str]':
        """
        Gets the DefaultBodyRules members 
        
        Signature ``GetDefaultBodyRulesMembers()`` 
        
        :returns: Value to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AllowConvergentObject: bool = ...
    """
    Returns or sets  the AllowConvergentObject
    
    <hr>
    
    Getter Method
    
    Signature ``AllowConvergentObject`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowConvergentObject`` 
    
    :param allowConvergentObject: 
    :type allowConvergentObject: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    AutomaticProgression: bool = ...
    """
    Returns or sets  the AutomaticProgression
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticProgression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticProgression`` 
    
    :param automaticProgression: 
    :type automaticProgression: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BlendVirtualCurveOverlay: bool = ...
    """
    Returns or sets  the BlendVirtualCurveOverlay
    
    <hr>
    
    Getter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BlendVirtualCurveOverlay`` 
    
    :param blendCurve: 
    :type blendCurve: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BodyRules: int = ...
    """
    Returns or sets  the BodyRules
    
    <hr>
    
    Getter Method
    
    Signature ``BodyRules`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BodyRules`` 
    
    :param bodyRules: 
    :type bodyRules: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CreateInterpartLink: bool = ...
    """
    Returns or sets  the CreateInterpartLink
    
    <hr>
    
    Getter Method
    
    Signature ``CreateInterpartLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateInterpartLink`` 
    
    :param createLink: 
    :type createLink: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Cue: str = ...
    """
    Returns or sets  the Cue
    
    <hr>
    
    Getter Method
    
    Signature ``Cue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Cue`` 
    
    :param cue: 
    :type cue: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DefaultBodyRulesAsString: str = ...
    """
    Returns or sets  the DefaultBodyRules as string
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultBodyRulesAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultBodyRulesAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EntityType: int = ...
    """
    Returns or sets  the EntityType
    
    <hr>
    
    Getter Method
    
    Signature ``EntityType`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EntityType`` 
    
    :param entityType: 
    :type entityType: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IncludeSheetBodies: bool = ...
    """
    Returns or sets  the IncludeSheetBodies
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeSheetBodies`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeSheetBodies`` 
    
    :param includeSheetBodies: 
    :type includeSheetBodies: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    InterpartSelectionAsString: str = ...
    """
    Returns or sets  the InterpartSelection as string
    
    <hr>
    
    Getter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterpartSelectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LabelString: str = ...
    """
    Returns or sets  the LabelString
    
    <hr>
    
    Getter Method
    
    Signature ``LabelString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelString`` 
    
    :param labelString: 
    :type labelString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumScopeAsString: str = ...
    """
    Returns or sets  the MaximumScope
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumScopeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumScopeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    PopupMenuEnabled: bool = ...
    """
    Returns or sets  the PopupMenuEnabled.  
    
    If true, displays the popup menu for the body.
    
    <hr>
    
    Getter Method
    
    Signature ``PopupMenuEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PopupMenuEnabled`` 
    
    :param enabled: 
    :type enabled: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectModeAsString: str = ...
    """
    Returns or sets  the SelectMode as string
    
    <hr>
    
    Getter Method
    
    Signature ``SelectModeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectModeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StepStatusAsString: str = ...
    """
    Returns or sets  the StepStatus as string
    
    <hr>
    
    Getter Method
    
    Signature ``StepStatusAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StepStatusAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ToolTip: str = ...
    """
    Returns or sets  the ToolTip
    
    <hr>
    
    Getter Method
    
    Signature ``ToolTip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolTip`` 
    
    :param toolTip: 
    :type toolTip: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: BodyCollector = ...  # unknown typename


class ChooseExpression(UIBlock):
    """
    Represents Choose Expression block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetExpressionSortTypeMembers(self) -> 'list[str]':
        """
        Gets the ExpressionSortType members 
        
        Signature ``GetExpressionSortTypeMembers()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetExpressionTypeIndexMembers(self) -> 'list[str]':
        """
        Gets the ExpressionTypeIndex members 
        
        Signature ``GetExpressionTypeIndexMembers()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    ExpressionSortTypeAsString: str = ...
    """
    Returns or sets  the ExpressionSortType as string
    
    <hr>
    
    Getter Method
    
    Signature ``ExpressionSortTypeAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpressionSortTypeAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ExpressionTypeIndexAsString: str = ...
    """
    Returns or sets  the ExpressionTypeIndex as string
    
    <hr>
    
    Getter Method
    
    Signature ``ExpressionTypeIndexAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpressionTypeIndexAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectedExpression: NXOpen.TaggedObject = ...
    """
    Returns or sets  the SelectedExpression
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedExpression`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectedExpression`` 
    
    :param selectedExpression: 
    :type selectedExpression: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: ChooseExpression = ...  # unknown typename


class SetListInsertionLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SetListInsertionLocation():
    """
    During Insert, indicates whether component should be
    inserted before or after the insertion location 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Before", " - "
       "After", " - "
    """
    Before = 0  # SetListInsertionLocationMemberType
    After = 1  # SetListInsertionLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SetList(UIBlock):
    """
    Represents a SetList block   
    
    .. versionadded:: NX6.0.0
    """
    
    class InsertionLocation():
        """
        During Insert, indicates whether component should be
        inserted before or after the insertion location 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Before", " - "
           "After", " - "
        """
        Before = 0  # SetListInsertionLocationMemberType
        After = 1  # SetListInsertionLocationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetSeed(self, dlxFile: str) -> None:
        """
        Sets the seed using a dlx file.  
        
        The seed must be set during initialization.
        Setting the seed will also reset any Add and Delete handlers that has been registered,
        so SetSeed should be called prior to calling SetAddHandler or SetDeleteHandler. 
        
        Signature ``SetSeed(dlxFile)`` 
        
        :param dlxFile:  The dlx file used to create the seed  
        :type dlxFile: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAddHandler(self, cb: typing.Callable) -> None:
        """
        Sets the AddNewSet handler.  
        
        If you set this handler, the handler will be
        called when the Add New Set button is pressed, and the handler will be responsible
        for adding an item to the list.  Nothing will be added to the list unless the handler
        adds it. 
        
        Signature ``SetAddHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDeleteHandler(self, cb: typing.Callable) -> None:
        """
        Sets the Delete handler.  
        
        If you set this handler, the handler will be
        called when the Delete button is pressed.  The handler does not need to implement code
        to delete the item.  The list will delete the item if and only if the handler returns 0. 
        
        Signature ``SetDeleteHandler(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetReorderObserver(self, cb: typing.Callable) -> None:
        """
        Sets the Reorder observer.  
        
        If you set this observer, the observer will
        be called after an item is moved by pressing the Move Up and Down buttons.
        The observer does not need to implement the move up and down behavior and is called
        after the item has already been moved. 
        
        Signature ``SetReorderObserver(cb)`` 
        
        :param cb: 
        :type cb: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddNewSet(self, copyPropertiesAndSelect: bool) -> UIBlock:
        """
        Adds an item to the end of the list  
        
        Signature ``AddNewSet(copyPropertiesAndSelect)`` 
        
        :param copyPropertiesAndSelect:  Indicates whether to copy properties from the                 currently selected component and set focus to the new set  
        :type copyPropertiesAndSelect: bool 
        :returns:  The added item  
        :rtype: :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Delete(self, uicomp: UIBlock) -> None:
        """
        Deletes an item from the list 
        
        Signature ``Delete(uicomp)`` 
        
        :param uicomp:  Item to delete  
        :type uicomp: :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Swap(self, uicomp1: UIBlock, uicomp2: UIBlock) -> None:
        """
        Swaps the location of two items 
        
        Signature ``Swap(uicomp1, uicomp2)`` 
        
        :param uicomp1:  Item to swap  
        :type uicomp1: :py:class:`NXOpen.BlockStyler.UIBlock` 
        :param uicomp2:  Item to swap  
        :type uicomp2: :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def InsertNewSet(self, location: UIBlock, insertBeforeOrAfter: SetListInsertionLocation, copyPropertiesAndSelect: bool) -> UIBlock:
        """
        Inserts an item before or after a specified item  
        
        Signature ``InsertNewSet(location, insertBeforeOrAfter, copyPropertiesAndSelect)`` 
        
        :param location:  Location to insert the new item  
        :type location: :py:class:`NXOpen.BlockStyler.UIBlock` 
        :param insertBeforeOrAfter:  Indicates whether to insert the new item before or after the specified location  
        :type insertBeforeOrAfter: :py:class:`NXOpen.BlockStyler.SetListInsertionLocation` 
        :param copyPropertiesAndSelect:  Indicates whether to copy properties from the                 currently selected component and set focus to the new set  
        :type copyPropertiesAndSelect: bool 
        :returns:  The inserted item  
        :rtype: :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItemText(self, item: UIBlock, strings: 'list[str]') -> None:
        """
        Sets the text for the specified item.  
        
        If the list has a title column, the title column is not included in the item text. 
        
        Signature ``SetItemText(item, strings)`` 
        
        :param item: 
        :type item: :py:class:`NXOpen.BlockStyler.UIBlock` 
        :param strings:  The text.  The text may only contain characters in the locale character set  
        :type strings: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemText(self, item: UIBlock) -> 'list[str]':
        """
        Gets the text for the specified item.  
        
        If the list has a title column, the title column is not included in the item text.  
        
        Signature ``GetItemText(item)`` 
        
        :param item: 
        :type item: :py:class:`NXOpen.BlockStyler.UIBlock` 
        :returns:  The text  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindUpdated(self) -> UIBlock:
        """
        When an update event occurs on the list, this method finds the
        item in the list that was updated  
        
        Signature ``FindUpdated()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelected(self) -> 'list[UIBlock]':
        """
        Gets the selected items  
        
        Signature ``GetSelected()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelected(self, items: 'list[UIBlock]') -> None:
        """
        Sets the selected items.  
        
        If the "Multiple Edit" property is false,
        no more than one item can be selected 
        
        Signature ``SetSelected(items)`` 
        
        :param items: 
        :type items: list of :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItems(self) -> 'list[UIBlock]':
        """
        Gets all the items in the list  
        
        Signature ``GetItems()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.BlockStyler.UIBlock` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnLabels(self) -> 'list[str]':
        """
        Gets the ColumnLabels 
        
        Signature ``GetColumnLabels()`` 
        
        :returns:  Values to get from the property 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnLabels(self, labels: 'list[str]') -> None:
        """
        Sets the ColumnLabels
        
        Signature ``SetColumnLabels(labels)`` 
        
        :param labels:  Values to set to the property 
        :type labels: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnWidths(self) -> 'list[int]':
        """
        Gets the ColumnWidths 
        
        Signature ``GetColumnWidths()`` 
        
        :returns:  Values to get from the property 
        :rtype: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnWidths(self, width: 'list[int]') -> None:
        """
        Sets the ColumnWidths
        
        Signature ``SetColumnWidths(width)`` 
        
        :param width:  Values to set to the property 
        :type width: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLayoutMembers(self) -> 'list[str]':
        """
        Gets the Layout members 
        
        Signature ``GetLayoutMembers()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AddNewSetLabel: str = ...
    """
    Returns or sets  the AddNewSetLabel.  
    
    Specifies the label for AddNewSet button.
    
    <hr>
    
    Getter Method
    
    Signature ``AddNewSetLabel`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AddNewSetLabel`` 
    
    :param label: 
    :type label: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DefaultColumnWidth: int = ...
    """
    Returns or sets  the DefaultColumnWidth
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultColumnWidth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultColumnWidth`` 
    
    :param defaultWidth: 
    :type defaultWidth: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IsAddButtonSensitive: bool = ...
    """
    Returns or sets  the IsAddButtonSensitive
    
    <hr>
    
    Getter Method
    
    Signature ``IsAddButtonSensitive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsAddButtonSensitive`` 
    
    :param addButton: 
    :type addButton: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LayoutAsString: str = ...
    """
    Returns or sets  the Layout as string
    
    <hr>
    
    Getter Method
    
    Signature ``LayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ListExpanded: bool = ...
    """
    Returns or sets  the ListExpanded.  
    
    If true, the list is expanded.
    
    <hr>
    
    Getter Method
    
    Signature ``ListExpanded`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ListExpanded`` 
    
    :param expanded: 
    :type expanded: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ListHideGroup: bool = ...
    """
    Returns or sets  the ListHideGroup
    
    <hr>
    
    Getter Method
    
    Signature ``ListHideGroup`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ListHideGroup`` 
    
    :param listHideGroup: 
    :type listHideGroup: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumHeight: int = ...
    """
    Returns or sets  the MaximumHeight
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumHeight`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumHeight`` 
    
    :param maxHeight: 
    :type maxHeight: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinimumHeight: int = ...
    """
    Returns or sets  the MinimumHeight
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumHeight`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumHeight`` 
    
    :param minHeight: 
    :type minHeight: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MultipleEdit: bool = ...
    """
    Returns or sets  the MultipleEdit
    
    <hr>
    
    Getter Method
    
    Signature ``MultipleEdit`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MultipleEdit`` 
    
    :param multipleEdit: 
    :type multipleEdit: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    NumberColumnString: str = ...
    """
    Returns or sets  the NumberColumnString as string
    
    <hr>
    
    Getter Method
    
    Signature ``NumberColumnString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberColumnString`` 
    
    :param columnString: 
    :type columnString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    NumberOfColumns: int = ...
    """
    Returns or sets  the NumberOfColumns
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfColumns`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfColumns`` 
    
    :param numColumns: 
    :type numColumns: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ResizeHeightWithDialog: bool = ...
    """
    Returns or sets  the ResizeHeightWithDialog.  
    
    If true, height of the block changes dynamically with dialog.
    
    <hr>
    
    Getter Method
    
    Signature ``ResizeHeightWithDialog`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ResizeHeightWithDialog`` 
    
    :param resize: 
    :type resize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SeedDlxFile: str = ...
    """
    Returns or sets  the SeedDlxFile as string
    
    <hr>
    
    Getter Method
    
    Signature ``SeedDlxFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeedDlxFile`` 
    
    :param dlxName: 
    :type dlxName: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowAddNewSet: bool = ...
    """
    Returns or sets  the ShowAddNewSet.  
    
    If true, "Add New Set" button is shown.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowAddNewSet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowAddNewSet`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowColumnHeadings: bool = ...
    """
    Returns or sets  the ShowColumnHeadings
    
    <hr>
    
    Getter Method
    
    Signature ``ShowColumnHeadings`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowColumnHeadings`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowRemove: bool = ...
    """
    Returns or sets  the ShowRemove.  
    
    If true, "Remove" button is shown.
    
    <hr>
    
    Getter Method
    
    Signature ``ShowRemove`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowRemove`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowReorderControls: bool = ...
    """
    Returns or sets  the ShowReorderControls
    
    <hr>
    
    Getter Method
    
    Signature ``ShowReorderControls`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowReorderControls`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SetList = ...  # unknown typename


class ScrolledWindow(UIBlock):
    """
    Represents a Scrolled Window block  
    
    .. versionadded:: NX8.5.0
    """
    Height: int = ...
    """
    Returns or sets  the Height
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Height`` 
    
    :param height: 
    :type height: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Members: PropertyList = ...
    """
    Returns  the Members
    
    <hr>
    
    Getter Method
    
    Signature ``Members`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BlockStyler.PropertyList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ResizeHeightWithDialog: bool = ...
    """
    Returns or sets  the ResizeHeightWithDialog.  
    
    If true, the height of block will dynamically change when the dialog is resized.
    
    <hr>
    
    Getter Method
    
    Signature ``ResizeHeightWithDialog`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ResizeHeightWithDialog`` 
    
    :param resize: 
    :type resize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Width: int = ...
    """
    Returns or sets  the Width
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param width: 
    :type width: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: ScrolledWindow = ...  # unknown typename


class DoubleBlock(UIBlock):
    """
    Represents a Double block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetBalloonTooltipLayoutMembers(self) -> 'list[str]':
        """
        Gets the BalloonTooltipLayout member  
        
        Signature ``GetBalloonTooltipLayoutMembers()`` 
        
        :returns: Value to get from the proprty.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetComboOptions(self) -> 'list[float]':
        """
        Gets the ComboOptions 
        
        Signature ``GetComboOptions()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetComboOptions(self, optionValue: 'list[float]') -> None:
        """
        Sets the ComboOptions
        
        Signature ``SetComboOptions(optionValue)`` 
        
        :param optionValue: 
        :type optionValue: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPresentationStyleMembers(self) -> 'list[str]':
        """
        Gets the PresentationStyle members  
        
        Signature ``GetPresentationStyleMembers()`` 
        
        :returns: Value to get for the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AdaptiveScaleLimits: bool = ...
    """
    Returns or sets  the AdaptiveScaleLimits
    
    <hr>
    
    Getter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdaptiveScaleLimits`` 
    
    :param scaleLimits: 
    :type scaleLimits: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipImage: str = ...
    """
    Returns or sets  the BalloonTooltipImage
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipImage`` 
    
    :param imageString: 
    :type imageString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipLayoutAsString: str = ...
    """
    Returns or sets  the BalloonTooltipLayout as string
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipLayoutAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    BalloonTooltipText: str = ...
    """
    Returns or sets  the BalloonTooltipText
    
    <hr>
    
    Getter Method
    
    Signature ``BalloonTooltipText`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BalloonTooltipText`` 
    
    :param balloonTooltipText: 
    :type balloonTooltipText: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Bitmap: str = ...
    """
    Returns or sets  the Bitmap
    
    <hr>
    
    Getter Method
    
    Signature ``Bitmap`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Bitmap`` 
    
    :param bitmapString: 
    :type bitmapString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Increment: float = ...
    """
    Returns or sets  the Increment
    
    <hr>
    
    Getter Method
    
    Signature ``Increment`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Increment`` 
    
    :param increment: 
    :type increment: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    LineIncrement: float = ...
    """
    Returns or sets  the LineIncrement
    
    <hr>
    
    Getter Method
    
    Signature ``LineIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineIncrement`` 
    
    :param lineIncrement: 
    :type lineIncrement: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Localize: bool = ...
    """
    Returns or sets  the Localize
    
    <hr>
    
    Getter Method
    
    Signature ``Localize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Localize`` 
    
    :param localize: 
    :type localize: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaxInclusive: bool = ...
    """
    Returns or sets  the MaxInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MaxInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxInclusive`` 
    
    :param maxInclusive: 
    :type maxInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumValue: float = ...
    """
    Returns or sets  the MaximumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumValue`` 
    
    :param maxValue: 
    :type maxValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinInclusive: bool = ...
    """
    Returns or sets  the MinInclusive
    
    <hr>
    
    Getter Method
    
    Signature ``MinInclusive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinInclusive`` 
    
    :param minInclusive: 
    :type minInclusive: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MinimumValue: float = ...
    """
    Returns or sets  the MinimumValue
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumValue`` 
    
    :param minValue: 
    :type minValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PageIncrement: float = ...
    """
    Returns or sets  the PageIncrement
    
    <hr>
    
    Getter Method
    
    Signature ``PageIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PageIncrement`` 
    
    :param pageIncrement: 
    :type pageIncrement: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PresentationStyleAsString: str = ...
    """
    Returns or sets  the PresentationStyle as string
    
    <hr>
    
    Getter Method
    
    Signature ``PresentationStyleAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PresentationStyleAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ReadOnlyValue: bool = ...
    """
    Returns or sets  the ReadOnlyValue
    
    <hr>
    
    Getter Method
    
    Signature ``ReadOnlyValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReadOnlyValue`` 
    
    :param readOnly: 
    :type readOnly: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ScaleLimits: bool = ...
    """
    Returns or sets  the ScaleLimits
    
    <hr>
    
    Getter Method
    
    Signature ``ScaleLimits`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScaleLimits`` 
    
    :param scaleLimits: 
    :type scaleLimits: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ScaleMaxLimitLabel: str = ...
    """
    Returns or sets  the ScaleMaxLimitLabel
    
    <hr>
    
    Getter Method
    
    Signature ``ScaleMaxLimitLabel`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScaleMaxLimitLabel`` 
    
    :param maxLimitLabel: 
    :type maxLimitLabel: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ScaleMinLimitLabel: str = ...
    """
    Returns or sets  the ScaleMinLimitLabel
    
    <hr>
    
    Getter Method
    
    Signature ``ScaleMinLimitLabel`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScaleMinLimitLabel`` 
    
    :param minLimitLabel: 
    :type minLimitLabel: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowScaleValue: bool = ...
    """
    Returns or sets  the ShowScaleValue
    
    <hr>
    
    Getter Method
    
    Signature ``ShowScaleValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowScaleValue`` 
    
    :param showValue: 
    :type showValue: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    TitleVisibility: bool = ...
    """
    Returns or sets  the TitleVisibility
    
    <hr>
    
    Getter Method
    
    Signature ``TitleVisibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TitleVisibility`` 
    
    :param visibility: 
    :type visibility: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Value: float = ...
    """
    Returns or sets  the Value
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param doubleValue: 
    :type doubleValue: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WrapSpin: bool = ...
    """
    Returns or sets  the WrapSpin
    
    <hr>
    
    Getter Method
    
    Signature ``WrapSpin`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WrapSpin`` 
    
    :param wrapSpin: 
    :type wrapSpin: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: DoubleBlock = ...  # unknown typename


class IntegerTable(UIBlock):
    """
    Represents a Integer Table block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetMaximumValues(self) -> tuple:
        """
        Gets the MaximumValues 
        
        Signature ``GetMaximumValues()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (matrixValue, nRows, nColumns). matrixValue is a list of int.  Values to get from the property nRows is a int.   Number of Rows in the 2D matrix nColumns is a int.   Number of Columns in the 2D matrix 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMaximumValues(self, nRows: int, nColumns: int, matrixValue: 'list[int]') -> None:
        """
        Sets the MaximumValues
        
        Signature ``SetMaximumValues(nRows, nColumns, matrixValue)`` 
        
        :param nRows:  Number of Rows in the 2D matrix  
        :type nRows: int 
        :param nColumns:  Number of Columns in the 2D matrix  
        :type nColumns: int 
        :param matrixValue: Value to set for given property.  
        :type matrixValue: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetMinimumValues(self) -> tuple:
        """
        Gets the MinimumValues 
        
        Signature ``GetMinimumValues()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (matrixValue, nRows, nColumns). matrixValue is a list of int.  Value to get for given property name. nRows is a int.   Number of Rows in the 2D matrix nColumns is a int.   Number of Columns in the 2D matrix 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMinimumValues(self, nRows: int, nColumns: int, matrixValue: 'list[int]') -> None:
        """
        Sets the MinimumValues
        
        Signature ``SetMinimumValues(nRows, nColumns, matrixValue)`` 
        
        :param nRows:  Number of Rows in the 2D matrix  
        :type nRows: int 
        :param nColumns:  Number of Columns in the 2D matrix  
        :type nColumns: int 
        :param matrixValue: Value to set for given property.  
        :type matrixValue: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetValues(self) -> tuple:
        """
        Gets the Values 
        
        Signature ``GetValues()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (matrixValue, nRows, nColumns). matrixValue is a list of int.  Values to get from the property. nRows is a int.   Number of Rows in the 2D matrix nColumns is a int.   Number of Columns in the 2D matrix 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValues(self, nRows: int, nColumns: int, matrixValue: 'list[int]') -> None:
        """
        Sets the Values
        
        Signature ``SetValues(nRows, nColumns, matrixValue)`` 
        
        :param nRows:  Number of Rows in the 2D matrix  
        :type nRows: int 
        :param nColumns:  Number of Columns in the 2D matrix  
        :type nColumns: int 
        :param matrixValue: Values to set for the property.  
        :type matrixValue: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRowTitles(self) -> 'list[str]':
        """
        Gets the RowTitles 
        
        Signature ``GetRowTitles()`` 
        
        :returns: Values to get from the property.  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRowTitles(self, rowTitle: 'list[str]') -> None:
        """
        Sets the RowTitles
        
        Signature ``SetRowTitles(rowTitle)`` 
        
        :param rowTitle: Value to set for the property.  
        :type rowTitle: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    ColumnTitles: str = ...
    """
    Returns or sets  the ColumnTitles
    
    <hr>
    
    Getter Method
    
    Signature ``ColumnTitles`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColumnTitles`` 
    
    :param title: 
    :type title: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Increment: float = ...
    """
    Returns or sets  the Increment.  
    
    Use this property only when Spin is true
    
    <hr>
    
    Getter Method
    
    Signature ``Increment`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Increment`` 
    
    :param increment: 
    :type increment: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RetainValue: bool = ...
    """
    Returns or sets  the RetainValue.  
    
    If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close. 
    
    <hr>
    
    Getter Method
    
    Signature ``RetainValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RetainValue`` 
    
    :param retain: 
    :type retain: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Spin: bool = ...
    """
    Returns or sets  the Spin
    
    <hr>
    
    Getter Method
    
    Signature ``Spin`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Spin`` 
    
    :param spin: 
    :type spin: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WrapSpin: bool = ...
    """
    Returns or sets  the WrapSpin.  
    
    Use this property only when Spin is true
    
    <hr>
    
    Getter Method
    
    Signature ``WrapSpin`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WrapSpin`` 
    
    :param wrapSpin: 
    :type wrapSpin: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: IntegerTable = ...  # unknown typename


class OrientXpress(UIBlock):
    """
    Represents OrientXpress Block  
    
    .. versionadded:: NX8.5.0
    """
    
    def GetDirectionMembers(self) -> 'list[str]':
        """
        Gets Direction members 
        
        Signature ``GetDirectionMembers()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPlaneMembers(self) -> 'list[str]':
        """
        Gets Plane members 
        
        Signature ``GetPlaneMembers()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetReferenceMembers(self) -> 'list[str]':
        """
        Gets Reference members 
        
        Signature ``GetReferenceMembers()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    DirectionAsString: str = ...
    """
    Returns or sets  the Direction as string
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PlaneAsString: str = ...
    """
    Returns or sets  the Plane as string
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ReferenceAsString: str = ...
    """
    Returns or sets  the Reference as string
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceAsString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceAsString`` 
    
    :param enumString: 
    :type enumString: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ReferenceCsys: NXOpen.TaggedObject = ...
    """
    Returns or sets  the ReferenceCsys
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceCsys`` 
    
    :param referenceCsys: 
    :type referenceCsys: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowAxisSubBlock: bool = ...
    """
    Returns or sets  the ShowAxisSubBlock
    
    <hr>
    
    Getter Method
    
    Signature ``ShowAxisSubBlock`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowAxisSubBlock`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowPlaneSubBlock: bool = ...
    """
    Returns or sets  the ShowPlaneSubBlock
    
    <hr>
    
    Getter Method
    
    Signature ``ShowPlaneSubBlock`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowPlaneSubBlock`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowReferenceSubBlock: bool = ...
    """
    Returns or sets  the ShowReferenceSubBlock
    
    <hr>
    
    Getter Method
    
    Signature ``ShowReferenceSubBlock`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowReferenceSubBlock`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowSceneControl: bool = ...
    """
    Returns or sets  the ShowSceneControl
    
    <hr>
    
    Getter Method
    
    Signature ``ShowSceneControl`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowSceneControl`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowXAxis: bool = ...
    """
    Returns or sets  the ShowXAxis
    
    <hr>
    
    Getter Method
    
    Signature ``ShowXAxis`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowXAxis`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowXYPlane: bool = ...
    """
    Returns or sets  the ShowXYPlane
    
    <hr>
    
    Getter Method
    
    Signature ``ShowXYPlane`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowXYPlane`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowXZPlane: bool = ...
    """
    Returns or sets  the ShowXZPlane
    
    <hr>
    
    Getter Method
    
    Signature ``ShowXZPlane`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowXZPlane`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowYAxis: bool = ...
    """
    Returns or sets  the ShowYAxis
    
    <hr>
    
    Getter Method
    
    Signature ``ShowYAxis`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowYAxis`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowYZPlane: bool = ...
    """
    Returns or sets  the ShowYZPlane
    
    <hr>
    
    Getter Method
    
    Signature ``ShowYZPlane`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowYZPlane`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ShowZAxis: bool = ...
    """
    Returns or sets  the ShowZAxis
    
    <hr>
    
    Getter Method
    
    Signature ``ShowZAxis`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowZAxis`` 
    
    :param show: 
    :type show: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: OrientXpress = ...  # unknown typename


