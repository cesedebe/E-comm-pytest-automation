import allure
import pytest
import os
import sys
import logging as logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

@pytest.fixture(scope="class")
def init_driver(request):

    supported_browsers = ['chrome', 
                          'ch', 
                          'headlesschrome', 
                          'remote_chrome', 
                          'firefox', 
                          'ff', 
                          'headlessfirefox', 
                          'remote_firefox']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

    browser = browser.lower()

    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser in ('headlesschrome'):
        logger.info("Opening Chrome headless")
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == 'remote_chrome':
        logger.info("Starting remote Chrome")
        chrome_remote_url = os.environ.get("REMOTE_WEBDRIVER")
        if not chrome_remote_url:
            raise Exception(f"If 'browser=remote_chrome' then 'REMOTE_WEBDRIVER' variable must be set.")
        chrome_options = ChOptions()
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Remote(
            command_executor=chrome_remote_url,
            options=chrome_options
        )

    elif browser == 'remote_firefox':
        capabilities = {
            'browserName': 'firefox',
            'marionette': True,
            'acceptInsecureCerts': True
        }
        driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=capabilities)
    elif browser == 'headlessfirefox':
        ff_options = FFOptions()
        ff_options.add_argument("--disable-gpu")
        ff_options.add_argument("--no-sandbox")
        ff_options.add_argument("--headless")
        driver = webdriver.Firefox(options=ff_options)

    logger.debug("############### BROWSER INFORMATION #####################")
    for k, v in driver.capabilities.items():
        logger.debug(f"{k}: {v}")
    logger.debug("#########################################################")

    request.cls.driver = driver

    yield

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture and attach screenshots for failed frontend tests.
    Screenshots are attached to both pytest-html and Allure reports.
    Screenshots are only captured for tests that use the 'init_driver' fixture
    and only when the test fails or is marked as xfail but skipped.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ["setup", "call", "teardown"]:
        # Check if test failed or was skipped with xfail
        xfail = hasattr(report, "wasxfail")
        test_failed = (report.skipped and xfail) or (report.failed and not xfail)

        if test_failed:
            # Check if this is a frontend test (uses browser)
            is_frontend_test = 'init_driver' in item.fixturenames

            if is_frontend_test:
                try:
                    # Access the driver directly from the class if available
                    driver = getattr(item.instance, 'driver', None)
                    if driver:
                        logger.info(f"Capturing screenshot for failed test: {item.name}")
                        screenshot_base64 = driver.get_screenshot_as_base64()
                        extra.append(pytest_html.extras.image(screenshot_base64))

                        # Capture and add screenshot for Allure report
                        screenshot_png = driver.get_screenshot_as_png()
                        # Use item.config.workerinput to create unique screenshot path
                        worker_id = item.config.workerinput['workerid'] if hasattr(item.config,
                                                                                   'workerinput') else 'main'
                        results_dir = os.environ.get("RESULTS_DIR", "/tmp/test_results")
                        os.makedirs(results_dir, exist_ok=True)
                        screenshot_path = os.path.join(results_dir, f"{item.name}_{worker_id}.png")
                        with open(screenshot_path, "wb") as f:
                            f.write(screenshot_png)
                        allure.attach.file(screenshot_path, name='screenshot',
                                           attachment_type=allure.attachment_type.PNG)
                        extra.append(pytest_html.extras.url(screenshot_path, name="🔗 Open Screenshot"))
                    else:
                        logger.error(f"Driver not found for test {item.name}")
                        error_html = f"<div class='image' style='color: red; border: 2px solid #e74c3c; padding: 10px;'>⚠️ Driver not found</div>"
                        extra.append(pytest_html.extras.html(error_html))

                    # Get screenshot as PNG for Allure
                    screenshot_png = driver.get_screenshot_as_png()
                    allure.attach(
                        screenshot_png,
                        name=f"{item.name}_screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )

                    # Add test name and error message to Allure report
                    allure.attach(
                        f"Test: {item.name}\nError: {report.longrepr}",
                        name="Test Details",
                        attachment_type=allure.attachment_type.TEXT
                    )

                except Exception as e:
                    error_msg = f"Failed to capture screenshot: {str(e)}"
                    logger.error(f"{error_msg} for test {item.name}")

                    # Add error message to pytest-html report
                    error_html = f"""
                        <div class="image" style="color: red; border: 2px solid #e74c3c; padding: 10px; text-align: center; width: 320px;">
                            <div style="font-size: 24px; margin-bottom: 10px;">⚠️</div>
                            {error_msg}
                        </div>
                    """
                    extra.append(pytest_html.extras.html(error_html))

                    # Add error message to Allure report
                    allure.attach(
                        error_msg,
                        name="Screenshot Error",
                        attachment_type=allure.attachment_type.TEXT
                    )

    report.extra = extra


