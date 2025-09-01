
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import time

# Aqui eu faço as configurações do WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executar em modo headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializa o WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10) # Espera implícita para elementos carregarem

# Primeiro passo é realizar o Login
print("Navegando para a página de login...")
driver.get("https://www.saucedemo.com/")

# Encontra os campos de usuário e senha e o botão de login
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Preenche as credenciais e clica no botão de login
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

# Verifica se o login foi bem-sucedido
try:
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    print("Login bem-sucedido!")
except:
    print("Falha no login ou página de inventário não carregada.")
    driver.quit()
    exit()

# Segundo passo é a extração e o processamento de Dados
print("Extraindo dados dos produtos...")
products = []
product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item")

for product_element in product_elements:
    name = product_element.find_element(By.CLASS_NAME, "inventory_item_name").text
    price_text = product_element.find_element(By.CLASS_NAME, "inventory_item_price").text
    
    # Remove o cifrão e converte para float
    price = float(price_text.replace("$", ""))
    
    products.append({"Nome": name, "Preco_Numerico": price})

# Terceiro passo é realizar a regra de negócio e adicionar ao Carrinho os produtos com menos de 20 reais
print("Aplicando regra de negócio e adicionando produtos ao carrinho...")
selected_products_names = []

for i, product in enumerate(products):
    if product["Preco_Numerico"] < 20.00:
        # Encontra o elemento pai do produto
        product_container = product_elements[i]
        
        try:
            # Encontra o botão "Add to cart" dentro do container do produto
            add_to_cart_button = product_container.find_element(By.XPATH, ".//button[starts-with(@id, 'add-to-cart-')]")
            add_to_cart_button.click()
            selected_products_names.append(product["Nome"])
        except Exception as e:
            print(f"Não foi possível adicionar o produto {product['Nome']} ao carrinho: {e}")

# Aqui é onde vamos gerar os arquivos de saída

# todos_os_produtos.csv
products_df = pd.DataFrame(products)
products_df.to_csv("todos_os_produtos.csv", index=False)
print("Arquivo todos_os_produtos.csv gerado.")

# produtos_selecionados.txt
with open("produtos_selecionados.txt", "w") as f:
    for name in selected_products_names:
        f.write(name + "\n")
print("Arquivo produtos_selecionados.txt gerado.")

driver.quit()
print("Automação concluída.")


