from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.formwidget.multifile import MultiFileFieldWidget

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer
from plone.autoform.directives import write_permission, read_permission
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from ilo.cop import MessageFactory as _


# Interface class; used to define content-type schema.

class ICOPItem(form.Schema, IImageScaleTraversable):
    """
    COP Item
    """
    form.widget(blog_body=WysiwygFieldWidget)
    blog_body = schema.Text(title=u"Body")

    write_permission(multifile='cmf.ReviewPortalContent')
    read_permission(multifile='cmf.ReviewPortalContent')
    form.widget(multifile=MultiFileFieldWidget)
    multifile = schema.List(
            title=_(u"File Attachment"),
            required=False,
            value_type=NamedFile(),
        )

    discussion_brief = NamedBlobFile(
            title=_(u"Discussion Brief"),
            description=_(u"Please attach a file"),
            required=False,
        )

    pass

alsoProvides(ICOPItem, IFormFieldProvider)
