from five import grok
from plone.directives import dexterity, form
from ilo.cop.content.cop_item import ICOPItem

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ICOPItem)
    grok.require('zope2.View')
    grok.template('cop_item_view')
    grok.name('view')

