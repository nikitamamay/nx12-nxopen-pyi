# module 'NXOpen.CAE.FTK'
#
# Automatically generated 2025-06-09T14:38:44.214885
#

import typing

import NXOpen
import NXOpen.CAE



class BaseRecord(NXOpen.NXObject):
    """
    Manages the base record.  
    
    Not support KF.
    
    .. versionadded:: NX7.5.0
    """
    
    def GetAbscissaUnit(self) -> BaseUnit:
        """
        Gets the abscissa unit  
        
        Signature ``GetAbscissaUnit()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOrdinateUnit(self) -> BaseUnit:
        """
        Gets the ordinate unit  
        
        Signature ``GetOrdinateUnit()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPointLabels(self) -> 'list[str]':
        """
        Gets the point labels  
        
        Signature ``GetPointLabels()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    LegendName: str = ...
    """
    Returns  the legend name 
    
    <hr>
    
    Getter Method
    
    Signature ``LegendName`` 
    
    :returns:  Legend name  
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: BaseRecord = ...  # unknown typename


class IApplicationDataOwner():
    """
    Represents the interface for  application specific data owner  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class SectionBasedMatrixRecord(BaseRecord, IApplicationDataOwner):
    """
    Represents a kind of record data could be displayed by 3D graphing.  
    
    The record is consist of multiple section data and each section
    data repsresents a 2D record data. 
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def RemoveSectionData(self, sectionIndex: int) -> None:
        """
        Removes the data values of the specific section.  
        
        The section index must be greater than
        or equal to 0 and less than :py:meth:`CAE.FTK.SectionBasedMatrixRecord.SectionCount`. 
        
        Signature ``RemoveSectionData(sectionIndex)`` 
        
        :param sectionIndex:  Section index  
        :type sectionIndex: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetApplicationData(self) -> IApplicationData:
        """
        Gets the application specific data associated with the record  
        
        Signature ``GetApplicationData()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.FTK.IApplicationData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetApplicationData(self, applicationData: IApplicationData) -> None:
        """
        Sets the application specific data to the record 
        
        Signature ``SetApplicationData(applicationData)`` 
        
        :param applicationData: 
        :type applicationData: :py:class:`NXOpen.CAE.FTK.IApplicationData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    SectionCount: int = ...
    """
    Returns  the section count 
    
    <hr>
    
    Getter Method
    
    Signature ``SectionCount`` 
    
    :returns:  Section count  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Title: str = ...
    """
    Returns  the title name 
    
    <hr>
    
    Getter Method
    
    Signature ``Title`` 
    
    :returns:  Title name  
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    XCoordinateUnit: BaseUnit = ...
    """
    Returns or sets  the X-Coordinate unit 
    
    <hr>
    
    Getter Method
    
    Signature ``XCoordinateUnit`` 
    
    :returns:  X-Coordinate unit  
    :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XCoordinateUnit`` 
    
    :param xCoordinateUnit:  X-Coordinate unit  
    :type xCoordinateUnit: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    YCoordinateUnit: BaseUnit = ...
    """
    Returns or sets  the Y-Coordinate unit 
    
    <hr>
    
    Getter Method
    
    Signature ``YCoordinateUnit`` 
    
    :returns:  Y-Coordinate unit  
    :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``YCoordinateUnit`` 
    
    :param yCoordinateUnit:  Y-Coordinate unit  
    :type yCoordinateUnit: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ZCoordinateUnit: BaseUnit = ...
    """
    Returns or sets  the Z-Coordinate unit 
    
    <hr>
    
    Getter Method
    
    Signature ``ZCoordinateUnit`` 
    
    :returns:  Z-Coordinate unit  
    :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZCoordinateUnit`` 
    
    :param zCoordinateUnit:  Z-Coordinate unit  
    :type zCoordinateUnit: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: SectionBasedMatrixRecord = ...  # unknown typename


