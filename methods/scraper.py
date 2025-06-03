from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re
import swifter

def scrape_courses():
    """
    This function scrapes course data from the KUCourses website and processes it into a cleaned DataFrame, and adds it to a csv file.
    """
    firefox_options = Options()
    #firefox_options.add_argument('--headless')
    firefox_options.add_argument('--disable-gpu')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--disable-dev-shm-usage')
    url = 'https://kucourses.dk'

    browser = webdriver.Firefox(options=firefox_options)
    browser.get(url)

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".w-full")))

    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            wait.until(lambda d: d.execute_script("return document.body.scrollHeight") > last_height)
            last_height = browser.execute_script("return document.body.scrollHeight")
        except:
            break

    boxes = browser.find_elements(By.XPATH, "/html/body/div/div[1]/div/div/main/div[4]/div/a")

    courses = []
    i = 0
    for box in boxes:
        title = box.find_element(By.XPATH, ".//div[1]/div[1]/div[1]/h1").text
        course_id = box.find_element(By.XPATH, ".//div[1]/div[1]/div[1]/h2").text
        level = box.find_element(By.XPATH, ".//div[1]/div[1]/table/tbody/tr[1]/td[1]").text
        length = box.find_element(By.XPATH, ".//div[1]/div[1]/table/tbody/tr[1]/td[2]").text
        timeslot = box.find_element(By.XPATH, ".//div[1]/div[1]/table/tbody/tr[2]/td[1]").text
        group = box.find_element(By.XPATH, ".//div[1]/div[1]/table/tbody/tr[2]/td[2]").text
        description = box.find_element(By.XPATH, ".//div[1]/p").text
        exam_type = box.find_element(By.XPATH, ".//div[2]/div[1]").text
        pass_pct = box.find_element(By.XPATH, ".//div[2]/table/tbody/tr[1]").text
        median = box.find_element(By.XPATH, ".//div[2]/table/tbody/tr[2]").text
        mean = box.find_element(By.XPATH, ".//div[2]/table/tbody/tr[3]").text
        courses.append({
            'course_id': course_id,
            'title': title,
            'level': level,
            'length': length,
            'timeslot': timeslot,
            'group': group,
            'description': description,
            'exam_type': exam_type,
            'pass_pct': pass_pct,
            'median': median,
            'mean': mean
        })

    df = pd.DataFrame(courses)
    regex_patterns = {
        r"ECTS:": "",
        r"Group\(s\):": "",
        r"Pass" : "",
        r"%" : "",
        r"Median": "",
        r"Average" : "",
        r"Block\(s\): ": ""
    }

    compile_regex = [(re.compile(pattern), replacement) for pattern, replacement in regex_patterns.items()]

    def remove_prefix(txt):
        for pattern, replacement in compile_regex:
            txt = re.sub(pattern, replacement, txt)
        return txt

    df = df[~df["pass_pct"].str.contains(" N/A", na=False)]

    df['length'] = df['length'].astype(str).swifter.progress_bar(True).apply(remove_prefix)
    df['timeslot'] = df['timeslot'].astype(str).swifter.progress_bar(True).apply(remove_prefix)
    df['group'] = df['group'].astype(str).swifter.progress_bar(True).apply(remove_prefix)
    df['fail_pct'] = round(100 - df['pass_pct'].astype(str).swifter.progress_bar(True).apply(remove_prefix).astype(float), 2)
    df['median'] = df['median'].astype(str).swifter.progress_bar(True).apply(remove_prefix)
    df['mean'] = df['mean'].astype(str).swifter.progress_bar(True).apply(remove_prefix)

    output_path = 'df_cleaned.csv'
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

    browser.quit()

if __name__ == "__main__":
    scrape_courses()