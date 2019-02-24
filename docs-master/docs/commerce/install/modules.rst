.. include:: /common/global.rst

|acquia-product:acm| Drupal module installation
===============================================

Installing |acquia-product:acm|

-  `Start </commerce/install>`__
-  Modules
-  `Magento </commerce/install/magento>`__

|acquia-product:acm| uses a specialized set of Drupal modules to connect
Drupal to your commerce solution, through the use of the
|acquia-product:ccs|.

Note

By default, if your website has only one language selected,
|acquia-product:acm| will not install Language or Content translation
Drupal core modules.

Enabling the modules
--------------------

After you have `obtained the |acquia-product:acm| Drupal
modules </commerce/install#start>`__, you must enable them for use with
your website. To do this, complete the following steps:

#. Using Composer, add the following modules to your website:

   -  |acquia-product:acm| modules
   -  `Address <https://www.drupal.org/project/address>`__
   -  `Key Value
      field <https://www.drupal.org/project/key_value_field>`__
   -  `Simple Oauth <https://www.drupal.org/project/simple_oauth>`__

#. Sign in to your Drupal website as an administrator with the
   permission to enable modules.
#. In the admin menu, click **Extend**
   (``http://[your site]/admin/extend``).
#. Select the check boxes for the following modules:

   -  Address
   -  Key Value field
   -  Simple Oauth
   -  Acquia Commerce Base SKU
   -  Acquia Commerce Cart
   -  Acquia Commerce Checkout
   -  Acquia Commerce Core
   -  Acquia Commerce Customer
   -  Acquia Commerce Payment
   -  Acquia Commerce Product
   -  Acquia Commerce Promotion

#. Click **Install** to enable the modules.

Next, you will need to configure the modules for your use.

Configure OAuth
---------------

To configure the modules that you have enabled to allow you to connect
to your commerce solution, complete the following steps:

#. Open a command prompt window, and then execute the following commands
   to generate a pair of RSA keys to encrypt your tokens:

   ``openssl genrsa -out private.key 2048 openssl rsa -in private.key -pubout > public.key``

   For security reasons, be sure to store the keys `outside of your
   docroot
   directory </acquia-cloud/manage/files/system-files/private>`__.

#. In your website, as an administrator, go to **Configuration > People>
   Simple OAuth**
   (``http://[your site]/admin/config/people/simple_oauth``).
#. Set the following values:

   -  **Access token expiration time** – ``300``\ (default)
   -  **Refresh token expiration time** – ``1209600`` (default)
   -  **Public Key** – The path to your public key file, from the
      previous step *(Required)*
   -  **Private key** – The path to your private key file, from the
      previous step *(Required)*

#. Click **Save configuration**.
#. Click the **Clients** tab, and then click **Add Client**
   (``http://[your site]/admin/config/people/simple_oauth/oauth2_client/add``).
#. Enter the following values to create a new OAuth client:

   -  **Label** – The client label *(Required)*
   -  **Logo** – The client logo
   -  **Description** – A description of the OAuth client being used
   -  **User**- The selected user will be used for creating content.
   -  **Language** – Specify a language, if desired.
   -  **New Secret** – Used to create a hash of the secret key.
   -  **Is Confidential?** – Select this check box to ensure the client
      secret is validated.

#. In the **Scopes** section, select the check box for **ACM**.
#. Click **Save**.
#. Copy the values from the following fields to use when setting up the
   |acquia-product:ccs| connection:

   -  **UUID**
   -  **Secret**
   -  **User**

Configure the |acquia-product:ccs|
----------------------------------

Using the details from the OAuth client, with additional details from
your account, you can configure the |acquia-product:ccs|.

#. Go to **Commerce > Configuration > Conductor Settings**, and enter
   the required information in the following fields:

   -  **Conductor URL** – You should receive this value either during
      onboarding or from your Acquia Account Manager *(Required)*
   -  **API version** – Currently set to **V2** *(Required)*
   -  **ACM ID** – A unique ID provided by your Acquia Account Manager
      *(Required)*
   -  **HMAC Key ID** – You should receive this value either during
      onboarding or from your Acquia Account Manager
   -  **HMAC Key Secret** – You should receive this value either during
      onboarding or from your Acquia Account Manager
   -  **Product Node Type** – The default Drupal node type that will be
      used to display products *(Required)*
   -  **Category Vocabulary** – The Drupal taxonomy vocabulary where
      product categories synchronize.
   -  **Enable this to use the SKU as the product title** – Select this
      check box to activate
   -  **Text Format** – The default text format used when content is
      imported.
   -  **Filter root level category** – Select this check box to remove
      the root level categories from your lists
   -  **Conductor Connection Timeout** – Set to 30 second by default
      *(Required)*
   -  **Conductor Verify SSL** – Select this check box to ensure SSL
      connections using the |acquia-product:ccs|
   -  **Conductor Product Synchronization Page Size** – The number of
      products that will synchronize at a time between the website and
      the commerce solution—Acquia strongly recommends leaving this at
      the default value of ``50``
   -  **Debug Level Logging Of API Connections** – Used for
      troubleshooting purposes—Acquia recommends that you do not select
      this unless necessary
   -  **Enable test mode to return mock data** – Used for
      troubleshooting purposes or testing—Acquia recommends that you do
      not select this unless necessary

#. Click **Save Configuration**
#. If you want to run page behind Basic Auth, download the
   `Shield <https://www.drupal.org/project/shield>`__ module, and then
   apply this
   `patch <https://www.drupal.org/files/issues/exclude_include_pages-2822720-15.patch>`__.

Your Drupal website should now be ready to connect to the
|acquia-product:ccs|.
