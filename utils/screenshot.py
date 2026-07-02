import os
from datetime import datetime


def take_screenshot(driver, name):

    os.makedirs("screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # file_path = f"screenshots/{name}_{timestamp}.png"
    file_path = f"screenshots/{name}.png"

    driver.save_screenshot(file_path)

    return file_path