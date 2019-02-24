.. include:: /common/global.rst

Using path-based domain names
=============================

Custom domains

-  `Prepare </site-factory/manage/domains>`__
-  `Point </site-factory/manage/domains/point>`__
-  `Verify </site-factory/manage/domains/verify>`__
-  `Email </site-factory/manage/domains/email>`__
-  `Complete </site-factory/manage/domains/complete>`__

As described in `Adding custom domains to your
site </site-factory/manage/domains>`__, you can add a custom
domain name to an |acquia-product:edg| site, such as ``www.example.com``
or ``store.example.com``. |acquia-product:edg| also supports using
path-based custom domains for sites. These are custom domains in the
form ``www.example.com/foo`` and ``www.example.com/bar``. This enables a
greater choice in custom domain names, as well as letting you use a
single SSL certificate to handle multiple sites under the same URL.

.. _reqs:

Important considerations and requirements
-----------------------------------------

To use path-based custom domains, you must keep in mind the following
considerations:

-  Each site must use the |acquia-product:edg| Connector module
   8.x-1.33, 7.x-1.33 or later.
-  All sites that come under the same URL must exist on the same Site
   Factory Stack. For example, if you have a site on one Stack with the
   domain ``www.example.com``, you cannot have a site on a different
   Stack with the domain ``www.example.com/full``.
-  The path for a site cannot be more than one level below the parent
   URL. For example, you can have a site at ``www.example.com/gibbous``,
   but not at ``www.example.com/phases/gibbous``.
-  For each site that uses a path-based custom domain, you must create a
   symbolic link (symlink) in the docroot. For more information, see
   `Creating symbolic links for path-based custom domains <#symlink>`__.

.. _add:

Adding a path-based custom domain
---------------------------------

You add a path-based custom domain in the |acquia-product:sfi| in the
same way you add any custom domain. See `Pointing your domain
name </site-factory/manage/domains/point>`__ for the available
procedures.

.. _symlink:

Creating symbolic links for path-based custom domains
-----------------------------------------------------

Suppose your sites are at paths under ``www.example.com``, and you want
to create symbolic links for sites at ``www.example.com/gibbous`` and
``www.example.com/crescent``.

#. In your code repository, change directories to your docroot:

   ``cd docroot``

#. Enter these commands to create the symbolic links:

   ``ln -s . gibbous ln -s . crescent``

#. Commit the changes in your code repository.

.. _conflict:

Resolving domain name conflicts
-------------------------------

If you try to assign a domain name that is already in use for a site,
you will see an error message like this:

    **Oops! Looks like there was a problem** A domain can belong only to
    a single server group. This domain is already assigned to the
    ``xyz654`` server group via the ``example`` site. This site is
    served via the ``abc123`` server group.

To resolve this error, either choose a different domain name, or remove
the conflicting domain name from the other site. It may take several
minutes after a conflicting domain name is removed before it becomes
available for re-use.

.. _dns:

DNS error message
-----------------

When you successfully add a path-based domain to a site, the
|acquia-product:sfi| displays a message like this:

    Your domain name has been successfully added to the site. The domain
    ``example.com/gibbous`` does not have a DNS record that points to
    this site. Confirm the domain and contact your DNS provider to add a
    CNAME or A record to point to ``example.gibbous.sfdev.acquia.com``.

If you have already pointed your DNS records to your Site Factory site,
you can ignore this message. A `known
issue </site-factory/known-issues>`__ in |acquia-product:edg| prevents
this |acquia-product:sfi| page from properly performing DNS lookups for
path-based domains.
