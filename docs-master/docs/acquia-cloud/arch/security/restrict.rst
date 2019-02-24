.. include:: /common/global.rst

Restricting website access
==========================

With industry security standards and audit requirements, you might need
high-level security tuning for a public Drupal website. There are
several methods you can use to do this, including adding a module to
your website or configuring IP restriction in Drupal itself. You may
also need to block particular IP addresses due to attacks or other
problems.

.. _by_ip:

IP restriction in Drupal (Recommended)
--------------------------------------

IP restriction in Drupal is an important addition to protect websites
from unwanted visitors. Whether these are test websites where new
features are being added and should be kept from the general web, or
private intranets of companies hosted in the cloud, it is important to
know that your website is safe from prying eyes.

Acquia hosting subscribers do not have access to Apache's VirtualHosts,
and therefore cannot add standard Apache protections. Because of this,
when it comes to protecting both administrative file paths and
restricting access to only whitelisted IP addresses, there is no
all-encompassing module or other easy method to do this on
|acquia-product:ac|.

However, with both some additions to your website's ``settings.php``
file and the inclusion of a new ``acquia.inc`` file to your ``/sites``
directory, you can restrict content service to users accessing the
website from an allowed IP, users with the correct HTTP authentication,
or both.

Important

Even with these protections in place, Varnish can cache a restricted
webpage if that webpage is not specifically marked uncacheable, is
accessed by a whitelisted user, and is not protected by HTTP
authentication. Admin webpages should *never* be cached. If you are
restricting an entire website, using Drupal's access controls and
requiring an authenticated user are better methods of accomplishing this
goal.

Procedure
~~~~~~~~~

To include this functionality, complete the following steps:

#. In a command prompt window, edit your website's ``settings.php`` file
   (located by default in ``docroot/sites/default/``).
#. Add the following code to the end of the file:

   ``if(!defined('DRUPAL_ROOT')) {  define('DRUPAL_ROOT', getcwd()); } if (file_exists(DRUPAL_ROOT . '/sites/acquia.inc')) {  require DRUPAL_ROOT . '/sites/acquia.inc'; }``

#. Save your changes to the ``settings.php`` file.
#. | In the ``docroot/sites/`` directory create a file called
     ``acquia.inc``.
   | You can
     `download <https://gist.github.com/acquialibrary/757c04ed3712c1e4fa129fd88bf65698>`__
     a sample ``acquia.inc`` file for your review and use. An
     `explanation of this file with
     examples <https://gist.github.com/acquialibrary/757c04ed3712c1e4fa129fd88bf65698#file-4096_readme-md>`__
     is also available.

   Note for Acquia hosting customers

   `Contact Acquia Support </support#contact>`__ to obtain a list of
   Acquia IP addresses for whitelisting in your ``acquia.inc`` file.

.. _other:

Alternate use cases
-------------------

If you do not need the flexibility that the `Drupal IP
restriction <#by_ip>`__ offers, there are some tasks that you can use
that require less code and if you have a fairly simple restriction, may
be easier to upkeep.

.. _outside:

Redirecting users outside an IP address range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a non-Acquia hosting environment, you can use the ``%{REMOTE_ADDR}``
variable in the ``.htaccess`` file to redirect users to Google if they
are not in the ``123.456.*`` IP address range. This does not work on
|acquia-product:ac|, however, because of its load balancing structure.

To accomplish the redirect on |acquia-product:ac|, use the
``%{ENV:AH_Client_IP}`` variable:

``RewriteCond %{ENV:AH_Client_IP} !^123\.456\..*  RewriteRule ^http://www.google.com [R=307,L]``

For more information about blocking with ``.htaccess`` and rewrites, see
`Blocking access using
rewrites <%5Bacquia-product:kb%5Darticles/blocking-access-using-rewrites>`__.

.. _block-ip:

Blocking by IP
~~~~~~~~~~~~~~

Because |acquia-product:ac| uses Varnish and load balancers, typical
access controls will not work correctly. This method is similar to the
one detailed in `Best practices on setting up an edit
domain <%5Bacquia-product:kb%5Darticles/best-practices-setting-edit-domain>`__.
You can use a combination of an environment variable that is present on
your |acquia-product:ac| server, ``AH_Client_IP``, and Apache's
``mod_setenvif``.

You should ensure that these rules are in the section that determines
that the Apache ``mod_rewrite`` module is enabled; if it is not, these
redirects will fail.

If you need to block a single IP, the following example sets an
environment variable on the specific IP address ``192.168.15.20``, using
``mod_setenvif``.

``SetEnvIf AH_CLIENT_IP ^192\.168\.15\.20$ DENY=1 Order allow,deny Allow From All Deny from env=DENY``

If you need to block multiple IPs, the following example blocks
addresses from the group ``104.128.*.*`` and the IP address
``192.168.10.10``. We are then able to specifically deny access to these
two subnets and allow access to all other IPs.

``# Match all IP addresses beginning with 104.128 SetEnvIf AH_CLIENT_IP ^104\.128\. Deny_Host # Match a specific IP address SetEnvIf AH_CLIENT_IP ^192\.168\.10\.10$ Deny_Host Order allow,deny Allow from all Deny from env=Deny_Host``

All IPs in the ``104.128`` subnet and the IP address ``192.168.10.10``
get a ``DENY`` header. The rewrite rules check for allowed, and then
deny everyone with a DENY header.

To restrict access and allow only certain IP addresses to reach a
website, you can use code similar to the following:

``# Match all IP addresses beginning with 104.128 SetEnvIf AH_CLIENT_IP ^104\.128\. Allow_Host  # Match a specific IP address SetEnvIf AH_CLIENT_IP ^192\.168\.10\.10$ Allow_Host  Order deny,allow Deny from all Allow from env=Allow_Host``

The immediately previous code is the opposite of the first example, by
using the ``ALLOW`` header to give only certain groups access to the
website, instead of denying those groups.

.. _using:

Using XFF headers to block by IP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If blocking by IP in ``.htaccess`` using ``AH_Client_IP`` does not work,
you can use the ``X-Forwarded-For`` header. The following example
includes this header in the blocking rules in ``.htaccess``:

Important

Because headers are easily spoofed, this method is *much* less reliable
than the other methods described on this page.

``SetEnvIf AH_CLIENT_IP ^123\.234\.123\.234$ DENY=1 SetEnvIf X-Forwarded-For 123\.234\.123\.234 DENY=1 Order allow,deny Allow From All Deny from env=DENY``

XFF headers use a pattern match without the ``^`` and ``$`` anchors—if
the IP address appears anywhere in the value of XFF header, the request
will be blocked. This method may generate false positives, especially
when using patterns to block entire subnets, such as ``123.234``.

However, if everything works as it should (assuming an attacker is not
`spoofing IP
addresses <https://en.wikipedia.org/wiki/IP_address_spoofing>`__), the
actual source IP should typically appear in the XFF header. Note that
you cannot be sure of the IP address' position, as its position can vary
depending on the proxy's or balancers' setup.
