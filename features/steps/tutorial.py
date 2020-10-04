from behave import *

@given('behave instalado')
def step_impl(context):
    pass

@when('implenta-se um teste')
def step_impl(context):
    assert True is not False

@then('behave conseguirá testar')
def step_impl(context):
    assert context.failed is False