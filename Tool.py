from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium import webdriver
from os import system
import pyfiglet
import time
import os

videoIndex = 0
windowIndex = 0
windowCount = 1
viewCount = 0

if __name__ == "__main__":

    system("cls")
    os.system("title Youtube Buff | QueenTech")

    print(f"""{pyfiglet.figlet_format("Tool | QueenTech", font="slant")}""")

    tab = int(input("\tNhập số tab: "))

    url = str(input("\tNhập link video: "))

    edge_options = EdgeOptions()
    edge_options.add_argument("--mute-audio")

    driver = Edge(
        executable_path=r"msedgedriver.exe", options=edge_options)
    driver.set_window_size(1024, 650)

    while True:
        windowIndex = (windowIndex + 1) % tab

        if windowCount < tab:
            windowCount += 1
            driver.execute_script(f"window.open('{url}')")
        else:
            driver.switch_to.window(driver.window_handles[windowIndex])
            time.sleep(0.5)
            driver.get(url)
            driver.find_element_by_css_selector(
                "#movie_player > div.ytp-cued-thumbnail-overlay > button").click()
        viewCount += 1

        print(f"[+1] | {viewCount}")

        time.sleep(5)
