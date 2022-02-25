from experimental.myplugin.rules import rules as myplugin_rules
# from experimental.myplugin.target_types import MyPluginTarget


def rules():
    return [*myplugin_rules()]


# def target_types():
#     return [MyPluginTarget]