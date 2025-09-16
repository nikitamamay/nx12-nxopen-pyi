# module 'NXOpen.PartFamily'
#
# Automatically generated 2025-06-09T14:38:47.203434
#
"""Default documentation for NXOpen.PartFamily."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class MemberIdentifier(NXOpen.TransientObject):
    """
    This class represents the unique identifier for a part family member.  
    
    It essentially consitiutes the FAM attr object and value pair. This object is to be used in lieu
    of member name, whenever a member is needed to be 
    uniquely identified.
    
    Use :py:meth:`PartFamily.TemplateManager.CreateMemberIdentifier` to create a new member identifier.
    
    .. versionadded:: NX10.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage collector
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class InstanceDefinition(NXOpen.TransientObject):
    """
    This class repesents a part family table record (or instance definition on the template) and is 
    created/deleted by :py:class:`PartFamily.TemplateManager`.  
    
    Use :py:meth:`PartFamily.TemplateManager.AddInstanceDefinition` to create a new instance defintion.
    
    .. versionadded:: NX9.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage collector
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValueOfAttribute(self, partFamAttr: FamilyAttribute, value: str) -> None:
        """
        Set the value for passed atribute with the value
        
        Signature ``SetValueOfAttribute(partFamAttr, value)`` 
        
        :param partFamAttr: 
        :type partFamAttr: :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        :param value: 
        :type value: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetValueOfAttribute(self, partFamAttr: FamilyAttribute) -> str:
        """
        Get the value for passed atribute
        
        Signature ``GetValueOfAttribute(partFamAttr)`` 
        
        :param partFamAttr: 
        :type partFamAttr: :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    


class TemplateManager(NXOpen.TransientObject):
    """
    This class serves as the manager for all the part family related operations.  
    
    All operations that create, edit or delete part family objects are done through this class. 
    Use the method :py:meth:`Part.NewPartFamilyTemplateManager`
    to create new instance of this class.
    
    .. versionadded:: NX9.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage collector
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectableAttributes(self, attrType: FamilyAttributeAttrType) -> 'list[str]':
        """
        The list of attribute names of a given type in the owning part
        These can be used to create part family attributes
        
        Signature ``GetSelectableAttributes(attrType)`` 
        
        :param attrType: 
        :type attrType: :py:class:`NXOpen.PartFamily.FamilyAttributeAttrType` 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def DeletePartFamilyAttribute(self, partFamilyAttribute: FamilyAttribute) -> None:
        """
        Deletes a given part family attribute 
        
        Signature ``DeletePartFamilyAttribute(partFamilyAttribute)`` 
        
        :param partFamilyAttribute: 
        :type partFamilyAttribute: :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetChosenAttributes(self) -> 'list[FamilyAttribute]':
        """
        Returns the attributes on the template manager
        These might include the attributes which have not yet been committed onto the core object and have only been created by this instance of the manager.  
        
        "Use :py:meth:`Template.GetAttributes` to get the committed attributes"   
        
        Signature ``GetChosenAttributes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def AddToChosenAttributes(self, attrsToAdd: 'list[str]', attrsTypes: 'list[FamilyAttributeAttrType]', indexAddAt: int) -> None:
        """
        Adds new attributes to chosen attributes list of a part family 
        
        Signature ``AddToChosenAttributes(attrsToAdd, attrsTypes, indexAddAt)`` 
        
        :param attrsToAdd: 
        :type attrsToAdd: list of str 
        :param attrsTypes: 
        :type attrsTypes: list of :py:class:`NXOpen.PartFamily.FamilyAttributeAttrType` 
        :param indexAddAt: 
        :type indexAddAt: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def AddAssertedMassToChosenAttributes(self, attrToAdd: str, indexAddAt: int) -> None:
        """
        Adds new attribute of type asserted mass to chosen attributes list of a part family 
        
        Signature ``AddAssertedMassToChosenAttributes(attrToAdd, indexAddAt)`` 
        
        :param attrToAdd: 
        :type attrToAdd: str 
        :param indexAddAt: 
        :type indexAddAt: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES"), solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def MoveDownAttributes(self, moveDownAttrs: 'list[FamilyAttribute]', moveDownCount: int) -> int:
        """
        Move down the specified attributes of a part family by the moveDownCount.  
        
        If the attributes cannot be moved down by the specified count, this method will execute the 
        partial move and return the count that the attributes are actually moved down by.
        
        Signature ``MoveDownAttributes(moveDownAttrs, moveDownCount)`` 
        
        :param moveDownAttrs: 
        :type moveDownAttrs: list of :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        :param moveDownCount: 
        :type moveDownCount: int 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def MoveUpAttributes(self, moveUpAttrs: 'list[FamilyAttribute]', moveUpCount: int) -> int:
        """
        Move up the specified attributes of a part family by the moveUpCount.  
        
        If the attributes cannot be moved up by the specified count, this method will execute the 
        partial move and return the count that the attributes are actually moved up by.
        
        Signature ``MoveUpAttributes(moveUpAttrs, moveUpCount)`` 
        
        :param moveUpAttrs: 
        :type moveUpAttrs: list of :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        :param moveUpCount: 
        :type moveUpCount: int 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def CutAttributes(self, cutAttrs: 'list[FamilyAttribute]') -> None:
        """
        Cut selected attributes of a part family.  
        
        These will be pasted during paste operation.
        If previously cut attributes are present then they will be lost because the new ones
        will overwrite them.
        
        Signature ``CutAttributes(cutAttrs)`` 
        
        :param cutAttrs: 
        :type cutAttrs: list of :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def PasteAttributes(self, pasteAfter: FamilyAttribute) -> None:
        """
        Paste the cut attributes of a part family.  
        
        The pasteAfter attribute must be present in
        chosen attributes list for this operation to succeed.
        
        Signature ``PasteAttributes(pasteAfter)`` 
        
        :param pasteAfter: 
        :type pasteAfter: :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def CreatePartFamily(self) -> Template:
        """
        Creates a part family associated with the owning part  
        
        Signature ``CreatePartFamily()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PartFamily.Template` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def EditPartFamily(self) -> None:
        """
        Edits a part family associated with the manager/owning part 
        
        Signature ``EditPartFamily()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def DeletePartFamily(self) -> None:
        """
        Deletes a part family associated with the manager/owning part 
        
        Signature ``DeletePartFamily()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def EstablishFamilyInstance(self, memberName: str) -> str:
        """
        Creates a part family member if it doesn't exist on disk.  
        
        Signature ``EstablishFamilyInstance(memberName)`` 
        
        :param memberName: 
        :type memberName: str 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetInstanceDefinition(self, familyMemberDefnName: str) -> InstanceDefinition:
        """
        Get the family member definition already present in family 
        
        Signature ``GetInstanceDefinition(familyMemberDefnName)`` 
        
        :param familyMemberDefnName: 
        :type familyMemberDefnName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetInstanceDefinitionUsingMemberIdentifier(self, familyMemberIdentifier: MemberIdentifier) -> InstanceDefinition:
        """
        Obtains the family member definition already present in family
        A non zero return code implies familyMemberDefinition is NULL
        
        Signature ``GetInstanceDefinitionUsingMemberIdentifier(familyMemberIdentifier)`` 
        
        :param familyMemberIdentifier: 
        :type familyMemberIdentifier: :py:class:`NXOpen.PartFamily.MemberIdentifier` 
        :returns: 
        :rtype: :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def AddInstanceDefinition(self, familyMemberDefnName: str, previousFamilyMemberDefn: InstanceDefinition, otherNameEntry: str) -> InstanceDefinition:
        """
        Creates a new family member definition with the supplied name and places it just under previous family member definition.  
        
        If the part family is importable, then the otherNameEntry is a mandatory input.
        Depending on whether we are in managed mode or native, familyMemberDefn name may be os_part_name or 
        db_part_name, and otherNameEntry may be db_part_name or os_part_name.
        In case of non-importable part family otherName Entry may be empty.
        
        Signature ``AddInstanceDefinition(familyMemberDefnName, previousFamilyMemberDefn, otherNameEntry)`` 
        
        :param familyMemberDefnName: 
        :type familyMemberDefnName: str 
        :param previousFamilyMemberDefn: 
        :type previousFamilyMemberDefn: :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        :param otherNameEntry: 
        :type otherNameEntry: str 
        :returns: 
        :rtype: :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def AddInstanceDefinitionUsingMemberIdentifier(self, familyMemberIdentifier: MemberIdentifier, previousFamilyMemberDefn: InstanceDefinition, otherNameEntry: str) -> InstanceDefinition:
        """
        Creates a new family member definition with the supplied member identifier places it just under previous family member definition.  
        
        If the part family is importable, then the otherNameEntry is a mandatory input.
        Depending on whether we are in managed mode or native, otherNameEntry may be db_part_name or os_part_name.
        In case of non-importable part family otherNameEntry may be empty.
        
        Signature ``AddInstanceDefinitionUsingMemberIdentifier(familyMemberIdentifier, previousFamilyMemberDefn, otherNameEntry)`` 
        
        :param familyMemberIdentifier: 
        :type familyMemberIdentifier: :py:class:`NXOpen.PartFamily.MemberIdentifier` 
        :param previousFamilyMemberDefn: 
        :type previousFamilyMemberDefn: :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        :param otherNameEntry: 
        :type otherNameEntry: str 
        :returns: 
        :rtype: :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def DeleteInstanceDefinition(self, familyMemberDefinition: InstanceDefinition) -> None:
        """
        Delete the family member definition from template manager
        
        Signature ``DeleteInstanceDefinition(familyMemberDefinition)`` 
        
        :param familyMemberDefinition: 
        :type familyMemberDefinition: :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def ReorderInstanceDefinition(self, familyMemberDefinition: InstanceDefinition, previousFamilyMemberDefn: InstanceDefinition) -> None:
        """
        Reorder (relocate) familyMemberDefinition just after the previousFamilyMemberDefn
        
        Signature ``ReorderInstanceDefinition(familyMemberDefinition, previousFamilyMemberDefn)`` 
        
        :param familyMemberDefinition: 
        :type familyMemberDefinition: :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        :param previousFamilyMemberDefn: 
        :type previousFamilyMemberDefn: :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def SavePartFamily(self) -> None:
        """
        Save the changes in template manager to core part family
        
        Signature ``SavePartFamily()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetPartFamilyAttribute(self, attrType: FamilyAttributeAttrType, attrName: str) -> FamilyAttribute:
        """
        Get the part family attribute from part family template  
        
        Signature ``GetPartFamilyAttribute(attrType, attrName)`` 
        
        :param attrType: 
        :type attrType: :py:class:`NXOpen.PartFamily.FamilyAttributeAttrType` 
        :param attrName: 
        :type attrName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def SaveFamilyAndCreateMembers(self, instDefsToCreate: 'list[InstanceDefinition]') -> 'list[int]':
        """
        Save part family and create the family members supplied through input array.  
        
        It returns success
        and failure codes via errorCodes array.
        
        Signature ``SaveFamilyAndCreateMembers(instDefsToCreate)`` 
        
        :param instDefsToCreate: 
        :type instDefsToCreate: list of :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        :returns: 
        :rtype: list of int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def SaveFamilyAndUpdateMembers(self, forceUpdate: bool, instDefsToUpdate: 'list[InstanceDefinition]') -> 'list[int]':
        """
        Save part family and update the family members supplied through input array.  
        
        It returns success
        and failure codes via errorCodes array. 
        If errorCodes contains error about locked attributes, use :py:meth:`PartFamily.TemplateManager.GetInfoMessages` 
        to query the names of those locked attributes.
        
        Signature ``SaveFamilyAndUpdateMembers(forceUpdate, instDefsToUpdate)`` 
        
        :param forceUpdate: 
        :type forceUpdate: bool 
        :param instDefsToUpdate: 
        :type instDefsToUpdate: list of :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        :returns: 
        :rtype: list of int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def SaveFamilyAndFixOrphanMembers(self, forceUpdate: bool, instDefsToFix: 'list[InstanceDefinition]') -> 'list[int]':
        """
        Save part family and fix the orphan family members supplied through input array.  
        
        The orphan member that is fixed would also be
        updated to the latest configuration. It returns success and failure codes via errorCodes array. If errorCodes contains error about locked attributes,
        use :py:meth:`PartFamily.TemplateManager.GetInfoMessages` to query the names of those locked attributes.
        
        Signature ``SaveFamilyAndFixOrphanMembers(forceUpdate, instDefsToFix)`` 
        
        :param forceUpdate: 
        :type forceUpdate: bool 
        :param instDefsToFix: 
        :type instDefsToFix: list of :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        :returns: 
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def SaveFamilyAndApplyValues(self, familyMemberDefinition: InstanceDefinition) -> int:
        """
        Save part family and apply the values of chosen family member definition to the template part,
        It returns failure codes through errorCode.  
        
        Signature ``SaveFamilyAndApplyValues(familyMemberDefinition)`` 
        
        :param familyMemberDefinition: 
        :type familyMemberDefinition: :py:class:`NXOpen.PartFamily.InstanceDefinition` 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetPartFamilyTemplate(self) -> Template:
        """
        Get the part family template 
        This method may return NULL if there is no template associated with the templatemanager
        
        Signature ``GetPartFamilyTemplate()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PartFamily.Template` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def AddOptionalCreationNonKeyAttrsToChosenAttrs(self, pasteAfter: FamilyAttribute) -> 'list[FamilyAttribute]':
        """
        Add all optional creation non key attributes to chosen list at the end or after a selected attribute from chosen attribute list.  
        
        To add all optional creation attributes at the end, pass pasteAfter as NULL.
        If an optional attribute is already present in chosen attribute list, it does not add it again.
        Outputs an array of the optional attributes that were actually added to chosen list
        
        Signature ``AddOptionalCreationNonKeyAttrsToChosenAttrs(pasteAfter)`` 
        
        :param pasteAfter: 
        :type pasteAfter: :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def RefreshDefaultAttrs(self) -> None:
        """
        Repopulates required attributes in chosen list so that it updates as per the teamcenter customizations, if it has changed since last saved template.  
        
        Signature ``RefreshDefaultAttrs()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetAllKeyAttrs(self) -> 'list[FamilyAttribute]':
        """
        Obtains all key attributes (required and optional) required to construct the MFK ID.  
        
        These would be used to create the unique member identifier.
        
        Signature ``GetAllKeyAttrs()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def CreateMemberIdentifier(self, keyAttrs: 'list[FamilyAttribute]', attrValues: 'list[str]', itemType: str) -> MemberIdentifier:
        """
        Creates a member identifier for a part family member from the key attributes
        and value pair.  
        
        In native mode the itemType is NULL
        In managed mode, the value of itemType could be NULL in which case Template's item type will be used while creating the MemberIdentifier
        
        Signature ``CreateMemberIdentifier(keyAttrs, attrValues, itemType)`` 
        
        :param keyAttrs: 
        :type keyAttrs: list of :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        :param attrValues: 
        :type attrValues: list of str 
        :param itemType: 
        :type itemType: str 
        :returns: 
        :rtype: :py:class:`NXOpen.PartFamily.MemberIdentifier` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetInfoMessages(self) -> 'list[str]':
        """
        Obtains the list of messages that may have been encountered in any workflow.  
        
        This is a generic routine to get all information (Error/Warning/Info) that are deemed useful to user.
        Contains error messages encountered during save like material issues, interpart expression issues, invalid member names.
        In addition, if there were locked attributes (i.e. attributes whose value cannot be updated), 
        this also would contain the names of such attributes.
        
        Signature ``GetInfoMessages()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    Importable: bool = ...
    """
    Returns or sets  the importable flag value 
    
    <hr>
    
    Getter Method
    
    Signature ``Importable`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``Importable`` 
    
    :param isImportable: 
    :type isImportable: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    SaveDirectory: str = ...
    """
    Returns or sets  the save directory path value 
    
    <hr>
    
    Getter Method
    
    Signature ``SaveDirectory`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    
    <hr>
    
    Setter Method
    
    Signature ``SaveDirectory`` 
    
    :param saveDirectory: 
    :type saveDirectory: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """


class Instance(NXOpen.TaggedObject):
    """
    Represents an instance of a part family member
    
    Use :py:meth:`NXOpen.Part.GetFamilyInstance` to get the instance of this class.
    
    .. versionadded:: NX9.0.0
    """
    
    def IsOutOfDate(self) -> bool:
        """
        Returns whether this instance/member is out of date relative to the definition on the template.  
        
        Signature ``IsOutOfDate()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    Family: Template = ...
    """
    Returns  the :py:class:`NXOpen.PartFamily.Template` of instance.  
    
    <hr>
    
    Getter Method
    
    Signature ``Family`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PartFamily.Template` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Version: int = ...
    """
    Returns  the version of instance.  
    
    <hr>
    
    Getter Method
    
    Signature ``Version`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Null: Instance = ...  # unknown typename


class Template(NXOpen.NXObject):
    """
    This class represents a part family template       
    
    Use :py:meth:`PartFamily.TemplateManager.CreatePartFamily` to get the instance of this class.
    
    .. versionadded:: NX9.0.0
    """
    
    def GetAttributes(self) -> 'list[FamilyAttribute]':
        """
        Returns the attributes of the part family template.  
        
        These are the attributes committed onto the core object
        
        Signature ``GetAttributes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetValidAttributeValues(self, attr: FamilyAttribute) -> 'list[str]':
        """
        Returns the valid attribute values for a given part family attribute.  
        
        These will be useful for selecting a valid match_criteria 
        
        Signature ``GetValidAttributeValues(attr)`` 
        
        :param attr: 
        :type attr: :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetMembers(self) -> 'list[str]':
        """
        Obtains the members in part family.  
        
        Signature ``GetMembers()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def IsValidMemberName(self, memberName: str) -> bool:
        """
        Returns true if a member name is valid, false otherwise 
        
        Signature ``IsValidMemberName(memberName)`` 
        
        :param memberName: 
        :type memberName: str 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    TemplateName: str = ...
    """
    Returns  the name of the part family template 
    
    <hr>
    
    Getter Method
    
    Signature ``TemplateName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Version: int = ...
    """
    Returns  the version of the part family template 
    
    <hr>
    
    Getter Method
    
    Signature ``Version`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Null: Template = ...  # unknown typename


class FamilyAttributeAttrTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FamilyAttributeAttrType():
    """
    The part family attribute types.
    These should always be in synch with the UF_fam_attr_types 
    
    .. versionadded:: NX9.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Text", "text attribute"
       "Numeric", "numeric attribute"
       "Integer", "integer attribute"
       "Double", "double attribute"
       "String", "string attribute"
       "Part", "part attribute"
       "Name", "name attribute"
       "Instance", "instance attribute"
       "Expression", "expression attribute"
       "Mirror", "mirror attribute"
       "Density", "density attribute"
       "Feature", "feature attribute"
       "Mass", "asserted mass attribute"
       "Material", "material attribute"
       "Undefined", "undefined attribute type"
    """
    Text = 1  # FamilyAttributeAttrTypeMemberType
    Numeric = 2  # FamilyAttributeAttrTypeMemberType
    Integer = 3  # FamilyAttributeAttrTypeMemberType
    Double = 4  # FamilyAttributeAttrTypeMemberType
    String = 5  # FamilyAttributeAttrTypeMemberType
    Part = 6  # FamilyAttributeAttrTypeMemberType
    Name = 7  # FamilyAttributeAttrTypeMemberType
    Instance = 8  # FamilyAttributeAttrTypeMemberType
    Expression = 9  # FamilyAttributeAttrTypeMemberType
    Mirror = 10  # FamilyAttributeAttrTypeMemberType
    Density = 11  # FamilyAttributeAttrTypeMemberType
    Feature = 12  # FamilyAttributeAttrTypeMemberType
    Mass = 13  # FamilyAttributeAttrTypeMemberType
    Material = 14  # FamilyAttributeAttrTypeMemberType
    Undefined = 15  # FamilyAttributeAttrTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FamilyAttribute(NXOpen.NXObject):
    """
    This class represents a part family attribute       
    
    Use :py:meth:`PartFamily.TemplateManager.GetPartFamilyAttribute` to get an instance of this class.
    This method will not create a new part family attribute. It will only return attribute that is already created.
    To create a new attribute, use :py:meth:`PartFamily.TemplateManager.AddToChosenAttributes`, which
    will create an attribute and add to chosen attributes list on template manager. It is not allowed to create
    a standalone attribute that is not added to chosen attributes list.
    
    .. versionadded:: NX9.0.0
    """
    
    class AttrType():
        """
        The part family attribute types.
        These should always be in synch with the UF_fam_attr_types 
        
        .. versionadded:: NX9.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Text", "text attribute"
           "Numeric", "numeric attribute"
           "Integer", "integer attribute"
           "Double", "double attribute"
           "String", "string attribute"
           "Part", "part attribute"
           "Name", "name attribute"
           "Instance", "instance attribute"
           "Expression", "expression attribute"
           "Mirror", "mirror attribute"
           "Density", "density attribute"
           "Feature", "feature attribute"
           "Mass", "asserted mass attribute"
           "Material", "material attribute"
           "Undefined", "undefined attribute type"
        """
        Text = 1  # FamilyAttributeAttrTypeMemberType
        Numeric = 2  # FamilyAttributeAttrTypeMemberType
        Integer = 3  # FamilyAttributeAttrTypeMemberType
        Double = 4  # FamilyAttributeAttrTypeMemberType
        String = 5  # FamilyAttributeAttrTypeMemberType
        Part = 6  # FamilyAttributeAttrTypeMemberType
        Name = 7  # FamilyAttributeAttrTypeMemberType
        Instance = 8  # FamilyAttributeAttrTypeMemberType
        Expression = 9  # FamilyAttributeAttrTypeMemberType
        Mirror = 10  # FamilyAttributeAttrTypeMemberType
        Density = 11  # FamilyAttributeAttrTypeMemberType
        Feature = 12  # FamilyAttributeAttrTypeMemberType
        Mass = 13  # FamilyAttributeAttrTypeMemberType
        Material = 14  # FamilyAttributeAttrTypeMemberType
        Undefined = 15  # FamilyAttributeAttrTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    IsOptional: bool = ...
    """
    Returns  a value indicating whether the attribute is an optional attribute.  
    
    This could be an optional creation non key attribute or an optional key attribute
    
    <hr>
    
    Getter Method
    
    Signature ``IsOptional`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    IsRequired: bool = ...
    """
    Returns  a value indicating whether the attribute is a required attribute.  
    
    This could be a required creation non key attribute or a required key attribute
    
    <hr>
    
    Getter Method
    
    Signature ``IsRequired`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Name: str = ...
    """
    Returns  the name of the given attribute 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Type: FamilyAttributeAttrType = ...
    """
    Returns  the type of the given attribute 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PartFamily.FamilyAttributeAttrType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Value: str = ...
    """
    Returns  the value of the given attribute 
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Version: int = ...
    """
    Returns  the version of the given attribute 
    
    <hr>
    
    Getter Method
    
    Signature ``Version`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Null: FamilyAttribute = ...  # unknown typename


