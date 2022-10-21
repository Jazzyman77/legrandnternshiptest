from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def main():
    input1= "Carson"
    input2=  "password123"
    driver.get("https://www.demoblaze.com/")
    print(runtest(input1,input2))
    driver.quit()

def runtest(username, password):
    """Function to run automated test cases"""
    errorstring  = ""
    print("Filling out sign up form and closing it \n")
    try: #Testcase fill out signup and click close
        filloutcreateAccount(username, password)
        time.sleep(2)
        cancelcreateAccount()
        time.sleep(2)
        
    except:
        errorstring += "Fail to fill out new account and cancel"
    print("Filling out sign up form and submiting it\n")
    try: #Testcase fill out signup and click signup
        filloutcreateAccount(username, password)
        time.sleep(2)
        submitcreateAccount()
        time.sleep(2)
    
        
    except:
        errorstring += "Error when filling out form and clicking signup\n"
    print("Filling out login form and submiting it.\n")
    try: 
        logintoAccount( username, password)
        time.sleep(2)
    except:
        errorstring += "Error when filling out login form and clicking log in\n"
    else:
        print("Logging out\n")
        try: 
            logout()
        except:
            errorstring += "Error when clicking logout \n"
    print("Adding two phones to cart\n")
    try:
        gotohomepage()
        time.sleep(1)
        addphonetocart(1)
        driver.refresh()
        time.sleep(1)
        gotohomepage()
        time.sleep(1)
        addphonetocart(2)
        driver.refresh()
    except:
        errorstring += "Error when adding phone one and two \n"
    else:
        gotocart()
        time.sleep(1)
        try:
            numberofitems= f'Number of items in cart after adding 2 items: {numberincart()}\n' 
            print(numberofitems)
        
        except:
            errorstring += "Error when counting items in cart."
        print("Deleting two items from cart\n")
        try:
                
            Deleteitem()
            time.sleep(1)
            Deleteitem()
            time.sleep(1)

        except:
            errorstring += "Error when deleting 2 items from cart \n"

        try:
            numberofitems= f'Number of items in cart after deleting two: {numberincart()}\n' 
            print(numberofitems)
        
        except:
            errorstring += "Error when counting items in cart."
    print("Adding two phones to cart\n")
    try:
        gotohomepage()
        time.sleep(1)
        addphonetocart(3)
        driver.refresh()
        time.sleep(1)
        gotohomepage()
        time.sleep(1)
        addphonetocart(4)
        driver.refresh()
    except:
        errorstring += "Error when adding phone three and four \n"
    else:
        gotocart()
        time.sleep(1)
        try:
            numberofitems= f'Number of items in cart after adding 2 items: {numberincart()}\n' 
            print(numberofitems)
        
        except:
            errorstring += "Error counting items in cart."
        print("Deleting one items from cart\n")
        try:    
            Deleteitem()
            time.sleep(1)

        except:
            errorstring += "Error when deleting one item from cart \n"
        try:
            numberofitems= f'Number of items in cart after deleting one: {numberincart()}\n' 
            print(numberofitems)
        
        except:
            errorstring += "error when counting items in cart."


    gotohomepage()
    errorstring += "End of Report"
    return errorstring
    
    
def gotohomepage():
    """Function that clicks on home button link to navigate to home page"""
    home = driver.find_element("partial link text", "Home")
    home.click()
 

def gotocart():
    """Function that clicks on cart button link to navigate to cart"""
    cart = driver.find_element("id", "cartur")
    cart.click()
    

def addphonetocart(phone):
    """Function that specifically is designed to click on phone product links on homepage"""
    driver.refresh()
    driver.implicitly_wait(3)
    items = driver.find_elements("xpath", "//div[@class= 'col-lg-4 col-md-6 mb-4']/div[@class= 'card h-100']/a")
    items[phone].click()
    addtocart= driver.find_elements("xpath", "//div[@class= 'col-md-7 col-sm-12 col-xs-12']/div[@class= 'row']/div[@class= 'col-sm-12 col-md-6 col-lg-6']/a")
    addtocart[0].click()

    
def filloutcreateAccount( username, password):
    """Function that clicks sign up link and fills out form"""
    signupbutton = driver.find_element("id", "signin2")
    signupbutton.click()
    driver.implicitly_wait(3)
    signupformuser = driver.find_element("id", "sign-username")
    signupformpass = driver.find_element("id", "sign-password")
    signupformuser.clear()
    signupformpass.clear()
    signupformuser.send_keys(username)
    signupformpass.send_keys(password)
    driver.implicitly_wait(3)
    
def submitcreateAccount():
    """Function that clicks submit in signup form"""
    button = driver.find_elements("xpath", "//button[@class= 'btn btn-primary']")
    button[1].click()
    driver.refresh() #submit throws alert


def cancelcreateAccount():
    """Function that clicks close in signup form"""
    button = driver.find_elements("xpath", "//button[@class= 'btn btn-secondary']")
    button[1].click()



def logintoAccount(username, password):
    """Function that clicks login link to form and fills out form and clicks submit"""
    driver.refresh()
    loginbutton = driver.find_element("id", "login2")
    loginbutton.click()
    button = driver.find_elements("xpath", "//button[@class= 'btn btn-primary']")
    driver.implicitly_wait(5)
    loginformuser = driver.find_element("id", "loginusername")
    loginformpass = driver.find_element("id", "loginpassword")
    loginformuser.send_keys(username)
    loginformpass.send_keys(password)
    
    driver.implicitly_wait(3)
    button[2].click()

    


def logout():
    """Clicks on logout link"""
    driver.refresh()
    logoutbutton = driver.find_element("id", "logout2")
    driver.implicitly_wait(1)
    logoutbutton.click()

def numberincart():
    """On cart page this function counts number of items in cart and returns integer amount"""
    amount = 0
    cartitems = driver.find_elements("class name", "success")
    for i in cartitems:
        amount += 1
    return amount

def Deleteitem():
    """On Cart page this function clicks on delete element on first item"""
    driver.implicitly_wait(5)
    deletebuttons = driver.find_elements("partial link text", "Delete") 
    deletebuttons[0].click()
    return 0

    


if __name__ == "__main__":
    main()
