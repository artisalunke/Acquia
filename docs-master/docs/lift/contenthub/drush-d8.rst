.. include:: /common/global.rst

Using Drush with |acquia-product:ch| for Drupal 8
=================================================

|acquia-product:ch| includes several
`Drush <https://www.drupal.org/project/drush>`__ commands for both
normal product use and for more advanced administration. You can use the
commands to administer your content from the command line. For more
information about Drush, see 
`Intro to Drush </articles/drush-intro>`__.

Drush commands
--------------

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Command
     - Description
   * - acquia-contenthub-compare_
     - Compares the CDF of an entity from a local source and a remote source and prints the differences
   * - acquia-contenthub-connect-site_
     - Connects client to |acquia-product:ch|
   * - acquia-contenthub-delete_
     - Deletes a single entity from |acquia-product:ch|
   * - acquia-contenthub-disconnect-site_
     - Disconnect the client from |acquia-product:ch|
   * - acquia-contenthub-list_
     - List content entities that exist in |acquia-product:ch|
   * - acquia-contenthub-local_
     - Prints an entity (in CDF format) from a local source (a Drupal website)
   * - acquia-contenthub-regenerate-secret_
     - Regenerates the shared secret used for webhook verification
   * - acquia-contenthub-remote_
     - Prints an entity (in CDF format) from a remote source (|acquia-product:ch|)
   * - acquia-contenthub-status-check_
     - Checks for stale content by comparing content published on subscribing websites with the original stored in |acquia-product:ch|
   * - acquia-contenthub-update-secret_
     - Updates the shared secret used for webhook verification
   * - acquia-contenthub-webhooks_
     - Perform a webhook management operation
   * - queue-list_
     - General Drush command that returns additional |acquia-product:ch|-related results
   * - queue-run_
     - General Drush command that accepts additional |acquia-product:ch|-related arguments


Advanced Drush commands
-----------------------

The following commands can remove data from |acquia-product:ch|, and
should be used with caution.

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Command
     - Description
   * - acquia-contenthub-logs_
     - View historic entity logs from |acquia-product:ch|
   * - acquia-contenthub-mapping_
     - Display Elastic Search field mappings from |acquia-product:ch|
   * - acquia-contenthub-purge_
     - Delete all entities from |acquia-product:ch| *(available in version 8.x-1.12 or greater)*
   * - acquia-contenthub-reindex_
     - Reindex all entities in |acquia-product:ch|
   * - acquia-contenthub-reset-entities_
     - Delete all entities of a specified type from |acquia-product:ch|, reindex, and then re-export the entities back to |acquia-product:ch|
   * - acquia-contenthub-restore_
     - Restore the backup taken by a previous execution of the ``acquia-contenthub-purge`` command


Troubleshooting Drush commands
------------------------------

If you have enabled |acquia-product:ch|, but Drush commands fail with the message ``Command [commandname] needs the following extension(s) enabled to run: acquia_contenthub``, execute the following commands to attempt to resolve the issue:

``drush en acquia_contenthub -y drush cr``

If Drush commands for |acquia-product:ch| continue to fail, 
`contact Acquia Support </support#contact>`__.

Command details
---------------



``acquia-contenthub-compare``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compares the CDF of an entity from a local source and a remote source
and prints the differences

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ach-comp``                      | ``entity-type``                   |
|                                   | ``uuid`` - The UUID of the entity |
+-----------------------------------+-----------------------------------+

``acquia-contenthub-connect-site``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connects client to |acquia-product:ch|

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| -  ``ach-connect``                | *none*                            |
+-----------------------------------+-----------------------------------+

``acquia-contenthub-delete``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deletes a single entity from |acquia-product:ch|

+-------------+-----------------------------------+
| Alias       | Arguments                         |
+=============+===================================+
| ``ach-del`` | ``UUID`` - The UUID of the entity |
+-------------+-----------------------------------+

``acquia-contenthub-disconnect-site``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disconnect the client from |acquia-product:ch|

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| -  ``ach-disconnect``             | *none*                            |
+-----------------------------------+-----------------------------------+

``acquia-contenthub-logs``
~~~~~~~~~~~~~~~~~~~~~~~~~~

(*Developer only*) - View historic entity logs from |acquia-product:ch|

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Alias
     - Arguments
   * - ``ach-logs``
     - This command takes the following arguments:

       - ``api`` - The |acquia-product:ch| API key
       - ``secret`` - Your secret key

       You can pass an array of options to control the output:

       - ``query`` - The Elastic Search query to search for in the logs; example: ``{"query": {"match_all": {}}}``
       - ``size`` - The number of log entries to be listed
       - ``from`` - The offset to start isting the log entries — used for pagination


``acquia-contenthub-list``
~~~~~~~~~~~~~~~~~~~~~~~~~~

