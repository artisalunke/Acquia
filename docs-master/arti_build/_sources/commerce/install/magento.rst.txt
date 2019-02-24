.. include:: /common/global.rst

Configuring Magento for |acquia-product:acm|
============================================

.. container:: internal-navigation

   **Installing Acquia Commerce Manager**

   * :doc:`Start </commerce/install>`
   * :doc:`Modules </commerce/install/modules>`
   * Magento

`Magento <https://magento.com/>`__, an open-source commerce platform
that can create and share customer information, transactions, products,
goods, and services, can be used with |acquia-product:acm| to create a
full user commerce experience for your customers.

Setting up Magento
------------------

|acquia-product:acm| and Magento must be configured to work together to
allow you to synchronize your products and users between the two
platforms. To do this, complete the following steps:

#. `Download Magento <https://magento.com/tech-resources/download>`__.
   Acquia recommends that you use the latest stable release (version 2.x
   or greater).
#. Install Magento on your commerce hosting server. For more information
   about the installation process, see `Magento's installation
   instructions <https://magento.com/resources/technical>`__.
#. Sign in to Magento as an administrator.
#. Go to **System > Integrations** to configure the |acquia-product:acm|
   integration.
#. Click either the gear icon or the information icon |Magento
   information icon| next to **AcquiaConductor**.
#. Make note of the following access details, for use later in the
   process:

   -  **Consumer Key**
   -  **Consumer Secret**
   -  **Access Token**
   -  **Access Token Secret**

#. Contact your account manager to create an |acquia-product:acm|
   instance to connect Magento and Drupal.
#. Complete the following steps:

   #. Go to **Stores > Configuration > Services > Magento Web API**.
   #. Add the **Acquia Commerce Conductor URL**.
   #. Set the **Connector version** to ``Version two`` unless you have
      reason to set it differently.
   #. Set **Enable Conductor API Module** to ``Yes``.
   #. Open the **Acquia Commerce API Security Settings** fieldset and
      add the following:

      -  **HMAC Key ID**
      -  **HMAC Key Secret**

      These values are based on the ``site`` created in `Mapping stores
      and store views </commerce/multilingual/connector>`__.
   #. Click **Save Config**.

#. Initialize your categories, and then your products to Drupal using
   **Commerce > Configuration > Synchronize**.

.. note:: Because categories are updated synchronously, they should quickly
   appear. Products, however, are updated asynchronously, and are processed
   in groups to maintain website performance. 

If you have commerce data in Magento as **Categories** and **Products**,
these should populate in your Drupal website. After synchronization
occurs, your categories in Magento should appear as Taxonomy terms in
Drupal. You can check for these in your Drupal website.

To start this process, see `Adding categories and products to
|acquia-product:acm| </commerce/categories-products>`__.

Magento version differences for importing products
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After products are imported into Magento (**System > Import >
Products**), the version of Magento you are using determines what is
done with the imported products:

-  *Magento Enterprise Edition (EE)* – The imported products are sent to
   the |acquia-product:ccs| asynchronously in small batches, using
   Magento EE MessageQueue classes.
-  *Magento Community Edition (CE)* – The imported products are *not*
   sent to the |acquia-product:ccs|. In this case, to synchronize your
   Drupal product data with the newly Magneto-imported products we
   recommend instigating an asynchronous product import from Drupal.

Additional settings
-------------------

For some configuration needs, such as `mapping multilingual stores and
store views </commerce/multilingual/connector>`__, you may need
additional information, such as the Magento store Base URL.

#. Sign in to Magento as an administrator.
#. Navigate to **Stores > Configuration > General > Web**.
#. Click **Base URLs** or **Base URLs (secure)** as needed for
   additional configuration.
#. If you have made changes, click **Save Config**.
#. Add or note the **Base URL** and the **Base URL (secure)** for use in
   configuring items like multilingual configuration.

.. |Magento information icon| image:: https://cdn2.webdamdb.com/100th_sm_QJzWNHu8CI11.png?1527630916
   :width: 25px
   :height: 24px
