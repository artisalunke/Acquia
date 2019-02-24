.. include:: /common/global.rst

Workbench Moderation integration
================================

|acquia-product:ch| integrates with the 
`Workbench Moderation <https://www.drupal.org/project/workbench_moderation>`__
module, enabling users to publish content to the hub in various
moderation states.

Basic configuration
-------------------

After you install and enable the Workbench Moderation module on your
website, a new **Workbench moderation settings** tab is available to
|acquia-product:ch| users. To configure these settings, complete the
following steps:

#. As an administrator, go to **Configuration > Content Hub connector >
   Workbench moderation settings**.
#. Select one or more checkboxes for **Publishable moderation states**.

   |Content Hub Workbench Moderation settings|

#. Click **Submit**.

.. |Content Hub Workbench Moderation settings| image:: https://cdn2.webdamdb.com/1280_2tZOTmu4t0Q2.png?1526475674

When new content is created, and the **Moderation state** matches a
state that can be posted to the hub, the content will be sent. This
content is not available to external Drupal users until its moderation
state is **Published**.

You can create additional states for Workbench moderation under
**Configuration > Workbench Moderation**. See the `module
documentation <https://www.drupal.org/documentation/modules/workbench_moderation>`__.

When you create a new moderation state, you will need to configure
|acquia-product:ch| to use that state before content using that state
will be published to the hub.

Additional options
------------------

Workbench moderation and |acquia-product:ch| can interact in several
ways, depending on how Workbench Moderation is configured. When content
is initially imported, it is either in the **Unpublished** or **Draft**
state. The default state is set by content type on the publishing
website. Content always exports to the subscribing websites in the
default state, even if the content itself is published on the origin.

When using Workbench Moderation with |acquia-product:ch|, content can
behave in the following manners on the subscribing website:

-  *Automatic updates* - A new, draft revision is created of the content
   if there is no published version, even if the subscriber's current
   content is in a different state. For example, if revision 1 is in
   ``Needs review``, revision 2 is created in the default state.
-  *Published revisions* - When a subscriber edits, you are editing the
   latest revision — the publishing website can send a new revision,
   which also goes into draft. Updates from the origin do not affect the
   published revision; the updates will be in default state. Users must
   make the changes to publish the new revision. Without Workbench
   Moderation, the revisions publish and overwrite the current content.
-  *Changing information on the subscriber* - Content that is edited on
   the subscriber website will be de-linked from the Hub and will not
   receive further updates from the origin website. Content will go from
   the origin to the Hub, but not to subscribers. To continue receiving
   updates and enable subscriber websites to both edit and obtain new
   versions, on the content's **Edit** page, select the **Allow the
   content to be overwritten** check box.
-  *Filters* - `Filters can contain
   actions </content-hub/discover/manage>`__. Workbench states will
   always take precedence, regardless of your filter's settings.
   Depending on your configuration, your content can end up in one of
   the following states on the subscribing application:

   +-----------------------------------+-----------------------------------+
   | Revision or action                | Result                            |
   +===================================+===================================+
   | No published revision             | A new revision in the default     |
   |                                   | state                             |
   +-----------------------------------+-----------------------------------+
   | A published revision              | Unchanged published revision,     |
   |                                   | with a new revision in the        |
   |                                   | default state and:                |
   |                                   |                                   |
   |                                   | -  *On local change* - content is |
   |                                   |    de-linked and no longer        |
   |                                   |    receives updates               |
   |                                   | -  *On re-sync* - the latest      |
   |                                   |    revision is imported in the    |
   |                                   |    default state and receives     |
   |                                   |    updates                        |
   +-----------------------------------+-----------------------------------+
   | Content is set to always import   | Initial import in the default     |
   |                                   | state                             |
   +-----------------------------------+-----------------------------------+
   | Content is set to always publish  | Workbench state takes precedence, |
   |                                   | application keeps the published   |
   |                                   | revision and receives a new       |
   |                                   | revision in the default state     |
   +-----------------------------------+-----------------------------------+


