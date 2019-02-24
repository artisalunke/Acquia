.. include:: /common/global.rst

Using the HTTPRL module
=======================

The `HTTP Parallel Request & Threading
Library <https://www.drupal.org/project/httprl>`__ (HTTPRL) module may
require some special configuration to use on |acquia-product:ac|. The
default HTTPRL configuration assumes that SSL requests are handled by
the web server; on |acquia-product:ac|, SSL requests are handled by the
load balancer or Elastic Load Balancer. As a result, you may see an
error like this:

``Error     HTTPRL - Core   drupal_http_request() Your system or network configuration does not allow Drupal to access web pages. This could be due to your webserver configuration or PHP settings.``

This error does not interfere with the normal operation of your Drupal
application on |acquia-product:ac|, but it is a good idea to configure
your application so that it doesn't generate errors that don't actually
indicate that a problem exists.

To eliminate this error message, set the ``httprl_server_addr`` variable
to ``-1``, so that the HTTPRL module uses the host name instead of an IP
address for self-server requests. To do this, use one of the following
methods:

-  Add the following line to your ``settings.php`` file:

   ``$conf['httprl_server_addr'] = -1; // If set to -1 httprl will use the host name    instead of an IP address for self-server requests.``

-  Set the following variable using
   `Drush <https://www.drupal.org/project/drush>`__:

   ``drush ev 'variable_set("httprl_server_addr", -1);'``
