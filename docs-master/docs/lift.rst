.. include:: /common/global.rst

|acquia-product:cha|
====================

.. toctree::
  :hidden:
  :glob:

  /lift/release-notes/
  /lift/known-issues/
  /lift/exp-builder/
  /lift/profile-mgr/
  /lift/contenthub/
  /lift/arch/
  /lift/glossary/
  /lift/omni/
  /lift/connectors/
  /lift/api/
  /lift/*

|Acquia Lift logo|

.. |Acquia Lift logo| image:: https://cdn4.webdamdb.com/1280_6hBD2tUaE8E2.png?-62169955200
   :class: float-right
   :width: 61px

|prodguidelink|_ lets you track customers' behavior throughout their buying journey—from anonymous visitor to loyal, repeat customer. Acquia Lift unifies customer content and profile data from multiple sources to deliver in-context, personalized experiences across any channel or device.

.. |prodguidelink| replace:: \ |acquia-product:cha|\ 
.. _prodguidelink: https://www.acquia.com/products-services/acquia-lift


.. _packages:

Available packages
------------------

|acquia-product:cha| has several packages from which you can choose to
personalize your content for customers, including the following:

.. list-table::
   :widths: 28 18 18 18 18
   :header-rows: 1

   * - Package
     - |lebheader|_
     - |lpmheader|_
     - |chheader|_
     - |ldbheader|
   * - |acquia-product:lpls|
     - |yes|
     - |yes|
     - |yes|
     - |no|
   * - |acquia-product:lplp|
     - |yes|
     - |yes|
     - |yes|
     - |yes|
   * - |acquia-product:lplpw|
     - (non-production only)
     - |yes|
     - (non-production only)
     - |no|
   * - |acquia-product:lplpo|
     - (non-production only)
     - |yes|
     - (non-production only)
     - |no|

.. |lebheader| replace:: \ |acquia-product:leb|\ 
.. _lebheader: /lift/exp-builder
.. |lpmheader| replace:: \ |acquia-product:lpm|\ 
.. _lpmheader: /lift/profile-mgr
.. |chheader| replace:: \ |acquia-product:ch|\ 
.. _chheader: /content-hub
.. |ldbheader| replace:: \ |acquia-product:ldb|\ 
.. _ldbheader: /lift/omni

.. _components:

Product components
------------------

|acquia-product:cha| includes the following components to help you
better engage with your website visitors:


-  |leb2|_

   |leblogo|\ Instead of having to use a separate
   application with its own interface and API to target content to your
   customers, |acquia-product:cha| features a collection of modules that
   integrates tightly with Drupal, allowing you to leverage the Drupal
   skills and knowledge you've developed from maintaining your website.
   Using these modules, you can `create
   personalizations </lift/exp-builder/slots>`__ that target your
   website's content to the segments you create using
   |acquia-product:lpm|, even if some of your websites aren't using
   Drupal.

-  |lpm2|_

   |lpmlogo|\ As a cloud-based application separate
   from your website, |acquia-product:lpm| lets you search for and
   categorize data about each of your visitors, based on customizable
   criteria such as location or the content type the visitor has viewed
   most frequently. |acquia-product:lpm| allows you to `organize this
   data into segments </lift/profile-mgr/segment>`__, or groups of
   criteria that visitors often have in common. For example, if your
   website specializes in vacation packages, a visitor who clicks on a
   skiing vacation might fit into a predefined *Sports Enthusiast*
   segment. You can also create JavaScript-based
   `slots </lift/exp-builder/slots>`__, or customizable placeholders, on
   your website to drag and drop customized content that can target
   those specific users.

-  |ch2|_

   |chlogo|\ |acquia-product:ch| is a cloud-based,
   centralized content distribution and syndication solution that
   provides you with the ability to share and enrich content throughout
   a network of content sources (including Drupal websites) with
   extensible, open APIs. It is a high-performance, scalable offering
   that connects content bidirectionally across multiple systems. It
   enables enterprises that operate many digital properties to
   effectively publish, reuse, and syndicate content across a variety of
   content sources and publishing channels.

.. |leb2| replace:: \ |acquia-product:leb|\ 
.. _leb2: /lift/exp-builder
.. |lpm2| replace:: \ |acquia-product:lpm|\ 
.. _lpm2: /lift/profile-mgr
.. |ch2| replace:: \ |acquia-product:ch|\ 
.. _ch2: /content-hub

.. |leblogo| image:: https://cdn4.webdamdb.com/1280_nTktEC8kDo19.png?1526476097
   :class: float-right
   :width: 40px

.. |lpmlogo| image:: https://cdn3.webdamdb.com/1280_c6X7m3brFd91.png?1526475558
   :class: float-right
   :width: 40px

.. |chlogo| image:: https://cdn2.webdamdb.com/1280_kOk3CtpKoqV9.png?-62169955200
   :class: float-right
   :width: 40px

.. _features:

Additional features
-------------------

Depending on the |acquia-product:cha| package that you select, you can
also access the |acquia-product:ldb| functionality, which provides the
following features:

-  |warehouse|_ – Using this feature, you can
   integrate data from other systems (such as marketing automation or
   CRM) into |acquia-product:cha| profiles by using a dedicated
   connection to `Amazon Redshift <https://aws.amazon.com/redshift/>`__.
   This cloud-based data warehouse contains all of your
   |acquia-product:cha|-hosted visitor data, and with this direct
   access, you can use your own business intelligence tools to analyze
   your website visitors and discover new insights.
-  |apis|_ – |acquia-product:ldb| includes access
   to several |acquia-product:cha| APIs that you can use to exchange
   your visitor data with other systems.
-  **Optional additional connectors** – An |acquia-product:ldb|
   subscription enables you to connect to other systems that contain
   user and sales information. Currently, |acquia-product:cha|
   officially supports the `Marketo </lift/connectors/marketo>`__
   connector.

.. |warehouse| replace:: **Data warehouse**
.. _warehouse: /lift/omni
.. |apis| replace:: **APIs**
.. _apis: /lift/omni/api

.. _browser:

Browser requirements
--------------------

|acquia-product:cha| supports the current and prior major releases of
the Chrome, Firefox, Internet Explorer, and Safari web browsers for
capturing visitor data and displaying personalized content. The
|acquia-product:leb| administrative sidebar is supported for Chrome and
Firefox.