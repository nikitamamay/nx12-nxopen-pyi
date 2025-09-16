# module 'NXOpen.Issue'
#
# Automatically generated 2025-06-09T14:38:46.874343
#
"""Default documentation for NXOpen.Issue."""

import typing

import NXOpen
import NXOpen.Assemblies



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class IssueAttachmentTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IssueAttachmentType():
    """
    Represents the possible attachment types
    for a :py:class:`NXOpen.Issue.IssueAttachment`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Generic", "Generic type"
       "Text", "Text type"
       "Part", "Part type"
       "Xml", "XML type"
       "Image", "Image type"
       "ValidationLog", "Validation log file"
       "Bookmark", "Bookmark type"
       "Snapshot", "Snapshot type"
       "ValidationResult", "ValidationResult object type"
       "Workset", "Workset type"
       "ShapeDesignElement", "Shape Design Element type"
       "ReuseDesignElement", "Reuse Design Element type"
       "SubordinateDesignElement", "Subordinate Design Element type"
       "PromissoryDesignElement", "Promissory Design Element type"
       "DesignControlElement", "Design Control Element type"
       "Subset", "Subset type"
       "MSWord", "Microsoft Word type"
       "MSExcel", "Microsoft Excel type"
       "MSPowerPoint", "Microsoft Power Point type"
    """
    Generic = 0  # IssueAttachmentTypeMemberType
    Text = 1  # IssueAttachmentTypeMemberType
    Part = 2  # IssueAttachmentTypeMemberType
    Xml = 3  # IssueAttachmentTypeMemberType
    Image = 4  # IssueAttachmentTypeMemberType
    ValidationLog = 5  # IssueAttachmentTypeMemberType
    Bookmark = 6  # IssueAttachmentTypeMemberType
    Snapshot = 7  # IssueAttachmentTypeMemberType
    ValidationResult = 8  # IssueAttachmentTypeMemberType
    Workset = 9  # IssueAttachmentTypeMemberType
    ShapeDesignElement = 10  # IssueAttachmentTypeMemberType
    ReuseDesignElement = 11  # IssueAttachmentTypeMemberType
    SubordinateDesignElement = 12  # IssueAttachmentTypeMemberType
    PromissoryDesignElement = 13  # IssueAttachmentTypeMemberType
    DesignControlElement = 14  # IssueAttachmentTypeMemberType
    Subset = 15  # IssueAttachmentTypeMemberType
    MSWord = 16  # IssueAttachmentTypeMemberType
    MSExcel = 17  # IssueAttachmentTypeMemberType
    MSPowerPoint = 18  # IssueAttachmentTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IssueAttachment(NXOpen.NXObject):
    """
    Represents the Issue Attachment object.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Issue.IssueManager.CreateIssueAttachment`
    
    .. versionadded:: NX8.5.0
    """
    
    class Type():
        """
        Represents the possible attachment types
        for a :py:class:`NXOpen.Issue.IssueAttachment`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Generic", "Generic type"
           "Text", "Text type"
           "Part", "Part type"
           "Xml", "XML type"
           "Image", "Image type"
           "ValidationLog", "Validation log file"
           "Bookmark", "Bookmark type"
           "Snapshot", "Snapshot type"
           "ValidationResult", "ValidationResult object type"
           "Workset", "Workset type"
           "ShapeDesignElement", "Shape Design Element type"
           "ReuseDesignElement", "Reuse Design Element type"
           "SubordinateDesignElement", "Subordinate Design Element type"
           "PromissoryDesignElement", "Promissory Design Element type"
           "DesignControlElement", "Design Control Element type"
           "Subset", "Subset type"
           "MSWord", "Microsoft Word type"
           "MSExcel", "Microsoft Excel type"
           "MSPowerPoint", "Microsoft Power Point type"
        """
        Generic = 0  # IssueAttachmentTypeMemberType
        Text = 1  # IssueAttachmentTypeMemberType
        Part = 2  # IssueAttachmentTypeMemberType
        Xml = 3  # IssueAttachmentTypeMemberType
        Image = 4  # IssueAttachmentTypeMemberType
        ValidationLog = 5  # IssueAttachmentTypeMemberType
        Bookmark = 6  # IssueAttachmentTypeMemberType
        Snapshot = 7  # IssueAttachmentTypeMemberType
        ValidationResult = 8  # IssueAttachmentTypeMemberType
        Workset = 9  # IssueAttachmentTypeMemberType
        ShapeDesignElement = 10  # IssueAttachmentTypeMemberType
        ReuseDesignElement = 11  # IssueAttachmentTypeMemberType
        SubordinateDesignElement = 12  # IssueAttachmentTypeMemberType
        PromissoryDesignElement = 13  # IssueAttachmentTypeMemberType
        DesignControlElement = 14  # IssueAttachmentTypeMemberType
        Subset = 15  # IssueAttachmentTypeMemberType
        MSWord = 16  # IssueAttachmentTypeMemberType
        MSExcel = 17  # IssueAttachmentTypeMemberType
        MSPowerPoint = 18  # IssueAttachmentTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def RecaptureSnapshot(self, bookmarkFileSpec: str, imageFileSpec: str) -> None:
        """
        Recapture the snapshot 
        
        Signature ``RecaptureSnapshot(bookmarkFileSpec, imageFileSpec)`` 
        
        :param bookmarkFileSpec: 
        :type bookmarkFileSpec: str 
        :param imageFileSpec: 
        :type imageFileSpec: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    AttachmentType: IssueAttachmentType = ...
    """
    Returns or sets  the attachment type 
    
    <hr>
    
    Getter Method
    
    Signature ``AttachmentType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.IssueAttachmentType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AttachmentType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Issue.IssueAttachmentType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    ReferencedAttachmentId: str = ...
    """
    Returns or sets  the refereced attachment id which specifies one attachment that is related 
    to this :py:class:`NXOpen.Issue.IssueAttachment` 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferencedAttachmentId`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferencedAttachmentId`` 
    
    :param referencedAttachmentId: 
    :type referencedAttachmentId: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Null: IssueAttachment = ...  # unknown typename


class IssueContentBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Issue.IssueContent` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Issue.IssueManager.CreateIssueContentBuilder`
    
    Default values.
    
    ========  ==========
    Property  Value
    ========  ==========
    Title     New Issue 
    ========  ==========
    
    .. versionadded:: NX8.5.0
    """
    
    def GetEditableUserProperties(self) -> 'list[IssueProperty]':
        """
        Returns the editable user defined :py:class:`NXOpen.Issue.IssueProperty`s  
        
        Signature ``GetEditableUserProperties()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Issue.IssueProperty` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def SetPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        """
        Sets the value of :py:class:`NXOpen.Issue.IssueProperty` 
        
        Signature ``SetPropertyValue(propertyName, propertyValue)`` 
        
        :param propertyName: 
        :type propertyName: str 
        :param propertyValue: 
        :type propertyValue: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetPropertyValue(self, propertyName: str) -> str:
        """
        Returns the value of :py:class:`NXOpen.Issue.IssueProperty`  
        
        Signature ``GetPropertyValue(propertyName)`` 
        
        :param propertyName: 
        :type propertyName: str 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetAllAttachments(self) -> 'list[IssueAttachment]':
        """
        Returns all the :py:class:`NXOpen.Issue.IssueAttachment`s  
        
        Signature ``GetAllAttachments()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetAttachment(self, attachmentName: str) -> IssueAttachment:
        """
        Returns the :py:class:`NXOpen.Issue.IssueAttachment` with this attachment name  
        
        Signature ``GetAttachment(attachmentName)`` 
        
        :param attachmentName: 
        :type attachmentName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def AddAttachment(self, attachment: IssueAttachment) -> None:
        """
        Adds an :py:class:`NXOpen.Issue.IssueAttachment` 
        
        Signature ``AddAttachment(attachment)`` 
        
        :param attachment: 
        :type attachment: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def RemoveAttachment(self, attachment: IssueAttachment) -> None:
        """
        Removes an :py:class:`NXOpen.Issue.IssueAttachment` 
        
        Signature ``RemoveAttachment(attachment)`` 
        
        :param attachment: 
        :type attachment: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def SetPreviewImage(self, attachment: IssueAttachment) -> None:
        """
        Sets preview image 
        
        Signature ``SetPreviewImage(attachment)`` 
        
        :param attachment: 
        :type attachment: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    AssignedUser: str = ...
    """
    Returns or sets  the assigned user 
    
    <hr>
    
    Getter Method
    
    Signature ``AssignedUser`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``AssignedUser`` 
    
    :param assignedUser: 
    :type assignedUser: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Comment: str = ...
    """
    Returns or sets  the issue comment 
    
    <hr>
    
    Getter Method
    
    Signature ``Comment`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``Comment`` 
    
    :param comment: 
    :type comment: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    DueDate: str = ...
    """
    Returns or sets  the due date 
    
    <hr>
    
    Getter Method
    
    Signature ``DueDate`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``DueDate`` 
    
    :param dueDate: 
    :type dueDate: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Priority: str = ...
    """
    Returns or sets  the issue priority 
    
    <hr>
    
    Getter Method
    
    Signature ``Priority`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``Priority`` 
    
    :param priority: 
    :type priority: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Status: str = ...
    """
    Returns or sets  the issue status 
    
    <hr>
    
    Getter Method
    
    Signature ``Status`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``Status`` 
    
    :param status: 
    :type status: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Title: str = ...
    """
    Returns or sets  the issue title 
    
    <hr>
    
    Getter Method
    
    Signature ``Title`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``Title`` 
    
    :param title: 
    :type title: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Null: IssueContentBuilder = ...  # unknown typename


