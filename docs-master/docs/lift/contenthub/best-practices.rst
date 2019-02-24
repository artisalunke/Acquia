.. include:: /common/global.rst

Best practices for developing with |acquia-product:ch|
======================================================

|acquia-product:ch| is a multi-layered product, and many of its
functions work through the use of `webhooks </content-hub/sharing>`__.
After you register a webhook successfully you should be able to send and
receive content.

Local development
-----------------

Here are some tips for testing |acquia-product:ch| on a local
environment.

Problems posting and receiving entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In general, local websites are unable to post to or receive entities
from the |acquia-product:ch|.

-  **Submitting** - |acquia-product:ch| will try to access a resource
   URL from your local website that would need to be accessible from the
   public internet.
-  **Receiving** - If you are running your website locally, you will not
   be able to receive content from |acquia-product:ch|, as the local
   website can not register or receive webhooks.

Solution
^^^^^^^^

You can expose your local website to the outside world using a tool such
as `ngrok <https://ngrok.com/>`__. You will need to download the latest
version from their website.

.. admonition::  Recommendations for Mac users

   -  We recommend against using Homebrew to install, as users have had problems with the included version of ngrok.
   -  Be sure to use a version of ngrok greater than 2.x.

After installation, complete the following steps:

#. Run ngrok from the command line, using the appropriate command for
   the version that you're using:

   -  *Free version*

      ``ngrok http -host-header=rewrite``

   -  *Paid version*

      ``ngrok http -subdomain= -host-header=rewrite``

#. Set the ``rewrite_localdomain`` variable to rewrite the resource URL
   that is sent to |acquia-product:ch|:

   ``drush config-set acquia_contenthub.admin_settings rewrite_domain 'http://mytunnel.ngrok.io'``

   where ``mytunnel`` is your ngrok tunnel name.

After these are set, the tunnel should be ready for use.
