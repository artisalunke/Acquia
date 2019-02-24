.. include:: /common/global.rst

|acquia-product:ch|
===================

.. toctree::
  :hidden:
  :glob:

  /lift/contenthub/service-rns
  /lift/contenthub/client-rns
  /lift/contenthub/install
  /lift/contenthub/sharing
  /lift/contenthub/discover
  /lift/contenthub/modules
  /lift/contenthub/api
  /lift/contenthub/troubleshooting
  /lift/contenthub/*

.. container:: message-status

   |liftlogo| |acquia-product:ch| is a component of `Acquia Lift </lift>`__.

.. |liftlogo| image:: https://cdn4.webdamdb.com/1280_6hBD2tUaE8E2.png?-62169955200
   :class: no-sb logo-sm-lift
   :width: 20px

|chlogo|

.. |chlogo| image:: https://cdn2.webdamdb.com/1280_kOk3CtpKoqV9.png?-62169955200
   :class: float-right
   :width: 61px

|acquia-product:ch| is a cloud-based, centralized content distribution
and syndication solution that provides you with the ability to share and
enrich content throughout a network of content sources (including Drupal
websites) with extensible, open APIs. It is a high-performance, scalable
offering that connects content bi-directionally across multiple systems.
It enables enterprises that operate many digital properties the ability
to effectively publish, reuse, and syndicate content across a variety of
content sources and publishing channels.

.. container:: message-status

   **QUICK LINKS:**   
   `Install </content-hub/install>`__  |  
   `Share </content-hub/sharing>`__  |  
   `Discover </content-hub/discover>`__  |  
   `Known issues </lift/known-issues>`__


.. container:: message-status

   **RELEASE NOTES:**   
   `Service </content-hub/service/release-notes>`__  |  
   `Clients for Drupal 7 and 8 </content-hub/client/release-notes>`__

How |acquia-product:ch| works
-----------------------------

|acquia-product:ch| creates a content interchange workflow between the
different websites in your content network. Each of the websites in your
content network can be both a publisher and a subscriber for content,
communicating through the |acquia-product:ch| service. You use
|acquia-product:ch| to establish rules for how and when content gets
shared between different members of the content network.

|acquia-product:ch| enables automated subscription updates from content
authors to content consumers in near real time, respecting local changes
and workflow rules. Publishers create content on their websites just
like normal. If a new content item is one of the entity types that get
shared, then it becomes available to subscriber websites to import.
Subscribers can create filters that specify what sorts of content items
they are interested in. They also establish rules about whether content
items are imported automatically or manually.

|acquia-product:ch| architecture
--------------------------------

|charchitecture|

.. |charchitecture| image:: https://cdn2.webdamdb.com/1280_sLADAfjL5D52.png?1527198504
   :class: no-sb

A website in a |acquia-product:ch| network can act as a publisher for
some content and a subscriber for some other content. The original
publisher of a content entity controls the definitive content of the
entity, and any changes made by a subscriber website that imported the
content entity are not contributed back into the |acquia-product:ch|.

|publishing|

.. |publishing| image:: https://cdn4.webdamdb.com/1280_YKTdMNvSHNC0.png?-62169955200
   :width: 760px
   :height: 378px

The main elements provided by |acquia-product:ch| are as follows:

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Element
     - Description
   * - |acquia-product:ch|
     - A central content repository hosted and managed by Acquia. Using a central hub for your content enables full-text and faceted search across all the available content.
   * - |acquia-product:ch| client
     - A set of Drupal modules that manage communication with the |acquia-product:ch| and help you manage how content is published and consumed. The |acquia-product:ch| client gets installed on each website in the content network that wants to publish or subscribe to content, or both.
   * - |acquia-product:ch| API
     - A set of `open RESTful APIs </content-hub/api>`__ you can use to interact directly with content inside or outside Drupal websites.
   * - |acquia-product:ch| SDK for PHP
     - A `software development kit (SDK) </content-hub/api#libs>`__ for the Content Hub API.


Getting started with |acquia-product:ch|
----------------------------------------

The following documentation pages contain information that you can use
to install and use |acquia-product:ch| with your websites:

-  |installing|_
-  `Sharing content </content-hub/sharing>`__
-  `Discovering content </content-hub/discover>`__
-  |usedrush|_

.. |installing| replace:: Installing the  \ |acquia-product:ch|\  client
.. _installing: /content-hub/install


.. |usedrush| replace:: Using Drush with  \ |acquia-product:ch|\ 
.. _usedrush: /content-hub/drush-d8