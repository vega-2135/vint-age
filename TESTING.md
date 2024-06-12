# Manual Testing

[Back to README](README.md)

The purpose of this document is to show the results, bugs and fixes made during the manually testing process of the VintAge website.

All tests were performed using the live environment deployed from Heroku.

<br>

## User Story Testing

<details>
<summary>As a shopper, I want to see a list of products upon visiting the site, so that I can select some to buy.</summary>

### Acceptance Criteria

- Given a logged-in user, they see a list of products.
- Given a logged-in user, they can select the products they want to buy.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper I can View individual prodict details, so that I can see images and available sizes of that product.</summary>

### Acceptance Criteria

- Given a user, they see a list of products.
- Given a  user, they can click on a product and a new page will open showing the product details. 


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper I can quickly indentify deals and special  offers, so that I can take advantage of special savings on products I would like to buy.</summary>

### Acceptance Criteria

- Given a user, they see a page with special offers.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper I can quickly indentify new arrivals, so that I can avoid goin through all the list of products searching for the new merchandise.</summary>

### Acceptance Criteria

- Given a user, they see a page with new arrived products.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I can easily view the total of my purchases at any time, so that I can avoid spending to much money</summary>

### Acceptance Criteria

- Given a logged in user, they see at any time, at the top right corner of the page the total cost of the products they have in their shopping cart.


**Result:** ✅ Pass
</details>

<details>
<summary>As a first-time visitor, I want a clear explanation of the advantages of being a registered user so that I can decide if I want to create an account on the site.</summary>

### Acceptance Criteria

- Given a first time visitor, upon being redirected to the sign-in page after clicking the register button, an explanation appears below the 'Sign in' title stating the advantages of having an account.


**Result:** ✅ Pass
</details>

<details>
<summary>As a user, I want to receive feedback messages upon registering and each time I log in or out of the site, providing assurance that the registration or login process was successful.</summary>

### Acceptance Criteria

- Given a user, after they click the register button, a welcome message appears at the top of the website.
- Given a user, after they log in and out of the website, a message pops up stating that they have logged in or out of the website.



**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I can easily register for an account, so that I have the benefits of having a personal account in the site.</summary>

### Acceptance Criteria

- Given a user, after they click the register button, they can fill a form with details required for creating an account.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I can easily login or logout from the site, so that I can see my personal account information any time I want.</summary>

### Acceptance Criteria

- Given a user, when they navigate to the site's login page, they see clear fields for entering their username/email and password.
- Upon entering valid credentials and clicking the login button, the users should be logged in to the site and have access to their profile information.
- Given a logged in user, there should be a clearly visible logout option, such as a "Logout" button or link, in the header or menu. Upon clicking the logout option, theusers should be logged out of the site and redirected to the site's homepage or another designated landing page.
- After logging out, if I they  try to access any protected pages or personal account information, they should be redirected to the login page and prompted to log in again.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I can recover my password in case I forget it, so that I can continue having access to my account.</summary>

### Acceptance Criteria

- Given a shopper who has forgotten their password, when they navigate to the site's password recovery page, they should see a clear option to initiate the password recovery process.
- Given a shopper who has successfully reset their password, when they attempt to log in using the new credentials, they should be able to access their account without any issues.
- After resetting the password and logging in, the shopper should have full access to their profile information and any other features available to logged-in users.
 


**Result:** ✅ Pass
</details>

<details>
<summary> As a shopper, I want to receive an email of confirmation after registering in the site, so that I can be sure that my account registration was successful.</summary>

### Acceptance Criteria

- Given a shopper who has successfully completed the registration process on the site, when they submit their registration details, they should receive an email confirmation request.
- The email confirmation request should be sent to the email address provided during registration and should contain a clear call-to-action to confirm the registration.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I want to have a profile page, so that I can view my personal order history and order confirmations, and save my payment information.</summary>

### Acceptance Criteria

