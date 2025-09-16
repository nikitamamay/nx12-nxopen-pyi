# module 'NXOpen.Drafting'
#
# Automatically generated 2025-06-09T14:38:45.589882
#
"""Default documentation for NXOpen.Drafting."""

import typing

import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Drawings
import NXOpen.GeometricUtilities
import NXOpen.Layout2d
import NXOpen.PDM
import NXOpen.Preferences



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class PrimaryContentItemBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder`.  
    
    This class is
    used to specify information pertaining to the primary content of a Drawing Booklet.
    Each instance represents a single drawing in a booklet.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.AutomationManager.CreatePrimaryContentItemBuilder`
    
    .. versionadded:: NX8.0.0
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
    
    Content: NXOpen.Assemblies.SelectComponentList = ...
    """
    Returns  the content.  
    
    <hr>
    
    Getter Method
    
    Signature ``Content`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    GeometryTemplate: str = ...
    """
    Returns or sets  the geometry template.  
    
    <hr>
    
    Getter Method
    
    Signature ``GeometryTemplate`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GeometryTemplate`` 
    
    :param geometryTemplate: 
    :type geometryTemplate: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Null: PrimaryContentItemBuilder = ...  # unknown typename


class PreferencesBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Drafting.PreferencesBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.SettingsManager.CreatePreferencesBuilder`
    
    Default values.
    
    ==========================================================  =============
    Property                                                    Value
    ==========================================================  =============
    ViewStyle.ViewStyleGeneral.AngleSetting.Angle.Value         0 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleGeneral.AngleSetting.Associative         0 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleGeneral.AngleSetting.EvaluationPlane     DrawingSheet 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleGeneral.Scale.Denominator                1.0 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleGeneral.Scale.Numerator                  1.0 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleGeneral.Scale.ScaleType                  Ratio 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleOrientation.HingeLine.ReverseDirection   false 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleOrientation.HingeLine.VectorOption       Inferred 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleOrientation.Ovt.AssociativeOrientation   0 
    ==========================================================  =============
    
    .. versionadded:: NX9.0.0
    """
    
    def InheritSettingsFromSelectedObjects(self, selectedObject: NXOpen.NXObject) -> None:
        """
        Inherit Settings From Selected Objects 
        
        Signature ``InheritSettingsFromSelectedObjects(selectedObject)`` 
        
        :param selectedObject:  The selected annotation or table or view instance object.                                                                None is not allowed.  
        :type selectedObject: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
        Inherit Settings From Customer Default 
        
        Signature ``InheritSettingsFromCustomerDefault()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def InheritSettingsFromPreferences(self) -> None:
        """
        Inherit Settings From Preference 
        
        Signature ``InheritSettingsFromPreferences()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    AnnotationStyle: NXOpen.Annotations.StyleBuilder = ...
    """
    Returns  the annotation style builder 
    
    <hr>
    
    Getter Method
    
    Signature ``AnnotationStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.StyleBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    AssemblyCreationSettingsBuilder: NXOpen.Layout2d.AssemblyCreationSettingsBuilder = ...
    """
    Returns  the assembly creation from 2d component builder 
    
    <hr>
    
    Getter Method
    
    Signature ``AssemblyCreationSettingsBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.AssemblyCreationSettingsBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    AutomationBooklet: NXOpen.Drawings.AutomationBookletBuilder = ...
    """
    Returns     the AutomationBookletBuilder builder 
    
    <hr>
    
    Getter Method
    
    Signature ``AutomationBooklet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.AutomationBookletBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    AutomationRule: AutomationRuleBuilder = ...
    """
    Returns  the drafting automation rule builder 
    
    <hr>
    
    Getter Method
    
    Signature ``AutomationRule`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drafting.AutomationRuleBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    AutomationTemplateRegion: NXOpen.Drawings.AutomationTemplateRegionBuilder = ...
    """
    Returns     the AutomationTemplateRegion builder 
    
    <hr>
    
    Getter Method
    
    Signature ``AutomationTemplateRegion`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.AutomationTemplateRegionBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BendTable: NXOpen.Annotations.BendTableSettingsBuilder = ...
    """
    Returns  the Bend table settings builder 
    
    <hr>
    
    Getter Method
    
    Signature ``BendTable`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.BendTableSettingsBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BorderAndZoneStyle: NXOpen.Drawings.BorderAndZoneStyleBuilder = ...
    """
    Returns  the border and zone style builder 
    
    <hr>
    
    Getter Method
    
    Signature ``BorderAndZoneStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.BorderAndZoneStyleBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    CommonWorkflow: NXOpen.Annotations.CommonWorkflowBuilder = ...
    """
    Returns  the common workflow builder 
    
    <hr>
    
    Getter Method
    
    Signature ``CommonWorkflow`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.CommonWorkflowBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Component2dSettings: NXOpen.Layout2d.ComponentSettingsBlockBuilder = ...
    """
    Returns  the 2d component settings block builder, this builder stores the settings of the 2d component 
    
    <hr>
    
    Getter Method
    
    Signature ``Component2dSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.ComponentSettingsBlockBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    CreateComponentFrom3DSettingsBuilder: NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder = ...
    """
    Returns  the create component from 3d builder 
    
    <hr>
    
    Getter Method
    
    Signature ``CreateComponentFrom3DSettingsBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    DimensionWorkflow: NXOpen.Annotations.DimensionWorkflowBuilder = ...
    """
    Returns  the Dimension Workflow builder 
    
    <hr>
    
    Getter Method
    
    Signature ``DimensionWorkflow`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.DimensionWorkflowBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    DrawingFormatTitle: NXOpen.Annotations.DrawingFormatTitleBuilder = ...
    """
    Returns     the drawing format title block builder  
    
    <hr>
    
    Getter Method
    
    Signature ``DrawingFormatTitle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.DrawingFormatTitleBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    DrawingFormatsheet: NXOpen.Drawings.DrawingFormatSheetBuilder = ...
    """
    Returns     the drawing format sheet builder 
    
    <hr>
    
    Getter Method
    
    Signature ``DrawingFormatsheet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.DrawingFormatSheetBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FramebarGeneral: NXOpen.Annotations.ShipDraftingFramebarGeneralBuilder = ...
    """
    Returns     the framebar general builder 
    
    <hr>
    
    Getter Method
    
    Signature ``FramebarGeneral`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.ShipDraftingFramebarGeneralBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    GeneralLayoutPreferencesBuilder: NXOpen.Layout2d.GeneralPreferencesBuilder = ...
    """
    Returns  the general layout preferences builder 
    
    <hr>
    
    Getter Method
    
    Signature ``GeneralLayoutPreferencesBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.GeneralPreferencesBuilder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    HoleTableContent: NXOpen.Annotations.HoleTableSettingsContentBuilder = ...
    """
    Returns  the Hole table settings content builder 
    
    <hr>
    
    Getter Method
    
    Signature ``HoleTableContent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.HoleTableSettingsContentBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    HoleTableFormat: NXOpen.Annotations.HoleTableSettingsFormatBuilder = ...
    """
    Returns  the Hole table settings format builder 
    
    <hr>
    
    Getter Method
    
    Signature ``HoleTableFormat`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.HoleTableSettingsFormatBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    HoleTableHoleFilters: NXOpen.Annotations.HoleTableSettingsHoleFiltersBuilder = ...
    """
    Returns  the Hole table settings hole filters builder 
    
    <hr>
    
    Getter Method
    
    Signature ``HoleTableHoleFilters`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.HoleTableSettingsHoleFiltersBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    HoleTableLabel: NXOpen.Annotations.HoleTableSettingsLabelBuilder = ...
    """
    Returns  the Hole table settings label builder 
    
    <hr>
    
    Getter Method
    
    Signature ``HoleTableLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.HoleTableSettingsLabelBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    HoleTableWorkflow: NXOpen.Annotations.HoleTableSettingsWorkflowBuilder = ...
    """
    Returns  the Hole table settings workflow builder 
    
    <hr>
    
    Getter Method
    
    Signature ``HoleTableWorkflow`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.HoleTableSettingsWorkflowBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    PartsList: NXOpen.Annotations.PartsListBuilder = ...
    """
    Returns     the parts list style builder 
    
    <hr>
    
    Getter Method
    
    Signature ``PartsList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.PartsListBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    RetainedAnnotations: NXOpen.Annotations.RetainedAnnotationsBuilder = ...
    """
    Returns     the General Retained Annotations builder 
    
    <hr>
    
    Getter Method
    
    Signature ``RetainedAnnotations`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.RetainedAnnotationsBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    SymbolWorkflow: NXOpen.Annotations.SymbolWorkflowBuilder = ...
    """
    Returns     the SymbolWorkflow builder 
    
    <hr>
    
    Getter Method
    
    Signature ``SymbolWorkflow`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.SymbolWorkflowBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TableCellStyle: NXOpen.Annotations.TableCellStyleBuilder = ...
    """
    Returns  the table cell style builder 
    
    <hr>
    
    Getter Method
    
    Signature ``TableCellStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.TableCellStyleBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TableSection: NXOpen.Annotations.TableSectionStyleBuilder = ...
    """
    Returns     the table section style builder 
    
    <hr>
    
    Getter Method
    
    Signature ``TableSection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.TableSectionStyleBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TabularNoteStyle: NXOpen.Annotations.TabularNoteStyleBuilder = ...
    """
    Returns  the tabular note style builder 
    
    <hr>
    
    Getter Method
    
    Signature ``TabularNoteStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.TabularNoteStyleBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TrackDrawingChangesGeneral: NXOpen.Drawings.TrackDrawingChangesGeneralBuilder = ...
    """
    Returns  the track drawing changes general settings builder 
    
    <hr>
    
    Getter Method
    
    Signature ``TrackDrawingChangesGeneral`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.TrackDrawingChangesGeneralBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    TrackDrawingChangesReportFilter: NXOpen.Drawings.TrackDrawingChangesReportFilterBuilder = ...
    """
    Returns  the track drawing changes report filter builder 
    
    <hr>
    
    Getter Method
    
    Signature ``TrackDrawingChangesReportFilter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.TrackDrawingChangesReportFilterBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ViewBreak: NXOpen.Drawings.ViewBreakBuilder = ...
    """
    Returns  the view break builder 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewBreak`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewBreakBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ViewCommonViewLabel: NXOpen.Drawings.ViewCommonViewLabelBuilder = ...
    """
    Returns  the view Common View label builder 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewCommonViewLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewCommonViewLabelBuilder` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`NXOpen.Drawings.ViewStyleBuilder.ViewCommonViewLabel` instead.
    
    License requirements: None.
    """
    ViewDetailLabel: NXOpen.Drawings.ViewDetailLabelBuilder = ...
    """
    Returns     the view detail label builder 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewDetailLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewDetailLabelBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ViewLabel: NXOpen.Drawings.ViewLabelBuilder = ...
    """
    Returns     the view label builder 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewLabelBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ViewProjectedLabel: NXOpen.Drawings.ViewProjectedLabelBuilder = ...
    """
    Returns     the view projected label builder 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewProjectedLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewProjectedLabelBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ViewSectionLabel: NXOpen.Drawings.ViewSectionLabelBuilder = ...
    """
    Returns     the view section label builder 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewSectionLabel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewSectionLabelBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ViewSectionLine: NXOpen.Drawings.ViewSectionLineBuilder = ...
    """
    Returns     the Section Line builder 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewSectionLine`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewSectionLineBuilder` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`NXOpen.Drawings.ViewStyleBuilder.ViewSectionLineStyleBuilder` instead.
    
    License requirements: None.
    """
    ViewStyle: NXOpen.Drawings.ViewStyleBuilder = ...
    """
    Returns  the view style builder 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewStyleBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ViewWorkflow: NXOpen.Drawings.ViewWorkflowBuilder = ...
    """
    Returns  the view workflow builder 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewWorkflow`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewWorkflowBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    VisualDrawingCompare: NXOpen.Drawings.VisualDrawingComparePrefsBuilder = ...
    """
    Returns  the visual drawing compare settings builder 
    
    <hr>
    
    Getter Method
    
    Signature ``VisualDrawingCompare`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.VisualDrawingComparePrefsBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Workflow: NXOpen.Drawings.GeneralWorkFlowBuilder = ...
    """
    Returns     the general workflow builder 
    
    <hr>
    
    Getter Method
    
    Signature ``Workflow`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.GeneralWorkFlowBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: PreferencesBuilder = ...  # unknown typename


class AttributeItemBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Drafting.AttributeItemBuilder`.  
    
    This class is
    used to specify information about a single NX attribute.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.AutomationManager.CreateAttributeItemBuilder`
    
    .. versionadded:: NX8.0.0
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
    
    Title: str = ...
    """
    Returns or sets  the title.  
    
    <hr>
    
    Getter Method
    
    Signature ``Title`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Title`` 
    
    :param attributeTitle: 
    :type attributeTitle: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Value: str = ...
    """
    Returns or sets  the value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param attributeValue: 
    :type attributeValue: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Null: AttributeItemBuilder = ...  # unknown typename


class AutomationPreferencesBuilder(NXOpen.Builder):
    """
    the builder for Drafting Automation Preferences   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.AutomationManager.CreatePreferencesBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    def GetRulesList(self) -> 'list[str]':
        """
        Get the ordered rules list  
        
        Signature ``GetRulesList()`` 
        
        :returns:  Rules list  
        :rtype: list of str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRulesList(self, rules: 'list[str]') -> None:
        """
        Set the ordered rules list 
        
        Signature ``SetRulesList(rules)`` 
        
        :param rules:  Rules list  
        :type rules: list of str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_drawing_auto ("NX Drawing Automation")
        """
        ...
    
    AllowFeetInchFractionForDimensionGreaterThan: bool = ...
    """
    Returns or sets  the determination of the feet inch fraction display for dimension greater than 
    
    <hr>
    
    Getter Method
    
    Signature ``AllowFeetInchFractionForDimensionGreaterThan`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowFeetInchFractionForDimensionGreaterThan`` 
    
    :param allowFeetInchFractionForDimensionGreaterThan: 
    :type allowFeetInchFractionForDimensionGreaterThan: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    AllowInchFractionToNearest: bool = ...
    """
    Returns or sets  the determination of the display for inch fraction to nearest 
    
    <hr>
    
    Getter Method
    
    Signature ``AllowInchFractionToNearest`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowInchFractionToNearest`` 
    
    :param allowInchFractionToNearest: 
    :type allowInchFractionToNearest: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    AnnotationInsideGeometry: bool = ...
    """
    Returns or sets  the annotation inside geometry 
    
    <hr>
    
    Getter Method
    
    Signature ``AnnotationInsideGeometry`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnnotationInsideGeometry`` 
    
    :param annotationInsideGeometry: 
    :type annotationInsideGeometry: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    DisplayRegion: bool = ...
    """
    Returns or sets  the display in non template 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayRegion`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayRegion`` 
    
    :param displayRegion: 
    :type displayRegion: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    DisplayRegionLabel: bool = ...
    """
    Returns or sets  the display region label 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayRegionLabel`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayRegionLabel`` 
    
    :param displayRegionLabel: 
    :type displayRegionLabel: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    DistanceBetweenAnnotations: float = ...
    """
    Returns or sets  the distance between annotations 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceBetweenAnnotations`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceBetweenAnnotations`` 
    
    :param distanceBetweenAnnotations: 
    :type distanceBetweenAnnotations: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    EqualDimensionCompareTolerance: float = ...
    """
    Returns or sets  the equal dimension compare tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``EqualDimensionCompareTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EqualDimensionCompareTolerance`` 
    
    :param equalDimensionCompareTolerance: 
    :type equalDimensionCompareTolerance: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    FeetInchFractionForDimensionGreaterThan: float = ...
    """
    Returns or sets  the feet inch fraction for dimension greater than 
    
    <hr>
    
    Getter Method
    
    Signature ``FeetInchFractionForDimensionGreaterThan`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FeetInchFractionForDimensionGreaterThan`` 
    
    :param feetInchFractionForDimensionGreaterThan: 
    :type feetInchFractionForDimensionGreaterThan: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    HideFeetInchMark: bool = ...
    """
    Returns or sets  the hide feet inch mark 
    
    <hr>
    
    Getter Method
    
    Signature ``HideFeetInchMark`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HideFeetInchMark`` 
    
    :param hideFeetInchMark: 
    :type hideFeetInchMark: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    InchFractionToNearest: float = ...
    """
    Returns or sets  the inch fraction to nearest 
    
    <hr>
    
    Getter Method
    
    Signature ``InchFractionToNearest`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InchFractionToNearest`` 
    
    :param inchFractionToNearest: 
    :type inchFractionToNearest: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    MaximumDistanceToGeometry: float = ...
    """
    Returns or sets  the maximum distance to geometry 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumDistanceToGeometry`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumDistanceToGeometry`` 
    
    :param maximumDistanceToGeometry: 
    :type maximumDistanceToGeometry: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    MinimumDistanceToGeometry: float = ...
    """
    Returns or sets  the minimum distance to geometry 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumDistanceToGeometry`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumDistanceToGeometry`` 
    
    :param minimumDistanceToGeometry: 
    :type minimumDistanceToGeometry: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    ReferenceGeometrySearchDistance: float = ...
    """
    Returns or sets  the reference geometry search distance 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceGeometrySearchDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceGeometrySearchDistance`` 
    
    :param referenceGeometrySearchDistance: 
    :type referenceGeometrySearchDistance: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    RegionColor: NXOpen.NXColor = ...
    """
    Returns or sets  the region color 
    
    <hr>
    
    Getter Method
    
    Signature ``RegionColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RegionColor`` 
    
    :param regionColor: 
    :type regionColor: Id 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    RegionFont: NXOpen.Preferences.PartDraftingFontType = ...
    """
    Returns or sets  the region font 
    
    <hr>
    
    Getter Method
    
    Signature ``RegionFont`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Preferences.PartDraftingFontType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RegionFont`` 
    
    :param regionFont: 
    :type regionFont: :py:class:`NXOpen.Preferences.PartDraftingFontType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    RegionWidth: NXOpen.Preferences.PartDraftingWidthType = ...
    """
    Returns or sets  the region width 
    
    <hr>
    
    Getter Method
    
    Signature ``RegionWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Preferences.PartDraftingWidthType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RegionWidth`` 
    
    :param regionWidth: 
    :type regionWidth: :py:class:`NXOpen.Preferences.PartDraftingWidthType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    SecondaryContentHiddenLineColor: NXOpen.NXColor = ...
    """
    Returns or sets  the secondary content hidden line color 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryContentHiddenLineColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondaryContentHiddenLineColor`` 
    
    :param secondaryContentHiddenLineColor: 
    :type secondaryContentHiddenLineColor: Id 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    SecondaryContentHiddenLineFont: NXOpen.Preferences.PartDraftingFontType = ...
    """
    Returns or sets  the secondary content hidden line font 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryContentHiddenLineFont`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Preferences.PartDraftingFontType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondaryContentHiddenLineFont`` 
    
    :param secondaryContentHiddenLineFont: 
    :type secondaryContentHiddenLineFont: :py:class:`NXOpen.Preferences.PartDraftingFontType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    SecondaryContentHiddenLineWidth: NXOpen.Preferences.PartDraftingWidthType = ...
    """
    Returns or sets  the secondary content hidden line width 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryContentHiddenLineWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Preferences.PartDraftingWidthType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondaryContentHiddenLineWidth`` 
    
    :param secondaryContentHiddenLineWidth: 
    :type secondaryContentHiddenLineWidth: :py:class:`NXOpen.Preferences.PartDraftingWidthType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    SecondaryContentVisibleLineColor: NXOpen.NXColor = ...
    """
    Returns or sets  the secondary content visible line color 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryContentVisibleLineColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondaryContentVisibleLineColor`` 
    
    :param secondaryContentVisibleLineColor: 
    :type secondaryContentVisibleLineColor: Id 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    SecondaryContentVisibleLineFont: NXOpen.Preferences.PartDraftingFontType = ...
    """
    Returns or sets  the secondary content visible line font 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryContentVisibleLineFont`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Preferences.PartDraftingFontType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondaryContentVisibleLineFont`` 
    
    :param secondaryContentVisibleLineFont: 
    :type secondaryContentVisibleLineFont: :py:class:`NXOpen.Preferences.PartDraftingFontType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    SecondaryContentVisibleLineWidth: NXOpen.Preferences.PartDraftingWidthType = ...
    """
    Returns or sets  the secondary content visible line width 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryContentVisibleLineWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Preferences.PartDraftingWidthType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondaryContentVisibleLineWidth`` 
    
    :param secondaryContentVisibleLineWidth: 
    :type secondaryContentVisibleLineWidth: :py:class:`NXOpen.Preferences.PartDraftingWidthType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Null: AutomationPreferencesBuilder = ...  # unknown typename


class AnnotateViewsBuilderExistingAutomaticAnnotationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AnnotateViewsBuilderExistingAutomaticAnnotation():
    """
    Option to delete or preserve existing automatic annotations when annotation views command
    is run. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Delete", " - "
       "Preserve", " - "
    """
    Delete = 0  # AnnotateViewsBuilderExistingAutomaticAnnotationMemberType
    Preserve = 1  # AnnotateViewsBuilderExistingAutomaticAnnotationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AnnotateViewsBuilder(NXOpen.Builder):
    """
    This class is used to annotate views based on the knowledge fusion rules.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.AutomationManager.CreateAnnotateViewsBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    class ExistingAutomaticAnnotation():
        """
        Option to delete or preserve existing automatic annotations when annotation views command
        is run. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Delete", " - "
           "Preserve", " - "
        """
        Delete = 0  # AnnotateViewsBuilderExistingAutomaticAnnotationMemberType
        Preserve = 1  # AnnotateViewsBuilderExistingAutomaticAnnotationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    ExistingAutomaticAnnotationOption: AnnotateViewsBuilderExistingAutomaticAnnotation = ...
    """
    Returns or sets  the existing automatic annotation option 
    
    <hr>
    
    Getter Method
    
    Signature ``ExistingAutomaticAnnotationOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drafting.AnnotateViewsBuilderExistingAutomaticAnnotation` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExistingAutomaticAnnotationOption`` 
    
    :param existingAutomaticAnnotationOption: 
    :type existingAutomaticAnnotationOption: :py:class:`NXOpen.Drafting.AnnotateViewsBuilderExistingAutomaticAnnotation` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Views: NXOpen.Drawings.SelectDraftingViewList = ...
    """
    Returns  the views to annotate 
    
    <hr>
    
    Getter Method
    
    Signature ``Views`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.SelectDraftingViewList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Null: AnnotateViewsBuilder = ...  # unknown typename


class DistributeAnnotationsBuilder(NXOpen.Builder):
    """
    This class is used to distribute annotations associated to a view.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.AutomationManager.CreateDistributeAnnotationsBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Views: NXOpen.Drawings.SelectDraftingViewList = ...
    """
    Returns  the views in which to distribute annotations.  
    
    <hr>
    
    Getter Method
    
    Signature ``Views`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.SelectDraftingViewList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: DistributeAnnotationsBuilder = ...  # unknown typename


class AttributeItemBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[AttributeItemBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: AttributeItemBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        
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
    
    
    def FindIndex(self, obj: AttributeItemBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> AttributeItemBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        
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
    def Erase(self, obj: AttributeItemBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: AttributeItemBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
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
    
    
    def GetContents(self) -> 'list[AttributeItemBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[AttributeItemBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        
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
    def Swap(self, object1: AttributeItemBuilder, object2: AttributeItemBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: AttributeItemBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        
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
    Null: AttributeItemBuilderList = ...  # unknown typename


class BaseEditSettingsBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Drafting.BaseEditSettingsBuilder`.  
    
    It provides an interface for editing settings.
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX9.0.0
    """
    Null: BaseEditSettingsBuilder = ...  # unknown typename


class CutCopyPasteBuilderTypePasteMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CutCopyPasteBuilderTypePaste():
    """
    Specifies the paste type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Transform", "Transform type"
       "Tracking", "Tracking type"
    """
    Transform = 0  # CutCopyPasteBuilderTypePasteMemberType
    Tracking = 1  # CutCopyPasteBuilderTypePasteMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CutCopyPasteBuilderTypeOperationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CutCopyPasteBuilderTypeOperation():
    """
    Specifies the copy cut operation type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Copy", "Copy type"
       "Cut", "Cut type"
    """
    Copy = 0  # CutCopyPasteBuilderTypeOperationMemberType
    Cut = 1  # CutCopyPasteBuilderTypeOperationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CutCopyPasteBuilder(NXOpen.Builder):
    """
    Represents a paste in Drafting.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.DraftingApplicationManager.CreateCutCopyPasteBuilder`
    
    Default values.
    
    ========================  =====================
    Property                  Value
    ========================  =====================
    Transform.DeltaEnum       ReferenceWcsWorkPart 
    ------------------------  ---------------------
    Transform.DeltaXc.Value   0.0 
    ------------------------  ---------------------
    Transform.DeltaYc.Value   0.0 
    ------------------------  ---------------------
    Transform.DeltaZc.Value   0.0 
    ------------------------  ---------------------
    Transform.Option          Distance 
    ========================  =====================
    
    .. versionadded:: NX7.5.0
    """
    
    class TypePaste():
        """
        Specifies the paste type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Transform", "Transform type"
           "Tracking", "Tracking type"
        """
        Transform = 0  # CutCopyPasteBuilderTypePasteMemberType
        Tracking = 1  # CutCopyPasteBuilderTypePasteMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TypeOperation():
        """
        Specifies the copy cut operation type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Copy", "Copy type"
           "Cut", "Cut type"
        """
        Copy = 0  # CutCopyPasteBuilderTypeOperationMemberType
        Cut = 1  # CutCopyPasteBuilderTypeOperationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetDefaultToPoint(self) -> NXOpen.Point3d:
        """
        Get the default to point.  
        
        The drop location.  
        
        Signature ``GetDefaultToPoint()`` 
        
        :returns:  the drop location  
        :rtype: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultToPoint(self, dropLocation: NXOpen.Point3d) -> None:
        """
        Set the default to point.  
        
        The drop location. 
        
        Signature ``SetDefaultToPoint(dropLocation)`` 
        
        :param dropLocation:  the drop location  
        :type dropLocation: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def SetMoveOnCommit(self, rot: NXOpen.Matrix3x3, trans: NXOpen.Vector3d) -> None:
        """
        Set the final motion from the drop location.  
        
        Signature ``SetMoveOnCommit(rot, trans)`` 
        
        :param rot:  rotational part of motion  
        :type rot: :py:class:`NXOpen.Matrix3x3` 
        :param trans:  translation part of motion  
        :type trans: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def InitPaste(self) -> None:
        """
        Make the initial drop.  
        
        Signature ``InitPaste()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    CutCopyPasteLeader: CutCopyPasteLeaderBuilder = ...
    """
    Returns  the leader builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``CutCopyPasteLeader`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drafting.CutCopyPasteLeaderBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    DestinationView: NXOpen.View = ...
    """
    Returns or sets  the destination view.  
    
    Either a drafting view or sheet view. 
    
    <hr>
    
    Getter Method
    
    Signature ``DestinationView`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.View` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DestinationView`` 
    
    :param destinationView: 
    :type destinationView: :py:class:`NXOpen.View` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: drafting ("DRAFTING")
    """
    ObjectsToCopy: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the objects list to copy.  
    
    May include drafting geometry, sketch objects
    and simple annotations.
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectsToCopy`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Originals: CutCopyPasteBuilderTypeOperation = ...
    """
    Returns or sets  the operation type.  
    
    If it is copy, we will keept the originals. If it is cut, we will delete the originals 
    
    <hr>
    
    Getter Method
    
    Signature ``Originals`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drafting.CutCopyPasteBuilderTypeOperation` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Originals`` 
    
    :param originals: 
    :type originals: :py:class:`NXOpen.Drafting.CutCopyPasteBuilderTypeOperation` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    OutputObjects: NXOpen.SelectTaggedObjectList = ...
    """
    Returns   the output Objects 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PasteType: CutCopyPasteBuilderTypePaste = ...
    """
    Returns or sets  the paste type 
    
    <hr>
    
    Getter Method
    
    Signature ``PasteType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drafting.CutCopyPasteBuilderTypePaste` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PasteType`` 
    
    :param pasteType: 
    :type pasteType: :py:class:`NXOpen.Drafting.CutCopyPasteBuilderTypePaste` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    PlaneToRestrictMotion: NXOpen.Plane = ...
    """
    Returns or sets   the plane to restrict motion 
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneToRestrictMotion`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneToRestrictMotion`` 
    
    :param plan: 
    :type plan: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: drafting ("DRAFTING")
    """
    Transform: NXOpen.GeometricUtilities.ModlMotion = ...
    """
    Returns  the motion from the default paste position 
    
    <hr>
    
    Getter Method
    
    Signature ``Transform`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.ModlMotion` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: CutCopyPasteBuilder = ...  # unknown typename


