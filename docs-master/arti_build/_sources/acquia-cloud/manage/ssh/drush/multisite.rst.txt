.. include:: /common/global.rst

Using Drush in a multisite installation
=======================================

If you're using a
`multisite <%5Bacquia-product:kb%5Darticle/multisite-definition>`__
installation, following best practices would have you ensure that you
are in the correct website directory before running a Drush command.
However, if you're using Drush across multiple applications in
succession, `using Drush aliases </acquia-cloud/drush/aliases>`__ can be
more efficient.

When executing Drush commands inside the
`docroot <%5Bacquia-product:kb%5Darticles/docroot-definition>`__, it is
necessary to use aliases. However, if you're not in the specific
multisite directory against which you want to execute Drush commands, it
is also necessary to specify the ``-l`` flag and provide a URI. If you
use an alias by itself and you are not in the relevant multisite
directory, Drush cannot determine which website it should execute
commands against.

For example, if you want to run a ``pm-list`` (or its alias, ``pml``)
and grep for the sync module on ``http://www.mysite.org``, use one of
the following commands based on your location:

-  *In the specific multisite installation directory (such as
   ``/var/www/html/mysite.test/sites/mysite.org``)* - No additional
   Drush parameters are needed. Use the following command:

   ``drush pml | grep sync``

-  *In the website's docroot, but not the specific multisite directory
   (such as ``/var/www/html/mysite.test``)* - You will need the URI for
   the specific multisite, similar to the following:

   ``drush -l http://domainb.mysite.org pml | grep sync``

-  *In the server's ``/var/www/html`` directory, but not in the Drupal
   installation docroot* - You will need both the URI and the Drush
   alias, similar to the following:

   ``drush @mysite.test -l http://domainb.mysite.org pml | grep sync``

   You need the alias to specify the Drupal website docroot since you're
   not in ``/var/www/html/mysite.test``, and you need the URI since
   you're not in the related multisite directory for
   ``http://domainb.mysite.org``.

-  *If you want to run Drush against all of the multisites in an
   environment that uses Cloud Hooks* - you can use the following
   command as an example, where ``[site]`` is the application, and
   ``[target.env]`` is the environment you want to run the command in:

   ``drush --root=/var/www/html/[site].[target_env]/docroot @sites updatedb --yes``
