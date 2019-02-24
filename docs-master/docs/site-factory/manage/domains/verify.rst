.. include:: /common/global.rst

Checking your CNAME record
==========================

Custom domains

-  `Prepare </site-factory/manage/domains>`__
-  `Point </site-factory/manage/domains/point>`__
-  Verify
-  `Email </site-factory/manage/domains/email>`__
-  `Complete </site-factory/manage/domains/complete>`__

After you follow the steps to use CNAME forwarding for your `domain or
subdomain </site-factory/manage/domains/point>`__, you can check
that the CNAME record is set up correctly and pointing to your
|acquia-product:edg| website or site collection.

#. Go to the `easyWhois webpage <https://www.easywhois.com/>`__.
#. Enter your domain name and select **DNS Information Lookup**

If the record is set up correctly, the page displays your sitename with
its |acquia-product:edg| URL.

|acquia-product:edg| Support cannot help you until the records are set
and propagated. After the CNAME record is set and correct, it can still
take up to 48 hours for the records to propagate. Until that time, the
|acquia-product:edg| servers cannot find your record, which
|acquia-product:edg| requires to be able to connect your record to your
account.

Check, and if necessary, repeat the steps you took to point your domain
to your |acquia-product:edg| website or site collection until the DNS
lookup for your domain name returns a |acquia-product:edg| URL address.
You can also contact your domain registrar or DNS provider for
assistance.

`Continue to the next step > </site-factory/manage/domains/email>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