- Given a registered shopper, when they log in to the site, there should be a clearly visible link or button in the navigation menu labeled "Profile" or "My Account".
- Upon clicking on the "Profile" link/button, the shopper should be directed to their profile page, which should display their personal information, order history, and any other relevant details.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I want to be able to sort the list of available products, so that I can easily identify products by category, ratings or price.</summary>

### Acceptance Criteria

- Given a shopper, when they navigates to the list of available products on the site, there should be clearly visible sorting options provided, such as dropdown menus or buttons, allowing the shopper to sort the products by category, ratings, or price.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I want to be able to sort the products of a specific category by name or sort a specific category of product, so that I can find the best-rated or best-priced product in a specific category.</summary>

### Acceptance Criteria

- Given a shopper, when they select a specific category of products, such as devises, jeans, or records, there should be sorting options provided exclusively for that category.
- The sorting options should include sorting by name, rating, and price, tailored specifically to the products within the selected category.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I want to have the capability to simultaneously sort various categories of products, enabling me to identify the product with the best price or higher rating across diverse product categories like "clothing" or "music".</summary>

### Acceptance Criteria

- Given a shopper navigating the product listings, when they select multiple categories to sort, the system should provide options to sort products across these chosen categories by price or rating.
- Upon selecting the sorting criteria, the products within the specified categories should be dynamically sorted based on the chosen parameters, allowing the shopper to view the best-priced or best-rated products across the selected categories simultaneously.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I want to be able to easily see the number of results of the product I have searched in the search box, so that I can quickly see whether the product I want is availabe and how many of that type of product are listed in the site.</summary>

### Acceptance Criteria

- Given a shopper using the search box to look for a specific product, when they enter their search query and press the search button, the site should display the total number of search results matching their query.
- Given a shopper entering a search query in the search box, when they refine or modify their search criteria, the site should dynamically update and display the updated number of search results without requiring a page refresh.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I want to select the size and quantity of a product when purchasing it, so that I can correct a mistaken quantity or size of a selected product.</summary>

### Acceptance Criteria

- Given a shopper, when they add a produt to the shopping cart, they have the option again in the shopping cart to select the size or/and quantity of the selected product.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper I want to view the items in my shopping bag, so that I can verify the total cost of my purchase and ensure all items I want to buy are included.
</summary>

### Acceptance Criteria

- Given a shopper, when they add items to the shopping bag, upon clicking the shopping bag, the bag page displays a list of all items added, including their names, quantities, and individual prices.

- Given a shopper, they can expect that the total cost of all items in the shopping bag are accurately calculated and displayed.

- Each item in the shopping bag provides a link to its detailed description page, so I can review the details before finalizing the purchase.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I want to be able to change the quantity of individual items in my shopping bag, so that I can easily modify my purchase before proceeding to checkout.</summary>

### Acceptance Criteria

- Given a shopper, once they are in the shopping bag page, they can make changes to the quantity of each of the items listed in the page.
- The total cost in the shopping bag updates automatically whenever they change the quantity of any item.
- The shopping bag page displays an error message if the shoppers attempt to set the quantity of an item to an invalid number (e.g., less than 1).


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I want to easily enter my payment information, so that I can checkout quickly and without any problems.</summary>

### Acceptance Criteria

- Given a shopper, they can expect that the payment form validates the entered information in real-time and displays appropriate error messages for any incorrect or incomplete entries.

- Given a shopper, they can expect that the the payment information is securely submitted and processed, ensuring customer data is protected during the transaction.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I can feel confident that my personal and payment information is safe and secure, so that I can provide the necessary details to complete my purchase.</summary>

### Acceptance Criteria

- The system uses Stripe for payment processing, ensuring that all transactions are handled securely and in compliance with Stripe's security standards.


**Result:** ✅ Pass
</details>

<details>
<summary>As a shopper, I want to add products to a wishlist, so that I can save items I'm interested in purchasing at a later time.</summary>

### Acceptance Criteria

- Given a logged-in shopper, when they view a product on the product detail page, upon clicking the "Add to Wishlist" button,
the product is added to their wishlist, and a message pops out stating that the product was added to their Wishlist.
    