class IssueList(NXOpen.NXObject):
    """
    Represents the Issue List object.  
    
    .. versionadded:: NX8.5.0
    """
    
    def ReloadIssues(self) -> None:
        """
        Reloads the :py:class:`NXOpen.Issue.IssueContent`s 
        
        Signature ``ReloadIssues()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetIssues(self) -> 'list[IssueContent]':
        """
        Returns all the :py:class:`NXOpen.Issue.IssueContent`s  
        
        Signature ``GetIssues()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Issue.IssueContent` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def ExistsInDatabase(self) -> bool:
        """
        Returns whether the list exists in database  
        
        Signature ``ExistsInDatabase()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def SaveChanges(self) -> None:
        """
        Saves the modified :py:class:`NXOpen.Issue.IssueContent`s 
        
        Signature ``SaveChanges()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def DiscardChanges(self) -> None:
        """
        Discards the modified :py:class:`NXOpen.Issue.IssueContent`s 
        
        Signature ``DiscardChanges()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def SaveConfig(self) -> None:
        """
        Saves the config of :py:class:`NXOpen.Issue.IssueList` to server 
        
        Signature ``SaveConfig()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def ResetConfig(self) -> None:
        """
        Resets the config of :py:class:`NXOpen.Issue.IssueList` 
        
        Signature ``ResetConfig()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def ChangeConfig(self, queryName: str, criteriaTitles: 'list[str]', criteriaValues: 'list[str]') -> None:
        """
        Changes the config of :py:class:`NXOpen.Issue.IssueList` 
        
        Signature ``ChangeConfig(queryName, criteriaTitles, criteriaValues)`` 
        
        :param queryName:  The saved query name  
        :type queryName: str 
        :param criteriaTitles:  The query critetia titles  
        :type criteriaTitles: list of str 
        :param criteriaValues:  The query critetia values  
        :type criteriaValues: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def SetRelatedParts(self, parts: 'list[NXOpen.NXObject]') -> None:
        """
        Sets the related parts of :py:class:`NXOpen.Issue.IssueList` 
        
        Signature ``SetRelatedParts(parts)`` 
        
        :param parts: 
        :type parts: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    Null: IssueList = ...  # unknown typename


class IssueBriefcase(IssueList):
    """
    Represents the Issue Briefcase object.  
    
    .. versionadded:: NX10.0.0
    """
    
    def AddIssue(self, issue: IssueContent) -> None:
        """
        Adds an :py:class:`NXOpen.Issue.IssueContent` from an existing :py:class:`NXOpen.Issue.IssueContent`.  
        
        Signature ``AddIssue(issue)`` 
        
        :param issue: 
        :type issue: :py:class:`NXOpen.Issue.IssueContent` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def RemoveIssue(self, issue: IssueContent) -> None:
        """
        Removes an :py:class:`NXOpen.Issue.IssueContent`.  
        
        Signature ``RemoveIssue(issue)`` 
        
        :param issue: 
        :type issue: :py:class:`NXOpen.Issue.IssueContent` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def Save(self) -> None:
        """
        Saves all :py:class:`NXOpen.Issue.IssueContent`s.  
        
        Signature ``Save()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def Close(self) -> None:
        """
        Closes :py:class:`NXOpen.Issue.IssueBriefcase`.  
        
        Signature ``Close()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def CreateSynchronizeContentBuilder(self) -> IssueBriefcaseSynchronizeBuilder:
        """
        Creates an :py:class:`NXOpen.Issue.IssueBriefcaseSynchronizeBuilder`  
        
        Signature ``CreateSynchronizeContentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueBriefcaseSynchronizeBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    Location: str = ...
    """
    Returns or sets  the briefcase location
    
    <hr>
    
    Getter Method
    
    Signature ``Location`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Location`` 
    
    :param folder: 
    :type folder: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Null: IssueBriefcase = ...  # unknown typename


class IssueFolderTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IssueFolderType():
    """
    Represents the possible folder types
    for a :py:class:`NXOpen.Issue.IssueFolder`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ProblemItems", "Problem items type"
       "ImpactedItems", "Impacted items type"
       "ReferenceItems", "Reference items type"
       "ImplementedBy", "Implemented by type"
       "IssueImage", "Issue image type"
       "IssueFixedImage", "Issue fixed image type"
       "SnapshotBeforeFix", "Snapshot before fix type"
       "SnapshotAfterFix", "Snapshot after fix type"
       "ValidationResults", "ValidationResult type"
    """
    ProblemItems = 0  # IssueFolderTypeMemberType
    ImpactedItems = 1  # IssueFolderTypeMemberType
    ReferenceItems = 2  # IssueFolderTypeMemberType
    ImplementedBy = 3  # IssueFolderTypeMemberType
    IssueImage = 4  # IssueFolderTypeMemberType
    IssueFixedImage = 5  # IssueFolderTypeMemberType
    SnapshotBeforeFix = 6  # IssueFolderTypeMemberType
    SnapshotAfterFix = 7  # IssueFolderTypeMemberType
    ValidationResults = 8  # IssueFolderTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IssueFolder(NXOpen.NXObject):
    """
    Represents the Issue Folder object.  
    
    .. versionadded:: NX8.5.0
    """
    
    class Type():
        """
        Represents the possible folder types
        for a :py:class:`NXOpen.Issue.IssueFolder`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ProblemItems", "Problem items type"
           "ImpactedItems", "Impacted items type"
           "ReferenceItems", "Reference items type"
           "ImplementedBy", "Implemented by type"
           "IssueImage", "Issue image type"
           "IssueFixedImage", "Issue fixed image type"
           "SnapshotBeforeFix", "Snapshot before fix type"
           "SnapshotAfterFix", "Snapshot after fix type"
           "ValidationResults", "ValidationResult type"
        """
        ProblemItems = 0  # IssueFolderTypeMemberType
        ImpactedItems = 1  # IssueFolderTypeMemberType
        ReferenceItems = 2  # IssueFolderTypeMemberType
        ImplementedBy = 3  # IssueFolderTypeMemberType
        IssueImage = 4  # IssueFolderTypeMemberType
        IssueFixedImage = 5  # IssueFolderTypeMemberType
        SnapshotBeforeFix = 6  # IssueFolderTypeMemberType
        SnapshotAfterFix = 7  # IssueFolderTypeMemberType
        ValidationResults = 8  # IssueFolderTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetAttachments(self) -> 'list[IssueAttachment]':
        """
        Returns the child :py:class:`NXOpen.Issue.IssueAttachment`s  
        
        Signature ``GetAttachments()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def AddAttachment(self, attachment: IssueAttachment) -> None:
        """
        Adds an :py:class:`NXOpen.Issue.IssueAttachment` 
        
        Signature ``AddAttachment(attachment)`` 
        
        :param attachment: 
        :type attachment: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def RemoveAttachment(self, attachment: IssueAttachment) -> None:
        """
        Removes an :py:class:`NXOpen.Issue.IssueAttachment` 
        
        Signature ``RemoveAttachment(attachment)`` 
        
        :param attachment: 
        :type attachment: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    FolderType: IssueFolderType = ...
    """
    Returns  the folder type 
    
    <hr>
    
    Getter Method
    
    Signature ``FolderType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.IssueFolderType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Null: IssueFolder = ...  # unknown typename


class SnapshotSubsetBuilderContextTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SnapshotSubsetBuilderContextType():
    """
    The option specifying which kinds of issue snapshot subset should be created. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Problem", "Problem Subset"
       "Impacted", "Impacted Subset"
       "Reference", "Reference Subset"
    """
    Problem = 0  # SnapshotSubsetBuilderContextTypeMemberType
    Impacted = 1  # SnapshotSubsetBuilderContextTypeMemberType
    Reference = 2  # SnapshotSubsetBuilderContextTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SnapshotSubsetBuilder(NXOpen.Builder):
    """
    Used to create or edit issue snapshot subset.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Issue.IssueManager.CreateIssueSnapshotSubsetBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    class ContextType():
        """
        The option specifying which kinds of issue snapshot subset should be created. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Problem", "Problem Subset"
           "Impacted", "Impacted Subset"
           "Reference", "Reference Subset"
        """
        Problem = 0  # SnapshotSubsetBuilderContextTypeMemberType
        Impacted = 1  # SnapshotSubsetBuilderContextTypeMemberType
        Reference = 2  # SnapshotSubsetBuilderContextTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Context: SnapshotSubsetBuilderContextType = ...
    """
    Returns or sets  the context indicating the issue snapshot subset type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Context`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.SnapshotSubsetBuilderContextType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Context`` 
    
    :param context: 
    :type context: :py:class:`NXOpen.Issue.SnapshotSubsetBuilderContextType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    SelectParts: NXOpen.Assemblies.SelectComponentList = ...
    """
    Returns  the select parts which will be collected into issue snapshot subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectParts`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SnapshotSubsetBuilder = ...  # unknown typename


class IssueListCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a :py:class:`NXOpen.Issue.IssueListCollection`   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Issue.IssueManager`
    
    .. versionadded:: NX8.5.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, name: str) -> IssueList:
        """
        Finds the :py:class:`NXOpen.Issue.IssueList` with the given name.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(name)`` 
        
        :param name:  The name of the :py:class:`NXOpen.Issue.IssueList`.  
        :type name: str 
        :returns:  :py:class:`NXOpen.Issue.IssueList` with this name.  
        :rtype: :py:class:`NXOpen.Issue.IssueList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    


class IssueBriefcaseSynchronizeBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Issue.IssueBriefcase` synchronize builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Issue.IssueBriefcase.CreateSynchronizeContentBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def AddPartAttachment(self, attachment: IssueAttachment) -> None:
        """
        Adds an part type :py:class:`NXOpen.Issue.IssueAttachment`,
        only the added parts can be synchronized to server.  
        
        Signature ``AddPartAttachment(attachment)`` 
        
        :param attachment: 
        :type attachment: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def RemovePartAttachment(self, attachment: IssueAttachment) -> None:
        """
        Adds an part type :py:class:`NXOpen.Issue.IssueAttachment`.  
        
        Signature ``RemovePartAttachment(attachment)`` 
        
        :param attachment: 
        :type attachment: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    Null: IssueBriefcaseSynchronizeBuilder = ...  # unknown typename


