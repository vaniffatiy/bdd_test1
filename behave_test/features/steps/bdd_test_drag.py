# from behave import given, then
# from UI_tests.src.pages.drag_page import DragPage
#
#
# @given(u"we have the website opened")
# def step_open_website(context):
#     assert hasattr(context, "webdriver_handler"), "Driver not found in context"
#     context.drag = DragPage(context.webdriver_handler)
#     context.drag.open_site()
#
#
# @then(u'we activate "drag and drop" function both source_to_target and by offset')
# def step_drag_and_drop(context):
#     context.drag.drag_drop()
#
#
# def step_drag_and_drop_offset(context):
#     context.drag.drag_drop_offset()
#
#
#
#
# # @then(u"we confirm that the functions work well")
# # def step_confirm_results(context):
# #     assert context.drag.verify_drag_drop_success(), "Drag and drop failed"
# #     assert context.drag.verify_drag_drop_offset_success(), "Drag and drop by offset failed"
