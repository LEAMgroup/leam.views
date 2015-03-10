from zope.interface import implements, Interface

from Products.Five import BrowserView
from plone import api

from leam.views import viewsMessageFactory as _


class IProjectionListingView(Interface):
    """
    ProjectionListing view interface
    """


class ProjectionListingView(BrowserView):
    """
    ProjectionListing browser view
    """
    implements(IProjectionListingView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def projections(self):
        """ returns a list of pre-processed projections """
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())

        brains = portal_catalog(portal_type='Projection', path=current_path)
        for b in brains:
            p = b.getObject()
            results.append({
                'title': b.Title,
                'description': b.Description,
                'url': b.getURL(),
                'author': 'steve',
                'modified': '15-Feb-2014',
                'endpop': '100,000',
                'endemp': '55,000',
                'uuid': b.UID,
                })
            return results

    def test(self):
        """
        test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}
