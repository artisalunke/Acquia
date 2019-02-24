.. include:: /common/global.rst

Sharing the same codebase using Drupal multisite
================================================

|acquia-product:add| supports Drupal multisite, where several individual
websites share code (Drupal core, modules, and themes), but each website
has its own database and so they do not share content, configuration,
settings, or displayed themes. For more information, see `Multisite -
Sharing the same code
base <https://drupal.org/documentation/install/multi-site>`__ on
Drupal.org.

To create a new Drupal multisite, complete the following steps:

#. Select an existing website in the left panel. This website's codebase
   will be used to create a new Drupal multisite that contains a new
   site name, database, and files.
#. Click the **More** button, and then click **New Drupal multisite**.

   |Create a new Drupal multisite|

#. In the **Create new multisite** dialog box, enter values for the
   following fields:

   -  **Local site name** - Enter a name for your local website. The
      local website URL will be based on this name, so it can only use
      characters valid for a URL.
   -  **Database** list - Specify how to set up the database for your
      Drupal website. If you're starting from scratch, select **Create a
      new database**. For information about other options, see
      `Importing a database </dev-desktop/start/db>`__.
   -  **New database name** - Enter a name for the database you want to
      create. (This field is visible only if you click the **Create a
      new database** item in the **Database** list.

#. Click **OK**.

Working with a Drupal multisite
-------------------------------

After you create a Drupal multisite, |acquia-product:add| displays a
Multisite selector in the right panel.

|Multisite selector|

Use this selector to choose which website within your Drupal multisite
you want to work with. Note that when you change websites within the
Drupal multisite, the local website URL and the name of the local
database change, but the local code URL does not change. In a Drupal
multisite, all the websites share the same codebase.

Working with multisites on |acquia-product:ac|
----------------------------------------------

You can create a Drupal multisite locally with |acquia-product:add| and
then host it on |acquia-product:ac|, just like a single website
installation. If you already have a multisite hosted on
|acquia-product:ac|, you can clone it locally, creating local copy of
one website's database and files to start and then adding the others.

After you have a Drupal multisite with both local and
|acquia-product:ac| versions, you can sync them just like you do with a
single website installation.

.. |Create a new Drupal multisite| image:: https://cdn2.webdamdb.com/1280_okzN6p8HcGf6.jpg?1526475667
   :width: 590px
   :height: 564px
.. |Multisite selector| image:: https://cdn4.webdamdb.com/1280_wmzVgEAwr5R5.png?1526476032
   :width: 590px
   :height: 309px
