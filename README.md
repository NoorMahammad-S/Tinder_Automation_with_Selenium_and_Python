# Tinder Automation with Selenium and Python
This project automates Tinder interactions to mass-like profiles using Selenium and Python.

## Prerequisites

Before you run this script, you'll need to have the following installed:

- Python (3.6 or higher)
- Selenium
- Chrome WebDriver (or WebDriver for your preferred browser)

You can install Python packages using pip:

```bash
pip install selenium
```

Make sure to download the appropriate WebDriver for your browser and provide the path in the code.

## Usage

1. Clone this repository to your local machine.

```bash
git clone https://github.com/NoorMahammad-S/tinder-automation.git
```

2. Install the necessary Python packages as mentioned above.

3. Update the `FB_EMAIL` and `FB_PASSWORD` variables with your Facebook login credentials in the script.

4. Update the `chrome_driver_path` variable with the path to your WebDriver executable.

5. Run the script:

```bash
python tinder_automation.py
```

The script will automate the process of logging into Tinder, allowing location and notifications, and liking profiles. 
Please be aware that Tinder's free tier only allows 100 "Likes" per day.

## Configuration

- You may need to adjust the XPaths used in the script to match the structure of the Tinder website. XPaths may change over time.

## Disclaimer

**Use this script responsibly and in accordance with Tinder's terms of service.** Automating interactions on Tinder or any other 
platform can lead to account suspension or other consequences.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script is for educational and demonstration purposes only.
- Thanks to the developers of Selenium for providing a powerful web automation framework.
