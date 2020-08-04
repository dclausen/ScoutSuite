import abc

from ScoutSuite.providers.base.resources.base import Resources, CompositeResources

class BambooHRResources(Resources, metaclass=abc.ABCMeta):
   """This is the base class for BambooHR resources."""

   pass

class BambooHRCompositeResources(BambooHRResources, CompositeResources, metaclass=abc.ABCMeta):

   pass