List content entities that exist in |acquia-product:ch|

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ach-list``                      | You can pass an array of options  |
|                                   | to control the output:            |
|                                   |                                   |
|                                   | -  ``limit`` - The number of      |
|                                   |    entities to be listed          |
|                                   | -  ``start`` - The offset to      |
|                                   |    start listing the entities     |
|                                   |    (useful for pagination)        |
|                                   | -  ``origin`` - The client's      |
|                                   |    origin UUID                    |
|                                   | -  ``language`` - Filter entities |
|                                   |    by language — for example,     |
|                                   |    ``en``                         |
|                                   | -  ``attributes`` - The           |
|                                   |    attributes to display for all  |
|                                   |    listed entities                |
|                                   | -  ``type`` - The entity types to |
|                                   |    include                        |
|                                   | -  ``filters`` - Key=value pairs  |
|                                   |    of conditions by which to      |
|                                   |    filter the output, comma       |
|                                   |    separated — for example,       |
|                                   |    ``title=New*, status=1``       |
+-----------------------------------+-----------------------------------+

``acquia-contenthub-local``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prints an entity (in CDF format) from a local source (a Drupal website)

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Alias
     - Arguments
   * - ``ach-lo``
     - 
       * ``entity-type``
       * ``entity-id`` - The UUID of the entity


``acquia-contenthub-mapping``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Shows Elastic Search field mappings for |acquia-product:ch|

+-----------------+-----------+
| Alias           | Arguments |
+=================+===========+
| ``ach-mapping`` | *none*    |
+-----------------+-----------+

``acquia-contenthub-purge``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

(*Developer only*) - Deletes all entities from |acquia-product:ch|

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ach-purge``                     | -  ``api`` - The                  |
|                                   |    |acquia-product:ch| API key    |
|                                   | -  ``secret`` - Your secret key   |
+-----------------------------------+-----------------------------------+

``acquia-contenthub-regenerate-secret``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Regenerates the shared secret used for webhook verification

+----------------+-----------+
| Alias          | Arguments |
+================+===========+
| ``ach-regsec`` | *none*    |
+----------------+-----------+

``acquia-contenthub-reindex``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(*Developer only*) - Reindexes all entities in |acquia-product:ch|

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ach-reindex``                   | -  ``api`` - The                  |
|                                   |    |acquia-product:ch| API key    |
|                                   | -  ``secret`` - Your secret key   |
+-----------------------------------+-----------------------------------+

``acquia-contenthub-remote``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prints an entity (in CDF format) from a remote source (|acquia-product:ch|)

+------------+-----------------------------------+
| Alias      | Arguments                         |
+============+===================================+
| ``ach-re`` | ``uuid`` - The UUID of the entity |
+------------+-----------------------------------+

``acquia-contenthub-reset-entities``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(*Developer only*) - Deletes all entities of a specified type from
|acquia-product:ch|, reindexes, and then re-exports the entities back
to |acquia-product:ch|

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ach-reset``                     | -  ``entity_type`` - The entity   |
|                                   |    type                           |
|                                   | -  ``api`` - The                  |
|                                   |    |acquia-product:ch| API key    |
|                                   | -  ``secret`` - Your secret key   |
+-----------------------------------+-----------------------------------+

``acquia-contenthub-restore``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(*Developer only*) - Restores the backup taken by a previous
execution of the ``purge`` command

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ach-restore``                   | -  ``api`` - The                  |
|                                   |    |acquia-product:ch| API key    |
|                                   | -  ``secret`` - Your secret key   |
+-----------------------------------+-----------------------------------+

``acquia-contenthub-status-check``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Checks for stale content by comparing content published on
subscribing websites with the original stored in |acquia-product:ch|

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ach-st-ch``                     | -  ``limit`` - The amount of      |
|                                   |    previous log events to review  |
|                                   |    for content changes            |
|                                   | -  ``threshold`` - The number of  |
|                                   |    minutes before content is      |
|                                   |    considered stale               |
+-----------------------------------+-----------------------------------+

``acquia-contenthub-update-secret``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Updates the shared secret used for webhook verification

+---------------+-----------+
| Alias         | Arguments |
+===============+===========+
| ``ach-upsec`` | *none*    |
+---------------+-----------+

``acquia-contenthub-webhooks``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perform a webhook management operation

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| -  ``ach-wh``                     | ``op`` - The operation to use:    |
|                                   | ``register``, ``unregister``, or  |
|                                   | ``list``; Requires the            |
|                                   | ``webhook_url`` as an option      |
+-----------------------------------+-----------------------------------+

``queue-list``
~~~~~~~~~~~~~~

This command is not specific to |acquia-product:ch|, but will return
additional results with it. See 
`drush queue-list <https://drushcommands.com/drush-8x/core/queue-list/>`__

+-----------------------------------+-----------------------------------+
| Result                            | Description                       |
+===================================+===================================+
| ``content_hub_webhook_queue``     | The number of items in the        |
|                                   | |acquia-product:ch| webhook       |
|                                   | queue.                            |
+-----------------------------------+-----------------------------------+

``queue-run``
~~~~~~~~~~~~~

This command is not specific to |acquia-product:ch|. See 
`drush queue-run <https://drushcommands.com/drush-8x/core/queue-run/>`__.

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Alias
     - Arguments
   * - ``acquia_contenthub_export_queue``
     - Processes the queue of entities to export_.
   * - ``acquia_contenthub_import_queue``
     - Processes the queue of entities to import_.
   * - ``content_hub_webhook_queue``
     - Processes the remaining |acquia-product:ch| webhook queue.

.. _export: /content-hub/sharing/export
.. _import: /content-hub/sharing/import
