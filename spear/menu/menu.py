# -*- coding: utf-8 -*-

from five import grok
from urllib import quote_plus
from Acquisition import aq_inner
from zope.i18n import translate
from zope.interface import Interface
from zope.component import getMultiAdapter, queryMultiAdapter, queryUtility
from spear.content.interfaces import IFactory
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.app.content.browser import folderfactories as plone
from plone.app import contentmenu as plone_menu 


class SpearMenu(plone_menu.menu.FactoriesSubMenuItem, grok.MultiAdapter):
    grok.adapts(Interface, Interface)
    grok.name("plone.contentmenu.factories")
    grok.provides(plone_menu.interfaces.IContentMenuItem)
    
    @property
    def action(self):
        addContext = self._addContext()
        if self._hideChildren():
            (addContext, fti) = self._itemsToAdd()[0]
            baseUrl = addContext.absolute_url()
            addingview = queryMultiAdapter((addContext,
                                            self.request), name='+')
            if addingview is not None and not fti.product:
                addview = queryMultiAdapter((addingview, self.request),
                                            name=fti.factory)
                if addview is not None:
                    return '%s/+/%s' % (baseUrl, fti.factory,)
                else:
                    workshop = queryUtility(IFactory, fti.factory)
                    url = (workshop and
                           "%s/+spear/spear.add=%s" % (baseUrl, fti.factory)
                           or None)
                    if url is not None:
                        return url
                
            return ('%s/createObject?type_name=%s' %
                    (baseUrl, quote_plus(fti.getId())))
        else:
            return ('%s/folder_factories' %
                    self.context_state.folder().absolute_url())


class SpearFactories(plone.FolderFactoriesView):

    def addable_types(self, include=None):
        context = aq_inner(self.context)
        request = self.request
        results = []
        
        portal_state = getMultiAdapter((context, request),
                                       name='plone_portal_state')
        portal_url = portal_state.portal_url()
        addContext = self.add_context()
        baseUrl = addContext.absolute_url()
        
        allowedTypes = plone._allowedTypes(request, addContext)
        exclude = addContext.getNotAddableTypes()

        addingview = queryMultiAdapter((addContext, request), name='+')
        idnormalizer = queryUtility(IIDNormalizer)
        for t in allowedTypes:
            url = None
            typeId = t.getId()
            if typeId not in exclude and (include is None or typeId in include):
                cssId = idnormalizer.normalize(typeId)
                cssClass = 'contenttype-%s' % cssId
                factory_name = t.factory
                if addingview is not None and not t.product:
                    factory = queryMultiAdapter((addingview, self.request),
                                                name=factory_name)
                    if factory is not None:
                        url = "+/%s" % factory_name
                    else:
                        workshop = queryUtility(IFactory, factory_name)
                        url = (workshop and
                               "+spear/spear.add=%s" % factory_name or None)

                if url is None:
                    url = 'createObject?type_name=%s' % quote_plus(typeId)

                icon = t.getIcon()
                if icon:
                    icon = '%s/%s' % (portal_url, icon)

                results.append({ 'id'           : typeId,
                                 'title'        : t.Title(),
                                 'description'  : t.Description(),
                                 'action'       : "%s/%s" % (baseUrl, url),
                                 'selected'     : False,
                                 'icon'         : icon,
                                 'extra'        : {'id' : cssId,
                                                   'separator' : None,
                                                   'class' : cssClass},
                                 'submenu'      : None,
                                })

        # Sort the addable content types based on their translated title
        results = [(translate(ctype['title'], context=request), ctype)
                   for ctype in results]
        results.sort()
        results = [ctype[-1] for ctype in results]

        return results
