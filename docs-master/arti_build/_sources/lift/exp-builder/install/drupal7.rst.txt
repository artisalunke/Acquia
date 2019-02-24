.. include:: /common/global.rst

Installing |acquia-product:leb| for Drupal 7
============================================

.. container:: internal-navigation

   **Installing Experience Builder**

   * :doc:`Install </lift/exp-builder/install>`
   * :doc:`Access </lift/exp-builder/access>`
   * :doc:`Content </lift/exp-builder/content-hub>`

Use the following instructions to install and configure the
|acquia-product:leb| client module on your Drupal 7 website.

Requirements
------------

As you are preparing to use |acquia-product:leb| with your website, be
sure to plan for the following requirements:

+-----------------------------------+-----------------------------------+
| Component                         | Requirement                       |
+===================================+===================================+
| **Drupal version**                | Drupal 7                          |
+-----------------------------------+-----------------------------------+
| **Keys**                          | After you purchase                |
|                                   | |acquia-product:cha|, Acquia will |
|                                   | email you a set of keys which are |
|                                   | required to connect to the        |
|                                   | |acquia-product:leb| service.     |
+-----------------------------------+-----------------------------------+

Installing |acquia-product:leb|
-------------------------------

To install and configure |acquia-product:leb|, complete the following
steps:

#. Sign in to your Drupal website as an administrator.
#. `Install and enable </resource/module-install-d7>`__ the following
   module on your website:

   -  `Acquia Lift
      Connector <https://www.drupal.org/project/acquia_lift>`__ *(be
      sure to select version 3.x—displayed as **Acquia Lift** on the
      Modules page)*

#. In the admin menu, click **Configuration**, and then click the
   **Acquia Lift** link.
#. In the **|acquia-product:cha| Credential** section, complete the
   following fields:

   -  **Account ID** – |acquia-product:lpm| account ID
   -  **Site ID** – The |acquia-product:cha| customer website associated
      with the account ID
   -  **Assets URL** – Obtain from your account manager
   -  **Decision API URL** – The API endpoint associated with your
      region (optional override)
   -  **Authentication URL** – Obtain from your account manager
      (optional override)

   .. important:: 

      Each website must have a unique Site ID. This includes development
      and testing environments.

#. Click **Save configuration**.

After you have ensured that all required modules are installed and
available for use, your website has the ability to connect to the
|acquia-product:leb| service.

`Continue to accessing the |acquia-product:leb| sidebar > </lift/exp-builder/access>`__
---------------------------------------------------------------------------------------