- Given a logged in shopper, when they navigate to their wishlist from the "My Account" menu option, they see a list of all the products they have added to their wishlist and each product display the name, price, a remove from wishlist button and an image thumbnail.

- Given a logged in shopper viewing their wishlist, when they click the "Remove from Wishlist" button in the product thumbnail, the product is removed from the wishlist and a confirmation message pops out stating that the product was removed from their wishlist.


**Result:** ✅ Pass
</details>

<details>
<summary>As a user, I can view reviews of a product so that I can see what other people think about this product.</summary>

### Acceptance Criteria

- Given one or more review any logged or non logged in user can view them.

**Result:** ✅ Pass
</details>


<details>

<summary>As a registered user, i can edit and/or delete product reviews done by me, so that I can give and update my opinion about a particular product.</summary>

### Acceptance Criteria

- Given a logged in user, they can edit their review.
- Given a logged in user, they can delete their review.


**Result:** ✅ Pass
</details>

<br>

## Page Validation

This test aims to check all features and links from across the site are working as designed and developed.

To perform the test I used a Firefox browser, and validated each page from a mobile and desktop perspective using the inbuilt developer tool as some features were unique to a particular screen size.

<br>

File path                                                                                    | Features working | Links active
-------------------------------------------------------------------------------------------- | ---------------- | ------------
bag/templates/bag/bag.html                                                                   | PASS             | PASS
checkout/templates/checkout/checkout\_success.html                                           | PASS             | PASS
checkout/templates/checkout/checkout.html                                                    | PASS             | PASS
contact/templates/contact.html                                                               | PASS             | PASS
faq/templates/faq.html                                                                       | PASS             | PASS
home/templates/index.html                                                                    | PASS             | PASS
products/templates/products/add\_product.html                                                | PASS             | PASS
products/templates/products/edit\_product.html                                               | PASS             | PASS
products/templates/products/product\_detail.html                                             | PASS             | PASS
products/templates/products/products.html                                                    | PASS             | PASS
products/templates/products/wishlist.html                                                    | PASS             | PASS
profiles/templates/profiles/profile.html                                                     | PASS             | PASS
templates/allauth/account/confirm-email.html                                                 | PASS             | PASS
templates/allauth/account/login.html                                                         | PASS             | PASS
templates/allauth/account/logout.html                                                        | PASS             | PASS
templates/allauth/account/signup.html                                                        | PASS             | PASS
templates/errors/400.html                                                                    | PASS             | PASS
templates/errors/403.html                                                                    | PASS             | PASS
templates/errors/404.html                                                                    | PASS             | PASS
templates/errors/500.html                                                                    | PASS             | PASS

<br>


## Responsiveness

To ensure the website's layout and content remain well-structured and accessible across different screen sizes, I used Firefox's Developer Tools to virtualize the look and feel of the website and all its pages. Given that I opted to use Bootstrap, which provides standard media queries for screen sizes from XS through XL, I selected the following screens for testing: Samsung Galaxy Fold, Samsung Galaxy Note, iPhone 4, iPhone SE, iPad, iPad Mini, Laptop at 1366x768, Monitor at 1920x1080, and iMac 5K.

<br>

File path                                                                                    | Features working | Links active
-------------------------------------------------------------------------------------------- | ---------------- | ------------
bag/templates/bag/bag.html                                                                   | PASS             | PASS        
checkout/templates/checkout/checkout\_success.html                                           | PASS             | PASS        
checkout/templates/checkout/checkout.html                                                    | PASS             | PASS               
contact/templates/contact.html                                                               | PASS             | PASS        
faq/templates/faq.html                                                                       | PASS             | PASS        
home/templates/index.html                                                                    | PASS             | PASS              
products/templates/products/add\_product.html                                                | PASS             | PASS           
products/templates/products/edit\_product.html                                               | PASS             | PASS        
products/templates/products/product\_detail.html                                             | PASS             | PASS        
products/templates/products/products.html                                                    | PASS             | PASS        
products/templates/products/wishlist.html                                                    | PASS             | PASS
profiles/templates/profiles/profile.html                                                     | PASS             | PASS        
templates/allauth/account/confirm-email.html                                                 | PASS             | PASS        
templates/allauth/account/login.html                                                         | PASS             | PASS        
templates/allauth/account/logout.html                                                        | PASS             | PASS        
templates/allauth/account/signup.html                                                        | PASS             | PASS
templates/errors/400.html                                                                    | PASS             | PASS        
templates/errors/403.html                                                                    | PASS             | PASS        
templates/errors/404.html                                                                    | PASS             | PASS        
templates/errors/500.html                                                                    | PASS             | PASS        