class SnapshotWorksetBuilder(NXOpen.Builder):
    """
    Used to create or edit issue snapshot workset which is a container to hold all the corresponding 
    parts to represent an issue.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Issue.IssueManager.CreateIssueSnapshotWorksetBuilder`
    
    .. versionadded:: NX9.0.0
    """
    ImpactedSubset: SnapshotSubsetBuilder = ...
    """
    Returns  the impactedSubset containing the impacted parts.  
    
    <hr>
    
    Getter Method
    
    Signature ``ImpactedSubset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.SnapshotSubsetBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ProblemSubset: SnapshotSubsetBuilder = ...
    """
    Returns  the problemSubset containing the problem parts.  
    
    <hr>
    
    Getter Method
    
    Signature ``ProblemSubset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.SnapshotSubsetBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ReferenceSubset: SnapshotSubsetBuilder = ...
    """
    Returns  the referenceSubset containing the reference parts.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSubset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.SnapshotSubsetBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SnapshotWorksetBuilder = ...  # unknown typename


class IssueContent(NXOpen.NXObject):
    """
    Represents the Issue Issue object.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Issue.IssueManager.CreateIssueContent`
    
    .. versionadded:: NX8.5.0
    """
    
    def GetUserProperties(self) -> 'list[IssueProperty]':
        """
        Returns the user definded :py:class:`NXOpen.Issue.IssueProperty`s  
        
        Signature ``GetUserProperties()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Issue.IssueProperty` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetProperty(self, propertyName: str) -> IssueProperty:
        """
        Returns the :py:class:`NXOpen.Issue.IssueProperty` with this property name  
        
        Signature ``GetProperty(propertyName)`` 
        
        :param propertyName: 
        :type propertyName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueProperty` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def ReloadProperties(self) -> None:
        """
        Reloads all the :py:class:`NXOpen.Issue.IssueProperty`s 
        
        Signature ``ReloadProperties()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def SetPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        """
        Sets the value of :py:class:`NXOpen.Issue.IssueProperty` 
        
        Signature ``SetPropertyValue(propertyName, propertyValue)`` 
        
        :param propertyName: 
        :type propertyName: str 
        :param propertyValue: 
        :type propertyValue: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetPropertyValue(self, propertyName: str) -> str:
        """
        Returns the value of :py:class:`NXOpen.Issue.IssueProperty`  
        
        Signature ``GetPropertyValue(propertyName)`` 
        
        :param propertyName: 
        :type propertyName: str 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetAllAttachments(self) -> 'list[IssueAttachment]':
        """
        Returns all the :py:class:`NXOpen.Issue.IssueAttachment`s  
        
        Signature ``GetAllAttachments()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetChildAttachments(self) -> 'list[IssueAttachment]':
        """
        Returns the child :py:class:`NXOpen.Issue.IssueAttachment`s  
        
        Signature ``GetChildAttachments()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetAttachment(self, attachmentName: str) -> IssueAttachment:
        """
        Returns the :py:class:`NXOpen.Issue.IssueAttachment` with this attachment name  
        
        Signature ``GetAttachment(attachmentName)`` 
        
        :param attachmentName: 
        :type attachmentName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetPartAttachment(self) -> IssueAttachment:
        """
        Returns the :py:class:`NXOpen.Issue.IssueAttachment` with part type  
        
        Signature ``GetPartAttachment()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def LoadAttachments(self) -> None:
        """
        Loads the :py:class:`NXOpen.Issue.IssueAttachment`s 
        
        Signature ``LoadAttachments()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def AddAttachment(self, attachment: IssueAttachment) -> None:
        """
        Adds an :py:class:`NXOpen.Issue.IssueAttachment` 
        
        Signature ``AddAttachment(attachment)`` 
        
        :param attachment: 
        :type attachment: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def RemoveAttachment(self, attachment: IssueAttachment) -> None:
        """
        Removes an :py:class:`NXOpen.Issue.IssueAttachment` 
        
        Signature ``RemoveAttachment(attachment)`` 
        
        :param attachment: 
        :type attachment: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetFolders(self) -> 'list[IssueFolder]':
        """
        Returns all the child :py:class:`NXOpen.Issue.IssueFolder`s  
        
        Signature ``GetFolders()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Issue.IssueFolder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def SaveChanges(self) -> None:
        """
        Saves the changes to issue server 
        
        Signature ``SaveChanges()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def DiscardIssue(self) -> None:
        """
        Discards the newly created issue which has not saved in external db yet 
        
        Signature ``DiscardIssue()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def IsCheckedOut(self) -> tuple:
        """
        Returns whether the issue is checked out   
        
        Signature ``IsCheckedOut()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (isCheckOut, user). isCheckOut is a bool. user is a str. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def Close(self, coseNote: str) -> None:
        """
        Closes the issue 
        
        Signature ``Close(coseNote)`` 
        
        :param coseNote: 
        :type coseNote: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def IsClosed(self) -> bool:
        """
        Returns whether the issue is closed  
        
        Signature ``IsClosed()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def IsReadOnly(self) -> bool:
        """
        Returns whether the issue is read only  
        
        Signature ``IsReadOnly()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def SendToWorkflow(self, workflowTemplate: str) -> None:
        """
        Sends the issue to workflow process 
        
        Signature ``SendToWorkflow(workflowTemplate)`` 
        
        :param workflowTemplate: 
        :type workflowTemplate: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def Review(self, reviewDecision: str, comment: str) -> None:
        """
        Signs off the current workflow task with decision 
        
        Signature ``Review(reviewDecision, comment)`` 
        
        :param reviewDecision: 
        :type reviewDecision: str 
        :param comment: 
        :type comment: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    AssignedUser: str = ...
    """
    Returns or sets  the assigned user 
    
    <hr>
    
    Getter Method
    
    Signature ``AssignedUser`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``AssignedUser`` 
    
    :param assignedUser: 
    :type assignedUser: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Comment: str = ...
    """
    Returns or sets  the issue comment 
    
    <hr>
    
    Getter Method
    
    Signature ``Comment`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``Comment`` 
    
    :param comment: 
    :type comment: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    DueDate: str = ...
    """
    Returns or sets  the due date 
    
    <hr>
    
    Getter Method
    
    Signature ``DueDate`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``DueDate`` 
    
    :param dueDate: 
    :type dueDate: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    IsLocked: bool = ...
    """
    Returns  the lock state 
    
    <hr>
    
    Getter Method
    
    Signature ``IsLocked`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    IssueId: str = ...
    """
    Returns  the issue id 
    
    <hr>
    
    Getter Method
    
    Signature ``IssueId`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    PreviewImage: IssueAttachment = ...
    """
    Returns or sets  the preview image 
    
    <hr>
    
    Getter Method
    
    Signature ``PreviewImage`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.IssueAttachment` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``PreviewImage`` 
    
    :param previewImage: 
    :type previewImage: :py:class:`NXOpen.Issue.IssueAttachment` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Priority: str = ...
    """
    Returns or sets  the issue priority 
    
    <hr>
    
    Getter Method
    
    Signature ``Priority`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``Priority`` 
    
    :param priority: 
    :type priority: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Status: str = ...
    """
    Returns or sets  the issue status 
    
    <hr>
    
    Getter Method
    
    Signature ``Status`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``Status`` 
    
    :param status: 
    :type status: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Title: str = ...
    """
    Returns or sets  the issue title 
    
    <hr>
    
    Getter Method
    
    Signature ``Title`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    
    <hr>
    
    Setter Method
    
    Signature ``Title`` 
    
    :param title: 
    :type title: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Null: IssueContent = ...  # unknown typename


class IssueSite(NXOpen.NXObject):
    """
    Represents the Issue Site object.  
    
    .. versionadded:: NX8.5.0
    """
    
    def IsConnected(self) -> bool:
        """
        Returns whether the site is connected  
        
        Signature ``IsConnected()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def RemoveList(self, list: IssueList) -> None:
        """
        Removes an :py:class:`NXOpen.Issue.IssueList` 
        
        Signature ``RemoveList(list)`` 
        
        :param list: 
        :type list: :py:class:`NXOpen.Issue.IssueList` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def CreateList(self, listName: str, queryName: str, criteriaTitles: 'list[str]', criteriaValues: 'list[str]') -> IssueList:
        """
        Creates an :py:class:`NXOpen.Issue.IssueList`  
        
        Signature ``CreateList(listName, queryName, criteriaTitles, criteriaValues)`` 
        
        :param listName:  The list name  
        :type listName: str 
        :param queryName:  The saved query name  
        :type queryName: str 
        :param criteriaTitles:  The query criteria titles  
        :type criteriaTitles: list of str 
        :param criteriaValues:  The query criteria values  
        :type criteriaValues: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueList` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetQuickSearchList(self) -> IssueList:
        """
        Gets the :py:class:`NXOpen.Issue.IssueList` for quick search  
        
        Signature ``GetQuickSearchList()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueList` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    Null: IssueSite = ...  # unknown typename


class IssuePropertyTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IssuePropertyType():
    """
    Represents the possible property types.
    for a :py:class:`NXOpen.Issue.IssueProperty`.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Text", "Text type"
       "Note", "Note type"
       "User", "User type"
       "Choice", "Choice type"
       "Url", "URL type"
       "Boolean", "Boolean type"
       "Date", "Date type"
       "Number", "Number type"
       "Integer", "Integer type"
       "Point3D", "3D point type"
       "Vector3D", "3D vector type"
    """
    Text = 0  # IssuePropertyTypeMemberType
    Note = 1  # IssuePropertyTypeMemberType
    User = 2  # IssuePropertyTypeMemberType
    Choice = 3  # IssuePropertyTypeMemberType
    Url = 4  # IssuePropertyTypeMemberType
    Boolean = 5  # IssuePropertyTypeMemberType
    Date = 6  # IssuePropertyTypeMemberType
    Number = 7  # IssuePropertyTypeMemberType
    Integer = 8  # IssuePropertyTypeMemberType
    Point3D = 9  # IssuePropertyTypeMemberType
    Vector3D = 10  # IssuePropertyTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IssueProperty(NXOpen.NXObject):
    """
    Represents the Issue Property object.  
    
    .. versionadded:: NX8.5.0
    """
    
    class Type():
        """
        Represents the possible property types.
        for a :py:class:`NXOpen.Issue.IssueProperty`.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Text", "Text type"
           "Note", "Note type"
           "User", "User type"
           "Choice", "Choice type"
           "Url", "URL type"
           "Boolean", "Boolean type"
           "Date", "Date type"
           "Number", "Number type"
           "Integer", "Integer type"
           "Point3D", "3D point type"
           "Vector3D", "3D vector type"
        """
        Text = 0  # IssuePropertyTypeMemberType
        Note = 1  # IssuePropertyTypeMemberType
        User = 2  # IssuePropertyTypeMemberType
        Choice = 3  # IssuePropertyTypeMemberType
        Url = 4  # IssuePropertyTypeMemberType
        Boolean = 5  # IssuePropertyTypeMemberType
        Date = 6  # IssuePropertyTypeMemberType
        Number = 7  # IssuePropertyTypeMemberType
        Integer = 8  # IssuePropertyTypeMemberType
        Point3D = 9  # IssuePropertyTypeMemberType
        Vector3D = 10  # IssuePropertyTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetChoices(self) -> 'list[str]':
        """
        Returns the choices   
        
        Signature ``GetChoices()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetDefaultChoice(self) -> str:
        """
        Returns the default choice   
        
        Signature ``GetDefaultChoice()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    IsReadOnly: bool = ...
    """
    Returns  whether the property is read only 
    
    <hr>
    
    Getter Method
    
    Signature ``IsReadOnly`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    StringValue: str = ...
    """
    Returns  the string value 
    
    <hr>
    
    Getter Method
    
    Signature ``StringValue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    ValueType: IssuePropertyType = ...
    """
    Returns  the property type 
    
    <hr>
    
    Getter Method
    
    Signature ``ValueType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.IssuePropertyType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    Null: IssueProperty = ...  # unknown typename


class IssueManagerModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IssueManagerMode():
    """
    Represents the possible issue site modes.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "TeamcenterCommunity", "Teamcenter community mode"
       "Teamcenter", "Teamcenter mode"
       "Briefcase", "Briefcase mode"
    """
    TeamcenterCommunity = 0  # IssueManagerModeMemberType
    Teamcenter = 1  # IssueManagerModeMemberType
    Briefcase = 2  # IssueManagerModeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IssueManagerStateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IssueManagerState():
    """
    Represents the possible issue object states.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Original", "Original state"
       "Created", "Created state"
       "Modified", "Modified state"
       "Removed", "Removed state"
    """
    Original = 0  # IssueManagerStateMemberType
    Created = 1  # IssueManagerStateMemberType
    Modified = 2  # IssueManagerStateMemberType
    Removed = 3  # IssueManagerStateMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IssueManager():
    """
    Contains the collection objects for creating and iterating over issue objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX8.5.0
    """
    
    class Mode():
        """
        Represents the possible issue site modes.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "TeamcenterCommunity", "Teamcenter community mode"
           "Teamcenter", "Teamcenter mode"
           "Briefcase", "Briefcase mode"
        """
        TeamcenterCommunity = 0  # IssueManagerModeMemberType
        Teamcenter = 1  # IssueManagerModeMemberType
        Briefcase = 2  # IssueManagerModeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class State():
        """
        Represents the possible issue object states.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Original", "Original state"
           "Created", "Created state"
           "Modified", "Modified state"
           "Removed", "Removed state"
        """
        Original = 0  # IssueManagerStateMemberType
        Created = 1  # IssueManagerStateMemberType
        Modified = 2  # IssueManagerStateMemberType
        Removed = 3  # IssueManagerStateMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreateIssueContent(self, list: IssueList) -> IssueContent:
        """
        Creates a :py:class:`NXOpen.Issue.IssueContent`  
        
        Signature ``CreateIssueContent(list)`` 
        
        :param list: 
        :type list: :py:class:`NXOpen.Issue.IssueList` 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueContent` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def CreateIssueAttachment(self, fileSpec: str, name: str, type: IssueAttachmentType) -> IssueAttachment:
        """
        Creates a :py:class:`NXOpen.Issue.IssueAttachment`  
        
        Signature ``CreateIssueAttachment(fileSpec, name, type)`` 
        
        :param fileSpec: 
        :type fileSpec: str 
        :param name: 
        :type name: str 
        :param type: 
        :type type: :py:class:`NXOpen.Issue.IssueAttachmentType` 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def CreateIssueContentBuilder(self, issue: IssueContent) -> IssueContentBuilder:
        """
        Creates a :py:class:`NXOpen.Issue.IssueContentBuilder`  
        
        Signature ``CreateIssueContentBuilder(issue)`` 
        
        :param issue: 
        :type issue: :py:class:`NXOpen.Issue.IssueContent` 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueContentBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def Connect(self, siteUrl: str, userName: str, password: str) -> IssueSite:
        """
        Connects to issue server and returns the :py:class:`NXOpen.Issue.IssueSite`  
        
        Signature ``Connect(siteUrl, userName, password)`` 
        
        :param siteUrl: 
        :type siteUrl: str 
        :param userName: 
        :type userName: str 
        :param password: 
        :type password: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueSite` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def Disconnect(self) -> None:
        """
        Disconnects from issue server 
        
        Signature ``Disconnect()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetWorkingList(self) -> IssueList:
        """
        Gets the current working :py:class:`NXOpen.Issue.IssueList`  
        
        Signature ``GetWorkingList()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetWorkingList(self, list: IssueList) -> None:
        """
        Sets the current working :py:class:`NXOpen.Issue.IssueList` 
        
        Signature ``SetWorkingList(list)`` 
        
        :param list: 
        :type list: :py:class:`NXOpen.Issue.IssueList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def GetIssueState(self, issue: IssueContent) -> IssueManagerState:
        """
        Gets the modified state of :py:class:`NXOpen.Issue.IssueContent`  
        
        Signature ``GetIssueState(issue)`` 
        
        :param issue: 
        :type issue: :py:class:`NXOpen.Issue.IssueContent` 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueManagerState` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAttachmentState(self, attachment: IssueAttachment) -> IssueManagerState:
        """
        Gets the modified state of :py:class:`NXOpen.Issue.IssueAttachment`  
        
        Signature ``GetAttachmentState(attachment)`` 
        
        :param attachment: 
        :type attachment: :py:class:`NXOpen.Issue.IssueAttachment` 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueManagerState` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPropertyState(self, property: IssueProperty) -> IssueManagerState:
        """
        Gets the modified state of :py:class:`NXOpen.Issue.IssueProperty`  
        
        Signature ``GetPropertyState(property)`` 
        
        :param property: 
        :type property: :py:class:`NXOpen.Issue.IssueProperty` 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueManagerState` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateIssueSnapshotSubsetBuilder(self, subsetPart: NXOpen.Part) -> SnapshotSubsetBuilder:
        """
        Creates a :py:class:`NXOpen.Issue.SnapshotSubsetBuilder`  
        
        Signature ``CreateIssueSnapshotSubsetBuilder(subsetPart)`` 
        
        :param subsetPart: 
        :type subsetPart: :py:class:`NXOpen.Part` 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.SnapshotSubsetBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def CreateIssueSnapshotWorksetBuilder(self, issue: IssueContent) -> SnapshotWorksetBuilder:
        """
        Creates a :py:class:`NXOpen.Issue.SnapshotWorksetBuilder`  
        
        Signature ``CreateIssueSnapshotWorksetBuilder(issue)`` 
        
        :param issue: 
        :type issue: :py:class:`NXOpen.Issue.IssueContent` 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.SnapshotWorksetBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def CreateAttachmentForSnapshot(self, bookmarkFileSpec: str, imageFileSpec: str, name: str) -> IssueAttachment:
        """
        Creates a :py:class:`NXOpen.Issue.IssueAttachment` for Sanpshot  
        
        Signature ``CreateAttachmentForSnapshot(bookmarkFileSpec, imageFileSpec, name)`` 
        
        :param bookmarkFileSpec:  The bookmark file  
        :type bookmarkFileSpec: str 
        :param imageFileSpec:  The image file  
        :type imageFileSpec: str 
        :param name:  The name of snapshot attachment  
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def CreateAttachmentForScreenImage(self) -> IssueAttachment:
        """
        Creates a :py:class:`NXOpen.Issue.IssueAttachment` for ScreenImage  
        
        Signature ``CreateAttachmentForScreenImage()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def CreateAttachmentForBookMark(self) -> IssueAttachment:
        """
        Creates a :py:class:`NXOpen.Issue.IssueAttachment` for BookMark  
        
        Signature ``CreateAttachmentForBookMark()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def CaptureAndCreateAttachmentForSnapshot(self) -> IssueAttachment:
        """
        Creates a :py:class:`NXOpen.Issue.IssueAttachment` for Snapshot  
        
        Signature ``CaptureAndCreateAttachmentForSnapshot()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueAttachment` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def CreateBriefcase(self, briefcaseName: str, filePath: str) -> IssueBriefcase:
        """
        Creates an :py:class:`NXOpen.Issue.IssueBriefcase`.  
        
        Signature ``CreateBriefcase(briefcaseName, filePath)`` 
        
        :param briefcaseName:  The briefcase name  
        :type briefcaseName: str 
        :param filePath:  The briefcase work root path  
        :type filePath: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueBriefcase` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    
    def OpenBriefcase(self, filePath: str) -> IssueBriefcase:
        """
        Opens an :py:class:`NXOpen.Issue.IssueBriefcase` .  
        
        Signature ``OpenBriefcase(filePath)`` 
        
        :param filePath:  The briefcase file path  
        :type filePath: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Issue.IssueBriefcase` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_issue_mgmt ("NX Issue Tracking")
        """
        ...
    
    CurrentMode: IssueManagerMode = ...
    """
    Returns or sets  the current mode 
    
    <hr>
    
    Getter Method
    
    Signature ``CurrentMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.IssueManagerMode` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurrentMode`` 
    
    :param mode: 
    :type mode: :py:class:`NXOpen.Issue.IssueManagerMode` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    CurrentSite: IssueSite = ...
    """
    Returns  the current :py:class:`NXOpen.Issue.IssueSite` 
    
    <hr>
    
    Getter Method
    
    Signature ``CurrentSite`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.IssueSite` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_issue_mgmt ("NX Issue Tracking")
    """
    IssueListCollection: IssueListCollection = ...
    """
    Returns the :py:class:`NXOpen.Issue.IssueListCollection` instance 
    
    Signature ``IssueListCollection`` 
    
    .. versionadded:: NX8.5.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Issue.IssueListCollection`
    """


