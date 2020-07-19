# RingFitAlarm
A tool to constantly check the inventory status of Ring Fit Adventure on Bestbuy and/or Target for you and send notifications once it becomes available.

# Installation
1. Run `pip install -r requirements.txt`
2. Install correct ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/home
3. Edit configurations in `config.py`
4. Run `python alarm.py`

# Things to Note
1. Checking the Bestbuy product status is disabled by default because it requires a Bestbuy developer api that you should get on your own. Once you have one, paste it into `config.py` and set the `use_bestbuy` flag to `True`.
2. Checking the Target product status currently only applies to your default store location. Replace the `target_store` variable with the correct store name for you.
3. This tool is initially developed to check the inventory of Ring Fit Adventure, but it can be readily used to check any other product. For Bestbuy products, replace the `bestbuy_sku` variable with the correct sku number. For Target products, replace the `target_url` variable with the correct url of the product's page.