<br>


## Accessibility 

Ensuring accessibility is essential for any successful eCommerce website. During the design phase, I used color contrast checkers to verify accessibility, and I was pleased with the positive results. Additionally, I employed Firefox Developer Tools to test each HTML page and the WAVE online assessment tool, which offers deeper insights and clearly highlights areas needing improvement.

<br>

File path                                                                                    | Features working | Links active
-------------------------------------------------------------------------------------------- | ---------------- | ------------
bag/templates/bag/bag.html                                                                   | PASS             | PASS        
checkout/templates/checkout/checkout\_success.html                                           | PASS             | PASS        
checkout/templates/checkout/checkout.html                                                    | PASS             | PASS               
contact/templates/contact/contact.html                                                       | PASS             | PASS        
faq/templates/faq/faq.html                                                                   | PASS             | PASS        
home/templates/home/index.html                                                               | PASS             | PASS              
products/templates/products/add\_product.html                                                | PASS             | PASS           
products/templates/products/edit\_product.html                                               | PASS             | PASS        
products/templates/products/product\_detail.html                                             | PASS             | PASS        
products/templates/products/products.html                                                    | PASS             | PASS        
products/templates/products/wishlist.html                                                    | PASS             | PASS
profiles/templates/profiles/profile.html                                                     | PASS             | PASS        
templates/allauth/account/confirm-email.html                                                 | PASS             | PASS        
templates/allauth/account/login.html                                                         | PASS             | PASS        
templates/allauth/account/logout.html                                                        | PASS             | PASS        
templates/allauth/account/signup.html                                                        | PASS             | PASS
templates/errors/400.html                                                                    | PASS             | PASS        
templates/errors/403.html                                                                    | PASS             | PASS        
templates/errors/404.html                                                                    | PASS             | PASS        
templates/errors/500.html                                                                    | PASS             | PASS   

<br>


## Performance
<br>
<br>


## Browser

Performing cross-browser testing is crucial for ensuring a positive user experience regardless of the user's preferred browser. To conduct a thorough test, I used Firefox, Chrome, and Edge on my local machine running Arch Linux. Additionally, I employed Lambda Testing, a browser testing tool that virtualizes various browsers, devices, and screen sizes, allowing me to test the site on Safari and Opera. 

<br>

| File path                                                                                    | Chrome (v107) | Firefox (v107 win 10) | Edge (v104 Win 10) | Safari (v15 macOS Monterey) | Opera (v89 macOS Monterey) |
| -------------------------------------------------------------------------------------------- | ------------- | --------------------- | ------------------ | --------------------------- | -------------------------- |
| bag/templates/bag/bag.html                                                                   | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| checkout/templates/checkout/checkout\_success.html                                           | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| checkout/templates/checkout/checkout.html                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| contact/templates/contact/contact.html                                                       | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| faq/templates/faq/faq.html                                                                   | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| home/templates/home/index.html                                                               | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| products/templates/products/add\_product.html                                                | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| products/templates/products/edit\_product.html                                               | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| products/templates/products/product\_detail.html                                             | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| products/templates/products/products.html                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| products/templates/products/wish\_list.html                                                  | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| profiles/templates/profiles/profile.html                                                     | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/allauth/account/confirm-email.html                                                 | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/allauth/account/login.html                                                         | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/allauth/account/logout.html                                                        | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/allauth/account/signup.html                                                        | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/errors/400.html                                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/errors/403.html                                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/errors/404.html                                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/errors/500.html                                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/includes/toasts/toast\_error.html                                                  | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/includes/toasts/toast\_info.html                                                   | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/includes/toasts/toast\_success.html                                                | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/includes/toasts/toast\_warning.html                                                | PASS          | PASS                  | PASS               | PASS                        | PASS                       |


