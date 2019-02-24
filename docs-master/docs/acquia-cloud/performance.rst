.. include:: /common/global.rst

Improving application performance
=================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/performance/*

This page provides a checklist of possible performance optimizations for
your |acquia-product:ac| application. Each Drupal application is
customized to meet your organization's business goals; therefore, not
every specific recommendation may apply to your application. The
checklist is ordered by priority of impact; generally speaking, you'll
get a greater return from items at the beginning of the list than from
those at the end.

-  :ref:`insight`
-  `Caching <#caching>`__
-  `Search <#search>`__
-  `CSS and JavaScript aggregation <#css-js>`__
-  `PHP memory usage <#memory>`__
-  `Database optimization <#database>`__
-  `Drupal core and modules <#drupal>`__
-  `Third-party scripts and styles <#scripts>`__
-  `Gzip compression <#compression>`__
-  `Very large numbers of files <#files>`__
-  `Image optimization <#image>`__

.. _insight:

|acquia-product:ais|
--------------------

|acquia-product:ais| provides real-time analysis of your application's
code and configuration settings to help you optimize performance and
security. It evaluates your application by examining many by reviewing
several of its aspects and attributes, including many of the ones
described in this topic, and then offers advice about fixing any
problems it discovers. For more information, see |ais|_.

Caching
-------

One of Drupal’s key strengths is the ability to dynamically generate
content, serving up different content depending on the user and the
context. To dynamically generate the webpage that is sent to the
browser, a series of complex events can be executed, such as the
following:

-  Establishing a database connection
-  Loading settings and modules
-  Initializing a user session
-  Mapping the URL to a PHP page callback function to run the
   application’s business logic
-  Collecting the fringe elements that surround the main content of the
   webpage

Most of these steps are executed every time a webpage is rendered and
can take more time than it would take a simple web server to serve a
static webpage. An effective caching strategy can greatly improve
performance by storing webpages, webpage elements, and other resources,
so that a cached version, rather than a newly generated version, can be
served. Caching can come into play at several different levels in a
Drupal web application:

-  Drupal caches
-  Varnish
-  Memcache
-  PHP opcode
-  CDNs

For information about these different caching techniques, see `Caching
overview <https://support.acquia.com/hc/en-us/articles/360005212334-Caching-overview>`__.

Search
------

Drupal's core search performs queries against the MySQL database. For
high-traffic applications, this can put enormous stress on the database
server. Instead, use |acquia-product:as|, which removes search load from
the database and offers many feature and usability improvements. For
more information, see |as|_.

.. _css-js:

CSS and JavaScript aggregation
------------------------------

A single Drupal webpage may invoke many different CSS and JavaScript
webpages. By using Drupal's aggregation settings, you can reduce the
number of HTTP requests for each webpage. You can examine the HTTP
requests each webpage is making with a web development tool, such as
Firebug or YSlow.

Enabling on Drupal 8
~~~~~~~~~~~~~~~~~~~~

To enable CSS and JavaScript aggregation in Drupal 8, complete the
following steps:

#. Go to ``http://[server_URL]/admin/config/development/performance``,
   where ``[server_URL]`` is your application's URL address.
#. In the **Bandwidth Optimization** section, select the check boxes for
   the following options:

   -  **Aggregate CSS files**
   -  **Aggregate JavaScript files**

#. Click **Save configuration**.

|Enable CSS and JS aggregation|

Enabling on Drupal 7
~~~~~~~~~~~~~~~~~~~~

To enable CSS and JavaScript aggregation in Drupal 7, complete the
following steps:

#. Go to ``http://[server_URL]/admin/config/development/performance``,
   where ``[server_URL]`` is your application's URL address.
#. In the **Bandwidth Optimization** section, select the check boxes for
   the following options:

   -  **Aggregate and compress CSS files**
   -  **Aggregate JavaScript files**

#. Click **Save configuration**.

|Enable CSS and JS aggregation|

.. _memory:

PHP memory usage
----------------

Each |acquia-product:ac| server has a fixed amount of PHP memory
available for building webpages. |acquia-product:acs| customers can
configure the PHP memory limit, as described in `Configuring PHP
settings </acquia-cloud/manage/php#php-mem>`__. Large and complex
webpages can consume a lot of memory, and if your server runs out of
memory, it can fail. However, the higher the amount of memory available
for each PHP process, the fewer processes can run simultaneously.

.. _database:

Database optimization
---------------------

MySQL queries per webpage
~~~~~~~~~~~~~~~~~~~~~~~~~

Overly complex webpages can generate an enormous number of MySQL
queries, which can slow webpage building and limit scalability. Even if
each individual query is fast, the cumulative load of database queries
can greatly slow down webpage load time. To address this issue, you can
decrease webpage complexity, optimize queries, and use Drupal's cache
API to store custom data for faster reuse.

.. _slowquery:

Identify slow database queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MySQL provides a slow query log that you can review to discover database
queries that are taking excessive time to complete. A slow query can
indicate improper SQL query construction or PHP code.

You can download your application's MySQL slow query log from the
**Logs** page for an environment in the |acquia-product:ui|. You can
examine the slow query log using tools like Percona Tools
`pt-query-digest <https://www.percona.com/doc/percona-toolkit/2.1/pt-query-digest.html>`__
and the MySQL EXPLAIN statement. For more information, see `Downloading
your slow query log </acquia-cloud/monitor/slow-query>`__ and `Tools for
parsing a slow query
log <%5Bacquia-product:kb%5Darticles/tools-parsing-slow-query-log>`__.

For another approach to identifying resource consumption issues and
bottlenecks, consider using `New Relic </acquia-cloud/monitor/apm>`__.
For more information, see `Using New Relic to troubleshoot site
issues <%5Bacquia-product:kb%5Darticles/using-new-relic-troubleshoot-site-issues>`__.

.. _drupal:

Drupal core and modules
-----------------------

Core hacked
~~~~~~~~~~~

Changes to Drupal's core PHP, JavaScript, and CSS files can adversely
affect the performance and behavior of the application and seriously
degrade the ability to support and maintain the application post-launch.
*Do not hack core!* Through the proper use of contributed and custom
modules and Drupal's APIs, you can achieve your web application's goals
without hacking core.

You can identify where your web application diverges from Drupal core
using |acquia-product:ais| by using the following steps:

#. `Install and enable the </acquia-cloud/insight/install>`__ 
   |acquia-product:anc| module.
#. On the **Configuration** page for **Acquia Settings**, in the **Allow
   collection and examination of the following items** section, select
   the **Source code** check box.

   |Enable code checks|

Each time |acquia-product:ais| examines your application, it analyzes
and reports any points in your code that diverge from Drupal core. You
can view alerts for this status on the **Insight** page for an
environment in the |acquia-product:ui|.

Module selection and activation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have Drupal modules installed and enabled in your application,
they can still adversely affect your application's performance even if
you don't use them. Disable unneeded modules to prevent inclusion by PHP
at run time.

Larger, custom modules should use includes in their ``hook_menu``
implementation, such as ``*.admin.inc`` and ``*.pages.inc``, which
causes them to not be loaded for every webpage.

Use the Fast 404 module
~~~~~~~~~~~~~~~~~~~~~~~

Use a module such as `Fast
404 <https://www.drupal.org/project/fast_404>`__ to serve static 404s
for image, icon, CSS, or other static files, rather than bootstrapping
Drupal. Drupal core includes a basic version of this functionality, but
the Fast 404 module provides additional enhancements.

.. _syslog:

Use syslog instead of logging to the Drupal database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, Drupal logs to the main database. On high traffic
applications, this can have a negative effect on performance. Instead,
use the core
`Syslog <https://www.drupal.org/docs/8/core/modules/syslog/overview>`__
module, which is included in Drupal core and logs to the operating
system logs instead. Enable the Syslog module, and then disable the
Database logging module in the Core section of your Drupal application's
Modules administration page.

.. _statistics:

Do not use the Drupal core statistics module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `statistics
module <https://www.drupal.org/docs/8/core/modules/statistics/overview>`__
in Drupal core saves data to the main database. Because every page view
generates statistics, this behavior can make a large number of writes to
the database. On high traffic applications this can have a negative
effect on performance. Instead, use another statistics service, such as
Google Analytics.

.. _theme:

Disable theme registry rebuilding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some Drupal themes (such as the Zen theme and the Fusion theme) have an
option to rebuild the theme registry on every webpage load. This is
great during development, but can have a severely negative effect on
performance. Disable the **Rebuild theme registry on every page**
setting for the theme on your Production environment before you go live.

.. _xhprof:

Profile your code with XHProf
-----------------------------

In order to evaluate the performance of your |acquia-product:ac|
application, you can use XHProf, a hierarchical profiler for PHP. Using
XHProf, you can see each PHP function called by a webpage, with data
about the resources used by each function. After you identify functions
that may be using an excessive amount of CPU time or memory, you can
investigate how to improve the code's efficiency. For more information,
read `Using XHProf to evaluate code
performance <https://support.acquia.com/hc/en-us/articles/360004268173-Using-XHProf-to-evaluate-code-performance>`__.

.. _scripts:

Third-party scripts and styles
------------------------------

When using third-party CSS and JavaScript, best practices would have you
use Drupal's ``drupal_add_css`` and ``drupal_add_js`` APIs—failing to do
so can lead to extra HTTP requests and can cause inconsistent behavior
of user interface elements. After you enable `CSS and JavaScript
aggregation <#css-js>`__, examine your application with tools such as
Firebug or YSlow. Identify any CSS or JavaScript that is being included
directly from themes or modules using HTML, and modify your code to add
CSS and JavaScript by using the proper hooks.

.. _compression:

Gzip compression
----------------

Using file compression reduces bandwidth use and improves user
perception of application performance. |acquia-product:ac| compresses
HTML, CSS, and JavaScript files by using ``mod_deflate`` on each Apache
server:

``AddOutputFilterByType DEFLATE text/css application/javascript application/x-javascript text/html``

To compress other file types that your application may output, you can
add a ``AddOutputFilterByType`` directive to your ``.htaccess`` file to
configure it for the appropriate MIME types. For more information, see
the following Apache documentation:

-  `AddOutputFilterByType <http://httpd.apache.org/docs/2.2/mod/core.html#addoutputfilterbytype>`__
   directive
-  `mod_deflate <http://httpd.apache.org/docs/2.2/mod/mod_deflate.html>`__

.. _files:

Very large numbers of files
---------------------------

In |acquia-product:ac|, uploaded files are separate from the Drupal
database and your code repository. |acquia-product:ac| deployment code
creates a symbolic link to your application's ``/files`` directory. For
more information, see `Understanding
files </acquia-cloud/manage/files/about>`__.

If you maintain a very large number of files in your application, it can
have a substantial negative effect on performance and stability,
especially if they are all contained in the same directory. We have
found that over 2,500 files in any single directory in the files
structure can seriously impact your server's performance and
potentially, its stability. If your application requires a large number
of files, maintain them in multiple directories. If your application
requires a greater number of files and you are concerned about
performance, we will be glad to work with you to use external storage,
CDNs or other best practices that can act to mitigate this risk.

These thresholds have some variability, because larger servers may have
more resources available to handle the files, and this can reduce the
impact. Your non-production environments may be more vulnerable to this
issue, because they commonly share resources.

To avoid this problem, you should split the files into subfolders that
are identified by some characteristic of the files. You can use dates as
tokens for these directories. The `File (Field)
Paths <https://www.drupal.org/project/filefield_paths>`__ and `File
Entity Paths <https://www.drupal.org/project/fe_paths>`__ modules allow
you to use node tokens to select the directory where the images or other
uploaded files should reside. Select the paths for files attached either
through file fields or by way of the Drupal core upload module.

For more information, see `Proactively organizing files in
subfolders <https://support.acquia.com/hc/en-us/articles/360005373314-Proactively-organizing-files-in-subfolders>`__,
`Optimizing file paths: Organizing files in
subfolders <https://support.acquia.com/hc/en-us/articles/360005434833-Optimizing-file-paths-Organizing-files-in-subfolders>`__,
and `Using external storage for
files <https://support.acquia.com/hc/en-us/articles/360005412654-Handling-large-files#sts=Using%20external%20storage>`__.

.. _image:

Image optimization
------------------

Because images often make up a majority of the downloaded data on a
webpage, excessively large images can impact your application's
performance. Optimizing images can help alleviate this issue. For more
information about how to optimize images, see `Scoping the impact of
image
processing <https://support.acquia.com/hc/en-us/articles/360005255734-Scoping-the-impact-of-image-processing>`__.

.. |Enable CSS and JS aggregation| image:: https://cdn3.webdamdb.com/1280_y9kOSCg2A311.png?1526475772
   :width: 590px
   :height: 201px
.. |Enable CSS and JS aggregation| image:: https://cdn2.webdamdb.com/1280_k5K6gFcDPct3.png?-62169955200
   :width: 560px
   :height: 204px
.. |Enable code checks| image:: https://cdn3.webdamdb.com/1280_6X6ilZagTGU8.png?1526475762
   :width: 750px
   :height: 483px


.. |ais| replace:: \ |acquia-product:ais|\
.. _ais: /acquia-cloud/insight

.. |anc| replace:: \ |acquia-product:anc|\
.. _anc: |acquia-product:anc|

.. |as| replace:: \ |acquia-product:as|\
.. _as: /acquia-search