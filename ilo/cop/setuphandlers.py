from collective.grok import gs
from ilo.cop import MessageFactory as _

@gs.importstep(
    name=u'ilo.cop', 
    title=_('ilo.cop import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ilo.cop.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
