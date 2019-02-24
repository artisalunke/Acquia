.. include:: /common/global.rst

Configuring multilingual Magento
================================

Magento uses different store views to separate and handle multilingual
content. You can configure Magento for multiple store views or locales,
mapped to multiple Drupal stores and languages through the
|acquia-product:ccs|. For full documentation about configuring multiple
store views in Magento, see the `Adding a
Language <http://docs.magento.com/m2/2.0/ee/user_guide/stores/store-language-add.html?Highlight=language>`__
Magento documentation page.

Configuring store views and locales in Magento
----------------------------------------------

To ensure that Drupal and Magento can communicate, you need to configure
Magento with the necessary locale information, and ensure that it has
the correct settings to connect to the |acquia-product:acm| API, by
completing the following steps:

#. Ensure `Magento is installed </commerce/install/magento>`__ and has
   at least a basic configuration.
#. Sign in to Magento as an administrator.
#. In the admin menu, go to **Stores > All Stores > Create Store View**.
#. Provide values for the following fields:

   -  **Store** – Select a Store from the list.
   -  **Name** – Create a name for the store view that reflects the
      purpose of the view. For example, ``Main Site en_US view`` for the
      primary United States store view in English.
   -  **Code** – A machine-friendly name for the view. It may, but is
      not required to, match your view **Name**, using underscores
      instead of spaces between each word.
   -  **Status** – Enable or disable your store view.
   -  **Sort order** – Add a manual sort order.

#. Click **Save Store View**.
#. For each store you create, make note of the store view **Code**, and
   review the admin URL to identify the **Store view ID**. In an admin
   URL containing ``...editStore/store_id/3/key/…`` the **Store view
   ID** is ``3``. Acquia recommends you use the Magento **Store view
   ID** in Drupal to identify the correct store view. Your list of store
   view **Code** and **Store view ID** fields should be similar to this
   example:
   +-----------------+---------------+
   | Store view code | Store view ID |
   +=================+===============+
   | default         | 1             |
   +-----------------+---------------+
   | main_fr_ca_view | 3             |
   +-----------------+---------------+
   | main_es_mx_view | 4             |
   +-----------------+---------------+

#. | In the admin menu, go to **Settings > Configuration > General >
     Locale Options**.
   | The current Magento scope will appear next to the **Store View**
     label. Your Magento installation will generally be set to the
     Default Config scope. For more information, see the `Scopes Magento
     documentation
     page <http://docs.magento.com/m2/ce/user_guide/configuration/scope.html>`__.

   |Magento store scopes|

#. Set each store view to its required locale by selecting a **Locale**
   from the menu. Other fields may be set manually, or by the system to
   a default value.
#. Click **Save Config**.
#. To set another store view to another locale, click the down arrow for
   the Magento configuration scope, and then select a different **Store
   View**, such as ``Main site es_MX``.

   |Switching store views|

#. In the **Locale** menu, select the correct locale, such as
   ``Spanish (Mexico)``.
#. Click **Save Config**.

With your store views complete, enter all the translations for the
products and categories. For more information, see the `Translating
Products Magento documentation
page <http://docs.magento.com/m2/ce/user_guide/catalog/product-translate.html>`__.

Update the Acquia Commerce API settings
---------------------------------------

Next, you must create unique IDs that can be mapped between Magento and
the |acquia-product:ccs|. Ensure your Magento installation is
`configured for use with Drupal </commerce/install/magento>`__.

#. Sign in to Magento as an administrator.
#. In the admin menu, go to **Stores > Configuration > Services >
   Magento Web API > Acquia Commerce API settings > Acquia Commerce
   Manager ID**.
#. Using the **Magento configuration scope**, set **Acquia Commerce
   Manager ID** for the ``default`` store view and set a different
   **Acquia Commerce Manager ID** for each additional store view
   (locale). Each store view's **Acquia Commerce Manager ID** must be
   different. Acquia recommends making the **Acquia Commerce Manager
   ID** the same as the store view code but there is no requirement to
   do so.
#. Click **Save Config** for each store view.

Be sure to note your **Acquia Commerce Manager ID** and the locale that
it corresponds to; you will need this for mapping purposes. Each ID
identifies the store mapping to the |acquia-product:ccs| to ensure that
the correct Drupal language connects to the correct Magento store view.

With your saved information, you can proceed to map Drupal and Magento
to each other.

Next step: `Map Drupal languages to Magento store views > </commerce/multilingual/connector>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |Magento store scopes| image:: https://cdn3.webdamdb.com/1280_cDRw782VPWD5.png?1527027911
   :width: 302px
   :height: 111px
.. |Switching store views| image:: https://cdn3.webdamdb.com/1280_gMlBTN9nG0k8.png?1527027902
   :width: 349px
   :height: 313px