<br>


## Devices Responsiveness

Similar to the aims of browser testing, I wanted to tests responsiveness and UX of the website across several conventional devices. For this I opened the website in several android and apple mobile devises, iPad and Laptop of several screen sizes.

<br>

| File path                                                                                    | Mobile (android) | Mobile (iOS)          | Tablet             | Laptop | 
| -------------------------------------------------------------------------------------------- | ---------------- | --------------------- | ------------------ |--------------------------- | 
| bag/templates/bag/bag.html                                                                   | PASS             | PASS                  | PASS               | PASS                        | 
| checkout/templates/checkout/checkout\_success.html                                           | PASS             | PASS                  | PASS               | PASS                        | 
| checkout/templates/checkout/checkout.html                                                    | PASS             | PASS                  | PASS               | PASS                        |
| contact/templates/contact/contact.html                                                       | PASS             | PASS                  | PASS               | PASS                        |
| faq/templates/faq/faq.html                                                                   | PASS             | PASS                  | PASS               | PASS                        |
| home/templates/home/index.html                                                               | PASS             | PASS                  | PASS               | PASS                        |
| products/templates/products/add\_product.html                                                | PASS             | PASS                  | PASS               | PASS                        |
| products/templates/products/edit\_product.html                                               | PASS             | PASS                  | PASS               | PASS                        |
| products/templates/products/product\_detail.html                                             | PASS             | PASS                  | PASS               | PASS                        |
| products/templates/products/products.html                                                    | PASS             | PASS                  | PASS               | PASS                        |
| products/templates/products/wish\_list.html                                                  | PASS             | PASS                  | PASS               | PASS                        |
| profiles/templates/profiles/profile.html                                                     | PASS             | PASS                  | PASS               | PASS                        |
| templates/allauth/account/confirm-email.html                                                 | PASS             | PASS                  | PASS               | PASS                        |
| templates/allauth/account/login.html                                                         | PASS             | PASS                  | PASS               | PASS                        |
| templates/allauth/account/logout.html                                                        | PASS             | PASS                  | PASS               | PASS                        |
| templates/allauth/account/signup.html                                                        | PASS             | PASS                  | PASS               | PASS                        |
| templates/errors/400.html                                                                    | PASS             | PASS                  | PASS               | PASS                        |
| templates/errors/403.html                                                                    | PASS             | PASS                  | PASS               | PASS                        |
| templates/errors/404.html                                                                    | PASS             | PASS                  | PASS               | PASS                        |
| templates/errors/500.html                                                                    | PASS             | PASS                  | PASS               | PASS                        |
| templates/includes/toasts/toast\_error.html                                                  | PASS             | PASS                  | PASS               | PASS                        |
| templates/includes/toasts/toast\_info.html                                                   | PASS             | PASS                  | PASS               | PASS                        |
| templates/includes/toasts/toast\_success.html                                                | PASS             | PASS                  | PASS               | PASS                        |
| templates/includes/toasts/toast\_warning.html                                                | PASS             | PASS                  | PASS               | PASS                        |    

<br>


## Code Validation

Writing well-structured, quality code is essential for the future development of this website or any other. To support this goal, I used industry-standard tools (see list below) to validate every line of code via the input method.

* W3 Validator for HTML
* W3 Jigsaw for CSS
* JS Hint for JavaScript
* CI Python Linter for Python

