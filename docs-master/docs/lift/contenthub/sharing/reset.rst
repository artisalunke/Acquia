.. include:: /common/global.rst

Resetting and reindexing entities by content type
=================================================

If you alter the content type configuration for a content type that you
are exporting to |acquia-product:ch|, search mappings for that content
type may no longer correctly function. For example, after changing a
field from a list of names to an entity reference, the field now cannot
be used by |acquia-product:ch| or indexed by the Elastic Search Index.

To address this, you can use the ``ach-reset [entity_type]`` Drush
command to clear all entities of that content type from
|acquia-product:ch|, reset that content type's mapping, reindex all
entities of the specified type, and then republish them back to
|acquia-product:ch|.

For ``ach-reset [entity_type]`` to fully remove, reindex, and republish
all entities of a certain type, it must be executed *twice*. Before
executing, the command performs the following tests as a failsafe to
determine whether or not resetting and reindexing can proceed:

Does this website have a registered webhook for notifications?
 Without a registered webhook for notifications after the reindex
 completes, the content will never begin the republishing process.

Is this entity type in use by multiple websites?
 If yes, removing content will affect only content published by this
 website, because a website cannot delete other websites' content. You
 must manually delete the content from the other websites using other
 means, such as the ``ach-delete`` command. The ``ach-reset`` command
 will provide you with a list of matching entities and their
 originating websites.

Has the ``reindex`` state variable been set to** ``Reindex Completed``?
 When a reindex request is sent, the ``reindex`` variable is set to
 ``Reindex Sent``, and until the webhook notifies the website that the
 reindexing process is complete (setting the variable to
 ``Reindex Completed``) |acquia-product:ch| will accept no additional
 reindexing requests.


First execution
---------------

If no ``reindex`` request currently exists, executing
``drush ach-reset`` will cause |acquia-product:ch| to perform the
following steps:

#. Mark all entitles of the specified type exported by this website for
   later re-export.
#. Delete all entities of the specified type from |acquia-product:ch|.
   Note that as a result, entity mappings for Search are also deleted.
#. Trigger a ``reindex`` request using a webhook to |acquia-product:ch|.
#. Set the ``reindex`` variable to ``Reindex Sent``, which indicates
   that the website is waiting for |acquia-product:ch| to reindex all
   content of the specified type.
#. Reindex all content of the specified type from this website.
#. Send a webhook to the website notifying it that the reindex is
   complete.

The website will change the ``Reindex`` state variable to
``Reindex Completed``, which cancels the ``waiting`` mode and indicates
that it is ready to re-export entities of the specified type to
|acquia-product:ch|.


Second execution
----------------

For the second execution of ``drush ach-reset``, if a ``reindex``
request has been marked ``Reindex Completed``, |acquia-product:ch| will
use the Batch API to re-export the previously-deleted entities back into
|acquia-product:ch|, using the current type mappings.
