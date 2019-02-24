.. include:: /common/global.rst

|acquia-product:cha| JavaScript API reference
=============================================

.. toctree::
   :hidden:
   :glob:

   /lift/api/javascript/*

Regardless of your website's content management system (CMS), simply `add the JavaScript tracking script </lift/offers/tracker/add>`__ to
your website's webpages. After you do so, you can then use the |acquia-product:cha| JavaScript API's functions to send additional information.

.. note::  We recommend that you `install and use the Drupal modules </lift/exp-builder/install>`__ to send information to |acquia-product:cha|. If you use the |acquia-product:leb| modules, you do not need to use the JavaScript API.

The following JavaScript functions are available for your use:

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Function
     - Description
   * - |capture|_
     - Capture a visitor's page view
   * - |captureIdentity|_
     - Capture specific visitor information
   * - |setDoNotTrack|_
     - Enable or disable the tracking of visitors
   * - |updatePerson|_
     - Update Person information without adding new records


.. |capture| replace:: ``capture``
.. _capture: /lift/javascript/view

.. |captureIdentity| replace:: ``captureIdentity``
.. _captureIdentity: /lift/javascript/identity

.. |setDoNotTrack| replace:: ``setDoNotTrack``
.. _setDoNotTrack: /lift/javascript/track

.. |updatePerson| replace:: ``updatePerson``
.. _updatePerson: /lift/javascript/updateperson