There were two errors find while validating some files from the project:
- In env.py file - E501 as line breached 79 characters, however when I tried to split these lines over two lines it not longer functioned. As a result I have chosen to allow this exceptions for the MVP.
- In settings.py I had the same E501 error in the section "AUTH_PASSWORD_VALIDATORS" as the value of one of the "Name" keys breached 79 characters. Again I tried to split that line into two in different ways and either the line was still too long or that line didn't worked. This I chose again to allow this exception for the MVP.
- During the validation of the html code from the register page, there was an error presumably located in a form code from the Allauth library thus I decided to allow this error as I don't know how a change in that line could affect the functionality of that code.

![Sign Up HTML validator error](docs_readme/images/accounts_signup_html_validation)

<br>

| File path                                                                                    | File Type | HTML | CSS  | JavaScript | Python | 
| -------------------------------------------------------------------------------------------- | --------- | ---- | ---- | ---------- | ------ | 
| bag/templates/bag/bag.html                                                                   | HTML      | PASS |      |            |        | 
| bag/templatetags/bag\_tools.py                                                               | PY        |      |      |            | PASS   | 
| bag/apps.py                                                                                  | PY        |      |      |            | PASS   | 
| bag/contexts.py                                                                              | PY        |      |      |            | PASS   | 
| bag/models.py                                                                                | PY        |      |      |            | PASS   | 
| bag/urls.py                                                                                  | PY        |      |      |            | PASS   | 
| bag/views.py                                                                                 | PY        |      |      |            | PASS   | 
| checkout/static/css/checkout.css                                                             | CSS       |      | PASS |            |        | 
| checkout/static/js/stripe\_elements.js                                                       | JS        |      |      | EXC        |        | 
| checkout/templates/checkout/checkout\_success.html                                           | HTML      | PASS |      |            |        | 
| checkout/templates/checkout/checkout.html                                                    | HTML      | PASS |      |            |        | 
| checkout/admin.py                                                                            | PY        |      |      |            | PASS   | 
| checkout/apps.py                                                                             | PY        |      |      |            | PASS   | 
| checkout/forms.py                                                                            | PY        |      |      |            | PASS   | 
| checkout/models.py                                                                           | PY        |      |      |            | PASS   | 
| checkout/signals.py                                                                          | PY        |      |      |            | PASS   | 
| checkout/urls.py                                                                             | PY        |      |      |            | PASS   | 
| checkout/views.py                                                                            | PY        |      |      |            | PASS   | 
| checkout/webhook\_handler.py                                                                 | PY        |      |      |            | PASS   | 
| checkout/webhooks.py                                                                         | PY        |      |      |            | PASS   | 
| contact/templates/contact/contact.html                                                       | HTML      | PASS |      |            |        |               
| contact/admin.py                                                                             | PY        |      |      |            | PASS   | 
| contact/apps.py                                                                              | PY        |      |      |            | PASS   | 
| contact/forms.py                                                                             | PY        |      |      |            | PASS   | 
| contact/models.py                                                                            | PY        |      |      |            | PASS   | 
| contact/urls.py                                                                              | PY        |      |      |            | PASS   | 
| contact/views.py                                                                             | PY        |      |      |            | PASS   | 
| faq/templates/faq/faq.html                                                                   | HTML      | PASS |      |            |        |              
| faq/admin.py                                                                                 | PY        |      |      |            | PASS   | 
| faq/apps.py                                                                                  | PY        |      |      |            | PASS   | 
| faq/models.py                                                                                | PY        |      |      |            | PASS   | 
| faq/urls.py                                                                                  | PY        |      |      |            | PASS   | 
| faq/views.py                                                                                 | PY        |      |      |            | PASS   | 
| home/tamplates/home/index.html                                                               | HTML      |      |      |            | PASS   | 
| home/apps.py                                                                                 | PY        |      |      |            | PASS   | 
| home/urls.py                                                                                 | PY        |      |      |            | PASS   | 
| home/views.py                                                                                | PY        |      |      |            | PASS   | 
| products/templates/products/custom\_widget\_templates/custom\_clearable\_file\_input.html    | HTML      | PASS |      |            |        | 
| products/templates/products/includes/quantity\_input\_script.html                            | HTML      | PASS |      |            |        | 
| products/templates/products/add\_product.html                                                | HTML      | PASS |      |            |        | 
| products/templates/products/base\_products\_display.html                                     | HTML      | PASS |      |            |        | 
| products/templates/products/edit\_product.html                                               | HTML      | PASS |      |            |        | 
| products/templates/products/product\_detail.html                                             | HTML      | PASS |      |            |        | 
| products/templates/products/products.html                                                    | HTML      | PASS |      |            |        | 
| products/templates/products/wish\_list.html                                                  | HTML      | PASS |      |            |        |
| products/admin.py                                                                            | PY        |      |      |            | PASS   | 
| products/apps.py                                                                             | PY        |      |      |            | PASS   | 
| products/forms.py                                                                            | PY        |      |      |            | PASS   | 
| products/models.py                                                                           | PY        |      |      |            | PASS   | 
| products/urls.py                                                                             | PY        |      |      |            | PASS   | 
| products/views.py                                                                            | PY        |      |      |            | PASS   | 
| products/widgets.py                                                                          | PY        |      |      |            | PASS   | 
| profiles/static/css/profiles.css                                                             | CSS       |      | PASS |            |        | 
| profiles/static/js/countryfield.js                                                           | JS        |      |      | EXC        |        | 
| profiles/templates/profiles/profile.html                                                     | HTML      | PASS |      |            |        | 
| profiles/apps.py                                                                             | PY        |      |      |            | PASS   | 
| profiles/forms.py                                                                            | PY        |      |      |            | PASS   | 
| profiles/models.py                                                                           | PY        |      |      |            | PASS   | 
| profiles/urls.py                                                                             | PY        |      |      |            | PASS   | 
| profiles/views.py                                                                            | PY        |      |      |            | PASS   | 
| static/css/style.css                                                                         | CSS       |      | PASS |            |        | 
| templates/allauth/account/confirm-email.html                                                 | HTML      | PASS |      |            |        | 
| templates/allauth/account/login.html                                                         | HTML      | PASS |      |            |        | 
| templates/allauth/account/logout.html                                                        | HTML      | PASS |      |            |        | 
| templates/allauth/account/signup.html                                                        | HTML      | PASS |      |            |        | 
| templates/errors/403.html                                                                    | HTML      | PASS |      |            |        | 
| templates/errors/404.html                                                                    | HTML      | PASS |      |            |        | 
| templates/errors/405.html                                                                    | HTML      | PASS |      |            |        | 
| templates/errors/500.html                                                                    | HTML      | PASS |      |            |        | 
| templates/includes/toasts/toast\_error.html                                                  | HTML      | PASS |      |            |        | 
| templates/includes/toasts/toast\_info.html                                                   | HTML      | PASS |      |            |        | 
| templates/includes/toasts/toast\_success.html                                                | HTML      | PASS |      |            |        | 
| templates/includes/toasts/toast\_warning.html                                                | HTML      | PASS |      |            |        |  
| templates/includes/main-nav.html                                                             | HTML      | PASS |      |            |        | 
| templates/includes/mobile-top\_head.html                                                     | HTML      | PASS |      |            |        | 
| templates/base.html                                                                          | HTML      | PASS |      |            |        | 
| vintage/settings.py                                                                          | PY        |      |      |            | PASS   | 
| vintage/urls.py                                                                              | PY        |      |      |            | PASS   | 
| vintage/views.py                                                                             | PY        |      |      |            | PASS   | 
| vintage/wsgi.py                                                                              | PY        |      |      |            | PASS   | 
| custom\_storages.py                                                                          | PY        |      |      |            | PASS   | 
| env.py                                                                                       | PY        |      |      |            | PASS   | 


<br>


## Challenges Faced
During the development phase, encountering bugs was inevitable. However, through active problem-solving strategies including consulting various resources, participating in forums, and revisiting bootcamp relevant materials, I successfully identified and resolved the issues that arose.

