.. include:: /common/global.rst

Using multi-region failover
===========================

Through multi-region failover, Acquia provides Continuity-as-a-Service
using a hot cloud recovery model. With multi-region failover, your
Production application has a cloned version of its full stack in a
secondary failover region. In the event of a failure or substantial
impairment in your primary region, your application can be switched
immediately to the clone in the secondary region. Multi-region failover
is available for |acquia-product:ace| applications as an add-on service
at an extra cost.

To use multi-region failover, you must also use a CDN service, such as
|edgelink|_. This is important to
avoid an interruption in service; the CDN can continue to serve cached
content while your application is switching over to the secondary
region.


.. |edgelink| replace:: \ |acquia-product:cfc|\ 
.. _edgelink: /acquia-cloud/edge

Multi-region failover on |acquia-product:ac| supports only a single
application on a single codebase. Multi-region failover does not support
multisites or multiple codebases on a common production server cluster,
due to the difficulties associated with properly re-syncing these types
of applications after a full or partial failover.

.. _how:

How it works
------------

|Multi-region failover architecture|

When you choose multi-region failover for your |acquia-product:ace|
application, Acquia duplicates your Production environment in a
different region from your primary region. For example, if your
application is hosted in the *US-East* region, your secondary
application might be created in the *US-West* region. The secondary
hardware cluster is configured to receive the same code deployments as
the primary cluster, so that it is always running the same code. In
addition, multi-region failover uses database replication to keep the
primary and secondary database servers in sync in both the primary and
secondary regions. This means that any changes to the database in either
the primary or secondary region will immediately sync to the database
servers in the other region.

During normal operations, your application continuously runs a special
one-way ``rsync`` process on the primary region application, which
ensures that any files added to the primary region are also sent to the
servers in the secondary (failover) region.

The combination of the synced code, databases, and files means that the
failover region and primary region are functionally identical. The main
difference, aside from the location of the hardware, is that each region
is assigned its own distinct Elastic IP (EIP) address.

.. _failover:

The failover process
--------------------

In the event of an emergency in your application's primary region, the
Acquia multi-region failover configuration ensures that there is an
alternative functional version of your live production application. This
might be an event that causes the primary hosting region to be, in part
or in whole, impaired or inoperative in such a way that Acquia’s support
teams cannot restore full service in the primary region immediately or
within a reasonable amount of time.

The multi-region failover configuration should not to be used to reduce
the impact of routine maintenance or upsizes, to mitigate the impact of
high-traffic events if your primary region’s hardware reaches capacity,
or to attempt to work around incidents where adverse code, file, or
database changes have been deployed to your Production application.

In the event of an emergency, you can begin the failover process at any
time; you do not need Acquia's assistance. If your application uses
|acquia-product:cfc|, you can request that Acquia Support assist with
the failover process. In any case, you should notify Acquia as soon as
possible, so that Acquia does not take any conflicting actions in
addressing the emergency.

To initiate the failover process, configure your application's CDN
settings to point to the Elastic IP address of the secondary region,
instead of the primary region. You can find the Elastic IP addresses on
the page of the |acquia-product:ui|. After the CDN changes take effect,
requests to the application will be handled by servers in the secondary
region, instead of the primary region.

Because the caches in the secondary region will be empty at first,
performance may be slower immediately following failover until the
caches rebuild.

.. _cron:

Cron and failover
~~~~~~~~~~~~~~~~~

Cron jobs in |acquia-product:ac| are set to run on servers in the
primary region. Upon failover, Acquia Support can edit cron jobs to run
in the secondary region instead of the primary region. Cron jobs do not
automatically transfer over to servers in the secondary region upon
failover. For more information, see `Using scheduled jobs to maintain
your application </acquia-cloud/manage/cron>`__.

.. _operating:

Operating while in failover
---------------------------

While your application is being served from the secondary region, many
common |acquia-product:ac| workflow tasks may not function properly. The
secondary region includes a clone of your Production environment, but
not other environments (such as Development and Staging). Workflow tasks
that are designed to facilitate communications between servers in the
same region won't work between environments in different regions. In
other instances (such as full or partial region-wide failures), tasks
may fail because Acquia’s code repository or task management servers in
those regions are also impaired.

.. important:: 

   For these reasons, while your application is operating in the secondary
   region, do not attempt any file or database copy, code commit, or code
   deployment tasks.

.. _failback:

The failback process
--------------------

After the emergency in the primary region has been resolved, you will
need to restore your application to its previous configuration so that
it is again served from the primary region. This process is called
*failback*.

Before initiating failback to the primary region, notify Acquia Support
to confirm the date and time of the failback. At the time of the
failback, Acquia will perform one final manual sync of the application’s
files between the secondary and primary regions to ensure that there are
no issues or inconsistencies. Acquia will then authorize you to proceed
with the CDN failback to the primary region, pointing the CDN settings
to the Elastic IP address of the primary region. If your application
uses |acquia-product:cfc|, you can request that Acquia Support assist
with the failback.

Similar to when your application first fails over to the secondary
region, caches in the primary region may be stale at the time of
failback, so site performance may be reduced while the caches rebuild.

.. _ssl:

SSL and multi-region failover
-----------------------------

If you use SSL with your application, you can either provide Acquia with
a single functional SSL certificate for installation on the dedicated
load balancers in both the primary and secondary region, or Acquia can
purchase an SSL certificate on your behalf and install it in both
regions.

Acquia strongly recommends the `standard </acquia-cloud/ssl#sni>`__
method for SSL certificates.

.. _multi:

|acquia-product:as| and multi-region failover
---------------------------------------------

If you use |searchlink|_, you can also use it
in a multi-region failover configuration, at an additional cost. If you
choose to do this, Acquia establishes a dedicated search farm in both
the primary and the secondary regions, with a separate search key for
each region.

.. |searchlink| replace:: \ |acquia-product:as|\ 
.. _searchlink: /acquia-search

To switch |acquia-product:as| to the secondary region during a failover,
configure your application to use the search key for the secondary
region by entering the secondary region's key on your Drupal
application's ``admin/config/system/acquia-agent/credentials`` page. The
application in the secondary region must then be re-indexed.

.. _test:

Testing the failover process
----------------------------

Acquia tests multi-region failovers during the setup process. After this
functionality is in place, Acquia does not support any additional
testing, and will not provide assistance with failovers or failbacks
unrelated to an emergency event in your primary region.

.. |Multi-region failover architecture| image:: https://cdn4.webdamdb.com/1280_2ZiEUw6un0I9.png?1526476108
   :class: no-sb
   :width: 590px
   :height: 327px
