import abc

from ScoutSuite.providers.base.resources.base import Resources, CompositeResources

class GsuiteResources(Resources, metaclass=abc.ABCMeta):
   """This is the base class for Gsuite resources."""

   pass

class GsuiteCompositeResources(GsuiteResources, CompositeResources, metaclass=abc.ABCMeta):

   pass