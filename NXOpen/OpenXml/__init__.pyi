# module 'NXOpen.OpenXml'
#
# Automatically generated 2025-06-09T14:38:47.187736
#
"""Default documentation for NXOpen.OpenXml."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class DocumentDataTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DocumentDataType():
    """
    the document data type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Base", "the base document data type"
       "Text", "the document data type of text"
       "Table", "the document data type of table"
       "TableCell", "the document data type of table cell"
       "Image", "the document data type of image"
       "ImageGroup", "the document data type of image group"
       "Group", "the document data type of data group"
    """
    Base = 0  # DocumentDataTypeMemberType
    Text = 1  # DocumentDataTypeMemberType
    Table = 2  # DocumentDataTypeMemberType
    TableCell = 3  # DocumentDataTypeMemberType
    Image = 4  # DocumentDataTypeMemberType
    ImageGroup = 5  # DocumentDataTypeMemberType
    Group = 6  # DocumentDataTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DocumentData(NXOpen.TransientObject):
    """
    Represents the definition of the base document data  
    
    .. versionadded:: NX11.0.0
    """
    
    class Type():
        """
        the document data type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Base", "the base document data type"
           "Text", "the document data type of text"
           "Table", "the document data type of table"
           "TableCell", "the document data type of table cell"
           "Image", "the document data type of image"
           "ImageGroup", "the document data type of image group"
           "Group", "the document data type of data group"
        """
        Base = 0  # DocumentDataTypeMemberType
        Text = 1  # DocumentDataTypeMemberType
        Table = 2  # DocumentDataTypeMemberType
        TableCell = 3  # DocumentDataTypeMemberType
        Image = 4  # DocumentDataTypeMemberType
        ImageGroup = 5  # DocumentDataTypeMemberType
        Group = 6  # DocumentDataTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    
    def GetDataType(self) -> DocumentDataType:
        """
        Gets a specified document data type  
        
        Signature ``GetDataType()`` 
        
        :returns:  the data type defined by the :py:class:`NXOpen.OpenXml.DocumentDataType`  
        :rtype: :py:class:`NXOpen.OpenXml.DocumentDataType` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class TableDocumentDataCaptionPositionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TableDocumentDataCaptionPosition():
    """
    the location of the caption for table data
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Above", "the above position"
       "Bellow", "the bellow position"
    """
    Above = 0  # TableDocumentDataCaptionPositionMemberType
    Bellow = 1  # TableDocumentDataCaptionPositionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TableDocumentData(DocumentData):
    """
    Represents the table to be exported to the speific Open XML file.  
    
    .. versionadded:: NX11.0.0
    """
    
    class CaptionPosition():
        """
        the location of the caption for table data
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Above", "the above position"
           "Bellow", "the bellow position"
        """
        Above = 0  # TableDocumentDataCaptionPositionMemberType
        Bellow = 1  # TableDocumentDataCaptionPositionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    
    def GetColumnCount(self) -> int:
        """
        Gets the column count of table data 
        
        Signature ``GetColumnCount()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRowCount(self) -> int:
        """
        Gets the row count of table data 
        
        Signature ``GetRowCount()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCaption(self) -> tuple:
        """
        Gets the caption of the table data 
        
        Signature ``GetCaption()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (caption, position). caption is a str. position is a :py:class:`NXOpen.OpenXml.TableDocumentDataCaptionPosition`. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCaption(self, position: TableDocumentDataCaptionPosition, caption: str) -> None:
        """
        Sets the caption of the table data
        
        Signature ``SetCaption(position, caption)`` 
        
        :param position: 
        :type position: :py:class:`NXOpen.OpenXml.TableDocumentDataCaptionPosition` 
        :param caption: 
        :type caption: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumnWidths(self) -> 'list[float]':
        """
        Gets the width array of the columns  
        
        Signature ``GetColumnWidths()`` 
        
        :returns:  the column width array  
        :rtype: list of float 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetColumnWidths(self, widths: 'list[float]') -> None:
        """
        Sets the width array of the columns 
        
        Signature ``SetColumnWidths(widths)`` 
        
        :param widths:  the column width array  
        :type widths: list of float 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRowHeigths(self) -> 'list[float]':
        """
        Gets the height array of the rows  
        
        Signature ``GetRowHeigths()`` 
        
        :returns:  the column width array  
        :rtype: list of float 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRowHeigths(self, heigths: 'list[float]') -> None:
        """
        Sets the height array of the rows 
        
        Signature ``SetRowHeigths(heigths)`` 
        
        :param heigths:  the column width array  
        :type heigths: list of float 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddCellData(self, grids: 'list[int]') -> TableCellData:
        """
        Creates a new :py:class:`NXOpen.OpenXml.TableCellData` object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.OpenXml.TableDocumentData` object 
        
        Signature ``AddCellData(grids)`` 
        
        :param grids:  the grid IDs to be mergered into the cell data 
        :type grids: list of int 
        :returns:  the table cell data  
        :rtype: :py:class:`NXOpen.OpenXml.TableCellData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCellsCount(self) -> int:
        """
        Gets the number of table cells  
        
        Signature ``GetCellsCount()`` 
        
        :returns:  number of table cells 
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNthCell(self, index: int) -> TableCellData:
        """
        Gets the nth table cell data 
        
        Signature ``GetNthCell(index)`` 
        
        :param index:  the index of table cell data 
        :type index: int 
        :returns:  the table cell data  
        :rtype: :py:class:`NXOpen.OpenXml.TableCellData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class ImageDocumentDataCaptionPositionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ImageDocumentDataCaptionPosition():
    """
    the location of the caption for image data
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Above", "the above position"
       "Bellow", "the bellow position"
    """
    Above = 0  # ImageDocumentDataCaptionPositionMemberType
    Bellow = 1  # ImageDocumentDataCaptionPositionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ImageDocumentData(DocumentData):
    """
    Represents the image to be exported to the speific Open XML file.  
    
    .. versionadded:: NX11.0.0
    """
    
    class CaptionPosition():
        """
        the location of the caption for image data
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Above", "the above position"
           "Bellow", "the bellow position"
        """
        Above = 0  # ImageDocumentDataCaptionPositionMemberType
        Bellow = 1  # ImageDocumentDataCaptionPositionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    
    def GetFileName(self) -> str:
        """
        Gets the file name of the image data 
        
        Signature ``GetFileName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFileName(self, fileName: str) -> None:
        """
        Sets the file name of the image data
        
        Signature ``SetFileName(fileName)`` 
        
        :param fileName: 
        :type fileName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCaption(self) -> tuple:
        """
        Gets the caption of the image data 
        
        Signature ``GetCaption()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (caption, position). caption is a str. position is a :py:class:`NXOpen.OpenXml.ImageDocumentDataCaptionPosition`. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCaption(self, position: ImageDocumentDataCaptionPosition, caption: str) -> None:
        """
        Sets the caption of the image data
        
        Signature ``SetCaption(position, caption)`` 
        
        :param position: 
        :type position: :py:class:`NXOpen.OpenXml.ImageDocumentDataCaptionPosition` 
        :param caption: 
        :type caption: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class TableCellData(DocumentData):
    """
    Represents the table cell to be exported to the speific Open XML file.  
    
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
    
    
    def GetGridsId(self) -> 'list[int]':
        """
        Gets the grid IDs of the table cell 
        
        Signature ``GetGridsId()`` 
        
        :returns:  the grid ID array  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddText(self, textContent: str) -> TextDocumentData:
        """
        Creates a new :py:class:`NXOpen.OpenXml.TextDocumentData` object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.OpenXml.TableCellData` object 
        
        Signature ``AddText(textContent)`` 
        
        :param textContent:  the content of the text data 
        :type textContent: str 
        :returns:  the text data  
        :rtype: :py:class:`NXOpen.OpenXml.TextDocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddImageGroup(self) -> ImageGroupDocumentData:
        """
        Creates a new :py:class:`NXOpen.OpenXml.ImageGroupDocumentData` object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.OpenXml.TableCellData` object 
        
        Signature ``AddImageGroup()`` 
        
        :returns:  the image group data  
        :rtype: :py:class:`NXOpen.OpenXml.ImageGroupDocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetContentCount(self) -> int:
        """
        Gets the number of content in the table cell 
        
        Signature ``GetContentCount()`` 
        
        :returns:  the number of content  
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNthContent(self, index: int) -> DocumentData:
        """
        Gets the nth content data        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.OpenXml.TableCellData` object 
        
        Signature ``GetNthContent(index)`` 
        
        :param index:  the index of content 
        :type index: int 
        :returns:  the content 
        :rtype: :py:class:`NXOpen.OpenXml.DocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteNthContent(self, index: int) -> None:
        """
        Removes the nth content data
        
        Signature ``DeleteNthContent(index)`` 
        
        :param index:  the index of content 
        :type index: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearContents(self) -> None:
        """
        Removes all contents data
        
        Signature ``ClearContents()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class DocumentDataGroup(DocumentData):
    """
    Contains methods for adding document data for CAE Report.  
    
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
    
    
    def AddText(self, textContent: str) -> TextDocumentData:
        """
        Creates a new :py:class:`NXOpen.OpenXml.TextDocumentData` object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.OpenXml.DocumentDataGroup` object 
        
        Signature ``AddText(textContent)`` 
        
        :param textContent:  the content of the text data 
        :type textContent: str 
        :returns:  the text data  
        :rtype: :py:class:`NXOpen.OpenXml.TextDocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddImageGroup(self) -> ImageGroupDocumentData:
        """
        Creates a new :py:class:`NXOpen.OpenXml.ImageGroupDocumentData` object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.OpenXml.DocumentDataGroup` object 
        
        Signature ``AddImageGroup()`` 
        
        :returns:  the image group data  
        :rtype: :py:class:`NXOpen.OpenXml.ImageGroupDocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddTable(self, columnCount: int, rowCount: int) -> TableDocumentData:
        """
        Creates a new :py:class:`NXOpen.OpenXml.TableDocumentData` object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.OpenXml.DocumentDataGroup` object 
        
        Signature ``AddTable(columnCount, rowCount)`` 
        
        :param columnCount:  the column size of the table 
        :type columnCount: int 
        :param rowCount:  the row size of the table 
        :type rowCount: int 
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
    
    
    def GetNthData(self, index: int) -> DocumentData:
        """
        Gets the nth document data object.  
        
        Does not to free this object, it will be free while deleting 
        :py:class:`NXOpen.OpenXml.DocumentDataGroup` object 
        
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
        Deletes the nth document data
        
        Signature ``DeleteNthData(index)`` 
        
        :param index:  the index of data 
        :type index: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteAllData(self) -> None:
        """
        Deletes all document data
        
        Signature ``DeleteAllData()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class ImageGroupDocumentData(DocumentData):
    """
    Represents the group of images to be exported to the speific Open XML file.  
    
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
    
    
    def AddImage(self, fileName: str, caption: str) -> ImageDocumentData:
        """
        Creates a new :py:class:`NXOpen.OpenXml.ImageDocumentData` object.  
        
        Signature ``AddImage(fileName, caption)`` 
        
        :param fileName:  the file name of the image data 
        :type fileName: str 
        :param caption:  the caption of the image data 
        :type caption: str 
        :returns:  the image data  
        :rtype: :py:class:`NXOpen.OpenXml.ImageDocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetImagesCount(self) -> int:
        """
        Gets the number of images  
        
        Signature ``GetImagesCount()`` 
        
        :returns:  number of images 
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNthImage(self, index: int) -> ImageDocumentData:
        """
        Gets the nth image data 
        
        Signature ``GetNthImage(index)`` 
        
        :param index:  the index of image data 
        :type index: int 
        :returns:  the image data 
        :rtype: :py:class:`NXOpen.OpenXml.ImageDocumentData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteNthImage(self, index: int) -> None:
        """
        Deletes the nth image data
        
        Signature ``DeleteNthImage(index)`` 
        
        :param index:  the index of image 
        :type index: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteAllImages(self) -> None:
        """
        Deletes all images data
        
        Signature ``DeleteAllImages()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class TextDocumentData(DocumentData):
    """
    Represents the text to be exported to the speific Open XML file.  
    
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
    
    
    def GetContent(self) -> str:
        """
        Gets the content to be exported of text data 
        
        Signature ``GetContent()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContent(self, content: str) -> None:
        """
        Sets the content to be exported of text data
        
        Signature ``SetContent(content)`` 
        
        :param content: 
        :type content: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


