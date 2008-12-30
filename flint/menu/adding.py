# -*- coding: utf-8 -*-

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
