.. include:: /common/global.rst

Enabling device-based redirects
===============================

Visitors can view your application from different device types (like
mobile phones, tablets, and desktops) with very different screen sizes.
One way to deliver the best experience for site visitors with different
screen sizes is to develop separate versions of your applications that
are optimized for smaller screens. For example, you might have one
application optimized for phone screens, one for tablet screens, and one
for laptop or larger screens. This article describes how you can use
device redirect headers to redirect site visitors to an application
version that is best suited for display on their devices.

Depending on your needs, another good option may be to use a `responsive
design <https://drupal.org/node/1322126>`__ for your application, which
will detect the type of device that is accessing the application and
adjust the way pages are displayed accordingly.

.. _header:

Redirects based on the request user-agent header
------------------------------------------------

In the |acquia-product:ac| platform, you can redirect visitors in the
Varnish layer, based on the devices they are using, as determined by the
``user-agent`` HTTP header in the request. |acquia-product:ac| supports
the following HTTP headers for device-based redirects:

-  *Desktop devices* - ``X-AH-Desktop-Redirect``
-  *Mobile devices* - ``X-AH-Mobile-Redirect``
-  *Tablet devices* - ``X-AH-Tablet-Redirect``

Important

Acquia strongly recommends that you test device-based redirects before
deploying to production. Incorrect redirect code can create serious
problems when you try to access your application.

.. _settingsphp:

Setting up device redirects in the settings.php file
----------------------------------------------------

You can set device-based redirects by using your Drupal application's
``settings.php`` file to set HTTP headers in the response.

Note

The following samples are for Drupal 7.

The following sample redirects tablets to ``t.mydomain.com``, while
redirecting mobile devices to ``m.mydomain.com``:

``drupal_add_http_header('X-AH-Tablet-Redirect', 'http://t.mydomain.com'); drupal_add_http_header('X-AH-Mobile-Redirect', 'http://m.mydomain.com');``

If you want to set this only for specific hosts (for example,
``www.mydomain.com``) in the docroot (for example, if you're running a
Drupal multisite), adjust the lines in the ``settings.php`` file as
follows:

``if (isset($_ENV['HTTP_HOST']) && strpos($_ENV['HTTP_HOST'], 'mydomain.com')) {   drupal_add_http_header('X-AH-Tablet-Redirect', 'http://t.mydomain.com');   drupal_add_http_header('X-AH-Mobile-Redirect', 'http://m.mydomain.com'); }``

You can set both redirects to the same domain if you have one subdomain
that handles both tablets and other mobile devices. If you set only the
``X-AH-Mobile-Redirect`` header, requests from tablets will remain on
the current domain.

The following example demonstrates how you might want to set up your
redirects if you are hosting a desktop, mobile, and tablet application
from the same codebase:

``if (isset($_ENV['HTTP_HOST'])) {   switch ($_ENV['HTTP_HOST']) {     case 'www.mydomain.com':     case 'mydomain.com':       drupal_add_http_header('X-AH-Tablet-Redirect', 'http://t.mydomain.com');       drupal_add_http_header('X-AH-Mobile-Redirect', 'http://m.mydomain.com');       break;      case 'm.mydomain.com':       drupal_add_http_header('X-AH-Tablet-Redirect',  'http://t.mydomain.com');       drupal_add_http_header('X-AH-Desktop-Redirect', 'http://www.mydomain.com');       break;      case 't.mydomain.com':       drupal_add_http_header('X-AH-Mobile-Redirect',  'http://m.mydomain.com');       drupal_add_http_header('X-AH-Desktop-Redirect', 'http://www.mydomain.com');       break;   } }``

The following examples shows how you might set up redirects for multiple
domains (``example.com`` and ``example2.com``) within a Drupal multisite
installation. You should modify these examples for your own domain
names.

``if (isset($_ENV['HTTP_HOST'])) {   if (strpos($_ENV['HTTP_HOST'], 'example.com') !== FALSE) {   // matches every domain where  'example.com' is a substring      drupal_add_http_header('X-AH-Tablet-Redirect', 'http://t.example.com');     drupal_add_http_header('X-AH-Mobile-Redirect', 'http://m.example.com');   }   else if (strpos($_ENV['HTTP_HOST'], 'example2.com') !== FALSE) {   // matches every domain where  'example2.com' is a substring     drupal_add_http_header('X-AH-Tablet-Redirect', 'http://t.example2.com');     drupal_add_http_header('X-AH-Mobile-Redirect', 'http://m.example.com');   } }``

``if (isset($_ENV['HTTP_HOST'])) {   if (strpos($_ENV['HTTP_HOST'], 'example.com') === 0) {   // matches every domain that *begins* with  'example.com'   // would also match a theoretical domain  'example.com.au' for example      drupal_add_http_header('X-AH-Tablet-Redirect', 'http://t.example.com');      drupal_add_http_header('X-AH-Mobile-Redirect', 'http://m.example.com');   }   else if (strpos($_ENV['HTTP_HOST'], 'example2.com') === 0) {   // matches every domain that *begins* with  'example2.com'   // would also match a theoretical domain  'example2.com.au' for example      drupal_add_http_header('X-AH-Tablet-Redirect', 'http://t.example2.com');      drupal_add_http_header('X-AH-Mobile-Redirect', 'http://m.example.com');   } }``

.. _https:

Redirects with HTTPS
--------------------

Drupal will correctly identify incoming HTTPS requests using the normal
"HTTPS" server environment variable if your application uses the
|acquia-product:ac| include file statement in your application's
``settings.php`` file.

.. _opt-out:

Opting out of device-based redirects
------------------------------------

You may need to provide a way for users on mobile or tablet devices to
view the desktop version of the application if they prefer. You can do
this with a custom block that appears on every page, letting visitors
select the desktop version. For information about how to do this, see
`Circumvent mobile redirects with a desktop
cookie <%5Bacquia-product:kb%5Darticles/circumvent-mobile-redirects-desktop-cookie>`__.

.. _drupal:

Setting headers in Drupal
-------------------------

You can also set the headers in Drupal itself to perform device-based
redirects. This method works only for pages actually served by Drupal.
Static assets, such as files, are not affected by the headers. The
benefit of using Drupal's headers is that you can create more complex
device-based redirects based solely on the landing page.

Many modules are available on `Drupal.org <https://www.drupal.org>`__
that can help you create device-based redirects for your application.
Acquia does not test these and cannot make specific recommendations for
their use on |acquia-product:ac|.

Use device-based redirects instead of using the Drupal `Mobile
Tools <https://www.drupal.org/project/mobile_tools>`__ module, since
that module sets a session cookie, which bypasses the Varnish cache and
therefore can negatively affect your application's performance on
|acquia-product:ac|.
