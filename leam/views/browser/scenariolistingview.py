from zope.interface import implements, Interface
from Products.Five import BrowserView
from plone import api

from leam.views import viewsMessageFactory as _
from leam.luc.interfaces import ILUCScenario


class IScenarioListingView(Interface):
    """
    ScenarioListing view interface
    """


class ScenarioListingView(BrowserView):
    """
    ScenarioListing browser view
    """
    implements(IScenarioListingView)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.catalog = api.portal.get_tool(name='portal_catalog')

    def history(self):
        return '0, 10, 55'

    def running(self, limit=10):   
        """
        Provide list of brains for running Scenarios
        @param limit: max number to return
        """

        listing = self.catalog(
                object_provides=ILUCScenario.__identifier__,
                review_state='running',
                sort_on='modified', sort_order='descending')
        return listing

    def queued(self, limit=10):   
        """
        Provide list of brains for queued Scenarios
        @param limit: max number to return
        """

        listing = self.catalog(
                object_provides=ILUCScenario.__identifier__,
                review_state='queued',
                sort_on='modified', sort_order='decending')
        return listing

    def failed(self, limit=10):   
        """
        Provide list of brains for failed Scenarios
        @param limit: max number to return
        """

        listing = self.catalog(
                object_provides=ILUCScenario.__identifier__,
                review_state='failed',
                sort_on='modified', sort_order='descending')
        return listing

    def finished(self, limit=10):   
        """
        Provide list of brains for finished, reviewed, or published Scenarios
        @param limit: max number to return
        """

        listing = self.catalog(
                object_provides=ILUCScenario.__identifier__,
                review_state=('finished', 'reviewed', 'published'),
                sort_on='modified', sort_order='descending')
        return listing

    def scenarios(self, state, limit=10):   
        """
        Provide list of finished Scenarios' metadata
        @param state: desired worflow states
        @param limit: max number to return
        """

        listing = self.catalog(
                object_provides=ILUCScenario.__identifier__,
                review_state=state,
                sort_limit=limit, sort_on='modified', sort_order='descending')
        return listing

