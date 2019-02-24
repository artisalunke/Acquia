.. include:: /common/global.rst

Using Drush with Acquia Dev Desktop
===================================

|acquia-product:add| includes `Drush <http://docs.drush.org/en/master/>`__, a command-line shell and scripting interface for Drupal. Drush includes tools for many Drupal development and management tasks. If you are accustomed to working from the command line, you may find that working with Drush is faster and easier than using the Drupal admin user interface.

Using Drush with local sites
----------------------------

For example, there are Drush commands to download, enable, and update contrib modules or themes from Drupal.org. If you wanted to use a module with your local website (in this case, the `Pathauto <https://www.drupal.org/project/pathauto>`__ module), use the following procedure:

#. In |acquia-product:add|, in the website list, click your local website.
#. To the right of the **Local code** field for your website, click its Drush console button |Drush console button|.
#. Enter one of the following Drush commands based on your needs:

   -  *Download* |--| Obtains the latest recommended version of the module, downloads it, and unzips it into your website's ``modules`` directory

      .. code-block:: none

         drush dl pathauto

   -  *Enable* |--| Enables the downloaded module for your website

      .. code-block:: none
      
         drush en pathauto

   -  *Update* |--| Similar to download, obtains the latest recommended version of the previously downloaded module, and also runs any required database updates

      .. code-block:: none
      
         drush up pathauto

.. _hosted:

Using Drush with Acquia-hosted sites
------------------------------------

Similarly, you can use Drush on an `Acquia Cloud </acquia-cloud>`__ website. To open a console window for your Drush commands, complete the following steps:

#. In |acquia-product:add|, in the website list, click your |acquia-product:ac| website.
#. To the right of the **SSH** address for your website, click its Drush console button |Drush console button|.

On |acquia-product:ac|, you can use Drush Cloud API commands, which provide a rich set of tools to extend, enhance, and customize your |acquia-product:ac| website. For more information, see `Developing with the Cloud API </acquia-cloud/api>`__.

.. _resources:

Additional resources
--------------------

-  `Introduction to Drush <%5Bacquia-product:kb%5Darticles/drush-intro>`__
-  `A Beginner's Guide To Drush <https://www.digitalocean.com/community/tutorials/a-beginner-s-guide-to-drush-the-drupal-shell>`__
-  `An introduction to Drush: The Drupal power tool <http://www.opc.com.au/media/blog/introduction-drush-drupal-power-tool>`__
-  `Drush Commands <http://www.drushcommands.com>`__.

.. |Drush console button| image:: https://cdn4.webdamdb.com/1280_cah0UkEaYQ35.png?1526475791
   :class: no-sb
   :width: 26px
   :height: 21px