class RealSectionBasedMatrixRecord(SectionBasedMatrixRecord):
    """
    Represents a section based matrix record which has real data values.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def AddSectionData(self, xCoordinatePoints: 'list[float]', yCoordinatePoints: 'list[float]', zCoordinatePoint: float) -> None:
        """
        Adds the real data values for each section.  
        
        Signature ``AddSectionData(xCoordinatePoints, yCoordinatePoints, zCoordinatePoint)`` 
        
        :param xCoordinatePoints:  X-Coordinate data  
        :type xCoordinatePoints: list of float 
        :param yCoordinatePoints:  Y-Coordinate data  
        :type yCoordinatePoints: list of float 
        :param zCoordinatePoint:  Z-Coordinate data  
        :type zCoordinatePoint: float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSectionData(self, sectionIndex: int) -> tuple:
        """
        Gets the real data values from specific section.  
        
        Signature ``GetSectionData(sectionIndex)`` 
        
        :param sectionIndex:  Section index  
        :type sectionIndex: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (xCoordinatePoints, yCoordinatePoints, zCoordinatePoints). xCoordinatePoints is a list of float.   X-Coordinate data yCoordinatePoints is a list of float.   Y-Coordinate data zCoordinatePoints is a float.   Z-Coordinate data 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: RealSectionBasedMatrixRecord = ...  # unknown typename


class Op2Record(BaseRecord):
    """
    Represents the op2 record data   
    
    Not support KF.
    
    .. versionadded:: NX12.0.0
    """
    
    def ListInformation(self, fileName: str, listInfo: bool, listData: bool) -> None:
        """
        Lists the record information to a file or listing information window 
        
        Signature ``ListInformation(fileName, listInfo, listData)`` 
        
        :param fileName:  if NULL, print information to listing information window. Otherwise write information to the file  
        :type fileName: str 
        :param listInfo:  if true, print header information  
        :type listInfo: bool 
        :param listData:  if true, print data information  
        :type listData: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Op2Record = ...  # unknown typename


