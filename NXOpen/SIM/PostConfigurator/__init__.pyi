# module 'NXOpen.SIM.PostConfigurator'
#
# Automatically generated 2025-06-09T14:38:47.488405
#

import typing

import NXOpen



class PostConfiguratorManager():
    """
    Represents Post Configurator Manager  
    
    Use :py:meth:`NXOpen.Session.PostConfiguratorManager` to get the instance of this class.
    
    .. versionadded:: NX10.0.3
    """
    
    def CreateCreationPostBuilder(self) -> CreationPostBuilder:
        """
        Creates a :py:class:`NXOpen.SIM.PostConfigurator.CreationPostBuilder` object  
        
        Signature ``CreateCreationPostBuilder()`` 
        
        :returns:  The new creation post builder  
        :rtype: :py:class:`NXOpen.SIM.PostConfigurator.CreationPostBuilder` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
        """
        ...
    
    
    def CreatePostConfiguratorBuilder(self, postProcessorFilename: str) -> PostConfiguratorBuilder:
        """
        Creates a :py:class:`NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder` object  
        
        Signature ``CreatePostConfiguratorBuilder(postProcessorFilename)`` 
        
        :param postProcessorFilename:  the post processor filename  
        :type postProcessorFilename: str 
        :returns:  The new post configurator builder  
        :rtype: :py:class:`NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
        """
        ...
    


class CreationPostBuilder(NXOpen.Builder):
    """
    This class is used to create a new postprocessor.  
    
    Calling :py:meth:`Builder.Commit` on this builder will only return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.PostConfigurator.PostConfiguratorManager.CreateCreationPostBuilder`
    
    .. versionadded:: NX10.0.3
    """
    
    def GetControllerNames(self) -> 'list[str]':
        """
        Returns the list of Controller Names in the postprocessor.  
        
        Signature ``GetControllerNames()`` 
        
        :returns:  the list of available controller  
        :rtype: list of str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetManufacturerNames(self) -> 'list[str]':
        """
        Returns the list of Manufacturer Names in the postprocessor.  
        
        Signature ``GetManufacturerNames()`` 
        
        :returns:  the list of available manufacturer  
        :rtype: list of str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetMachineNames(self) -> 'list[str]':
        """
        Returns the list of Machine Names in the postprocessor.  
        
        Signature ``GetMachineNames()`` 
        
        :returns:  the list of available machine  
        :rtype: list of str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    ControllerName: str = ...
    """
    Returns or sets  the controller's name that is used for the postprocessor.  
    
    <hr>
    
    Getter Method
    
    Signature ``ControllerName`` 
    
    :returns:  The controller's name  
    :rtype: str 
    
    .. versionadded:: NX10.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ControllerName`` 
    
    :param name:  the controller's new name  
    :type name: str 
    
    .. versionadded:: NX10.0.3
    
    License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    """
    MachineName: str = ...
    """
    Returns or sets  the machine's name that is used for the postprocessor.  
    
    <hr>
    
    Getter Method
    
    Signature ``MachineName`` 
    
    :returns:  The machine's name  
    :rtype: str 
    
    .. versionadded:: NX10.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MachineName`` 
    
    :param name:  the machine's new name  
    :type name: str 
    
    .. versionadded:: NX10.0.3
    
    License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    """
    ManufacturerName: str = ...
    """
    Returns or sets  the manufacturer's name that is used for the postprocessor.  
    
    <hr>
    
    Getter Method
    
    Signature ``ManufacturerName`` 
    
    :returns:  The manufacturer's name  
    :rtype: str 
    
    .. versionadded:: NX10.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ManufacturerName`` 
    
    :param name:  the manufacturer's new name  
    :type name: str 
    
    .. versionadded:: NX10.0.3
    
    License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    """
    PostprocessorName: str = ...
    """
    Returns or sets  the postprocessor's name.  
    
    <hr>
    
    Getter Method
    
    Signature ``PostprocessorName`` 
    
    :returns:  The postprocessor's name  
    :rtype: str 
    
    .. versionadded:: NX10.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PostprocessorName`` 
    
    :param name:  the postprocessor's new name  
    :type name: str 
    
    .. versionadded:: NX10.0.3
    
    License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    """
    PostprocessorOutputDirectory: str = ...
    """
    Returns or sets  the postprocessor's output directory where the postprocessor is created.  
    
    <hr>
    
    Getter Method
    
    Signature ``PostprocessorOutputDirectory`` 
    
    :returns:  The postprocessor's output directory  
    :rtype: str 
    
    .. versionadded:: NX10.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PostprocessorOutputDirectory`` 
    
    :param outputDirectory:  the postprocessor's new output directory  
    :type outputDirectory: str 
    
    .. versionadded:: NX10.0.3
    
    License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    """
    Null: CreationPostBuilder = ...  # unknown typename


class PostConfiguratorBuilder(NXOpen.Builder):
    """
    This class is used to create a post configurator builder.  
    
    Calling :py:meth:`Builder.Commit` on this builder will only return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.PostConfigurator.PostConfiguratorManager.CreatePostConfiguratorBuilder`
    
    .. versionadded:: NX10.0.3
    """
    
    def Reset(self) -> None:
        """
        Resets the post configurator data.  
        
        Signature ``Reset()`` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
        """
        ...
    
    
    def ShowChanges(self) -> None:
        """
        Shows the post configurator data changes in the listing window.  
        
        Signature ``ShowChanges()`` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
        """
        ...
    
    
    def EncryptPostConfiguratorFiles(self, soldToID: str, expirationDate: str) -> None:
        """
        Encrypts a post processor with Sold-To ID and expiration date.  
        
        Signature ``EncryptPostConfiguratorFiles(soldToID, expirationDate)`` 
        
        :param soldToID:  the sold to id  
        :type soldToID: str 
        :param expirationDate:  the expiration date  
        :type expirationDate: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
        """
        ...
    
    
    def SaveAs(self, postprocessorName: str, outputDirectory: str) -> None:
        """
        Saves the post configurator data in different name.  
        
        Signature ``SaveAs(postprocessorName, outputDirectory)`` 
        
        :param postprocessorName:  the postprocessor name  
        :type postprocessorName: str 
        :param outputDirectory:  the output directory  
        :type outputDirectory: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
        """
        ...
    
    DateValue: NXOpen.DateBuilder = ...
    """
    Returns  the date value.  
    
    The Date object will contain the value for expiration date. 
    
    <hr>
    
    Getter Method
    
    Signature ``DateValue`` 
    
    :returns:  the date value  
    :rtype: :py:class:`NXOpen.DateBuilder` 
    
    .. versionadded:: NX10.0.3
    
    License requirements: None.
    """
    Null: PostConfiguratorBuilder = ...  # unknown typename


