.. include:: /common/global.rst

Configuring the |acquia-product:ch| client
==========================================

.. toctree::
   :hidden:
   :glob:

   /lift/contenthub/install/configure/*

.. container:: internal-navigation

   **Installing Content Hub**

   * :doc:`Install </lift/contenthub/install>`
   * Configure


After you have |installed|_, configure the user permissions to
administer and use the service, and then use the Drupal admin interface
to configure them to connect your website to the |acquia-product:ch|
repository.

.. |installed| replace:: installed the  \ |acquia-product:ch|\  client modules
.. _installed: /content-hub/install


Configuring user permissions
----------------------------

To manage |acquia-product:ch| settings (including the values on the
**Connections** that that control your Hub assignment), signed-in users
must have the appropriate permissions. To set the access permissions for
|acquia-product:ch|, complete the following steps:

#. In the admin menu, go to **People**, and then click the
   **Permissions** tab.
#. Assign the appropriate permissions to your website's roles from the
   following list:

   -  **Content Hub: Administer content hub**
   -  **Acquia Content Hub Connector: Administer content hub connector**

   By default, all users with the Administrator role have these
   permissions.
#. Click **Save permissions** to save your permission changes.


Configuring content sharing (publishing)
----------------------------------------

Next, see `Sharing content </content-hub/sharing>`__ to learn how to use
the Entity Configuration and Settings tabs to configure how you share or
publish content from your website to |acquia-product:ch|, where it can
be discovered and used by other members of your content network.

To ensure the data from your production environment is not corrupted by
data from non-production environments, configure 
`per-environment settings </lift/drupal/3/install#env>`__.

.. container:: message-status

   |Learning Services logo|\ For a step-by-step video tutorial introducing you to personalization with |acquia-product:cha|, including configuring content sharing, see |tutoriallink|_.

.. |Learning Services logo| image:: https://cdn3.webdamdb.com/1280_w1WjsvuWixS1.png?-62169955200
   :class: no-sb float-left logo-sm-lift
   :width: 36px

.. |tutoriallink| replace:: Creating Personalized Experiences with  \ |acquia-product:cha|\ 
.. _tutoriallink: /tutorials/creating-personalized-experiences-acquia-lift


Disconnecting from |acquia-product:ch|
--------------------------------------

|acquia-product:ch| allows you to disconnect your website from
|acquia-product:ch|. It can be reconnected at a later time, if desired.
Any content already published to the hub from the website you are
disconnecting will remain on the hub, but it will be orphaned.
Reconnecting your website to the hub will not reconnect the copy of the
content on the hub to its original source.

Depending on your installed version of Drupal, use the one of the
following methods to disconnect your website from |acquia-product:ch|:

-  *Drupal 7*

   #. In the Admin menu, go to **Configuration > Content Hub
      connector**.
   #. If it is not already selected, click the **Connection** page.
   #. Click **Disconnect**.

-  *Drupal 8* - Use one of the following `Drush </content-hub/drush>`__
   commands:

   -  acquia-contenthub-disconnect-site_
   -  acquia-contenthub-webhooks_

.. _acquia-contenthub-disconnect-site: /content-hub/drush-d8#acquia-contenthub-disconnect-site
.. _acquia-contenthub-webhooks: /content-hub/drush-d8#acquia-contenthub-webhooks