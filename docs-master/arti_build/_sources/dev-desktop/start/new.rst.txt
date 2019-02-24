.. include:: /common/global.rst

Starting from scratch
=====================

Watch a video about installing Drupal (2:00)

.. raw:: html

   <iframe width="560" height="315" src="//www.youtube.com/embed/z1mdg4eXKcY?rel=0" frameborder="0" allowfullscreen=""></iframe>

To create a new Drupal website, starting from one of a variety of
popular Drupal distributions, complete the following steps:

In the |acquia-product:add| window, click the **+** button, and then click **New Drupal site**. If you are starting from the Welcome window shown in `Getting started </dev-desktop/start>`__, skip this step. Ensure that the PHP version is the right one for the Drupal version you're installing.

|Install a Drupal distribution|

Select a Drupal distribution to start from, and click **Install**.

|Choose a Drupal distribution|

Choosing a Drupal distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Drupal distribution is a curated package of Drupal software, including Drupal core, Drupal contributed modules, themes, libraries, and installation profiles that together provide a Drupal solution. While most Drupal distributions can be used with |acquia-product:add|, a selection of popular Drupal distributions are linked from |acquia-product:add| for easy installation. If you don't know which distribution you want to start with, use Drupal 8.

For more information about choosing a Drupal distribution, read `Distributions <http://drupal.org/documentation/build/distributions>`__ and `Additional distribution documentation <http://drupal.org/node/1085574>`__ on `drupal.org <http://drupal.org>`__.

The **Install a Drupal distribution (Step 2)** dialog box displays. Click **Finish** to install the selected distribution using the default options, or modify them by completing the following steps:

|Install step 2|

a. Enter the folder on your computer where the Drupal website codebase should be installed. The default folder name is based on the Dev Desktop ``sites`` folder you selected when you `installed Acquia Dev Desktop </dev-desktop/install>`__, with a subfolder based on the Drupal distribution and version you selected. Click **Change** to select a different folder.
b. Enter a name for your local website. The local website URL will be based on this name, so it can only use characters valid for a URL.
c. Select a PHP version to use. You can accept the default PHP version; however, some Drupal distributions or modules may require specific PHP versions.
d. Specify how to set up the database for your Drupal website. If you're really starting from scratch, select **Create a new database**. For other options, read `Importing a database </dev-desktop/start/db>`__.
e. Enter a name for your Drupal website's database. In most cases, you can accept the default value, which will match the local site name that you chose.
f. Click **Finish**.

|acquia-product:add| downloads the distribution you selected and extracts it in your local Drupal codebase folder.

Completing the installation
---------------------------

After you finish installing the Drupal distribution using |acquia-product:add|, you need to finish setting up the Drupal website using Drupal.

#. In |acquia-product:add|, select your site name, and click the local website URL.

   |Visit your website to complete installation|

   |acquia-product:add| uses Apache web server handles this URL request, and the Drupal install page for your new website opens in a browser window.

#. What happens next depends on which Drupal distribution you selected. The Drupal install page completes the installation of your website, including installing Drupal core and modules and setting up the website's database. In most cases, you will be prompted to complete the configuration of your website with administration account information.

After you have completed installing your Drupal website, you can proceed to develop it and add content to meet your organization's needs. If you are hosting your website on |acquia-product:ac|, see `Hosting a site on Acquia Cloud </dev-desktop/cloud>`__ for information about syncing your local website with the |acquia-product:ac| version of the website.

.. |Install a Drupal distribution| image:: https://cdn4.webdamdb.com/1280_otZt36hVXe41.png?1526475487
   :width: 590px
   :height: 261px
.. |Choose a Drupal distribution| image:: https://cdn2.webdamdb.com/1280_oa1MngEC9xP0.png?1526475513
   :width: 400px
   :height: 401px
.. |Install step 2| image:: https://cdn3.webdamdb.com/1280_2QUuLD8USkI7.png?1526475475
   :width: 590px
   :height: 224px
.. |Visit your website to complete installation| image:: https://cdn2.webdamdb.com/1280_EWZ027QzDWw0.png?1526475981
   :width: 590px
   :height: 284px
