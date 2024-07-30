import data
import helpers
from locators import UrbanRoutesPage
from selenium import webdriver

# configuración entorno de pruebas y pruebas automatizadas

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()

# Verifica la funcionalidad de establecer una ruta en la aplicación "Urban Routes".
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

# Verifica que el texto del botón para la tarifa "Comfort"
# sea el esperado después de seleccionar la opción correspondiente
    def test_texto_tarifa_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_click_boton_pedir_un_taxi()
        routes_page.set_click_boton_tarifa_comfort()
        assert 'Comfort' == routes_page.get_boton_comfort()

    # Verifica agregar número de teléfono y el código de verificación.
    def test_agregar_numero_de_telefono(self):
        routes_page = UrbanRoutesPage(self.driver)
        numero = data.phone_number
        routes_page.set_proceso_numero_de_telefono_ingresar(numero)
        codigo = helpers.retrieve_phone_code(driver=self.driver)
        routes_page.set_codigo_numero_telefono(codigo)
        assert routes_page.get_numero_telefono() == numero

# Verifica los pasos de agregar una tarjeta de crédito
    def test_agregar_una_tarjeta_de_credito(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_click_metodo_pago
        routes_page.set_click_agregar_tarjeta_por_favor()
        numeroDeTarjeta = data.card_number
        numeroCode = data.card_code
        routes_page.set_click_agregar_tarjeta()
        routes_page.set_rellenar_campos_tarjeta_y_codigo(numeroDeTarjeta, numeroCode)
        routes_page.set_click_para_perder_el_enfoque()
        routes_page.set_click_boton_agregar_tarjeta()
        routes_page.set_click_cerrar_ventana_emergente()
        assert routes_page.get_obtener_campo_tarjeta() == numeroDeTarjeta
        assert routes_page.get_obtener_campo_codigo() == numeroCode
        assert routes_page.get_obtener_metodo_de_pago() == 'Tarjeta'

#     def test_agregar_una_tarjeta_de_credito(self):
        #         routes_page = UrbanRoutesPage(self.driver)
        #         routes_page.set_clicks_metodo_pago_agregar_tarjeta()
        #         numeroDeTarjeta = data.card_number
        #         numeroCode = data.card_code
        #         routes_page.set_rellenar_campos_tarjeta_y_codigo(numeroDeTarjeta, numeroCode)
        #         assert routes_page.get_obtener_campo_tarjeta() == numeroDeTarjeta
        #         assert routes_page.get_obtener_campo_codigo() == numeroCode
        #         routes_page.set_clicks_perder_enfoque_agregar_tarjeta_cerrar_ventana()
        #         assert routes_page.get_obtener_metodo_de_pago() == 'Tarjeta'

        def test_payment_method(self):
            routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
            card_number = data.card_number
            card_code = data.card_code

            routes_page.click_payment_method()
            routes_page.click_add_card()
            routes_page.add_card_number(card_number)
            routes_page.add_card_code(card_code)

            routes_page.click_outside_card_fields()
            routes_page.click_add_card_button()
            routes_page.click_close_payment_method()

            assert routes_page.get_payment_method_selected() == 'Tarjeta'

# Verifica que el comentario para el conductor se agregue correctamente
    def test_agregar_comentario_al_conductor(self):
        routes_page = UrbanRoutesPage(self.driver)
        comentario = data.message_for_driver
        routes_page.set_agregar_comentario(comentario)
        assert routes_page.get_comprobar_comentario() == comentario
 # Verifica que manta y pañuelos sean seleccionados correctamente
    def test_seleccionar_manta_y_pañuelos(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_click_manta_y_pañuelos()
        assert routes_page.get_saber_si_slider_esta_seleccionado() == True
    def test_agregar_2_helados(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_agregar_helado()
        assert routes_page.get_cantidad_de_helados() == '2'

# Verifica que el modal se muestre correctamente con el texto esperado
    def test_ventana_emergente(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_click_pedir_taxi()
        assert routes_page.get_comprobar_ventana_emergente_si() == 'Buscar automóvil'

# Verifica el cambio de un modal a otro (información conductor)
    def test_ventana_opcional(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_tiempo()
        assert 'El conductor llegará en' in routes_page.get_comprobar_informacion_de_conductor()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



















