from collective.grok import gs
from sinarngo.partner import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.partner', 
    title=_('sinarngo.partner import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.partner.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
