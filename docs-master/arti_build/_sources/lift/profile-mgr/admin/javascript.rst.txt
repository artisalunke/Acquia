.. include:: /common/global.rst

Managing your visitor capture settings
======================================

Depending on your needs, |acquia-product:lpm| allows you to configure
how the Drupal modules and the JavaScript tracking code interact with
|acquia-product:cha|.

To modify your capture settings, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the **Admin** tab.
#. Click the **Manage data collection settings** link.
#. Under **JavaScript Data Collection**, in the **Activity Level** list,
   select the amount of information that you want to store in
   |acquia-product:cha| about your visitors from the following options:

   -  **NONE** - Does not collect or store any visitor information
   -  **CAPTUREONLY** - Collects visitor information, but does not
      calculate segments or enable containers
   -  **FULL** - Collects visitor information, calculates segments, and
      enables containers

#. To control how long cookies (both first- and third-party cookies)
   used by the tracking code persist in visitors' browsers, enter values
   for the following fields:

   -  **Tracking time** - Positive integer for the amount of time to
      keep the tracking cookie (default value: **2**)
   -  **Time unit** list - Select from the following values:

      -  **years** (default)
      -  **months**
      -  **weeks**
      -  **days**
      -  **minutes**

#. In the **Maximum Size for Queue Cookie (Bytes)** field, enter
   ``4096``. If, after you have configured this field, your website
   experiences performance problems, the queue cookie's maximum size may
   be too large. The recommended range for optimal website performance
   is between 4096 and 1024 bytes. For more information about the queue
   cookie and possible size issues, see the `|acquia-product:cha|
   troubleshooting guide </lift/drupal/troubleshooting>`__.
#. In some cases, your website's visitors will use a shared resource to
   access your website — for example, an office that shares a single
   Internet-connected computer. To allow |acquia-product:cha| to
   identify specific visitors to your website in these situations, in
   the **Shared Machine Identifier** list, click the `standard or custom
   identity type </lift/profile-mgr/admin/customer>`__ that you want to
   use for your visitor identifier.
   When website visitors use a shared computer or resource,
   |acquia-product:cha| will assign a tracking ID to the visitor that's
   based on both the identifier provided by the visitor and a unique
   identifier value.
#. If you want to track visitors across different domains, select the
   **Third-Party Cookie Enabled** check box. |acquia-product:cha| will
   attempt to create third-party
   `cookies <https://en.wikipedia.org/wiki/HTTP_cookie>`__ that are
   associated with an Acquia server domain.

   .. note::  
   
      Not all browsers enable third-party cookies, and some visitors may
      install software to block third-party cookies.

   If you do not select this check box, |acquia-product:cha| will track
   visitors on your domain's websites by selecting **Use base domain to
   create Lift first-party cookie**.

#. After you have made all of the required modifications, click
   **Update**.