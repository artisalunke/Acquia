.. include:: /common/global.rst

Stopping non-production environments from sending module update alerts
======================================================================

It is a best practice to keep your application's Drupal modules as
up-to-date as possible. This is for many reasons, including helping to
keep your application secure. An easy way to keep track of module
updates is to configure Drupal to email you when new module updates are
available on `Drupal.org <https://drupal.org>`__.

If you enable this feature with your |acquia-product:ac|-hosted
applications, you'll receive emails from each of your environments
informing you of any module updates. This can result in three times as
much email as you probably want about module updates. While you can
disable this setting in each of the environments, the next time that you
`copy your Production database to Development or
Staging </acquia-cloud/manage/database#copy>`__, you'll start receiving
these emails again because the setting is stored in the database.

Important

If you disable these notifications, it can be difficult to notice if
your environments have inconsistent module versions. Be sure to keep all
of your environments up-to-date as a group, whenever possible.

.. _disable:

Disabling update alert emails in an environment
-----------------------------------------------

To permanently disable this feature on any server other than Production,
you can add the following code snippet to the end of your application's
``settings.php`` file:

``if (isset($_ENV['AH_SITE_ENVIRONMENT']) && $_ENV['AH_SITE_ENVIRONMENT'] != 'prod') {   $conf['update_notify_emails'] = array(); }``

This forces the ``update_notify_emails`` setting to be empty for your
non-production environments, regardless of the setting in your
application's database. When this setting is empty, Drupal will ignore
the update emails functionality on all environments except for the
Production environment. Your Production environment will continue to
generate emails regarding module updates.