class BaseUnit(NXOpen.NXObject):
    """
    Manages the base unit   
    
    Not support KF.
    
    .. versionadded:: NX7.5.0
    """
    
    def SetMeasureName(self, measureName: str) -> None:
        """
        Sets measure name 
        
        Signature ``SetMeasureName(measureName)`` 
        
        :param measureName:  Measure name  
        :type measureName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetUnitName(self, unitName: str) -> None:
        """
        Sets unit name 
        
        Signature ``SetUnitName(unitName)`` 
        
        :param unitName:  Unit name  
        :type unitName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetConstituentUnitsCount(self) -> int:
        """
        Gets the count of constituent units  
        
        Signature ``GetConstituentUnitsCount()`` 
        
        :returns:  constituent units count  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetConstituentUnit(self, nthConstituentUnitIndex: int) -> BaseUnit:
        """
        Gets constituent unit by index 
        
        Signature ``GetConstituentUnit(nthConstituentUnitIndex)`` 
        
        :param nthConstituentUnitIndex:  The index must be greater or equal to 0  and less than :py:meth:`CAE.FTK.BaseUnit.GetConstituentUnitsCount`  
        :type nthConstituentUnitIndex: int 
        :returns:  constituent unit  
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNxUnit(self, nxUnit: NXOpen.Unit) -> None:
        """
        Sets nx unit. 
        
        To make sure the base unit could be changed successfully,two conditions must be satisfied:
        
          #. The measure of input nx unit must be same as the nx unit saved in BaseUnit.
          #. The BaseUnit must be created by method :py:meth:`CAE.FTK.DataManager.CreateArrayUnit`,but except for the method which creates
        unit by numerator and denominator unit.
        
        Signature ``SetNxUnit(nxUnit)`` 
        
        :param nxUnit: 
        :type nxUnit: :py:class:`NXOpen.Unit` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: BaseUnit = ...  # unknown typename


class ArrayRecord2D(BaseRecord, IApplicationDataOwner):
    """
    Manages the 2d array record   
    
    Not support KF.
    
    .. versionadded:: NX7.5.0
    """
    
    def SetXCoordinateUnit(self, xCoordinateUnit: BaseUnit) -> None:
        """
        Sets X-Coordinate unit 
        
        Signature ``SetXCoordinateUnit(xCoordinateUnit)`` 
        
        :param xCoordinateUnit:  X-Coordinate unit  
        :type xCoordinateUnit: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetXCoordinateUnit(self) -> BaseUnit:
        """
        Gets X-Coordinate unit  
        
        Signature ``GetXCoordinateUnit()`` 
        
        :returns:  X-Coordinate unit  
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetYCoordinateUnit(self, yCoordinateUnit: BaseUnit) -> None:
        """
        Sets Y-Coordinate unit 
        
        Signature ``SetYCoordinateUnit(yCoordinateUnit)`` 
        
        :param yCoordinateUnit:  Y-Coordinate unit  
        :type yCoordinateUnit: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetYCoordinateUnit(self) -> BaseUnit:
        """
        Gets Y-Coordinate unit  
        
        Signature ``GetYCoordinateUnit()`` 
        
        :returns:  Y-Coordinate unit  
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRealData(self, xCoordinatePoints: 'list[float]', yCoordinatePoints: 'list[float]') -> None:
        """
        Sets real points data 
        
        Signature ``SetRealData(xCoordinatePoints, yCoordinatePoints)`` 
        
        :param xCoordinatePoints:  X-Coordinate data  
        :type xCoordinatePoints: list of float 
        :param yCoordinatePoints:  Y-Coordinate data  
        :type yCoordinatePoints: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRealData(self) -> tuple:
        """
        Gets real points data  
        
        Signature ``GetRealData()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (xCoordinatePoints, yCoordinatePoints). xCoordinatePoints is a list of float.   X-Coordinate data yCoordinatePoints is a list of float.   Y-Coordinate data 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetComplexData(self, xCoordinatePoints: 'list[float]', yCoordinateReal: 'list[float]', yCoordinateImag: 'list[float]') -> None:
        """
        Sets complex points data 
        
        Signature ``SetComplexData(xCoordinatePoints, yCoordinateReal, yCoordinateImag)`` 
        
        :param xCoordinatePoints:  X-Coordinate data  
        :type xCoordinatePoints: list of float 
        :param yCoordinateReal:  Real part of Y-Coordinate data  
        :type yCoordinateReal: list of float 
        :param yCoordinateImag:  Imaginary part of Y-Coordinate data  
        :type yCoordinateImag: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetComplexData(self) -> tuple:
        """
        Gets complex points data  
        
        Signature ``GetComplexData()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (xCoordinatePoints, yCoordinateReal, yCoordinateImag). xCoordinatePoints is a list of float.   X-Coordinate data yCoordinateReal is a list of float.   Real part of Y-Coordinate data yCoordinateImag is a list of float.   Imaginary part of Y-Coordinate data 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTitle(self) -> str:
        """
        Gets the title  
        
        Signature ``GetTitle()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPointLabels(self, pointLabels: 'list[str]') -> None:
        """
        Sets the point labels 
        
        Signature ``SetPointLabels(pointLabels)`` 
        
        :param pointLabels: 
        :type pointLabels: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetApplicationData(self) -> IApplicationData:
        """
        Gets the application specific data associated with the record  
        
        Signature ``GetApplicationData()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.FTK.IApplicationData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetApplicationData(self, applicationData: IApplicationData) -> None:
        """
        Sets the application specific data to the record 
        
        Signature ``SetApplicationData(applicationData)`` 
        
        :param applicationData: 
        :type applicationData: :py:class:`NXOpen.CAE.FTK.IApplicationData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ArrayRecord2D = ...  # unknown typename


class ArrayRecord2DEven(ArrayRecord2D):
    """
    Manages the 2d array record with even abscissa data   
    
    Not support KF.
    
    .. versionadded:: NX7.5.0
    """
    
    def SetEvenRealData(self, xMinimum: float, xIncrement: float, yCoordinatePoints: 'list[float]') -> None:
        """
        Sets even real data 
        
        Signature ``SetEvenRealData(xMinimum, xIncrement, yCoordinatePoints)`` 
        
        :param xMinimum:  Minimum abscissa data value  
        :type xMinimum: float 
        :param xIncrement:  Abscissa increment  
        :type xIncrement: float 
        :param yCoordinatePoints:  Y-Coordinate data  
        :type yCoordinatePoints: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetEvenRealData(self) -> tuple:
        """
        Gets even real data  
        
        Signature ``GetEvenRealData()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (yCoordinatePoints, xMinimum, xIncrement). yCoordinatePoints is a list of float.   Y-Coordinate data xMinimum is a float.   Minimum abscissa data value xIncrement is a float.   Abscissa increment 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEvenComplexData(self, xMinimum: float, xIncrement: float, yCoordinateReal: 'list[float]', yCoordinateImag: 'list[float]') -> None:
        """
        Sets even complex data 
        
        Signature ``SetEvenComplexData(xMinimum, xIncrement, yCoordinateReal, yCoordinateImag)`` 
        
        :param xMinimum:  Minimum abscissa data value  
        :type xMinimum: float 
        :param xIncrement:  Abscissa increment  
        :type xIncrement: float 
        :param yCoordinateReal:  Real part of Y-Coordinate data  
        :type yCoordinateReal: list of float 
        :param yCoordinateImag:  Imaginary part of Y-Coordinate data  
        :type yCoordinateImag: list of float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetEvenComplexData(self) -> tuple:
        """
        Gets even complex data  
        
        Signature ``GetEvenComplexData()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (yCoordinateReal, xMinimum, xIncrement, yCoordinateImag). yCoordinateReal is a list of float.   Real part of Y-Coordinate data xMinimum is a float.   Minimum abscissa data value xIncrement is a float.   Abscissa increment yCoordinateImag is a list of float.   Imaginary part of Y-Coordinate data 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ArrayRecord2DEven = ...  # unknown typename


class ArrayRecord3D(ArrayRecord2D):
    """
    Manages the 3d array record   
    
    Not support KF.
    
    .. versionadded:: NX7.5.0
    """
    
    def SetZCoordinateUnit(self, zCoordinateUnit: BaseUnit) -> None:
        """
        Sets Z-Coordinate unit 
        
        Signature ``SetZCoordinateUnit(zCoordinateUnit)`` 
        
        :param zCoordinateUnit:  Z-Coordinate unit  
        :type zCoordinateUnit: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetZCoordinateUnit(self) -> BaseUnit:
        """
        Gets Z-Coordinate unit  
        
        Signature ``GetZCoordinateUnit()`` 
        
        :returns:  Z-Coordinate unit  
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetZCoordinatePoints(self, zCoordinatePoints: 'list[float]') -> None:
        """
        Sets Z-Coordinate points 
        
        Signature ``SetZCoordinatePoints(zCoordinatePoints)`` 
        
        :param zCoordinatePoints:  Z-Coordinate data  
        :type zCoordinatePoints: list of float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    Null: ArrayRecord3D = ...  # unknown typename


class DataManagerAfuRecordZValueMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DataManagerAfuRecordZValue():
    """
    Represents the method to get Z value for afu record in 3D plot 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SelectionOrder", "The Z value is selection order"
       "General", "The Z value is attribute of General field in an afu record"
       "Rpm", "The z value is attribute of RPM field in an afu record"
       "Time", "The z value is attribute of Time field in an afu record"
       "Order", "The z value is attribute of Order field in an afu record"
    """
    SelectionOrder = 0  # DataManagerAfuRecordZValueMemberType
    General = 1  # DataManagerAfuRecordZValueMemberType
    Rpm = 2  # DataManagerAfuRecordZValueMemberType
    Time = 3  # DataManagerAfuRecordZValueMemberType
    Order = 4  # DataManagerAfuRecordZValueMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DataManagerFileContainerTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DataManagerFileContainerType():
    """
    Represents the file container type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Not any container"
       "AssociatedContainer", "Part associated container which has the same simple name with the part"
       "ResultContainer", "Solution result container which has the same name with the solution"
       "UserContainer", "User container"
       "All", "All containers"
    """
    NotSet = 0  # DataManagerFileContainerTypeMemberType
    AssociatedContainer = 1  # DataManagerFileContainerTypeMemberType
    ResultContainer = 2  # DataManagerFileContainerTypeMemberType
    UserContainer = 3  # DataManagerFileContainerTypeMemberType
    All = 4  # DataManagerFileContainerTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DataManager():
    """
    Ftk data manager   
    
    To obtain an instance of this class use :py:meth:`NXOpen.Session.DataManager`.
    
    .. versionadded:: NX7.5.0
    """
    
    class AfuRecordZValue():
        """
        Represents the method to get Z value for afu record in 3D plot 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SelectionOrder", "The Z value is selection order"
           "General", "The Z value is attribute of General field in an afu record"
           "Rpm", "The z value is attribute of RPM field in an afu record"
           "Time", "The z value is attribute of Time field in an afu record"
           "Order", "The z value is attribute of Order field in an afu record"
        """
        SelectionOrder = 0  # DataManagerAfuRecordZValueMemberType
        General = 1  # DataManagerAfuRecordZValueMemberType
        Rpm = 2  # DataManagerAfuRecordZValueMemberType
        Time = 3  # DataManagerAfuRecordZValueMemberType
        Order = 4  # DataManagerAfuRecordZValueMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FileContainerType():
        """
        Represents the file container type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Not any container"
           "AssociatedContainer", "Part associated container which has the same simple name with the part"
           "ResultContainer", "Solution result container which has the same name with the solution"
           "UserContainer", "User container"
           "All", "All containers"
        """
        NotSet = 0  # DataManagerFileContainerTypeMemberType
        AssociatedContainer = 1  # DataManagerFileContainerTypeMemberType
        ResultContainer = 2  # DataManagerFileContainerTypeMemberType
        UserContainer = 3  # DataManagerFileContainerTypeMemberType
        All = 4  # DataManagerFileContainerTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    def LoadFile(self, fileName: str) -> None:
        """
        Loads afu/op2 file to User container
        
        Signature ``LoadFile(fileName)`` 
        
        :param fileName:  Afu/Op2 file name with full path  
        :type fileName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def LoadFile(self, fileName: str, containerType: DataManagerFileContainerType) -> None:
        """
        Loads an AFU/OP2 file to the specified container.
        
        An AFU/OP2 file can be loaded under associated container, solution result container or user container.
        The container type indicates under which container the file is loaded.
        
        Signature ``LoadFile(fileName, containerType)`` 
        
        :param fileName:  AFU/OP2 file name with full path  
        :type fileName: str 
        :param containerType: 
        :type containerType: :py:class:`NXOpen.CAE.FTK.DataManagerFileContainerType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def UnloadFile(self, fileName: str) -> None:
        """
        Unloads afu/op2 file from User container
        
        Signature ``UnloadFile(fileName)`` 
        
        :param fileName:  Afu/Op2 file name with full path  
        :type fileName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def UnloadFile(self, fileName: str, containerType: DataManagerFileContainerType) -> None:
        """
        Unloads an AFU/OP2 file from the specified container.
        
        An AFU/OP2 file can be loaded under associated container, solution result container or user container.
        The container type indicates under which container the file is unloaded.
        
        Signature ``UnloadFile(fileName, containerType)`` 
        
        :param fileName:  AFU/OP2 file name with full path  
        :type fileName: str 
        :param containerType: 
        :type containerType: :py:class:`NXOpen.CAE.FTK.DataManagerFileContainerType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteFile(self, fileName: str) -> None:
        """
        Deletes afu/op2 file 
        
        Signature ``DeleteFile(fileName)`` 
        
        :param fileName:  Afu/Op2 file name with full path  
        :type fileName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAfuRecord(self, afuFileName: str, recordName: str) -> BaseRecord:
        """
        Gets afu record  
        
        Signature ``GetAfuRecord(afuFileName, recordName)`` 
        
        :param afuFileName:  Afu file name with full path  
        :type afuFileName: str 
        :param recordName:  Afu record name  
        :type recordName: str 
        :returns:  Afu record data  
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOp2Record(self, op2FileName: str, dataSetName: str, recordName: str) -> BaseRecord:
        """
        Gets op2 record  
        
        Signature ``GetOp2Record(op2FileName, dataSetName, recordName)`` 
        
        :param op2FileName:  Op2 file name with full path  
        :type op2FileName: str 
        :param dataSetName:  Op2 data set name  
        :type dataSetName: str 
        :param recordName:  Op2 record name  
        :type recordName: str 
        :returns:  Op2 record data  
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateArrayRecord2d(self, titleName: str, legendName: str, numPoints: int) -> ArrayRecord2D:
        """
        Creates 2d array record  
        
        Signature ``CreateArrayRecord2d(titleName, legendName, numPoints)`` 
        
        :param titleName:  Title name  
        :type titleName: str 
        :param legendName:  Legend name  
        :type legendName: str 
        :param numPoints:  Point count  
        :type numPoints: int 
        :returns:  2D array record  
        :rtype: :py:class:`NXOpen.CAE.FTK.ArrayRecord2D` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateArrayRecord2dEvenSpacing(self, titleName: str, legendName: str) -> ArrayRecord2DEven:
        """
        Creates 2d array record with even spacing  
        
        Signature ``CreateArrayRecord2dEvenSpacing(titleName, legendName)`` 
        
        :param titleName:  Title name  
        :type titleName: str 
        :param legendName:  Legend name  
        :type legendName: str 
        :returns:  2D even array record  
        :rtype: :py:class:`NXOpen.CAE.FTK.ArrayRecord2DEven` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateArrayRecord3d(self, titleName: str, legendName: str, numPoints: int) -> ArrayRecord3D:
        """
        Creates 3d array record  
        
        Signature ``CreateArrayRecord3d(titleName, legendName, numPoints)`` 
        
        :param titleName:  Title name  
        :type titleName: str 
        :param legendName:  Legend name  
        :type legendName: str 
        :param numPoints:  Point count  
        :type numPoints: int 
        :returns:  3D array record  
        :rtype: :py:class:`NXOpen.CAE.FTK.ArrayRecord3D` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteRecord(self, deletedRecord: BaseRecord) -> None:
        """
        Deletes record 
        
        Signature ``DeleteRecord(deletedRecord)`` 
        
        :param deletedRecord:  Deleted record  
        :type deletedRecord: :py:class:`NXOpen.CAE.FTK.BaseRecord` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateArrayUnit(self, nxUnit: NXOpen.Unit, aliasMeasureName: str) -> BaseUnit:
        """
        Creates array unit by NX unit with new alias measure type name. 
        
        Please use the method :py:meth:`NXOpen.CAE.FTK.DataManager.CreateArrayUnit`` which has two parameters if the alias measure name is not needed
        
        Signature ``CreateArrayUnit(nxUnit, aliasMeasureName)`` 
        
        :param nxUnit:  NX unit  
        :type nxUnit: :py:class:`NXOpen.Unit` 
        :param aliasMeasureName:  alias measure name  
        :type aliasMeasureName: str 
        :returns:  Array unit  
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateArrayUnit(self, numeratorUnit: BaseUnit, denominatorUnit: BaseUnit) -> BaseUnit:
        """
        Creates array unit by numerator and denominator unit  
        
        Signature ``CreateArrayUnit(numeratorUnit, denominatorUnit)`` 
        
        :param numeratorUnit:  Numerator unit  
        :type numeratorUnit: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        :param denominatorUnit:  Denominator unit  
        :type denominatorUnit: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        :returns:  Array unit  
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateArrayRecordUnit(self, unitType: NXOpen.CAE.XyFunctionUnit) -> BaseUnit:
        """
        Creates an array record unit by xy function unit  
        
        Signature ``CreateArrayRecordUnit(unitType)`` 
        
        :param unitType:  Unit type  
        :type unitType: :py:class:`NXOpen.CAE.XyFunctionUnit` 
        :returns:  Array unit  
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX11.0.0
        
        .. deprecated::  NX12.0.0
           Use :py:meth:`NXOpen.CAE.FTK.DataManager.CreateArrayUnit`` instead.
        
        License requirements: None.
        """
        ...
    
    
    def CreateUnitlessUnit(self, unitName: str) -> BaseUnit:
        """
        Creates unitless unit 
        
        Signature ``CreateUnitlessUnit(unitName)`` 
        
        :param unitName:  Unit name  
        :type unitName: str 
        :returns:  Array unit  
        :rtype: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteArrayUnit(self, deletedUnit: BaseUnit) -> None:
        """
        Deletes array unit 
        
        Signature ``DeleteArrayUnit(deletedUnit)`` 
        
        :param deletedUnit:  Deleted unit  
        :type deletedUnit: :py:class:`NXOpen.CAE.FTK.BaseUnit` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateRealMatrixRecord(self, titleName: str, legendName: str) -> RealSectionBasedMatrixRecord:
        """
        Creates an empty real matrix record which section data is real data.  
        
        Signature ``CreateRealMatrixRecord(titleName, legendName)`` 
        
        :param titleName:  Title name  
        :type titleName: str 
        :param legendName:  Legend name  
        :type legendName: str 
        :returns:  Real matrix record  
        :rtype: :py:class:`NXOpen.CAE.FTK.RealSectionBasedMatrixRecord` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateComplexMatrixRecord(self, titleName: str, legendName: str) -> ComplexSectionBasedMatrixRecord:
        """
        Creates an empty complex matrix record which section data is complex data.  
        
        Signature ``CreateComplexMatrixRecord(titleName, legendName)`` 
        
        :param titleName:  Title name  
        :type titleName: str 
        :param legendName:  Legend name  
        :type legendName: str 
        :returns:  Complex matrix record  
        :rtype: :py:class:`NXOpen.CAE.FTK.ComplexSectionBasedMatrixRecord` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class ComplexSectionBasedMatrixRecord(SectionBasedMatrixRecord):
    """
    Represents a section based matrix record which has complex data values.  
    
    Not support KF.
    
    .. versionadded:: NX10.0.0
    """
    
    def AddSectionData(self, xCoordinatePoints: 'list[float]', yCoordinateReal: 'list[float]', yCoordinateImag: 'list[float]', zCoordinatePoint: float) -> None:
        """
        Adds the complex data values for each section.  
        
        Signature ``AddSectionData(xCoordinatePoints, yCoordinateReal, yCoordinateImag, zCoordinatePoint)`` 
        
        :param xCoordinatePoints:  X-Coordinate data  
        :type xCoordinatePoints: list of float 
        :param yCoordinateReal:  Real part of Y-Coordinate data  
        :type yCoordinateReal: list of float 
        :param yCoordinateImag:  Imaginary part of Y-Coordinate data  
        :type yCoordinateImag: list of float 
        :param zCoordinatePoint:  Z-Coordinate data  
        :type zCoordinatePoint: float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSectionData(self, sectionIndex: int) -> tuple:
        """
        Gets the complex data values from specific section.  
        
        Signature ``GetSectionData(sectionIndex)`` 
        
        :param sectionIndex:  Section index  
        :type sectionIndex: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (xCoordinatePoints, yCoordinateReal, yCoordinateImag, zCoordinatePoints). xCoordinatePoints is a list of float.   X-Coordinate data yCoordinateReal is a list of float.   Real part of Y-Coordinate data yCoordinateImag is a list of float.   Imaginary part of Y-Coordinate data zCoordinatePoints is a float.   Z-Coordinate data 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ComplexSectionBasedMatrixRecord = ...  # unknown typename


class IApplicationData():
    """
    Represents the interface for  application specific data class  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier
    
    def __repr__(self) -> None:
        """Return repr(self)."""
        ...
    
    
    def __hash__(self) -> None:
        """Return hash(self)."""
        ...
    
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    
    def __getattribute__(self) -> None:
        """Return getattr(self, name)."""
        ...
    
    
    def __setattr__(self) -> None:
        """Implement setattr(self, name, value)."""
        ...
    
    
    def __delattr__(self) -> None:
        """Implement delattr(self, name)."""
        ...
    
    
    def __lt__(self) -> None:
        """Return self<value."""
        ...
    
    
    def __le__(self) -> None:
        """Return self<=value."""
        ...
    
    
    def __eq__(self) -> None:
        """Return self==value."""
        ...
    
    
    def __ne__(self) -> None:
        """Return self!=value."""
        ...
    
    
    def __gt__(self) -> None:
        """Return self>value."""
        ...
    
    
    def __ge__(self) -> None:
        """Return self>=value."""
        ...
    


