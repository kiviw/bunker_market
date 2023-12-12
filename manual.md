# Bunker Marketplace User Manual

## Introduction

Welcome to Bunker Marketplace! Bunker Marketplace is a peer-to-peer marketplace platform that allows users to buy and sell both digital and physical goods using Monero as the exclusive payment method. This user manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to use the marketplace effectively.

## Installation

To install Bunker Marketplace, please follow the steps below:

1. Clone the repository from GitHub by running the following command in your terminal:

   ```
   git clone https://github.com/your-username/bunker-marketplace.git
   ```

2. Install the required Python packages by running the following command in the terminal:

   ```
   pip install -r requirements.txt
   ```

3. Set up the MySQL database by creating a new database for Bunker Marketplace and updating the database connection details in the `config.ini` file.

4. Start the Bunker Marketplace by running the following command in the terminal:

   ```
   python main.py
   ```

5. Access the marketplace by opening your web browser and navigating to `http://localhost:5000`.

## Main Functions

### Registration

To register as a new user, follow these steps:

1. Click on the "Register" link on the homepage.

2. Fill in the registration form with your desired username and password.

3. Solve the captcha to verify that you are not a bot.

4. Click on the "Register" button to create your account.

### Login

To log in to your account, follow these steps:

1. Click on the "Login" link on the homepage.

2. Enter your username and password in the login form.

3. Solve the captcha to verify your identity.

4. Click on the "Login" button to access your account.

### Dashboard

Once logged in, you will be redirected to the dashboard. The dashboard provides an overview of your account, including your Monero account balance and recent transactions.

### Product Listing

To list a product for sale, follow these steps:

1. Click on the "Create Product" button on the dashboard.

2. Fill in the product details, including the name, description, price in USD, and category.

3. Upload an image of the product.

4. Click on the "Create" button to list the product.

### Product Search

To search for products, use the search bar on the homepage. Enter keywords related to the product you are looking for, and the marketplace will display relevant listings.

### Buying a Product

To buy a product, follow these steps:

1. Click on the product listing to view the details.

2. Click on the "Buy Now" button.

3. Confirm the purchase and provide any necessary information.

4. Complete the payment using Monero.

### Messaging

Buyers and sellers can communicate with each other through the messaging feature. To send a message, follow these steps:

1. Go to the product listing page.

2. Click on the "Message Seller" button.

3. Enter your message in the text box.

4. Click on the "Send" button to send the message.

### Dispute Resolution

In case of a dispute between the buyer and seller, the marketplace provides a dispute resolution feature. To open a dispute, follow these steps:

1. Go to the product listing page.

2. Click on the "Open Dispute" button.

3. Provide details about the dispute.

4. Submit the dispute for review by the admin.

## Conclusion

Congratulations! You have successfully installed Bunker Marketplace and learned about its main functions. You can now start buying and selling products on the marketplace. If you have any further questions or need assistance, please refer to the documentation or contact our support team. Happy trading!