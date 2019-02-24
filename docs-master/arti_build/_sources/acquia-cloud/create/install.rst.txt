.. include:: /common/global.rst

Installing a Drupal distribution
================================

You can install a Drupal distribution (or Drupal core) using the
|acquia-product:ui|. A `*Drupal
distribution* <%5Bacquia-product:kb%5Darticles/distribution-definition>`__
is a custom edition of Drupal, tuned and extended with custom developed
and contributed modules to enable desired features, such as
`|acquia-product:ld| </lightning>`__. Using the |acquia-product:ui|, you
can install many of the best and most popular Drupal distributions with
just a few clicks. For a list, see `Choosing a Drupal
distribution </acquia-cloud/create/distro>`__.

To install a new Drupal distribution in an |acquia-product:ac|
environment, complete the following steps:

#. Sign in to the |acquia-product:ui| and select the application and
   environment where you want to install Drupal. You cannot install
   Drupal in a Production environment.
#. On the environment's **Overview** page, click **Install Drupal**.

   |Click the Install Drupal button|

   Note

   If **Install Drupal** is disabled for use, ensure that the following
   required items are in place for your environment:

   -  The **Code** entity in the environment has a branch or trunk
      selected — you cannot install to a tag.
   -  Livedev mode must be
      `disabled </acquia-cloud/develop/livedev#disable>`__ for your
      application. Livedev expects Drupal installation attempts only
      from the command line.

#. On the **Install distribution** page, locate the Drupal distribution
   that you want to install and then click **Install**. For many
   distributions, you can click **Learn more** to get more information
   about a distribution. If you are not sure which Drupal distribution
   to us, select **Lightning**.
#. If you want to install a distribution that's not listed (for example,
   your organization might have its own Drupal distributions, or you
   might want to install another distribution from drupal.org), click
   Install from URL. In the **Install Drupal from URL** dialog, enter a
   URL for the distribution. It must be either:

   -  The URL of the distribution's download file (which must be in
      ``.tar.gz`` format), or
   -  The URL of the distribution's Drush ``.make`` file.

   |Install another distro|

   Then, in the **Install Drupal from URL** dialog, click **Install**.

Deploying a new Drupal distribution in an environment takes a few
minutes. After the Installation process completes, click the
environment's website URL to visit your Drupal website. This runs
``install.php`` to complete the Drupal installation. The Drupal
``install.php`` script opens in a new browser window. It creates a
standard Drupal database, sets up the administrator username and
password, and configures additional modules and features relevant to the
Drupal distribution you chose.

|Install Drupal|

To start modifying your code, `make a local copy of the
repository </acquia-cloud/develop/checkout>`__ using the Git
``checkout`` command.

.. _related:

Related topics
--------------

-  `Creating a new application </acquia-cloud/create>`__
-  `Choosing a Drupal distribution </acquia-cloud/create/distro>`__

.. |Click the Install Drupal button| image:: https://cdn2.webdamdb.com/1280_Aj9mdUANbkh2.png?1527195748
   :width: 1260px
   :height: 438px
.. |Install another distro| image:: https://cdn3.webdamdb.com/1280_MPSpnQ9eiF38.png?1527200591
   :width: 675px
   :height: 339px
.. |Install Drupal| image:: https://cdn4.webdamdb.com/1280_s6togqSVXf46.png?1527200591
   :width: 400px
