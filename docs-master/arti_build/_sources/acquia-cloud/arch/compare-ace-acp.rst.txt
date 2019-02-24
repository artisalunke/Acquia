.. include:: /common/global.rst

Comparing |acquia-product:acs| and |acquia-product:ace|
=======================================================

The |acquia-product:ac| platform delivers comprehensive Drupal
infrastructure support from a single vendor, and offers three levels of
service for hosting Drupal applications in the cloud:

-  *|acquia-product:acs|*, a self-service Drupal hosting environment
   built for developing and deploying one or more production
   applications.
-  *|acquia-product:ace|*, a fully managed, high-availability, scalable,
   clustered Drupal hosting environment built for the most complex
   Drupal applications with the highest performance and uptime
   requirements.
-  *|acquia-product:acfs|*, a free, self-service Drupal hosting
   environment built for developing and testing one application, with a
   more limited server and disk size. `Learn more about
   |acquia-product:acfs| </acquia-cloud/free>`__.

Both |acquia-product:acs| and |acquia-product:ace| deliver a complete
infrastructure to support Drupal deployment workflow processes from
development and staging through to production. |acquia-product:ac|
includes broad developer UIs and APIs, secure server access using SSH,
and automated deployment from a version-controlled code repository.

|acquia-product:acs| and |acquia-product:ace| use the same user
interface as part of the |acquia-product:ac| platform. For the purposes
of the |acquia-product:ac| user documentation, you can assume that all
instructions apply equally to |acquia-product:acs| and
|acquia-product:ace|, unless otherwise stated.

Paid |acquia-product:acs| and |acquia-product:ace| applications each
have three environments by default: development, staging, and
production. |acquia-product:acfs| applications have just two
environments: development and staging. Optionally, |acquia-product:ace|
applications can use `additional
environments </acquia-cloud/manage/more-envs>`__.

Here’s a more detailed comparison between |acquia-product:acs| and
|acquia-product:ace|:

+-----------------------+-----------------------+-----------------------+
|                       | |acquia-product:acs|  | |acquia-product:ace|  |
+=======================+=======================+=======================+
| **Infrastructure**    | Single web server and | Customizable, highly  |
|                       | database server, with | available cluster of  |
|                       | Varnish caching       | multiple web servers  |
|                       | supplied by           | and database servers, |
|                       | non-dedicated load    | spanning at least two |
|                       | balancers.            | availability zones.   |
|                       |                       | Optional multi-region |
|                       |                       | failover.             |
+-----------------------+-----------------------+-----------------------+
| **Uptime**            | Not guaranteed, but   | Guaranteed 99.95%     |
|                       | in practice, 99.9%+.  | Because               |
|                       | Because               | |acquia-product:ace|  |
|                       | |acquia-product:acs|  | provides redundant    |
|                       | provides single       | servers,              |
|                       | servers,              | |acquia-product:ace|  |
|                       | |acquia-product:acs|  | applications will not |
|                       | applications do       | experience downtime   |
|                       | experience downtime   | when servers are      |
|                       | when servers are      | rebooted for system   |
|                       | rebooted for system   | security updates,     |
|                       | security updates,     | scheduled             |
|                       | scheduled             | maintenance, or       |
|                       | maintenance, or       | server resizing.      |
|                       | server resizing.      |                       |
+-----------------------+-----------------------+-----------------------+
| **Tools and add-ons** | Access to most, but   | Access to all         |
|                       | not all,              | |acquia-product:aqs|  |
|                       | |acquia-product:aqs|  | tools and add-ons.    |
|                       | tools and add-ons.    | Extensive platform    |
|                       | Less platform         | monitoring.           |
|                       | monitoring.           |                       |
+-----------------------+-----------------------+-----------------------+

.. _pro:

|acquia-product:acs| details
----------------------------

|acquia-product:acs| is a self-service platform, while
|acquia-product:ace| is fully managed by Acquia. Here are some examples
of tasks that Acquia performs for |acquia-product:ace| customers, which
|acquia-product:acs| customers must manage for themselves:

-  Detecting and responding to changes in traffic that require resizing
   servers or making other changes in available resources
-  Detecting and responding to denial of service attacks
-  Restarting servers
-  Recovering from backups

Because you manage several of your own server settings on
|acquia-product:acs|, there is the risk that improper use of these
settings can lead to server instability or poor application performance.

If you have an |acquia-product:acs| subscription that you want to
upgrade to |acquia-product:ace|, contact sales@acquia.com.

.. _ace:

|acquia-product:ace| details
----------------------------

|acquia-product:ace| supports customized infrastructure and integration,
with customized reverse proxy, web server, caching, and database sizes.
For example, some |acquia-product:ace| applications may require
comparatively more database resources, while others may require
comparatively more or larger web servers. |acquia-product:ace| supports
custom integrations for use cases like single sign-on or integration
with other enterprise systems.