class DraftingApplicationManager():
    """
    Represents an object that manages drafting objects and member views.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX7.5.0
    """
    
    def CreateCutCopyPasteBuilder(self) -> CutCopyPasteBuilder:
        """
        Creates the CutCopyPaste builder  
        
        Signature ``CreateCutCopyPasteBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.CutCopyPasteBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateMoveToDrawingViewBuilder(self) -> MoveToDrawingViewBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.MoveToDrawingViewBuilder`  
        
        Signature ``CreateMoveToDrawingViewBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.MoveToDrawingViewBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateSmashDrawingViewBuilder(self) -> SmashDrawingViewBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.SmashDrawingViewBuilder`  
        
        Signature ``CreateSmashDrawingViewBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.SmashDrawingViewBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    TitleBlocks: NXOpen.Annotations.TitleBlockCollection = ...
    """
    Returns the TitleBlockCollection belonging to this part 
    
    Signature ``TitleBlocks`` 
    
    .. versionadded:: NX8.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.TitleBlockCollection`
    """


class RulesBuilder(NXOpen.Builder):
    """
    This class is used to specify knowledge fusion rules in a drawing template.  
    
    The rules are 
    executed when the template is instantiated. 
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.AutomationManager.CreateRulesBuilder`
    
    .. versionadded:: NX8.0.0
    """
    DimensionRule: str = ...
    """
    Returns or sets  the dimension rule 
    
    <hr>
    
    Getter Method
    
    Signature ``DimensionRule`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DimensionRule`` 
    
    :param dimensionRule: 
    :type dimensionRule: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    NoteRule: str = ...
    """
    Returns or sets  the note rule 
    
    <hr>
    
    Getter Method
    
    Signature ``NoteRule`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NoteRule`` 
    
    :param noteRule: 
    :type noteRule: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    SymbolRule: str = ...
    """
    Returns or sets  the symbol rule 
    
    <hr>
    
    Getter Method
    
    Signature ``SymbolRule`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SymbolRule`` 
    
    :param symbolRule: 
    :type symbolRule: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Null: RulesBuilder = ...  # unknown typename


class CutCopyPasteLeaderBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a Drafting Paste, especially when reassociating a leader on paste.  
    
    .. versionadded:: NX8.0.0
    """
    
    def SetMoveOnCommit(self, rot: NXOpen.Matrix3x3, trans: NXOpen.Vector3d) -> None:
        """
        Set the final motion from the drop location.  
        
        Signature ``SetMoveOnCommit(rot, trans)`` 
        
        :param rot:  rotational part of motion  
        :type rot: :py:class:`NXOpen.Matrix3x3` 
        :param trans:  translation part of motion  
        :type trans: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: drafting ("DRAFTING")
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
    
    DestinationView: NXOpen.View = ...
    """
    Returns or sets  the destination view.  
    
    Either a drafting view or sheet view. 
    
    <hr>
    
    Getter Method
    
    Signature ``DestinationView`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.View` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DestinationView`` 
    
    :param destinationView: 
    :type destinationView: :py:class:`NXOpen.View` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    IsLeaderSelection: bool = ...
    """
    Returns or sets  the variable of is leader selection or not
    
    <hr>
    
    Getter Method
    
    Signature ``IsLeaderSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsLeaderSelection`` 
    
    :param isLeaderSelection:  True If it is leader selection 
    :type isLeaderSelection: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    LeaderSelection: NXOpen.SelectTaggedObject = ...
    """
    Returns  the selection to reassociate single leader 
    
    <hr>
    
    Getter Method
    
    Signature ``LeaderSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObject` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ReassociateLeader: bool = ...
    """
    Returns or sets  the flag to reassociate a leader 
    
    <hr>
    
    Getter Method
    
    Signature ``ReassociateLeader`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReassociateLeader`` 
    
    :param reassociateLeader: 
    :type reassociateLeader: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    Selection: NXOpen.SelectTaggedObject = ...
    """
    Returns  the selection to reassociate leader 
    
    <hr>
    
    Getter Method
    
    Signature ``Selection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObject` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: CutCopyPasteLeaderBuilder = ...  # unknown typename


class DrawingAutomationWizard(NXOpen.TransientObject):
    """
    Represents callback data for the drawing automation wizard.  
    
    .. versionadded:: NX8.5.3
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX8.5.3
        
        License requirements: None.
        """
        ...
    
    Builder: DrawingCreationWizardBuilder = ...
    """
    Returns or sets  the drawing automation wizard builder 
    
    <hr>
    
    Getter Method
    
    Signature ``Builder`` 
    
    :returns:  drawing automation wizard builder  
    :rtype: :py:class:`NXOpen.Drafting.DrawingCreationWizardBuilder` 
    
    .. versionadded:: NX8.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Builder`` 
    
    :param builder:  drawing automation wizard builder  
    :type builder: :py:class:`NXOpen.Drafting.DrawingCreationWizardBuilder` 
    
    .. versionadded:: NX8.5.3
    
    License requirements: None.
    """
    ContinueProcessing: bool = ...
    """
    Returns or sets  the flag denoting whether or not to create the booklet in the current session 
    
    <hr>
    
    Getter Method
    
    Signature ``ContinueProcessing`` 
    
    :returns:  flag denoting whether or not to create the booklet in the current session  
    :rtype: bool 
    
    .. versionadded:: NX8.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContinueProcessing`` 
    
    :param continueProcessing:  flag denoting whether or not to create the booklet in the current session  
    :type continueProcessing: bool 
    
    .. versionadded:: NX8.5.3
    
    License requirements: None.
    """
    ErrorCode: int = ...
    """
    Returns or sets  the error code to be returned from the callback 
    
    <hr>
    
    Getter Method
    
    Signature ``ErrorCode`` 
    
    :returns:  error code returned from callback  
    :rtype: int 
    
    .. versionadded:: NX8.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ErrorCode`` 
    
    :param errorCode:  error code returned from callback  
    :type errorCode: int 
    
    .. versionadded:: NX8.5.3
    
    License requirements: None.
    """
    Part: NXOpen.Part = ...
    """
    Returns or sets  the part from which the booklet drawings are created 
    
    <hr>
    
    Getter Method
    
    Signature ``Part`` 
    
    :returns:  part from which the booklet drawings are created  
    :rtype: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX8.5.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Part`` 
    
    :param part:  part from which the booklet drawings are created  
    :type part: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX8.5.3
    
    License requirements: None.
    """


class SettingsManager():
    """
    Represents an object that manages drafting settings.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX9.0.0
    """
    
    def CreatePreferencesBuilder(self) -> PreferencesBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.PreferencesBuilder` 
        
        Signature ``CreatePreferencesBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.PreferencesBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def CreateAnnotationEditSettingsBuilder(self, objects: 'list[NXOpen.DisplayableObject]') -> NXOpen.Annotations.EditSettingsBuilder:
        """
        Creates a :py:class:`NXOpen.Annotations.EditSettingsBuilder`
        
        For multiple object settings, first create primary settings builder by passing all 
        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
        object starting from second selected object.
        Client must call :py:meth:`Drafting.SettingsManager.ProcessForMultipleObjectsSettings` 
        after creating all settings builder for selected objects.
        
        Signature ``CreateAnnotationEditSettingsBuilder(objects)`` 
        
        :param objects:  the array of objects for style, None not allowed 
        :type objects: list of :py:class:`NXOpen.DisplayableObject` 
        :returns:  The annotations settings builder  
        :rtype: :py:class:`NXOpen.Annotations.EditSettingsBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def CreateDrawingEditSectionLineSettingsBuilder(self, sectionLines: 'list[NXOpen.Drawings.SectionLine]') -> NXOpen.Drawings.EditSectionLineSettingsBuilder:
        """
        Creates a :py:class:`NXOpen.Drawings.EditSectionLineSettingsBuilder`
        
        For multiple object settings, first create primary settings builder by passing all 
        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
        object starting from second selected object.
        Client must call :py:meth:`Drafting.SettingsManager.ProcessForMultipleObjectsSettings` 
        after creating all settings builder for selected objects.
        
        Signature ``CreateDrawingEditSectionLineSettingsBuilder(sectionLines)`` 
        
        :param sectionLines:  The array of object for section line style, None is allowed.  
        :type sectionLines: list of :py:class:`NXOpen.Drawings.SectionLine` 
        :returns:  The section line settings builder  
        :rtype: :py:class:`NXOpen.Drawings.EditSectionLineSettingsBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def CreateDrawingEditViewSettingsBuilder(self, views: 'list[NXOpen.View]') -> NXOpen.Drawings.EditViewSettingsBuilder:
        """
        Creates a :py:class:`NXOpen.Drawings.EditViewSettingsBuilder`
        
        For multiple object settings, first create primary settings builder by passing all 
        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
        object starting from second selected object.
        Client must call :py:meth:`Drafting.SettingsManager.ProcessForMultipleObjectsSettings` 
        after creating all settings builder for selected objects.
        
        Signature ``CreateDrawingEditViewSettingsBuilder(views)`` 
        
        :param views:  The array of objects for view style, None not allowed.  
        :type views: list of :py:class:`NXOpen.View` 
        :returns:  The view settings builder  
        :rtype: :py:class:`NXOpen.Drawings.EditViewSettingsBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def CreateLayout2dEditComponentSettingsBuilder(self, components: 'list[NXOpen.Layout2d.Component]') -> NXOpen.Layout2d.EditComponentSettingsBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.EditComponentSettingsBuilder` 
        This builder is the interface to edit the 2d component settings of layout
        
        For multiple object settings, first create primary settings builder by passing all 
        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
        object starting from second selected object.
        Client must call :py:meth:`Drafting.SettingsManager.ProcessForMultipleObjectsSettings` 
        after creating all settings builder for selected objects.
        
        Signature ``CreateLayout2dEditComponentSettingsBuilder(components)`` 
        
        :param components:  The array of components to edit.  None is not allowed  
        :type components: list of :py:class:`NXOpen.Layout2d.Component` 
        :returns:  The layout2d component settings builder  
        :rtype: :py:class:`NXOpen.Layout2d.EditComponentSettingsBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateDrawingEditViewLabelSettingsBuilder(self, viewLabels: 'list[NXOpen.DisplayableObject]') -> NXOpen.Drawings.EditViewLabelSettingsBuilder:
        """
        Creates a :py:class:`NXOpen.Drawings.EditViewLabelSettingsBuilder`
        
        For multiple object settings, first create primary settings builder by passing all 
        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
        object starting from second selected object.
        Client must call :py:meth:`Drafting.SettingsManager.ProcessForMultipleObjectsSettings` 
        after creating all settings builder for selected objects.
        
        Signature ``CreateDrawingEditViewLabelSettingsBuilder(viewLabels)`` 
        
        :param viewLabels:  the array of view labels to edit, None is not allowed.  
        :type viewLabels: list of :py:class:`NXOpen.DisplayableObject` 
        :returns:  The view label settings builder  
        :rtype: :py:class:`NXOpen.Drawings.EditViewLabelSettingsBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def CreateTableEditSettingsBuilder(self, objects: 'list[NXOpen.DisplayableObject]') -> NXOpen.Annotations.TableEditSettingsBuilder:
        """
        Creates a :py:class:`NXOpen.Annotations.TableEditSettingsBuilder`
        
        For multiple object settings, first create primary settings builder by passing all 
        selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
        object starting from second selected object.
        Client must call :py:meth:`Drafting.SettingsManager.ProcessForMultipleObjectsSettings` 
        after creating all settings builder for selected objects.
        
        Signature ``CreateTableEditSettingsBuilder(objects)`` 
        
        :param objects:  the array of objects for style, If None, section or cell preferences for all sections or cells will be set.  
        :type objects: list of :py:class:`NXOpen.DisplayableObject` 
        :returns:  The table settings builder  
        :rtype: :py:class:`NXOpen.Annotations.TableEditSettingsBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def ProcessForMutipleObjectsSettings(self, editSettingsBuilders: 'list[BaseEditSettingsBuilder]') -> None:
        """
        Process edit settings builders for mutiple objects
        
        Signature ``ProcessForMutipleObjectsSettings(editSettingsBuilders)`` 
        
        :param editSettingsBuilders: 
        :type editSettingsBuilders: list of :py:class:`NXOpen.Drafting.BaseEditSettingsBuilder` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`Drafting.SettingsManager.ProcessForMultipleObjectsSettings` instead.
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def ProcessForMultipleObjectsSettings(self, editSettingsBuilders: 'list[BaseEditSettingsBuilder]') -> None:
        """
        Process edit settings builders for multiple objects
        User must call this API for multiple object settings and pass all edit settings builders for selected objects
        
        Signature ``ProcessForMultipleObjectsSettings(editSettingsBuilders)`` 
        
        :param editSettingsBuilders: 
        :type editSettingsBuilders: list of :py:class:`NXOpen.Drafting.BaseEditSettingsBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    


class SpecifyRuleBuilder(NXOpen.Builder):
    """
    This class is used to specify knowledge fusion rule for a note object in a drawing template.  
    
    The rule is stored on the note and is executed when the template is instantiated. 
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.AutomationManager.CreateSpecifyRuleBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Note: NXOpen.Annotations.Note = ...
    """
    Returns or sets  the note to add rule to
    
    <hr>
    
    Getter Method
    
    Signature ``Note`` 
    
    :returns:  Note object  
    :rtype: :py:class:`NXOpen.Annotations.Note` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Note`` 
    
    :param note:  Note object  
    :type note: :py:class:`NXOpen.Annotations.Note` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Rule: str = ...
    """
    Returns or sets  the rule 
    
    <hr>
    
    Getter Method
    
    Signature ``Rule`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Rule`` 
    
    :param rule: 
    :type rule: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Null: SpecifyRuleBuilder = ...  # unknown typename


