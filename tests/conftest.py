import shutil

import pytest

from pyoracle_forms import Module, Item, DataBlock, Canvas, Window, initialize_context


@pytest.fixture(scope="session")
def context():
    initialize_context()


@pytest.fixture(scope="session")
def module(context):
    with Module.load(path="./tests/test_modules/simple_module.fmb") as module:
        yield module


@pytest.fixture(scope="session")
def data_block(module):
    return module.data_blocks[0]


@pytest.fixture(scope="session")
def item(data_block):
    return data_block.items[0]


@pytest.fixture(scope="session")
def canvas(module):
    return module.canvases[0]


@pytest.fixture(scope="session")
def test_dir(tmpdir_factory):
    test_directory = tmpdir_factory.mktemp("forms")
    yield test_directory
    shutil.rmtree(test_directory)


@pytest.fixture(scope="function")
def new_module(context):
    with Module.create(module_name="new_module") as module:
        yield module


@pytest.fixture(scope="function")
def make_item():
    def _make_item(new_data_block, name):
        return Item.create(new_data_block, name)

    return _make_item


@pytest.fixture(scope="function")
def make_data_block(new_module):
    def _make_data_block(name):
        return DataBlock.create(new_module, name)

    return _make_data_block


@pytest.fixture(scope="function")
def make_canvas(new_module):
    def _make_canvas(name):
        return Canvas.create(new_module, name)

    return _make_canvas


@pytest.fixture(scope="function")
def make_window(new_module):
    def _make_window(name):
        return Window.create(new_module, name)

    return _make_window


@pytest.fixture(scope="function")
def new_canvas(make_canvas):
    return make_canvas("CNV")


@pytest.fixture(scope="function")
def new_data_block(make_data_block):
    return make_data_block("BLK")


@pytest.fixture(scope="function")
def new_item(new_data_block, make_item):
    return make_item(new_data_block, "ITM")
