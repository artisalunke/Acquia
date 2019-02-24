.. include:: /common/global.rst

Setting up email for your domain
================================

Custom domains

-  `Prepare </site-factory/manage/domains>`__
-  `Point </site-factory/manage/domains/point>`__
-  `Verify </site-factory/manage/domains/verify>`__
-  Email
-  `Complete </site-factory/manage/domains/complete>`__

If you use a custom domain name for your |acquia-product:edg| website or
site collection, you can configure your domain to send and receive email
using that domain name. For example, if you create a website or site
collection with a custom domain name of ``www.example.com``, you can
create email addresses associated with that domain, such as
``info@example.com``.

You will need to change your domain's MX (Mail eXchange) records to
route your incoming email to your email service provider. Most domain
registrars (the service where you bought your domain name) are also DNS
providers and provide the DNS services you need to change your mail
records for your |acquia-product:edg| website. Follow your email service
provider's instructions for changing the MX records for your domain name
to point to their servers.

If for any reason you change your custom domain name to a different DNS
provider, you must also update your MX records for the new DNS. If you
don't, your website or site collection will experience a DNS conflict,
and your email service provider will not process emails.

Notes

-  You cannot associate the MX records for |acquia-product:edg| domain
   names with email service providers.
-  |acquia-product:edg| does not provide email services, but you can
   create, manage and use email addresses for that domain name using
   Gmail as part of Google Apps.

.. _setup:

Setting up Gmail for your domain
--------------------------------

One such available email service provider is Gmail (a part of `Google
Apps <http://www.google.com/intx/en/enterprise/apps/business/index.html>`__).

To configure your custom domain to use Gmail for your domain's email:

#. Register for a Google Apps account for your domain name on the
   `Google Apps page <http://www.google.com/apps>`__.

   If you do not already own a domain name, you can also buy one as part
   of the Google Apps sign-up process. In this case, email and other
   configuration options will be set up for you to work with Google
   Apps.

#. Complete the registration process and create the administrator
   account and email address.
#. Connect to your DNS provider's management interface to create a new
   CNAME record for your domain.

   Use the information provided by the Google Apps interface for the
   **alias** of a new CNAME record in your domain name's account.

   For the **points to** or **host name** of the new CNAME record, enter
   ``google.com``.

#. Confirm the new CNAME record by entering it in a `CNAME lookup
   service <http://www.google.com/search?q=cname+lookup&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US>`__.

   Note

   Do not include "http://" in the CNAME lookup. The correct format is
   ``google1234.yourdomain.com`` (the Google string you used to create
   the CNAME record and your domain name, separated by a period).

#. Complete the configuration process for the Google Apps account.
#. Change the MX records for your domain name.

   Google Apps provides
   `instructions <http://support.google.com/a/bin/answer.py?hl=en&answer=33352>`__
   on how to change the MX records for your domain that are specific to
   a variety of DNS providers as well as a list of the mail servers and
   priorities to use when you create the MX records.

Google reference pages
~~~~~~~~~~~~~~~~~~~~~~

For more information about Google apps, MX records, and email, see the
following Google Help pages:

-  `Set up MX records for G Suite and
   Gmail <http://www.google.com/support/a/bin/answer.py?hl=en&answer=33352>`__
-  `Configuring Your MX Records: Other domain
   hosts <http://www.google.com/support/a/bin/answer.py?answer=33915>`__
-  `Troubleshoot MX
   records <http://www.google.com/support/a/bin/answer.py?answer=140038>`__

`Continue to the next step > </site-factory/manage/domains/complete>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
