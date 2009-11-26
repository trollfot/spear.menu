# -*- coding: utf-8 -*-

"""IAdding in plone is not traversable. We needed to reimplement the view
in order to get it grokked and also have a controlable traversing. Note that
it's a personal choice not to override the '+' view, in order to keep Spear 
as transparent as possible.
"""

from five import grok
from OFS.SimpleItem import SimpleItem
from Products.Five.browser.adding import BasicAdding
from Products.CMFCore.interfaces import IFolderish
from Globals import InitializeClass
from AccessControl import ClassSecurityInfo

from zope.interface import implements
from zope.publisher import interfaces as zp
from zope.app.container.interfaces import IAdding


class SpearAddingView(SimpleItem, BasicAdding, grok.MultiAdapter):
    grok.name('+spear')
    grok.adapts(IFolderish, zp.http.IHTTPRequest)
    grok.provides(IAdding)
    grok.require("zope2.View")

    security = ClassSecurityInfo()

    def publishTraverse(self, request, name):
        # We authorize the access to emptypage. We need this because
        # BasicAdding inherit from BrowserView which forbides it.
        if name in ['emptypage',]:
            return getattr(self.aq_base, name)
        return super(SpearAddingView, self).publishTraverse(request, name)

    security.declarePublic('Title')
    def Title(self):
        return u"Add a new content"

    security.declarePublic('emptypage')
    def emptypage(self):
        """Return an empty page for Kupu.
        """
        return self.context.emptypage()

    id = '+spear'
    contentName = None

InitializeClass(SpearAddingView)
