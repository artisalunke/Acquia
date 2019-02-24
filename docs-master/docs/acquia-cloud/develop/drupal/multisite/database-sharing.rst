.. include:: /common/global.rst

Sharing database tables across a Drupal multisite
=================================================

You can also configure your `multisite
installation </acquia-cloud/multisite>`__ to share database tables (such
as the users, sessions, and profiles tables) across multiple websites.

To share tables from a database across a Drupal multisite, retrieve the
full name of the shared database and then assign it using the ``prefix``
array, as you would normally. For example, to use the *drupal_shared*
database for users, sessions, and profiles, while using the *mysite*
database for everything else, enter the following text in your websites'
``settings.php`` files:

``'',   'authmap' => $shared,   'profile_fields' => $shared,   'profile_values' => $shared,   'permission' => $shared,   'role' => $shared,   'sessions' => $shared,   'users' => $shared,   'users_roles' => $shared, );  // Connect to the database. acquia_hosting_db_choose_active(); ?>``

For Drupal 8, omit these final lines:

``// Connect to the database. acquia_hosting_db_choose_active();``

Maintaining cross-domain sessions with the $cookie_domain variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a Drupal multisite configuration where the additional
websites are subdomains of the main domain (for example,
``www.example.com`` and ``multisite.example.com``), you may want to keep
the user session active when the user moves between the websites. All
that is needed is to add the following line to ``settings.php``, along
with the shared database code:

``$cookie_domain = '.example.com';``

With this setting, you share the user tables between the websites and
when a user signs in to ``www.example.com``, they are signed in to
``multisite.example.com`` and vice versa.

This only works if each of the domains is on the same
|acquia-product:ac| server and has the same second-level and top-level
domain name. (For example, ``www.example.com`` and
``multisite.example.com`` works, if both are on the same server, but
``www.example1.com`` and ``myothersite.example2.com`` will not.)
Otherwise, browser security policies will invalidate the session cookie.
