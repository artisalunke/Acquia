.. include:: /common/global.rst

Configuring multilingual Drupal for |acquia-product:acm|
========================================================

Drupal can, on its own, support several languages. Because of Drupal's
support for multiple languages, you can add one or more additional
languages to your Drupal application and its
|acquia-product:acm|-related content by using the Languages module in
Drupal core.

To configure multi-language support for your Drupal application with a
`configured |acquia-product:acm|
installation </commerce/install/modules>`__, complete the following
steps:

#. Sign in to your Drupal website as an administrator.
#. `Enable the following Drupal
   modules </resource/module-install-d8#enable>`__ on your website:

   -  **Language**
   -  **Content Translation**
   -  **Configuration Translation**
   -  **Taxonomy**

#. In the admin menu, go to **Configuration > Regional and Language >
   Languages**, and then click **Add language**.
#. Select the new language from the list, and then click **Add
   language**. For example, you can add French and Spanish.
#. In the admin menu, select **Configuration > Regional and Language >
   Content language and translation**.
#. Select the **Content** and **Taxonomy Term** check boxes.
#. In the **Translatable** section, select the check boxes for the
   fields that you want to make translatable. The list of selected
   fields should include the following selections:

   -  **Product** (Content)
   -  **Promotion** (Content)
   -  **Product Category** (Taxonomy)
   -  **SKU Product option** (Taxonomy)

#. Click **Save configuration**.
#. In the admin menu, go to **Commerce > Configuration > Store
   Settings**
#. Set the **Store ID** (also known as the **ACM UUID**) to the en_US or
   primary store view id from Magento. This ID generally has a value of
   ``1``.
#. Click **Translate store settings**, and then click **Edit** for one
   of the languages (such as **Spanish**).
   The webpage will display the translatable configuration fields. The
   **Store ID** for the EN Drupal language will be displayed on the
   left, and the **Store ID** for the Magento Spanish store view will be
   displayed on the right.
#. Enter the Spanish Magento store's ID value, such as ``2``.
   The **Store ID** or **ACM UUID** does not have to be meaningful.
   However, the values for each language or region must be unique in
   Drupal. It is recommended that you use the Magento store view integer
   IDs for this step.
#. Click **Save translation**.
#. Verify that your Drupal website has the authorization configured to
   enable the connector to properly map to the Magento store views. You
   will need the following items:

   -  *`OAuth user in Drupal with the proper scope for this
      connection </commerce/install/modules#oauth>`__* – In the **Add
      Client** step, ensure that you have a client with the **Scope**
      type of ``ACM``, or create a new user for connecting to
      |acquia-product:acm|.
      Keep a record of the **OAuth client ID** and **secret** used. We
      will use them later in the |acquia-product:ccs| when we create the
      `Drupal authentication
      mapping </commerce/multilingual/connector#auth-drupal>`__.
   -  *`**Conductor URL**, **HMAC Key ID**, and **HMAC Key Secret**
      values </commerce/install/modules#connector>`__*

Your Drupal website should now be ready to receive communications from
the |acquia-product:ccs|.

Next step: `Configuring multilingual Magento > </commerce/multilingual/magento>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
