.. include:: /common/global.rst

Connecting to |acquia-product:ch|
=================================

.. toctree::
   :hidden:
   :glob:

   /lift/exp-builder/*


.. container:: internal-navigation

   **Installing Experience Builder**

   * :doc:`Install </lift/exp-builder/install>`
   * :doc:`Access </lift/exp-builder/access>`
   * Content

After you finish your |acquia-product:leb| installation, you have a
personalization interface on your website, but you need content for
|acquia-product:leb| to use. Because |acquia-product:ch| is part of the
overall |acquia-product:cha| product, you can connect your website to a
single |acquia-product:ch| domain to access your websites' published
content in the |acquia-product:leb| sidebar.

For complete instructions on how to install and connect your website to
|acquia-product:ch|, see `Installing the |acquia-product:ch|
client </content-hub/install>`__.

After you install |acquia-product:ch| modules and connect your website
to |acquia-product:ch|, your publisher websites' content should be
available for you to use with your website.

Configuring your |acquia-product:ch| settings
---------------------------------------------

If you have a Drupal website and are using the Drupal client modules,
you can configure your |acquia-product:ch| settings by using the
following procedure:

#. Sign in to your website as a user with the *Administrator* role.
#. In your website's admin menu, click **Configuration**, and then click
   the **Acquia Content Hub** link.
#. In a new tab, `sign in to the |acquia-product:lpm|
   interface </lift/profile-mgr#signing>`__ using an account with
   administrative privileges, and then click the **Admin** tab.
#. Click the **Manage Customers** link.
#. Click the customer name with the |acquia-product:ch| settings that
   you want to inspect.
#. In the **Content Hub Module** section, obtain the following values:

   -  **Content Hub Hostname**
   -  **API Key**
   -  **Secret Key**
   -  **Client Name**

#. Return to your website, and then update the values based on those
   from the |acquia-product:lpm| interface.
#. Click **Save configuration**.

Troubleshooting |acquia-product:ch| and |acquia-product:leb|
------------------------------------------------------------

If |acquia-product:ch| is not configured correctly, no content will
appear in the |acquia-product:leb| sidebar. |acquia-product:leb|
displays the following message when this situation occurs:

``Publish content to Content Hub in order to begin creating Rules. Check your Content Hub configuration page or contact your site administrator for additional details.``

Note

If you uninstall and reinstall |acquia-product:ch| at any point, you
will not be able to use the **Client Name** that you used during the
previous configuration process. In that case, append a unique number to
the **Client Name** that you used previously. For example, if you
previously used ``LIFTSITE2``, enter ``LIFTSITE3``.
