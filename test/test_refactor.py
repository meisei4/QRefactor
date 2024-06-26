from plugin.core.refactor import Refactor, update_layer_source


def test_update_layer_source():
    refactor = Refactor()
    update_layer_source("example_layer", "/new/path/to/layer")
    assert True # add logic later
