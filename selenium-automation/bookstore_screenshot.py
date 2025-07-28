from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Setup
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Comment this line if you want to see browser
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)
wait = WebDriverWait(driver, 10)

# Create Screenshots directory
if not os.path.exists("Screenshots"):
    os.makedirs("Screenshots")

# Step 1: Open homepage
driver.get("https://demo.nopcommerce.com")
time.sleep(2)
driver.save_screenshot("Screenshots/step1_homepage.png")

# Step 2: Go to Login page
driver.find_element(By.CLASS_NAME, "ico-login").click()
time.sleep(2)
driver.save_screenshot("Screenshots/step2_login_page.png")

# Step 3: Try login with invalid credentials
driver.find_element(By.ID, "Email").send_keys("fake@example.com")
driver.find_element(By.ID, "Password").send_keys("wrongpassword")
driver.find_element(By.CSS_SELECTOR, "button.login-button").click()
time.sleep(2)
driver.save_screenshot("Screenshots/step3_login_error.png")

# Step 4: Search for a product
search_box = driver.find_element(By.ID, "small-searchterms")
search_box.clear()
search_box.send_keys("Apple MacBook Pro")
search_box.send_keys(Keys.RETURN)
time.sleep(2)
driver.save_screenshot("Screenshots/step4_search_result.png")

# Step 5: Click on the product
try:
    product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Apple MacBook Pro")))
    product.click()
    time.sleep(2)
    driver.save_screenshot("Screenshots/step5_product_page.png")
except Exception as e:
    print("❌ Step 5 failed:", e)

# Step 6: Add to cart
try:
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-4")))
    add_to_cart_button.click()
    time.sleep(3)  # Allow time for the notification popup
    driver.save_screenshot("Screenshots/step6_added_to_cart.png")
except Exception as e:
    print("❌ Step 6 failed:", e)

# Step 7: Go to Shopping Cart
try:
    driver.get("https://demo.nopcommerce.com/cart")  # <-- Direct navigation to cart
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
    time.sleep(2)
    driver.save_screenshot("Screenshots/step7_cart_page.png")
except Exception as e:
    print("❌ Step 7 failed:", e)

# Step 8: Try to checkout
try:
    wait.until(EC.element_to_be_clickable((By.ID, "termsofservice"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    time.sleep(2)
    driver.save_screenshot("Screenshots/step8_checkout_redirect.png")
except Exception as e:
    print("❌ Step 8 failed:", e)

# Cleanup
driver.quit()
print("✅ All steps completed. Screenshots saved in 'Screenshots/' folder.")
