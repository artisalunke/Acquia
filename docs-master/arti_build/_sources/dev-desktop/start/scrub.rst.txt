.. include:: /common/global.rst

Sanitizing the database on import
=================================

When you clone a website or pull a database from |acquia-product:ac| to
|acquia-product:add|, you can optionally sanitize (or scrub) the
database of user emails and passwords. This is a best practice for
security, so that your local website never includes real user emails (to
prevent developers from accidentally emailing users) and passwords.

|Sanitize database option|

Selecting the **Sanitize database** check box is the equivalent of using
the ``--sanitize`` option with the
```drush sql-sync`` <http://www.drushcommands.com/drush-7x/sql/sql-sync>`__
command. By default, it changes all email addresses to
``user+%uid@localhost`` and changes all passwords to ``password``. You
can customize these operations by editing your ``~/.drush/drushrc.php``
file. You can also add more sanitization operations using
```hook_drush_sql_sync_sanitize`` <http://api.drush.ws/api/drush/docs!drush.api.php/function/hook_drush_sql_sync_sanitize/6.x>`__
in a command file. Some Drupal contrib modules already do this to
sanitize their own data. When you select ``Sanitize database`` in
|acquia-product:add|, you also run those contrib module sanitizations.

.. |Sanitize database option| image:: https://cdn3.webdamdb.com/1280_Y2hDPjhXIhF4.png?1526475637
   :width: 590px
   :height: 321px
