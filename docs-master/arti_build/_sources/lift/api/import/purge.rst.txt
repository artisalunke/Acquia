.. include:: /common/global.rst

Purging a person from the database
==================================

Sometimes, it may be necessary to remove a person from your database.
This can be done by using the ``purgePerson`` event type, and passing it
on import through the File Import API. The person will remain active in
the database, but their tracking ID will be deleted and replaced with a
new, anonymous identifier. This is to ensure that the identifier no
longer relates the person to their navigation history.

The following is an example of how to purge a person from a database:

.. code-block:: none

   {"identity":"user@website.com","event_date":"2015-07-22 08:30:00.000","identity_source":"email","event_name":"purgePerson","event_source":"email"}

You will use an identifier to purge the person. You can only use
resolvable identifiers; in other words, the identifiers must be unique
and point to only one person. The following are resolvable identifiers:

-  ``email``
-  ``tracking ID``
-  ``account ID``
-  ``Facebook ID``
-  ``Twitter ID``
-  any custom identifiers that you have set up as resolvable

For more information about identifiers, see the person_identifier table
in `Omni-channel add-on Person field
types <https://docs.acquia.com/lift/omni/person#person_identifier>`__

.
