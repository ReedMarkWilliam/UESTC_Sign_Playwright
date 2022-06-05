import time

from playwright.sync_api import sync_playwright
import sys
userName = sys.argv[1]
userID = sys.argv[2]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://jinshuju.net/f/kDiOo6")
        page.pause()
        # Click input[name="field_1"]
        page.locator("input[name=\"field_1\"]").click()
        page.locator("input[name=\"field_1\"]").fill(userName)
        # Click input[name="field_2"]
        page.locator("input[name=\"field_2\"]").click()
        # Fill input[name="field_2"]
        page.locator("input[name=\"field_2\"]").fill(userID)
        # Check input[name="field_3"] >> nth=0
        page.locator("input[name=\"field_3\"]").first.check()
        # Check input[name="field_6"] >> nth=0
        page.locator("input[name=\"field_6\"]").first.check()
        # Check input[name="field_4"] >> nth=0
        page.locator("input[name=\"field_4\"]").first.check()
        # Check input[name="field_7"] >> nth=0
        page.locator("input[name=\"field_7\"]").first.check()
        # Click button:has-text("获取地理位置")
        page.locator("button:has-text(\"获取地理位置\")").click()
        # Click [placeholder="请输入要搜索的地点"]
        page.locator("[placeholder=\"请输入要搜索的地点\"]").click()
        page.locator("[placeholder=\"请输入要搜索的地点\"]").fill("电子科技大学清水河校区")
        time.sleep(2)
        # Click button >> nth=2
        page.locator("button").nth(2).click()
        # Check input[name="field_21"] >> nth=1
        page.locator("input[name=\"field_21\"]").nth(1).check()
        # Click button:has-text("提 交")
        page.locator("button:has-text(\"提 交\")").click()
        print(userName + "Successfully sign")
        browser.close()

if __name__ == "__main__":
    main()