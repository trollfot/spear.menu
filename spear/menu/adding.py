# -*- coding: utf-8 -*-

"""IAdding in plone is not traversable. We needed to reimplement the view
in order to get it grokked and also have a controlable traversing. Note that
it's a personal choice not to override the "+" name, in order to keep the
flint us as transparent as possible.
"""

from five import grok
from OFS.SimpleItem import SimpleItem
from Products.Five.browser.adding import BasicAdding
from Products.CMFCore.interfaces import IFolderish

from zope.interface import implements
from zope.publisher import interfaces as zp
from zope.app.container.interfaces import IAdding


class FlintCarver(SimpleItem, BasicAdding, grok.MultiAdapter):
    grok.name('+flint')
    grok.adapts(IFolderish, zp.http.IHTTPRequest)
    grok.provides(IAdding)
    grok.require("zope2.View")

    id = '+flint'
    contentName = None
    
    def nextURL(self):
        return "%s/%s/view" % (self.context.absolute_url(), self.contentName)
