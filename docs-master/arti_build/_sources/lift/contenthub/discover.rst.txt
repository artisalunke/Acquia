.. include:: /common/global.rst

Discovering content
===================

.. toctree::
   :hidden:
   :glob:

   /lift/contenthub/discover/*

After you `install </content-hub/install>`__ and
`configure </content-hub/configure>`__ |acquia-product:ch| for your
websites and `content sharing is enabled </content-hub/sharing>`__, you
can use |acquia-product:ch| to discover content to add to your website.

To discover your websites' shared content, in your website's admin menu
go to **Content > Acquia Content Hub**
(``/admin/content/acquia-contenthub`` or
``http://[site_URL]/admin/content/content-hub``).

.. note::  |acquia-product:ch| will only synchronize entities that were saved 
  after |acquia-product:ch| was enabled. After synchronization of an entity type 
  is enabled in the `configuration settings </content-hub/sharing>`__, 
  |acquia-product:ch| will react to saved changes for entities of that type.

|Hub filter page|

.. |Hub filter page| image:: https://cdn3.webdamdb.com/1280_3IE62B0Gc67.png?-62169955200
   :width: 750px
   :height: 288px

Filtering content
-----------------

By default, the **Acquia Content Hub** tab displays all of the content
entities that all members of your content network have uploaded in
|acquia-product:ch|, in chronological order from newest to oldest. You
can use filters to limit which items are displayed, helping you discover
the items in which you are most interested.

To create a filter, select one or more of the following filter criteria:

-  **Keyword** - |acquia-product:ch| searches with this string against
   each field in each shared entity.
-  **Date** - You can filter by only a start date (content created on or
   after that date), only an end date (content created on or before that
   date), or both.
-  **Source** - One or more members of your content network. Only
   content from those sources will be included in the results.
-  **Tags** - Filter by one or more tags on your content.
-  **Type** - Filter by one or more content types.
-  **Bundle** - Filter by one or more bundles from entities,
   vocabularies, and blocks. For information about bundles, see
   `Bundles <https://www.drupal.org/docs/8/api/entity-api/bundles>`__ on
   Drupal.org.

|acquia-product:ch| displays all of the available content entities that
match the filter facets.

The following video details the |acquia-product:ch| search and filter
functionality:

.. raw:: html

   <iframe width="750" height="422" src="https://www.youtube.com/embed/7tmvwmgFOzg" frameborder="0" allowfullscreen></iframe>


You may also sort the available content by selecting an option from the
**Sort by** menu:

-  Newest
-  Oldest
-  Relevance

Saving filters and publish settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click **Save Filter** to save a filter to use later. When you save a
filter, you can enter a name to help you identify it. You can select a
saved filter in the left panel.

When you use a saved filter, you can configure its publish settings.
Select one of the following:

-  **None** - No entities are automatically imported or published. To
   publish an entity, you can visit the filter page from time to time
   when you need content and pick individual entities to publish.
-  **Auto Import** - Every entity that matches the filter is
   automatically imported to your website, but left in unpublished
   state. You can review each entity and decide whether to publish it or
   not.
-  **Auto Publish** - Every entity that matches the filter is
   automatically imported to your website and immediately published.

Managing your saved filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you save a filter, you can update it or delete it at a later time.
To update or delete a filter, see 
`Managing filters </content-hub/discover/manage>`__.

Importing content
-----------------

Each content item displayed on the **Content > Content Hub** tab can be
imported to your website. Select the content items you want, then click
**Import**. Items that you have already imported are displayed in the
filter list and marked as **Imported to site**.

If there is no content to be imported, the website will display a
``No content is available for import.`` message.

If there is more than one page of available content, a pager will
display at the bottom of the page.

Imported items will sometimes bring all dependent items with them during
the import process. This includes images and files. If items are not
imported, they will include a reference to the original.

When using the 
`Workbench Moderation <https://www.drupal.org/project/workbench_moderation>`__
module, some content may not be available for import. If your content
type is defined using Workbench Moderation, and defaults to the
``Draft`` state, you may not always see all the content you expect. If
you are importing content onto a website using Workbench Moderation, and
that website uses the ``Draft`` state by default, you will then need to
process the imported content.

For information about using canonical URLs to improve your websites' SEO
(search engine optimization), see |seometadata|_.

.. |seometadata| replace:: SEO and social publishing metadata with  \ |acquia-product:ch|\ 
.. _seometadata: /content-hub/seo

Updating content
~~~~~~~~~~~~~~~~

|acquia-product:ch| can help you keep content synchronized, so that if a
content entity is updated by its original publisher, you can ensure that
the updated version is available on all of the other websites that may
have imported it.

Automatic updates property
~~~~~~~~~~~~~~~~~~~~~~~~~~

When |acquia-product:ch| imports a content entity, the entity includes a
**Enable Automatic Updates** setting. By default, this setting's check
box is selected, which means that updates to the content by the original
publisher are pushed to the consuming website.

|Enable automatic updates property setting|

If you disable automatic updates for a content entity,
|acquia-product:ch| will not push updates to your website from the
original publisher.

Exactly how content updating works depends on several settings in
addition to the automatic updates property:

-  Does the content type have *revisions* enabled?
-  Is the content entity marked as *published* on the consuming website?

.. list-table::
   :widths: 10 10 80
   :header-rows: 1 

   * - Revisions?
     - Published?
     - When content is updated by the publisher...
   * - |no|
     - |yes|
     - The content is immediately updated on the consuming website.
   * - |no|
     - |no|
     - The content is immediately updated on the consuming website and remains not published.
   * - |yes|
     - |yes|
     - The updated content is immediately published as a new revision on the consuming website and the previous version is saved as an old revision.
   * - |yes|
     - |no|
     - The updated content is a new unpublished revision on the consuming website and the previous version is saved as an old revision.


Re-enabling updates
~~~~~~~~~~~~~~~~~~~

If you disable automatic updates for an entity, the entity will stop
receiving changes from the upstream content. Automatic updates can be
re-enabled at any time. If the Diff_ module is enabled on your
website, when automatic updates are re-enabled you have the option to
both review and potentially discard the upstream changes before saving
the automatic updates.

.. _Diff: https://www.drupal.org/project/diff

Deleting content
----------------

If a content entity is deleted by the publishing website, by default,
that action has no effect on the entity on the consuming website. Only
changes to the existing text (and not the removal of the entity) will
result in updates to the consuming website. Although the originating
website sends a webhook to inform subscribers that the content was
removed, the content will remain on the subscriber websites unless you
implement a custom module to delete the content (as described in
`Deleting content from subscribing sites </content-hub/sharing/delete>`__).

After you have imported a content entity to your website, it has the
same status as any other content entity of the same entity type on your
website — you can modify it, publish or unpublish it, or delete it. Any
actions that you take on the content entity have no effect on the item
on the source website, or on any other member of your content network
that may have already imported the content entity or might import it in
the future. If no local changes have been made to an imported entity on
a subscribing website, the imported entity will be updated if the
original publisher website pushes a new version of the content. However,
if local changes have been made to the imported entity, a content update
made on the original publisher website will not update the imported
entity unless the **Enable Automatic Updates** check box has been
selected.

Developers can write applications to watch for ``delete`` requests.
These webhook notifications are tracked in the watchdog log. For
example:

.. code-block:: none

   Webhook landing: @"uuid":"47c937d3-1504-46e6-6b68-a654620a279c",
   "status":"successful","crud":"delete","assets":
   [{"uuid":"23377268-4bb6-49db-97ff-bb024b82cde8","type":"node"],
   "endpoint":"http://mytestsite.acquia.com/acquia-contenthub/webhook",
   "initiator":"163ef3342-d2c2-49d9-5716-d25fc02ec7ac",...


Retries
-------

If a publisher or subscriber website is down during synchronization,
|acquia-product:ch| will retry over time to complete the process. It
uses a backoff strategy similar to what is described 
`by Amazon <https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html>`__.

|acquia-product:ch| will continue to retry sending content at the
following predefined intervals:

-  Initial attempt (0:00)
-  One minute after the initial attempt (0:01)
-  15 minutes after the previous attempt (0:16)
-  One hour after the previous attempt (1:16)
-  Four hours after the previous attempt (5:16)
-  12 hours after the previous attempt (17:16)

If the webhook cannot be successfully delivered (a ``HTTP 200`` response
from Drupal), |acquia-product:ch| will unregister the webhook of your
website after 48 hours.


.. |Enable automatic updates property setting| image:: https://cdn2.webdamdb.com/1280_gckNBeJNHk44.png?-62169955200
   :width: 590px
   :height: 209px