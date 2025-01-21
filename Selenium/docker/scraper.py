from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import time

# Selenium Hub URL
HUB_URL = "http://127.0.0.1:54199/wd/hub"

# Function to scrape a single page
def scrape_page(page_url):
    print("Scraping")
    try:
        # Set up Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode
        print("Loading page")
        driver = webdriver.Remote(
            command_executor=HUB_URL,
            options=options
        )
        print("Connected")

        # Open the web page
        driver.get(page_url)
        print("Page read")

        # Scrape data (example: get the page title)
        num = int(driver.find_element(By.TAG_NAME, "p").text)
        print(f"Scraped: {num}")

        # Close the browser
        driver.quit()
        return num
    except Exception as e:
        print(f"Error scraping {page_url}: {e}")

# Function to run the scraper with multithreading
def run_scraper(url, num_requests):
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
        futures = [executor.submit(scrape_page, url) for _ in range(num_requests)]
        for future in futures:
            results.append(future.result())
    print(f"Final result: {sum(results)/len(results)}")

if __name__ == "__main__":
    # URL of the web page to scrape
    WEB_PAGE_URL = "http://sws-svc.default.svc.cluster.local:80" #"http://127.0.0.1:50740"
    # Number of requests to make
    NUM_REQUESTS = 100

    # Start scraping
    print("Starting")
    start_time = time.time()
    run_scraper(WEB_PAGE_URL, NUM_REQUESTS)
    end_time = time.time()

    print(f"Scraping completed in {end_time - start_time} seconds.")