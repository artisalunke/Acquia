.. include:: /common/global.rst

Key concepts in |acquia-product:ac|
===================================

|acquia-product:ac| is a cloud-based hosting platform tuned for Drupal
performance and scalability. Acquia manages your servers and provides an
easy-to-use workflow for developing, staging, and publishing your Drupal
applications. We designed the |acquia-product:ac| workflow to support
the best practices identified by the Drupal community for managing a
Drupal application. In order to make the most of |acquia-product:ac|,
you should understand the following key concepts.

.. _vsvps:

Comparing |acquia-product:ac| to virtual private servers
--------------------------------------------------------

|acquia-product:ac| is not just a virtual private server. It is a
carefully crafted platform optimized to run highly available Drupal
applications. In creating |acquia-product:ac|, we have carefully
selected, configured, tested, and deployed the best open-source platform
for this goal.

Your |acquia-product:ac| platform may consist of a single shared server
or one or more dedicated servers. Each |acquia-product:ac| server runs
the same versions of each element of the platform:

-  Linux operating system
-  Apache web server
-  MySQL database
-  nginx reverse proxy load balancing server
-  Varnish Cache

This enables Acquia to efficiently provision, test, manage, monitor, and
upgrade the platform. As a result, you cannot select and install your
own versions of the operating system, web server, or other platform
software your application runs on. For more information about what is
installed on |acquia-product:ac| and what other software is and is not
supported, see `|acquia-product:ac| technology platform and supported
software </acquia-cloud/arch/tech-platform>`__.

You have non-privileged access to your servers using SSH, using a public
key you register with your |acquia-product:ac| account. You do not have
root or ``sudo`` privileges. You have full control over the Drupal
docroot, including Drupal core, contributed, and custom modules and the
web servers' ``.htaccess`` files, but do not have write privileges for
``php.ini``,\ ``my.cnf``, or Apache configuration files.

.. _components:

Code, databases, and files
--------------------------

The key components of a Drupal application are the code, databases, and
files.

-  The code is your Drupal core installation, any contributed or custom
   Drupal modules you have installed, and themes.
-  The databases store your application’s content, configuration, and
   other information, including Drupal nodes, user information and log
   information.
-  The files store user-uploaded objects, such as pictures and PDF
   files.

The |acquia-product:ac| workflow enables you to manage your
application’s code, database, and files separately in each of the local,
Development, Staging, and Production environments. For more information,
read:

-  `Working with code </acquia-cloud/develop/code>`__
-  `Working with databases </acquia-cloud/manage/database>`__
-  `Working with files </acquia-cloud/manage/files>`__

.. _multiple_environments:

Multiple environments: local, Development, Staging, and Production
------------------------------------------------------------------

Each |acquia-product:ac| application has four (or more) environments to
optimize your application development and publishing workflow:

-  **Local** - You develop your application locally. This enables you to
   see the effects of your changes immediately. Using version control
   enables multiple web developers to work simultaneously on different
   parts of the application.
-  **Development** - When you have multiple developers working on an
   application, the Development environment is for initial integration
   testing. The developers commit their changes to the version control
   system, and the changes are deployed immediately in the Development
   environment so that everyone can see them. Alternatively, you can
   enable the `Live Development </acquia-cloud/develop/livedev>`__
   feature, and edit your code directly in your Development or Staging
   environment.
-  **Staging** - In the Staging environment, you can test changes to
   your application before deploying them to Production.
-  **Production** - Your users see only your Production environment. You
   can pull your application’s database and files from Production to
   Staging or Development, so you can work with the current state and
   content of your application as you test and develop it.

|acquia-product:ac| provides a separate instance of your databases and
file directories for each of your application's environments. The
|acquia-product:ac| settings include file for your application
configures your ``settings.php`` file so that for each environment, your
application connects to the correct database instance and files
directory.

If you are an |acquia-product:ace| customer, you can, if you choose, set
up `additional environments </acquia-cloud/manage/more-envs>`__. This
can be useful for integration or load testing and may also enable
|acquia-product:ac| to fit better with your development workflow.

.. _dev:

Developing code locally or in the Development environment
---------------------------------------------------------

|acquia-product:ac| supports two models for developing code: local
development and live development.

-  Using local development, you develop your application locally, using
   a local checkout of your |acquia-product:ac| repository, and then
   commit to your codebase. `|acquia-product:add| </dev-desktop>`__ is a
   free tool you can use to accelerate your local development and sync
   with your |acquia-product:ac| environments.
-  Using `live development </acquia-cloud/develop/livedev>`__, you
   develop your application on your |acquia-product:ac| Development
   environment.

.. _vcs:

Version control and multiple environments
-----------------------------------------

|acquia-product:ac| enforces the use of a version control system to
efficiently manage your codebase. We support the Git version control
system. As you develop your application locally, you send changes to
your application’s code on |acquia-product:ac| using version control
software, instead of copying the files directly using file upload tools,
such as FTP. If you are not familiar with using version control and
multiple environments, we believe that the time you spend learning these
best practices will pay off with more efficient, more flexible, and less
error-prone development and deployment.

Any environment can deploy any branch or tag from your code repository.
An environment that is deploying a branch automatically gets any code
committed to that branch. So, when you commit your code to your codebase
(for example, in master, if you are using Git, your changes are
automatically deployed.

.. _debug:

Debugging your application
--------------------------

If your application is on |acquia-product:acs|, you are responsible for
managing your application, while Acquia manages your servers. To
successfully manage your application, you should be able to perform the
following basic debugging tasks:

-  Looking at the Apache error logs to review PHP errors
-  Running basic Drush commands from the command line, such as
   ``drush status``, to obtain error messages for debugging applications
   that may be offline

.. _elb:

Load balancing
--------------

|acquia-product:ac| uses `nginx <http://nginx.org/en/>`__ for HTTP and
HTTPS load balancing. When the load balancer detects a web server
failure, it will stop sending web requests to the failed server. To
guard against load balancer failures, Acquia uses a redundant load
balancer configuration, with an active load balancer backed up by a
passive load balancer. If the active load balancer fails, the passive
load balancer is available to take over.

Acquia's operational infrastructure constantly monitors all load
balancers (and the websites behind those balancers) to ensure that they
are accessible, reliable, and reachable. When our monitoring detects an
error, it immediately alerts our 24x7 operations staff. We then
determine the reason for the failure, which can include high website
traffic, a denial-of-service attack, or hardware failure. Depending on
the type of failure, the passive balancer is brought online within
seconds.
