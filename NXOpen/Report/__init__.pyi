# module 'NXOpen.Report'
#
# Automatically generated 2025-06-09T14:38:47.319808
#
"""Default documentation for NXOpen.Report."""

import typing

import NXOpen
import NXOpen.Assemblies
import NXOpen.OpenXml



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class ResultXmlFileWriter(NXOpen.TransientObject):
    """
    Contains methods for adding document data and generating result XML file 
    for CAE Report.  
    
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
    
    
    def AddText(self, textContent: str) -> NXOpen.OpenXml.TextDocumentData:
        """
        Creates a new :py:class:`NXOpen.OpenXml.TextDocumentData` object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.Report.ResultXmlFileWriter` object 
        
        Signature ``AddText(textContent)`` 
        
        :param textContent:  the content of the text data 
        :type textContent: str 
        :returns:  the text data  
        :rtype: :py:class:`NXOpen.OpenXml.TextDocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddImageGroup(self) -> NXOpen.OpenXml.ImageGroupDocumentData:
        """
        Creates a new :py:class:`NXOpen.OpenXml.ImageGroupDocumentData` object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.Report.ResultXmlFileWriter` object 
        
        Signature ``AddImageGroup()`` 
        
        :returns:  the image group data  
        :rtype: :py:class:`NXOpen.OpenXml.ImageGroupDocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddTable(self, columnSize: int, rowSize: int) -> NXOpen.OpenXml.TableDocumentData:
        """
        Creates a new :py:class:`NXOpen.OpenXml.TableDocumentData` object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.Report.ResultXmlFileWriter` object 
        
        Signature ``AddTable(columnSize, rowSize)`` 
        
        :param columnSize:  the column size of the table 
        :type columnSize: int 
        :param rowSize:  the row size of the table 
        :type rowSize: int 
        :returns:  the table data  
        :rtype: :py:class:`NXOpen.OpenXml.TableDocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDataCount(self) -> int:
        """
        Gets the number of data to be exported 
        
        Signature ``GetDataCount()`` 
        
        :returns:  the number of data  
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNthData(self, index: int) -> NXOpen.OpenXml.DocumentData:
        """
        Gets the nth document data object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.Report.ResultXmlFileWriter` object 
        
        Signature ``GetNthData(index)`` 
        
        :param index:  the index of data 
        :type index: int 
        :returns:  the data 
        :rtype: :py:class:`NXOpen.OpenXml.DocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteNthData(self, index: int) -> None:
        """
        Removes the nth document data
        
        Signature ``DeleteNthData(index)`` 
        
        :param index:  the index of data 
        :type index: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteAllData(self) -> None:
        """
        Removes all document data
        
        Signature ``DeleteAllData()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveToFile(self, fileName: str) -> None:
        """
        Exports all document data to result XML file
        
        Signature ``SaveToFile(fileName)`` 
        
        :param fileName:  the file name to be exported 
        :type fileName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class CommandBuilderUserInputLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CommandBuilderUserInputLocation():
    """
    Represents the user input location in command. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BeforeAutomation", "The user item before automation"
       "AfterAutomation", "The user item after automation"
    """
    BeforeAutomation = 0  # CommandBuilderUserInputLocationMemberType
    AfterAutomation = 1  # CommandBuilderUserInputLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CommandBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Report.CommandBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Report.CommandManager.CreateCommandBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    class UserInputLocation():
        """
        Represents the user input location in command. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BeforeAutomation", "The user item before automation"
           "AfterAutomation", "The user item after automation"
        """
        BeforeAutomation = 0  # CommandBuilderUserInputLocationMemberType
        AfterAutomation = 1  # CommandBuilderUserInputLocationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetHint(self) -> 'list[str]':
        """
        Gets the command hint 
        
        Signature ``GetHint()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetHint(self, commandHint: 'list[str]') -> None:
        """
        Sets the command hint 
        
        Signature ``SetHint(commandHint)`` 
        
        :param commandHint: 
        :type commandHint: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNamespaces(self, pNamespaces: 'list[str]') -> None:
        """
        Sets the categories which command apply to.  
        
        Signature ``SetNamespaces(pNamespaces)`` 
        
        :param pNamespaces: 
        :type pNamespaces: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNamespaces(self) -> 'list[str]':
        """
        Gets the categories which command apply to.  
        
        Signature ``GetNamespaces()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddArgument(self, argumentType: BaseArgumentType) -> BaseArgument:
        """
        Adds an argument and adds it to the command.  
        
        Signature ``AddArgument(argumentType)`` 
        
        :param argumentType: 
        :type argumentType: :py:class:`NXOpen.Report.BaseArgumentType` 
        :returns: 
        :rtype: :py:class:`NXOpen.Report.BaseArgument` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetArguments(self) -> 'list[BaseArgument]':
        """
        Gets all arguments in the command.  
        
        Signature ``GetArguments()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Report.BaseArgument` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveArguments(self, pArguments: 'list[BaseArgument]') -> None:
        """
        Removes the arguments.  
        
        Signature ``RemoveArguments(pArguments)`` 
        
        :param pArguments: 
        :type pArguments: list of :py:class:`NXOpen.Report.BaseArgument` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddUserInput(self, userInputLocation: CommandBuilderUserInputLocation, userInputType: UserInputType) -> UserInput:
        """
        Adds an user input and adds it to command.  
        
        Signature ``AddUserInput(userInputLocation, userInputType)`` 
        
        :param userInputLocation: 
        :type userInputLocation: :py:class:`NXOpen.Report.CommandBuilderUserInputLocation` 
        :param userInputType: 
        :type userInputType: :py:class:`NXOpen.Report.UserInputType` 
        :returns: 
        :rtype: :py:class:`NXOpen.Report.UserInput` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetUserInputs(self, userInputLocation: CommandBuilderUserInputLocation) -> 'list[UserInput]':
        """
        Gets all user inputs.  
        
        Signature ``GetUserInputs(userInputLocation)`` 
        
        :param userInputLocation: 
        :type userInputLocation: :py:class:`NXOpen.Report.CommandBuilderUserInputLocation` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Report.UserInput` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveUserInputs(self, userInputLocation: CommandBuilderUserInputLocation, pUserInputs: 'list[UserInput]') -> None:
        """
        Removes the user inputs.  
        
        Signature ``RemoveUserInputs(userInputLocation, pUserInputs)`` 
        
        :param userInputLocation: 
        :type userInputLocation: :py:class:`NXOpen.Report.CommandBuilderUserInputLocation` 
        :param pUserInputs: 
        :type pUserInputs: list of :py:class:`NXOpen.Report.UserInput` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveUserInputs(self, userInputLocation: CommandBuilderUserInputLocation, pUserInputs: 'list[UserInput]', isBeforeRefUserInput: bool, pRefUserInputs: UserInput) -> None:
        """
        Moves the user inputs to the new position.  
        
        Signature ``MoveUserInputs(userInputLocation, pUserInputs, isBeforeRefUserInput, pRefUserInputs)`` 
        
        :param userInputLocation: 
        :type userInputLocation: :py:class:`NXOpen.Report.CommandBuilderUserInputLocation` 
        :param pUserInputs: 
        :type pUserInputs: list of :py:class:`NXOpen.Report.UserInput` 
        :param isBeforeRefUserInput: 
        :type isBeforeRefUserInput: bool 
        :param pRefUserInputs:  the target reference user input  
        :type pRefUserInputs: :py:class:`NXOpen.Report.UserInput` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Active: bool = ...
    """
    Returns or sets  a value that indicates whether the command is active or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``Active`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Active`` 
    
    :param isActive: 
    :type isActive: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DisplayName: str = ...
    """
    Returns or sets  the command display name 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayName`` 
    
    :param displayName: 
    :type displayName: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Name: str = ...
    """
    Returns or sets  the command name 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param commandName: 
    :type commandName: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ProgramInformation: ProgramInformation = ...
    """
    Returns  the automation program information object.  
    
    <hr>
    
    Getter Method
    
    Signature ``ProgramInformation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Report.ProgramInformation` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: CommandBuilder = ...  # unknown typename


class BaseArgumentTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BaseArgumentType():
    """
    Represents the argument type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Integer", "Argument for integer data"
       "Double", "Argument for double data"
       "String", "Argument for string data"
       "Enumeration", "Argument for enumeration data"
    """
    Integer = 0  # BaseArgumentTypeMemberType
    Double = 1  # BaseArgumentTypeMemberType
    String = 2  # BaseArgumentTypeMemberType
    Enumeration = 3  # BaseArgumentTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BaseArgument(NXOpen.TaggedObject, NXOpen.INXObject):
    """
    Represents an abstract command argument.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    class Type():
        """
        Represents the argument type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Integer", "Argument for integer data"
           "Double", "Argument for double data"
           "String", "Argument for string data"
           "Enumeration", "Argument for enumeration data"
        """
        Integer = 0  # BaseArgumentTypeMemberType
        Double = 1  # BaseArgumentTypeMemberType
        String = 2  # BaseArgumentTypeMemberType
        Enumeration = 3  # BaseArgumentTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def FindObject(self, journalIdentifier: str) -> NXOpen.INXObject:
        """
        Finds the :py:class:`NXOpen.NXObject` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier of the object  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.INXObject` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Print(self) -> None:
        """
        Prints a representation of this object to the system log file.  
        
        Signature ``Print()`` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetName(self, name: str) -> None:
        """
        Sets the custom name of the object.  
        
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetName(name)`` 
        
        :param name: 
        :type name: str 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    DisplayName: str = ...
    """
    Returns or sets  the argument display name 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayName`` 
    
    :param displayName: 
    :type displayName: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Hint: str = ...
    """
    Returns or sets  the argument hint.  
    
    <hr>
    
    Getter Method
    
    Signature ``Hint`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Hint`` 
    
    :param argumentHint: 
    :type argumentHint: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Optional: bool = ...
    """
    Returns or sets  a value that indicates whether this argument is optional or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``Optional`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Optional`` 
    
    :param isOptional: 
    :type isOptional: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    JournalIdentifier: str = ...
    """
    Returns  the identifier that would be recorded in a journal for this object.  
    
    This may not be the same across different releases of the software. 
    
    <hr>
    
    Getter Method
    
    Signature ``JournalIdentifier`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    IsOccurrence: bool = ...
    """
    Returns  whether this object is an occurrence or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsOccurrence`` 
    
    :returns:  This object is an occurrence  
    :rtype: bool 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Prototype: NXOpen.INXObject = ...
    """
    Returns  the prototype of this object if it is an occurrence.  
    
    <hr>
    
    Getter Method
    
    Signature ``Prototype`` 
    
    :returns:  The prototype of this object or null if this object is not an occurrence  
    :rtype: :py:class:`NXOpen.INXObject` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    OwningComponent: NXOpen.Assemblies.Component = ...
    """
    Returns  the owning component, if this object is an occurrence.  
    
    <hr>
    
    Getter Method
    
    Signature ``OwningComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    OwningPart: NXOpen.BasePart = ...
    """
    Returns  the owning part of this object 
    
    <hr>
    
    Getter Method
    
    Signature ``OwningPart`` 
    
    :returns:  The owning part of this object or null if it does not have an owner  
    :rtype: :py:class:`NXOpen.BasePart` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Name: str = ...
    """
    Returns  the custom name of the object.  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Null: BaseArgument = ...  # unknown typename


class StringArgument(BaseArgument):
    """
    Represents an argument for string type data.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    DefaultValue: str = ...
    """
    Returns or sets  the argument default value.  
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultValue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultValue`` 
    
    :param defaultValue: 
    :type defaultValue: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: StringArgument = ...  # unknown typename


class BaseItem(NXOpen.NXObject):
    """
    Represents an abstract report item.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def Clear(self) -> None:
        """
        Clears the content in this class.  
        
        Signature ``Clear()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    DisplayName: str = ...
    """
    Returns  the item display name.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Hint: str = ...
    """
    Returns  the item hint.  
    
    <hr>
    
    Getter Method
    
    Signature ``Hint`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: BaseItem = ...  # unknown typename


class CommandManager():
    """
    Represents the command manager.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def ExportCommandsToLibraryFile(self, pCommands: 'list[Command]', libraryFile: str) -> None:
        """
        Export selected commands to a library folder zip file.  
        
        Signature ``ExportCommandsToLibraryFile(pCommands, libraryFile)`` 
        
        :param pCommands: 
        :type pCommands: list of :py:class:`NXOpen.Report.Command` 
        :param libraryFile:  Library folder zip file name with full path  
        :type libraryFile: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCommandLibraries(self) -> 'list[CommandLibrary]':
        """
        Gets all command libraries.  
        
        Signature ``GetCommandLibraries()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Report.CommandLibrary` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateCommandBuilder(self, commandLibrary: CommandLibrary, command: Command) -> CommandBuilder:
        """
        Creates the command builder.  
        
        Signature ``CreateCommandBuilder(commandLibrary, command)`` 
        
        :param commandLibrary: 
        :type commandLibrary: :py:class:`NXOpen.Report.CommandLibrary` 
        :param command: 
        :type command: :py:class:`NXOpen.Report.Command` 
        :returns: 
        :rtype: :py:class:`NXOpen.Report.CommandBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewCommandImporter(self, pCommandLibrary: CommandLibrary, libraryFile: str) -> CommandImporter:
        """
        Creates a transient object :py:class:`NXOpen.Report.CommandImporter` to import
        the selected commands of a command library file to a command library.  
        
        The object
        should be destroyed after finishing import.  
        
        Signature ``NewCommandImporter(pCommandLibrary, libraryFile)`` 
        
        :param pCommandLibrary: 
        :type pCommandLibrary: :py:class:`NXOpen.Report.CommandLibrary` 
        :param libraryFile:   Library folder zip file name with full path  
        :type libraryFile: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Report.CommandImporter` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Find(self, journalIdentifier: str) -> NXOpen.TaggedObject:
        """
        Finds the :py:class:`TaggedObject` with the given identifier as recorded in a journal.  
        
        Signature ``Find(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier of the :py:class:`TaggedObject` to be found  
        :type journalIdentifier: str 
        :returns:  Object found, or null if no such object exists  
        :rtype: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class TextItem(BaseItem):
    """
    Represents a text item.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def GetText(self) -> 'list[str]':
        """
        Get the text content.  
        
        Signature ``GetText()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetText(self, lineTexts: 'list[str]') -> None:
        """
        Set the text content.  
        
        Signature ``SetText(lineTexts)`` 
        
        :param lineTexts: 
        :type lineTexts: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: TextItem = ...  # unknown typename


class IUserItem(NXOpen.INXObject):
    """
    Represents an user defined report item.  
    
    .. versionadded:: NX11.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class UserTextItem(TextItem, IUserItem):
    """
    Represents a user text item.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def SetDisplayName(self, displayName: str) -> None:
        """
        Sets the display name.  
        
        Signature ``SetDisplayName(displayName)`` 
        
        :param displayName: 
        :type displayName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: UserTextItem = ...  # unknown typename


class Command(NXOpen.NXObject):
    """
    Represents a command in command library.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Report.CommandBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def Delete(self) -> None:
        """
        Deletes the command.  
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Command = ...  # unknown typename


class ReportMoveItemLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReportMoveItemLocation():
    """
    Represents the moving item location. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Before", "Move item to the location before reference item"
       "After", "Move item to the location after reference item"
    """
    Before = 0  # ReportMoveItemLocationMemberType
    After = 1  # ReportMoveItemLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Report(NXOpen.NXObject):
    """
    Represents a report.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    class MoveItemLocation():
        """
        Represents the moving item location. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Before", "Move item to the location before reference item"
           "After", "Move item to the location after reference item"
        """
        Before = 0  # ReportMoveItemLocationMemberType
        After = 1  # ReportMoveItemLocationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetTemplateItems(self) -> 'list[TemplateItem]':
        """
        Gets all template items.  
        
        Signature ``GetTemplateItems()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Report.TemplateItem` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateUserItem(self, inputType: UserInputType) -> IUserItem:
        """
        Creates a user item and adds it to the report.  
        
        Signature ``CreateUserItem(inputType)`` 
        
        :param inputType: 
        :type inputType: :py:class:`NXOpen.Report.UserInputType` 
        :returns: 
        :rtype: :py:class:`NXOpen.Report.IUserItem` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CopyUserItem(self, userItem: IUserItem) -> IUserItem:
        """
        Copy an user item to the :py:class:`Report.Report`.  
        
        Signature ``CopyUserItem(userItem)`` 
        
        :param userItem:  input user item  
        :type userItem: :py:class:`NXOpen.Report.IUserItem` 
        :returns:  the copy of the input user item  
        :rtype: :py:class:`NXOpen.Report.IUserItem` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetUserItems(self) -> 'list[IUserItem]':
        """
        Gets all user items in the report.  
        
        Signature ``GetUserItems()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Report.IUserItem` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveUserItems(self, userItems: 'list[IUserItem]', newLocation: ReportMoveItemLocation, referencedItem: IUserItem) -> None:
        """
        Moves the user items to the new position.  
        
        Signature ``MoveUserItems(userItems, newLocation, referencedItem)`` 
        
        :param userItems: 
        :type userItems: list of :py:class:`NXOpen.Report.IUserItem` 
        :param newLocation: 
        :type newLocation: :py:class:`NXOpen.Report.ReportMoveItemLocation` 
        :param referencedItem:  the target reference user item  
        :type referencedItem: :py:class:`NXOpen.Report.IUserItem` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Export(self, reportDocument: str, listError: bool) -> None:
        """
        Exports the report contents to a document.  
        
        Signature ``Export(reportDocument, listError)`` 
        
        :param reportDocument: 
        :type reportDocument: str 
        :param listError:  list error information in listing window  
        :type listError: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearTemplateItems(self) -> None:
        """
        Clears all template items in :py:class:`Report.Report`.  
        
        Signature ``ClearTemplateItems()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteUserItems(self) -> None:
        """
        Deletes all user items in :py:class:`Report.Report`.  
        
        Signature ``DeleteUserItems()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def HideTempalteItemsWithoutInput(self, hideTemplateItemsWithoutInput: bool) -> None:
        """
        Hide template items without user input in :py:class:`Report.Report`.  
        
        Signature ``HideTempalteItemsWithoutInput(hideTemplateItemsWithoutInput)`` 
        
        :param hideTemplateItemsWithoutInput: 
        :type hideTemplateItemsWithoutInput: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SynchronizeWithCommands(self) -> None:
        """
        Synchronize the :py:class:`Report.Report` with commands.  
        
        Signature ``SynchronizeWithCommands()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    ReportCollection: IReportCollection = ...
    """
    Returns  the report collection object.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReportCollection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Report.IReportCollection` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    TemplateFile: str = ...
    """
    Returns or sets  the template document file.  
    
    <hr>
    
    Getter Method
    
    Signature ``TemplateFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TemplateFile`` 
    
    :param templateFile:   Template file name with full path  
    :type templateFile: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: Report = ...  # unknown typename


class ProgramInformationLanguageTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ProgramInformationLanguageType():
    """
    Represents the automation program. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None language"
       "CPlusplus", "C plus plus language"
       "CSharp", "C sharp language"
       "Vb", "Visual basic language"
       "Java", "Java language"
       "Python", "Python language"
    """
    NotSet = 0  # ProgramInformationLanguageTypeMemberType
    CPlusplus = 1  # ProgramInformationLanguageTypeMemberType
    CSharp = 2  # ProgramInformationLanguageTypeMemberType
    Vb = 3  # ProgramInformationLanguageTypeMemberType
    Java = 4  # ProgramInformationLanguageTypeMemberType
    Python = 5  # ProgramInformationLanguageTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ProgramInformation(NXOpen.TaggedObject, NXOpen.INXObject):
    """
    Represents the program information for command automation.  
    
    .. versionadded:: NX11.0.0
    """
    
    class LanguageType():
        """
        Represents the automation program. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None language"
           "CPlusplus", "C plus plus language"
           "CSharp", "C sharp language"
           "Vb", "Visual basic language"
           "Java", "Java language"
           "Python", "Python language"
        """
        NotSet = 0  # ProgramInformationLanguageTypeMemberType
        CPlusplus = 1  # ProgramInformationLanguageTypeMemberType
        CSharp = 2  # ProgramInformationLanguageTypeMemberType
        Vb = 3  # ProgramInformationLanguageTypeMemberType
        Java = 4  # ProgramInformationLanguageTypeMemberType
        Python = 5  # ProgramInformationLanguageTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def FindObject(self, journalIdentifier: str) -> NXOpen.INXObject:
        """
        Finds the :py:class:`NXOpen.NXObject` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier of the object  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.INXObject` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Print(self) -> None:
        """
        Prints a representation of this object to the system log file.  
        
        Signature ``Print()`` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetName(self, name: str) -> None:
        """
        Sets the custom name of the object.  
        
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetName(name)`` 
        
        :param name: 
        :type name: str 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    FunctionName: str = ...
    """
    Returns or sets  the program entry function name.  
    
    CPlusplus language: the function name is the exported function following required interface,
    Java language: the function name is the exported java class name,
    CSharp, Vb and Python language: the function name is "Main". 
    
    <hr>
    
    Getter Method
    
    Signature ``FunctionName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FunctionName`` 
    
    :param functionName: 
    :type functionName: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Language: ProgramInformationLanguageType = ...
    """
    Returns or sets  the automation program language.  
    
    <hr>
    
    Getter Method
    
    Signature ``Language`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Report.ProgramInformationLanguageType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Language`` 
    
    :param languageType: 
    :type languageType: :py:class:`NXOpen.Report.ProgramInformationLanguageType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ProgramFile: str = ...
    """
    Returns or sets  the automation program executer file.  
    
    CPlusplus language: the dll file,
    CSharp language: the CS file or CS dll file,
    Vb language: the VB file or VB dll file,
    Java language: the Jar file,
    Python language: the Py file. 
    
    <hr>
    
    Getter Method
    
    Signature ``ProgramFile`` 
    
    :returns:  the program file with full path   
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProgramFile`` 
    
    :param programFile:  the program file with full path  
    :type programFile: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    JournalIdentifier: str = ...
    """
    Returns  the identifier that would be recorded in a journal for this object.  
    
    This may not be the same across different releases of the software. 
    
    <hr>
    
    Getter Method
    
    Signature ``JournalIdentifier`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    IsOccurrence: bool = ...
    """
    Returns  whether this object is an occurrence or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsOccurrence`` 
    
    :returns:  This object is an occurrence  
    :rtype: bool 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Prototype: NXOpen.INXObject = ...
    """
    Returns  the prototype of this object if it is an occurrence.  
    
    <hr>
    
    Getter Method
    
    Signature ``Prototype`` 
    
    :returns:  The prototype of this object or null if this object is not an occurrence  
    :rtype: :py:class:`NXOpen.INXObject` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    OwningComponent: NXOpen.Assemblies.Component = ...
    """
    Returns  the owning component, if this object is an occurrence.  
    
    <hr>
    
    Getter Method
    
    Signature ``OwningComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    OwningPart: NXOpen.BasePart = ...
    """
    Returns  the owning part of this object 
    
    <hr>
    
    Getter Method
    
    Signature ``OwningPart`` 
    
    :returns:  The owning part of this object or null if it does not have an owner  
    :rtype: :py:class:`NXOpen.BasePart` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Name: str = ...
    """
    Returns  the custom name of the object.  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Null: ProgramInformation = ...  # unknown typename


class DoubleArgument(BaseArgument):
    """
    Represents an argument for double type data.  
    
    This class
    does not include upper bound and lower bound in default. 
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    DefaultValue: float = ...
    """
    Returns or sets  the arguement dafault value.  
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultValue`` 
    
    :param argumentValue: 
    :type argumentValue: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    IncludeLowerBound: bool = ...
    """
    Returns or sets  a value that indicates whether includes the lower bound.  
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeLowerBound`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeLowerBound`` 
    
    :param includeLowerBound: 
    :type includeLowerBound: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    IncludeUpperBound: bool = ...
    """
    Returns or sets  a value that indicates whether includes the upper bound.  
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeUpperBound`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeUpperBound`` 
    
    :param includeUpperBound: 
    :type includeUpperBound: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MaximumValue: float = ...
    """
    Returns or sets  the maximum value.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumValue`` 
    
    :param maximumValue: 
    :type maximumValue: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MimimumValue: float = ...
    """
    Returns or sets  the minimum value.  
    
    <hr>
    
    Getter Method
    
    Signature ``MimimumValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MimimumValue`` 
    
    :param minimumValue: 
    :type minimumValue: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: DoubleArgument = ...  # unknown typename


class ReportPreference(NXOpen.TaggedObject):
    """
    Manages the preference data.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def SaveMemoryFile(self) -> None:
        """
        Saves preference settings to memory file 
        
        Signature ``SaveMemoryFile()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    MaximumRecentReportDocumentCount: int = ...
    """
    Returns or sets  the maximum count of the recent report documents which could be viewed 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumRecentReportDocumentCount`` 
    
    :returns:  Maximum recent report document  
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumRecentReportDocumentCount`` 
    
    :param maxRecentReportDoc:  Maximum recent report document  
    :type maxRecentReportDoc: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    OpenReportDocumentAfterExport: bool = ...
    """
    Returns or sets  the option indicates whether to open report document after exporting report 
    
    <hr>
    
    Getter Method
    
    Signature ``OpenReportDocumentAfterExport`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OpenReportDocumentAfterExport`` 
    
    :param openReportAfterExportSetting: 
    :type openReportAfterExportSetting: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    SearchTemplateFromSiteDirectory: bool = ...
    """
    Returns or sets  the option indicates whether to use site template directory as start to choose a report template file  
    
    <hr>
    
    Getter Method
    
    Signature ``SearchTemplateFromSiteDirectory`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchTemplateFromSiteDirectory`` 
    
    :param searchTemplateFromSiteDirectorySetting: 
    :type searchTemplateFromSiteDirectorySetting: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    UsePartDirectoryAsDefaultExportLocation: bool = ...
    """
    Returns or sets  the option indicates whehter to use part direcotry as default report document location  
    
    <hr>
    
    Getter Method
    
    Signature ``UsePartDirectoryAsDefaultExportLocation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UsePartDirectoryAsDefaultExportLocation`` 
    
    :param usePartDirAsDefaultExportLocationSetting: 
    :type usePartDirAsDefaultExportLocationSetting: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ViewImageAfterSnapshotting: bool = ...
    """
    Returns or sets  the option indicates whether to view image after snopshotting  
    
    <hr>
    
    Getter Method
    
    Signature ``ViewImageAfterSnapshotting`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ViewImageAfterSnapshotting`` 
    
    :param viewImageAfterSnapshotSetting: 
    :type viewImageAfterSnapshotSetting: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: ReportPreference = ...  # unknown typename


class IReportCollection(NXOpen.INXObject):
    """
    This interface is used to manage associated reports :py:class:`Report.Report`   
    
    .. versionadded:: NX11.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class CommandLibraryMoveCommandLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CommandLibraryMoveCommandLocation():
    """
    Represents the moving command location. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Before", "Move commands ahead of a referenced command"
       "After", "Move commands behind a referenced command"
    """
    Before = 0  # CommandLibraryMoveCommandLocationMemberType
    After = 1  # CommandLibraryMoveCommandLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CommandLibrary(NXOpen.TaggedObject, NXOpen.INXObject):
    """
    Represents a command library in the command manager.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    class MoveCommandLocation():
        """
        Represents the moving command location. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Before", "Move commands ahead of a referenced command"
           "After", "Move commands behind a referenced command"
        """
        Before = 0  # CommandLibraryMoveCommandLocationMemberType
        After = 1  # CommandLibraryMoveCommandLocationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetCommands(self) -> 'list[Command]':
        """
        Gets all commands in command library.  
        
        Signature ``GetCommands()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Report.Command` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Save(self) -> None:
        """
        Saves all commands to their binding xml file.  
        
        Signature ``Save()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveCommands(self, pCommand: 'list[Command]', newLocation: CommandLibraryMoveCommandLocation, pReferenceCommand: Command) -> None:
        """
        Moves the commands to the new position.  
        
        Signature ``MoveCommands(pCommand, newLocation, pReferenceCommand)`` 
        
        :param pCommand: 
        :type pCommand: list of :py:class:`NXOpen.Report.Command` 
        :param newLocation: 
        :type newLocation: :py:class:`NXOpen.Report.CommandLibraryMoveCommandLocation` 
        :param pReferenceCommand: 
        :type pReferenceCommand: :py:class:`NXOpen.Report.Command` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> NXOpen.INXObject:
        """
        Finds the :py:class:`NXOpen.NXObject` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier of the object  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.INXObject` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Print(self) -> None:
        """
        Prints a representation of this object to the system log file.  
        
        Signature ``Print()`` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetName(self, name: str) -> None:
        """
        Sets the custom name of the object.  
        
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetName(name)`` 
        
        :param name: 
        :type name: str 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    JournalIdentifier: str = ...
    """
    Returns  the identifier that would be recorded in a journal for this object.  
    
    This may not be the same across different releases of the software. 
    
    <hr>
    
    Getter Method
    
    Signature ``JournalIdentifier`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    IsOccurrence: bool = ...
    """
    Returns  whether this object is an occurrence or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsOccurrence`` 
    
    :returns:  This object is an occurrence  
    :rtype: bool 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Prototype: NXOpen.INXObject = ...
    """
    Returns  the prototype of this object if it is an occurrence.  
    
    <hr>
    
    Getter Method
    
    Signature ``Prototype`` 
    
    :returns:  The prototype of this object or null if this object is not an occurrence  
    :rtype: :py:class:`NXOpen.INXObject` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    OwningComponent: NXOpen.Assemblies.Component = ...
    """
    Returns  the owning component, if this object is an occurrence.  
    
    <hr>
    
    Getter Method
    
    Signature ``OwningComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    OwningPart: NXOpen.BasePart = ...
    """
    Returns  the owning part of this object 
    
    <hr>
    
    Getter Method
    
    Signature ``OwningPart`` 
    
    :returns:  The owning part of this object or null if it does not have an owner  
    :rtype: :py:class:`NXOpen.BasePart` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Name: str = ...
    """
    Returns  the custom name of the object.  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Null: CommandLibrary = ...  # unknown typename


class EnumerationArgument(BaseArgument):
    """
    Represents an argument for enumeration type data.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def GetEnumerationOptions(self) -> 'list[str]':
        """
        Gets the enumeration options.  
        
        Signature ``GetEnumerationOptions()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEnumerationOptions(self, enumerationOptions: 'list[str]') -> None:
        """
        Sets the enumeration options.  
        
        Signature ``SetEnumerationOptions(enumerationOptions)`` 
        
        :param enumerationOptions: 
        :type enumerationOptions: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    DefaultValue: int = ...
    """
    Returns or sets  the argument default value.  
    
    The default value index is between 0 and options count queried
    by :py:meth:`NXOpen.Report.EnumerationArgument.GetEnumerationOptions`, 0 is inclusive. 
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultValue`` 
    
    :param defaultValueIndex: 
    :type defaultValueIndex: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: EnumerationArgument = ...  # unknown typename


class ImagesGroupItem(NXOpen.NXObject):
    """
    Represents a images group item.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def CreateImage(self, imageFile: str, displayName: str) -> ReportImage:
        """
        Creates an image in images group.  
        
        Signature ``CreateImage(imageFile, displayName)`` 
        
        :param imageFile: 
        :type imageFile: str 
        :param displayName: 
        :type displayName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Report.ReportImage` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CopyImage(self, pReportImage: ReportImage) -> ReportImage:
        """
        Copy a :py:class:`NXOpen.Report.ReportImage` to the this class.  
        
        Signature ``CopyImage(pReportImage)`` 
        
        :param pReportImage:  input image  
        :type pReportImage: :py:class:`NXOpen.Report.ReportImage` 
        :returns:  copy of the input image  
        :rtype: :py:class:`NXOpen.Report.ReportImage` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetImages(self) -> 'list[ReportImage]':
        """
        Gets all images in images group.  
        
        Signature ``GetImages()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Report.ReportImage` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveImages(self, pReportImages: 'list[ReportImage]', newLocation: ReportMoveItemLocation, pReferencedImage: ReportImage) -> None:
        """
        Moves the images to the new position.  
        
        Signature ``MoveImages(pReportImages, newLocation, pReferencedImage)`` 
        
        :param pReportImages: 
        :type pReportImages: list of :py:class:`NXOpen.Report.ReportImage` 
        :param newLocation: 
        :type newLocation: :py:class:`NXOpen.Report.ReportMoveItemLocation` 
        :param pReferencedImage: 
        :type pReferencedImage: :py:class:`NXOpen.Report.ReportImage` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteImages(self) -> None:
        """
        Deletes all images in class.  
        
        Signature ``DeleteImages()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ImagesGroupItem = ...  # unknown typename


class ImageOption(NXOpen.TaggedObject):
    """
    Represents an image option object.  
    
    .. versionadded:: NX11.0.0
    """
    ImageHeight: float = ...
    """
    Returns or sets  the image height .  
    
    <hr>
    
    Getter Method
    
    Signature ``ImageHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageHeight`` 
    
    :param imageHeight: 
    :type imageHeight: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ImageRotation: float = ...
    """
    Returns or sets  the image rotation angle in degree.  
    
    <hr>
    
    Getter Method
    
    Signature ``ImageRotation`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageRotation`` 
    
    :param imageRotation: 
    :type imageRotation: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ImageWidth: float = ...
    """
    Returns or sets  the image width .  
    
    <hr>
    
    Getter Method
    
    Signature ``ImageWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageWidth`` 
    
    :param imageWidth: 
    :type imageWidth: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LockOriginalAspectRatio: bool = ...
    """
    Returns or sets  a value that indicates whether locks original image aspect ratio. If locks ratio, the image
    width will be updated according to the ratio when image height changes , and vice versa. 
    
    <hr>
    
    Getter Method
    
    Signature ``LockOriginalAspectRatio`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LockOriginalAspectRatio`` 
    
    :param lockOriginalRatio: 
    :type lockOriginalRatio: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: ImageOption = ...  # unknown typename


class TemplateItem(BaseItem):
    """
    Represents a template item object.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def GetChildItems(self, itemsLocation: CommandBuilderUserInputLocation) -> 'list[BaseItem]':
        """
        Gets child items in template item.  
        
        Signature ``GetChildItems(itemsLocation)`` 
        
        :param itemsLocation: 
        :type itemsLocation: :py:class:`NXOpen.Report.CommandBuilderUserInputLocation` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Report.BaseItem` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: TemplateItem = ...  # unknown typename


class UserImagesGroupItem(ImagesGroupItem, IUserItem):
    """
    Represents a user images group item.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def SetDisplayName(self, displayName: str) -> None:
        """
        Sets the display name.  
        
        Signature ``SetDisplayName(displayName)`` 
        
        :param displayName: 
        :type displayName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: UserImagesGroupItem = ...  # unknown typename


class AutomationLoggerMessageTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AutomationLoggerMessageType():
    """
    Represents the automation logger message type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Empty", "None"
       "Information", "Information message"
       "Debug", "Debug message"
       "Exception", "Exception message"
    """
    Empty = 0  # AutomationLoggerMessageTypeMemberType
    Information = 1  # AutomationLoggerMessageTypeMemberType
    Debug = 2  # AutomationLoggerMessageTypeMemberType
    Exception = 3  # AutomationLoggerMessageTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AutomationLogger():
    """
    Represents the automation logger to log information for report automation program.  
    
    No support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    class MessageType():
        """
        Represents the automation logger message type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Empty", "None"
           "Information", "Information message"
           "Debug", "Debug message"
           "Exception", "Exception message"
        """
        Empty = 0  # AutomationLoggerMessageTypeMemberType
        Information = 1  # AutomationLoggerMessageTypeMemberType
        Debug = 2  # AutomationLoggerMessageTypeMemberType
        Exception = 3  # AutomationLoggerMessageTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    @typing.overload
    def LogMessage(self, message: str) -> None:
        """
        Adds debug message to the logger.
        
        Signature ``LogMessage(message)`` 
        
        :param message: 
        :type message: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def LogMessage(self, message: str, messageType: AutomationLoggerMessageType) -> None:
        """
        Adds required type of message to the logger.
        
        Signature ``LogMessage(message, messageType)`` 
        
        :param message: 
        :type message: str 
        :param messageType: 
        :type messageType: :py:class:`NXOpen.Report.AutomationLoggerMessageType` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Clear(self) -> None:
        """
        Clears the messages in the logger.  
        
        Signature ``Clear()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveLog(self, logFileName: str) -> None:
        """
        Saves the messages in the logger to a file.  
        
        Signature ``SaveLog(logFileName)`` 
        
        :param logFileName: 
        :type logFileName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsEmpty(self) -> bool:
        """
        Has messages in the logger.  
        
        Signature ``IsEmpty()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class ReportManager():
    """
    Represents the report manager.  
    
    To obtain an instance of this class use :py:meth:`NXOpen.Session.ReportManager`.
    
    .. versionadded:: NX11.0.0
    """
    
    def CreateResultXmlFileWriter(self) -> ResultXmlFileWriter:
        """
        Creates a new :py:class:`NXOpen.Report.ResultXmlFileWriter` object.  
        
        Signature ``CreateResultXmlFileWriter()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Report.ResultXmlFileWriter` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOriginalImageDimension(self, imageFullFileName: str) -> tuple:
        """
        Gets the original dimension of a given image file.  
        
        Signature ``GetOriginalImageDimension(imageFullFileName)`` 
        
        :param imageFullFileName:  the full image file name  
        :type imageFullFileName: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (width, height). width is a float. height is a float. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Preference: ReportPreference = ...
    """
    Returns  the report preference.  
    
    <hr>
    
    Getter Method
    
    Signature ``Preference`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Report.ReportPreference` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    AutomationLogger: AutomationLogger = ...
    """
    Returns the :py:class:`NXOpen.Report.AutomationLogger` belonging to the report manager 
    
    Signature ``AutomationLogger`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Report.AutomationLogger`
    """
    CommandManager: CommandManager = ...
    """
    Returns the :py:class:`NXOpen.Report.CommandManager` belonging to the report manager 
    
    Signature ``CommandManager`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Report.CommandManager`
    """


class CommandImporterOverrideOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CommandImporterOverrideOption():
    """
    Represents the override option when there is already a command existing. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Ignore", "No action, do not import to library"
       "Replace", "Import to replace the existing one"
       "Copy", "Import and append a new one"
    """
    Ignore = 0  # CommandImporterOverrideOptionMemberType
    Replace = 1  # CommandImporterOverrideOptionMemberType
    Copy = 2  # CommandImporterOverrideOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CommandImporter(NXOpen.TransientObject):
    """
    Represents a command importer to import the commands into command libary.  
    
    .. versionadded:: NX11.0.0
    """
    
    class OverrideOption():
        """
        Represents the override option when there is already a command existing. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Ignore", "No action, do not import to library"
           "Replace", "Import to replace the existing one"
           "Copy", "Import and append a new one"
        """
        Ignore = 0  # CommandImporterOverrideOptionMemberType
        Replace = 1  # CommandImporterOverrideOptionMemberType
        Copy = 2  # CommandImporterOverrideOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetImportCandidates(self) -> 'list[Command]':
        """
        Gets all candidate commands in library file.  
        
        Signature ``GetImportCandidates()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Report.Command` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ImportCommands(self, pCommandIndexes: 'list[int]') -> None:
        """
        Imports the selected commands into command library.  
        
        Signature ``ImportCommands(pCommandIndexes)`` 
        
        :param pCommandIndexes: 
        :type pCommandIndexes: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Destroys the object 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    ImportOption: CommandImporterOverrideOption = ...
    """
    Returns or sets  the command override option.  
    
    <hr>
    
    Getter Method
    
    Signature ``ImportOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Report.CommandImporterOverrideOption` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImportOption`` 
    
    :param importOption: 
    :type importOption: :py:class:`NXOpen.Report.CommandImporterOverrideOption` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """


class UserInputTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserInputType():
    """
    Represents the user input type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Text", "User input for text data"
       "Images", "User input for images data"
    """
    Text = 0  # UserInputTypeMemberType
    Images = 1  # UserInputTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserInput(NXOpen.TaggedObject, NXOpen.INXObject):
    """
    Represents a user input in command.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    class Type():
        """
        Represents the user input type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Text", "User input for text data"
           "Images", "User input for images data"
        """
        Text = 0  # UserInputTypeMemberType
        Images = 1  # UserInputTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetHint(self) -> 'list[str]':
        """
        Gets the user input hint.  
        
        Signature ``GetHint()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetHint(self, inputHint: 'list[str]') -> None:
        """
        Sets the user input hint.  
        
        Signature ``SetHint(inputHint)`` 
        
        :param inputHint: 
        :type inputHint: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> NXOpen.INXObject:
        """
        Finds the :py:class:`NXOpen.NXObject` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier of the object  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.INXObject` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Print(self) -> None:
        """
        Prints a representation of this object to the system log file.  
        
        Signature ``Print()`` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetName(self, name: str) -> None:
        """
        Sets the custom name of the object.  
        
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetName(name)`` 
        
        :param name: 
        :type name: str 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    InputType: UserInputType = ...
    """
    Returns or sets  the user input type.  
    
    <hr>
    
    Getter Method
    
    Signature ``InputType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Report.UserInputType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputType`` 
    
    :param inputType: 
    :type inputType: :py:class:`NXOpen.Report.UserInputType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    JournalIdentifier: str = ...
    """
    Returns  the identifier that would be recorded in a journal for this object.  
    
    This may not be the same across different releases of the software. 
    
    <hr>
    
    Getter Method
    
    Signature ``JournalIdentifier`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    IsOccurrence: bool = ...
    """
    Returns  whether this object is an occurrence or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsOccurrence`` 
    
    :returns:  This object is an occurrence  
    :rtype: bool 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Prototype: NXOpen.INXObject = ...
    """
    Returns  the prototype of this object if it is an occurrence.  
    
    <hr>
    
    Getter Method
    
    Signature ``Prototype`` 
    
    :returns:  The prototype of this object or null if this object is not an occurrence  
    :rtype: :py:class:`NXOpen.INXObject` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    OwningComponent: NXOpen.Assemblies.Component = ...
    """
    Returns  the owning component, if this object is an occurrence.  
    
    <hr>
    
    Getter Method
    
    Signature ``OwningComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    OwningPart: NXOpen.BasePart = ...
    """
    Returns  the owning part of this object 
    
    <hr>
    
    Getter Method
    
    Signature ``OwningPart`` 
    
    :returns:  The owning part of this object or null if it does not have an owner  
    :rtype: :py:class:`NXOpen.BasePart` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Name: str = ...
    """
    Returns  the custom name of the object.  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Null: UserInput = ...  # unknown typename


class ReportImage(NXOpen.NXObject):
    """
    Represents a report image.  
    
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    
    def SetImage(self, imageFile: str) -> None:
        """
        Replaces the old image file with a new image file.  
        
        Signature ``SetImage(imageFile)`` 
        
        :param imageFile: 
        :type imageFile: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Caption: str = ...
    """
    Returns or sets  the image caption text.  
    
    <hr>
    
    Getter Method
    
    Signature ``Caption`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Caption`` 
    
    :param captionText: 
    :type captionText: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ImageOption: ImageOption = ...
    """
    Returns  the image option.  
    
    <hr>
    
    Getter Method
    
    Signature ``ImageOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Report.ImageOption` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: ReportImage = ...  # unknown typename


class IntegerArgument(BaseArgument):
    """
    Represents an argument for integer type data.  
    
    This class
    does not include upper bound and lower bound in default. 
    Not support KF.
    
    .. versionadded:: NX11.0.0
    """
    DefaultValue: int = ...
    """
    Returns or sets  the argument default value.  
    
    <hr>
    
    Getter Method
    
    Signature ``DefaultValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefaultValue`` 
    
    :param defaultValue: 
    :type defaultValue: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    IncludeLowerBound: bool = ...
    """
    Returns or sets  a value that indicates whether includes the lower bound.  
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeLowerBound`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeLowerBound`` 
    
    :param includeLowerBound: 
    :type includeLowerBound: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    IncludeUpperBound: bool = ...
    """
    Returns or sets  a value that indicates whether includes the upper bound.  
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeUpperBound`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeUpperBound`` 
    
    :param includeUpperBound: 
    :type includeUpperBound: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MaximumValue: int = ...
    """
    Returns or sets  the maximum value.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumValue`` 
    
    :param maximumValue: 
    :type maximumValue: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MinimumValue: int = ...
    """
    Returns or sets  the minimum value.  
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumValue`` 
    
    :param minimumValue: 
    :type minimumValue: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: IntegerArgument = ...  # unknown typename


