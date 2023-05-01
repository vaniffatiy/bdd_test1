from bdd_test1.src.pages.drag_page import DragPage


class TestDynamic:

    def test_drag_drop(self, webdriver_handler):
        drag = DragPage(webdriver_handler)
        drag.open_site()
        drag.drag_drop()
        drag.drag_drop_offset()










