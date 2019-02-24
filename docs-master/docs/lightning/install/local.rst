.. include:: /common/global.rst

Installing Lightning locally
============================

Use the procedure on this page to install Acquia's |acquia-product:ld|
distribution for Drupal 8 on a local server.

Requirements
------------

-  `Composer <https://getcomposer.org/doc/00-intro.md>`__
-  `Node <https://www.npmjs.com/>`__

Procedure
---------

After you confirm that you have access to the required software,
complete the following steps:

#. Open a command prompt window.
#. Run the following command:

   .. code-block:: none

      composer create-project acquia/lightning-project MY_PROJECT --no-interaction

Composer will create a new directory called ``MYPROJECT`` containing a
``docroot`` directory with a full |acquia-product:ld| codebase. You can
then 
`install Drupal </articles/simplified-drupal-install-guide>`__
normally.

For information about features available during the installation
process, see 
`Managing the additional Lightning features </lightning/install/features>`__.

.. note::

   If you want to push your local installation to |acquia-product:ac|, you must update your ``.gitignore`` file as described in the `.gitignore on Acquia-hosted sites versus Drupal default .gitignore <%5Bacquia-product:kb%5Darticle/gitignore-acquia-hosted-sites-versus-drupal-default-gitignore>`__ Acquia Knowledgebase article.
