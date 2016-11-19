from five import grok
from zope.formlib import form
from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.portlets.portlets import base
from plone.app.portlets import PloneMessageFactory as _

class IContentNavigation(IPortletDataProvider):
    
    portlet_header_title = schema.TextLine(
        title = _(u"Portlet Header Title"),
        required = True,
    )
    

class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    def __init__(self, portlet_header_title=None):
        self.portlet_header_title = portlet_header_title

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('templates/discussion_brief_attachment_portlet.pt')
    
    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        
    
    def data(self):
        return self.data
    
    def contents(self):
        context = self.context
        brains = context.portal_catalog.unrestrictedSearchResults(path={'query':'/'.join(context.getPhysicalPath()), 'depth':1}, portal_type='ilo.cop.copitem')
        return brains


class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Add Discussion Brief Attachment Portlet"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment
    

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Edit Discussion Brief Attachment Portlet"
    description = ''