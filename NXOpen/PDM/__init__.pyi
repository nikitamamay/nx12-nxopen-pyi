# module 'NXOpen.PDM'
#
# Automatically generated 2025-06-09T14:38:47.203434
#
"""Default documentation for NXOpen.PDM."""

import typing

import NXOpen
import NXOpen.Assemblies
import NXOpen.GeometricUtilities



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class PartCreationObject(NXOpen.NXObject):
    """
    This class is a proxy for a to-be-created part prior to the part being created.  
    
    Used only in NX Manager mode. 
    Use :py:meth:`PDM.PartBuilder.CreatePartCreationObject` to get the instance of this class.
    
    .. versionadded:: NX8.0.0
    """
    
    def CreateAttributePropertiesBuilder(self) -> PartCreationObjectAttributePropertiesBuilder:
        """
        Create the PartCreationObjectAttributePropertiesBuilder  
        
        Signature ``CreateAttributePropertiesBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartCreationObjectAttributePropertiesBuilder` 
        
        .. versionadded:: NX8.0.0
        
        .. deprecated::  NX8.5.0
           Use :py:meth:`AttributeManager.CreateAttributePropertiesBuilder` instead.
        
        License requirements: None.
        """
        ...
    
    Null: PartCreationObject = ...  # unknown typename


class PdmSoaqueryNxmgrfielddatatypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PdmSoaqueryNxmgrfielddatatype():
    """
    NX Manager search field data type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Char", "Char type"
       "Date", "Date"
       "Double", "Double"
       "Float", "Float"
       "Int", "Integer"
       "Bool", "Boolean"
       "Short", "Short"
       "String", "String"
       "Reference", "Reference"
       "UntypedReference", "Untyped reference"
       "ExternalReference", "External reference"
    """
    Char = 2001  # PdmSoaqueryNxmgrfielddatatypeMemberType
    Date = 2002  # PdmSoaqueryNxmgrfielddatatypeMemberType
    Double = 2003  # PdmSoaqueryNxmgrfielddatatypeMemberType
    Float = 2004  # PdmSoaqueryNxmgrfielddatatypeMemberType
    Int = 2005  # PdmSoaqueryNxmgrfielddatatypeMemberType
    Bool = 2006  # PdmSoaqueryNxmgrfielddatatypeMemberType
    Short = 2007  # PdmSoaqueryNxmgrfielddatatypeMemberType
    String = 2008  # PdmSoaqueryNxmgrfielddatatypeMemberType
    Reference = 2009  # PdmSoaqueryNxmgrfielddatatypeMemberType
    UntypedReference = 2010  # PdmSoaqueryNxmgrfielddatatypeMemberType
    ExternalReference = 2011  # PdmSoaqueryNxmgrfielddatatypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartManager():
    """
    This class contains methods to create and manage parts in NX Manager mode.  
    
    Use :py:meth:`NXOpen.PartCollection.PDMPartManager` to get the instance of this class.
    
    .. versionadded:: NX4.0.0
    """
    
    def NewPartFromTemplateBuilder(self) -> PartFromTemplateBuilder:
        """
        Create an instance of a part builder that creates a new part from a template part.  
        
        This is analagous to a File New operation in NX Manager mode.
        
        This method will throw an error if the session is not running in
        NX Manager mode.
        
        :py:class:`NXOpen.PDM.PartFromTemplateBuilder` is a singleton
        meaning only one instance of it can exist at one time. Calling this method
        will destroy the builder if one already exists and return a new instance.
        
        Signature ``NewPartFromTemplateBuilder()`` 
        
        :returns:  the part builder  
        :rtype: :py:class:`NXOpen.PDM.PartFromTemplateBuilder` 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:class:`NXOpen.PDM.PartOperationCreateBuilder` instead.
        
        License requirements: None.
        """
        ...
    
    
    def NewPartFromPartBuilder(self) -> PartFromPartBuilder:
        """
        Create an instance of a part builder that creates a new part from an existing part.  
        
        This is analagous to a File SaveAs operation in NX Manager mode.
        
        This method will throw an error if the session is not running in
        NX Manager mode.
        
        :py:class:`NXOpen.PDM.PartFromTemplateBuilder` is a singleton
        meaning only one instance of it can exist at one time. Calling this method
        will destroy the builder if one already exists and return a new instance.
        
        Deprecated in NX10 for "Save As of master parts" operation. 
        This should only be used in case of Save As Non Master parts and Save As New Item Type Operations.
        For Save As of master parts, use :py:class:`NXOpen.PDM.PartOperationCopyBuilder` instead.
        
        Signature ``NewPartFromPartBuilder()`` 
        
        :returns:  the part builder  
        :rtype: :py:class:`NXOpen.PDM.PartFromPartBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewPendingComponentsManager(self, part: NXOpen.BasePart) -> PendingComponentsManager:
        """
        Creates a pending component manager for a given part.  
        
        Pending components
        are ones that have been added from Teamcenter, but are not yet present in NX.
        
        Signature ``NewPendingComponentsManager(part)`` 
        
        :param part:  the part  
        :type part: :py:class:`NXOpen.BasePart` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PendingComponentsManager` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCaeCloneManager(self, part: NXOpen.BasePart) -> CaeCloneManager:
        """
        Create or get a Clone Manager that can execute a CAE Clone process for a Simulation File or a FeModel File.  
        
        Creates a Clone Manager for a Simulation tag or a FeModel tag, if it does not already exist.
        Creates part from part builder :py:class:`NXOpen.PDM.PartFromPartBuilder` objects for cloning a Simulation File or a FeModel File.
        If called for a FeModel tag, the function will create Part Builders for FeModel Part , associated Idealized Part and CAD master part.
        If called for a Simulation tag, the function will create Part Builders for Simulation Part, associated FeModel Part, Idealized Part and CAD master part.
        
        Signature ``GetCaeCloneManager(part)`` 
        
        :param part:  the part  
        :type part: :py:class:`NXOpen.BasePart` 
        :returns:  the clone manager  
        :rtype: :py:class:`NXOpen.PDM.CaeCloneManager` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    


class CAEFileContainer(NXOpen.TransientObject):
    """
    This class is a File Container class for uploading JT files created by NX CAE Post Processing to Teamcenter. 
    Users can add the JT file names and their corresponding dataset names to this container class.
    Once all the JT file names are added, this class can be used to upload the JT files to Teamcenter.
    The class can be used to upload only to a a single part at a time.
    
    Use :py:class:`NXOpen.PDM.PdmSession` to get the instance of this class.
    
    .. versionadded:: NX8.5.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOwningPart(self) -> str:
        """
        Get the part tag of the owning part of the class :py:class:`NXOpen.PDM.CAEFileContainer`.  
        
        Signature ``GetOwningPart()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def SetOwningPart(self, partspec: str) -> None:
        """
        Sets the part tag of the owning part of the class :py:class:`NXOpen.PDM.CAEFileContainer`.  
        
        Signature ``SetOwningPart(partspec)`` 
        
        :param partspec: 
        :type partspec: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def AddFile(self, datasetname: str, filename: str) -> None:
        """
        Add a file to the list of files in the file container class :py:class:`NXOpen.PDM.CAEFileContainer`.  
        
        Signature ``AddFile(datasetname, filename)`` 
        
        :param datasetname: 
        :type datasetname: str 
        :param filename: 
        :type filename: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def DeleteFile(self, datasetname: str, filename: str) -> None:
        """
        Delete a file from the list of files in the file container class :py:class:`NXOpen.PDM.CAEFileContainer`.  
        
        Signature ``DeleteFile(datasetname, filename)`` 
        
        :param datasetname: 
        :type datasetname: str 
        :param filename: 
        :type filename: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def DoUpload(self) -> None:
        """
        Upload CAE files to Teamcenter, independent of a standard file->save.  
        
        Upload all the files in the file container class :py:class:`NXOpen.PDM.CAEFileContainer` using this function.
        The JT files should be present in the temporary directory of the system prior to calling this function.
        
        Signature ``DoUpload()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    


class IAttributeGroupOwner():
    """
    An interface class for objects that own attribute groups.  
    
    .. versionadded:: NX9.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ModelElement(NXOpen.NXObject, IAttributeGroupOwner):
    """
    Represents a base class that provides common methods for various model elements in a :py:class:`NXOpen.CollaborativeDesign`.  
    
    Instance of this class can not be created
    
    .. versionadded:: NX11.0.0
    """
    
    def GetMemberPartitions(self) -> 'list[NXOpen.Assemblies.Partition]':
        """
        Get all the partitions of this model element revision.  
        
        Signature ``GetMemberPartitions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Create(self, attributeGroupDescription: AttributeGroupDescription) -> AttributeGroup:
        """
        Creates an attribute group for a :py:class:`NXOpen.PDM.IAttributeGroupOwner`, based on an attribute
        group type.  
        
        An attribute group type is represented by an :py:class:`NXOpen.PDM.AttributeGroupDescription`.
        
        Signature ``Create(attributeGroupDescription)`` 
        
        :param attributeGroupDescription: 
        :type attributeGroupDescription: :py:class:`NXOpen.PDM.AttributeGroupDescription` 
        :returns:  The new attribute group.  
        :rtype: :py:class:`NXOpen.PDM.AttributeGroup` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateAttributeGroupReviseBuilder(self, attributeGroups: 'list[AttributeGroup]') -> AttributeGroupReviseBuilder:
        """
        Creates a :py:class:`NXOpen.PDM.AttributeGroupReviseBuilder` object.  The builder creates a
        revision for each attribute group in the input list of existing attribute groups.  
        
        Signature ``CreateAttributeGroupReviseBuilder(attributeGroups)`` 
        
        :param attributeGroups: 
        :type attributeGroups: list of :py:class:`NXOpen.PDM.AttributeGroup` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.AttributeGroupReviseBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateAttributeGroupReviseBuilder(self, attributeGroups: 'list[AttributeGroup]', keepOriginal: bool, saveAsActionType: AttributeGroupReviseBuilderSaveAsActionType) -> AttributeGroupReviseBuilder:
        """
        The builder will do a revise or save-as operation for each attribute group in the input list of existing attribute groups 
        depending on input operation type.  
        
        Signature ``CreateAttributeGroupReviseBuilder(attributeGroups, keepOriginal, saveAsActionType)`` 
        
        :param attributeGroups: 
        :type attributeGroups: list of :py:class:`NXOpen.PDM.AttributeGroup` 
        :param keepOriginal: 
        :type keepOriginal: bool 
        :param saveAsActionType: 
        :type saveAsActionType: :py:class:`NXOpen.PDM.AttributeGroupReviseBuilderSaveAsActionType` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.AttributeGroupReviseBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAttributeGroups(self) -> 'list[AttributeGroup]':
        """
        Returns the :py:class:`NXOpen.PDM.AttributeGroup` objects owned by this object.  
        
        Signature ``GetAttributeGroups()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.AttributeGroup` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAttributeGroupDescriptions(self) -> 'list[AttributeGroupDescription]':
        """
        Returns the :py:class:`NXOpen.PDM.AttributeGroupDescription` objects representing the attribute
        group types supported by this object.  
        
        Signature ``GetAttributeGroupDescriptions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.AttributeGroupDescription` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    OwningCollaborativeDesign: NXOpen.CollaborativeDesign = ...
    """
    Returns  the owning :py:class:`NXOpen.CollaborativeDesign`.  
    
    <hr>
    
    Getter Method
    
    Signature ``OwningCollaborativeDesign`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CollaborativeDesign` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: ModelElement = ...  # unknown typename


