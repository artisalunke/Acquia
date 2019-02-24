.. include:: /common/global.rst

Using |acquia-product:leb| with a non-Drupal website
====================================================

.. container:: internal-navigation

   **Installing Experience Builder**

   * :doc:`Install </lift/exp-builder/install>`
   * :doc:`Access </lift/exp-builder/access>`
   * :doc:`Content </lift/exp-builder/content-hub>`

The |acquia-product:leb| can be added to any website, regardless of what
content management service it uses, by configuring several environment
variables and including a link to the ``lift.js`` script.


Requirements
------------

As you are preparing to use |acquia-product:leb| with your website, be
sure to plan for the following requirements:

+-----------------------------------+-----------------------------------+
| Component                         | Requirement                       |
+===================================+===================================+
| **Keys**                          | After you purchase                |
|                                   | |acquia-product:cha|, Acquia will |
|                                   | email you a set of keys which are |
|                                   | required to connect to the        |
|                                   | |acquia-product:leb| service.     |
+-----------------------------------+-----------------------------------+


Installing |acquia-product:leb|
-------------------------------

The JavaScript code in the following link should be called as early in the page's ``<head>`` section as possible, enabling |acquia-product:cha| to make the appropriate calls during the rendering process. After this code is in place on your website, you can use the |acquia-product:cha| bookmark_ tool to help you `get started </lift/exp-builder/slots>`__ with adding more content to your website.

|visit|_

.. |visit| replace:: Visit the ``lift.js`` source webpage.
.. _visit: https://gist.github.com/acquialibrary/c6bdcc4e54008a706e382005ab9d319e/

.. _bookmark: /lift/exp-builder/access


.. list-table::
   :widths: 30 30 40
   :header-rows: 1 

   * - Variable name
     - Example value
     - Definition
   * - account_id
     - 
     - Your Acquia Lift account id (Required)
   * - site_id
     - 
     - Acquia Lift site ID to use for segments and capture data *(Required)*
   * - liftAssetsURL
     - ``https://liftasseturl.acquia.com``
     - Where to load additional administrative assets
   * - liftDecisionAPIURL
     - ``https://region.lift.acquia.com``
     - The base url for the decision API
   * - authEndpoint
     - ``https://region-oauth2.lift.acquia.com/authorize``
     - The URL to the OAuth server endpoint
   * - contentReplacementMode
     - ``trusted``
     - The site-wide setting for content replacement — valid values are ``untrusted``, ``trusted``, or ``customized`` (see `content replacement modes </lift/exp-builder/config/modes>`__)
   * - contentOrigin
     - ``aaaabbbb-0000-1111-2222-333334444466``
     - Limit the content available in the content list to a specific origin website (see `content origin </lift/exp-builder/discover/limit>`__)
   * - profile
     - ``{ UDFieldName: UDFFieldValue }``
     - A collection of capture values to be sent either from the captureView_ parameters list or the `data warehouse </lift/omni>`__ UDF fields, which override any values set in the website's ``<meta>`` tags (see `capturing custom values </lift/exp-builder/tips#capture>`__)

.. _captureView: /lift/javascript/view


`Continue to accessing the Experience Builder sidebar > </lift/exp-builder/access>`__
---------------------------------------------------------------------------------------
