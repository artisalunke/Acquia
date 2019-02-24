.. include:: /common/global.rst

What to expect during onboarding
================================

|acquia-product:ac| leverages a `stack of
technologies </acquia-cloud/arch>`__ specifically tuned to the needs of
high-availability enterprise Drupal. Key elements of the stack include:

-  ŽVarnish and Nginx on a pair of balancers
-  ŽApache, Memcached, and APC on one or more web servers
-  ŽGluster shared file system
-  ŽPercona on the database servers
-  ŽCode deployment using Git

Migrating to |acquia-product:ac| involves making some changes to your
application’s code and configuration to leverage these components
effectively. For example, to connect to your database, you include a
file that is automatically updated by our hosting stack to point to the
active database server. In the event that the primary database server
becomes unavailable, this file is automatically updated to point to the
secondary database server. Other changes are necessary to allow your
application to connect to
`Memcached </acquia-cloud/performance/memcached>`__, and some
configuration may be required to allow your application to leverage
Varnish properly.

Apart from these basic changes, some applications may require additional
effort to bring them in line with best practices. For example, files in
nonstandard locations (outside of ``sites/[site]/files``), modules that
prevent Varnish from caching, complex ``.htaccess`` files, and
customizations of how Drupal interacts with the database all may present
challenges during onboarding. This is why we pair every
|acquia-product:onb| Concierge customer with a Customer Onboarding
Manager (COM) and Engineer (COE).

Your |acquia-product:onb| team walks through all the products and tools
available to you with your subscription. Your COM introduces you to
Acquia’s workflow, third-party performance monitoring, load testing, and
website diagnostic tools. Your COE evaluates your website for any
potential issues, and the team works through these issues with you to
help ensure a successful launch.

Note

Acquia considers thorough application reviews and load testing as part
of your critical path to launch, both for existing and for newly
developed applications.

Even if your application has been running without issue on other
hosting, we recommend you engage your COE to ensure all aspects of your
application are fully compatible with `Acquia’s
platform </acquia-cloud/arch/tech-platform>`__. If you are developing a
new application, we recommend you engage with your COE to ensure your
build exemplifies best practices from the very beginning.