class SmashDrawingViewBuilder(NXOpen.Builder):
    """
    This builder allows the user to break a Drawing View into its parts and delete the Drawing View
    
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.DraftingApplicationManager.CreateSmashDrawingViewBuilder`
    
    .. versionadded:: NX8.5.0
    """
    SelectView: NXOpen.Drawings.SelectDraftingView = ...
    """
    Returns  the select drawing views to smash
    
    <hr>
    
    Getter Method
    
    Signature ``SelectView`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.SelectDraftingView` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: SmashDrawingViewBuilder = ...  # unknown typename


class AutomationRuleBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Drafting.AutomationRuleBuilder`   
    
    .. versionadded:: NX9.0.0
    """
    
    def GetRulesList(self) -> 'list[str]':
        """
        The automation rules in the order of decreasing priorities.  
        
        So, the first
        rule in the VLA has the highest priority  
        
        Signature ``GetRulesList()`` 
        
        :returns:  Rules list  
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRulesList(self, rules: 'list[str]') -> None:
        """
        The set of order list 
        
        Signature ``SetRulesList(rules)`` 
        
        :param rules:  Rules list  
        :type rules: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_drawing_auto ("NX Drawing Automation")
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
    
    AllowInsideGeometry: bool = ...
    """
    Returns or sets  the allow inside geometry option allows annotation inside geometry 
    
    <hr>
    
    Getter Method
    
    Signature ``AllowInsideGeometry`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowInsideGeometry`` 
    
    :param allowInsideGeometry: 
    :type allowInsideGeometry: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    EqualDimensionTolerance: float = ...
    """
    Returns or sets  the equal dimension comparison tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``EqualDimensionTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EqualDimensionTolerance`` 
    
    :param equalDimensionTolerance: 
    :type equalDimensionTolerance: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    HideFeetAndInchMarks: bool = ...
    """
    Returns or sets  the hide feet and inch marks option Show/Hide feet and inch marks.  
    
    True to hide and False to show 
    
    <hr>
    
    Getter Method
    
    Signature ``HideFeetAndInchMarks`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HideFeetAndInchMarks`` 
    
    :param hideFeetAndInchMarks: 
    :type hideFeetAndInchMarks: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Increment: float = ...
    """
    Returns or sets  the increment Display dimension value in inches and fractions to nearest specified value 
    
    <hr>
    
    Getter Method
    
    Signature ``Increment`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Increment`` 
    
    :param increment: 
    :type increment: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    LowerThreshold: float = ...
    """
    Returns or sets  the lower threshold display dimension value in feet, inches and fractions if
    it is greater than the specified value 
    
    <hr>
    
    Getter Method
    
    Signature ``LowerThreshold`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LowerThreshold`` 
    
    :param lowerThreshold: 
    :type lowerThreshold: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    MaximumGapToGeometry: float = ...
    """
    Returns or sets  the maximum gap from the view geometry to the annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumGapToGeometry`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumGapToGeometry`` 
    
    :param maximumGapToGeometry: 
    :type maximumGapToGeometry: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    MinimumGapBetweenAnnotations: float = ...
    """
    Returns or sets  the minimum gap between annotations 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumGapBetweenAnnotations`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumGapBetweenAnnotations`` 
    
    :param minimumGapBetweenAnnotations: 
    :type minimumGapBetweenAnnotations: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    MinimumGapToGeometry: float = ...
    """
    Returns or sets  the minimum gap from the view geometry to the annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumGapToGeometry`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumGapToGeometry`` 
    
    :param minimumGapToGeometry: 
    :type minimumGapToGeometry: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    ReferenceGeometryGapTolerance: float = ...
    """
    Returns or sets  the reference geometry search gap tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceGeometryGapTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceGeometryGapTolerance`` 
    
    :param referenceGeometryGapTolerance: 
    :type referenceGeometryGapTolerance: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    RoundFeetAndInches: bool = ...
    """
    Returns or sets  the round feet and inches determine wheather or not to display dimension value 
    in inches and fractions to nearest specified value 
    
    <hr>
    
    Getter Method
    
    Signature ``RoundFeetAndInches`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RoundFeetAndInches`` 
    
    :param roundFeetAndInches: 
    :type roundFeetAndInches: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    UseFeetInchesAndFraction: bool = ...
    """
    Returns or sets  the use feet inches and fraction determine wheather or not to display dimension value 
    in feet, inches and fractions if it is greater than the specified value 
    
    <hr>
    
    Getter Method
    
    Signature ``UseFeetInchesAndFraction`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseFeetInchesAndFraction`` 
    
    :param useFeetInchesAndFraction: 
    :type useFeetInchesAndFraction: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Null: AutomationRuleBuilder = ...  # unknown typename


class DrawingCreationWizardBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Drafting.DrawingCreationWizardBuilder`.  
    
    This class is
    used to create Booklets (i.e. a set of fully populated drawings).  The builder operates
    in both create and edit modes as well as in native and managed (Teamcenter) modes.  The
    following information is important when using this builder in edit mode:<br/>
    
      * 
    Native Mode
    
        * 
    The :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.Folder` must be the first thing set after creating the builder.
    Setting this will populate the builder with the booklet's information.
    
      * 
    Managed Mode
    
        * 
    The :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.Number` and :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.Revision` must be the first things set after
    creating the builder (in that order).  The setting of the :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.Revision` will populate the builder with the booklet's information.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.AutomationManager.CreateDrawingCreationWizardBuilder`
    
    Default values.
    
    ===================  =====
    Property             Value
    ===================  =====
    ApplyTemplateToAll   0 
    ===================  =====
    
    .. versionadded:: NX8.0.0
    """
    
    def GetSummary(self) -> 'list[str]':
        """
        Returns the summary.  
        
        This is in HTML format.  
        
        Signature ``GetSummary()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSummary(self, summary: 'list[str]') -> None:
        """
        Sets the summary 
        
        Signature ``SetSummary(summary)`` 
        
        :param summary: 
        :type summary: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_drawing_auto ("NX Drawing Automation")
        """
        ...
    
    
    def SetObjectCreateBuilder(self, objectCreateBuilder: NXOpen.PDM.ObjectCreateBuilder) -> None:
        """
        Sets :py:class:`NXOpen.PDM.ObjectCreateBuilder` 
        
        Signature ``SetObjectCreateBuilder(objectCreateBuilder)`` 
        
        :param objectCreateBuilder: 
        :type objectCreateBuilder: :py:class:`NXOpen.PDM.ObjectCreateBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_drawing_auto ("NX Drawing Automation")
        """
        ...
    
    ApplyTemplateToAll: bool = ...
    """
    Returns or sets  the flag which controls the behavior of setting :py:meth:`NXOpen.Drafting.PrimaryContentItemBuilder.GeometryTemplate`
    on an item in :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.PrimaryContent`.  
    
    When set to true the builder
    will respond to the setting of :py:meth:`NXOpen.Drafting.PrimaryContentItemBuilder.GeometryTemplate` on an item in
    :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.PrimaryContent` by setting the same value on
    :py:meth:`NXOpen.Drafting.PrimaryContentItemBuilder.GeometryTemplate` on all of the other items in
    :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.PrimaryContent` 
    
    <hr>
    
    Getter Method
    
    Signature ``ApplyTemplateToAll`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ApplyTemplateToAll`` 
    
    :param applyTemplateToAll: 
    :type applyTemplateToAll: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Attributes: AttributeItemBuilderList = ...
    """
    Returns  the attributes.  
    
    <hr>
    
    Getter Method
    
    Signature ``Attributes`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drafting.AttributeItemBuilderList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    DetailID: str = ...
    """
    Returns or sets  the detail id.  
    
    <hr>
    
    Getter Method
    
    Signature ``DetailID`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DetailID`` 
    
    :param detailID: 
    :type detailID: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Discipline: str = ...
    """
    Returns or sets  the discipline.  
    
    <hr>
    
    Getter Method
    
    Signature ``Discipline`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Discipline`` 
    
    :param discipline: 
    :type discipline: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    DrawingStyle: str = ...
    """
    Returns or sets  the drawing style.  
    
    <hr>
    
    Getter Method
    
    Signature ``DrawingStyle`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DrawingStyle`` 
    
    :param drawingStyle: 
    :type drawingStyle: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    ExcludedContent: NXOpen.Assemblies.SelectComponentList = ...
    """
    Returns  the excluded content.  
    
    Setting a component into :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.ExcludedContent` 
    will cause that component to be removed from :py:meth:`NXOpen.Drafting.PrimaryContentItemBuilder.Content`
    of each item in :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.PrimaryContent` and 
    :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.SecondaryContent` if they contain that component. 
    
    <hr>
    
    Getter Method
    
    Signature ``ExcludedContent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Folder: str = ...
    """
    Returns or sets  the folder.  
    
    <hr>
    
    Getter Method
    
    Signature ``Folder`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Folder`` 
    
    :param foldername: 
    :type foldername: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    IntroductoryTemplate: str = ...
    """
    Returns or sets  the introductory template.  
    
    <hr>
    
    Getter Method
    
    Signature ``IntroductoryTemplate`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IntroductoryTemplate`` 
    
    :param introductoryTemplate: 
    :type introductoryTemplate: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Name: str = ...
    """
    Returns or sets  the name.  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    Number: str = ...
    """
    Returns or sets  the number.  
    
    This property is only used in managed mode and must be set before anything else.  
    
    <hr>
    
    Getter Method
    
    Signature ``Number`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Number`` 
    
    :param number: 
    :type number: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    PrimaryContent: PrimaryContentItemBuilderList = ...
    """
    Returns  the primary content.  
    
    Setting a component into :py:meth:`NXOpen.Drafting.PrimaryContentItemBuilder.Content` of an item in
    :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.PrimaryContent` will cause that component to be removed from 
    :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.SecondaryContent` and 
    :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.ExcludedContent` if they contain that component. 
    
    <hr>
    
    Getter Method
    
    Signature ``PrimaryContent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drafting.PrimaryContentItemBuilderList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    References: NXOpen.SelectNXObjectList = ...
    """
    Returns  the references.  
    
    <hr>
    
    Getter Method
    
    Signature ``References`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Revision: str = ...
    """
    Returns or sets  the revision.  
    
    This is only used in managed mode. In edit mode it must be set after the :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.Number` and at the time
    is set it will populate the builder with the booklet's information. 
    
    <hr>
    
    Getter Method
    
    Signature ``Revision`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Revision`` 
    
    :param revision: 
    :type revision: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_drawing_auto ("NX Drawing Automation")
    """
    SecondaryContent: NXOpen.Assemblies.SelectComponentList = ...
    """
    Returns  the secondary content.  
    
    Setting a component into :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.SecondaryContent` 
    will cause that component to be removed from :py:meth:`NXOpen.Drafting.PrimaryContentItemBuilder.Content`
    of each item in :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.PrimaryContent` and 
    :py:meth:`NXOpen.Drafting.DrawingCreationWizardBuilder.ExcludedContent` if they contain that component. 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryContent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: DrawingCreationWizardBuilder = ...  # unknown typename


class AutomationManager():
    """
    Represents a :py:class:`NXOpen.Drafting.AutomationManager`.  
    
    This class is
    used to create objects which are used in the automation of drawing creation.
    
    Use :py:meth:`NXOpen.DraftingManager.AutomationManager` to get the instance of this class.
    
    .. versionadded:: NX8.0.0
    """
    
    def CreatePrimaryContentItemBuilder(self) -> PrimaryContentItemBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder`  
        
        Signature ``CreatePrimaryContentItemBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAttributeItemBuilder(self) -> AttributeItemBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.AttributeItemBuilder`  
        
        Signature ``CreateAttributeItemBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.AttributeItemBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDrawingCreationWizardBuilder(self, isEditing: bool) -> DrawingCreationWizardBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.DrawingCreationWizardBuilder`  
        
        Signature ``CreateDrawingCreationWizardBuilder(isEditing)`` 
        
        :param isEditing:  If this is set to true then the builder will be configured for edit mode, otherwise it will be configured for create mode.  
        
        Please see the :py:class:`NXOpen.Drafting.DrawingCreationWizardBuilder` class documentation for more information on how                        to use the builder in these different modes.  
        :type isEditing: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.DrawingCreationWizardBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDrawingCreationWizardBuilderFromRule(self, className: str) -> DrawingCreationWizardBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.DrawingCreationWizardBuilder`  
        
        Signature ``CreateDrawingCreationWizardBuilderFromRule(className)`` 
        
        :param className:  Drawing Booklet class used to populate the builder  
        :type className: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.DrawingCreationWizardBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreatePreferencesBuilder(self) -> AutomationPreferencesBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.AutomationPreferencesBuilder`  
        
        Signature ``CreatePreferencesBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.AutomationPreferencesBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_drawing_auto ("NX Drawing Automation")
        """
        ...
    
    
    def CreateAnnotateViewsBuilder(self) -> AnnotateViewsBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.AnnotateViewsBuilder`  
        
        Signature ``CreateAnnotateViewsBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.AnnotateViewsBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateRulesBuilder(self) -> RulesBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.RulesBuilder`  
        
        Signature ``CreateRulesBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.RulesBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateSpecifyRuleBuilder(self) -> SpecifyRuleBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.SpecifyRuleBuilder`  
        
        Signature ``CreateSpecifyRuleBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.SpecifyRuleBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDistributeAnnotationsBuilder(self) -> DistributeAnnotationsBuilder:
        """
        Creates a :py:class:`NXOpen.Drafting.DistributeAnnotationsBuilder`  
        
        Signature ``CreateDistributeAnnotationsBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Drafting.DistributeAnnotationsBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRemainingPartsOfBooklet(self) -> tuple:
        """
        Returns the remaining loaded parts and remaining unloaded parts full names from the booklet 
        
        Signature ``GetRemainingPartsOfBooklet()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (remainingParts, remainingPartFileSpecs). remainingParts is a list of :py:class:`NXOpen.Part`. remainingPartFileSpecs is a list of str. 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    DrawingRegions: NXOpen.Drawings.DrawingRegionCollection = ...
    """
    Returns the RegionCollection instance  
    
    Signature ``DrawingRegions`` 
    
    .. versionadded:: NX8.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.DrawingRegionCollection`
    """


class PrimaryContentItemBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[PrimaryContentItemBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: PrimaryContentItemBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        
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
    
    
    def FindIndex(self, obj: PrimaryContentItemBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> PrimaryContentItemBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        
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
    def Erase(self, obj: PrimaryContentItemBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: PrimaryContentItemBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
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
    
    
    def GetContents(self) -> 'list[PrimaryContentItemBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[PrimaryContentItemBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        
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
    def Swap(self, object1: PrimaryContentItemBuilder, object2: PrimaryContentItemBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: PrimaryContentItemBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Drafting.PrimaryContentItemBuilder` 
        
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
    Null: PrimaryContentItemBuilderList = ...  # unknown typename


