.. include:: /common/global.rst

Setting $base_url without breaking the Development and Staging environments
===========================================================================

Occasionally, it may be necessary to set the ``$base_url`` value in a
Drupal application's ``settings.php`` file, because a contributed module
may require this variable to be set, or an application may have
specialized configurations.

Unfortunately, setting this variable can cause issues on
|acquia-product:ac|, where there are separate Development, Staging, and
Production environments. If it is set unconditionally, the ``$base_url``
variable instructs Drupal to rewrite all requests for all environments,
which breaks environments to which this variable doesn't point.

The solution is to make use of the ```$_ENV['AH_SITE_ENVIRONMENT']``
environment variable </acquia-cloud/develop/env-variable#examples>`__
that is set by the |acquia-product:ac| environment.

Note for multisite users

`Multisite
installations <%5Bacquia-product:kb%5Darticles/multisite-definition>`__
should set ``$base_url`` in a dynamic fashion, as outlined here. Setting
the ``$base_url`` to an empty string disables caching and is not
recommended.

Modify and use the following example code as necessary to fit your
needs, and be sure to add your `Remote Administration
environment </ra/environment>`__ if your application has one:

``if (isset($_ENV['AH_SITE_ENVIRONMENT'])) {   switch ($_ENV['AH_SITE_ENVIRONMENT'])     {      case 'dev': $base_url = 'http://dev.example.com';        break;      case 'test': $base_url = 'http://test.example.com';         break;      case 'prod': $base_url = 'http://www.example.com';        break;     } }``

You can further modify the preceding code if there are environments that
don't require ``$base_url`` to be explicitly set. For example, if the
``$base_url`` variable is required only for Production, you can use the
following much shorter code snippet:

``if (isset($_ENV['AH_SITE_ENVIRONMENT']) && $_ENV['AH_SITE_ENVIRONMENT'] === 'prod') {   $base_url = 'http://www.example.com';  }``

Note

If you set a custom ``$base_url``, be aware that the variable should not
contain a trailing slash and should always start with either ``http://``
or ``https://``.