class InstanceSelectionCriteria(NXOpen.TaggedObject):
    """
    Represents the selection criteria of a part family instance
    
    Use :py:meth:`NXOpen.Assemblies.Component.CreateEmptyPartFamilyInstanceSelectionCriteria` to get an instance of this class.
    
    .. versionadded:: NX9.0.0
    """
    
    def GetCriteriaStrings(self) -> 'list[str]':
        """
        Obtains the criteria strings associated with this selection criteria.  
        
        Output "criteriaStringArray" would be an array of TEXT_pc_t with each element of the form for e.g. "p7 > 100",
        where "p7" is the attribute, "100" the value and ">" the expression connecting both 
        
        Signature ``GetCriteriaStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    @typing.overload
    def SetPartFamilyInstanceSelectionCriteria(self, attributes: 'list[FamilyAttribute]', criteriaStringArray: 'list[str]') -> None:
        """
        Sets criteria on :py:class:`NXOpen.PartFamily.InstanceSelectionCriteria`.
        This criteria can be used while adding a part family member to assembly. 
        Number of elements in "attributes" and "criteriaStringArray" should always match the "attributeCount".
        "criteriaStringArray" has to be an array of TEXT_pc_t with each element of the form for e.g. "p7 >= 100",
        where "p7" is the attribute, "100" the value and ">=" the expression connecting both 
        
        Signature ``SetPartFamilyInstanceSelectionCriteria(attributes, criteriaStringArray)`` 
        
        :param attributes: 
        :type attributes: list of :py:class:`NXOpen.PartFamily.FamilyAttribute` 
        :param criteriaStringArray: 
        :type criteriaStringArray: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    @typing.overload
    def SetPartFamilyInstanceSelectionCriteria(self, memberName: str) -> None:
        """
        Sets criteria on :py:class:`NXOpen.PartFamily.InstanceSelectionCriteria`.
        This routine can be used when user wants to add a part family member to assembly directly using 
        the "memberName" instead of using attribute criteria. This "memberName" will be ignored in case 
        the InstenaceSelectionCriteria already has any valid attribute criteria or if the user adds a valid 
        attribute criteria later on.
        User could obtain valid "memberName" using :py:meth:`NXOpen.PartFamily.Template.GetMembers`.
        
        Signature ``SetPartFamilyInstanceSelectionCriteria(memberName)`` 
        
        :param memberName: 
        :type memberName: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def IsValidPartFamilyInstanceSelectionCriteria(self) -> bool:
        """
        Returns true if the selection criteria evaluates to a valid part family instance, false otherwise.  
        
        Signature ``IsValidPartFamilyInstanceSelectionCriteria()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    Family: Template = ...
    """
    Returns  the :py:class:`NXOpen.PartFamily.Template` that corresponds to this criteria object 
    
    <hr>
    
    Getter Method
    
    Signature ``Family`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PartFamily.Template` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Instance: Instance = ...
    """
    Returns  the :py:class:`NXOpen.PartFamily.Instance` of criteria.  
    
    <hr>
    
    Getter Method
    
    Signature ``Instance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PartFamily.Instance` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Null: InstanceSelectionCriteria = ...  # unknown typename


