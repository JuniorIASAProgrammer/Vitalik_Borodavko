class product_grid_contain(object):
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)  # Finding the referenced element
        product_names = list(map(lambda x: x.accessible_name, elements))
        if self.name in product_names:
            return elements
        else:
            return False