class ConditionalElementRevision(ModelElement):
    """
    Represents a base class that provides common methods for various conditional model elements in a :py:class:`NXOpen.CollaborativeDesign`.  
    
    Instance of this class can not be created
    
    .. versionadded:: NX11.0.0
    """
    EffectivityFormula: str = ...
    """
    Returns  the formula string that represents the effectivity of this object in database.  
    
    <hr>
    
    Getter Method
    
    Signature ``EffectivityFormula`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: ConditionalElementRevision = ...  # unknown typename


class LogicalElementRevision(ConditionalElementRevision):
    """
    Represents a base class that provides common methods for various model elements in a :py:class:`NXOpen.CollaborativeDesign`.  
    
    Instance of this can not directly created.
    
    .. versionadded:: NX11.0.0
    """
    Null: LogicalElementRevision = ...  # unknown typename


class PortArtifact(NXOpen.NXObject):
    """
    Represents a base class that provides common methods for port artifact in a :py:class:`NXOpen.PDM.LogicalElementRevision`.  
    
    .. versionadded:: NX11.0.0
    """
    Null: PortArtifact = ...  # unknown typename


class PartOperationBuilderOperationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationBuilderOperationType():
    """
    Represents an operation type that can be performed on a part   
    
    .. versionadded:: NX9.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SaveAs", "Save As Part"
       "Revise", "Revise Part"
       "Create", "Create Part"
       "Import", "Import Part"
    """
    SaveAs = 0  # PartOperationBuilderOperationTypeMemberType
    Revise = 1  # PartOperationBuilderOperationTypeMemberType
    Create = 2  # PartOperationBuilderOperationTypeMemberType
    Import = 3  # PartOperationBuilderOperationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationBuilderNonMasterSaveAsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationBuilderNonMasterSaveAs():
    """
    This enum is used to specify which non-master parts 
    should be saved during the save as operation.   
    
    .. deprecated::  NX10.0.0
       Use :py:class:`NXOpen.PDM.PartOperationCopyBuilderCopyNonMasterParts` instead
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", "save all during save as"
       "NotSet", "save none during save as"
    """
    All = 0  # PartOperationBuilderNonMasterSaveAsMemberType
    NotSet = 1  # PartOperationBuilderNonMasterSaveAsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationBuilderDependentFileSaveAsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationBuilderDependentFileSaveAs():
    """
    This enum is used to specify which dependent files
    should be saved during the save as operation.   
    
    .. deprecated::  NX10.0.0
       Use :py:class:`NXOpen.PDM.PartOperationCopyBuilderCopyDependentFiles` instead
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", "save all during save as"
       "NotSet", "save none during save as"
    """
    All = 0  # PartOperationBuilderDependentFileSaveAsMemberType
    NotSet = 1  # PartOperationBuilderDependentFileSaveAsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationBuilder(NXOpen.Builder, NXOpen.IAttributeSourceObjectBuilder):
    """
    Represents a builder class that performs various design element operations.  
    
    The operation can be one of :py:class:`NXOpen.PDM.PartOperationBuilderOperationType` 
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreateOperationBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    class OperationType():
        """
        Represents an operation type that can be performed on a part   
        
        .. versionadded:: NX9.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SaveAs", "Save As Part"
           "Revise", "Revise Part"
           "Create", "Create Part"
           "Import", "Import Part"
        """
        SaveAs = 0  # PartOperationBuilderOperationTypeMemberType
        Revise = 1  # PartOperationBuilderOperationTypeMemberType
        Create = 2  # PartOperationBuilderOperationTypeMemberType
        Import = 3  # PartOperationBuilderOperationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class NonMasterSaveAs():
        """
        This enum is used to specify which non-master parts 
        should be saved during the save as operation.   
        
        .. deprecated::  NX10.0.0
           Use :py:class:`NXOpen.PDM.PartOperationCopyBuilderCopyNonMasterParts` instead
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", "save all during save as"
           "NotSet", "save none during save as"
        """
        All = 0  # PartOperationBuilderNonMasterSaveAsMemberType
        NotSet = 1  # PartOperationBuilderNonMasterSaveAsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DependentFileSaveAs():
        """
        This enum is used to specify which dependent files
        should be saved during the save as operation.   
        
        .. deprecated::  NX10.0.0
           Use :py:class:`NXOpen.PDM.PartOperationCopyBuilderCopyDependentFiles` instead
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", "save all during save as"
           "NotSet", "save none during save as"
        """
        All = 0  # PartOperationBuilderDependentFileSaveAsMemberType
        NotSet = 1  # PartOperationBuilderDependentFileSaveAsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreateLogicalObjects(self) -> 'list[LogicalObject]':
        """
        Creates the pre-creation objects for the parts 
        
        Signature ``CreateLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDialogOperation(self) -> PartOperationBuilderOperationType:
        """
        Returns the dialog operation Applicable only for operation types 
        :py:class:`PartOperationBuilderOperationType.SaveAs <PartOperationBuilderOperationType>` and 
        :py:class:`PartOperationBuilderOperationType.Revise <PartOperationBuilderOperationType>` 
        
        Signature ``GetDialogOperation()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationBuilderOperationType` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDialogOperation(self, dialogOperation: PartOperationBuilderOperationType) -> None:
        """
        Sets the dialog operation.  
        
        Applicable only for operation types 
        :py:class:`PartOperationBuilderOperationType.SaveAs <PartOperationBuilderOperationType>` and 
        :py:class:`PartOperationBuilderOperationType.Revise <PartOperationBuilderOperationType>`
        
        Signature ``SetDialogOperation(dialogOperation)`` 
        
        :param dialogOperation: 
        :type dialogOperation: :py:class:`NXOpen.PDM.PartOperationBuilderOperationType` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
        Returns part operation failures  
        
        Signature ``GetOperationFailures()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX12.0.0
           Use :py:meth:`NXOpen.PDM.PartOperationBuilder.GetErrorMessageHandler` instead
        
        License requirements: None.
        """
        ...
    
    
    def GetAlternateIDManager(self, logicalObject: LogicalObject) -> AlternateIdManager:
        """
        Create an instance of a :py:class:`NXOpen.PDM.AlternateIdManager`
        class that will be used to create alternate ID information while creating the new part.  
        
        CreateSpec call should happen before calling this method. 
        
        Signature ``GetAlternateIDManager(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :returns:  the new :py:class:`NXOpen.PDM.AlternateIdManager` instance  
        :rtype: :py:class:`NXOpen.PDM.AlternateIdManager` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateSpecificationsForLogicalObjects(self, logicalObjects: 'list[LogicalObject]') -> None:
        """
        Create new specifications for Logical Objects 
        
        Signature ``CreateSpecificationsForLogicalObjects(logicalObjects)`` 
        
        :param logicalObjects: 
        :type logicalObjects: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ValidateLogicalObjectsToCommit(self) -> None:
        """
        Validates :py:class:`NXOpen.PDM.LogicalObject` objects with this builder and udpates the operation failuers.  
        
        :py:meth:`NXOpen.PDM.PartOperationBuilder.GetOperationFailures` can be called to get the errors occurred
        during this operation. 
        
        Signature ``ValidateLogicalObjectsToCommit()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedParts(self, selectedParts: 'list[NXOpen.BasePart]') -> 'list[NXOpen.BasePart]':
        """
        Sets the selected parts.  
        
        Applicable only for operation types
        :py:class:`PartOperationBuilderOperationType.SaveAs <PartOperationBuilderOperationType>` and 
        :py:class:`PartOperationBuilderOperationType.Revise <PartOperationBuilderOperationType>`
        Also returns an array of parts failed to added, these are not removed from the input array though.
        :py:meth:`NXOpen.PDM.PartOperationBuilder.GetOperationFailures` can be called to get the errors occurred
        during this operation.
        
        Signature ``SetSelectedParts(selectedParts)`` 
        
        :param selectedParts: 
        :type selectedParts: list of :py:class:`NXOpen.BasePart` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.SetSelectedPartsToCopy` instead
        
        License requirements: None.
        """
        ...
    
    
    def AddRelatedPartToOperate(self, basePart: NXOpen.BasePart, relatedParts: 'list[NXOpen.BasePart]', relatedPartsReasons: 'list[str]', operation: PartOperationBuilderOperationType) -> None:
        """
        Add related part to the part undergoing an operation.  
        
        Example: if user selects a part
        for Save As which has Linked Part Modules that should also undergo Save As, they should
        be added as related parts.
        Applicable only for operation types 
        :py:class:`PartOperationBuilderOperationType.SaveAs <PartOperationBuilderOperationType>` and 
        :py:class:`PartOperationBuilderOperationType.Revise <PartOperationBuilderOperationType>`
        
        Signature ``AddRelatedPartToOperate(basePart, relatedParts, relatedPartsReasons, operation)`` 
        
        :param basePart: 
        :type basePart: :py:class:`NXOpen.BasePart` 
        :param relatedParts: 
        :type relatedParts: list of :py:class:`NXOpen.BasePart` 
        :param relatedPartsReasons: 
        :type relatedPartsReasons: list of str 
        :param operation: 
        :type operation: :py:class:`NXOpen.PDM.PartOperationBuilderOperationType` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.AddRelatedPartsToCopy` instead
        
        License requirements: None.
        """
        ...
    
    
    def CreateNonMasterListForLogicalObject(self, logicalObject: LogicalObject) -> None:
        """
        Create NonMaster list for the selected logical Object 
        
        Signature ``CreateNonMasterListForLogicalObject(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.CreateNonMasterListForCopyLogicalObject` instead
        
        License requirements: None.
        """
        ...
    
    
    def SetNonMasterSaveAsOption(self, logicalObject: LogicalObject, saveOption: PartOperationBuilderNonMasterSaveAs) -> None:
        """
        Set the nonmasters saveAs option for given logical object
        
        Signature ``SetNonMasterSaveAsOption(logicalObject, saveOption)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param saveOption: 
        :type saveOption: :py:class:`NXOpen.PDM.PartOperationBuilderNonMasterSaveAs` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.SetCopyNonMasterPartsOption` instead
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedNonMasterToSaveAs(self, logicalObject: LogicalObject, partName: str) -> None:
        """
        Sets whether or not the non-master part specified will actually get
        saved during the save as operation.  
        
        True means that it will be
        saved. False means that it will not be saved.  
        
        Signature ``SetSelectedNonMasterToSaveAs(logicalObject, partName)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param partName:  the non-master part whose save option is being set here  
        :type partName: str 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.SetSelectedNonMasterToCopy` instead
        
        License requirements: None.
        """
        ...
    
    
    def GetNonMasterList(self, logicalObject: LogicalObject) -> 'list[str]':
        """
        Gets NonMaster list for the given logical Object  
        
        Signature ``GetNonMasterList(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :returns:  Non-master part file names  
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.GetNonMasterListForCopyLogicalObject` instead
        
        License requirements: None.
        """
        ...
    
    
    def IsNonMasterBeingCopied(self, logicalObject: LogicalObject, partName: str) -> bool:
        """
        Returns whether or not the non master part specified for the given :py:class:`NXOpen.PDM.LogicalObject`will actually get
        saved during the save as operation.  
        
        Signature ``IsNonMasterBeingCopied(logicalObject, partName)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param partName:  the non-master part that the caller wants to save or not save  
        :type partName: str 
        :returns:  True means that this non-master will be saved. False means that this non master will not be saved.  
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.IsNonMasterForLogicalObjectBeingCopied` instead
        
        License requirements: None.
        """
        ...
    
    
    def GetNonMasterCopyOption(self, logicalObject: LogicalObject) -> PartOperationBuilderNonMasterSaveAs:
        """
        Get the nonmasters saveAs option for given logical object.  
        
        Save As option can be one of these
        :py:class:`PartOperationBuilderNonMasterSaveAs.All <PartOperationBuilderNonMasterSaveAs>` and 
        :py:class:`PartOperationBuilderNonMasterSaveAs.None <PartOperationBuilderNonMasterSaveAs>` 
        
        Signature ``GetNonMasterCopyOption(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationBuilderNonMasterSaveAs` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.GetCopyNonMasterPartsOption` instead
        
        License requirements: None.
        """
        ...
    
    
    def EditNonMasterName(self, logicalObject: LogicalObject, oldName: str, newName: str) -> bool:
        """
        Sets the name the non-master part will get saved as.  
        
        It will get saved as the
        original non-master name if this method is not called.  
        
        Signature ``EditNonMasterName(logicalObject, oldName, newName)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param oldName:  the non-master part whose save as name is being set here  
        :type oldName: str 
        :param newName:  the new name  
        :type newName: str 
        :returns:  flag to indicate whether the newName is valid  
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.EditNonMasterToCopyName` instead
        
        License requirements: None.
        """
        ...
    
    
    def ClearWarnings(self) -> None:
        """
        Executes method ClearWarningCodeToLogicalObjectsSetMap() which clears m_warningCodeToLogicalObjectsSetMap 
        
        Signature ``ClearWarnings()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetErrorMessageHandler(self, refresh: bool) -> ErrorMessageHandler:
        """
        Returns ErrorMessageHandler  
        
        Signature ``GetErrorMessageHandler(refresh)`` 
        
        :param refresh: 
        :type refresh: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.ErrorMessageHandler` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributes(self, objects: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given array of objects and returns an array of objects that failed to auto assign.  
        
        Signature ``AutoAssignAttributes(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributesWithNamingPattern(self, objects: 'list[NXOpen.NXObject]', properties: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given object and returns an array of objects that failed to auto assign.  
        
        properties needs to be created using :py:meth:`CreateAttributeTitleToNamingPatternMap`
        
        Signature ``AutoAssignAttributesWithNamingPattern(objects, properties)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :param properties: 
        :type properties: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: 'list[str]', titlePatterns: 'list[str]') -> NXOpen.NXObject:
        """
        Creates a map object of attribute titles to their corresponding naming pattern  
        
        Signature ``CreateAttributeTitleToNamingPatternMap(attributeTitles, titlePatterns)`` 
        
        :param attributeTitles: 
        :type attributeTitles: list of str 
        :param titlePatterns: 
        :type titlePatterns: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    DefaultDestinationFolder: str = ...
    """
    Returns or sets  the default destination folder string for the part being created .  
    
    It will be ignored in case of 
    revise and creation of non-masters.
    The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
    In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultDestinationFolder`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultDestinationFolder`` 
    
    :param defaultDestinationFolder: 
    :type defaultDestinationFolder: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    DependentFileSaveAsOption: PartOperationBuilderDependentFileSaveAs = ...
    """
    Returns or sets  the Dependent files Save As option.  
    
    Save As option can be one of these
    :py:class:`PartOperationBuilderDependentFileSaveAs.All <PartOperationBuilderDependentFileSaveAs>` and 
    :py:class:`PartOperationBuilderDependentFileSaveAs.None <PartOperationBuilderDependentFileSaveAs>`
    
    <hr>
    
    Getter Method
    
    Signature ``DependentFileSaveAsOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartOperationBuilderDependentFileSaveAs` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.DependentFilesToCopyOption` instead
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DependentFileSaveAsOption`` 
    
    :param saveOption: 
    :type saveOption: :py:class:`NXOpen.PDM.PartOperationBuilderDependentFileSaveAs` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.SetDependentFilesToCopyOption` instead
    
    License requirements: None.
    """
    ReplaceAllComponents: bool = ...
    """
    Returns or sets  the replace all components.  
    
    This option specifies whether part will be replaced or copied.             
    Applicable only for operation types 
    :py:class:`PartOperationBuilderOperationType.SaveAs <PartOperationBuilderOperationType>` and 
    :py:class:`PartOperationBuilderOperationType.Revise <PartOperationBuilderOperationType>`
    
    <hr>
    
    Getter Method
    
    Signature ``ReplaceAllComponents`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.ReplaceAllComponentsInSession` instead
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReplaceAllComponents`` 
    
    :param replaceAllComponents: 
    :type replaceAllComponents: bool 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.SetReplaceAllComponentsInSession` instead
    
    License requirements: None.
    """
    Null: PartOperationBuilder = ...  # unknown typename


class PartOperationCreateBuilderOperationSubTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationCreateBuilderOperationSubType():
    """
    Represents an operation sub type for creating a part 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FromTemplate", "Create New Part from template"
       "SelectTemplate", "Populate Part already created in Teamcenter"
       "Rename", "Rename Existing Part"
       "CreateSpecification", "Create Specification and not a Part"
    """
    FromTemplate = 0  # PartOperationCreateBuilderOperationSubTypeMemberType
    SelectTemplate = 1  # PartOperationCreateBuilderOperationSubTypeMemberType
    Rename = 2  # PartOperationCreateBuilderOperationSubTypeMemberType
    CreateSpecification = 3  # PartOperationCreateBuilderOperationSubTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationCreateBuilder(PartOperationBuilder):
    """
    Represents a builder class that performs Create operations   
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreateCreateOperationBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    class OperationSubType():
        """
        Represents an operation sub type for creating a part 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FromTemplate", "Create New Part from template"
           "SelectTemplate", "Populate Part already created in Teamcenter"
           "Rename", "Rename Existing Part"
           "CreateSpecification", "Create Specification and not a Part"
        """
        FromTemplate = 0  # PartOperationCreateBuilderOperationSubTypeMemberType
        SelectTemplate = 1  # PartOperationCreateBuilderOperationSubTypeMemberType
        Rename = 2  # PartOperationCreateBuilderOperationSubTypeMemberType
        CreateSpecification = 3  # PartOperationCreateBuilderOperationSubTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetItemType(self, itemType: str) -> None:
        """
        Sets the selected Item Type 
        
        Signature ``SetItemType(itemType)`` 
        
        :param itemType: 
        :type itemType: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetModelType(self, modelType: str) -> None:
        """
        Sets the selected Model Type 
        This is same as the Relation Type that is set by :py:meth:`NXOpen.FileNew.RelationType` and is same as
        the relation type specified in Template PAX files.  
        
        This is needed to be set only when the :py:class:`NXOpen.PDM.PartOperationCreateBuilderOperationSubType` is set 
        to :py:class:`NXOpen.PDM.PartOperationCreateBuilderOperationSubType.CreateSpecification <NXOpen.PDM.PartOperationCreateBuilderOperationSubType>`. In other cases
        this is read from the Template. If not set this is always assumed to be "master".
        Example strings are "specification", "manifestation", etc.
        
        Signature ``SetModelType(modelType)`` 
        
        :param modelType: 
        :type modelType: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMasterPart(self, masterPart: NXOpen.BasePart) -> None:
        """
        Sets the Master Part 
        Use this only in case the part your are trying to create supports master model.  
        
        Signature ``SetMasterPart(masterPart)`` 
        
        :param masterPart: 
        :type masterPart: :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOperationSubType(self) -> PartOperationCreateBuilderOperationSubType:
        """
        Returns the :py:class:`NXOpen.PDM.PartOperationCreateBuilderOperationSubType` for Create.  
        
        Signature ``GetOperationSubType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationCreateBuilderOperationSubType` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOperationSubType(self, operatioSubType: PartOperationCreateBuilderOperationSubType) -> None:
        """
        Sets the :py:class:`NXOpen.PDM.PartOperationCreateBuilderOperationSubType` for Create.  
        
        Signature ``SetOperationSubType(operatioSubType)`` 
        
        :param operatioSubType: 
        :type operatioSubType: :py:class:`NXOpen.PDM.PartOperationCreateBuilderOperationSubType` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAddMaster(self, addMaster: bool) -> None:
        """
        Sets the Add Master Flag 
        Use this only in case creating a new Altrep.  
        
        This will add master as a component to newly created master.
        This will be set to false if tempalte selected doesn't supports creating new altrep.
        
        Signature ``SetAddMaster(addMaster)`` 
        
        :param addMaster: 
        :type addMaster: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPartsToRename(self, partsToRename: 'list[NXOpen.BasePart]') -> None:
        """
        Sets the Parts To Rename on the Builder.  
        
        This is only applicable if :py:class:`NXOpen.PDM.PartOperationCreateBuilderOperationSubType` is set to
        :py:class:`NXOpen.PDM.PartOperationCreateBuilderOperationSubType.Rename <NXOpen.PDM.PartOperationCreateBuilderOperationSubType>`
        
        Signature ``SetPartsToRename(partsToRename)`` 
        
        :param partsToRename: 
        :type partsToRename: list of :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAddMaster(self) -> bool:
        """
        Returns logical value to indicate whether master to be added as child component  
        
        Signature ``GetAddMaster()`` 
        
        :returns:  whether master to be added as child component  
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPartSpecToOpen(self, partSpecToOpen: str) -> None:
        """
        Sets the Part Spec of the part to open in case of Select Template Dialog
        This is only applicable if :py:class:`NXOpen.PDM.PartOperationCreateBuilderOperationSubType` is set to
        :py:class:`NXOpen.PDM.PartOperationCreateBuilderOperationSubType.SelectTemplate <NXOpen.PDM.PartOperationCreateBuilderOperationSubType>`
        partSpecTopOpen can be a CLI format (<@>DB/MFKID/RevId) or full TCIN file specification (starting with %UGMGR)
        
        Signature ``SetPartSpecToOpen(partSpecToOpen)`` 
        
        :param partSpecToOpen: 
        :type partSpecToOpen: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: PartOperationCreateBuilder = ...  # unknown typename


class SheetRevision(ConditionalElementRevision):
    """
    Represents a base class that provides common methods for various model elements in a :py:class:`NXOpen.CollaborativeDesign`.  
    
    Use the static method in this class to obtain an instance.
    
    .. versionadded:: NX11.0.0
    """
    Null: SheetRevision = ...  # unknown typename


class SearchResult(NXOpen.TransientObject):
    """
    Represents search query   
    
    .. versionadded:: NX6.0.0
    """
    
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
    
    
    def GetResultObjectNames(self) -> 'list[str]':
        """
        Gets a list of the object names from the search result  
        
        Signature ``GetResultObjectNames()`` 
        
        :returns:  array of object names  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetResultItemIds(self) -> 'list[str]':
        """
        Gets a list of the item_ids from the search result.  
        
        If Multifield Key environment is enabled, 
        then use Multifield key function :py:meth:`PDM.SearchResult.GetResultMfkIds`, as 
        this function may return us duplicate item ids if the corresponding parts belong to different domains.  
        
        Signature ``GetResultItemIds()`` 
        
        :returns:  array of item_ids  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`PDM.SearchResult.GetResultMfkIds` instead.
        
        License requirements: None.
        """
        ...
    
    
    def GetResultMfkIds(self) -> 'list[str]':
        """
        Gets a list of the Multifield Keys from the search results.  
        
        If Multifield Key
        environment is enabled then always use this function 
        Multifield Key: e.g. %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x  
        
        Signature ``GetResultMfkIds()`` 
        
        :returns:  array of mfk_ids  
        :rtype: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetResultObjectTypes(self) -> 'list[str]':
        """
        Gets a list of the object types from the search result  
        
        Signature ``GetResultObjectTypes()`` 
        
        :returns:  array of object types  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    


class AlternateIdManagerAlternateIdsData_Struct():
    """
    Contains alternate Ids data .  
    
    Constructor: 
    NXOpen.PDM.AlternateIdManager.AlternateIdsData()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    AlternateItemId: str = ...
    """
    the new value for the alternate item ID  
    <hr>
    
    Field Value
    Type:str
    """
    AlternateRevId: str = ...
    """
    the new value for the alternate Revision ID
    <hr>
    
    Field Value
    Type:str
    """
    AlternateName: str = ...
    """
    the new value for the alternate Name
    <hr>
    
    Field Value
    Type:str
    """
    AlternateDescription: str = ...
    """
    the new value for the alternate Description
    <hr>
    
    Field Value
    Type:str
    """
    Modifiable: bool = ...
    """
    the new value for the alternate for modifiable flag
    <hr>
    
    Field Value
    Type:bool
    """


class PdmPartCheckinInput_Struct():
    """
    Reservation check-in input struct .  
    
    Constructor: 
    NXOpen.PDM.PdmPart.CheckinInput()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    AllowRemote: bool = ...
    """
    True to allow remote check in, false otherwise 
    <hr>
    
    Field Value
    Type:bool
    """
    ExplicitCheckIn: bool = ...
    """
    True to perform explicit check in, false otherwise 
    <hr>
    
    Field Value
    Type:bool
    """
    IncludeSecondary: bool = ...
    """
    True to check out secondary dataset, false otherwise 
    <hr>
    
    Field Value
    Type:bool
    """


class AttributeGroup(NXOpen.NXObject, IAttributeGroupOwner):
    """
    Represents an attribute group.  
    
    KF not supported.
    
    .. versionadded:: NX9.0.0
    """
    
    def GetReferencingAttributeGroupOwners(self) -> 'list[IAttributeGroupOwner]':
        """
        Returns a list of :py:class:`NXOpen.PDM.IAttributeGroupOwner` objects referencing this attribute group.  
        
        Signature ``GetReferencingAttributeGroupOwners()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.IAttributeGroupOwner` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DetachAttributeGroup(self, attributeGroupOwner: IAttributeGroupOwner) -> None:
        """
        Detaches Attribute Group 
        
        Signature ``DetachAttributeGroup(attributeGroupOwner)`` 
        
        :param attributeGroupOwner: 
        :type attributeGroupOwner: :py:class:`NXOpen.PDM.IAttributeGroupOwner` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Create(self, attributeGroupDescription: AttributeGroupDescription) -> AttributeGroup:
        """
        Creates an attribute group for a :py:class:`NXOpen.PDM.IAttributeGroupOwner`, based on an attribute
        group type.  
        
        An attribute group type is represented by an :py:class:`NXOpen.PDM.AttributeGroupDescription`.
        
        Signature ``Create(attributeGroupDescription)`` 
        
        :param attributeGroupDescription: 
        :type attributeGroupDescription: :py:class:`NXOpen.PDM.AttributeGroupDescription` 
        :returns:  The new attribute group.  
        :rtype: :py:class:`NXOpen.PDM.AttributeGroup` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateAttributeGroupReviseBuilder(self, attributeGroups: 'list[AttributeGroup]') -> AttributeGroupReviseBuilder:
        """
        Creates a :py:class:`NXOpen.PDM.AttributeGroupReviseBuilder` object.  The builder creates a
        revision for each attribute group in the input list of existing attribute groups.  
        
        Signature ``CreateAttributeGroupReviseBuilder(attributeGroups)`` 
        
        :param attributeGroups: 
        :type attributeGroups: list of :py:class:`NXOpen.PDM.AttributeGroup` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.AttributeGroupReviseBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateAttributeGroupReviseBuilder(self, attributeGroups: 'list[AttributeGroup]', keepOriginal: bool, saveAsActionType: AttributeGroupReviseBuilderSaveAsActionType) -> AttributeGroupReviseBuilder:
        """
        The builder will do a revise or save-as operation for each attribute group in the input list of existing attribute groups 
        depending on input operation type.  
        
        Signature ``CreateAttributeGroupReviseBuilder(attributeGroups, keepOriginal, saveAsActionType)`` 
        
        :param attributeGroups: 
        :type attributeGroups: list of :py:class:`NXOpen.PDM.AttributeGroup` 
        :param keepOriginal: 
        :type keepOriginal: bool 
        :param saveAsActionType: 
        :type saveAsActionType: :py:class:`NXOpen.PDM.AttributeGroupReviseBuilderSaveAsActionType` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.AttributeGroupReviseBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAttributeGroups(self) -> 'list[AttributeGroup]':
        """
        Returns the :py:class:`NXOpen.PDM.AttributeGroup` objects owned by this object.  
        
        Signature ``GetAttributeGroups()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.AttributeGroup` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAttributeGroupDescriptions(self) -> 'list[AttributeGroupDescription]':
        """
        Returns the :py:class:`NXOpen.PDM.AttributeGroupDescription` objects representing the attribute
        group types supported by this object.  
        
        Signature ``GetAttributeGroupDescriptions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.AttributeGroupDescription` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    DisplayName: str = ...
    """
    Returns  the display name for the attribute group.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: AttributeGroup = ...  # unknown typename


class NonMasterDataCopyNonMasterPartsOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NonMasterDataCopyNonMasterPartsOption():
    """
    This enum is used to specify which non-master parts 
    should be copied to new part during the save as operation.   
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", "save all during save as"
       "NotSet", "save none during save as"
    """
    All = 0  # NonMasterDataCopyNonMasterPartsOptionMemberType
    NotSet = 1  # NonMasterDataCopyNonMasterPartsOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NonMasterData(NXOpen.TransientObject):
    """
    Represents a class that performs various operations on NonMaster Datasets   
    
    .. versionadded:: NX11.0.0
    """
    
    class CopyNonMasterPartsOption():
        """
        This enum is used to specify which non-master parts 
        should be copied to new part during the save as operation.   
        
        .. versionadded:: NX11.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", "save all during save as"
           "NotSet", "save none during save as"
        """
        All = 0  # NonMasterDataCopyNonMasterPartsOptionMemberType
        NotSet = 1  # NonMasterDataCopyNonMasterPartsOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateNonMasterListForLogicalObject(self, logicalObject: LogicalObject) -> None:
        """
        Create NonMaster list for the selected logical Object 
        
        Signature ``CreateNonMasterListForLogicalObject(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNonMasterListForCopyLogicalObject(self, logicalObject: LogicalObject) -> 'list[str]':
        """
        Gets NonMaster list for the given logical Object  
        
        Signature ``GetNonMasterListForCopyLogicalObject(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :returns:  Non-master part file names  
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsNonMasterForLogicalObjectBeingCopied(self, logicalObject: LogicalObject, partName: str) -> bool:
        """
        Returns whether or not the non-master part specified for the given :py:class:`NXOpen.PDM.LogicalObject`will actually
        get saved during the save as operation.  
        
        Signature ``IsNonMasterForLogicalObjectBeingCopied(logicalObject, partName)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param partName:  the non-master part that the caller wants to save or not save  
        :type partName: str 
        :returns:  True means that this non-master will be saved.
        False means that this non-master will not be saved.  
        :rtype: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCopyNonMasterPartsOption(self, logicalObject: LogicalObject) -> NonMasterDataCopyNonMasterPartsOption:
        """
        Get the nonmasters saveAs option for given logical object.  
        
        Save As option can be one of these
        :py:class:`NonMasterDataCopyNonMasterPartsOption.All <NonMasterDataCopyNonMasterPartsOption>` and 
        :py:class:`NonMasterDataCopyNonMasterPartsOption.None <NonMasterDataCopyNonMasterPartsOption>` 
        
        Signature ``GetCopyNonMasterPartsOption(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.NonMasterDataCopyNonMasterPartsOption` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNonMasterSaveAsOption(self, logicalObject: LogicalObject, saveOption: NonMasterDataCopyNonMasterPartsOption) -> None:
        """
        Set the nonmasters saveAs option for given logical object.  
        
        Save As option can be one of these
        :py:class:`NonMasterDataCopyNonMasterPartsOption.All <NonMasterDataCopyNonMasterPartsOption>` and 
        :py:class:`NonMasterDataCopyNonMasterPartsOption.None <NonMasterDataCopyNonMasterPartsOption>`
        
        Signature ``SetNonMasterSaveAsOption(logicalObject, saveOption)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param saveOption: 
        :type saveOption: :py:class:`NXOpen.PDM.NonMasterDataCopyNonMasterPartsOption` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedNonMasterToCopy(self, logicalObject: LogicalObject, partName: str) -> None:
        """
        Sets whether or not the non-master part specified will actually
        get saved during the save as operation.  
        
        True means that it will be
        saved. False means that it will not be saved.  
        
        Signature ``SetSelectedNonMasterToCopy(logicalObject, partName)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param partName:  the non-master part whose save option is being set here  
        :type partName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EditNonMasterToCopyName(self, logicalObject: LogicalObject, oldName: str, newName: str) -> bool:
        """
        Sets the name the non-master part will get saved as.  
        
        It will get saved as the
        original non-master name if this method is not called.  
        
        Signature ``EditNonMasterToCopyName(logicalObject, oldName, newName)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param oldName:  the non-master part whose save as name is being set here  
        :type oldName: str 
        :param newName:  the new name  
        :type newName: str 
        :returns:  flag to indicate whether the newName is valid  
        :rtype: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class CaeCloneManagerCloneOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CaeCloneManagerCloneOption():
    """
    Option for creation of part builder for CAE Clone 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Sim", " - "
       "Fem", " - "
       "Ideal", " - "
       "Master", " - "
    """
    NotSet = -1  # CaeCloneManagerCloneOptionMemberType
    Sim = 0  # CaeCloneManagerCloneOptionMemberType
    Fem = 1  # CaeCloneManagerCloneOptionMemberType
    Ideal = 2  # CaeCloneManagerCloneOptionMemberType
    Master = 3  # CaeCloneManagerCloneOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CaeCloneManager(NXOpen.TransientObject):
    """
    This class is used for executing CAE Clone on a Simulation File or a FeModel File.
    
    Use :py:class:`NXOpen.PDM.PartManager` to get the instance of this class.
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:class:`NXOpen.PDM.PartOperationCopyBuilder` instead.
    """
    
    class CloneOption():
        """
        Option for creation of part builder for CAE Clone 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Sim", " - "
           "Fem", " - "
           "Ideal", " - "
           "Master", " - "
        """
        NotSet = -1  # CaeCloneManagerCloneOptionMemberType
        Sim = 0  # CaeCloneManagerCloneOptionMemberType
        Fem = 1  # CaeCloneManagerCloneOptionMemberType
        Ideal = 2  # CaeCloneManagerCloneOptionMemberType
        Master = 3  # CaeCloneManagerCloneOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPartBuilderForClone(self, option: CaeCloneManagerCloneOption) -> PartFromPartBuilder:
        """
        Get Part Builders for Clone Operation of a CAE Simulation or a CAE Model part.  
        
        Get  builder class :py:class:`NXOpen.PDM.PartFromPartBuilder` using this function.
        
        Signature ``GetPartBuilderForClone(option)`` 
        
        :param option: 
        :type option: :py:class:`NXOpen.PDM.CaeCloneManagerCloneOption` 
        :returns:  the part builder  
        :rtype: :py:class:`NXOpen.PDM.PartFromPartBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def SetIncludeMaster(self, value: bool) -> None:
        """
        Sets the option for include master on the Clone Manager class 
        
        Signature ``SetIncludeMaster(value)`` 
        
        :param value: 
        :type value: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetContainer(self, option: CaeCloneManagerCloneOption) -> str:
        """
        Gets the container in Teamcenter where the cloned part is saved
        
        Signature ``GetContainer(option)`` 
        
        :param option: 
        :type option: :py:class:`NXOpen.PDM.CaeCloneManagerCloneOption` 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def SetContainer(self, option: CaeCloneManagerCloneOption, container: str) -> None:
        """
        Sets the container in Teamcenter where the cloned part is saved
        
        Signature ``SetContainer(option, container)`` 
        
        :param option: 
        :type option: :py:class:`NXOpen.PDM.CaeCloneManagerCloneOption` 
        :param container: 
        :type container: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def CommitClone(self) -> None:
        """
        Commits the Clone Operation for the Clone Manager class :py:class:`NXOpen.PDM.CaeCloneManager`.  
        
        Deletes all the Part Builders associated with the Clone Manager
        
        Signature ``CommitClone()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    


class PdmSearch(NXOpen.TransientObject):
    """
    Represents search query   
    
    .. versionadded:: NX6.0.0
    """
    
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
    
    
    def Advanced(self, entries: 'list[str]', values: 'list[str]') -> SearchResult:
        """
        This API performs advanced search in the teamcenter and returns the result vector .  
        
        Internally it will execute the NX standard Query
        "__NX_STD_ANY_ITEM_QUERY". Advanced search takes in detailed inputs to perform the search. 
        The parameters "entries" and "values" are the internal property names and their values to be searched.
        The attribute/value pairs are combined logically using AND so that only objects matching ALL of the specified
        criteria are returned.
        The method can only be used to search for matches on Teamcenter properties that are string valued.
        It does not work for properties which are Object/LOV valued.
        For example "owning_user" is TC Object valued so the search does not find any matches when attempting to search on it.
        **
        Please note, this functionality is available starting in Teamcenter 2007.1 MP2.
        To see how to spell the "real" attribute names rather than the displayed attribute (column) names,
        use Edit-> Options...-> General-> UI-> Sys Admin-> Real Property Name in the Rich Client.
        </b>
        
        Signature ``Advanced(entries, values)`` 
        
        :param entries:  search criteria entries  
        :type entries: list of str 
        :param values:  search criteria values  
        :type values: list of str 
        :returns:  search result  
        :rtype: :py:class:`NXOpen.PDM.SearchResult` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Simple(self, searchCriteria: str) -> SearchResult:
        """
        Perform simple search in the teamcenter and returns the result vector.  
        
        Internally it will execute the NX standard Query "__NX_STD_SIMPLE_ITEM_QUERY". 
        ItemId should be given as the searchCriteria for searching the items
        **
        Please note,  this functionality is available starting in Teamcenter 2007.1 MP2.
        </b>
        
        Signature ``Simple(searchCriteria)`` 
        
        :param searchCriteria:  search criteria as string  
        :type searchCriteria: str 
        :returns:  search result  
        :rtype: :py:class:`NXOpen.PDM.SearchResult` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    


class DBEntityProxy(NXOpen.NXObject):
    """
    JA class for the DBEntityProxy object  
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX11.0.0
    """
    Null: DBEntityProxy = ...  # unknown typename


class PdmSession():
    """
    Represents the NX Manager session   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX7.5.0
    """
    
    def GetTcserverSettings(self) -> tuple:
        """
        Returns the connect string and discriminator used by NX session to connect to the Tcserver.  
        
        The client applications can use these settings to connect to the same Tcserver that NX
        is using.
        
        Tcserver connect string: The connect string is path of the server hosting the services.
        The connect string for the different transport protocols will be in the following form:
        4-Tier(HTTP mode): similar to http:
        2-Tier(IIOP mode): The Tcserver IOR string 
        
        Discriminator: The discriminator is a unique identifier and contains unique information related 
        to a given TC server. This unique identifier (discriminator) is recognized by TC pool manager as
        the session number that ties the server process to the client. The discriminator functionality 
        is part of the SOA package. The discriminator allows multiple clients to connect to the same TC server.
        In 2-Tier(IIOP mode), the discriminator will be an empty string.
        
        To connect to the same Tcserver as NX, the client can create a Teamcenter::Soa::Client::Connection 
        object using the connect string and then use the Teamcenter::Services::Core::SessionService to login
        to Teamcenter Server with the discriminator and the connection object. More information about
        connecting to the Teamcenter server can be found in the TC SOA API Documentation.
        
        Signature ``GetTcserverSettings()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (connectString, discriminator). connectString is a str.   the connection string discriminator is a str.   the discriminator 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSsoSettings(self) -> tuple:
        """
        Returns the SSO credentials, if SSO is available 
        The client applications can use these settings to connect to the same Tcserver that NX
        is using.  
        
        Signature ``GetSsoSettings()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (isSsoEnabled, ssoServerUrl, ssoAppID). isSsoEnabled is a bool.   if SSO is enabled ssoServerUrl is a str.   the SSO server URL ssoAppID is a str.   the SSO app id 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultFolder(self, defaultFolderSpec: str) -> None:
        """
        Sets default folder.  
        
        The input default folder path in format &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, where username is optional.
        In that case, in :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container
        
        Signature ``SetDefaultFolder(defaultFolderSpec)`` 
        
        :param defaultFolderSpec:  Default folder path including default folder name to be set  
        :type defaultFolderSpec: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def NewFileManagement(self) -> FileManagement:
        """
        Returns a new :py:class:`NXOpen.PDM.FileManagement` object  
        
        Signature ``NewFileManagement()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.FileManagement` 
        
        .. versionadded:: NX7.5.4
        
        License requirements: None.
        """
        ...
    
    
    def NewCaeFileContainer(self) -> CAEFileContainer:
        """
        Returns a new :py:class:`NXOpen.PDM.CAEFileContainer` object  
        
        Signature ``NewCaeFileContainer()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.CAEFileContainer` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateCopyOperationBuilder(self, operation: PartOperationBuilderOperationType) -> PartOperationCopyBuilder:
        """
        Returns a new :py:class:`NXOpen.PDM.PartOperationCopyBuilder` object 
        
        Signature ``CreateCopyOperationBuilder(operation)`` 
        
        :param operation: 
        :type operation: :py:class:`NXOpen.PDM.PartOperationBuilderOperationType` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationCopyBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateCreateOperationBuilder(self, operation: PartOperationBuilderOperationType) -> PartOperationCreateBuilder:
        """
        Returns a new :py:class:`NXOpen.PDM.PartOperationCreateBuilder` object 
        
        Signature ``CreateCreateOperationBuilder(operation)`` 
        
        :param operation: 
        :type operation: :py:class:`NXOpen.PDM.PartOperationBuilderOperationType` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationCreateBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateOperationBuilder(self, operation: PartOperationBuilderOperationType) -> PartOperationBuilder:
        """
        Returns a new :py:class:`NXOpen.PDM.PartOperationBuilder` object 
        
        Signature ``CreateOperationBuilder(operation)`` 
        
        :param operation: 
        :type operation: :py:class:`NXOpen.PDM.PartOperationBuilderOperationType` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationBuilder` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.PDM.PdmSession.CreateCopyOperationBuilder` instead
        
        License requirements: None.
        """
        ...
    
    
    def CreateObjectCreateBuilder(self, tcTypes: 'list[str]', baseTCTypes: 'list[str]') -> ObjectCreateBuilder:
        """
        Returns a new :py:class:`NXOpen.PDM.ObjectCreateBuilder` object 
        
        Signature ``CreateObjectCreateBuilder(tcTypes, baseTCTypes)`` 
        
        :param tcTypes: 
        :type tcTypes: list of str 
        :param baseTCTypes: 
        :type baseTCTypes: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.ObjectCreateBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateMakeUniqueOperationBuilder(self, part: NXOpen.BasePart) -> PartOperationMakeUniqueBuilder:
        """
        Returns a new :py:class:`NXOpen.PDM.PartOperationMakeUniqueBuilder` object 
        
        Signature ``CreateMakeUniqueOperationBuilder(part)`` 
        
        :param part: 
        :type part: :py:class:`NXOpen.BasePart` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationMakeUniqueBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateImportOperationBuilder(self) -> PartOperationImportBuilder:
        """
        Returns a new :py:class:`NXOpen.PDM.PartOperationImportBuilder` object 
        
        Signature ``CreateImportOperationBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreatePartOperationAttributePropertiesBuilder(self, objects: 'list[NXOpen.NXObject]') -> PartOperationAttributePropertiesBuilder:
        """
        Creates a new :py:class:`NXOpen.PDM.PartOperationAttributePropertiesBuilder` object.  
        
        Signature ``CreatePartOperationAttributePropertiesBuilder(objects)`` 
        
        :param objects:  the array of objects  
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationAttributePropertiesBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreatePartOperationValidationPropertiesBuilder(self, objects: 'list[NXOpen.NXObject]') -> NXOpen.AttributePropertiesBuilder:
        """
        Creates a new :py:class:`AttributePropertiesBuilder` object.  
        
        Signature ``CreatePartOperationValidationPropertiesBuilder(objects)`` 
        
        :param objects:  the array of objects  
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.AttributePropertiesBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetDatabaseObjectManager(self) -> DatabaseObjectManager:
        """
        Gets the :py:class:`NXOpen.PDM.DatabaseObjectManager` object.  
        
        Signature ``GetDatabaseObjectManager()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.DatabaseObjectManager` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateSmartSaveBuilder(self, saveType: SmartSaveBuilderSaveType) -> SmartSaveBuilder:
        """
        Creates a new :py:class:`SmartSaveBuilder` object.  
        
        Signature ``CreateSmartSaveBuilder(saveType)`` 
        
        :param saveType: 
        :type saveType: :py:class:`NXOpen.PDM.SmartSaveBuilderSaveType` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.SmartSaveBuilder` 
        
        .. versionadded:: NX11.0.0
        
        .. deprecated::  NX11.0.1
           Use :py:meth:`NXOpen.PDM.PdmSession.CreateSmartSaveBuilderWithContext` instead
        
        License requirements: None.
        """
        ...
    
    
    def CreateSmartSaveContext(self, saveType: SmartSaveBuilderSaveType) -> SmartSaveContext:
        """
        Creates a new :py:class:`SmartSaveContext` object.  
        
        Signature ``CreateSmartSaveContext(saveType)`` 
        
        :param saveType: 
        :type saveType: :py:class:`NXOpen.PDM.SmartSaveBuilderSaveType` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.SmartSaveContext` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CreateSmartSaveBuilderWithContext(self, smartSaveContext: SmartSaveContext) -> SmartSaveBuilder:
        """
        Creates a new :py:class:`SmartSaveBuilder` object.  
        
        Signature ``CreateSmartSaveBuilderWithContext(smartSaveContext)`` 
        
        :param smartSaveContext: 
        :type smartSaveContext: :py:class:`NXOpen.PDM.SmartSaveContext` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.SmartSaveBuilder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CreateExportWorksetForReferenceBuilder(self, workset: NXOpen.BasePart) -> ExportWorksetForReferenceBuilder:
        """
        Creates a new :py:class:`NXOpen.PDM.ExportWorksetForReferenceBuilder` object used for
        exporting workset outside Teamcenter for reference.  
        
        Signature ``CreateExportWorksetForReferenceBuilder(workset)`` 
        
        :param workset:  workset assembly to export  
        :type workset: :py:class:`NXOpen.BasePart` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.ExportWorksetForReferenceBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetActiveEngineeringChangeNotice(self, part: NXOpen.Part, ecnId: str, ecnRevsionId: str) -> None:
        """
        Sets active ECN for the session.  
        
        The input will be in the format of ECN ID and the ECN Revision ID.
        
        Signature ``SetActiveEngineeringChangeNotice(part, ecnId, ecnRevsionId)`` 
        
        :param part:  tag of the displayed part  
        :type part: :py:class:`NXOpen.Part` 
        :param ecnId:  ECN ItemID to be set  
        :type ecnId: str 
        :param ecnRevsionId:  ECN ItemRevID to be set  
        :type ecnRevsionId: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    AttributeGroupDescriptions: AttributeGroupDescriptionCollection = ...
    """
    Returns a collection of :py:class:`NXOpen.PDM.AttributeGroupDescription` objects representing
    attribute group types.  
    
    The collection contains attribute group descriptions for
    :py:class:`NXOpen.PDM.IAttributeGroupOwner` objects loaded within the NX session.
    Use the :py:meth:`NXOpen.PDM.IAttributeGroupOwner.GetAttributeGroupDescriptions`
    to get the specific attribute group descriptions for an attribute group owner.  
    
    Signature ``AttributeGroupDescriptions`` 
    
    .. versionadded:: NX9.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.AttributeGroupDescriptionCollection`
    """
    PartOperationImportObserver: PartOperationImportObserver = ...
    """
    Returns the :py:class:`NXOpen.PDM.PartOperationImportObserver` belonging to this session 
    
    Signature ``PartOperationImportObserver`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartOperationImportObserver`
    """
    SaveAsReviseObserver: SaveAsReviseObserver = ...
    """
    Returns the :py:class:`NXOpen.PDM.SaveAsReviseObserver` belonging to this session 
    
    Signature ``SaveAsReviseObserver`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.SaveAsReviseObserver`
    """


class ErrorMessageHandler(NXOpen.TransientObject):
    """
    Represents the class that contains ErrorObjects and Failed Logical Objects.  
    
    .. versionadded:: NX11.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetErrorList(self) -> NXOpen.ErrorList:
        """
        Returns ERROR_LIST_s  
        
        Signature ``GetErrorList()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetErrorMessages(self) -> 'list[str]':
        """
        Returns Error Messages  
        
        Signature ``GetErrorMessages()`` 
        
        :returns:  Error Messages   
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetWarningMessages(self) -> 'list[str]':
        """
        Returns Warning Messages  
        
        Signature ``GetWarningMessages()`` 
        
        :returns:  Warning Messages   
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class PartOperationAttributePropertiesBuilder(NXOpen.AttributePropertiesBuilder):
    """
    Represents an :py:class:`NXOpen.PDM.PartOperationAttributePropertiesBuilder` to be used for 
    creating attributes in part operation.  
    
    The attribute will be distributed to all objects supplied in the selected object list.
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreatePartOperationAttributePropertiesBuilder`
    
    Default values.
    
    ==========================  =======
    Property                    Value
    ==========================  =======
    BooleanValue                False 
    --------------------------  -------
    DataType                    String 
    --------------------------  -------
    IntegerValue                0 
    --------------------------  -------
    NumberValue                 0 
    --------------------------  -------
    ObjectPicker (deprecated)   Object 
    ==========================  =======
    
    .. versionadded:: NX10.0.0
    """
    
    def CreateOrModifyAttribute(self) -> bool:
        """
        Create the attribute from the data set in the builder.  
        
        Unlike calling commit,
        this method will not perform an update.  
        
        Signature ``CreateOrModifyAttribute()`` 
        
        :returns:  True if the attribute was created/edited successfully  
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    ReferenceObject: LogicalObject = ...
    """
    Returns or sets  the referenced logical object from this attribute.  
    
    Only used for attribute
    of Reference Part.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.LogicalObject` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceObject`` 
    
    :param referencedLogicalObject: 
    :type referencedLogicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: PartOperationAttributePropertiesBuilder = ...  # unknown typename


class ConnectionElementRevision(ConditionalElementRevision):
    """
    Represents a base class that provides common methods for various model elements in a :py:class:`NXOpen.CollaborativeDesign`.  
    
    Instance of this can not directly created.
    
    .. versionadded:: NX11.0.0
    """
    Null: ConnectionElementRevision = ...  # unknown typename


class DatabaseObjectManager(NXOpen.TransientObject):
    """
    This class is used for retrieving PDM database objects.  
    
    Use :py:class:`PDM.PdmSession.GetDatabaseObjectManager` to get the instance of this class.
    
    .. versionadded:: NX11.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewFindcriteria(self, nCriteria: int) -> 'list[FindCriteria]':
        """
        This API constructs an array of empty :py:class:`NXOpen.PDM.FindCriteria` objects.  
        
        Signature ``NewFindcriteria(nCriteria)`` 
        
        :param nCriteria: 
        :type nCriteria: int 
        :returns:  Find criteria  
        :rtype: list of :py:class:`NXOpen.PDM.FindCriteria` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewDatabaseobjects(self) -> DatabaseObjects:
        """
        This API constructs a new :py:class:`NXOpen.PDM.DatabaseObjects` object.  
        
        Signature ``NewDatabaseobjects()`` 
        
        :returns:  Database objects  
        :rtype: :py:class:`NXOpen.PDM.DatabaseObjects` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObjects(self, findCriterias: 'list[FindCriteria]') -> 'list[DatabaseObjects]':
        """
        This API finds database objects in the Teamcenter database using a Teamcenter saved query.  
        
        Signature ``FindObjects(findCriterias)`` 
        
        :param findCriterias:  Find critieria  
        :type findCriterias: list of :py:class:`NXOpen.PDM.FindCriteria` 
        :returns:  Database objects  
        :rtype: list of :py:class:`NXOpen.PDM.DatabaseObjects` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class AttributeGroupDescriptionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of attribute group description objects.  
    
    A smaller list of attribute groups
    descriptions can be retrieved by using the method
    :py:meth:`NXOpen.PDM.IAttributeGroupOwner.GetAttributeGroupDescriptions`
    for classes that implement the :py:class:`NXOpen.PDM.IAttributeGroupOwner` interface.
    To obtain an instance of this class, refer to :py:class:`NXOpen.PDM.PdmSession`
    
    .. versionadded:: NX9.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> AttributeGroupDescription:
        """
        Finds the :py:class:`NXOpen.PDM.AttributeGroupDescription` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier to be found  
        :type journalIdentifier: str 
        :returns:  AttributeGroupDescription found, or null if no such attribute group description exists. 
        :rtype: :py:class:`NXOpen.PDM.AttributeGroupDescription` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    


class SaveAsReviseCallbackData(NXOpen.TaggedObject):
    """
    JA interface for SaveAsReviseCallbackData object   
    
    This cannot be created
    
    .. versionadded:: NX11.0.0
    """
    
    def GetSourceObjects(self) -> tuple:
        """
        Gets the source objects tags participating in saveas or revise operation  
        
        Signature ``GetSourceObjects()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (nObjects, sourceObjects). nObjects is a int.   get number of source objects going for SaveAs or Revise sourceObjects is a list of :py:class:`NXOpen.TaggedObject`.   array of source objects to be saveas or revise 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCopiedObjects(self, sourceObjects: NXOpen.TaggedObject) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the source objects tags along with copied objects tags after saveas or revise operation 
        
        Signature ``GetCopiedObjects(sourceObjects)`` 
        
        :param sourceObjects:  tag of source object for which copied objects are required  
        :type sourceObjects: :py:class:`NXOpen.TaggedObject` 
        :returns:  array of copied objects to be saveas or revise  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: SaveAsReviseCallbackData = ...  # unknown typename


class PersistentSettings(NXOpen.TransientObject):
    """
    Persistently held settings for a Teamcenter user account.  
    
    Any changes will only
    take effect when :py:meth:`PDM.PersistentSettings.Apply` is callsed. 
    
    .. versionadded:: NX4.0.0
    """
    
    def GetGroups(self) -> 'list[str]':
        """
        Gets the names of the Teamcenter groups to which the
        user belongs.  
        
        Signature ``GetGroups()`` 
        
        :returns:  the names of the groups  
        :rtype: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetVolumes(self) -> 'list[str]':
        """
        Gets the names of the Teamcenter volumes which the
        user may use, given the current group returned by :py:meth:`PDM.PersistentSettings.GetGroups`.  
        
        Signature ``GetVolumes()`` 
        
        :returns:  the names of the volumes  
        :rtype: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Apply(self) -> None:
        """
        Applies any changes to the settings 
        
        Signature ``Apply()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    Group: str = ...
    """
    Returns or sets  the Teamcenter group in which the user acts by default.  
    
    Should be
    one of those given by :py:meth:`PDM.PersistentSettings.GetGroups`
    
    <hr>
    
    Getter Method
    
    Signature ``Group`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Group`` 
    
    :param group: 
    :type group: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    Volume: str = ...
    """
    Returns or sets  the Teamcenter volume to which the user used by default.  
    
    Should be
    one of those given by :py:meth:`PDM.PersistentSettings.GetVolumes` 
    
    <hr>
    
    Getter Method
    
    Signature ``Volume`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Volume`` 
    
    :param volume: 
    :type volume: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """


class FileManagementFileTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FileManagementFileType():
    """
    PDM file types  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CmmDmi", " - "
       "CpdFeaturePart", " - "
       "CpdGeometryOverride", " - "
       "DirectModel", " - "
       "Excel", " - "
       "ExcelX", " - "
       "Image", " - "
       "Jpeg", " - "
       "NxAttachedPart", " - "
       "NxPart", " - "
       "NxPosBin", " - "
       "NxleSymbolXml", " - "
       "NxleSymbolPreview", " - "
       "Preview2d", " - "
       "Preview3d", " - "
       "QafBinary", " - "
       "QafText", " - "
       "RoutePipeRun", " - "
       "RoutePipeSpec", " - "
       "RoutePipeRunAttachment", " - "
       "Text", " - "
       "Tif", " - "
       "TrushapeData", " - "
       "ValidationRuleSet", " - "
    """
    CmmDmi = 0  # FileManagementFileTypeMemberType
    CpdFeaturePart = 1  # FileManagementFileTypeMemberType
    CpdGeometryOverride = 2  # FileManagementFileTypeMemberType
    DirectModel = 3  # FileManagementFileTypeMemberType
    Excel = 4  # FileManagementFileTypeMemberType
    ExcelX = 5  # FileManagementFileTypeMemberType
    Image = 6  # FileManagementFileTypeMemberType
    Jpeg = 7  # FileManagementFileTypeMemberType
    NxAttachedPart = 8  # FileManagementFileTypeMemberType
    NxPart = 9  # FileManagementFileTypeMemberType
    NxPosBin = 10  # FileManagementFileTypeMemberType
    NxleSymbolXml = 11  # FileManagementFileTypeMemberType
    NxleSymbolPreview = 12  # FileManagementFileTypeMemberType
    Preview2d = 13  # FileManagementFileTypeMemberType
    Preview3d = 14  # FileManagementFileTypeMemberType
    QafBinary = 15  # FileManagementFileTypeMemberType
    QafText = 16  # FileManagementFileTypeMemberType
    RoutePipeRun = 17  # FileManagementFileTypeMemberType
    RoutePipeSpec = 18  # FileManagementFileTypeMemberType
    RoutePipeRunAttachment = 19  # FileManagementFileTypeMemberType
    Text = 20  # FileManagementFileTypeMemberType
    Tif = 21  # FileManagementFileTypeMemberType
    TrushapeData = 22  # FileManagementFileTypeMemberType
    ValidationRuleSet = 23  # FileManagementFileTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FileManagement(NXOpen.TransientObject):
    """
    This class is responsible for Teamcenter file management related activities.  
    
    Use :py:meth:`PDM.PdmSession.NewFileManagement` to get the instance of this class.
    
    .. versionadded:: NX6.0.3
    """
    
    class FileType():
        """
        PDM file types  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CmmDmi", " - "
           "CpdFeaturePart", " - "
           "CpdGeometryOverride", " - "
           "DirectModel", " - "
           "Excel", " - "
           "ExcelX", " - "
           "Image", " - "
           "Jpeg", " - "
           "NxAttachedPart", " - "
           "NxPart", " - "
           "NxPosBin", " - "
           "NxleSymbolXml", " - "
           "NxleSymbolPreview", " - "
           "Preview2d", " - "
           "Preview3d", " - "
           "QafBinary", " - "
           "QafText", " - "
           "RoutePipeRun", " - "
           "RoutePipeSpec", " - "
           "RoutePipeRunAttachment", " - "
           "Text", " - "
           "Tif", " - "
           "TrushapeData", " - "
           "ValidationRuleSet", " - "
        """
        CmmDmi = 0  # FileManagementFileTypeMemberType
        CpdFeaturePart = 1  # FileManagementFileTypeMemberType
        CpdGeometryOverride = 2  # FileManagementFileTypeMemberType
        DirectModel = 3  # FileManagementFileTypeMemberType
        Excel = 4  # FileManagementFileTypeMemberType
        ExcelX = 5  # FileManagementFileTypeMemberType
        Image = 6  # FileManagementFileTypeMemberType
        Jpeg = 7  # FileManagementFileTypeMemberType
        NxAttachedPart = 8  # FileManagementFileTypeMemberType
        NxPart = 9  # FileManagementFileTypeMemberType
        NxPosBin = 10  # FileManagementFileTypeMemberType
        NxleSymbolXml = 11  # FileManagementFileTypeMemberType
        NxleSymbolPreview = 12  # FileManagementFileTypeMemberType
        Preview2d = 13  # FileManagementFileTypeMemberType
        Preview3d = 14  # FileManagementFileTypeMemberType
        QafBinary = 15  # FileManagementFileTypeMemberType
        QafText = 16  # FileManagementFileTypeMemberType
        RoutePipeRun = 17  # FileManagementFileTypeMemberType
        RoutePipeSpec = 18  # FileManagementFileTypeMemberType
        RoutePipeRunAttachment = 19  # FileManagementFileTypeMemberType
        Text = 20  # FileManagementFileTypeMemberType
        Tif = 21  # FileManagementFileTypeMemberType
        TrushapeData = 22  # FileManagementFileTypeMemberType
        ValidationRuleSet = 23  # FileManagementFileTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
        
        .. versionadded:: NX6.0.3
        
        License requirements: None.
        """
        ...
    
    
    def ImportFiles(self, itemIds: 'list[str]', itemRevisionIds: 'list[str]', datasetNames: 'list[str]', datasetTypeNames: 'list[str]', datasetRelationTypeNames: 'list[str]', importDirectoryNames: 'list[str]') -> 'list[int]':
        """
        Imports all associated files for the specified dataset(s)
        into the Teamcenter database.  
        
        The files will be attached to the
        dataset(s) as named references.  The dataset(s) are identified by
        their Teamcenter multifield key, Teamcenter item revision id, Teamcenter 
        dataset name, NX dataset type, and NX dataset relation type.  
        An import directory containing the files must be specified for each 
        dataset.  An array of PDI result codes is returned indicating the 
        success (0) or failure (non-zero) of each import.
        The dataset types for FOREIGN_MODEL are the ones included in the 
        Teamcenter preference "TC_NX_Foreign_Datasets". In such a case the 
        input relation type should be "Foreign". The named reference information
        from BMIDE setting will be used for the imported file extension.
        
          #. NX dataset types and relation names
          #. NX Model Type         NX Relation Type        NX Dataset Type
          #. MASTER_MODEL          "has shape"             "UGMASTER"
          #. SPEC_MODEL            "has specification"     "UGPART"
          #. MAN_MODEL             "has manifestation"     "UGPART"
          #. ALTREP_MODEL          "has altrep"            "UGALTREP"
          #. SCENARIO_MODEL        "UG_scenario"           "UGSCENARIO"
          #. SIMULATION_MODEL      "NX_simulation"         "NXSimulation"
          #. MOTION_MODEL          "NX_simulation"         "NXMotion"
          #. CAE_SOLN_MODEL        "NX_simulation"         "CAESolution"
          #. CAE_MESH_MODEL        "NX_simulation"         "CAEMesh"
          #. CAE_GEOM_MODEL        "NX_simulation"         "CAEGeom"
          #. FOREIGN_MODEL         "Foreign"               "*"
          #. MOTION_MODEL_SPEC     "has specification"     "MotionSim"
        
        For the input itemIds:
        In case of Default Domain: it is Teamcenter item ID.
        In case of non-Default Domain: it is the multifield key.
        e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        And the encoded part filename would be containing the MFK.
        
        Signature ``ImportFiles(itemIds, itemRevisionIds, datasetNames, datasetTypeNames, datasetRelationTypeNames, importDirectoryNames)`` 
        
        :param itemIds:  Multifield key.  
        :type itemIds: list of str 
        :param itemRevisionIds:  Teamcenter item revision ids.  
        :type itemRevisionIds: list of str 
        :param datasetNames:  Teamcenter dataset names.  
        :type datasetNames: list of str 
        :param datasetTypeNames:  NX dataset type names.  
        :type datasetTypeNames: list of str 
        :param datasetRelationTypeNames:  NX dataset relation type names.  
        :type datasetRelationTypeNames: list of str 
        :param importDirectoryNames:  Import directories which contain the files to import.  
        :type importDirectoryNames: list of str 
        :returns:  Result codes. Success (0), failure (non-zero).  
        :rtype: list of int 
        
        .. versionadded:: NX6.0.3
        
        License requirements: None.
        """
        ...
    
    
    def ExportFiles(self, itemIds: 'list[str]', itemRevisionIds: 'list[str]', datasetNames: 'list[str]', datasetTypeNames: 'list[str]', datasetRelationTypeNames: 'list[str]', baseDirectoryNames: 'list[str]', toolNames: 'list[str]') -> tuple:
        """
        Exports all associated files for the specified dataset(s)
        to a directory.  
        
        The dataset(s) are identified by their Teamcenter 
        item id, Teamcenter item revision id, Teamcenter dataset name, 
        NX dataset type, and  NX dataset relation type.  A base export directory
        name must be specified for each dataset along with the tool name that
        is requesting the export.  The full path to the exported files is 
        returned in an output array.  The full path will be 
        NX_default_directory or export_directory.  Additionally, an array of
        PDI result codes is returned indicating the success (0) or failure 
        (non-zero) of each export.
        The dataset types for FOREIGN_MODEL are the ones included in the 
        Teamcenter preference "TC_NX_Foreign_Datasets". In such a case the 
        input relation type should be "Foreign".
        The exporting of the associated file is governed by following conditions:        
        The associated filetype should be exportable for combination of the Tool 
        used and the Open action for operation.
        The associated file should not be in the excluded named reference list. 
        For Foreign Datasets it will not export file types included in the Teamcenter
        preference "TC_NX_Foreign_Datasets". NX Clone can be used for exporting Foreign datasets.
        In case of NX CAM dataset type like "UGCAMCLSF", "UGCAMPTP", "UGCAMShopDoc",
        all the associated files will be exported irrespective of above conditions.
        
          #. Excluded Named Reference List:
          #. "UGPART"             
          #. "UGPART-MASSPR            
          #. "UGPART-BBOX              
          #. "UGPART-ATTRIBUTES        
          #. "UGPART-ATTR             
          #. "Trushape-Data            
          #. "BVRSYNCINFO              
          #. "UG-QuickAccess-Binary    
          #. "UG-QuickAccess-Text   
        
          #. NX dataset types and relation names
          #. NX Model Type         NX Relation Type        NX Dataset Type
          #. MASTER_MODEL          "has shape"             "UGMASTER"
          #. SPEC_MODEL            "has specification"     "UGPART"
          #. MAN_MODEL             "has manifestation"     "UGPART"
          #. ALTREP_MODEL          "has altrep"            "UGALTREP"
          #. SCENARIO_MODEL        "UG_scenario"           "UGSCENARIO"
          #. SIMULATION_MODEL      "NX_simulation"         "NXSimulation"
          #. MOTION_MODEL          "NX_simulation"         "NXMotion"
          #. CAE_SOLN_MODEL        "NX_simulation"         "CAESolution"
          #. CAE_MESH_MODEL        "NX_simulation"         "CAEMesh"
          #. CAE_GEOM_MODEL        "NX_simulation"         "CAEGeom"
          #. FOREIGN_MODEL         "Foreign"               "*"
          #. MOTION_MODEL_SPEC     "has specification"     "MotionSim"
        
        For the input itemIds:
        In case of Default Domain: it is Teamcenter item ID.
        In case of non-Default Domain: it is the multifield key.
        e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        And the encoded part filename would be containing the MFK.
        
        Signature ``ExportFiles(itemIds, itemRevisionIds, datasetNames, datasetTypeNames, datasetRelationTypeNames, baseDirectoryNames, toolNames)`` 
        
        :param itemIds:  Multifield Key.  
        :type itemIds: list of str 
        :param itemRevisionIds:  Teamcenter item revision ids.  
        :type itemRevisionIds: list of str 
        :param datasetNames:  Teamcenter dataset names.  
        :type datasetNames: list of str 
        :param datasetTypeNames:  NX dataset type names.  
        :type datasetTypeNames: list of str 
        :param datasetRelationTypeNames:  NX dataset relation type names.  
        :type datasetRelationTypeNames: list of str 
        :param baseDirectoryNames:  Base export directory name.  
        :type baseDirectoryNames: list of str 
        :param toolNames:  Tool names ("UGII V10-ALL").  
        :type toolNames: list of str 
        :returns: a tuple 
        :rtype: A tuple consisting of (resultCodes, exportDirectoryNames). resultCodes is a list of int.   Result codes. Success (0), failure (non-zero). exportDirectoryNames is a list of str.   Resulting location of export directory 
        
        .. versionadded:: NX6.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetAssociatedFiles(self, parts: 'list[NXOpen.BasePart]', fileTypesToExclude: 'list[FileManagementFileType]') -> 'list[PdmFile]':
        """
        Given an NX part, this method will return a list of named
        reference files in the corresponding Teamcenter dataset.  
        
        Signature ``GetAssociatedFiles(parts, fileTypesToExclude)`` 
        
        :param parts: 
        :type parts: list of :py:class:`NXOpen.BasePart` 
        :param fileTypesToExclude: 
        :type fileTypesToExclude: list of :py:class:`NXOpen.PDM.FileManagementFileType` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.PdmFile` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DownloadAssociatedFiles(self, parts: 'list[NXOpen.BasePart]', files: 'list[PdmFile]') -> None:
        """
        Download the specified named reference files for NX use.  
        
        Signature ``DownloadAssociatedFiles(parts, files)`` 
        
        :param parts: 
        :type parts: list of :py:class:`NXOpen.BasePart` 
        :param files: 
        :type files: list of :py:class:`NXOpen.PDM.PdmFile` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ImportFilesAndCreateDatasets(self, itemIds: 'list[str]', itemRevisionIds: 'list[str]', datasetNames: 'list[str]', datasetTypeNames: 'list[str]', datasetRelationTypeNames: 'list[str]', datasetToolNames: 'list[str]', fileType: 'list[bool]', namedReferenceNames: 'list[str]', importFileNames: 'list[str]', importFileDirectoryNames: 'list[str]') -> 'list[int]':
        """
        Import files and create datasets in Teamcenter.  
        
        The Dataset Relation Type Names are the names of the Teamcenter relationships used to attach the Datasets
        to the correponding Item Revisions. 
        Any ImanRelation types can be used. 
        
        Signature ``ImportFilesAndCreateDatasets(itemIds, itemRevisionIds, datasetNames, datasetTypeNames, datasetRelationTypeNames, datasetToolNames, fileType, namedReferenceNames, importFileNames, importFileDirectoryNames)`` 
        
        :param itemIds:  Multifield key.  
        :type itemIds: list of str 
        :param itemRevisionIds:  Teamcenter item revision ids.  
        :type itemRevisionIds: list of str 
        :param datasetNames:  Teamcenter dataset names.  
        :type datasetNames: list of str 
        :param datasetTypeNames:  NX dataset type names.  
        :type datasetTypeNames: list of str 
        :param datasetRelationTypeNames:  Exact Teamcenter relation type names.  
        :type datasetRelationTypeNames: list of str 
        :param datasetToolNames:  NX dataset tool names. This is not currently supported. For future use only.  
        :type datasetToolNames: list of str 
        :param fileType:  Types of files - true = Binary, false = Ascii. 
        :type fileType: list of bool 
        :param namedReferenceNames:  NX dataset named reference names.  
        :type namedReferenceNames: list of str 
        :param importFileNames:  Import file names which contain the files to import per dataset.  
        :type importFileNames: list of str 
        :param importFileDirectoryNames:  Import file directory names which contain the files to import.  
        :type importFileDirectoryNames: list of str 
        :returns:  Result codes. Success (0), failure (non-zero).  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    


class EffectivityTableBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a builder class for effectivity configuration.  
    
    .. versionadded:: NX9.0.0
    """
    
    def GetEffectivityRows(self) -> 'list[EffectivityTableRow]':
        """
        Gets the existing effectivity rows from effectivity table
        
        Signature ``GetEffectivityRows()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.EffectivityTableRow` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateNewEffectivityRow(self) -> EffectivityTableRow:
        """
        Creates new effectivity row in :py:class:`NXOpen.PDM.EffectivityTableBuilder` object  
        
        Signature ``CreateNewEffectivityRow()`` 
        
        :returns:  newly created empty effectivity row  
        :rtype: :py:class:`NXOpen.PDM.EffectivityTableRow` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AddEffectivityRow(self, effectivityRow: EffectivityTableRow) -> None:
        """
        Adds the given effectivity row to :py:class:`NXOpen.PDM.EffectivityTableBuilder` 
        
        Signature ``AddEffectivityRow(effectivityRow)`` 
        
        :param effectivityRow: 
        :type effectivityRow: :py:class:`NXOpen.PDM.EffectivityTableRow` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def RemoveEffectivityRows(self, effectivityRows: 'list[EffectivityTableRow]') -> None:
        """
        Removes the given effectivity rows from :py:class:`NXOpen.PDM.EffectivityTableBuilder` 
        
        Signature ``RemoveEffectivityRows(effectivityRows)`` 
        
        :param effectivityRows:  effectivity rows to be removed 
        :type effectivityRows: list of :py:class:`NXOpen.PDM.EffectivityTableRow` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def UpdateBuilderDetails(self, cd: NXOpen.CollaborativeDesign, validationBasisFormula: str, effectivityFormulae: 'list[str]') -> None:
        """
        Updates this builder with new :py:class:`NXOpen.CollaborativeDesign`, validation basis formula and effectivity formulae to edit.  
        
        Effectivity formulae will be validated against provided validation basis formula.
        
        Signature ``UpdateBuilderDetails(cd, validationBasisFormula, effectivityFormulae)`` 
        
        :param cd: 
        :type cd: :py:class:`NXOpen.CollaborativeDesign` 
        :param validationBasisFormula: 
        :type validationBasisFormula: str 
        :param effectivityFormulae: 
        :type effectivityFormulae: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def Commit(self) -> None:
        """
        Commit the modified effectivity rows 
        
        Signature ``Commit()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
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
    
    Null: EffectivityTableBuilder = ...  # unknown typename


class ModelElementRevisionPositioningStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ModelElementRevisionPositioningStatus():
    """
    Represents the positioning status of a design element 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AbsolutelyPositioned", " - "
       "OutOfDate", " - "
       "UpToDate", " - "
       "Unknown", " - "
    """
    AbsolutelyPositioned = 0  # ModelElementRevisionPositioningStatusMemberType
    OutOfDate = 1  # ModelElementRevisionPositioningStatusMemberType
    UpToDate = 2  # ModelElementRevisionPositioningStatusMemberType
    Unknown = 3  # ModelElementRevisionPositioningStatusMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ModelElementRevision(NXOpen.NXObject, IAttributeGroupOwner):
    """
    Represents a base class that provides common methods for various model elements in a :py:class:`NXOpen.CollaborativeDesign`.  
    
    Instance of this class can not be created
    
    .. versionadded:: NX9.0.0
    """
    
    class PositioningStatus():
        """
        Represents the positioning status of a design element 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AbsolutelyPositioned", " - "
           "OutOfDate", " - "
           "UpToDate", " - "
           "Unknown", " - "
        """
        AbsolutelyPositioned = 0  # ModelElementRevisionPositioningStatusMemberType
        OutOfDate = 1  # ModelElementRevisionPositioningStatusMemberType
        UpToDate = 2  # ModelElementRevisionPositioningStatusMemberType
        Unknown = 3  # ModelElementRevisionPositioningStatusMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetMemberPartitions(self) -> 'list[NXOpen.Assemblies.Partition]':
        """
        Get all the partitions of this model element revision.  
        
        Signature ``GetMemberPartitions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOverridePart(self) -> NXOpen.Part:
        """
        Get the override part of this model element revision if it has any.  
        
        Signature ``GetOverridePart()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsExcludedFromSpatialSearch(self) -> bool:
        """
        Determines whether this model element revision is excluded from spatial search.  
        
        Signature ``IsExcludedFromSpatialSearch()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetExcludeFromSpatialSearch(self, excludeFromSpatialSearch: bool) -> None:
        """
        Set or unset this model element revision from exclusion from spatial search.  
        
        Signature ``SetExcludeFromSpatialSearch(excludeFromSpatialSearch)`` 
        
        :param excludeFromSpatialSearch: 
        :type excludeFromSpatialSearch: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPositionStatus(self) -> ModelElementRevisionPositioningStatus:
        """
        Gets positioning status of design element.  
        
        It returns absolute position if design element is absolutely positioned, 
        up-to-date if design element is in work collection of positioning task, 
        out-of-date if design element is in context collection of positioning task and 
        unknown if design element is not in any of the above.
        Return status will be one of :py:class:`NXOpen.PDM.ModelElementRevisionPositioningStatus`.
        
        Signature ``GetPositionStatus()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.ModelElementRevisionPositioningStatus` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def IsAbsolutelyPositioned(self) -> bool:
        """
        Determine whether this design element is absolutely positioned or not.  
        
        Signature ``IsAbsolutelyPositioned()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPositioningGroups(self) -> 'list[NXOpen.Assemblies.PositioningGroup]':
        """
        Gets all positioning group which are associated with this design element.  
        
        Signature ``GetPositioningGroups()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.PositioningGroup` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def IsMemberOfPositioningGroup(self) -> bool:
        """
        Determine whether this design element is part of positioning group or not.  
        
        Signature ``IsMemberOfPositioningGroup()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Create(self, attributeGroupDescription: AttributeGroupDescription) -> AttributeGroup:
        """
        Creates an attribute group for a :py:class:`NXOpen.PDM.IAttributeGroupOwner`, based on an attribute
        group type.  
        
        An attribute group type is represented by an :py:class:`NXOpen.PDM.AttributeGroupDescription`.
        
        Signature ``Create(attributeGroupDescription)`` 
        
        :param attributeGroupDescription: 
        :type attributeGroupDescription: :py:class:`NXOpen.PDM.AttributeGroupDescription` 
        :returns:  The new attribute group.  
        :rtype: :py:class:`NXOpen.PDM.AttributeGroup` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateAttributeGroupReviseBuilder(self, attributeGroups: 'list[AttributeGroup]') -> AttributeGroupReviseBuilder:
        """
        Creates a :py:class:`NXOpen.PDM.AttributeGroupReviseBuilder` object.  The builder creates a
        revision for each attribute group in the input list of existing attribute groups.  
        
        Signature ``CreateAttributeGroupReviseBuilder(attributeGroups)`` 
        
        :param attributeGroups: 
        :type attributeGroups: list of :py:class:`NXOpen.PDM.AttributeGroup` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.AttributeGroupReviseBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateAttributeGroupReviseBuilder(self, attributeGroups: 'list[AttributeGroup]', keepOriginal: bool, saveAsActionType: AttributeGroupReviseBuilderSaveAsActionType) -> AttributeGroupReviseBuilder:
        """
        The builder will do a revise or save-as operation for each attribute group in the input list of existing attribute groups 
        depending on input operation type.  
        
        Signature ``CreateAttributeGroupReviseBuilder(attributeGroups, keepOriginal, saveAsActionType)`` 
        
        :param attributeGroups: 
        :type attributeGroups: list of :py:class:`NXOpen.PDM.AttributeGroup` 
        :param keepOriginal: 
        :type keepOriginal: bool 
        :param saveAsActionType: 
        :type saveAsActionType: :py:class:`NXOpen.PDM.AttributeGroupReviseBuilderSaveAsActionType` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.AttributeGroupReviseBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAttributeGroups(self) -> 'list[AttributeGroup]':
        """
        Returns the :py:class:`NXOpen.PDM.AttributeGroup` objects owned by this object.  
        
        Signature ``GetAttributeGroups()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.AttributeGroup` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAttributeGroupDescriptions(self) -> 'list[AttributeGroupDescription]':
        """
        Returns the :py:class:`NXOpen.PDM.AttributeGroupDescription` objects representing the attribute
        group types supported by this object.  
        
        Signature ``GetAttributeGroupDescriptions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.AttributeGroupDescription` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    EffectivityFormula: str = ...
    """
    Returns  the formula string that represents the effectivity of this object in database.  
    
    <hr>
    
    Getter Method
    
    Signature ``EffectivityFormula`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    OwningCollaborativeDesign: NXOpen.CollaborativeDesign = ...
    """
    Returns  the owning :py:class:`NXOpen.CollaborativeDesign`.  
    
    <hr>
    
    Getter Method
    
    Signature ``OwningCollaborativeDesign`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CollaborativeDesign` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: ModelElementRevision = ...  # unknown typename


class DesignFeatureRevision(ModelElementRevision):
    """
    Represents the design feature revision in the database.  
    
    Instance of this class can not be created
    
    .. versionadded:: NX9.0.0
    """
    Null: DesignFeatureRevision = ...  # unknown typename


class DesignElementRevisionDesignElementCategoryMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignElementRevisionDesignElementCategory():
    """
    Represents the category for this design element revision.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Shape", " - "
       "Reuse", " - "
       "Promissory", " - "
       "DesignControlElement", " - "
    """
    Shape = 0  # DesignElementRevisionDesignElementCategoryMemberType
    Reuse = 1  # DesignElementRevisionDesignElementCategoryMemberType
    Promissory = 2  # DesignElementRevisionDesignElementCategoryMemberType
    DesignControlElement = 3  # DesignElementRevisionDesignElementCategoryMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DesignElementRevision(ModelElementRevision):
    """
    Represents the design element revision in the database.  
    
    An instance of this class can be obtained from the :py:class:`NXOpen.Assemblies.Component`.
    
    Instance of this class can not be created
    
    .. versionadded:: NX8.5.0
    """
    
    class DesignElementCategory():
        """
        Represents the category for this design element revision.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Shape", " - "
           "Reuse", " - "
           "Promissory", " - "
           "DesignControlElement", " - "
        """
        Shape = 0  # DesignElementRevisionDesignElementCategoryMemberType
        Reuse = 1  # DesignElementRevisionDesignElementCategoryMemberType
        Promissory = 2  # DesignElementRevisionDesignElementCategoryMemberType
        DesignControlElement = 3  # DesignElementRevisionDesignElementCategoryMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetTransform(self) -> tuple:
        """
        Get the transform.  
        
        Note: The translation component is in meters.
        
        Signature ``GetTransform()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (orientation, positionInMeters). orientation is a :py:class:`NXOpen.Matrix3x3`. positionInMeters is a :py:class:`NXOpen.Point3d`. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDesignSubordinateRevisions(self) -> 'list[DesignSubordinateRevision]':
        """
        Get the immediate child :py:class:`NXOpen.PDM.DesignSubordinateRevision` objects.  
        
        This will return None.for non subordinate design element.
        
        Signature ``GetDesignSubordinateRevisions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.DesignSubordinateRevision` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    Category: DesignElementRevisionDesignElementCategory = ...
    """
    Returns  the category for design element.  
    
    Category can be unknown 
    if the design element is new and does not yet exist in database.
    
    <hr>
    
    Getter Method
    
    Signature ``Category`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.DesignElementRevisionDesignElementCategory` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DesignPart: NXOpen.Part = ...
    """
    Returns  the part of the underlying design element.  
    
    This can be None for a promissory design element.
    
    <hr>
    
    Getter Method
    
    Signature ``DesignPart`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Modified: bool = ...
    """
    Returns 
    whether the selected :py:class:`NXOpen.PDM.DesignElementRevision` is modified in the session.  
    
    <hr>
    
    Getter Method
    
    Signature ``Modified`` 
    
    :returns:  Whether the selected :py:class:`NXOpen.PDM.DesignElementRevision` is modified 
    in the session. 
    :rtype: bool 
    
    .. versionadded:: NX8.5.3
    
    License requirements: None.
    """
    Null: DesignElementRevision = ...  # unknown typename


class RequirementUtils():
    """
    Collection of PDM utility methods   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX6.0.3
    """
    
    def NewTracelinkQuery(self) -> TracelinkQuery:
        """
        Returns a Tracelink query object  
        
        Signature ``NewTracelinkQuery()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.TracelinkQuery` 
        
        .. versionadded:: NX6.0.3
        
        License requirements: None.
        """
        ...
    
    
    def CreateTraceLinks(self, requirementItemNumbers: 'list[str]', requirementRevisions: 'list[str]', parts: 'list[str]') -> None:
        """
        Creates Trace Links from :py:class:`NXOpen.Validate.Requirement`s to :py:class:`NXOpen.Part`s
        For the input requirement_item_numbers:
        In case of Default Domain: it is Teamcenter item ID.  
        
        In case of non-Default Domain: it is the multifield key.
        e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        And the encoded part filename would be containing the MFK.
        
        Signature ``CreateTraceLinks(requirementItemNumbers, requirementRevisions, parts)`` 
        
        :param requirementItemNumbers:  requirement multifield key  
        :type requirementItemNumbers: list of str 
        :param requirementRevisions:  requirement item revisions. Must be same size as the item number array  
        :type requirementRevisions: list of str 
        :param parts:  part CLI names  
        :type parts: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveTraceLinks(self, requirementItemNumbers: 'list[str]', requirementRevisions: 'list[str]', parts: 'list[str]') -> None:
        """
        Removes Trace Links between :py:class:`NXOpen.Validate.Requirement`s and :py:class:`NXOpen.Part`s
        For the input requirement_item_numbers:
        In case of Default Domain: it is Teamcenter item ID.  
        
        In case of non-Default Domain: it is the multifield key.
        e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        And the encoded part filename would be containing the MFK.
        
        Signature ``RemoveTraceLinks(requirementItemNumbers, requirementRevisions, parts)`` 
        
        :param requirementItemNumbers:  requirement multifield Key  
        :type requirementItemNumbers: list of str 
        :param requirementRevisions:  requirement item revisions. Must be same size as the item number array  
        :type requirementRevisions: list of str 
        :param parts:  part CLI names  
        :type parts: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    


class GenericObjectAttributeHolder(NXOpen.NXObject):
    """
    Represents the class that contains database business logic or pre-creation information for the objects.  
    
    Instances of this class can be accessed through various application specific builders
    
    .. versionadded:: NX10.0.0
    """
    Null: GenericObjectAttributeHolder = ...  # unknown typename


class ObjectCreateBuilder(NXOpen.Builder, NXOpen.IAttributeSourceObjectBuilder):
    """
    Represents a builder class that perofrms create operation  
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreateObjectCreateBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def SetTypes(self, tcTypes: 'list[str]', baseTCTypes: 'list[str]') -> None:
        """
        Set Types for which AttributeHolderObject needs to be created.  
        
        This method will remove all previously set types.
        
        Signature ``SetTypes(tcTypes, baseTCTypes)`` 
        
        :param tcTypes: 
        :type tcTypes: list of str 
        :param baseTCTypes: 
        :type baseTCTypes: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateLogicalObjects(self) -> 'list[LogicalObject]':
        """
        Creates Pre-Creation LogicalObjects 
        
        Signature ``CreateLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAttributeHolderObjects(self) -> 'list[GenericObjectAttributeHolder]':
        """
        Returns an array of AttributeHolderObjects created as part of commit.  
        
        Signature ``GetAttributeHolderObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.GenericObjectAttributeHolder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributes(self, objects: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given array of objects and returns an array of objects that failed to auto assign.  
        
        Signature ``AutoAssignAttributes(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributesWithNamingPattern(self, objects: 'list[NXOpen.NXObject]', properties: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given object and returns an array of objects that failed to auto assign.  
        
        properties needs to be created using :py:meth:`CreateAttributeTitleToNamingPatternMap`
        
        Signature ``AutoAssignAttributesWithNamingPattern(objects, properties)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :param properties: 
        :type properties: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: 'list[str]', titlePatterns: 'list[str]') -> NXOpen.NXObject:
        """
        Creates a map object of attribute titles to their corresponding naming pattern  
        
        Signature ``CreateAttributeTitleToNamingPatternMap(attributeTitles, titlePatterns)`` 
        
        :param attributeTitles: 
        :type attributeTitles: list of str 
        :param titlePatterns: 
        :type titlePatterns: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    DefaultDestinationFolder: str = ...
    """
    Returns or sets  the default destination folder string for the object being created.  
    
    The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
    In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultDestinationFolder`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultDestinationFolder`` 
    
    :param defaultDestinationFolder: 
    :type defaultDestinationFolder: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: ObjectCreateBuilder = ...  # unknown typename


class PartOperationImportCallbackData(NXOpen.TaggedObject):
    """
    JA interface for PartOperationImportCallbackData object   
    
    This cannot be created
    
    .. versionadded:: NX10.0.0
    """
    
    def GetLogicalObjects(self) -> 'list[NativePartLogicalObject]':
        """
        Gets the logical objects for parts participating in import operation 
        
        Signature ``GetLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.NativePartLogicalObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    ImportBuilder: PartOperationImportBuilder = ...
    """
    Returns  the :py:class:`NXOpen.PDM.PartOperationImportBuilder` builder used in this operation 
    
    <hr>
    
    Getter Method
    
    Signature ``ImportBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: PartOperationImportCallbackData = ...  # unknown typename


class ListOfValues(NXOpen.TransientObject):
    """
    Represents list of values to be used in search query   
    
    .. versionadded:: NX6.0.0
    """
    
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
    


class AttributeGroupDescription(NXOpen.NXObject):
    """
    Represents an attribute group type.  
    
    PDM.AttributeGroupDescription object cannot be created.
    
    .. versionadded:: NX9.0.0
    """
    DisplayName: str = ...
    """
    Returns  the display name for the attribute group description.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    MaximumNumberOfAttributeGroupsAllowed: int = ...
    """
    Returns  the maximum number of attribute groups of this type that can be assigned to an object.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumNumberOfAttributeGroupsAllowed`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    MinimumNumberOfAttributeGroupsAllowed: int = ...
    """
    Returns  the minimum number of attribute groups of this type that can be assigned to an object.  
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumNumberOfAttributeGroupsAllowed`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: AttributeGroupDescription = ...  # unknown typename


class ConfigurationManager():
    """
    Represents Configuration Manager    
    
    Use :py:meth:`NXOpen.Session.ConfigurationManager` to get the instance of this class.
    
    .. versionadded:: NX9.0.0
    """
    
    def CreateConfigurationContextBuilder(self) -> ConfigurationContextBuilder:
        """
        Creates a new :py:class:`NXOpen.PDM.ConfigurationContextBuilder` object for 
        :py:class:` NXOpen.PDM.ConfigurationContextBuilderConfigContextMode.Assemblies  < NXOpen.PDM.ConfigurationContextBuilderConfigContextMode>`
        mode configuration.  
        
        Signature ``CreateConfigurationContextBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.ConfigurationContextBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateEffectivityAttributePropertiesBuilder(self, part: NXOpen.BasePart, objects: 'list[NXOpen.NXObject]') -> EffectivityAttributePropertiesBuilder:
        """
        Creates a new :py:class:`NXOpen.PDM.EffectivityAttributePropertiesBuilder` object.  
        
        Signature ``CreateEffectivityAttributePropertiesBuilder(part, objects)`` 
        
        :param part:  The part that owns the builder. The builder owner is not                                                    strictly required (that is, it can be None), but it is                                                    highly suggested to ensure proper cleanup of the builder in                                                    case the client does not explicitly clean it up properly.   
        :type part: :py:class:`NXOpen.BasePart` 
        :param objects:  the array of objects  
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.EffectivityAttributePropertiesBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    


class OperationErrors(NXOpen.TransientObject):
    """
    Represents Operation Errors to be returned in TCIN related operations   
    
    .. versionadded:: NX8.5.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    


class PartOperationCopyBuilderCopyNonMasterPartsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationCopyBuilderCopyNonMasterParts():
    """
    This enum is used to specify which non-master parts 
    should be copied to new part during the save as operation.   
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX11.0.0
       Use :py:class:`NXOpen.PDM.NonMasterDataCopyNonMasterPartsOption` instead
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", "save all during save as"
       "NotSet", "save none during save as"
    """
    All = 0  # PartOperationCopyBuilderCopyNonMasterPartsMemberType
    NotSet = 1  # PartOperationCopyBuilderCopyNonMasterPartsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationCopyBuilderCopyDependentFilesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationCopyBuilderCopyDependentFiles():
    """
    This enum is used to specify which dependent files
    should be copied to new part during the save as operation.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", "save all during save as"
       "NotSet", "save none during save as"
    """
    All = 0  # PartOperationCopyBuilderCopyDependentFilesMemberType
    NotSet = 1  # PartOperationCopyBuilderCopyDependentFilesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationCopyBuilderOperationSubTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationCopyBuilderOperationSubType():
    """
    Represents an operation sub type for copying a part 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Default", "Save As dialog"
       "MakeUnique", "MakeUnique flavour of Save As dialog"
    """
    Default = 0  # PartOperationCopyBuilderOperationSubTypeMemberType
    MakeUnique = 1  # PartOperationCopyBuilderOperationSubTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationCopyBuilder(PartOperationBuilder):
    """
    Represents a builder class that performs various Save As operations.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreateCopyOperationBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    class CopyNonMasterParts():
        """
        This enum is used to specify which non-master parts 
        should be copied to new part during the save as operation.   
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:class:`NXOpen.PDM.NonMasterDataCopyNonMasterPartsOption` instead
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", "save all during save as"
           "NotSet", "save none during save as"
        """
        All = 0  # PartOperationCopyBuilderCopyNonMasterPartsMemberType
        NotSet = 1  # PartOperationCopyBuilderCopyNonMasterPartsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CopyDependentFiles():
        """
        This enum is used to specify which dependent files
        should be copied to new part during the save as operation.   
        
        .. versionadded:: NX10.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", "save all during save as"
           "NotSet", "save none during save as"
        """
        All = 0  # PartOperationCopyBuilderCopyDependentFilesMemberType
        NotSet = 1  # PartOperationCopyBuilderCopyDependentFilesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OperationSubType():
        """
        Represents an operation sub type for copying a part 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Default", "Save As dialog"
           "MakeUnique", "MakeUnique flavour of Save As dialog"
        """
        Default = 0  # PartOperationCopyBuilderOperationSubTypeMemberType
        MakeUnique = 1  # PartOperationCopyBuilderOperationSubTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetSelectedPartsToCopy(self, selectedParts: 'list[NXOpen.BasePart]') -> 'list[NXOpen.BasePart]':
        """
        Sets the selected parts.  
        
        Applicable only for operation types
        :py:class:`PartOperationBuilderOperationType.SaveAs <PartOperationBuilderOperationType>` and 
        :py:class:`PartOperationBuilderOperationType.Revise <PartOperationBuilderOperationType>`
        Also returns an array of parts failed to added, these are not removed from the input array though.
        :py:meth:`NXOpen.PDM.PartOperationBuilder.GetOperationFailures` can be called to get the errors occurred
        during this operation.
        
        Signature ``SetSelectedPartsToCopy(selectedParts)`` 
        
        :param selectedParts: 
        :type selectedParts: list of :py:class:`NXOpen.BasePart` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddRelatedPartsToCopy(self, basePart: NXOpen.BasePart, relatedParts: 'list[NXOpen.BasePart]', relatedPartsReasons: 'list[str]', operation: PartOperationBuilderOperationType) -> None:
        """
        Add related part to the part undergoing an operation.  
        
        Example: if user selects a part
        for Save As which has Linked Part Modules that should also undergo Save As, they should
        be added as related parts.
        Applicable only for operation types 
        :py:class:`PartOperationBuilderOperationType.SaveAs <PartOperationBuilderOperationType>` and 
        :py:class:`PartOperationBuilderOperationType.Revise <PartOperationBuilderOperationType>`
        
        Signature ``AddRelatedPartsToCopy(basePart, relatedParts, relatedPartsReasons, operation)`` 
        
        :param basePart: 
        :type basePart: :py:class:`NXOpen.BasePart` 
        :param relatedParts: 
        :type relatedParts: list of :py:class:`NXOpen.BasePart` 
        :param relatedPartsReasons: 
        :type relatedPartsReasons: list of str 
        :param operation: 
        :type operation: :py:class:`NXOpen.PDM.PartOperationBuilderOperationType` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateNonMasterListForCopyLogicalObject(self, logicalObject: LogicalObject) -> None:
        """
        Create NonMaster list for the selected logical Object 
        
        Signature ``CreateNonMasterListForCopyLogicalObject(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.PDM.NonMasterData.CreateNonMasterListForLogicalObject` instead
        
        License requirements: None.
        """
        ...
    
    
    def GetNonMasterListForCopyLogicalObject(self, logicalObject: LogicalObject) -> 'list[str]':
        """
        Gets NonMaster list for the given logical Object  
        
        Signature ``GetNonMasterListForCopyLogicalObject(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :returns:  Non-master part file names  
        :rtype: list of str 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.PDM.NonMasterData.GetNonMasterListForCopyLogicalObject` instead
        
        License requirements: None.
        """
        ...
    
    
    def IsNonMasterForLogicalObjectBeingCopied(self, logicalObject: LogicalObject, partName: str) -> bool:
        """
        Returns whether or not the non-master part specified for the given :py:class:`NXOpen.PDM.LogicalObject`will actually
        get saved during the save as operation.  
        
        Signature ``IsNonMasterForLogicalObjectBeingCopied(logicalObject, partName)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param partName:  the non-master part that the caller wants to save or not save  
        :type partName: str 
        :returns:  True means that this non-master will be saved.
        False means that this non-master will not be saved.  
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.PDM.NonMasterData.IsNonMasterForLogicalObjectBeingCopied` instead
        
        License requirements: None.
        """
        ...
    
    
    def GetCopyNonMasterPartsOption(self, logicalObject: LogicalObject) -> PartOperationCopyBuilderCopyNonMasterParts:
        """
        Get the nonmasters saveAs option for given logical object.  
        
        Save As option can be one of these
        :py:class:`PartOperationCopyBuilderCopyNonMasterParts.All <PartOperationCopyBuilderCopyNonMasterParts>` and 
        :py:class:`PartOperationCopyBuilderCopyNonMasterParts.None <PartOperationCopyBuilderCopyNonMasterParts>` 
        
        Signature ``GetCopyNonMasterPartsOption(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationCopyBuilderCopyNonMasterParts` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.PDM.NonMasterData.GetCopyNonMasterPartsOption` instead
        
        License requirements: None.
        """
        ...
    
    
    def SetCopyNonMasterPartsOption(self, logicalObject: LogicalObject, saveOption: PartOperationCopyBuilderCopyNonMasterParts) -> None:
        """
        Set the nonmasters saveAs option for given logical object.  
        
        Save As option can be one of these
        :py:class:`PartOperationCopyBuilderCopyNonMasterParts.All <PartOperationCopyBuilderCopyNonMasterParts>` and 
        :py:class:`PartOperationCopyBuilderCopyNonMasterParts.None <PartOperationCopyBuilderCopyNonMasterParts>`
        
        Signature ``SetCopyNonMasterPartsOption(logicalObject, saveOption)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param saveOption: 
        :type saveOption: :py:class:`NXOpen.PDM.PartOperationCopyBuilderCopyNonMasterParts` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.PDM.NonMasterData.SetNonMasterSaveAsOption` instead
        
        License requirements: None.
        """
        ...
    
    
    def SetSelectedNonMasterToCopy(self, logicalObject: LogicalObject, partName: str) -> None:
        """
        Sets whether or not the non-master part specified will actually
        get saved during the save as operation.  
        
        True means that it will be
        saved. False means that it will not be saved.  
        
        Signature ``SetSelectedNonMasterToCopy(logicalObject, partName)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param partName:  the non-master part whose save option is being set here  
        :type partName: str 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.PDM.NonMasterData.SetSelectedNonMasterToCopy` instead
        
        License requirements: None.
        """
        ...
    
    
    def EditNonMasterToCopyName(self, logicalObject: LogicalObject, oldName: str, newName: str) -> bool:
        """
        Sets the name the non-master part will get saved as.  
        
        It will get saved as the
        original non-master name if this method is not called.  
        
        Signature ``EditNonMasterToCopyName(logicalObject, oldName, newName)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param oldName:  the non-master part whose save as name is being set here  
        :type oldName: str 
        :param newName:  the new name  
        :type newName: str 
        :returns:  flag to indicate whether the newName is valid  
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.PDM.NonMasterData.EditNonMasterToCopyName` instead
        
        License requirements: None.
        """
        ...
    
    
    def GetOperationSubType(self) -> PartOperationCopyBuilderOperationSubType:
        """
        Returns the :py:class:`NXOpen.PDM.PartOperationCopyBuilderOperationSubType` for Create.  
        
        Signature ``GetOperationSubType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationCopyBuilderOperationSubType` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOperationSubType(self, operationSubType: PartOperationCopyBuilderOperationSubType) -> None:
        """
        Sets the :py:class:`NXOpen.PDM.PartOperationCopyBuilderOperationSubType` for Create.  
        
        Signature ``SetOperationSubType(operationSubType)`` 
        
        :param operationSubType: 
        :type operationSubType: :py:class:`NXOpen.PDM.PartOperationCopyBuilderOperationSubType` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    DependentFilesToCopyOption: PartOperationCopyBuilderCopyDependentFiles = ...
    """
    Returns or sets  the Dependent files Save As option.  
    
    Save As option can be one of these
    :py:class:`PartOperationCopyBuilderCopyDependentFiles.All <PartOperationCopyBuilderCopyDependentFiles>` and 
    :py:class:`PartOperationCopyBuilderCopyDependentFiles.None <PartOperationCopyBuilderCopyDependentFiles>`
    
    <hr>
    
    Getter Method
    
    Signature ``DependentFilesToCopyOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartOperationCopyBuilderCopyDependentFiles` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DependentFilesToCopyOption`` 
    
    :param saveOption: 
    :type saveOption: :py:class:`NXOpen.PDM.PartOperationCopyBuilderCopyDependentFiles` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ReplaceAllComponentsInSession: bool = ...
    """
    Returns or sets  the replace all components.  
    
    This option specifies whether part will be replaced or copied.             
    Applicable only for operation types 
    :py:class:`PartOperationBuilderOperationType.SaveAs <PartOperationBuilderOperationType>` and 
    :py:class:`PartOperationBuilderOperationType.Revise <PartOperationBuilderOperationType>`
    
    <hr>
    
    Getter Method
    
    Signature ``ReplaceAllComponentsInSession`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReplaceAllComponentsInSession`` 
    
    :param replaceAllComponents: 
    :type replaceAllComponents: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: PartOperationCopyBuilder = ...  # unknown typename


class PartOperationMakeUniqueBuilder(PartOperationCopyBuilder):
    """
    Represents a :py:class:`NXOpen.PDM.PartOperationMakeUniqueBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreateMakeUniqueOperationBuilder`
    
    .. versionadded:: NX10.0.0
    """
    SelectedComponents: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the selected components to be made unique are returned.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedComponents`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: PartOperationMakeUniqueBuilder = ...  # unknown typename


class EffectivityAttributePropertiesBuilder(NXOpen.Builder):
    """
    Represents an :py:class:`NXOpen.PDM.EffectivityAttributePropertiesBuilder` to be used for creating effectivity attributes.  
    
    The attribute will be distributed to all objects supplied in the selected object list.
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.ConfigurationManager.CreateEffectivityAttributePropertiesBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    def Delete(self, object: NXOpen.NXObject) -> None:
        """
        Delete the attribute from the given object.  
        
        Signature ``Delete(object)`` 
        
        :param object:  The object containing the attribute  
        :type object: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateAttribute(self) -> bool:
        """
        Create the attribute from the data set in the builder.  
        
        Unlike calling commit,
        this method will not perform an update.   
        
        Signature ``CreateAttribute()`` 
        
        :returns:  True if the attribute was created/edited successfully  
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetAttributeObjects(self, objects: 'list[NXOpen.NXObject]') -> None:
        """
        Sets the array of objects that have this attribute 
        
        Signature ``SetAttributeObjects(objects)`` 
        
        :param objects:  the array of objects  
        :type objects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    Category: str = ...
    """
    Returns or sets  the category.  
    
    The category is an optional, user-defined string that allows 
    attributes to be grouped together. 
    
    <hr>
    
    Getter Method
    
    Signature ``Category`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Category`` 
    
    :param category: 
    :type category: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    DisplayValue: str = ...
    """
    Returns or sets  the display value.  
    
    Required if creating an attribute of type String. 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayValue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayValue`` 
    
    :param displayValue: 
    :type displayValue: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    EffectivityTableBuilder: EffectivityTableBuilder = ...
    """
    Returns  the effectivity table builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``EffectivityTableBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.EffectivityTableBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    SelectedObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the selected object(s) list.  
    
    The created attribute will be applied to
    all objects in this list.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    StringValue: str = ...
    """
    Returns or sets  the string value.  
    
    Required if creating an attribute of type String. 
    
    <hr>
    
    Getter Method
    
    Signature ``StringValue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``StringValue`` 
    
    :param stringValue: 
    :type stringValue: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Title: str = ...
    """
    Returns or sets  the attribute title.  
    
    The title is required for creating an attribute
    and must be unique on the given object.  Once the attribute is created,
    the title cannot be modified. 
    
    <hr>
    
    Getter Method
    
    Signature ``Title`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Title`` 
    
    :param title: 
    :type title: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: EffectivityAttributePropertiesBuilder = ...  # unknown typename


class SessionSettings(NXOpen.TransientObject):
    """
    Values for the settings that affect the current Teamcenter session.  
    
    Any changes will only
    take effect when :py:meth:`PDM.SessionSettings.Apply` is callsed. 
    
    .. versionadded:: NX4.0.0
    """
    
    def GetGroups(self) -> 'list[str]':
        """
        Gets the names of the Teamcenter groups to which the
        user belongs.  
        
        Signature ``GetGroups()`` 
        
        :returns:  the names of the groups  
        :rtype: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRoles(self) -> 'list[str]':
        """
        Gets the names of the Teamcenter roles in which the
        user may act, given the current group returned by :py:meth:`PDM.SessionSettings.Group`.  
        
        Signature ``GetRoles()`` 
        
        :returns:  the names of the roles  
        :rtype: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetVolumes(self) -> 'list[str]':
        """
        Gets the names of the Teamcenter volumes which the
        user may use, given the current group returned by :py:meth:`PDM.SessionSettings.Group`.  
        
        Signature ``GetVolumes()`` 
        
        :returns:  the names of the volumes  
        :rtype: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLocalVolumes(self) -> 'list[str]':
        """
        Gets the names of the Teamcenter local volumes which the user may use,
        given the current group returned by :py:meth:`PDM.SessionSettings.Group`.  
        
        Signature ``GetLocalVolumes()`` 
        
        :returns:  the names of the local volumes  
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLocationCodes(self) -> 'list[str]':
        """
        Gets the names of the Teamcenter location codes which the user may use, 
        given the current group returned by :py:meth:`PDM.SessionSettings.Group`.  
        
        Signature ``GetLocationCodes()`` 
        
        :returns:  the names of the location codes  
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetProjects(self) -> 'list[str]':
        """
        Gets the names of the Teamcenter projects to which the user belongs also
        the first entry of the returned projects list is always empty.  
        
        Signature ``GetProjects()`` 
        
        :returns:  the names of the projects  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def Apply(self) -> None:
        """
        Applies any changes to the settings 
        
        Signature ``Apply()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DumpValidationInfo(self, logFileName: str) -> None:
        """
        Dump the validation info .  
        
        This API can be used to expose the current state from the 
        UGMGR session, typically the information about the session,assembly,components,their states
        etc. 
        
        Signature ``DumpValidationInfo(logFileName)`` 
        
        :param logFileName:  log file name  
        :type logFileName: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    AdministrationBypass: bool = ...
    """
    Returns or sets  a flag controlling the Teamcenter administrator's bypass option.  
    
    Only available to administrators. 
    
    <hr>
    
    Getter Method
    
    Signature ``AdministrationBypass`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdministrationBypass`` 
    
    :param adminBypassOn: 
    :type adminBypassOn: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    AdministrationLogging: bool = ...
    """
    Returns or sets  a flag controlling Teamcenter administration logging.  
    
    Only available to administrators. 
    
    <hr>
    
    Getter Method
    
    Signature ``AdministrationLogging`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AdministrationLogging`` 
    
    :param adminLoggingOn: 
    :type adminLoggingOn: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    ApplicationLogging: bool = ...
    """
    Returns or sets  a flag controlling Teamcenter application logging 
    
    <hr>
    
    Getter Method
    
    Signature ``ApplicationLogging`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ApplicationLogging`` 
    
    :param appLoggingOn: 
    :type appLoggingOn: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    Group: str = ...
    """
    Returns or sets  the Teamcenter group in which the user acts.  
    
    Should be
    one of those given by :py:meth:`PDM.SessionSettings.GetGroups`
    
    <hr>
    
    Getter Method
    
    Signature ``Group`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Group`` 
    
    :param group: 
    :type group: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    IsAdministrator: bool = ...
    """
    Returns  a flag indicating if the user has Teamcenter administator privileges.  
    
    Some
    settings can are only available to administrators, and will raise errors
    if non-administrators try to access them.
    
    <hr>
    
    Getter Method
    
    Signature ``IsAdministrator`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    Journaling: bool = ...
    """
    Returns or sets  a flag controlling Teamcenter journaling 
    
    <hr>
    
    Getter Method
    
    Signature ``Journaling`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Journaling`` 
    
    :param journalingOn: 
    :type journalingOn: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    LocalVolume: str = ...
    """
    Returns or sets  the Teamcenter local volume.  
    
    Should be
    one of those given by :py:meth:`PDM.SessionSettings.GetLocalVolumes`
    
    <hr>
    
    Getter Method
    
    Signature ``LocalVolume`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LocalVolume`` 
    
    :param localvolume: 
    :type localvolume: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LocationCode: str = ...
    """
    Returns or sets  the Teamcenter location code.  
    
    Should be
    one of those given by :py:meth:`PDM.SessionSettings.GetLocationCodes`
    
    <hr>
    
    Getter Method
    
    Signature ``LocationCode`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LocationCode`` 
    
    :param locationCode: 
    :type locationCode: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Project: str = ...
    """
    Returns or sets  the Teamcenter project in which the user acts.  
    
    Should be
    one of those given by :py:meth:`PDM.SessionSettings.GetProjects`
    
    <hr>
    
    Getter Method
    
    Signature ``Project`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Project`` 
    
    :param project: 
    :type project: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Role: str = ...
    """
    Returns or sets  the Teamcenter role in which the user acts.  
    
    Should be
    one of those given by :py:meth:`PDM.SessionSettings.GetRoles`
    
    <hr>
    
    Getter Method
    
    Signature ``Role`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Role`` 
    
    :param role: 
    :type role: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    SecurityLogging: bool = ...
    """
    Returns or sets  a flag controlling Teamcenter security logging.  
    
    Only available to administrators. 
    
    <hr>
    
    Getter Method
    
    Signature ``SecurityLogging`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecurityLogging`` 
    
    :param securityLoggingOn: 
    :type securityLoggingOn: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    Volume: str = ...
    """
    Returns or sets  the Teamcenter role in which the user acts.  
    
    Should be
    one of those given by :py:meth:`PDM.SessionSettings.GetVolumes`
    
    <hr>
    
    Getter Method
    
    Signature ``Volume`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Volume`` 
    
    :param volume: 
    :type volume: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """


class AlternateIdManagerAssignAlternateRevData_Struct():
    """
    Contains alternate Revision Id data .  
    
    Constructor: 
    NXOpen.PDM.AlternateIdManager.AssignAlternateRevData()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    AlternateRevId: str = ...
    """
    the new value the alternate Revision ID  
    <hr>
    
    Field Value
    Type:str
    """
    Modifiable: bool = ...
    """
    the new value of flag for revision modifiable 
    <hr>
    
    Field Value
    Type:bool
    """


class AlternateIdManager(NXOpen.TransientObject):
    """
    This class is responsible for setting and getting NX Manager database attribute.  
    
    Use :py:meth:`PDM.PartBuilder.NewAlternateIdManager` to get the instance of this class.
    
    .. versionadded:: NX4.0.0
    """
    
    class AlternateIdsData():
        """
        Contains alternate Ids data .  
        
        Constructor: 
        NXOpen.PDM.AlternateIdManager.AlternateIdsData()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        AlternateItemId: str = ...
        """
        the new value for the alternate item ID  
        <hr>
        
        Field Value
        Type:str
        """
        AlternateRevId: str = ...
        """
        the new value for the alternate Revision ID
        <hr>
        
        Field Value
        Type:str
        """
        AlternateName: str = ...
        """
        the new value for the alternate Name
        <hr>
        
        Field Value
        Type:str
        """
        AlternateDescription: str = ...
        """
        the new value for the alternate Description
        <hr>
        
        Field Value
        Type:str
        """
        Modifiable: bool = ...
        """
        the new value for the alternate for modifiable flag
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    class AssignAlternateRevData():
        """
        Contains alternate Revision Id data .  
        
        Constructor: 
        NXOpen.PDM.AlternateIdManager.AssignAlternateRevData()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        AlternateRevId: str = ...
        """
        the new value the alternate Revision ID  
        <hr>
        
        Field Value
        Type:str
        """
        Modifiable: bool = ...
        """
        the new value of flag for revision modifiable 
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContext(self, context: str) -> None:
        """
        Sets the value of a context.  
        
        Signature ``SetContext(context)`` 
        
        :param context:  the new value the context is to be set to  
        :type context: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetContext(self) -> str:
        """
        Gets the value of a context as it is currently set on this manager class.  
        
        Signature ``GetContext()`` 
        
        :returns:  the current value of the context on this manager  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllContexts(self) -> 'list[str]':
        """
        Gets a list of all the available contexts.  
        
        Signature ``GetAllContexts()`` 
        
        :returns:  list of contexts  
        :rtype: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetIdType(self, idType: str) -> None:
        """
        Sets the value of an ID type.  
        
        Signature ``SetIdType(idType)`` 
        
        :param idType:  the new value the ID type is to be set to  
        :type idType: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetIdType(self) -> str:
        """
        Gets the value of a ID type as it is currently set on this manager class.  
        
        Signature ``GetIdType()`` 
        
        :returns:  the current value of the ID type on this manager  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllIdTypes(self, context: str) -> 'list[str]':
        """
        Gets a list of all the available ID types for a given context.  
        
        Signature ``GetAllIdTypes(context)`` 
        
        :param context:  the context  
        :type context: str 
        :returns:  list of ID types  
        :rtype: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAlternateItemId(self, alternateItemId: str) -> None:
        """
        Sets the value of the alternate item ID.  
        
        Signature ``SetAlternateItemId(alternateItemId)`` 
        
        :param alternateItemId:  the new value the alternate item ID is to be set to  
        :type alternateItemId: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AssignAlternateId(self) -> tuple:
        """
        This method generates alternate item and revision IDs and sets these generated
        values on this manager class.  
        
        Note that the ID context and type must be set on the
        builder in order for this assign operation to be successful. 
        
        Signature ``AssignAlternateId()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (alternateItemId, alternateRevId). alternateItemId is a str.   the newly generated alternate item ID value                                               that was set on this manager alternateRevId is a str.   the newly generated alternate revision ID value                                               that was set on this manager 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAlternateItemId(self) -> str:
        """
        Gets the value of a alternate ID as it is currently set on this manager class.  
        
        Signature ``GetAlternateItemId()`` 
        
        :returns:  the current value of the alternate item ID on this manager  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAlternateRevId(self, alternateRevId: str) -> None:
        """
        Sets the value of the alternate rev ID.  
        
        Signature ``SetAlternateRevId(alternateRevId)`` 
        
        :param alternateRevId:  the new value the alternate rev ID                                                is to be set to  
        :type alternateRevId: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AssignAlternateRevId(self) -> str:
        """
        This method generates an alternate rev ID and sets this generated value on
        this manager class.  
        
        Note that the ID context and type must be set on the
        builder in order for this assign operation to be successful.  
        
        Signature ``AssignAlternateRevId()`` 
        
        :returns:  the newly generated alternate rev ID
        value that was set on this manager  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAlternateRevId(self) -> str:
        """
        Gets the value of a alternate rev ID as it is currently set on this manager class.  
        
        Signature ``GetAlternateRevId()`` 
        
        :returns:  the current value of the alternate rev ID
        on this manager  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAlternateName(self, alternateName: str) -> None:
        """
        Sets the value of the alternate name.  
        
        Signature ``SetAlternateName(alternateName)`` 
        
        :param alternateName:  the new value the alternate name is to be set to  
        :type alternateName: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAlternateName(self) -> str:
        """
        Gets the value of a alternate name as it is currently set on this manager class.  
        
        Signature ``GetAlternateName()`` 
        
        :returns:  the current value of the alternate name on
        this manager  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAlternateDescription(self, alternateDescription: str) -> None:
        """
        Sets the value of the alternate description.  
        
        Signature ``SetAlternateDescription(alternateDescription)`` 
        
        :param alternateDescription:  the new value the alternate description                                                     is to be set to  
        :type alternateDescription: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAlternateDescription(self) -> str:
        """
        Gets the value of a alternate name as it is currently set on this manager class.  
        
        Signature ``GetAlternateDescription()`` 
        
        :returns:  the current value of the alternate
        description on this manager  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAlternateIdAsDefaultIndentifier(self, alternateIdAsDefaultIndentifier: bool) -> None:
        """
        Sets whether the alternate ID information should be the default indentifier.  
        
        Signature ``SetAlternateIdAsDefaultIndentifier(alternateIdAsDefaultIndentifier)`` 
        
        :param alternateIdAsDefaultIndentifier:  the new value the option                                                              is to be set to  
        :type alternateIdAsDefaultIndentifier: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAlternateIdAsDefaultIndentifier(self) -> bool:
        """
        Gets (as it is currently set on this manager class) whether the
        alternate ID information should be the default indentifier.  
        
        Signature ``GetAlternateIdAsDefaultIndentifier()`` 
        
        :returns:  the current value of option
        on this manager  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAlternateIdInformation(self, context: str, idType: str, alternateItemId: str, alternateRevId: str, alternateName: str, alternateDescription: str, alternateIdAsDefaultIndentifier: bool) -> None:
        """
        Sets alternate ID information on this manager class.  
        
        None can be specified
        for parameters which are set via other set or assign methods on this builder. 
        
        Signature ``SetAlternateIdInformation(context, idType, alternateItemId, alternateRevId, alternateName, alternateDescription, alternateIdAsDefaultIndentifier)`` 
        
        :param context:  the new value the context is to be set to  
        :type context: str 
        :param idType:  the new value the ID type is to be set to  
        :type idType: str 
        :param alternateItemId:  the new value the alternate item ID is to be set to  
        :type alternateItemId: str 
        :param alternateRevId:  the new value the alternate rev ID                                                is to be set to  
        :type alternateRevId: str 
        :param alternateName:  the new value the alternate name is to be set to  
        :type alternateName: str 
        :param alternateDescription:  the new value the alternate description                                                      is to be set to  
        :type alternateDescription: str 
        :param alternateIdAsDefaultIndentifier:  the new value the option                                                               is to be set to  
        :type alternateIdAsDefaultIndentifier: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAlternateIdInformation(self) -> None:
        """
        Adds the alternate ID information set by calling
        :py:meth:`SetAlternateIdInformation` and the various "assign" and "set"
        methods. The context, ID type, alternate ID, alternate revision ID, and the
        alternate name must all be set before calling this method. 
        
        Signature ``CreateAlternateIdInformation()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AssignAlternateIds(self, context: str, idType: str) -> AlternateIdManagerAlternateIdsData_Struct:
        """
        Generates the alternate ID information by calling
        :py:meth:`AssignAlternateIds` . Returns pointer to  PDM.Altids.AlternateIdsData object. 
        Sets Alternate Name,Alternate Id,Alternate Revision ,Alternate Description,
        flag for alternate Id modifiable and flag for revision modifiable into Alternate Manager object.
        
        Signature ``AssignAlternateIds(context, idType)`` 
        
        :param context:  the context  
        :type context: str 
        :param idType:  the Id type  
        :type idType: str 
        :returns: Contains alternate Ids data  
        :rtype: :py:class:`NXOpen.PDM.AlternateIdManagerAlternateIdsData_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AssignAlternateRevision(self) -> AlternateIdManagerAssignAlternateRevData_Struct:
        """
        Generates the alternate Revision ID information.  
        
        Sets Alternate Revision and flag for revision modifiable into Alternate Manager object.
        
        Signature ``AssignAlternateRevision()`` 
        
        :returns: Contains alternate Revision Id data  
        :rtype: :py:class:`NXOpen.PDM.AlternateIdManagerAssignAlternateRevData_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class DatabaseObjects(NXOpen.TransientObject):
    """
    Represents a collection of :py:class:`NXOpen.PDM.DatabaseObject`.  
    
    .. versionadded:: NX11.0.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDatabaseObjects(self, databaseObjects: 'list[DatabaseObject]') -> None:
        """
        This API sets the collection of :py:class:`NXOpen.PDM.DatabaseObject`.  
        
        Signature ``SetDatabaseObjects(databaseObjects)`` 
        
        :param databaseObjects:  Database objects  
        :type databaseObjects: list of :py:class:`NXOpen.PDM.DatabaseObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDatabaseObjects(self) -> 'list[DatabaseObject]':
        """
        This API returns the collection of :py:class:`NXOpen.PDM.DatabaseObject` as an array.  
        
        Signature ``GetDatabaseObjects()`` 
        
        :returns:  Database objects  
        :rtype: list of :py:class:`NXOpen.PDM.DatabaseObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Append(self, databaseObjects: 'list[DatabaseObjects]') -> None:
        """
        This API appends to the collection of :py:class:`NXOpen.PDM.DatabaseObject`.  
        
        Signature ``Append(databaseObjects)`` 
        
        :param databaseObjects:  Database objects  
        :type databaseObjects: list of :py:class:`NXOpen.PDM.DatabaseObjects` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class PdmFile(NXOpen.TransientObject):
    """
    Contains methods for accessing PDM file data.  
    
    .. versionadded:: NX11.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFileName(self) -> str:
        """
        Get the file name of a PDM file.  
        
        Signature ``GetFileName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFileLastModifiedDate(self) -> str:
        """
        Get the last modified date of a PDM file.  
        
        Signature ``GetFileLastModifiedDate()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFileSize(self) -> str:
        """
        Get the file size of a PDM file.  
        
        Signature ``GetFileSize()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class PdmPartCheckoutInput_Struct():
    """
    Reservation check-out input struct .  
    
    Constructor: 
    NXOpen.PDM.PdmPart.CheckoutInput()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    InputComment: str = ...
    """
    Field Value
    Type:str
    """
    InputChangeId: str = ...
    """
    Field Value
    Type:str
    """
    AllowRemote: bool = ...
    """
    True to allow remote check out, false otherwise 
    <hr>
    
    Field Value
    Type:bool
    """
    ExplicitCheckOut: bool = ...
    """
    True to perform explicit check out, false otherwise 
    <hr>
    
    Field Value
    Type:bool
    """
    IncludeSecondary: bool = ...
    """
    True to check out secondary dataset, false otherwise 
    <hr>
    
    Field Value
    Type:bool
    """


class CrossSheetReference(ModelElement):
    """
    Represents a base class that provides common methods for various model elements in a :py:class:`NXOpen.CollaborativeDesign`.  
    
    Instance of this can not directly created.
    
    .. versionadded:: NX11.0.0
    """
    Null: CrossSheetReference = ...  # unknown typename


class PartBuilderPartNumberData_Struct():
    """
    Contains part number information.  
    
    .
    Constructor: 
    NXOpen.PDM.PartBuilder.PartNumberData()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    PartName: str = ...
    """
    The part name
    <hr>
    
    Field Value
    Type:str
    """
    PartNameModifiable: bool = ...
    """
    Modifiable flag for part name.  
    
    <hr>
    
    Field Value
    Type:bool
    """
    PartDescription: str = ...
    """
    The part description
    <hr>
    
    Field Value
    Type:str
    """
    PartDescriptionModifiable: bool = ...
    """
    Modifiable flag for part description.  
    
    <hr>
    
    Field Value
    Type:bool
    """
    PartNumber: str = ...
    """
    The multifield key
    <hr>
    
    Field Value
    Type:str
    """
    PartNumberModifiable: bool = ...
    """
    Modifiable flag for part number.  
    
    <hr>
    
    Field Value
    Type:bool
    """


class PartBuilderPartRevisionData_Struct():
    """
    Contains part revision information .  
    
    Constructor: 
    NXOpen.PDM.PartBuilder.PartRevisionData()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    PartRevision: str = ...
    """
    Part revision
    <hr>
    
    Field Value
    Type:str
    """
    PartRevisionModifiable: bool = ...
    """
    Revision Modifiable flag.  
    
    False if part revision is not modifiable
    <hr>
    
    Field Value
    Type:bool
    """


class PartBuilderPartFileNameData_Struct():
    """
    Contains part file name information .  
    
    Constructor: 
    NXOpen.PDM.PartBuilder.PartFileNameData()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    PartFileName: str = ...
    """
    Part file name
    <hr>
    
    Field Value
    Type:str
    """
    PartFileNameModifiable: bool = ...
    """
    False if part file name is not modifiable
    <hr>
    
    Field Value
    Type:bool
    """


class PartBuilderOperationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartBuilderOperation():
    """
    Tokens identifying every possible UG/Manager part selection dialog. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ExportPartNew", "File->Export->NXOpen.Part:New radio button"
       "AssemblyDiagram", "Assembly->Report->Assembly Diagram..."
       "AssemblyCreateNewComponent", "Assembly->NXOpen.Assemblies.Component->Create New..."
       "Default", "Default UG/Manager part selection dialog"
    """
    ExportPartNew = 0  # PartBuilderOperationMemberType
    AssemblyDiagram = 1  # PartBuilderOperationMemberType
    AssemblyCreateNewComponent = 2  # PartBuilderOperationMemberType
    Default = 3  # PartBuilderOperationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartBuilder(NXOpen.TransientObject):
    """
    This class serves as the base class for NX Manager part builders.  
    
    The
    NX Manager part builders are used to create new parts in NX Manager mode.
    
    This class is **deprecated in NX10</b> for "Create" and "Save As of master parts" operations.
    This class should only be used in case of Save As Non Master parts and
    Save As New Item Type Operations.
    For Create of all parts use :py:class:`NXOpen.PDM.PartOperationBuilder` and :py:class:`NXOpen.FileNew`
    For Save As of master parts, use :py:class:`NXOpen.PDM.PartOperationCopyBuilder`.
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX4.0.0
    """
    
    class PartNumberData():
        """
        Contains part number information.  
        
        .
        Constructor: 
        NXOpen.PDM.PartBuilder.PartNumberData()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        PartName: str = ...
        """
        The part name
        <hr>
        
        Field Value
        Type:str
        """
        PartNameModifiable: bool = ...
        """
        Modifiable flag for part name.  
        
        <hr>
        
        Field Value
        Type:bool
        """
        PartDescription: str = ...
        """
        The part description
        <hr>
        
        Field Value
        Type:str
        """
        PartDescriptionModifiable: bool = ...
        """
        Modifiable flag for part description.  
        
        <hr>
        
        Field Value
        Type:bool
        """
        PartNumber: str = ...
        """
        The multifield key
        <hr>
        
        Field Value
        Type:str
        """
        PartNumberModifiable: bool = ...
        """
        Modifiable flag for part number.  
        
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    class PartRevisionData():
        """
        Contains part revision information .  
        
        Constructor: 
        NXOpen.PDM.PartBuilder.PartRevisionData()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        PartRevision: str = ...
        """
        Part revision
        <hr>
        
        Field Value
        Type:str
        """
        PartRevisionModifiable: bool = ...
        """
        Revision Modifiable flag.  
        
        False if part revision is not modifiable
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    class PartFileNameData():
        """
        Contains part file name information .  
        
        Constructor: 
        NXOpen.PDM.PartBuilder.PartFileNameData()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        PartFileName: str = ...
        """
        Part file name
        <hr>
        
        Field Value
        Type:str
        """
        PartFileNameModifiable: bool = ...
        """
        False if part file name is not modifiable
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    class Operation():
        """
        Tokens identifying every possible UG/Manager part selection dialog. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ExportPartNew", "File->Export->NXOpen.Part:New radio button"
           "AssemblyDiagram", "Assembly->Report->Assembly Diagram..."
           "AssemblyCreateNewComponent", "Assembly->NXOpen.Assemblies.Component->Create New..."
           "Default", "Default UG/Manager part selection dialog"
        """
        ExportPartNew = 0  # PartBuilderOperationMemberType
        AssemblyDiagram = 1  # PartBuilderOperationMemberType
        AssemblyCreateNewComponent = 2  # PartBuilderOperationMemberType
        Default = 3  # PartBuilderOperationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreatePartSpec(self, partType: str, partNumber: str, partRevision: str, partFileType: str, partFileName: str) -> None:
        """
        Create the specification for the new part that will be created.  
        
        For the input part_number:
        In case of Default Domain: it is Teamcenter item ID.
        In case of non-Default Domain: it is the multifield key.
        e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        And the encoded part filename would be containing the MFK.
        
        NOTE: The part_file_name argument is the Dataset Name and is applicable only while creating
        specs for non-master parts.
        
        Deprecated in NX10 except for Save As Non Master part and
        Save As to New Item Type operations. Use :py:meth:`NXOpen.PDM.PartOperationBuilder.CreateSpecificationsForLogicalObjects`
        instead.
        
        Signature ``CreatePartSpec(partType, partNumber, partRevision, partFileType, partFileName)`` 
        
        :param partType:  the part type  
        :type partType: str 
        :param partNumber:  the multifield key  
        :type partNumber: str 
        :param partRevision:  the part revision  
        :type partRevision: str 
        :param partFileType:  the part file type  
        :type partFileType: str 
        :param partFileName:  the dataset name  
        :type partFileName: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewDatabaseAttributeManager(self) -> DatabaseAttributeManager:
        """
        Create an instance of a :py:class:`NXOpen.PDM.DatabaseAttributeManager`
        class that will be used to modify database attributes while creating the new part.  
        
        Signature ``NewDatabaseAttributeManager()`` 
        
        :returns:  the new :py:class:`NXOpen.PDM.DatabaseAttributeManager` instance  
        :rtype: :py:class:`NXOpen.PDM.DatabaseAttributeManager` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreatePartCreationObject(self) -> PartCreationObject:
        """
        Create an instance of a :py:class:`NXOpen.PDM.PartCreationObject`
        class that acts as a proxy for a part in NX Manager mode prior to that part
        being created.  
        
        Signature ``CreatePartCreationObject()`` 
        
        :returns:  the new :py:class:`NXOpen.PDM.PartCreationObject` instance  
        :rtype: :py:class:`NXOpen.PDM.PartCreationObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewAlternateIdManager(self) -> AlternateIdManager:
        """
        Create an instance of a :py:class:`NXOpen.PDM.AlternateIdManager`
        class that will be used to create alternate ID information while creating the new part.  
        
        Signature ``NewAlternateIdManager()`` 
        
        :returns:  the new :py:class:`NXOpen.PDM.AlternateIdManager` instance  
        :rtype: :py:class:`NXOpen.PDM.AlternateIdManager` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def AssignPartNumber(self, partType: str) -> str:
        """
        This method generates a part number given an input part type and
        assigns this part number to the builder.
        
        The input part type will also be assigned to the builder. If the
        input part type is None then this method will fail unless the part
        type has already been set on the builder via a previous call to this method
        or to :py:meth:`PDM.PartBuilder.CreatePartSpec`.
        
        If this method is called before :py:meth:`PDM.PartBuilder.CreatePartSpec`
        (as will typically be the case) then the **part_type</b> and
        **part_number</b> parameters of
        :py:meth:`PDM.PartBuilder.CreatePartSpec`
        should be set to None so that the builder will use the values assigned
        by this method. Otherwise, CreatePartSpec will override the values assigned
        here and assign the values of the **part_type</b> and **part_number</b>
        parameters to the builder.
        
        The output part_number:
        In case of Default Domain: it is Teamcenter item ID.
        In case of non-Default Domain: it is the multifield key.
        e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        
        Deprecated in NX10 except for Save As Non Master part and
        Save As to New Item Type operations. Use :py:class:`NXOpen.PDM.PartOperationCreateBuilder`
        for Create and :py:class:`NXOpen.PDM.PartOperationCopyBuilder` for Save As instead.
        To assign part number, use :py:class:`NXOpen.PDM.LogicalObject` and
        :py:class:`NXOpen.AttributePropertiesBuilder` to create DB_PART_NO attribute.
        
        Signature ``AssignPartNumber(partType)`` 
        
        :param partType:  the part type  
        :type partType: str 
        :returns:  the assigned multifield key  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def AssignPartNumber(self, oldPartNumber: str, partType: str) -> PartBuilderPartNumberData_Struct:
        """
        This method generates a part number given an input part type and
        sets this part number to the builder.
        
        The input part type will also be assigned to the builder. If the
        input part type is None then this method will fail unless the part
        type has already been set on the builder via a previous call to this method
        or to :py:meth:`PDM.PartBuilder.CreatePartSpec`.
        
        If this overloaded method is called before :py:meth:`PDM.PartBuilder.CreatePartSpec`
        then the **part_number</b> parameter of
        :py:meth:`PDM.PartBuilder.CreatePartSpec`
        should be set to None so that the builder will use the value assigned
        by this method. Otherwise, CreatePartSpec will override the value assigned
        here and assign the value of **part_number</b>
        parameter to the builder.
        
        The output part_number in part_info structure:
        In case of Default Domain: it is Teamcenter item ID.
        In case of non-Default Domain: it is the multifield key.
        e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        
        Deprecated in NX10 except for Save As Non Master part and
        Save As to New Item Type operations. Use :py:class:`NXOpen.PDM.PartOperationCreateBuilder`
        for Create and :py:class:`NXOpen.PDM.PartOperationCopyBuilder` for Save As instead.
        To assign part number, use :py:class:`NXOpen.PDM.LogicalObject` and
        :py:class:`NXOpen.AttributePropertiesBuilder` to create DB_PART_NO attribute.
        
        Signature ``AssignPartNumber(oldPartNumber, partType)`` 
        
        :param oldPartNumber:  Old part number  
        :type oldPartNumber: str 
        :param partType:  Part type  
        :type partType: str 
        :returns:  Contains part number information. 
        :rtype: :py:class:`NXOpen.PDM.PartBuilderPartNumberData_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def AssignPartRevision(self) -> str:
        """
        This method generates a part revision and assigns this part revision
        to the builder.
        
        This method depends on the part type and part number already being
        set on the builder. Therefore, a call to
        :py:meth:`PDM.PartBuilder.CreatePartSpec` or,
        more likely, to :py:meth:`AssignPartNumber` must be made
        before calling this method.
        
        If this method is called before :py:meth:`PDM.PartBuilder.CreatePartSpec`
        (as will typically be the case) then the **part_revision</b> parameter of
        :py:meth:`PDM.PartBuilder.CreatePartSpec`
        should be set to None so that the builder will use the value assigned
        by this method. Otherwise, CreatePartSpec will override the value assigned
        here and assign the value of the **part_revision</b>
        parameters to the builder.
        
        Deprecated in NX10 except for Save As Non Master part and
        Save As to New Item Type operations. Use :py:class:`NXOpen.PDM.PartOperationCreateBuilder`
        for Create and :py:class:`NXOpen.PDM.PartOperationCopyBuilder` for Save As instead.
        To assign part number, use :py:class:`NXOpen.PDM.LogicalObject` and
        :py:class:`NXOpen.AttributePropertiesBuilder` to create DB_PART_REV attribute.
        
        Signature ``AssignPartRevision()`` 
        
        :returns:  the assigned part revision  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def AssignPartRevision(self, overload: int) -> PartBuilderPartRevisionData_Struct:
        """
        This method generates a part revision and sets this part revision to the builder.
        
        This method depends on the part type and part number already being
        set on the builder. Therefore, a call to
        :py:meth:`PDM.PartBuilder.CreatePartSpec` or,
        more likely, to :py:meth:`AssignPartNumber` must be made
        before calling this method.
        
        If this method is called before :py:meth:`PDM.PartBuilder.CreatePartSpec`
        then the **part_revision</b> parameter of
        :py:meth:`PDM.PartBuilder.CreatePartSpec`
        should be set to None so that the builder will use the value assigned
        by this method. Otherwise, CreatePartSpec will override the value assigned
        here and assign the value of the **part_revision</b>
        parameters to the builder.
        
        Deprecated in NX10 except for Save As Non Master part and
        Save As to New Item Type operations. Use :py:class:`NXOpen.PDM.PartOperationCreateBuilder`
        for Create and :py:class:`NXOpen.PDM.PartOperationCopyBuilder` for Save As instead.
        To assign part number, use :py:class:`NXOpen.PDM.LogicalObject` and
        :py:class:`NXOpen.AttributePropertiesBuilder` to create DB_PART_REV attribute.
        
        Signature ``AssignPartRevision(overload)`` 
        
        :param overload:  Dummy parameter to call this overloaded method 
        :type overload: int 
        :returns:  Contains part revision information  
        :rtype: :py:class:`NXOpen.PDM.PartBuilderPartRevisionData_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def AssignPartFileName(self, partFileType: str) -> str:
        """
        This method generates a part file name given an input part file type and
        assigns this part file name to the builder.
        
        This method depends on the part type, part number, and part revision
        already being set on the builder. Therefore, a call to
        :py:meth:`PDM.PartBuilder.CreatePartSpec` or,
        more likely, calls to :py:meth:`PDM.PartBuilder.AssignPartNumber` and
        :py:meth:`PDM.PartBuilder.AssignPartRevision` must be made
        before calling this method.
        
        If this method is called before :py:meth:`PDM.PartBuilder.CreatePartSpec`
        (as will typically be the case) then the **part_file_type</b> and
        **part_file_name</b> parameters of
        :py:meth:`PDM.PartBuilder.CreatePartSpec`
        should be set to None so that the builder will use the values assigned
        by this method. Otherwise, CreatePartSpec will override the values assigned
        here and assign the values of the **part_file_type</b> and **part_file_name</b>
        parameters to the builder.
        
        Deprecated in NX10 except for Save As Non Master part and
        Save As to New Item Type operations.  Use :py:meth:`NXOpen.PDM.PartOperationBuilder.CreateSpecificationsForLogicalObjects`
        instead.
        
        Signature ``AssignPartFileName(partFileType)`` 
        
        :param partFileType:  the part file type. Note that if the               part file type is "master", then this method will return None but               will still set the part file type in the builder.  
        :type partFileType: str 
        :returns:  the assigned part file name  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def AssignPartFileName(self, partNumber: str, partRevision: str, partFileNameType: str, oldPartFileName: str) -> PartBuilderPartFileNameData_Struct:
        """
        This method generates a part file name and assigns this part 
        file name to the builder.
        
        If this method is called before :py:meth:`PDM.PartBuilder.CreatePartSpec`
        then the **part_file_name</b> parameter of :py:meth:`PDM.PartBuilder.CreatePartSpec`
        should be set to None so that the builder will use the value assigned
        by this method. Otherwise, CreatePartSpec will override the value assigned
        here and assign the values of the **part_file_type</b> and **part_file_name</b>
        parameters to the builder.
        
        Deprecated in NX10 except for Save As Non Master part and
        Save As to New Item Type operations.  Use :py:meth:`NXOpen.PDM.PartOperationBuilder.CreateSpecificationsForLogicalObjects`
        instead.
        
        Signature ``AssignPartFileName(partNumber, partRevision, partFileNameType, oldPartFileName)`` 
        
        :param partNumber: Part Number 
        :type partNumber: str 
        :param partRevision:  part revision 
        :type partRevision: str 
        :param partFileNameType: Part file name type.                Note that if the part file type is "master", then this method will set the                 field **PartFileName</b> of :py:class:`PDM.PartBuilderPartFileNameData_Struct`                with None 
        :type partFileNameType: str 
        :param oldPartFileName: Old part file name 
        :type oldPartFileName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartBuilderPartFileNameData_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAssignPartNumber(self, partNumber: str) -> None:
        """
        Sets the part number explicitly into builder.  
        
        This method is called before :py:meth:`PDM.PartBuilder.CreatePartSpec`
        
        Deprecated in NX10 except for Save As Non Master part and
        Save As to New Item Type operations. Use :py:class:`NXOpen.PDM.PartOperationCreateBuilder`
        for Create and :py:class:`NXOpen.PDM.PartOperationCopyBuilder` for Save As instead.
        To assign part number, use :py:class:`NXOpen.PDM.LogicalObject` and
        :py:class:`NXOpen.AttributePropertiesBuilder` to set the DB_PART_NO attribute.
        
        Signature ``SetAssignPartNumber(partNumber)`` 
        
        :param partNumber:  the part number  
        :type partNumber: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAssignPartType(self, partType: str) -> None:
        """
        Sets the part type explicitly into builder.  
        
        This method is called before :py:meth:`PDM.PartBuilder.CreatePartSpec`
        
        Deprecated in NX10 except for Save As Non Master part and
        Save As to New Item Type operations. Use :py:meth:`NXOpen.PDM.PartOperationBuilder.CreateSpecificationsForLogicalObjects`
        instead.
        
        Signature ``SetAssignPartType(partType)`` 
        
        :param partType: 
        :type partType: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContextOperation(self, operation: PartBuilderOperation) -> None:
        """
        Sets explicitly the place from where part selection dialog invoked into builder.  
        
        Deprecated in NX10 except for Save As Non Master part and
        Save As to New Item Type operations. Use :py:meth:`NXOpen.PDM.PartOperationBuilder.CreateSpecificationsForLogicalObjects`
        instead.
        
        Signature ``SetContextOperation(operation)`` 
        
        :param operation:  Token identifying place from where UG/Manager part selection dialog invoked  
        :type operation: :py:class:`NXOpen.PDM.PartBuilderOperation` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class TracelinkQuery(NXOpen.TransientObject):
    """
    Represents the Trace link query   
    
    To obtain an instance of this class use :py:class:`NXOpen.PDM.RequirementUtils`
    
    .. versionadded:: NX6.0.3
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX6.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetTracelinkRelationsXml(self) -> str:
        """
        Gets the Traceline Relations.  
        
        Signature ``GetTracelinkRelationsXml()`` 
        
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.3
        
        License requirements: None.
        """
        ...
    


class EffectivityTableRow(NXOpen.NXObject):
    """
    Represents the class that contains effectivity parameters.  
    
    Instances of this class can be accessed through various application specific builders
    
    .. versionadded:: NX9.0.0
    """
    Null: EffectivityTableRow = ...  # unknown typename


class OrderedElementGroup(NXOpen.NXObject):
    """
    Represents a base class that provides common methods for ordered elements group in a :py:class:`NXOpen.PDM.ElementGroup`.  
    
    Instance of this can not directly created.
    
    .. versionadded:: NX11.0.0
    """
    Null: OrderedElementGroup = ...  # unknown typename


class PdmSearchManager():
    """
    Represents search manager class   
    
    Use :py:meth:`NXOpen.Session.PdmSearchManager` to get the instance of this class.
    
    .. versionadded:: NX6.0.0
    """
    
    def NewPdmSearch(self) -> PdmSearch:
        """
        Creates a new pdm search  
        
        Signature ``NewPdmSearch()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PdmSearch` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewPdmSoaquery(self) -> SoaQuery:
        """
        Creates a new pdm search soa query 
        
        Signature ``NewPdmSoaquery()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.SoaQuery` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX9.0.0
           This method is not useful. For NX Search use :py:meth:`NXOpen.PDM.PdmSearchManager.NewPdmSearch` instead
        
        License requirements: None.
        """
        ...
    
    
    def NewPdmSearchresult(self) -> SearchResult:
        """
        Creates a new pdm search result  
        
        Signature ``NewPdmSearchresult()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.SearchResult` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewPdmListofvalues(self) -> ListOfValues:
        """
        Creates a new pdm search list of values 
        
        Signature ``NewPdmListofvalues()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.ListOfValues` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    


class PartOperationImportBuilderExistingPartActionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationImportBuilderExistingPartAction():
    """
    This enum is used to specify the default action for import. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Overwrite", " - "
       "UseExisting", " - "
       "NewRevision", " - "
       "Default", " - "
    """
    Overwrite = 0  # PartOperationImportBuilderExistingPartActionMemberType
    UseExisting = 1  # PartOperationImportBuilderExistingPartActionMemberType
    NewRevision = 2  # PartOperationImportBuilderExistingPartActionMemberType
    Default = 3  # PartOperationImportBuilderExistingPartActionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationImportBuilderNumberingSourceOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationImportBuilderNumberingSourceOption():
    """
    This enum is used to specify the default behavior for auto assign. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PartIDGenerator", " - "
       "OSFilename", " - "
       "Attribute", " - "
    """
    PartIDGenerator = 0  # PartOperationImportBuilderNumberingSourceOptionMemberType
    OSFilename = 1  # PartOperationImportBuilderNumberingSourceOptionMemberType
    Attribute = 2  # PartOperationImportBuilderNumberingSourceOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationImportBuilderConversionRuleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationImportBuilderConversionRule():
    """
    This enum is used to specify the conversion rule for :py:class:`NXOpen.PDM.PartOperationImportBuilderNumberingSourceOption.OSFilename <NXOpen.PDM.PartOperationImportBuilderNumberingSourceOption>`. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AsID", " - "
       "AsIDandRevision", " - "
       "WithPrefix", " - "
       "WithSuffix", " - "
       "WithReplaceString", " - "
    """
    AsID = 0  # PartOperationImportBuilderConversionRuleMemberType
    AsIDandRevision = 1  # PartOperationImportBuilderConversionRuleMemberType
    WithPrefix = 2  # PartOperationImportBuilderConversionRuleMemberType
    WithSuffix = 3  # PartOperationImportBuilderConversionRuleMemberType
    WithReplaceString = 4  # PartOperationImportBuilderConversionRuleMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationImportBuilderValidationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationImportBuilderValidation():
    """
    This enum is used to specify the validation mode. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Off", " - "
       "ImportFromPart", " - "
       "RunValidation", " - "
       "RunValidationHybrid", " - "
       "Default", " - "
    """
    Off = 0  # PartOperationImportBuilderValidationMemberType
    ImportFromPart = 1  # PartOperationImportBuilderValidationMemberType
    RunValidation = 2  # PartOperationImportBuilderValidationMemberType
    RunValidationHybrid = 3  # PartOperationImportBuilderValidationMemberType
    Default = 4  # PartOperationImportBuilderValidationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationImportBuilderValidationRuleSetFileBrowseOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartOperationImportBuilderValidationRuleSetFileBrowseOption():
    """
    This enum is used to specify the option to browse the validation rule set file from. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Native", " - "
       "Teamcenter", " - "
    """
    Native = 0  # PartOperationImportBuilderValidationRuleSetFileBrowseOptionMemberType
    Teamcenter = 1  # PartOperationImportBuilderValidationRuleSetFileBrowseOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationImportBuilder(PartOperationBuilder):
    """
    Represents a builder class that performs Create operations   
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreateImportOperationBuilder`
    
    Default values.
    
    ==============================  ================
    Property                        Value
    ==============================  ================
    ConversionType                  AsID 
    ------------------------------  ----------------
    DefaultAction                   Overwrite 
    ------------------------------  ----------------
    IncludeComponentParts           1 
    ------------------------------  ----------------
    IncludeDependentParts           0 
    ------------------------------  ----------------
    NumberingSource                 PartIDGenerator 
    ------------------------------  ----------------
    UseItemTypeFromPartFile         0 
    ------------------------------  ----------------
    ValidationAbortImportOnFail     0 
    ------------------------------  ----------------
    ValidationMode                  Off 
    ------------------------------  ----------------
    ValidationRuleSetBrowseOption   Native 
    ------------------------------  ----------------
    ValidationTreatOutdatedAsPass   0 
    ------------------------------  ----------------
    ValidationTreatWarningAsPass    1 
    ==============================  ================
    
    .. versionadded:: NX10.0.0
    """
    
    class ExistingPartAction():
        """
        This enum is used to specify the default action for import. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Overwrite", " - "
           "UseExisting", " - "
           "NewRevision", " - "
           "Default", " - "
        """
        Overwrite = 0  # PartOperationImportBuilderExistingPartActionMemberType
        UseExisting = 1  # PartOperationImportBuilderExistingPartActionMemberType
        NewRevision = 2  # PartOperationImportBuilderExistingPartActionMemberType
        Default = 3  # PartOperationImportBuilderExistingPartActionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class NumberingSourceOption():
        """
        This enum is used to specify the default behavior for auto assign. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PartIDGenerator", " - "
           "OSFilename", " - "
           "Attribute", " - "
        """
        PartIDGenerator = 0  # PartOperationImportBuilderNumberingSourceOptionMemberType
        OSFilename = 1  # PartOperationImportBuilderNumberingSourceOptionMemberType
        Attribute = 2  # PartOperationImportBuilderNumberingSourceOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ConversionRule():
        """
        This enum is used to specify the conversion rule for :py:class:`NXOpen.PDM.PartOperationImportBuilderNumberingSourceOption.OSFilename <NXOpen.PDM.PartOperationImportBuilderNumberingSourceOption>`. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AsID", " - "
           "AsIDandRevision", " - "
           "WithPrefix", " - "
           "WithSuffix", " - "
           "WithReplaceString", " - "
        """
        AsID = 0  # PartOperationImportBuilderConversionRuleMemberType
        AsIDandRevision = 1  # PartOperationImportBuilderConversionRuleMemberType
        WithPrefix = 2  # PartOperationImportBuilderConversionRuleMemberType
        WithSuffix = 3  # PartOperationImportBuilderConversionRuleMemberType
        WithReplaceString = 4  # PartOperationImportBuilderConversionRuleMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Validation():
        """
        This enum is used to specify the validation mode. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Off", " - "
           "ImportFromPart", " - "
           "RunValidation", " - "
           "RunValidationHybrid", " - "
           "Default", " - "
        """
        Off = 0  # PartOperationImportBuilderValidationMemberType
        ImportFromPart = 1  # PartOperationImportBuilderValidationMemberType
        RunValidation = 2  # PartOperationImportBuilderValidationMemberType
        RunValidationHybrid = 3  # PartOperationImportBuilderValidationMemberType
        Default = 4  # PartOperationImportBuilderValidationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ValidationRuleSetFileBrowseOption():
        """
        This enum is used to specify the option to browse the validation rule set file from. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Native", " - "
           "Teamcenter", " - "
        """
        Native = 0  # PartOperationImportBuilderValidationRuleSetFileBrowseOptionMemberType
        Teamcenter = 1  # PartOperationImportBuilderValidationRuleSetFileBrowseOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def AddParts(self, parts: 'list[str]') -> 'list[str]':
        """
        Add parts to import 
        
        Signature ``AddParts(parts)`` 
        
        :param parts: 
        :type parts: list of str 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def AddPartsUsingLogFile(self, logFilePath: str) -> 'list[str]':
        """
        Add parts using log file either clone log file or import log file 
        
        Signature ``AddPartsUsingLogFile(logFilePath)`` 
        
        :param logFilePath: 
        :type logFilePath: str 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def AddPartsFromFolder(self, folderPath: str) -> 'list[str]':
        """
        Add parts to import from selected folder 
        
        Signature ``AddPartsFromFolder(folderPath)`` 
        
        :param folderPath: 
        :type folderPath: str 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetUpdatedLogicalObjects(self) -> 'list[LogicalObject]':
        """
        Gets the updated logical object objects for the parts after item type, relation type or
        master part for nonmaster is set or changed.  
        
        Signature ``GetUpdatedLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLogicalObjectForPart(self, partFilename: str) -> LogicalObject:
        """
        Gets the known logical object for the given part filename.  
        
        Signature ``GetLogicalObjectForPart(partFilename)`` 
        
        :param partFilename: 
        :type partFilename: str 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetAttributes(self, logicalObjects: 'list[LogicalObject]') -> None:
        """
        Clear all attributes from the selected logical objects 
        
        Signature ``ResetAttributes(logicalObjects)`` 
        
        :param logicalObjects: 
        :type logicalObjects: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ExecuteDryRun(self) -> None:
        """
        Execute the dry run 
        
        Signature ``ExecuteDryRun()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetDefaultProjectInformation(self) -> tuple:
        """
        Get default projects information 
        
        Signature ``GetDefaultProjectInformation()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (projectNames, assignmentStates). projectNames is a list of str.   names of the projects assignmentStates is a list of :py:class:`NXOpen.SessionProjectAssignmentState`.   assignment states 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetDefaultProjectInformation(self, projectNames: 'list[str]', assignmentStates: 'list[NXOpen.SessionProjectAssignmentState]') -> None:
        """
        Set default projects information 
        
        Signature ``SetDefaultProjectInformation(projectNames, assignmentStates)`` 
        
        :param projectNames:  names of the projects to assign  
        :type projectNames: list of str 
        :param assignmentStates:  assignment states  
        :type assignmentStates: list of :py:class:`NXOpen.SessionProjectAssignmentState` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetDfaFiles(self) -> 'list[str]':
        """
        Get the dfa files 
        
        Signature ``GetDfaFiles()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDfaFiles(self, dfaFiles: 'list[str]') -> None:
        """
        Set the dfa files 
        
        Signature ``SetDfaFiles(dfaFiles)`` 
        
        :param dfaFiles: 
        :type dfaFiles: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RemoveDfaFile(self, filename: str) -> None:
        """
        Remove the dfa file 
        
        Signature ``RemoveDfaFile(filename)`` 
        
        :param filename: 
        :type filename: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetExistingPartAttributes(self, logicalObject: LogicalObject, existingPartCliSpec: str) -> None:
        """
        Set attributes of existing part on the given logical object so that 
        the part gets imported into specified existing item based on action.  
        
        Signature ``SetExistingPartAttributes(logicalObject, existingPartCliSpec)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        :param existingPartCliSpec: 
        :type existingPartCliSpec: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ValidateLogicalObjects(self) -> None:
        """
        Validate the user inputs for following things:
        - Validates whether the input property values are valid according to defined naming rules and specified user exits for the input property.  
        
        - Check for duplicate Ids/Mfk-Ids
        - Check if all required attributes have been set
        - Check for cyclic references
        - Check if the part to import already exists in database and has no read access
        - Check if the part to import already exists in database and belong to an invalid type for import(e.g. Shape Design)
        - Check for duplicate non-master dataset names under same master
        - Check if it is trying to create two new revisions of same item.
        - Check if the final name given to the imported part already open in session
        - Validate master for a non-master being imported; the master should be present in import operation or has to exist in database for successful creation of non-master.
        - Validate validation parameters e.g. user has selected Run Validation option which requires the user to specify the validation rule set file.
        - Update Teamcenter information attribute on logical objects
        
        Signature ``ValidateLogicalObjects()`` 
        
        .. versionadded:: NX10.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def UpdateTeamcenterInformation(self, logicalObjects: 'list[LogicalObject]') -> None:
        """
        Update the Teamcenter information string attribute TCIN_IMPORT_TEAMCENTER_INFORMATION on given logical objects 
        
        Signature ``UpdateTeamcenterInformation(logicalObjects)`` 
        
        :param logicalObjects: 
        :type logicalObjects: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX10.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    AddCAENonMastersToImport: bool = ...
    """
    Returns or sets  the add non master to import 
    
    <hr>
    
    Getter Method
    
    Signature ``AddCAENonMastersToImport`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AddCAENonMastersToImport`` 
    
    :param addCAENonMasters: 
    :type addCAENonMasters: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    AddDfaMixins: bool = ...
    """
    Returns or sets  the add dfa mixins 
    
    <hr>
    
    Getter Method
    
    Signature ``AddDfaMixins`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AddDfaMixins`` 
    
    :param addDfaMixins: 
    :type addDfaMixins: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    AssignAlternateIds: bool = ...
    """
    Returns or sets  the method returns the value indicating whether alternate IDs should be created during import 
    
    <hr>
    
    Getter Method
    
    Signature ``AssignAlternateIds`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AssignAlternateIds`` 
    
    :param createAlternateIDs: 
    :type createAlternateIDs: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    AssociatedFilesRootDirectory: str = ...
    """
    Returns or sets  the associated files root directory 
    
    <hr>
    
    Getter Method
    
    Signature ``AssociatedFilesRootDirectory`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AssociatedFilesRootDirectory`` 
    
    :param foldername: 
    :type foldername: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ConversionType: PartOperationImportBuilderConversionRule = ...
    """
    Returns or sets  the conversion type 
    
    <hr>
    
    Getter Method
    
    Signature ``ConversionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilderConversionRule` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConversionType`` 
    
    :param conversionType: 
    :type conversionType: :py:class:`NXOpen.PDM.PartOperationImportBuilderConversionRule` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DefaultAction: PartOperationImportBuilderExistingPartAction = ...
    """
    Returns or sets  the default action 
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultAction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilderExistingPartAction` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultAction`` 
    
    :param defaultAction: 
    :type defaultAction: :py:class:`NXOpen.PDM.PartOperationImportBuilderExistingPartAction` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DefaultAlternateIdContext: str = ...
    """
    Returns or sets  the method returns the IdContext to be used while assigning alternate IDs during import 
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultAlternateIdContext`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultAlternateIdContext`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DefaultAlternateIdType: str = ...
    """
    Returns or sets  the method returns the IdType to be used while assigning alternate IDs during import
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultAlternateIdType`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultAlternateIdType`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DefaultDescription: str = ...
    """
    Returns or sets  the default description 
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultDescription`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultDescription`` 
    
    :param defaultDescription: 
    :type defaultDescription: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DefaultItemType: str = ...
    """
    Returns or sets  the default item type 
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultItemType`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultItemType`` 
    
    :param defaultItemType: 
    :type defaultItemType: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DefaultName: str = ...
    """
    Returns or sets  the default name 
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultName`` 
    
    :param defaultName: 
    :type defaultName: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DefaultOwningGroup: str = ...
    """
    Returns or sets  the default owning group 
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultOwningGroup`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultOwningGroup`` 
    
    :param defaultOwningGroup: 
    :type defaultOwningGroup: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DefaultOwningUser: str = ...
    """
    Returns or sets  the default owning user 
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultOwningUser`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultOwningUser`` 
    
    :param defaultOwningUser: 
    :type defaultOwningUser: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    IncludeComponentParts: bool = ...
    """
    Returns or sets  the include component parts 
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeComponentParts`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeComponentParts`` 
    
    :param includeComponentParts: 
    :type includeComponentParts: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    IncludeDependentParts: bool = ...
    """
    Returns or sets  the include dependent parts 
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeDependentParts`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeDependentParts`` 
    
    :param includeDependentParts: 
    :type includeDependentParts: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    NumberAttr: str = ...
    """
    Returns or sets  the number attr 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberAttr`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberAttr`` 
    
    :param numberAttr: 
    :type numberAttr: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    NumberingSource: PartOperationImportBuilderNumberingSourceOption = ...
    """
    Returns or sets  the numbering source 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberingSource`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilderNumberingSourceOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberingSource`` 
    
    :param numberingSource: 
    :type numberingSource: :py:class:`NXOpen.PDM.PartOperationImportBuilderNumberingSourceOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    OutputLogFile: str = ...
    """
    Returns or sets  the output log file 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputLogFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputLogFile`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    PrefixStr: str = ...
    """
    Returns or sets  the prefix str 
    
    <hr>
    
    Getter Method
    
    Signature ``PrefixStr`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PrefixStr`` 
    
    :param prefixStr: 
    :type prefixStr: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ProductInterfaces: bool = ...
    """
    Returns or sets  the product interfaces 
    
    <hr>
    
    Getter Method
    
    Signature ``ProductInterfaces`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX10.0.2
       It is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProductInterfaces`` 
    
    :param productInterfaces: 
    :type productInterfaces: bool 
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX10.0.2
       It is no longer supported.
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    PublishOptionalInfo: bool = ...
    """
    Returns or sets  the optional information publishing 
    
    <hr>
    
    Getter Method
    
    Signature ``PublishOptionalInfo`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PublishOptionalInfo`` 
    
    :param publishOptionalInfo: 
    :type publishOptionalInfo: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ReplaceWithStr: str = ...
    """
    Returns or sets  the replace with str 
    
    <hr>
    
    Getter Method
    
    Signature ``ReplaceWithStr`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReplaceWithStr`` 
    
    :param replaceWithStr: 
    :type replaceWithStr: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    RevisionAttr: str = ...
    """
    Returns or sets  the revision attr 
    
    <hr>
    
    Getter Method
    
    Signature ``RevisionAttr`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RevisionAttr`` 
    
    :param revisionAttr: 
    :type revisionAttr: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    StringToReplace: str = ...
    """
    Returns or sets  the string to replace 
    
    <hr>
    
    Getter Method
    
    Signature ``StringToReplace`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StringToReplace`` 
    
    :param stringToReplace: 
    :type stringToReplace: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SuffixStr: str = ...
    """
    Returns or sets  the suffix str 
    
    <hr>
    
    Getter Method
    
    Signature ``SuffixStr`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SuffixStr`` 
    
    :param suffixStr: 
    :type suffixStr: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SyncArrangements: bool = ...
    """
    Returns or sets  the sync arrangements 
    
    <hr>
    
    Getter Method
    
    Signature ``SyncArrangements`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX10.0.2
       It is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SyncArrangements`` 
    
    :param syncArrangements: 
    :type syncArrangements: bool 
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX10.0.2
       It is no longer supported.
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    UseItemTypeFromPartFile: bool = ...
    """
    Returns or sets  the flag to specify if Import can use the Item Type already present in the part during import 
    
    <hr>
    
    Getter Method
    
    Signature ``UseItemTypeFromPartFile`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``UseItemTypeFromPartFile`` 
    
    :param useItemTypeFromPartFile: 
    :type useItemTypeFromPartFile: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ValidationAbortImportOnFail: bool = ...
    """
    Returns or sets  the validation abort import on fail 
    
    <hr>
    
    Getter Method
    
    Signature ``ValidationAbortImportOnFail`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValidationAbortImportOnFail`` 
    
    :param validationAbortImportOnFail: 
    :type validationAbortImportOnFail: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ValidationMode: PartOperationImportBuilderValidation = ...
    """
    Returns or sets  the validation mode 
    
    <hr>
    
    Getter Method
    
    Signature ``ValidationMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilderValidation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValidationMode`` 
    
    :param validationMode: 
    :type validationMode: :py:class:`NXOpen.PDM.PartOperationImportBuilderValidation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ValidationRuleSetBrowseOption: PartOperationImportBuilderValidationRuleSetFileBrowseOption = ...
    """
    Returns or sets  the validation rule set browse option 
    
    <hr>
    
    Getter Method
    
    Signature ``ValidationRuleSetBrowseOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilderValidationRuleSetFileBrowseOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValidationRuleSetBrowseOption`` 
    
    :param validationRuleSetBrowseOption: 
    :type validationRuleSetBrowseOption: :py:class:`NXOpen.PDM.PartOperationImportBuilderValidationRuleSetFileBrowseOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ValidationRuleSetFile: str = ...
    """
    Returns or sets  the validation rule set file 
    
    <hr>
    
    Getter Method
    
    Signature ``ValidationRuleSetFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValidationRuleSetFile`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ValidationTreatOutdatedAsPass: bool = ...
    """
    Returns or sets  the validation treat outdated as pass 
    
    <hr>
    
    Getter Method
    
    Signature ``ValidationTreatOutdatedAsPass`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValidationTreatOutdatedAsPass`` 
    
    :param validationTreatOutdatedAsPass: 
    :type validationTreatOutdatedAsPass: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ValidationTreatWarningAsPass: bool = ...
    """
    Returns or sets  the validation treat warning as pass 
    
    <hr>
    
    Getter Method
    
    Signature ``ValidationTreatWarningAsPass`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValidationTreatWarningAsPass`` 
    
    :param validationTreatWarningAsPass: 
    :type validationTreatWarningAsPass: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: PartOperationImportBuilder = ...  # unknown typename


class CustomWebAppMenuHandler(NXOpen.TransientObject):
    """
    Represents Custom WebApp Menu Handler class   
    
    .. versionadded:: NX11.0.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RegisterCustomWebAppInvokedCallback(self, webappCb: typing.Callable) -> None:
        """
        Registers the add_custom_web_app_menu_callback callback method with the webApp menu
        handler object.  
        
        Signature ``RegisterCustomWebAppInvokedCallback(webappCb)`` 
        
        :param webappCb: 
        :type webappCb: CallableObject 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedUids(self) -> 'list[str]':
        """
        Returns the unique identifier of the uids in PDM 
        
        Signature ``GetSelectedUids()`` 
        
        :returns:  Selected uids  
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCommandName(self) -> str:
        """
        Returns the command name  
        
        Signature ``GetCommandName()`` 
        
        :returns:  the command name  
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class LogicalObject(NXOpen.NXObject):
    """
    Represents the class that contains database business logic or pre-creation information for the objects.  
    
    Instances of this class can be accessed through various application specific builders
    
    .. versionadded:: NX8.5.0
    """
    Null: LogicalObject = ...  # unknown typename


class NativePartLogicalObject(LogicalObject):
    """
    Represents the class that contains information for the objects participating in import operation.  
    
    Instances of this class can be accessed through various application specific builders
    
    .. versionadded:: NX10.0.0
    """
    
    def GetInitialName(self) -> str:
        """
        Gets the initial name of this logical object.  
        
        Signature ``GetInitialName()`` 
        
        :returns:  the filename of added for import  
        :rtype: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFinalName(self) -> str:
        """
        Gets the final name of this logical object.  
        
        Signature ``GetFinalName()`` 
        
        :returns:  the database name assigned to the part being imported  
        :rtype: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsPartNameAutoAssigned(self) -> bool:
        """
        Gets the flag indicating whether part name is autoassigned or not.  
        
        Signature ``IsPartNameAutoAssigned()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsCandidateForImport(self) -> bool:
        """
        Checks if the part represented by this logical object is a candidate for import.  
        
        The part is not a candidate for import if it is lost or name-only.  
        
        Signature ``IsCandidateForImport()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetExistingPartAction(self) -> PartOperationImportBuilderExistingPartAction:
        """
        Gets the existing part action defined for this part  
        
        Signature ``GetExistingPartAction()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilderExistingPartAction` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetExistingPartAction(self, existingPartAction: PartOperationImportBuilderExistingPartAction) -> None:
        """
        Sets the existing part action defined for this part 
        
        Signature ``SetExistingPartAction(existingPartAction)`` 
        
        :param existingPartAction: 
        :type existingPartAction: :py:class:`NXOpen.PDM.PartOperationImportBuilderExistingPartAction` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetValidationMode(self) -> PartOperationImportBuilderValidation:
        """
        Gets the validation mode setting defined for this part  
        
        Signature ``GetValidationMode()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilderValidation` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValidationMode(self, validationMode: PartOperationImportBuilderValidation) -> None:
        """
        Sets the validation mode setting defined for this part 
        
        Signature ``SetValidationMode(validationMode)`` 
        
        :param validationMode: 
        :type validationMode: :py:class:`NXOpen.PDM.PartOperationImportBuilderValidation` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetValidationRuleSetFileBrowseOption(self) -> PartOperationImportBuilderValidationRuleSetFileBrowseOption:
        """
        Gets the validation rule set file browse option defined for this part  
        
        Signature ``GetValidationRuleSetFileBrowseOption()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilderValidationRuleSetFileBrowseOption` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValidationRuleSetFileBrowseOption(self, browseOption: PartOperationImportBuilderValidationRuleSetFileBrowseOption) -> None:
        """
        Sets the validation rule set file browse option defined for this part 
        
        Signature ``SetValidationRuleSetFileBrowseOption(browseOption)`` 
        
        :param browseOption: 
        :type browseOption: :py:class:`NXOpen.PDM.PartOperationImportBuilderValidationRuleSetFileBrowseOption` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Null: NativePartLogicalObject = ...  # unknown typename


class SmartSaveObject(NXOpen.NXObject):
    """
    Represents the class for object participating in the smart save operation.  
    
    Instances of this class can be accessed through smart save builder.
    
    .. versionadded:: NX11.0.0
    """
    
    def GetEffectivityFormula(self) -> str:
        """
        Returns the current effectivity formula for this smart save object  
        
        Signature ``GetEffectivityFormula()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEffectivityFormula(self, effectivityFormula: str, effectivityDisplayString: str) -> None:
        """
        Sets the new effectivity formula to be applied on this smart save object 
        
        Signature ``SetEffectivityFormula(effectivityFormula, effectivityDisplayString)`` 
        
        :param effectivityFormula: 
        :type effectivityFormula: str 
        :param effectivityDisplayString: 
        :type effectivityDisplayString: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    Null: SmartSaveObject = ...  # unknown typename


class PartFromTemplateBuilder(PartBuilder):
    """
    This class provides the methods necessary to create a new part in NX Manager
    from a template part.  
    
    Deprecated in NX10.0.0.  Use :py:class:`PDM.PartOperationCreateBuilder`  instead.
    
    The operation that this builder supports is equivalent to the file new operation which
    creates a new part from a template (or seed) part.
    
    If the operation is successful, then the newly created part will be the display part.
    
    This class is a singleton meaning only one instance of it can be exist at a time.
    
    .. versionadded:: NX4.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSeedPart(self, seedName: str) -> None:
        """
        Sets the seed part on which the new part will be based.  
        
        Signature ``SetSeedPart(seedName)`` 
        
        :param seedName:  display name of the seed part. E.g. "Metric"  
        :type seedName: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:class:`PDM.PartOperationCreateBuilder` instead.
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Commit(self) -> NXOpen.BasePart:
        """
        Creates the new part that has been fully-specified by calling methods on this
        builder. The new part will be set to display part after it is created.  
        
        Signature ``Commit()`` 
        
        :returns:  newly created part  
        :rtype: :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:class:`PDM.PartOperationCreateBuilder` instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Commit(self, setAsDisplayPart: bool) -> NXOpen.BasePart:
        """
        Creates the new part that has been fully-specified by calling methods on this
        builder. The caller specifies whether
        the new part should be set as the display after it is created.  
        
        Signature ``Commit(setAsDisplayPart)`` 
        
        :param setAsDisplayPart:  True means the new part will                set as the display part. False means that it will not.  
        :type setAsDisplayPart: bool 
        :returns:  newly created part  
        :rtype: :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:class:`PDM.PartOperationCreateBuilder` instead.
        
        License requirements: None.
        """
        ...
    


class SoaQuery(NXOpen.TransientObject):
    """
    Represents search soa query to perform Teamcenter search  
    
    .. versionadded:: NX6.0.0
    """
    
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
    
    
    def AddFieldDescription(self, searchVar: PdmSearch, type: PdmSoaqueryNxmgrfielddatatype, name: str, attrName: str, defaultValue: str, logicalOperation: str, mathOperation: str, lov: ListOfValues) -> None:
        """
        Add the field description to create an SOA query 
        
        Signature ``AddFieldDescription(searchVar, type, name, attrName, defaultValue, logicalOperation, mathOperation, lov)`` 
        
        :param searchVar:  pdm search structure  
        :type searchVar: :py:class:`NXOpen.PDM.PdmSearch` 
        :param type:  search field data type  
        :type type: :py:class:`NXOpen.PDM.PdmSoaqueryNxmgrfielddatatype` 
        :param name:  name of search  
        :type name: str 
        :param attrName:  search attribute  name  
        :type attrName: str 
        :param defaultValue:  default value  
        :type defaultValue: str 
        :param logicalOperation:  logical operation for search criteria  
        :type logicalOperation: str 
        :param mathOperation:  math operation for search criteria  
        :type mathOperation: str 
        :param lov:  List of values  
        :type lov: :py:class:`NXOpen.PDM.ListOfValues` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX8.0.0
           It's not needed in any context of search based on queries.
        
        License requirements: None.
        """
        ...
    


class FindCriteria(NXOpen.TransientObject):
    """
    Represents find criteria objects   
    
    .. versionadded:: NX11.0.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCriteria(self, queryName: str, entries: 'list[str]', values: 'list[str]') -> None:
        """
        This API sets the search query name, entries, and values.  
        
        Signature ``SetCriteria(queryName, entries, values)`` 
        
        :param queryName:  Search query name  
        :type queryName: str 
        :param entries:  Search criteria entries  
        :type entries: list of str 
        :param values:  Search criteria values  
        :type values: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCriteria(self) -> tuple:
        """
        This API returns the search query name, entries, and values.  
        
        Signature ``GetCriteria()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (queryName, entries, values). queryName is a str.   Search query name entries is a list of str.   Search criteria entries values is a list of str.   Search criteria values 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class DBEntityProxyCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.PDM.DBEntityProxy` objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX11.0.1
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindProxy(self, journalIdentifier: str) -> NXOpen.NXObject:
        """
        Find the DBEntityProxy object with input name  
        
        Signature ``FindProxy(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier of the DBEntity object you want  
        :type journalIdentifier: str 
        :returns:  DBEntity Object with this identifier  
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CreateDbEntityProxy(self, title: str, index: int, context: NXOpen.TaggedObject, attributeOwner: NXOpen.TaggedObject) -> DBEntityProxy:
        """
        Creates a :py:class:`NXOpen.PDM.DBEntityProxy`  
        
        Signature ``CreateDbEntityProxy(title, index, context, attributeOwner)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :param context: 
        :type context: :py:class:`NXOpen.TaggedObject` 
        :param attributeOwner: 
        :type attributeOwner: :py:class:`NXOpen.TaggedObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.DBEntityProxy` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    


class PdmNavigatorNode(NXOpen.TreeListNode):
    """
    Represents a PdmNavigatorNode   
    
    .. versionadded:: NX6.0.4
    """
    
    def GetUid(self) -> str:
        """
        Returns the unique identifier of the PdmNavigatorNode in PDM  
        
        Signature ``GetUid()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX6.0.4
        
        License requirements: None.
        """
        ...
    
    
    def GetNodeType(self) -> str:
        """
        Returns the type of the PdmNavigatorNode in PDM  
        
        Signature ``GetNodeType()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX6.0.4
        
        License requirements: None.
        """
        ...
    
    Null: PdmNavigatorNode = ...  # unknown typename


class SmartSaveContext(NXOpen.TransientObject):
    """
    Represents smart save context   
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreateSmartSaveContext`
    
    .. versionadded:: NX11.0.1
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetWorkObjectToRootObjectMap(self, workObjects: 'list[NXOpen.TaggedObject]', rootObjects: 'list[NXOpen.TaggedObject]') -> None:
        """
        Adds the given set of work object to root object pairs to the context 
        
        Signature ``SetWorkObjectToRootObjectMap(workObjects, rootObjects)`` 
        
        :param workObjects:  array of work objects to be saved  
        :type workObjects: list of :py:class:`NXOpen.TaggedObject` 
        :param rootObjects:  array of root objects  
        :type rootObjects: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetWorkObjectToRootObjectMap(self) -> tuple:
        """
        Returns the set of work object to root object pairs from the context 
        
        Signature ``GetWorkObjectToRootObjectMap()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (workObjects, rootObjects). workObjects is a list of :py:class:`NXOpen.TaggedObject`.   array of work objects to be saved rootObjects is a list of :py:class:`NXOpen.TaggedObject`.   array of root objects  
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetSaveType(self) -> SmartSaveBuilderSaveType:
        """
        Returns the save operation type  
        
        Signature ``GetSaveType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.SmartSaveBuilderSaveType` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    


class SaveAsReviseObserver(NXOpen.TaggedObjectCollection):
    """
    This class is responsible for invoking registered callback when objects goes for SaveAs and Revise and after the process.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.PDM.PdmSession`
    
    .. versionadded:: NX11.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def AddPrecopyoperationCallback(self, precopyoperationCb: typing.Callable) -> int:
        """
        Registers a user defined precopyoperation callback that is called just before SaveAs and Revise process  
        
        Signature ``AddPrecopyoperationCallback(precopyoperationCb)`` 
        
        :param precopyoperationCb:  method to register  
        :type precopyoperationCb: CallableObject 
        :returns:  identifier of registered method (used to deregister the method)  
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemovePrecopyoperationCallback(self, id: int) -> None:
        """
        Deregister the user defined precopyoperation callback 
        
        Signature ``RemovePrecopyoperationCallback(id)`` 
        
        :param id:  identifier for method to deregister  
        :type id: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddPostcopyoperationCallback(self, postcopyoperationCb: typing.Callable) -> int:
        """
        Registers a user defined postcopyoperation callback that is called just before SaveAs and Revise process  
        
        Signature ``AddPostcopyoperationCallback(postcopyoperationCb)`` 
        
        :param postcopyoperationCb:  method to register  
        :type postcopyoperationCb: CallableObject 
        :returns:  identifier of registered method (used to deregister the method)  
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemovePostcopyoperationCallback(self, id: int) -> None:
        """
        Deregister the user defined postcopyoperation callback 
        
        Signature ``RemovePostcopyoperationCallback(id)`` 
        
        :param id:  identifier for method to deregister  
        :type id: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class PendingComponentsManager(NXOpen.TransientObject):
    """
    This class is used for managing a part's pending components, that
    is, those that have been added within Teamcenter but are not yet
    present in NX.  
    
    An instance of this class for a particular part can
    be created by calling :py:meth:`PDM.PartManager.NewPendingComponentsManager`.
    
    .. versionadded:: NX4.0.1
    """
    
    def GetComponents(self) -> 'list[str]':
        """
        Gets "handles" for the pending components of the part associated
        with this object.  
        
        Signature ``GetComponents()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX4.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetComponentPartFileName(self, handle: str) -> str:
        """
        Gets the NX Manager file name for the part corresponding to
        a pending component.  
        
        Signature ``GetComponentPartFileName(handle)`` 
        
        :param handle:  the handle for the pending component  
        :type handle: str 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX4.0.1
        
        License requirements: None.
        """
        ...
    
    
    def ComponentHasPosition(self, handle: str) -> bool:
        """
        Determines whether a given pending component has been positioned
        by Teamcenter.  
        
        If :py:meth:`PDM.PendingComponentsManager.AddComponent`
        is called regarding a component without a position, it will automatically
        be positioned at the origin.
        
        Signature ``ComponentHasPosition(handle)`` 
        
        :param handle:  the handle for the pending component  
        :type handle: str 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX4.0.1
        
        License requirements: None.
        """
        ...
    
    
    def DeleteComponent(self, handle: str) -> None:
        """
        Deletes a pending component.  
        
        Signature ``DeleteComponent(handle)`` 
        
        :param handle:  the handle for the pending component  
        :type handle: str 
        
        .. versionadded:: NX4.0.1
        
        License requirements: None.
        """
        ...
    
    
    def AddComponent(self, handle: str) -> tuple:
        """
        Adds a pending component.  
        
        Signature ``AddComponent(handle)`` 
        
        :param handle:  the handle for the pending component  
        :type handle: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (component, loadStatus). component is a :py:class:`NXOpen.Assemblies.Component`. loadStatus is a :py:class:`NXOpen.PartLoadStatus`.   result of loading the component part 
        
        .. versionadded:: NX4.0.1
        
        License requirements: None.
        """
        ...
    
    
    def AddNgcComponent(self, handle: str) -> tuple:
        """
        Adds a pending NGC component.  
        
        Signature ``AddNgcComponent(handle)`` 
        
        :param handle:  the handle for the pending ngc component  
        :type handle: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (component, loadStatus). component is a :py:class:`NXOpen.Assemblies.Component`. loadStatus is a :py:class:`NXOpen.PartLoadStatus`.   result of loading the ngc component part 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX4.0.1
        
        License requirements: None.
        """
        ...
    


class DatabaseAttributeManager(NXOpen.TransientObject):
    """
    This class is responsible for setting and getting NX Manager database attribute.  
    
    Use :py:meth:`PDM.PartBuilder.NewDatabaseAttributeManager` or :py:meth:`PDM.PdmPart.NewDatabaseAttributeManager` to get the instance of this class.
    
    .. versionadded:: NX4.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAttribute(self, attributeTitle: str, attributeValue: str) -> None:
        """
        Sets the value of a writable database attribute.  
        
        Signature ``SetAttribute(attributeTitle, attributeValue)`` 
        
        :param attributeTitle:  the title of the attribute to be set  
        :type attributeTitle: str 
        :param attributeValue:  the new value the attribute is to be set to  
        :type attributeValue: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAttribute(self, attributeTitle: str) -> str:
        """
        Gets the value of a writable database attribute.  
        
        Signature ``GetAttribute(attributeTitle)`` 
        
        :param attributeTitle:  the title of the attribute  
        :type attributeTitle: str 
        :returns:  the value of the attribute  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def StoreAttributes(self) -> None:
        """
        Register DB_PART_NAME and DB_PART_DESC attributes with values set in the attribute_manager 
        
        Signature ``StoreAttributes()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RefreshAttributes(self) -> None:
        """
        Force load the Database Attributes from Teamcenter.  
        
        This removes changes to values made in NX. 
        
        Signature ``RefreshAttributes()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def LoadAttributes(self, reload: bool) -> None:
        """
        Load the Database Attributes from Teamcenter.  
        
        This operation will not discard any changes made in this session that aren't committed to Teamcenter.
        If 'reload' is set to 'true', attributes that have already been loaded will be loaded again, if otherwise allowed.
        
        Signature ``LoadAttributes(reload)`` 
        
        :param reload:  Reload attributes that have already been loaded, if otherwise allowed.  
        :type reload: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def LoadAttributesRecursively(self, reload: bool) -> None:
        """
        Recursively load the Database Attributes of this part and all its partially or fully loaded components from Teamcenter.  
        
        This operation will not discard any changes made in this session that aren't committed to Teamcenter.
        
        Signature ``LoadAttributesRecursively(reload)`` 
        
        :param reload:  Reload attributes that have already been loaded, if otherwise allowed.  
        :type reload: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    


class AttributeGroupReviseBuilderSaveAsActionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AttributeGroupReviseBuilderSaveAsActionType():
    """
    Represents the save as action on a managed attribute group 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NewRevision", " - "
       "NewAttributeGroup", " - "
    """
    NewRevision = 0  # AttributeGroupReviseBuilderSaveAsActionTypeMemberType
    NewAttributeGroup = 1  # AttributeGroupReviseBuilderSaveAsActionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AttributeGroupReviseBuilder(NXOpen.Builder):
    """
    Represents an attribute group revise builder.  
    
    Given a list of existing attribute groups for an
    attribute group owner, a new revision for each attribute group is created.
    
    Note: The :py:meth:`Builder.Commit` returns None for this builder.  Use the 
    :py:meth:`NXOpen.PDM.AttributeGroupReviseBuilder.GetRevisedAttributeGroups` to get the
    successfully revised attribute groups after the builder is committed.
    
    Use :py:meth:`NXOpen.PDM.IAttributeGroupOwner.CreateAttributeGroupReviseBuilder` to create an instance of this class
    
    .. versionadded:: NX9.0.0
    """
    
    class SaveAsActionType():
        """
        Represents the save as action on a managed attribute group 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NewRevision", " - "
           "NewAttributeGroup", " - "
        """
        NewRevision = 0  # AttributeGroupReviseBuilderSaveAsActionTypeMemberType
        NewAttributeGroup = 1  # AttributeGroupReviseBuilderSaveAsActionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetRevisedAttributeGroups(self) -> 'list[AttributeGroup]':
        """
        Returns a list of attribute groups for use during the revise operation.  
        
        Before the builder is committed
        this list of attribute groups is used to set any required user attribute.  The attribute groups do
        not exist in Teamcenter until the builder is committed.  After the builder is committed the list only
        contains successfully revised attribute groups.  Any attribute groups that failed to revise are removed
        from the list and are no longer valid after commit.  Call this method after commit to get a list of the
        successfully revised attribute groups.  
        
        Signature ``GetRevisedAttributeGroups()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.AttributeGroup` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOperationErrors(self) -> OperationErrors:
        """
        Returns the :py:class:`NXOpen.PDM.OperationErrors` object containing
        information about the attribute groups that failed to revise.  
        
        Signature ``GetOperationErrors()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.OperationErrors` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
        Returns the operation failures during revise of the attribute groups  
        
        Signature ``GetOperationFailures()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLogicalObjects(self) -> 'list[LogicalObject]':
        """
        Returns list of logical objects created by the builder for use during the revise operation.  
        
        Signature ``GetLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: AttributeGroupReviseBuilder = ...  # unknown typename


class WebAppSession():
    """
    Represents the Web App session   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX11.0.0
    """
    
    def CreateCustomWebAppMenuHandler(self) -> CustomWebAppMenuHandler:
        """
        Create a custom WebApp menu handler.  
        
        Signature ``CreateCustomWebAppMenuHandler()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.CustomWebAppMenuHandler` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Open(self, databaseObjects: 'list[DatabaseObject]') -> None:
        """
        Open parts represented by database objects inside NX.  
        
        Signature ``Open(databaseObjects)`` 
        
        :param databaseObjects: 
        :type databaseObjects: list of :py:class:`NXOpen.PDM.DatabaseObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ShowSummary(self, uid: str, objType: str, classId: str) -> None:
        """
        Send data to Active Workspace from NX 
        
        Signature ``ShowSummary(uid, objType, classId)`` 
        
        :param uid: 
        :type uid: str 
        :param objType: 
        :type objType: str 
        :param classId: 
        :type classId: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    


class PartOperationValidationPropertiesBuilder(NXOpen.AttributePropertiesBuilder):
    """
    Represents an :py:class:`NXOpen.PDM.PartOperationValidationPropertiesBuilder` to be used 
    for overriding the default validation parameters for a part in import operation.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreatePartOperationValidationPropertiesBuilder`
    
    Default values.
    
    ==========================  =======
    Property                    Value
    ==========================  =======
    BooleanValue                False 
    --------------------------  -------
    DataType                    String 
    --------------------------  -------
    IntegerValue                0 
    --------------------------  -------
    NumberValue                 0 
    --------------------------  -------
    ObjectPicker (deprecated)   Object 
    ==========================  =======
    
    .. versionadded:: NX10.0.0
    """
    
    def GetValidationRuleSetBrowseOption(self) -> PartOperationImportBuilderValidationRuleSetFileBrowseOption:
        """
        Gets the validation rule set browse option  
        
        Signature ``GetValidationRuleSetBrowseOption()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.PartOperationImportBuilderValidationRuleSetFileBrowseOption` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValidationRuleSetBrowseOption(self, validationRuleSetBrowseOption: PartOperationImportBuilderValidationRuleSetFileBrowseOption) -> None:
        """
        Sets the validation rule set browse option 
        
        Signature ``SetValidationRuleSetBrowseOption(validationRuleSetBrowseOption)`` 
        
        :param validationRuleSetBrowseOption: 
        :type validationRuleSetBrowseOption: :py:class:`NXOpen.PDM.PartOperationImportBuilderValidationRuleSetFileBrowseOption` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetValidationRuleSetFile(self) -> str:
        """
        Gets the validation rule set file  
        
        Signature ``GetValidationRuleSetFile()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValidationRuleSetFile(self, filename: str) -> None:
        """
        Sets the validation rule set file 
        
        Signature ``SetValidationRuleSetFile(filename)`` 
        
        :param filename: 
        :type filename: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetValidationTreatWarningAsPass(self) -> bool:
        """
        Gets the validation treat warning as pass flag  
        
        Signature ``GetValidationTreatWarningAsPass()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValidationTreatWarningAsPass(self, validationTreatWarningAsPass: bool) -> None:
        """
        Sets the validation treat warning as pass flag 
        
        Signature ``SetValidationTreatWarningAsPass(validationTreatWarningAsPass)`` 
        
        :param validationTreatWarningAsPass: 
        :type validationTreatWarningAsPass: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetValidationTreatOutdatedAsPass(self) -> bool:
        """
        Gets the validation treat outdated as pass flag  
        
        Signature ``GetValidationTreatOutdatedAsPass()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValidationTreatOutdatedAsPass(self, validationTreatOutdatedAsPass: bool) -> None:
        """
        Sets the validation treat outdated as pass flag 
        
        Signature ``SetValidationTreatOutdatedAsPass(validationTreatOutdatedAsPass)`` 
        
        :param validationTreatOutdatedAsPass: 
        :type validationTreatOutdatedAsPass: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Null: PartOperationValidationPropertiesBuilder = ...  # unknown typename


class ConfigurationContextBuilderConfigContextModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConfigurationContextBuilderConfigContextMode():
    """
    configuration mode 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Nx4gd", " - "
       "Assemblies", " - "
    """
    Nx4gd = 0  # ConfigurationContextBuilderConfigContextModeMemberType
    Assemblies = 1  # ConfigurationContextBuilderConfigContextModeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ConfigurationContextBuilderConfigContextTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConfigurationContextBuilderConfigContextType():
    """
    configuration type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AsSaved", " - "
       "PushedfromTeamcenter", " - "
       "DefineorLoadContext", " - "
    """
    AsSaved = 0  # ConfigurationContextBuilderConfigContextTypeMemberType
    PushedfromTeamcenter = 1  # ConfigurationContextBuilderConfigContextTypeMemberType
    DefineorLoadContext = 2  # ConfigurationContextBuilderConfigContextTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ConfigurationContextBuilderConfigurationDetailMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConfigurationContextBuilderConfigurationDetail():
    """
    configuration detail 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "LoadfromTeamcenter", " - "
       "DefineinNX", " - "
    """
    LoadfromTeamcenter = 0  # ConfigurationContextBuilderConfigurationDetailMemberType
    DefineinNX = 1  # ConfigurationContextBuilderConfigurationDetailMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ConfigurationContextBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.PDM.ConfigurationContextBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.ConfigurationManager.CreateConfigurationContextBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    class ConfigContextMode():
        """
        configuration mode 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Nx4gd", " - "
           "Assemblies", " - "
        """
        Nx4gd = 0  # ConfigurationContextBuilderConfigContextModeMemberType
        Assemblies = 1  # ConfigurationContextBuilderConfigContextModeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ConfigContextType():
        """
        configuration type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AsSaved", " - "
           "PushedfromTeamcenter", " - "
           "DefineorLoadContext", " - "
        """
        AsSaved = 0  # ConfigurationContextBuilderConfigContextTypeMemberType
        PushedfromTeamcenter = 1  # ConfigurationContextBuilderConfigContextTypeMemberType
        DefineorLoadContext = 2  # ConfigurationContextBuilderConfigContextTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ConfigurationDetail():
        """
        configuration detail 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "LoadfromTeamcenter", " - "
           "DefineinNX", " - "
        """
        LoadfromTeamcenter = 0  # ConfigurationContextBuilderConfigurationDetailMemberType
        DefineinNX = 1  # ConfigurationContextBuilderConfigurationDetailMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    CollaborativeDesign: NXOpen.CollaborativeDesign = ...
    """
    Returns or sets  the collaborative design 
    
    <hr>
    
    Getter Method
    
    Signature ``CollaborativeDesign`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CollaborativeDesign` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CollaborativeDesign`` 
    
    :param collaborativeDesign: 
    :type collaborativeDesign: :py:class:`NXOpen.CollaborativeDesign` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    ConfigDetail: ConfigurationContextBuilderConfigurationDetail = ...
    """
    Returns or sets  the configuration detail 
    
    <hr>
    
    Getter Method
    
    Signature ``ConfigDetail`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.ConfigurationContextBuilderConfigurationDetail` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConfigDetail`` 
    
    :param configDetail: 
    :type configDetail: :py:class:`NXOpen.PDM.ConfigurationContextBuilderConfigurationDetail` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ConfigMode: ConfigurationContextBuilderConfigContextMode = ...
    """
    Returns  the configuration mode 
    
    <hr>
    
    Getter Method
    
    Signature ``ConfigMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.ConfigurationContextBuilderConfigContextMode` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ConfigType: ConfigurationContextBuilderConfigContextType = ...
    """
    Returns or sets  the configuration type 
    
    <hr>
    
    Getter Method
    
    Signature ``ConfigType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.ConfigurationContextBuilderConfigContextType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConfigType`` 
    
    :param configType: 
    :type configType: :py:class:`NXOpen.PDM.ConfigurationContextBuilderConfigContextType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ContentDefinition: NXOpen.ContentDefinition = ...
    """
    Returns or sets  the :py:class:`NXOpen.ContentDefinition` of the subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``ContentDefinition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ContentDefinition` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContentDefinition`` 
    
    :param contentDefinition: 
    :type contentDefinition: :py:class:`NXOpen.ContentDefinition` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    EffectivityTable: EffectivityTableBuilder = ...
    """
    Returns  the :py:class:`NXOpen.PDM.EffectivityTableBuilder` builder used to edit the effectivity 
    
    <hr>
    
    Getter Method
    
    Signature ``EffectivityTable`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.EffectivityTableBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    OverrideFolder: str = ...
    """
    Returns or sets  the override folder 
    
    <hr>
    
    Getter Method
    
    Signature ``OverrideFolder`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OverrideFolder`` 
    
    :param folderName: 
    :type folderName: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    RevisionRule: str = ...
    """
    Returns or sets  the revision rule  
    
    <hr>
    
    Getter Method
    
    Signature ``RevisionRule`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RevisionRule`` 
    
    :param revisionRule: 
    :type revisionRule: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    VariantConfiguration: VariantConfigurationBuilder = ...
    """
    Returns  the :py:class:`NXOpen.PDM.VariantConfigurationBuilder` builder used to edit variant rule configuration 
    
    <hr>
    
    Getter Method
    
    Signature ``VariantConfiguration`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.VariantConfigurationBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: ConfigurationContextBuilder = ...  # unknown typename


class SmartSaveBuilderSaveTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SmartSaveBuilderSaveType():
    """
    Represents an File Save type   
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Save", "File Save"
       "SaveAll", "File SaveAll"
       "SavePreciseAssembly", "File SavePreciseAssembly"
       "SaveWorkPartOnly", "File SaveWorkPartOnly"
       "SaveAndClose", "File Save And Close"
       "SaveDesignElements", "Save Design Elements"
    """
    Save = 0  # SmartSaveBuilderSaveTypeMemberType
    SaveAll = 1  # SmartSaveBuilderSaveTypeMemberType
    SavePreciseAssembly = 2  # SmartSaveBuilderSaveTypeMemberType
    SaveWorkPartOnly = 3  # SmartSaveBuilderSaveTypeMemberType
    SaveAndClose = 4  # SmartSaveBuilderSaveTypeMemberType
    SaveDesignElements = 5  # SmartSaveBuilderSaveTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SmartSaveBuilder(NXOpen.Builder, NXOpen.IAttributeSourceObjectBuilder):
    """
    TODO: Add a documentation comment describing this class.  
    
    The comment must be placed inside  and should describe conceptually
    what this class represents or does.  Don't use a comment that just states
    something that would be obvious if the comment didn't exist.
    Such comments add no value for the customer.
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreateSmartSaveBuilderWithContext`
    
    .. versionadded:: NX10.0.0
    """
    
    class SaveType():
        """
        Represents an File Save type   
        
        .. versionadded:: NX11.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Save", "File Save"
           "SaveAll", "File SaveAll"
           "SavePreciseAssembly", "File SavePreciseAssembly"
           "SaveWorkPartOnly", "File SaveWorkPartOnly"
           "SaveAndClose", "File Save And Close"
           "SaveDesignElements", "Save Design Elements"
        """
        Save = 0  # SmartSaveBuilderSaveTypeMemberType
        SaveAll = 1  # SmartSaveBuilderSaveTypeMemberType
        SavePreciseAssembly = 2  # SmartSaveBuilderSaveTypeMemberType
        SaveWorkPartOnly = 3  # SmartSaveBuilderSaveTypeMemberType
        SaveAndClose = 4  # SmartSaveBuilderSaveTypeMemberType
        SaveDesignElements = 5  # SmartSaveBuilderSaveTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetSmartSaveObjects(self) -> 'list[SmartSaveObject]':
        """
        Gets the smart save objects for the modified objects in session.  
        
        Signature ``GetSmartSaveObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.SmartSaveObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OnOperationTypeChanged(self, smartSaveObjects: 'list[SmartSaveObject]', operationType: NXOpen.AttributePropertiesBuilderOperationType) -> None:
        """
        Updates the given smart save objects after operation type change.  
        
        Signature ``OnOperationTypeChanged(smartSaveObjects, operationType)`` 
        
        :param smartSaveObjects:  the objects for which operation type is changed 
        :type smartSaveObjects: list of :py:class:`NXOpen.PDM.SmartSaveObject` 
        :param operationType:  the new operation type  
        :type operationType: :py:class:`NXOpen.AttributePropertiesBuilderOperationType` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
        Returns operation failures  
        
        Signature ``GetOperationFailures()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearValidationFailures(self) -> None:
        """
        Clears operation failures if any 
        
        Signature ``ClearValidationFailures()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UpdateSmartSaveObjectsOnBuilder(self) -> None:
        """
        Updates the smart save objects with valid operation type and dependencies 
        
        Signature ``UpdateSmartSaveObjectsOnBuilder()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CanPerformDefaultSave(self) -> bool:
        """
        Checks whether smart save operation can be performed with default operation type set  
        
        Signature ``CanPerformDefaultSave()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ValidateSmartSaveObjects(self) -> None:
        """
        Validates whether the save operation can be performed on the smart save objects 
        
        Signature ``ValidateSmartSaveObjects()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateSpecificationsForSmartSaveObjects(self, smartSaveObjects: 'list[SmartSaveObject]') -> None:
        """
        Create new specifications for Logical Objects 
        
        Signature ``CreateSpecificationsForSmartSaveObjects(smartSaveObjects)`` 
        
        :param smartSaveObjects: 
        :type smartSaveObjects: list of :py:class:`NXOpen.PDM.SmartSaveObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetErrorMessageHandler(self, refresh: bool) -> ErrorMessageHandler:
        """
        Returns ErrorMessageHandler  
        
        Signature ``GetErrorMessageHandler(refresh)`` 
        
        :param refresh: 
        :type refresh: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.ErrorMessageHandler` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AssignRemoveProjects(self, smartSaveObjects: 'list[SmartSaveObject]', projectNames: 'list[str]', assignmentStates: 'list[NXOpen.SessionProjectAssignmentState]') -> None:
        """
        Assign or remove projects to/from objects
        
        Signature ``AssignRemoveProjects(smartSaveObjects, projectNames, assignmentStates)`` 
        
        :param smartSaveObjects:  Array of objects to assign/remove projects to  
        :type smartSaveObjects: list of :py:class:`NXOpen.PDM.SmartSaveObject` 
        :param projectNames:  names of the projects to assign  
        :type projectNames: list of str 
        :param assignmentStates:  assignment states  
        :type assignmentStates: list of :py:class:`NXOpen.SessionProjectAssignmentState` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributes(self, objects: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given array of objects and returns an array of objects that failed to auto assign.  
        
        Signature ``AutoAssignAttributes(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributesWithNamingPattern(self, objects: 'list[NXOpen.NXObject]', properties: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given object and returns an array of objects that failed to auto assign.  
        
        properties needs to be created using :py:meth:`CreateAttributeTitleToNamingPatternMap`
        
        Signature ``AutoAssignAttributesWithNamingPattern(objects, properties)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :param properties: 
        :type properties: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: 'list[str]', titlePatterns: 'list[str]') -> NXOpen.NXObject:
        """
        Creates a map object of attribute titles to their corresponding naming pattern  
        
        Signature ``CreateAttributeTitleToNamingPatternMap(attributeTitles, titlePatterns)`` 
        
        :param attributeTitles: 
        :type attributeTitles: list of str 
        :param titlePatterns: 
        :type titlePatterns: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    DebugDumpEnabled: bool = ...
    """
    Returns or sets  the debug dump enabled 
    
    <hr>
    
    Getter Method
    
    Signature ``DebugDumpEnabled`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DebugDumpEnabled`` 
    
    :param debugDumpEnabled: 
    :type debugDumpEnabled: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    UseNewSortForDebug: bool = ...
    """
    Returns or sets  the new debug sort enabled 
    
    <hr>
    
    Getter Method
    
    Signature ``UseNewSortForDebug`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseNewSortForDebug`` 
    
    :param useNewSortForDebug: 
    :type useNewSortForDebug: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: SmartSaveBuilder = ...  # unknown typename


class PartOperationImportObserver(NXOpen.TaggedObjectCollection):
    """
    This class is responsible for invoking registered callbacks at different stages in import operation.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.PDM.PdmSession`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def AddInitializeCallback(self, initializeCb: typing.Callable) -> int:
        """
        Registers a user defined Initialize callback that is called during initialization of import builder  
        
        Signature ``AddInitializeCallback(initializeCb)`` 
        
        :param initializeCb:  method to register  
        :type initializeCb: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveInitializeCallback(self, id: int) -> None:
        """
        Unregisters the user defined Initialize callback 
        
        Signature ``RemoveInitializeCallback(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddPreAutoassignCallback(self, preAutoassignCb: typing.Callable) -> int:
        """
        Registers a user defined PreAutoAssign callback that is called before auto-assigning attributes  
        
        Signature ``AddPreAutoassignCallback(preAutoassignCb)`` 
        
        :param preAutoassignCb:  method to register  
        :type preAutoassignCb: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemovePreAutoassignCallback(self, id: int) -> None:
        """
        Unregisters the user defined PreAutoAssign callback 
        
        Signature ``RemovePreAutoassignCallback(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddPreCommitCallback(self, preCommitCb: typing.Callable) -> int:
        """
        Registers a user defined PreCommit callback that is called before commit of import operation  
        
        Signature ``AddPreCommitCallback(preCommitCb)`` 
        
        :param preCommitCb:  method to register  
        :type preCommitCb: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemovePreCommitCallback(self, id: int) -> None:
        """
        Unregisters the user defined PreCommit callback 
        
        Signature ``RemovePreCommitCallback(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddPostCommitCallback(self, postCommitCb: typing.Callable) -> int:
        """
        Registers a user defined PostCommit callback that is called after commit of import operation  
        
        Signature ``AddPostCommitCallback(postCommitCb)`` 
        
        :param postCommitCb:  method to register  
        :type postCommitCb: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemovePostCommitCallback(self, id: int) -> None:
        """
        Unregisters the user defined PostCommit callback 
        
        Signature ``RemovePostCommitCallback(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddTerminateCallback(self, terminateCb: typing.Callable) -> int:
        """
        Registers a user defined Terminate callback that is called during destruction of import builder  
        
        Signature ``AddTerminateCallback(terminateCb)`` 
        
        :param terminateCb:  method to register  
        :type terminateCb: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveTerminateCallback(self, id: int) -> None:
        """
        Unregisters the user defined Terminate callback 
        
        Signature ``RemoveTerminateCallback(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class DesignSubordinateRevision(ModelElementRevision):
    """
    Represents the design subordinate revision in the database.  
    
    An instance of this class can be obtained from the :py:class:`NXOpen.Assemblies.Component`.
    
    Instance of this class can not be created
    
    .. versionadded:: NX8.5.0
    """
    DesignPart: NXOpen.Part = ...
    """
    Returns  the underlying loaded part of this subordinate.  
    
    Note that it will return None if part is not loaded.
    
    <hr>
    
    Getter Method
    
    Signature ``DesignPart`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Modified: bool = ...
    """
    Returns 
    whether the selected :py:class:`NXOpen.PDM.DesignSubordinateRevision` is modified in the session.  
    
    <hr>
    
    Getter Method
    
    Signature ``Modified`` 
    
    :returns:  Whether the selected :py:class:`NXOpen.PDM.DesignSubordinateRevision` is modified 
    in the session. 
    :rtype: bool 
    
    .. versionadded:: NX8.5.3
    
    License requirements: None.
    """
    RootDesignElementRevision: DesignElementRevision = ...
    """
    Returns  the root reuse design element revision.  
    
    <hr>
    
    Getter Method
    
    Signature ``RootDesignElementRevision`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.DesignElementRevision` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: DesignSubordinateRevision = ...  # unknown typename


class AttributeGroupCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of attribute group objects.  
    
    A smaller list of attribute groups can be
    retrieved by using the method :py:meth:`NXOpen.PDM.IAttributeGroupOwner.GetAttributeGroups`
    for classes that implement the :py:class:`NXOpen.PDM.IAttributeGroupOwner` interface.  
    To obtain an instance of this class, refer to :py:class:`NXOpen.CollaborativeDesign`
    
    .. versionadded:: NX9.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> AttributeGroup:
        """
        Finds the :py:class:`NXOpen.PDM.AttributeGroup` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier to be found  
        :type journalIdentifier: str 
        :returns:  AttributeGroup found, or null if no such attribute group exists. 
        :rtype: :py:class:`NXOpen.PDM.AttributeGroup` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    


class PartFromPartBuilderFileSaveAsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartFromPartBuilderFileSaveAs():
    """
    This enum is used to specify which non-master parts and dependent files
    should be saved during the save as operation. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Some", "save selected during save as"
       "All", "save all during save as"
       "NotSet", "save none during save as"
    """
    Some = 0  # PartFromPartBuilderFileSaveAsMemberType
    All = 1  # PartFromPartBuilderFileSaveAsMemberType
    NotSet = 2  # PartFromPartBuilderFileSaveAsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartFromPartBuilder(PartBuilder):
    """
    This class provides the methods necessary to create a new part in NX Manager
    from an existing part.  
    
    This class is **deprecated in NX10</b> for "Save As of master parts" operation.
    This class should only be used in case of Save As Non Master parts and
    Save As New Item Type Operations.
    For Save As of master parts, use :py:class:`NXOpen.PDM.PartOperationCopyBuilder`.
    This class will not support Save As if there are duplicate item ids in database.
    
    The operation that this builder supports is equivalent to the file save as operation which can:
    
      #. Copy a non-master dataset into a previously existing item revision,
      #. Save a master dataset (and possibly non-master datasets) into a new revision of the same item,
      #. Save any master or non-master dataset as a completely new item.
    
    The part that is saved is always the work part. If the save is successful, then the newly
    saved part will be the display part.
    
    This class is a singleton meaning only one instance of it can be exist at a time.
    
    .. versionadded:: NX4.0.0
    """
    
    class FileSaveAs():
        """
        This enum is used to specify which non-master parts and dependent files
        should be saved during the save as operation. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Some", "save selected during save as"
           "All", "save all during save as"
           "NotSet", "save none during save as"
        """
        Some = 0  # PartFromPartBuilderFileSaveAsMemberType
        All = 1  # PartFromPartBuilderFileSaveAsMemberType
        NotSet = 2  # PartFromPartBuilderFileSaveAsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateNonmasterList(self) -> None:
        """
        Initializes the list of non-master parts that can be saved during the
        save as operation.  
        
        Deprecated in NX10 for "Save As of master parts" operation. 
        This should only be used in case of Save As New Item Type Operations. 
        For Save As of master parts, use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.CreateNonMasterListForCopyLogicalObject`.
        
        Signature ``CreateNonmasterList()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNonmasterList(self) -> 'list[str]':
        """
        Gets the list of non-master parts.  
        
        Deprecated in NX10 for "Save As of master parts" operation. 
        This should only be used in case of Save As New Item Type Operations. 
        For Save As of master parts, use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.GetNonMasterListForCopyLogicalObject`.
        
        Signature ``GetNonmasterList()`` 
        
        :returns:  Non-master part file names  
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNonmasterToSaveAs(self, partName: str) -> bool:
        """
        Returns whether or not the non-master part specified will actually
        get saved during the save as operation.  
        
        Deprecated in NX10 for "Save As of master parts" operation. 
        This should only be used in case of Save As New Item Type Operations. 
        For Save As of master parts, use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.IsNonMasterForLogicalObjectBeingCopied`.
        
        Signature ``GetNonmasterToSaveAs(partName)`` 
        
        :param partName:  the non-master part that the caller                wants to save or not save  
        :type partName: str 
        :returns:  True means that this non-master will be saved.
        False means that this non-master will not be saved.  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNonmasterToSaveAs(self, partName: str, doSaveAs: bool) -> None:
        """
        Sets whether or not the non-master part specified will actually
        get saved during the save as operation.  
        
        True means that it will be
        saved. False means that it will not be saved.
        
        Deprecated in NX10 for "Save As of master parts" operation. 
        This should only be used in case of Save As New Item Type Operations. 
        For Save As of master parts, use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.SetSelectedNonMasterToCopy`.
        
        Signature ``SetNonmasterToSaveAs(partName, doSaveAs)`` 
        
        :param partName:  the non-master part whose save option is being set here  
        :type partName: str 
        :param doSaveAs:  True means that this non-master part will be saved.                False means that this non-master part will not be saved.  
        :type doSaveAs: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EditNonmasterNameToSaveAs(self, oldName: str, newName: str) -> bool:
        """
        Sets the name the non-master part will get saved as.  
        
        It will get saved as the
        original non-master name if this method is not called.
        
        Deprecated in NX10 for "Save As of master parts" operation. 
        This should only be used in case of Save As New Item Type Operations. 
        For Save As of master parts, use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.EditNonMasterToCopyName`.
        
        Signature ``EditNonmasterNameToSaveAs(oldName, newName)`` 
        
        :param oldName:  the non-master part whose save as name is being set here  
        :type oldName: str 
        :param newName:  the new name  
        :type newName: str 
        :returns:  Whether  or not the name is a valid data set
        name. The name will get set on the builder no matter if it is valid or not.  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Commit(self) -> None:
        """
        Creates the new part that has been fully-specified by calling methods on this
        builder.  
        
        Deprecated in NX10 for "Save As of master parts" operation. 
        This should only be used in case of Save As Non Master parts and Save As New Item Type Operations. 
        For Save As of master parts, use :py:meth:`Builder.Commit`
        instead.
        
        Signature ``Commit()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    DependentFileSaveAsOption: PartFromPartBuilderFileSaveAs = ...
    """
    Returns or sets  the dependent files to save during the save as operation
    
    Deprecated in NX10 for "Save As of master parts" operation. 
    This should only be used in case of Save As New Item Type Operations. 
    For Save As of master parts, use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.DependentFilesToCopyOption`.
    
    <hr>
    
    Getter Method
    
    Signature ``DependentFileSaveAsOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartFromPartBuilderFileSaveAs` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DependentFileSaveAsOption`` 
    
    :param saveOption: 
    :type saveOption: :py:class:`NXOpen.PDM.PartFromPartBuilderFileSaveAs` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    NonmasterSaveAsOption: PartFromPartBuilderFileSaveAs = ...
    """
    Returns or sets  the non-master parts to save during the save as operation
    
    Deprecated in NX10 for "Save As of master parts" operation. 
    This should only be used in case of Save As New Item Type Operations. 
    For Save As of master parts, use :py:meth:`NXOpen.PDM.PartOperationCopyBuilder.GetCopyNonMasterPartsOption`.
    
    <hr>
    
    Getter Method
    
    Signature ``NonmasterSaveAsOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.PartFromPartBuilderFileSaveAs` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NonmasterSaveAsOption`` 
    
    :param saveOption: 
    :type saveOption: :py:class:`NXOpen.PDM.PartFromPartBuilderFileSaveAs` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """


class DatabaseObject(NXOpen.TransientObject):
    """
    Represents a Teamcenter database object   
    
    .. versionadded:: NX11.0.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class ExportWorksetForReferenceBuilder(NXOpen.Builder, NXOpen.IAttributeSourceObjectBuilder):
    """
    Represents a builder class that performs Create operations   
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PdmSession.CreateExportWorksetForReferenceBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def GetObjects(self) -> 'list[NXOpen.NXObject]':
        """
        Gets the objects for the modified objects in session.  
        
        Signature ``GetObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ValidateObjects(self) -> NXOpen.ErrorList:
        """
        Validate the inputs provided for export  
        
        Signature ``ValidateObjects()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributes(self, objects: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given array of objects and returns an array of objects that failed to auto assign.  
        
        Signature ``AutoAssignAttributes(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributesWithNamingPattern(self, objects: 'list[NXOpen.NXObject]', properties: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given object and returns an array of objects that failed to auto assign.  
        
        properties needs to be created using :py:meth:`CreateAttributeTitleToNamingPatternMap`
        
        Signature ``AutoAssignAttributesWithNamingPattern(objects, properties)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :param properties: 
        :type properties: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: 'list[str]', titlePatterns: 'list[str]') -> NXOpen.NXObject:
        """
        Creates a map object of attribute titles to their corresponding naming pattern  
        
        Signature ``CreateAttributeTitleToNamingPatternMap(attributeTitles, titlePatterns)`` 
        
        :param attributeTitles: 
        :type attributeTitles: list of str 
        :param titlePatterns: 
        :type titlePatterns: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    DestinationFolder: str = ...
    """
    Returns or sets  the export directory path 
    
    <hr>
    
    Getter Method
    
    Signature ``DestinationFolder`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DestinationFolder`` 
    
    :param folderPath: 
    :type folderPath: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: ExportWorksetForReferenceBuilder = ...  # unknown typename


class PartCreationObjectAttributePropertiesBuilder(NXOpen.AttributePropertiesBaseBuilder):
    """
    Represents an :py:class:`NXOpen.PDM.PartCreationObjectAttributePropertiesBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.PDM.PartCreationObject.CreateAttributePropertiesBuilder`
    
    Default values.
    
    ==========================  =======
    Property                    Value
    ==========================  =======
    BooleanValue                False 
    --------------------------  -------
    DataType                    String 
    --------------------------  -------
    IntegerValue                0 
    --------------------------  -------
    NumberValue                 0 
    --------------------------  -------
    ObjectPicker (deprecated)   Object 
    ==========================  =======
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX8.5.0
       Use :py:class:`NXOpen.AttributePropertiesBuilder` instead.
    """
    Null: PartCreationObjectAttributePropertiesBuilder = ...  # unknown typename


class PdmPart():
    """
    This class serves as a gateway to part-specific tools for NX Manager mode.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX4.0.0
    """
    
    class CheckoutInput():
        """
        Reservation check-out input struct .  
        
        Constructor: 
        NXOpen.PDM.PdmPart.CheckoutInput()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        InputComment: str = ...
        """
        Field Value
        Type:str
        """
        InputChangeId: str = ...
        """
        Field Value
        Type:str
        """
        AllowRemote: bool = ...
        """
        True to allow remote check out, false otherwise 
        <hr>
        
        Field Value
        Type:bool
        """
        ExplicitCheckOut: bool = ...
        """
        True to perform explicit check out, false otherwise 
        <hr>
        
        Field Value
        Type:bool
        """
        IncludeSecondary: bool = ...
        """
        True to check out secondary dataset, false otherwise 
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    class CheckinInput():
        """
        Reservation check-in input struct .  
        
        Constructor: 
        NXOpen.PDM.PdmPart.CheckinInput()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        AllowRemote: bool = ...
        """
        True to allow remote check in, false otherwise 
        <hr>
        
        Field Value
        Type:bool
        """
        ExplicitCheckIn: bool = ...
        """
        True to perform explicit check in, false otherwise 
        <hr>
        
        Field Value
        Type:bool
        """
        IncludeSecondary: bool = ...
        """
        True to check out secondary dataset, false otherwise 
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    def NewAlternateIdManager(self) -> AlternateIdManager:
        """
        Create an instance of a :py:class:`NXOpen.PDM.AlternateIdManager`
        class that will be used to create alternate ID information on the part.  
        
        Signature ``NewAlternateIdManager()`` 
        
        :returns:  the new :py:class:`NXOpen.PDM.AlternateIdManager` instance  
        :rtype: :py:class:`NXOpen.PDM.AlternateIdManager` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewDatabaseAttributeManager(self) -> DatabaseAttributeManager:
        """
        Create an instance of a :py:class:`NXOpen.PDM.DatabaseAttributeManager`
        class that will be used to modify database attributes of the part.  
        
        Signature ``NewDatabaseAttributeManager()`` 
        
        :returns:  the new :py:class:`NXOpen.PDM.DatabaseAttributeManager` instance  
        :rtype: :py:class:`NXOpen.PDM.DatabaseAttributeManager` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Checkout(self) -> None:
        """
        Checkout the part 
        
        Signature ``Checkout()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AssignPermanentName(self, newFileName: str) -> None:
        """
        Assign a permanent name to the temporary part 
        
        Signature ``AssignPermanentName(newFileName)`` 
        
        :param newFileName:  name of new part file to create  
        :type newFileName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultFolderForPart(self) -> None:
        """
        Set default folder for the part in which it is to be saved 
        
        Signature ``SetDefaultFolderForPart()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CheckoutParts(self, partsToCheckOut: 'list[NXOpen.BasePart]', checkOutInput: PdmPartCheckoutInput_Struct) -> OperationErrors:
        """
        Given an array of parts, check out the parts.  
        
        Signature ``CheckoutParts(partsToCheckOut, checkOutInput)`` 
        
        :param partsToCheckOut:  Array of parts to check out   
        :type partsToCheckOut: list of :py:class:`NXOpen.BasePart` 
        :param checkOutInput:  Input which control the check out behavior  
        :type checkOutInput: :py:class:`NXOpen.PDM.PdmPartCheckoutInput_Struct` 
        :returns:  Errors encountered during the checkout  
        :rtype: :py:class:`NXOpen.PDM.OperationErrors` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CheckinParts(self, partsToCheckIn: 'list[NXOpen.BasePart]', checkInInput: PdmPartCheckinInput_Struct) -> OperationErrors:
        """
        Given an array of parts, check in the parts.  
        
        Signature ``CheckinParts(partsToCheckIn, checkInInput)`` 
        
        :param partsToCheckIn:  Array of parts to check in   
        :type partsToCheckIn: list of :py:class:`NXOpen.BasePart` 
        :param checkInInput:  Input which control the check in behavior  
        :type checkInInput: :py:class:`NXOpen.PDM.PdmPartCheckinInput_Struct` 
        :returns:  Errors encountered during the checkin  
        :rtype: :py:class:`NXOpen.PDM.OperationErrors` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPreciseStructureOnSave(self, partsToSetPreciseOnSave: 'list[NXOpen.BasePart]') -> None:
        """
        Given an array of parts, Parts to set precise structure on save.  
        
        Signature ``SetPreciseStructureOnSave(partsToSetPreciseOnSave)`` 
        
        :param partsToSetPreciseOnSave:  Array of parts to set precise structure on save  
        :type partsToSetPreciseOnSave: list of :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    


class ElementGroup(ConditionalElementRevision):
    """
    Represents a base class that provides common methods for various model elements in a :py:class:`NXOpen.CollaborativeDesign`.  
    
    Instance of this can not directly created.
    
    .. versionadded:: NX11.0.0
    """
    Null: ElementGroup = ...  # unknown typename


class VariantConfigurationBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a builder class that performs variant rule configuration.  
    
    .. versionadded:: NX9.0.0
    """
    
    def AskAvailableVariantRules(self, contextId: str, revId: str) -> 'list[str]':
        """
        Returns the saved variant rules for the give context ID
        The input contextId:
        In case of default domain: it should be Teamcenter item ID.  
        
        In case of non-default domain: it should be the multifield key.
        e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        
        Signature ``AskAvailableVariantRules(contextId, revId)`` 
        
        :param contextId:  multifield key in case of product assembly or collaborative design id  
        :type contextId: str 
        :param revId:  itemRev_id in case of product assembly 
        :type revId: str 
        :returns:  variant rules from the given context  
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetVariantRuleTableInformation(self) -> tuple:
        """
        Returns selected variant rules stored inside :py:class:`NXOpen.PDM.VariantConfigurationBuilder`
        The input contextIds comprising of multifield key and itemRev_id:
        In case of default domain: contextId should contain Teamcenter item ID.  
        
        In case of non-default domain: contextId should contain the multifield keys.
        e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        
        Signature ``GetVariantRuleTableInformation()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (contextIds, variantRules). contextIds is a list of str.   array of contextIds comprising of multifield key and itemRev_id from which variant rules are selected variantRules is a list of str.   array of selected variant rules 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RemoveVariantRule(self, contextId: str, variantRule: str) -> None:
        """
        Removes the given variant rule from :py:class:`NXOpen.PDM.VariantConfigurationBuilder` if applicable
        The input contextId comprising of multifield key and itemRev_id:
        In case of default domain: contextId should contain Teamcenter item ID.  
        
        In case of non-default domain: contextId should contain the multifield keys.
        e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        
        Signature ``RemoveVariantRule(contextId, variantRule)`` 
        
        :param contextId:  context id comprising of multifield key and itemRev_id in which variant rule resides  
        :type contextId: str 
        :param variantRule:  variant rule to be removed  
        :type variantRule: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def AddMultipleVariantRules(self, contextIds: 'list[str]', variantRules: 'list[str]') -> None:
        """
        Adds given variant rules in case of multiple variant rules to :py:class:`NXOpen.PDM.VariantConfigurationBuilder`
        The input contextIds comprising of multifield key and itemRev_id:
        In case of default domain: contextId should contain Teamcenter item ID.  
        
        In case of non-default domain: contextId should contain the multifield keys.
        e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
        
        Signature ``AddMultipleVariantRules(contextIds, variantRules)`` 
        
        :param contextIds:  context id comprising of multifield key and itemRev_id in which variant rule resides  
        :type contextIds: list of str 
        :param variantRules:  variant rules of corresponding context ids to be added  
        :type variantRules: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
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
    
    Null: VariantConfigurationBuilder = ...  # unknown typename


