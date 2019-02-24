.. include:: /common/global.rst

|acquia-product:leb| methods
============================

The |acquia-product:cha| JavaScript API enables manipulation of
|acquia-product:leb| through the ``window.AcquiaLiftPublicApi`` global
namespace. This page describes the methods that are available for use,
by function.


Handling the |acquia-product:leb| sidebar
-----------------------------------------

Use the following methods to handle the |acquia-product:leb| sidebar:

+-----------------------------------+-----------------------------------+
| Method                            | Description                       |
+===================================+===================================+
| ``activate``                      | Activates |acquia-product:leb|    |
|                                   | for the user. If the user is      |
|                                   | currently signed in, using this   |
|                                   | method opens the sidebar — if     |
|                                   | not, it will trigger an           |
|                                   | authentication request.           |
+-----------------------------------+-----------------------------------+
| ``deactivate``                    | Deactivates the                   |
|                                   | |acquia-product:leb|, which       |
|                                   | closes the sidebar and signs out  |
|                                   | the current user. It will leave   |
|                                   | the markup for the                |
|                                   | |acquia-product:leb| in the DOM   |
|                                   | for reactivation.                 |
+-----------------------------------+-----------------------------------+
| ``remove``                        | Performs the ``deactivate``       |
|                                   | process, and then removes the     |
|                                   | |acquia-product:leb| markup from  |
|                                   | the DOM.                          |
+-----------------------------------+-----------------------------------+


Managing displayed data
-----------------------

Use the following methods to handle the information displayed by
|acquia-product:leb|:

+-----------------------------------+-----------------------------------+
| Method                            | Description                       |
+===================================+===================================+
| ``refresh``                       | Refreshes the data that is        |
|                                   | displayed in an open instance of  |
|                                   | the |acquia-product:leb|. This    |
|                                   | can be helpful when using a       |
|                                   | custom application that modifies  |
|                                   | slots_, rules_, or segments_      |
|                                   | outside of the                    |
|                                   | |acquia-product:leb|, and you     |
|                                   | want the |acquia-product:leb| to  |
|                                   | recognize the changes without     |
|                                   | forcing a refresh of the entire   |
|                                   | page.                             |
|                                   | Optionally, you can specify an    |
|                                   | array of the types of data to     |
|                                   | refresh. The valid types are      |
|                                   | ``slot``, ``rule``, and           |
|                                   | ``segment``.                      |
+-----------------------------------+-----------------------------------+

.. _slots: /lift/exp-builder/slots
.. _rules: /lift/exp-builder/rule
.. _segments: /lift/profile-mgr/segment

Examples
~~~~~~~~

To refresh all of the |acquia-product:leb|-related data on a page, use
the following code:

``window.AcquiaLiftPublicApi.refresh();``

To trigger a refresh of the slot data, use code similar to the
following:

``window.AcquiaLiftPublicApi.refresh(['slot']);``
