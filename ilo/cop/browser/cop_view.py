from five import grok
from plone.directives import dexterity, form
from ilo.cop.content.cop import ICOP

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ICOP)
    grok.require('zope2.View')
    grok.template('cop_view')
    grok.name('view')

