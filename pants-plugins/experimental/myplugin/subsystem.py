from pants.option.subsystem import Subsystem

class MyPlugin(Subsystem):
    options_scope = "myplugin"
    help = ("An example subsystem that does nothing.",)
