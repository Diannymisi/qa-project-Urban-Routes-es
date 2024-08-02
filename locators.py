from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    boton_pedir_taxi = (By.CSS_SELECTOR, "button.button.round")
    boton_tarifa_comfort = (By.XPATH, ".//div[@class='tcard-icon']//img[@alt='Comfort']") # Nuevo selector para mejorar las buenas prácticas
    #(By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    selector_tcard_title = (By.CSS_SELECTOR, '.tcard-title')
    campo_numero_telefono = (By.CLASS_NAME, "np-text")
    agregar_numero_de_telefono = (By.ID, 'phone')
    boton_siguiente_numero_de_telefono = (By.CLASS_NAME, 'button.full')
    campo_ingresar_codigo = (By.ID, "code")
    boton_confirmar_codigo = (By.XPATH, ".//div[@class='modal']//button[text()='Confirmar']") # Nuevo selector para mejorar las buenas prácticas
    #(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    click_metodo_de_pago = (By.CSS_SELECTOR, '.pp-button.filled')
    click_agregar_tarjeta = (By.CSS_SELECTOR, 'div.pp-plus-container')
    campo_rellenar_tarjeta = (By.ID, 'number')
    rellenar_card_code = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    click_para_perder_foco = (By.CSS_SELECTOR, "div.plc")  # Nuevo selector para mejorar las buenas prácticas
    #(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[2]')
    boton_agregar_tarjeta = By.XPATH, "//button[@type='submit' and @class='button full' and text()='Agregar']" # Nuevo selector para mejorar las buenas prácticas
    #(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    boton_cerrar_ventana_emergente = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')
    obtener_metodo_de_pago = (By.CLASS_NAME, "pp-value-text")
    campo_comentario = (By.ID, "comment")
    slider_manta_y_pañuelos = (By.CSS_SELECTOR, ".slider.round")
    boton_agregar_helado = (By.CLASS_NAME, 'counter-plus')
    obtener_cantidad_de_helados = (By.CLASS_NAME, 'counter-value')
    pedir_taxi = (By.CLASS_NAME, 'smart-button')
    titulo_ventana_emergente = (By.CLASS_NAME, 'order-header-title')

    def set_from(self, from_address):
        from_field_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.from_field)
        )
        from_field_element.send_keys(from_address)

    def set_to(self, to_address):
        to_field_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.to_field)
        )
        to_field_element.send_keys(to_address)

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_from(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.from_field)
        ).get_property('value')

    def get_to(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.to_field)
        ).get_property('value')

    def set_click_boton_pedir_un_taxi(self):
        orderTaxi = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.boton_pedir_taxi)
        )
        orderTaxi.click()

    def set_click_boton_tarifa_comfort(self):
        clickComfort = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.boton_tarifa_comfort)
        )
        clickComfort.click()

    def get_boton_comfort(self):
        container = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.tcard.active'))        # Cambios en base a correcciones
        )
        textComfortRate = container.find_element(*self.selector_tcard_title).text
        return textComfortRate

    def set_boton_numero_telefono(self):
        clickPhoneNumber = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.campo_numero_telefono)
        )
        clickPhoneNumber.click()

    def set_ingresar_numero_de_telefono(self, numero):
        addNumber = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.agregar_numero_de_telefono)
        )
        addNumber.send_keys(numero)

    def set_click_boton_siguiente_numero_telefono(self):
        next = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.boton_siguiente_numero_de_telefono)
        )
        next.click()

    def set_ingresar_codigo(self, codigo):
        enterCode = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.campo_ingresar_codigo)
        )
        enterCode.send_keys(codigo)

    def set_confirmar_codigo(self):
        check = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.boton_confirmar_codigo)
        )
        check.click()

    def get_numero_telefono(self):
        numero = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.campo_numero_telefono)
        )
        return numero.text

    def set_proceso_numero_de_telefono_ingresar(self, numero):
        self.set_boton_numero_telefono()
        self.set_ingresar_numero_de_telefono(numero)
        self.set_click_boton_siguiente_numero_telefono()

    def set_codigo_numero_telefono(self, codigo):
        self.set_ingresar_codigo(codigo)
        self.set_confirmar_codigo()

    def set_click_metodo_pago(self):
        creditCard = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.click_metodo_de_pago)
        )
        creditCard.click()

    def set_click_agregar_tarjeta_por_favor(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.click_metodo_de_pago)
        ).click()

    def set_click_agregar_tarjeta(self):
        addButton = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.click_agregar_tarjeta)
        )
        addButton.click()

    def set_clicks_metodo_pago_agregar_tarjeta(self):
        self.set_click_metodo_pago()
        self.set_click_agregar_tarjeta_por_favor()

    def set_rellenar_campo_tarjeta(self, numeroDeTarjeta):
        addCard = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.campo_rellenar_tarjeta)
        )
        addCard.send_keys(numeroDeTarjeta)

    def set_rellenar_campo_codigo(self, numeroCode):
        enterCode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.rellenar_card_code)
        )
        enterCode.send_keys(numeroCode)

    def set_rellenar_campos_tarjeta_y_codigo(self, numeroDeTarjeta, numeroCode):
        self.set_rellenar_campo_tarjeta(numeroDeTarjeta)
        self.set_rellenar_campo_codigo(numeroCode)

    def get_obtener_campo_tarjeta(self):
        enterCard = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.campo_rellenar_tarjeta)
        )
        return enterCard.get_property('value')

    def get_obtener_campo_codigo(self):
        enterCode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.rellenar_card_code)
        )
        return enterCode.get_property('value')

    def set_click_para_perder_el_enfoque(self):
        clickOterSide = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.click_para_perder_foco)
        )
        clickOterSide.click()

    def set_click_boton_agregar_tarjeta(self):
        clickAdd = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.boton_agregar_tarjeta)
        )
        clickAdd.click()

    def set_click_cerrar_ventana_emergente(self):
        closeWindow = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.boton_cerrar_ventana_emergente)
        )
        closeWindow.click()

    def set_clicks_perder_enfoque_agregar_tarjeta_cerrar_ventana(self):
        self.driver.implicitly_wait(3)
        self.set_click_para_perder_el_enfoque()
        self.set_click_boton_agregar_tarjeta()
        self.set_click_cerrar_ventana_emergente()

    def get_obtener_metodo_de_pago(self):
        checkText = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.obtener_metodo_de_pago)
        )
        return checkText.text

    def set_agregar_comentario(self, message_for_driver):
        addComment = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.campo_comentario)
        )
        addComment.send_keys(message_for_driver)

    def get_comprobar_comentario(self):
        checkComment = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.campo_comentario)
        )
        return checkComment.get_attribute('value')

    def set_click_manta_y_pañuelos(self):
        clickSlider = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.slider_manta_y_pañuelos)
        )
        clickSlider.click()

    def get_saber_si_slider_esta_seleccionado(self):
        press = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='r-sw-container']/*[contains(text(),'Manta')]/..//div[@class='switch']//input[@class='switch-input']")
            )
        )
        return press.is_selected()  # Cambio a métodos y variables que coinciden en Inglés antes "apretar"

    def set_agregar_helado(self):
        two_ice_creams = WebDriverWait(self.driver, 20).until(  # Variable en inglés
            EC.presence_of_element_located(self.boton_agregar_helado)
        )
        two_ice_creams.click()
        two_ice_creams.click()  # Cambio a métodos y variables que coinciden en Inglés antes "dosHelados"

    def get_cantidad_de_helados (self):
        ice_cream = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.obtener_cantidad_de_helados)
        )
        return ice_cream.text

    def set_click_pedir_taxi(self):
        order = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.pedir_taxi)
        )
        order.click()

    def get_comprobar_ventana_emergente_si(self):
        pop_up_window = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.titulo_ventana_emergente)
        )
        return pop_up_window.text

    def set_tiempo(self):
        WebDriverWait(self.driver, 40).until(
            EC.text_to_be_present_in_element(self.titulo_ventana_emergente, 'El conductor llegará en')
        )

    def get_comprobar_informacion_de_conductor(self):
        other = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(self.titulo_ventana_emergente)
        )
        return other.text




