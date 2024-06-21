def classFactory(iface):
    from .qrefactor_plugin import QRefactorPlugin
    return QRefactorPlugin(iface)
