from playwright.sync_api import expect, Page

example = {"a": 1, "b": 2, "c": 3}

for i in example:
    print(i)



def test_temp(page: Page):
    res = page.get_by_test_id("dasdas")
    expect(res).to_have_count(3)