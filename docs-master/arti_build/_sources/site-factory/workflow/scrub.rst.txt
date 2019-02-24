.. include:: /common/global.rst

Scrubbing sensitive data from staged sites
==========================================

To work correctly, both your website and its modules require information
that is specific to your website, such as the following:

-  Your website maintains a list of accounts that can access the
   website, along with their passwords.
-  Modules have configuration information that they use to connect to
   third-party services.

Although this information is essential for your production website, not
all of the information may be necessary when you're testing your website
in your staging environment. If the information existed in both
production and staging, it could represent a security or performance
risk.

|acquia-product:edg| uses a scrub script called
``/hooks/common/post-db-copy/000-acquia_required_scrub.php``, which
clears certain sensitive information from your databases as they are
copied from production to staging.

Important

Do not edit or delete the ``000-acquia_required_scrub.php`` file.

The default scrub script runs a custom command (``acsf-site-scrub``) on
the website's database. This command uses the ``drush_sql_sanitize()``
function, which executes the Drush hook
```hook_drush_sql_sync_sanitize()`` <http://drupalcontrib.org/api/drupal/contributions!drush!docs!drush.api.php/function/hook_drush_sql_sync_sanitize/7>`__
to remove information relating to the website or the
|acquia-product:sfi|. The scrubbed information can include the following
items:

-  Website and |acquia-product:sfi| email addresses
-  Accounts locally created on websites (does not include OpenID
   accounts)
-  Caching information (including webforms and CDNs, if used)
-  301 website redirection settings
-  Google Analytics service settings
-  Internal logging and statistics

If you have added modules or features to your codebase, you can use one
of the following methods to either scrub your database or execute custom
actions:

-  Use ``hook_drush_sql_sync_sanitize()`` in your own, custom scrub
   script to remove any information that could have security or
   performance implications.
-  Use `|acquia-product:edg| hooks </site-factory/extend/hooks>`__ in
   your code either to do additional scrubbing or to execute custom
   actions.

.. _protectsf:

Protecting accounts during staging
----------------------------------

When the scrub scripts process user accounts, the accounts' user names
are changed to ``userXXXXX`` (where ``XXXXX`` is their user account
number), and their email addresses are removed. Users whose accounts
have been scrubbed therefore must sign in with the ``userXXXXX``
username and their regular |acquia-product:edg| password.

Not all user accounts are scrubbed, however. User accounts with the
`*developer* </site-factory/users/admin/developer>`__ or `*release
engineer* </site-factory/users/admin/release-engineer>`__ role are not
scrubbed during the staging process.

In addition, you can protect other accounts from scrubbing. If you have
an account that you don't want to be scrubbed during staging, complete
the following steps:

#. `Sign in to your *Prod* environment's
   |acquia-product:sfi| </site-factory/manage/login>`__ using an account
   with the `*platform
   admin* </site-factory/users/admin/platform-admin>`__ role.
#. In the admin menu, click **User**.
#. Find the user account that you want to prevent from being scrubbed,
   and click its **edit** link.
#. Click the **View** tab, and then click the **Click to preserve this
   user during scrubbing** link.

The account's information will not be scrubbed during any website
staging that takes place. To configure the account to once again have
its username and email information scrubbed, use the same process, but
instead click the **Click to scrub this user during scrubbing** link on
the user's **View** tab.

.. _protecthosted:

Protecting hosted website accounts during staging
-------------------------------------------------

As the scrub scripts process each website during the staging process,
they remove specific user information from each local account, including
each account's email address. User names are changed to ``userXXXXX``
(where ``XXXXX`` is their user account number), and their email
addresses are removed. Users whose accounts have been scrubbed therefore
must log in to staged websites with the ``userXXXXX`` username and their
regular password for the website.

If you have one or more accounts that you don't want to be scrubbed
during staging, you must one of the following hooks in your website's
code:

-  ``hook_acsf_staging_scrub_preserved_users_alter()`` - Protects local
   user accounts
-  ``hook_acsf_staging_scrub_admin_roles_alter()`` - Protects local
   roles

Each of the hooks accept an array by reference of one or more user or
role IDs, respectively.

When you reference the hooks, Drupal requires that you replace the
*hook* reference in the hook with the name of the module that contains
the hook. For example, if you use
``hook_acsf_staging_scrub_preserved_users_alter()`` in a module called
*example*, you would use
``example_acsf_staging_scrub_preserved_users_alter()``.

Example
~~~~~~~

The following code example demonstrates both of the hooks in use by a
module called *example*, protecting the account information for the
account with a user ID of 16 and for all accounts with a role ID of 26:

````

Note

To enable account protection during the staging process, be sure to
enable the module that contains the scrub protection hooks on your
production website.

.. _scrub:

Managing your scrub script
--------------------------

|acquia-product:edg| looks for your scrub script in the
``/hooks/common/post-db-copy`` folder off of docroot.

Your code distribution includes a sample scrub script called
``acquia-cloud-site-factory-post-db.sh`` that you can use as you develop
your own scrub script file. The sample file (located in the
``acsf_init/lib/cloud_hooks/samples/`` folder in the Drupal 8 module, or
the ``/hooks/samples`` folder in the Drupal 7 module) contains the
following code:

:literal:`#!/bin/sh # # Cloud Hook: post-db-copy # # The post-db-copy hook is run whenever you use the Workflow page to copy a # database from one environment to another. (Note: this script is run when # staging a site, but not when duplicating a site, because the latter happens on # the same environment.) See ../README.md for details. # # Usage: post-db-copy site target-env db-role source-env  site="$1" target_env="$2" db_role="$3" source_env="$4"  # You need the URI of the site factory website in order for drush to target that # site. Without it, the drush command will fail. The uri.php file below will # locate the URI based on the site, environment and db role arguments. uri=`/usr/bin/env php /mnt/www/html/$site.$target_env/hooks/acquia/uri.php $site $target_env $db_role`  # Print a statement to the cloud log. echo "$site.$target_env: Received copy of database from $uri ($source_env environment)."  # The websites' document root can be derived from the site/env: docroot="/var/www/html/$site.$target_env/docroot"  # Acquia recommends the following two practices: # 1. Hardcode the drush version. # 2. When running drush, provide the docroot + url, rather than relying on #    aliases. This can prevent some hard to trace problems. DRUSH_CMD="drush8 --root=$docroot --uri=https://$uri"  # Retrieve the site name. $DRUSH_CMD cget system.site name`

Be sure to include all of the variables defined in the sample scrub
script, because they are required for
`Drush <https://www.drupal.org/project/drush>`__ to locate your specific
website, which includes using the ``--uri=[URI]`` parameter, where
``[URI]`` is your website's location. To obtain your website's URI, in
the ``/hooks/samples`` folder in your distribution's files, run the
``acquia-cloud-site-factory-post-db.sh`` script.

As you add new modules or features to your website, be sure to edit your
website's scrub script to remove any unneeded database information
relating to the new additions.

After you create your new scrub script and deploy the code to your
codebase, be sure to test the operation of the scrub script by staging a
website and inspecting the website to ensure that the scrubbed
information doesn't appear in the staging environment.

.. _examples:

Scrub script command examples
-----------------------------

Based on your website and its custom needs, use the following examples
with your scrub script to accomplish different tasks.

Disabling modules for the staging environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To disable modules for the staging environment, use the following:

``drush @$site.$target_env --uri=$uri pm-disable [modules]``

Running custom commands defined in a module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use custom commands to act on your users' stored data, such as
removing phone numbers or credit card information.

``drush @$site.$target_env --uri=$uri [custom_command]``
