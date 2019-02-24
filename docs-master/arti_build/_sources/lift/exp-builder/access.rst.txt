.. include:: /common/global.rst

Setting up access to the |acquia-product:leb|
=============================================

.. container:: internal-navigation

   **Installing Experience Builder**

   * :doc:`Install </lift/exp-builder/install>`
   * Access
   * :doc:`Content </lift/exp-builder/content-hub>`

To personalize your website with |acquia-product:leb|, you and your
users must be able to access the |acquia-product:leb| sidebar. Use the
procedures on this page to set up and activate your |acquia-product:leb|
bookmark.

|acquia-product:cha| link
-------------------------

Drupal 8 users with the permissions:

-  **Access Acquia Lift links**
-  **Access toolbar**

are able to click the **Acquia Lift** link in the toolbar to
activate the |acquia-product:lpm| toolbar. This link will appear only on
pages that support the |acquia-product:leb|.


Chrome extension
----------------

Google Chrome users can install a browser extension to enable the
|acquia-product:cha| toolbar.

#. `Download and
   install <https://chrome.google.com/webstore/detail/acquia-lift/pljoceedhfkdbnbljknbiadphecoipca>`__
   the extension.
#. When visiting a page that uses |acquia-product:cha|, click the rocket
   icon |Rocket icon| in your extension bar.

This activates the |acquia-product:lpm| administrative login, and then
the toolbar.

Setting up a bookmark
---------------------

The |acquia-product:lpm| toolbar is supported for Google Chrome and
Mozilla Firefox, and can be used for Drupal or non-Drupal users. Select
one of the following methods and follow its instructions to set up an
|acquia-product:leb| bookmark for your use:

-  *Google Chrome*

   #. Right-click the bookmarks toolbar.
   #. Click **Add Page**.
   #. Add a **Name** like **Lift Admin UI bookmarklet**.
   #. Add the bookmark code in the **URL**.
   #. Click **Save**.

-  *Firefox*

   #. Right-click the bookmarks toolbar.
   #. Click **New Bookmark**.
   #. Add a **Name** like **Lift Admin UI bookmark**.
   #. Add the bookmark code in the **Location**.
   #. Click **Add**.

Bookmark code
~~~~~~~~~~~~~

Enter the following code in the appropriate place in the bookmark.

.. code-block:: none

   javascript:(function() { if (window.AcquiaLiftPublicApi) { window.AcquiaLiftPublicApi.activate(); } else { alert('Sorry, Acquia Lift could not be found'); } })();

Activating the |acquia-product:cha| toolbar
-------------------------------------------

After setting up and saving your bookmark, complete the following steps:

#. Select a customizable page, such as your website's homepage.
#. Click the bookmark that you created.
   |acquia-product:cha| displays a sign-in page for the
   |acquia-product:lpm| administrative interface.
#. Sign in using an |acquia-product:lpm| account in the Administrators
   group.

|lift-bookmarklet-dots.png|

After you sign in to |acquia-product:lpm|, a sidebar slides out from the
right side of the browser window. This sidebar is used for configuring
|acquia-product:leb| operations, including creating
`slots </lift/exp-builder/slots>`__ and
`rules </lift/exp-builder/rule>`__.

Click the three vertical dots to open or close the toolbar.

`Continue to connecting to Content Hub for content > </lift/exp-builder/content-hub>`__
-----------------------------------------------------------------------------------------------

.. |Rocket icon| image:: https://cdn2.webdamdb.com/1280_gNkvE9WIT5G0.png?1526475627
   :class: inline-img
   :width: 29px
   :height: 29px
.. |lift-bookmarklet-dots.png| image:: https://cdn2.webdamdb.com/1280_cqzvRdWv9Rc2.png?1526475828
   :class: float-right
   :width: 27px
   :height: 113px