class MoveToDrawingViewBuilder(NXOpen.Builder):
    """
    This builder allows the user to extract contents from a sheet and transfer them to a new Drawing
    view, also provide some other options for view creation
    
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.DraftingApplicationManager.CreateMoveToDrawingViewBuilder`
    
    Default values.
    
    ==========================================================  =============
    Property                                                    Value
    ==========================================================  =============
    ViewScale.Denominator                                       1.0 
    ----------------------------------------------------------  -------------
    ViewScale.Numerator                                         1.0 
    ----------------------------------------------------------  -------------
    ViewScale.ScaleType                                         Ratio 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleGeneral.AngleSetting.Angle.Value         0 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleGeneral.AngleSetting.Associative         0 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleGeneral.AngleSetting.EvaluationPlane     DrawingSheet 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleOrientation.HingeLine.ReverseDirection   false 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleOrientation.HingeLine.VectorOption       Inferred 
    ----------------------------------------------------------  -------------
    ViewStyle.ViewStyleOrientation.Ovt.AssociativeOrientation   0 
    ----------------------------------------------------------  -------------
    XCoordinate                                                 0 
    ----------------------------------------------------------  -------------
    YCoordinate                                                 0 
    ==========================================================  =============
    
    .. versionadded:: NX8.5.0
    """
    SelectObjects: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the select objects from the current sheet
    
    <hr>
    
    Getter Method
    
    Signature ``SelectObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SelectPoint: NXOpen.Point = ...
    """
    Returns or sets  the select point to calculate the new created drawing view's reference point
    
    <hr>
    
    Getter Method
    
    Signature ``SelectPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectPoint`` 
    
    :param selectPoint: 
    :type selectPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_layout ("NX Layout")
    """
    TwoDOrientation: NXOpen.Drawings.View2dOrientBuilder = ...
    """
    Returns  the view orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``TwoDOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.View2dOrientBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ViewScale: NXOpen.Drawings.ViewScaleBuilder = ...
    """
    Returns  the view scale 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewScale`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewScaleBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ViewStyle: NXOpen.Drawings.ViewStyleBuilder = ...
    """
    Returns  the view style 
    
    <hr>
    
    Getter Method
    
    Signature ``ViewStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.ViewStyleBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    XCoordinate: float = ...
    """
    Returns or sets  the x coordinate to calculate the new created drawing view's reference point
    
    <hr>
    
    Getter Method
    
    Signature ``XCoordinate`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XCoordinate`` 
    
    :param xCoordinate: 
    :type xCoordinate: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_layout ("NX Layout")
    """
    YCoordinate: float = ...
    """
    Returns or sets  the y coordinate to calculate the new created drawing view's reference point
    
    <hr>
    
    Getter Method
    
    Signature ``YCoordinate`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``YCoordinate`` 
    
    :param yCoordinate: 
    :type yCoordinate: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: MoveToDrawingViewBuilder = ...  # unknown typename