class OptionSetting():
    """
    Manager the options data for AFU Data Record   
    
    Not support KF.
    
    .. versionadded:: NX6.0.0
    """
    
    def GetRecordOptionData(self) -> tuple:
        """
        Get the record options data for an AFU Data Record 
        
        Signature ``GetRecordOptionData()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (recordName, functionType, abscissaType, xUnit, ordinateType, yUnit, yDenominatorUnit, sortValueType). recordName is a str.   The name of the AFU Data Record functionType is a :py:class:`NXOpen.CAE.XyFunctionGeneralType`.   Usage type of AFU Data Record used abscissaType is a :py:class:`NXOpen.CAE.AfuDataAbscissaType`.   Abscissa specific data type xUnit is a :py:class:`NXOpen.CAE.XyFunctionUnit`.   Unit Code of AFU data ordinateType is a :py:class:`NXOpen.CAE.AfuDataOrdinateType`.   Ordinate data type yUnit is a :py:class:`NXOpen.CAE.XyFunctionUnit`.   Ordinate Numerator Unit Code of AFU data yDenominatorUnit is a :py:class:`NXOpen.CAE.XyFunctionUnit`.   Ordinate Denominator Unit Code of AFU data sortValueType is a bool.   If want to sort value in x direction 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRecordOptionData(self, recordName: str, functionType: NXOpen.CAE.XyFunctionGeneralType, abscissaType: NXOpen.CAE.AfuDataAbscissaType, xUnit: NXOpen.CAE.XyFunctionUnit, ordinateType: NXOpen.CAE.AfuDataOrdinateType, yUnit: NXOpen.CAE.XyFunctionUnit, yDenominatorUnit: NXOpen.CAE.XyFunctionUnit, sortValueType: bool) -> None:
        """
        Set the record options data for an AFU Data Record 
        
        Signature ``SetRecordOptionData(recordName, functionType, abscissaType, xUnit, ordinateType, yUnit, yDenominatorUnit, sortValueType)`` 
        
        :param recordName:  The name of the AFU Data Record  
        :type recordName: str 
        :param functionType:  Usage type of AFU Data Record used  
        :type functionType: :py:class:`NXOpen.CAE.XyFunctionGeneralType` 
        :param abscissaType:  Abscissa specific data type  
        :type abscissaType: :py:class:`NXOpen.CAE.AfuDataAbscissaType` 
        :param xUnit:  Unit Code of AFU data  
        :type xUnit: :py:class:`NXOpen.CAE.XyFunctionUnit` 
        :param ordinateType:  Ordinate data type  
        :type ordinateType: :py:class:`NXOpen.CAE.AfuDataOrdinateType` 
        :param yUnit:  Unit Code of AFU data  
        :type yUnit: :py:class:`NXOpen.CAE.XyFunctionUnit` 
        :param yDenominatorUnit:  Unit Code of AFU data  
        :type yDenominatorUnit: :py:class:`NXOpen.CAE.XyFunctionUnit` 
        :param sortValueType:  If want to sort value in x direction  
        :type sortValueType: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetHeaderFlag(self) -> bool:
        """
        Get the adding header flag when export to CSV file  
        
        Signature ``GetHeaderFlag()`` 
        
        :returns:  If want to add header when export to CSV file  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetHeaderFlag(self, addHeader: bool) -> None:
        """
        Set the adding header flag when export to CSV file 
        
        Signature ``SetHeaderFlag(addHeader)`` 
        
        :param addHeader:  If want to add header when export to CSV file  
        :type addHeader: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    


class FTKManager():
    """
    FTK function data manager   
    
    To obtain an instance of this class use :py:meth:`NXOpen.Session.FTKManager`.
    
    .. versionadded:: NX6.0.0
    """
    OptionSetting: OptionSetting = ...
    """
    Returns the :py:class:`NXOpen.CAE.FTK.OptionSetting` belonging to this session 
    
    Signature ``OptionSetting`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.FTK.OptionSetting`
    """


