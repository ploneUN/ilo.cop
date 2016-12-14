from five import grok
from plone.directives import dexterity, form
from ilo.cop.content.cop import ICOP
from Products.CMFCore.utils import getToolByName

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ICOP)
    grok.require('zope2.View')
    grok.template('cop_view')
    grok.name('view')

    @property
    def catalog(self):
    	return getToolByName(self.context, 'portal_catalog')

    def contents(self):
        context = self.context
        catalog = self.catalog
        path = '/'.join(context.getPhysicalPath())
        results = []
        brains = catalog.searchResults(path={'query': path, 'depth':1},portal_type='ilo.cop.copitem',sort_on='created', sort_order='reverse')[:5]
        
        return brains
        

    def searchedValue(self, name=None):
        result = 0
        if self.request.form.has_key(name):
            form = self.request.form
            result = form[name]
        return result
    
    def highlight_news(self):
        context = self.context
        catalog = self.catalog
        path = '/'.join(context.getPhysicalPath())
        brains = catalog.unrestrictedSearchResults(path={'query':path, 'depth':5}, portal_type='News Item', Subject=('highlight',), sort_order='reverse', sort_on='created', review_state='shared_intranet')
        if brains:
            return brains[0]
        return []
    
    def news(self):
        context = self.context
        catalog = self.catalog
        path = '/'.join(context.getPhysicalPath())
        results = []
        brains = catalog.unrestrictedSearchResults(path={'query':path, 'depth':5}, portal_type='News Item', sort_order='reverse', sort_on='created', review_state='shared_intranet')
        for brain in brains or []:
            if 'highlight' not in brain.Subject:
                if len(results) < 3:
                    results.append({'title':brain.Title, 'desc':brain.Description, 'img':brain.getObject().getImage(), 'url':brain.getPath()})
                else:
                    break
                        
        return results
    
    def publications(self):
        context = self.context
        catalog = self.catalog
        path = '/'.join(context.getPhysicalPath())
        brains = catalog.unrestrictedSearchResults(path={'query':path, 'depth':5}, portal_type='File', sort_order='reverse', sort_on='created', review_state='shared_intranet')
        results = []
        for brain in brains:
            if 'publication' in brain.Subject:
                if len(results) < 3:
                    results.append(brain)
                else:
                    break
        return results
                
                
    
