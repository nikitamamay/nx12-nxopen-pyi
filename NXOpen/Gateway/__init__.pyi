# module 'NXOpen.Gateway'
#
# Automatically generated 2025-06-09T14:38:46.696429
#
"""Default documentation for NXOpen.Gateway."""

import typing

import NXOpen
import NXOpen.PDM



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class PasteBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Gateway.PasteBuilder`
    
    To create a new instance of this class, use :py:meth:`NXOpen.ClipboardOperationsManager.CreatePasteBuilder`
    
    .. versionadded:: NX7.5.0
    """
    Null: PasteBuilder = ...  # unknown typename


class ImageCaptureManager():
    """
    the ImageCaptureManager class  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX7.5.0
    """
    
    def CreateImageCaptureBuilder(self) -> ImageCaptureBuilder:
        """
        Creates a :py:class:`NXOpen.Gateway.ImageCaptureBuilder`  
        
        Signature ``CreateImageCaptureBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Gateway.ImageCaptureBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    


class BookmarkFile():
    """
    Represents operations which can be done on bookmark files.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX10.0.0
    """
    
    def SaveWithDescription(self, pathName: str, bookmarkOption: NXOpen.BasePartBookmarkOption, description: str) -> None:
        """
        Creates a bookmark file including a description.  
        
        See :py:class:`NXOpen.BasePartBookmarkOption` for an explanation of the options
        which are not supported in batch mode.  Also in batch mode, the description is not
        written to the bookmark file. 
        
        Signature ``SaveWithDescription(pathName, bookmarkOption, description)`` 
        
        :param pathName:  Full path name of bookmark file.  
        :type pathName: str 
        :param bookmarkOption:  See definitions of :py:class:`NXOpen.BasePartBookmarkOption`  
        :type bookmarkOption: :py:class:`NXOpen.BasePartBookmarkOption` 
        :param description:  A text string to be stored in the bookmark file  
        :type description: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Rename(self, oldPathName: str, newFileName: str, okToOverwriteExistingFile: bool) -> str:
        """
        Renames an existing bookmark file.  
        
        Signature ``Rename(oldPathName, newFileName, okToOverwriteExistingFile)`` 
        
        :param oldPathName:  Full path name of existing bookmark file.  
        :type oldPathName: str 
        :param newFileName:  New name to assign to the bookmark file.                                                         This will replace the basic name in                                                         the oldPathname.  
        :type newFileName: str 
        :param okToOverwriteExistingFile:  Is it okay to overwrite an existing file                                                         with the same name as oldPathName plus                                                         newFileName?  
        :type okToOverwriteExistingFile: bool 
        :returns:  Full path name to the renamed bookmark file.
        This text string must be freed by the
        caller.  
        :rtype: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDescription(self, pathName: str, description: str) -> None:
        """
        Changes the description of an existing bookmark file.  
        
        Otherwise the bookmark file is unchanged. 
        
        Signature ``SetDescription(pathName, description)`` 
        
        :param pathName:  Full path name of an existing bookmark file.  
        :type pathName: str 
        :param description:  A text string to replace the current description in the bookmark file  
        :type description: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Delete(self, pathName: str) -> None:
        """
        Deletes an existing bookmark file.  
        
        Signature ``Delete(pathName)`` 
        
        :param pathName:  Full path name of existing bookmark file to delete  
        :type pathName: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class ImageCaptureBuilderCaptureMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageCaptureBuilderCaptureMethodType():
    """
    the selection method
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "GraphicsArea", "the graphics area"
       "Region", "the region area"
       "File", "the input from file"
       "Automatic", "the automatic preview mode"
    """
    GraphicsArea = 0  # ImageCaptureBuilderCaptureMethodTypeMemberType
    Region = 1  # ImageCaptureBuilderCaptureMethodTypeMemberType
    File = 2  # ImageCaptureBuilderCaptureMethodTypeMemberType
    Automatic = 3  # ImageCaptureBuilderCaptureMethodTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageCaptureBuilderImageFormatMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageCaptureBuilderImageFormat():
    """
    the image format
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Bmp", "the bmp image format"
       "Jpg", "the jpg image format"
       "Gif", "the gif image format"
       "Png", "the png image format"
       "Tiff", "the tiff image format"
    """
    Bmp = 0  # ImageCaptureBuilderImageFormatMemberType
    Jpg = 1  # ImageCaptureBuilderImageFormatMemberType
    Gif = 2  # ImageCaptureBuilderImageFormatMemberType
    Png = 3  # ImageCaptureBuilderImageFormatMemberType
    Tiff = 4  # ImageCaptureBuilderImageFormatMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageCaptureBuilderImageSizeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageCaptureBuilderImageSize():
    """
    the image size
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Pixels16", "the 16 pixel size"
       "Pixels24", "the 24 pixel size"
       "Pixels32", "the 32 pixel size"
       "Pixels48", "the 48 pixel size"
       "Pixels64", "the 64 pixel size"
       "Pixels96", "the 96 pixel size"
       "Pixels128", "the 128 pixel size"
    """
    Pixels16 = 0  # ImageCaptureBuilderImageSizeMemberType
    Pixels24 = 1  # ImageCaptureBuilderImageSizeMemberType
    Pixels32 = 2  # ImageCaptureBuilderImageSizeMemberType
    Pixels48 = 3  # ImageCaptureBuilderImageSizeMemberType
    Pixels64 = 4  # ImageCaptureBuilderImageSizeMemberType
    Pixels96 = 5  # ImageCaptureBuilderImageSizeMemberType
    Pixels128 = 6  # ImageCaptureBuilderImageSizeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageCaptureBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Gateway.ImageCaptureBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Gateway.ImageCaptureManager.CreateImageCaptureBuilder`
    
    Default values.
    
    ==============  =============
    Property        Value
    ==============  =============
    CaptureMethod   GraphicsArea 
    --------------  -------------
    Format          Bmp 
    --------------  -------------
    Size            Pixels64 
    ==============  =============
    
    .. versionadded:: NX7.5.0
    """
    
    class CaptureMethodType():
        """
        the selection method
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "GraphicsArea", "the graphics area"
           "Region", "the region area"
           "File", "the input from file"
           "Automatic", "the automatic preview mode"
        """
        GraphicsArea = 0  # ImageCaptureBuilderCaptureMethodTypeMemberType
        Region = 1  # ImageCaptureBuilderCaptureMethodTypeMemberType
        File = 2  # ImageCaptureBuilderCaptureMethodTypeMemberType
        Automatic = 3  # ImageCaptureBuilderCaptureMethodTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ImageFormat():
        """
        the image format
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Bmp", "the bmp image format"
           "Jpg", "the jpg image format"
           "Gif", "the gif image format"
           "Png", "the png image format"
           "Tiff", "the tiff image format"
        """
        Bmp = 0  # ImageCaptureBuilderImageFormatMemberType
        Jpg = 1  # ImageCaptureBuilderImageFormatMemberType
        Gif = 2  # ImageCaptureBuilderImageFormatMemberType
        Png = 3  # ImageCaptureBuilderImageFormatMemberType
        Tiff = 4  # ImageCaptureBuilderImageFormatMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ImageSize():
        """
        the image size
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Pixels16", "the 16 pixel size"
           "Pixels24", "the 24 pixel size"
           "Pixels32", "the 32 pixel size"
           "Pixels48", "the 48 pixel size"
           "Pixels64", "the 64 pixel size"
           "Pixels96", "the 96 pixel size"
           "Pixels128", "the 128 pixel size"
        """
        Pixels16 = 0  # ImageCaptureBuilderImageSizeMemberType
        Pixels24 = 1  # ImageCaptureBuilderImageSizeMemberType
        Pixels32 = 2  # ImageCaptureBuilderImageSizeMemberType
        Pixels48 = 3  # ImageCaptureBuilderImageSizeMemberType
        Pixels64 = 4  # ImageCaptureBuilderImageSizeMemberType
        Pixels96 = 5  # ImageCaptureBuilderImageSizeMemberType
        Pixels128 = 6  # ImageCaptureBuilderImageSizeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetRegion(self) -> tuple:
        """
        Returns the region 
        
        Signature ``GetRegion()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (topLeftCorner, bottomRightCorner). topLeftCorner is a list of int.   Array of 2 integers for Top Left Corner of Region bottomRightCorner is a list of int.   Array of 2 integers for Bottom Right Corner of Region 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRegion(self, topLeftCorner: 'list[int]', bottomRightCorner: 'list[int]') -> None:
        """
        Sets the region 
        
        Signature ``SetRegion(topLeftCorner, bottomRightCorner)`` 
        
        :param topLeftCorner:  Array of 2 integers for Top Left Corner of Region  
        :type topLeftCorner: list of int 
        :param bottomRightCorner:  Array of 2 integers for Bottom Right Corner of Region  
        :type bottomRightCorner: list of int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    CaptureMethod: ImageCaptureBuilderCaptureMethodType = ...
    """
    Returns or sets  the capture method 
    
    <hr>
    
    Getter Method
    
    Signature ``CaptureMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Gateway.ImageCaptureBuilderCaptureMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CaptureMethod`` 
    
    :param captureMethod: 
    :type captureMethod: :py:class:`NXOpen.Gateway.ImageCaptureBuilderCaptureMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: drafting ("DRAFTING")
    """
    File: str = ...
    """
    Returns or sets  the file 
    
    <hr>
    
    Getter Method
    
    Signature ``File`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``File`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: drafting ("DRAFTING")
    """
    Format: ImageCaptureBuilderImageFormat = ...
    """
    Returns or sets  the format 
    
    <hr>
    
    Getter Method
    
    Signature ``Format`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Gateway.ImageCaptureBuilderImageFormat` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Format`` 
    
    :param format: 
    :type format: :py:class:`NXOpen.Gateway.ImageCaptureBuilderImageFormat` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: drafting ("DRAFTING")
    """
    ImageFile: str = ...
    """
    Returns or sets  the image file 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageFile`` 
    
    :param imageFilename: 
    :type imageFilename: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: drafting ("DRAFTING")
    """
    Size: ImageCaptureBuilderImageSize = ...
    """
    Returns or sets  the size 
    
    <hr>
    
    Getter Method
    
    Signature ``Size`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Gateway.ImageCaptureBuilderImageSize` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Size`` 
    
    :param size: 
    :type size: :py:class:`NXOpen.Gateway.ImageCaptureBuilderImageSize` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: drafting ("DRAFTING")
    """
    Null: ImageCaptureBuilder = ...  # unknown typename


class IGenericFileNewApplicationBuilder(NXOpen.Builder, NXOpen.IAttributeSourceObjectBuilder):
    """
    Represents the class Application Builder.  
    
    Instances of this class can be accessed through various application specific builders
    
    .. versionadded:: NX11.0.0
    """
    
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
    
    Null: IGenericFileNewApplicationBuilder = ...  # unknown typename


class BaseExplicitOrderBuilder(NXOpen.Builder):
    """
    This is the :py:class:`NXOpen.Gateway.BaseExplicitOrderBuilder` for the explicit order  
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX9.0.0
    """
    
    def Save(self, orderList: 'list[str]', saveName: str) -> None:
        """
        Saves an explicit order defined by the user 
        
        Signature ``Save(orderList, saveName)`` 
        
        :param orderList: 
        :type orderList: list of str 
        :param saveName: 
        :type saveName: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Paste(self, pastePoint: int, selectedEntries: 'list[str]', currentOrder: 'list[str]') -> 'list[str]':
        """
        Pastes the rows that have been previously selected using the cut operation  
        
        Signature ``Paste(pastePoint, selectedEntries, currentOrder)`` 
        
        :param pastePoint: 
        :type pastePoint: int 
        :param selectedEntries: 
        :type selectedEntries: list of str 
        :param currentOrder: 
        :type currentOrder: list of str 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Delete(self, selectedEntries: 'list[str]', currentOrder: 'list[str]', numOfRemainingEntries: int) -> 'list[str]':
        """
        Deletes the saved order/orders that has/have been selected by the user from the list of saved orders  
        
        Signature ``Delete(selectedEntries, currentOrder, numOfRemainingEntries)`` 
        
        :param selectedEntries: 
        :type selectedEntries: list of str 
        :param currentOrder: 
        :type currentOrder: list of str 
        :param numOfRemainingEntries: 
        :type numOfRemainingEntries: int 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Clear(self) -> None:
        """
        Clears the current order and restores it to the default order 
        
        Signature ``Clear()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DownArrow(self, selectedEntries: 'list[str]', currentOrder: 'list[str]') -> 'list[str]':
        """
        Moves down the row/rows selected by the user in the lists  
        
        Signature ``DownArrow(selectedEntries, currentOrder)`` 
        
        :param selectedEntries: 
        :type selectedEntries: list of str 
        :param currentOrder: 
        :type currentOrder: list of str 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UpArrow(self, selectedEntries: 'list[str]', currentOrder: 'list[str]') -> 'list[str]':
        """
        Moves up the row/rows selected by the user in the lists  
        
        Signature ``UpArrow(selectedEntries, currentOrder)`` 
        
        :param selectedEntries: 
        :type selectedEntries: list of str 
        :param currentOrder: 
        :type currentOrder: list of str 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveAsTextFile(self, savedOrderName: str, saveFileName: str, overwriteFile: bool) -> None:
        """
        Saves the selected saved order in the form of a text file 
        
        Signature ``SaveAsTextFile(savedOrderName, saveFileName, overwriteFile)`` 
        
        :param savedOrderName: 
        :type savedOrderName: str 
        :param saveFileName: 
        :type saveFileName: str 
        :param overwriteFile: 
        :type overwriteFile: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    SaveName: str = ...
    """
    Returns or sets  the save name 
    
    <hr>
    
    Getter Method
    
    Signature ``SaveName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SaveName`` 
    
    :param saveName: 
    :type saveName: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: BaseExplicitOrderBuilder = ...  # unknown typename


class CopyCutBuilderStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CopyCutBuilderStatus():
    """
    Status of Copy or Cut Operation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoObjectsCopied", "No objects were successfully copied"
       "NonExportableObjects", "Certain non-exportable objects were not copied"
       "PartExportFailed", "Error while exporting part with copied/cut objects"
       "ErrorDuringCut", "Error during the cut operation"
       "AllObjectsCopied", "All objects were successfully copied"
    """
    NoObjectsCopied = 0  # CopyCutBuilderStatusMemberType
    NonExportableObjects = 1  # CopyCutBuilderStatusMemberType
    PartExportFailed = 2  # CopyCutBuilderStatusMemberType
    ErrorDuringCut = 3  # CopyCutBuilderStatusMemberType
    AllObjectsCopied = 4  # CopyCutBuilderStatusMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CopyCutBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Gateway.CopyCutBuilder`
    
    To create a new instance of this class, use :py:meth:`NXOpen.ClipboardOperationsManager.CreateCopyCutBuilder`
    
    .. versionadded:: NX7.5.0
    """
    
    class Status():
        """
        Status of Copy or Cut Operation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoObjectsCopied", "No objects were successfully copied"
           "NonExportableObjects", "Certain non-exportable objects were not copied"
           "PartExportFailed", "Error while exporting part with copied/cut objects"
           "ErrorDuringCut", "Error during the cut operation"
           "AllObjectsCopied", "All objects were successfully copied"
        """
        NoObjectsCopied = 0  # CopyCutBuilderStatusMemberType
        NonExportableObjects = 1  # CopyCutBuilderStatusMemberType
        PartExportFailed = 2  # CopyCutBuilderStatusMemberType
        ErrorDuringCut = 3  # CopyCutBuilderStatusMemberType
        AllObjectsCopied = 4  # CopyCutBuilderStatusMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetCopyCutStatus(self) -> CopyCutBuilderStatus:
        """
        Gets the status of copy-cut operation  
        
        Signature ``GetCopyCutStatus()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Gateway.CopyCutBuilderStatus` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNonExportableObjects(self) -> 'list[NXOpen.NXObject]':
        """
        Gets all non-exportable objects  
        
        Signature ``GetNonExportableObjects()`` 
        
        :returns:  All the non-exportable objects  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetObjects(self) -> 'list[NXOpen.NXObject]':
        """
        Gets all objects to be copied or to be cut  
        
        Signature ``GetObjects()`` 
        
        :returns:  All the objects to be copied or to be cut 
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetObjects(self, objects: 'list[NXOpen.NXObject]') -> None:
        """
        Sets all objects to be copied or to be cut 
        
        Signature ``SetObjects(objects)`` 
        
        :param objects:  All the objects to be copied or to be cut 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetInitialCopyLocation(self) -> None:
        """
        Reset the initial copy location.  
        
        After this previously set initial copy location will not be used 
        
        Signature ``ResetInitialCopyLocation()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    CanCopyAsSketch: bool = ...
    """
    Returns or sets  a flag indicating whether to copy as sketch curves or not 
    
    <hr>
    
    Getter Method
    
    Signature ``CanCopyAsSketch`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanCopyAsSketch`` 
    
    :param canCopyAsSketch: 
    :type canCopyAsSketch: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    DestinationFilename: str = ...
    """
    Returns or sets  the string of the filename to which to copy or cut the objects to 
    
    <hr>
    
    Getter Method
    
    Signature ``DestinationFilename`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DestinationFilename`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    InitialCopyLocation: NXOpen.Point3d = ...
    """
    Returns or sets  the initial copy location mainly used to define default copy location of sketch objects 
    
    <hr>
    
    Getter Method
    
    Signature ``InitialCopyLocation`` 
    
    :returns:  Copy location in absolute coordinates  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InitialCopyLocation`` 
    
    :param copyLocation:  Copy location in absolute coordinates  
    :type copyLocation: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    IsCut: bool = ...
    """
    Returns or sets  a flag indicating whether it is a copy or cut operation 
    
    <hr>
    
    Getter Method
    
    Signature ``IsCut`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsCut`` 
    
    :param isCut: 
    :type isCut: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ToClipboard: bool = ...
    """
    Returns or sets  a flag indicating whether copy cut to clipboard or copy cut to a file
    
    <hr>
    
    Getter Method
    
    Signature ``ToClipboard`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToClipboard`` 
    
    :param isToClipboard: 
    :type isToClipboard: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: CopyCutBuilder = ...  # unknown typename


class GenericFileNewBuilder(NXOpen.Builder):
    """
    Represents a builder class that performs Generic File New operations.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.PartCollection.CreateGenericFileNewBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def CreateLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Creates the pre-creation objects for the parts 
        
        Signature ``CreateLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetApplicationBuilder(self, applicationBuilder: IGenericFileNewApplicationBuilder) -> None:
        """
        Sets :py:class:`NXOpen.Gateway.IGenericFileNewApplicationBuilder` 
        
        Signature ``SetApplicationBuilder(applicationBuilder)`` 
        
        :param applicationBuilder: 
        :type applicationBuilder: :py:class:`NXOpen.Gateway.IGenericFileNewApplicationBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: GenericFileNewBuilder = ...  # unknown typename


