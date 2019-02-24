.. include:: /common/global.rst

Sharing content
===============

.. toctree::
   :hidden:
   :glob:

   /lift/contenthub/sharing/*

|acquia-product:ch| enables each website in a content network to publish
content to the central repository, from which other websites can import
the content. A website in a content network can act as a *publisher* for
some content and a *subscriber* for other content. The original
publisher of a content entity controls the definitive content of the
entity, and any changes made by a subscriber website that imported the
content entity are not contributed back into |acquia-product:ch|. The
|acquia-product:ch| API enables client applications to act directly on
|acquia-product:ch|, creating, modifying, and deleting content entities.

.. container:: message-status

   |Learning Services logo|\ For a step-by-step video tutorial introducing you to personalization with |acquia-product:cha|, including content, see |tutorial|_.

.. |Learning Services logo| image:: https://cdn3.webdamdb.com/1280_w1WjsvuWixS1.png?-62169955200
   :class: no-sb float-left logo-sm-lift
   :width: 36px

.. |tutorial| replace:: Creating Personalized Experiences with  \ |acquia-product:cha|\ 
.. _tutorial: /tutorials/creating-personalized-experiences-acquia-lift


What can be shared?
-------------------

|acquia-product:ch| supports sharing of
`entities <https://www.drupal.org/node/1261744>`__, such as nodes and
taxonomies. The hub is concerned with the sharing of content. It is
possible to share taxonomy terms, additional layout elements (including
`blocks <#blocks>`__ and panels), or configuration information (such as
field configuration) with |acquia-product:ch|.

|acquia-product:ch| and its Drupal modules do not currently support
every entity or use case. Some contributed modules implement entities
that are compatible with |acquia-product:ch|, including the following:

-  `Paragraphs <https://www.drupal.org/project/paragraphs>`__
-  `Field Collections <https://www.drupal.org/project/field_collection>`__

For specific configuration information, see `Modules to use </content-hub/modules>`__ 
with |acquia-product:ch| .

.. important::

   Fields that are shared across publishers and subscribers must share the same attributes, such as type or size. If this is not the case, content may not import correctly.

To ensure the data from your production environment is not corrupted by
data from non-production environments, configure 
`per-environment settings </lift/drupal/3/install#env>`__.

Configuring shared content entities in the |acquia-product:ch| client
---------------------------------------------------------------------

To share content from your website to other members of your content
network, you need to configure which entity types you want to make
available for sharing. You can configure this in the Drupal
administration page for the |acquia-product:ch| client.

#. In the admin menu, go to **Configuration > Content Hub Connector**,
   and then click the **Entity Configuration** tab.
#. Select the entity types that you want to make available for sharing.
   All entities of these types will be shared through the
   |acquia-product:ch| and made available to all the other members of
   your |acquia-product:ch| network. You can choose not to share
   specific properties of a shared entity type. See `Excluded
   properties </content-hub/configure/connector>`__.
#. Ensure that you have selected at least one view mode for every
   content type that you want to publish. |acquia-product:cha| can
   import nodes from |acquia-product:ch| for both Drupal 7 and Drupal 8.

   |Select a view mode|

   .. important::
   
        If your entity type contains entity references (such as a ``blog`` entity type containing references to ``media`` or ``file`` entities), for the referenced content to be available for display with the ``blog`` entity type, the referenced entities must also be shared with |acquia-product:ch|. The field for the entity reference must specify a bundle, and that bundle must also contain at least one view mode.

        If the entity reference was created before configuring |acquia-product:ch|, ensure that the referenced entities are syndicated to |acquia-product:ch| before referencing them in other entities — failing to do so will cause them to not be displayed.

#. In the **User Role** list, click a role to determine how the content
   type will be rendered. |acquia-product:ch| will use the permissions
   of the selected role for both displayed content and `generated CDF
   data </content-hub/cdf>`__.
   In many cases, the **Anonymous user** default option is fine.
   However, if applicable, be sure to select the proper role to ensure
   that subscribing websites do not receive sensitive data.
#. Click **Save configuration**.

`View modes <https://www.drupal.org/node/1577752>`__ determine the way a
piece of content is displayed. Drupal has several built-in view modes,
and others may be added by users. Drupal 8 makes use of these view modes
to enable users to more easily control their content across multiple
websites. If you change the publishing website's view mode
configuration, you must resync your content between your website and
|acquia-product:ch|.

To resync your content, complete the following steps:

#. Go to **Content > Content Hub**.
#. In the **Keyword** field, enter the type of content you changed, such
   as ``article``.
#. Select the checkbox next to **Import to site** to select all content.
#. Click **Import to site**.

For information about custom blocks and view modes, see |useblocks|_.


.. |useblocks| replace:: Using blocks with  \ |acquia-product:ch|\ 
.. _useblocks: /content-hub/sharing/blocks

Which entities are shared
~~~~~~~~~~~~~~~~~~~~~~~~~

To be shared, an entity type must exist on both the publisher (source)
website and the subscriber (target or consumer) website. The entity type
does not need to be defined with exactly the same fields. Fields in
shared entities that don't exist on the subscriber website will be
ignored.

Taxonomy term sharing
~~~~~~~~~~~~~~~~~~~~~

To be shared, taxonomy vocabularies must exist on both the publisher
(source) website and the subscriber (target or consumer) website.
Taxonomy terms will be syndicated with the entities that they are
attached to. If a taxonomy term exists on the subscribing website and
has the same UUID as the publishing website, the term will be used on
the subscribing website. If the vocabulary exists on both websites but
the term does not—or the UUIDs do not match—the term will be added to
the subscribing website, potentially resulting in term duplication.

Block sharing
~~~~~~~~~~~~~

Because blocks are not entities in Drupal 7, the Content Hub Blocks
module for Drupal 7 (included with |acquia-product:ch|) must be enabled
to share blocks. This module allows Drupal 7 blocks to be pushed to
|acquia-product:ch| as rendered content entities. These rendered
entities are only available to be used for personalization and cannot be
syndicated.

.. note::

   Blocks and entities created with the Drupal 7 Bean_ module are fully supported for content syndication and personalization.

.. _Bean: https://www.drupal.org/project/bean

To enable this module, complete the following steps:

#. Sign in to your website as an administrator, and in the admin menu,
   click **Modules**.
#. Select the check box for the **|acquia-product:ch| for Blocks**
   module.
#. Scroll to the end of the webpage, and then click **Save
   configuration**.
#. In the admin menu, go to **Configuration > Content Hub Connector**,
   and then click the **Entity Configuration** tab
#. Select the block content types that you want to make available for
   sharing.
#. Click **Save configuration**.

After enabling the module, a **Publish to Content Hub** check box will
appear on the block editing page. The enabled module also provides the
following Drush command to export blocks by block ID:

.. code-block:: none

   drush -l [URI] ch-export-block [blockID]

Configuring webhooks
--------------------

To receive content from other members of your content network, you need
to set up `webhooks <https://en.wikipedia.org/wiki/Webhook>`__ on your
website. To do this, complete the following steps:

#. In the admin menu, go to **Configuration > Content Hub Connector**,
   and then click the **Webhooks** tab.
#. Enter the webhook URL. The default webhook URL is:

   .. code-block:: none

        http://[site_URL]/content-hub/webhook

#. Click **Save configuration**.

.. note::

   Because the IP addresses used by the |acquia-product:ch| service can change frequently, it is not practical to use a whitelist to enable connection between your website and |acquia-product:ch|.

|acquia-product:ch| requires a valid SSL certificate on the domain if
you want your webhooks to transfer data with a SSL connection. If you
want to use |acquia-product:ch| with an invalid SSL certificate during
your development phase, you must use ``http://`` URLs on pages that
trigger content exports (such as node editing forms) and ensure that
your webhook URL is a non-SSL URL in your webhook settings form.

Deleting content using webhooks
-------------------------------

When content is unpublished or deleted from your publishing website, you
may also want to remove the content from your subscribing websites. To
do this, create a small, custom module, as described in |deleting|_.

.. |deleting| replace:: Deleting content from  \ |acquia-product:ch|\ 
.. _deleting: /content-hub/sharing/delete

Troubleshooting webhooks
------------------------

If |acquia-product:ch| cannot send webhooks to a subscribing website, it
also cannot notify the subscribing website of a problem with the
webhook. If a webhook fails for four days, |acquia-product:ch| will
remove the webhook and then add the following error message to the
history log regarding the failure:

.. code-block:: none

   A webhook endpoint has been automatically removed, because webhook delivery has failed to that URL for a long time (URL: [URL to endpoint])

To review the history logs for |acquia-product:ch|, use |historyendpoint|_. For
more information, see `Using the Content Hub API </content-hub/api>`__.

.. |historyendpoint| replace:: the ``/v1/history`` API endpoint
.. _historyendpoint: http://api.content-hub.acquia.com/#v1_history_get

Removing and reindexing by content type
---------------------------------------

If you alter content types on a subscribing website, and want
|acquia-product:ch| to use the new or altered fields in your content
type, you can use ``drush ach-reset`` to 
`remove, reset, reindex, and reimport </content-hub/sharing/reset>`__ all entities matching the content type you specify.

.. |Select a view mode| image:: https://cdn2.webdamdb.com/1280_UHl4FK63X8C0.png?-62169955200
   :width: 598px
   :height: 576px
