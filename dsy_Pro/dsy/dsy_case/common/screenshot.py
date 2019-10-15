import sys
from selenium import webdriver


def screen_image(driver, filename):
    base_dir = sys.path[0]
    # F:\python_project\dsy_Pro\dsy\dsy_case\common\screenshot.py
    # base_dir = str(base_dir)
    # base_dir = base_dir.replace('\\', '/')
    base = base_dir.split("\\dsy_case")[0]
    image_dir = base + "\\report\\image\\" + filename + ".png"
    # F:\python_project\dsy_Pro\dsy\report\image\filename.png
    # print(image_dir)
    driver.get_screenshot_as_file(image_dir)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://dsy.10333.com/")
    driver.set_window_size(1200, 700)
    screen_image(driver, 'test')
    driver.quit()
