.. include:: /common/global.rst

About Drupal multisite installations
====================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/drupal/multisite/*

Drupal can run multiple separate websites from a single codebase. The individual websites share code (the Drupal core, modules, and themes), but each website has its own database so they do not share content, configuration, settings, or displayed themes. This style of architecture is known as *Drupal Multisite*.

This configuration can be very helpful for global website management tasks, such as website upgrades, since you only have to upgrade one codebase. However, having multiple websites running from the same codebase can multiply problems, such as security issues across your websites. For a more robust solution, consider |acquia-product:edg|.

To create a Drupal multisite, complete the following steps:

#. Sign in to the |acquia-product:ui| and select your application
#. `Create an additional database </acquia-cloud/manage/database#add>`__ for your new website.
#. Drupal 7 and 8 use the selection rules based on the multisite aliasing file ``sites/sites.php``, which must be present. Its optional settings will be loaded. The aliases in the array ``$sites`` will override the default directory rules. See `default.settings.php <http://cgit.drupalcode.org/drupal/tree/sites/default/default.settings.php?h=8.4.2#n13>`__ for more information about setting up the file. This enables you to map multiple domains to a specific directory.
#. Set up your aliases based on the ``sites/example.sites.php`` file.
#. In your local code repository, go to your ``[docroot]/sites/`` directory, and copy the ``/sites/example.sites.php`` file to ``sites.php`` in that directory.
#. Edit ``sites.php`` to include an entry for each of your websites, mapping the website directory to the URL. For example, for a website with the URL ``emea.example.com`` and the website directory ``[docroot]/sites/europe``, add the following line:

   .. code-block:: none
   
      $sites['emea.example.com'] = 'europe';

   For more information, see `Using sites.php to specify an alternate settings.php file <%5Bacquia-product:kb%5Darticles/using-sitesphp-specify-alternate-settingsphp-file>`__.
#. Copy the ``/sites/default/default.settings.php`` file into your new website's subdirectory, and then rename it to ``settings.php``.
#. In the |acquia-product:ui|, go to the **Databases** page, and click **PHP** to display the include statement (also called the require statement) for your website.

   |Display the require statement|

   Copy the include statement to the clipboard.

#. Edit the ``settings.php`` file in the new website's subdirectory, and then paste your website's include statement to the end of the file.
#. Commit the changes to the new website's ``settings.php`` file (and, if applicable, ``sites.php`` file) to |acquia-product:ac|:

   In the following Git commit, note that the ``-a`` option commits all the changes that you made to the workspace. To commit only a specific file or directory, replace ``-a`` with the name of the folder or directory.

   .. code-block:: none
   
      git commit -a -m "Added settings.php [and sites.php] for new website."

   When you use Git, the ``commit`` command only commits your changes to your local clone of the repository. To push those changes up to your |acquia-product:ac| website for deployment, use the ``git push`` command to push the changes to the appropriate branch. For example, if you are deploying from a branch named ``master``, use the following command:

   .. code-block:: none
   
      git push origin master

   Some Drupal distributions might have a ``.gitignore`` file that includes a line like this:

   .. code-block:: none
   
      # Ignore configuration files that may contain sensitive information. sites/*/settings*.php

   If it is present, delete the line, because it prevents you from being able to commit your website's ``settings.php`` file. As an alternative, use the ``git add -f settings.php`` command to force the code commit.

#. In your browser address bar, enter ``[site_URL]/install.php`` (where ``[site_URL]`` is the URL of the new website), and then press **Enter**. Continue with the standard Drupal installation procedure.

If you run a Drupal multisite on |acquia-product:ac|, you can add ``settings.php`` files to as many ``[docroot]/sites`` subdirectories as you need. Any domains for which you do not create a subdirectory will fall back to the ``[docroot]/sites/default/settings.php`` file and load that website.

Creating a multisite in a subdirectory of a domain
--------------------------------------------------

If you have a Drupal installation for a domain name (for example, ``example.com``) and you would like to add another website that will be located in a subdirectory of the same domain (for example, ``example.com/subsite``), the multisite configuration process is somewhat different.

#. Ensure that you have ``example.com`` defined on your |acquia-product:ac| **Domains** page. There is no need to add additional domains that have the subdirectory appended.
#. Add a new database for your multisite, if you have not already done so. See `Working with databases </acquia-cloud/manage/database>`__ for more information.
#. Add a multisite subdirectory to the ``/sites`` directory, as described in `step 3 <#sitesdir>`__ in the preceding procedure. In our example, the multisite directory would be named something like ``/sites/example.com.subsite``.
#. On the **Databases** page, click **PHP** for the |acquia-product:ac| require statement for the new database. On your server, you should copy the default ``settings.php`` file from the ``/sites/default`` directory and add the |acquia-product:ac| require statement.
#. You may need to `Create a symlink in your docroot <%5Bacquia-product:kb%5Darticles/adding-flexibility-your-server-structure-using-symlinks>`__, linking the subdirectory name up one level, to the docroot. For our example, create the symlink by executing the following from the command line while in the ``/docroot`` directory:

   .. code-block:: none
   
      ln -s ../docroot subsite

#. Add and commit the symlink and your multisite directory to your code repository.

After the changes have been propagated to the servers, you will be able to access your website at ``example.com/subsite``. If you need to import a database, you should do that as well, or visit ``example.com/subsite/install.php`` to install a new Drupal website. You can also `share database tables across a Drupal multisite </acquia-cloud/multisite/database-sharing>`__.

Related topics
--------------

-  `Using sites.php to specify an alternate settings.php file <%5Bacquia-product:kb%5Darticles/using-sitesphp-specify-alternate-settingsphp-file>`__
-  `Multi-site Drupal <https://www.drupal.org/docs/7/multisite-drupal>`__ at Drupal.org
-  `Multi-site - Sharing the same code base <https://www.drupal.org/docs/7/multisite-drupal/multi-site-sharing-the-same-code-base>`__ at Drupal.org

.. |Display the require statement| image:: https://cdn3.webdamdb.com/1280_ciyh2f99WPE9.png?1526475636

