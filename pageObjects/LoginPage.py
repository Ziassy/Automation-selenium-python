from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


class LoginPage:
    textboxt_email_id = 'login'
    textbox_password_id = 'password'
    button_login_xpath = '//*[@id="wrapwrap"]/main/div/div/div/div/div[2]/div/form/div[3]/button'
    list_so_xpath = '//td[text()="Request Proforma Invoice"]'
    list_rfq_xpath = '//td[text()="Submit Proforma Invoice"]'
    button_accept_order_name = 'popup_accept_order'
    button_yes_fill_the_form_xpath = '//span[text()="Yes fill the form"]'
    button_edit_proforma_invoice_xpath = '//span[text()="Edit Proforma Invoice"]'
    shipping_mode_name = 'shipping_mode'
    shipping_mode_option_xpath = '//option[text()="Air Freight"]'
    shipment_type_name = 'shipment_type'
    shipment_type_option_xpath = '//option[text()="Less Container Load"]'
    container_type_name = 'container_type'
    container_type_option_xpath = '//option[text()="Dry Container"]'
    container_qty_name = 'container_qty'
    cargo_packaging_name = 'cargo_packaging'
    cargo_packaging_option_xpath = '//option[text()="Bagged Cargo"]'
    container_option_name = 'container_option'
    date_picker_name = 'shipment_date'
    date_xpath = '//tr[2]/td[5]'
    port_origin_name = 'port_origin'
    port_origin_option_xpath = "//a[contains(.,'Pelabuhan Kalianget, Surabaya')]"
    port_destination_name = 'port_destination'
    port_destination_option_xpath = "//ul[@id='ui-id-2']/li[3]/a"
    # untuk perkondisian takut addressnya kosong
    address_name = 'div_address'
    hs_code_name = 'hs_code'
    notes_name = 'notes'
    button_confirm_rfq_name = 'confirm_rfq'
    button_submit_rfq_xpath = '//span[text()="Ok"]'
    status_seller_name = 'so_status_seller'

    # Forwarder session
    sidebar_menu_id = 'openSidebar'
    rfq_menu_id = '//*[@id="sidebar_panel"]/div/ul/li[2]/a'
    button_accept_rfq_name = 'accept_rfq'
    shipping_price_name = 'shipping_price'
    # insert document
    upload_doc_xpath = 'ufile'
    button_confirm_price_xpath = '//span[text()="Confirm"]'
    # checking status
    fwd_order_status_name = 'order_status'

    # admin
    fwd_submitPI_xpath = '//td[text()="Forwarder Submit Proforma Invoice (1/25)"]'
    fwd_tab_xpath = '//a[text()="Forwarder"]'
    btn_approve_fwd_name = 'approve_forwarder'
    btn_approve_ok_xpath = '//span[text()="Ok"]'
    sale_status_admin = 'so_status_admin'

    # Login buyer web
    btn_login_page_xpath = '//button[text()="Login"]'
    input_username_name = 'login'
    input_password_name = 'password'
    checkbox1 = "recaptcha-checkbox-border"
    btn_login_name = 'btn-login'
    btn_login_xpath = "//button[contains(.,'Log In')]"


    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
    # Buyer login
    def clickBtnLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_page_xpath).click()
        self.driver.find_element(By.NAME, self.input_username_name).send_keys('fauziahfz216@gmail.com')
        self.driver.find_element(By.NAME, self.input_password_name).send_keys('Sinergi01!')
        time.sleep(5)
        # fix click checkbox using witch to frame
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CLASS_NAME, self.checkbox1).click()
        time.sleep(3)
        # Setelah switch frame, kembaliin lagi ke default content biar elementnnya ke define
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
        # self.driver.find_element(By.NAME, self.btn_login_name).click()



    def setUserName(self, username):
        self.driver.find_element_by_id(
            self.textboxt_email_id).send_keys(username)

    def setPassword(self, username):
        self.driver.find_element_by_id(
            self.textbox_password_id).send_keys(username)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    # Accept forwarder oleh admin
    def clickSOAcceptFWD(self):
        self.driver.find_element_by_xpath(self.fwd_submitPI_xpath).click()
        self.driver.find_element_by_xpath(self.fwd_tab_xpath).click()
        self.driver.find_element_by_name(self.btn_approve_fwd_name).click()
        self.driver.find_element_by_xpath(self.btn_approve_ok_xpath).click()
        status = self.driver.find_element_by_xpath(self.sale_status_admin).get_attribute('innerText')
        print(status)

    # Menu forwarder
    def clickSidebarMenu(self):
        self.driver.find_element_by_id(self.sidebar_menu_id).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.rfq_menu_id).click()


    # Bagian forwarder
    def clickRFQ(self):
        self.driver.find_element_by_xpath(self.list_rfq_xpath).click()
        self.driver.find_element_by_name(self.button_accept_rfq_name).click()
        self.driver.find_element_by_name(self.shipping_price_name).clear()
        self.driver.find_element_by_name(self.shipping_price_name).send_keys('1')
        self.driver.find_element_by_name(self.upload_doc_xpath).send_keys('D:/Automation_test/62trade/cms62trade/pageObjects/doc.jpg')
        self.driver.find_element_by_xpath(self.button_confirm_price_xpath).click()
        # untuk condition get attribut
        test = self.driver.find_element_by_name(self.fwd_order_status_name).get_attribute('innerText')
        print(test)

    # Bagian seller
    def clickSalesOrder(self):
        self.driver.find_element_by_xpath(self.list_so_xpath).click()

    # Seller with forwarder
    def clickAcceptOrder(self):
        self.driver.find_element_by_name(self.button_accept_order).click()

    def clickAcceptOrderForwarder(self):
        self.driver.find_element_by_xpath(self.button_yes_fill_the_form_xpath).click()

    def clickEditProformaInvoice(self):
        self.driver.find_element_by_xpath(self.button_edit_proforma_invoice_xpath).click()

    def clickChooseShippingMode(self):
        self.driver.find_element_by_name(self.shipping_mode_name).click()
        self.driver.find_element_by_xpath(self.shipping_mode_option_xpath).click()
        self.driver.find_element_by_name(self.shipment_type_name).click()
        self.driver.find_element_by_xpath(self.shipment_type_option_xpath).click()
        self.driver.find_element_by_name(self.container_type_name).click()
        self.driver.find_element_by_xpath(self.container_type_option_xpath).click()
        self.driver.find_element_by_name(self.container_qty_name).send_keys('Setengah Container')
        self.driver.find_element_by_name(self.cargo_packaging_name).click()
        self.driver.find_element_by_xpath(self.cargo_packaging_option_xpath).click()
        self.driver.find_element_by_name(self.container_option_name).click()
        # self.driver.find_element_by_xpath(self.container_option_xpath).click()
        # Dropdown
        select = Select(self.driver.find_element_by_name(self.container_option_name))
        select.select_by_visible_text("Shipper's Own Container")
        self.driver.find_element_by_name(self.date_picker_name).click()
        self.driver.find_element_by_xpath(self.date_xpath).click()
        self.driver.find_element_by_name(self.port_origin_name).click()
        self.driver.find_element_by_xpath(self.port_origin_option_xpath).click()
        self.driver.find_element_by_name(self.port_destination_name).click()
        self.driver.find_element_by_xpath(self.port_destination_option_xpath).click()
        self.driver.find_element_by_name(self.hs_code_name).send_keys('378')
        self.driver.find_element_by_name(self.notes_name).send_keys('Testing Notes')
        self.driver.find_element_by_name(self.button_confirm_rfq_name).click()
        self.driver.find_element_by_xpath(self.button_submit_rfq_xpath).click()
        # self.driver.find_element_by_name(self.status_seller_name)get_attribute('innerText')
        # buat kondisi address ilang atau nggk
        # print(self.driver.find_element_by_name(self.address_name).get_attribute('innerText'))
















