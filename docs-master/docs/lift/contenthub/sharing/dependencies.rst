.. include:: /common/global.rst

Working with content dependencies
=================================

Drupal content can contain dependencies, such as node references, which
rely on other content. |acquia-product:ch| is capable of exporting
content to the central hub, and including all of the dependent content.
This includes websites with complex, nested, highly interdependent
content.

When sharing content with |acquia-product:ch|, be aware of what content
may be related to it. Each of those entities must also be examined for
content they are related to. However, with some complex data
relationships, the data may not have room to fit within the memory
footprint allowed by the server.

For example: your website may have content related to a particular
office. That office may have relationships with all of the members of
the office. Those members can have relationships with their workgroups,
which may have relationships with other offices.

If all of your content is related to each other, you can export your
entire website to |acquia-product:ch| each time a piece of content is
updated. This changes a minor update into a potentially large set of
requests being sent to |acquia-product:ch|, and has the potential to
cause serious performance issues for your website.

To prevent these types of occurrences, |acquia-product:ch| takes
precautionary steps. Users can create their own queue using Drupal's
`Queue
operations <https://api.drupal.org/api/drupal/modules%21system%21system.queue.inc/group/queue/7.x>`__
system (or another queue system of your choice), and then
|acquia-product:ch| can use that queue to help limit the amount of data
processed on both the subscriber and publisher websites.

.. _content-dependency-table:

+-----------------------+-----------------------+-----------------------+
| Concept               | Definition            | Default value         |
+=======================+=======================+=======================+
| Depth                 | The number of         | 30                    |
|                       | dependency levels     |                       |
|                       | that will be checked  |                       |
+-----------------------+-----------------------+-----------------------+
| Load                  | The number of         | 500                   |
|                       | dependencies to load  |                       |
+-----------------------+-----------------------+-----------------------+
| Send/Receive          | The number of         | 500                   |
|                       | dependent entities    |                       |
|                       | that will be          |                       |
|                       | sent/received         |                       |
+-----------------------+-----------------------+-----------------------+

In Drupal 7, deferred entities are available to other modules for custom
processing by using the following hooks:

-  ``hook_content_hub_webhook_get_unprocessed_entities()``
-  ``hook_content_hub_connector_defer_entities()``
-  ``hook_content_hub_connector_defer_entities_import()``


Setting limits for export
-------------------------

When preparing to publish content, |acquia-product:ch| reviews both the
number of nodes and how many levels of referenced content will be sent.
This content is then processed, and any remaining content is sent to the
queue. Variable names are dependent on your Drupal version, and are
described as follows:

-  | *Drupal 8*
   | Drupal 8 has a single parameter to limit exported dependencies. The
     ``dependency_depth`` parameter limits the level of dependencies
     that are evaluated, but does not limit the actual number of
     exported items. This parameter can be also set by using Drush.

   ``drush config-set acquia_contenthub.entity_config dependency_depth 3``

   This example sets the value to ``3`` (which is the default), and
   indicates that exporting collects entities on the first three level
   of dependencies.

-  | *Drupal 7*
   | The following variables can be set for export:

   -  Depth - ``content_hub_connector_max_dep_depth``
   -  Load - ``content_hub_connector_max_dep_load``
   -  Send - ``content_hub_connector_max_dep_send``
   -  ``cache_exported`` - ``FALSE`` - When ``TRUE``, this tracks which
      items that have changed, and does not send unchanged items. This
      feature is still under development.

   | Based on the default values for these variables,
     |acquia-product:ch| will initially evaluate up to 30 levels of
     dependent content, and then load and send up to 500 items to the
     Hub.
   | If |acquia-product:ch| reaches the limits of what it can send, it
     displays the following warning message:

   ``Content dependency limits were reached. Not all dependencies were submitted to Content Hub.``

   A message will also be recorded in the status report (**Reports >
   Status report**), from ``content_hub_connector``, which states how
   many items were sent to the queue, and will look similar to the
   following message:

   ``entity limit enforced: X not charted, Y not loaded, Z not sent``

   | where ``X``, ``Y``, and ``Z`` are the number of items not
     processed.
   | The queue will process during normal Drupal cron runs.

Setting limits for import
-------------------------

When importing content from |acquia-product:ch|, the amount of
discovered and imported content also faces limitations based on
dependency levels.

Variable names on the subscribing website:

-  Load -
   ``content_hub_connector_max_entities_webhook_request``
-  Depth - ``content_hub_connector_max_dep_depth_import`` -
   limits how many levels of dependent content will be imported
-  Send/Receive - ``content_hub_connector_max_dep_receive``

You can `use Drush </content-hub/drush>`__ to check the import queue
variable values and status, which returns these items and their current
values:

-  Load - ``max dependencies``
-  Depth - ``max dependency gap``
-  Send/Receive - ``max items``


Queuing for publishing
----------------------

|acquia-product:ch|, by default, uses Drupal's queueing system. When the
system detects that an update needs to be sent to the central hub, it
analyzes the number of changes that will be processed. It then sends the
first batch of content to the hub, and adds the remainder of the content
to the queue for processing. Normally this processing completes in under
five minutes.

If you have your own queuing solution, it is possible to use that
solution in place of what |acquia-product:ch| provides.
