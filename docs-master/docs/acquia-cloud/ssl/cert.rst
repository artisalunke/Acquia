.. include:: /common/global.rst

Managing SSL certificates
=========================

.. container:: internal-navigation

   **Using SSL**

   * :doc:`Introduction </acquia-cloud/ssl>`
   * :doc:`Generate </acquia-cloud/ssl/csr>`
   * :doc:`Purchase </acquia-cloud/ssl/purchase>`
   * Manage

Using the |acquia-product:ui| **SSL** page, you can perform several
tasks to manage an environment's SSL certificates and CSRs, including:

-  `Installing an SSL certificate <#install>`__
-  `Viewing an SSL certificate <#view>`__
-  `Activating an SSL certificate <#activate>`__
-  `Removing an SSL certificate <#remove>`__

.. _install:

Installing an SSL certificate
-----------------------------

After you have obtained an SSL certificate for an environment (as
described in `Obtaining an SSL
certificate </acquia-cloud/ssl/purchase>`__) you can use the
|acquia-product:ui| **SSL** page to install the certificate on an
environment. There are two ways to install an SSL certificate, depending
on whether you used a CSR you generated with the |acquia-product:ui| or
whether you obtained the certificate some other way.

.. note::  

   By default, the following SSL private keys and files are stored in
   ``/mnt/gfs/site.env/ssl``:

   -  ``ca.crt``
   -  ``ssl.crt``
   -  ``ssl.csr``
   -  ``ssl.key``

At this time, you may want to verify the validity of your SSL
certificate before you upload or attempt to activate it on
|acquia-product:ac|. For assistance, see `Verifying the validity of an
SSL
certificate <%5Bacquia-product:kb%5Darticle/verifying-validity-ssl-certificate>`__.

.. _csr:

Installing an SSL certificate based on a CSR you generated with the |acquia-product:ui|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install an SSL certificate that is based on a CSR you generated with
the |acquia-product:ui|:

#. Sign in to the |cloud-ui| as
   a user with the necessary
   `permissions </acquia-cloud/ssl#permissions>`__.
#. Select your organization, application, and environment, and then, in
   the left menu, click **SSL**.
#. | On the **SSL** page, click the **Install SSL certificate** link for
     the CSR.

   |Install an SSL certificate|

#. On the **Install new SSL certificate** page, enter the following
   information about the certificate:

   -  If you want this certificate to use the `legacy (ELB-based) SSL
      model </acquia-cloud/ssl#sni>`__, select **Install legacy SSL
      certificate**. See `Standard certificates and legacy
      certificates </acquia-cloud/ssl#sni>`__ for a summary of some of
      the differences between standard SSL certificates and legacy SSL
      certificates.
   -  Optionally, in the **Label** field, enter a label that will help
      you identify this certificate in the |acquia-product:ui|. If you
      selected **Install legacy SSL certificate**, there is no label
      field, since you can only have a single legacy SSL certificate on
      an environment.
   -  In the **SSL certificate** field, enter the SSL certificate in PEM
      format. Private key files must be unencrypted and non-password
      protected, or the certificate cannot be deployed. The certificate
      should look something like this, but much longer:

      .. code-block:: none

            -----BEGIN CERTIFICATE-----
            MIIFWzCCBEOgAwIG1bBouS1O/ob8scTviFvVCKVzzANBgkqhkiG9w0BAQsFADBw
            MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3
            d3cuZGlnaWNlcnQuY29tMS8wLQYDVQQDEyZEaWdpQ2VydCBTSEEyIEhpZ2ggQXNz
            dXJhbmNlIFNlcnZlciBDQTAeFw0xNjA5MTUwMDAwMDBaFw0xNzEyMDgxMjAwMDBa
            MGYxCzAJBgNVBAYTAlVTMRYwFAYDVQQIEw1NYXNzYWNodXNldHRzMQ8wDQYDVQQH
            Us8/azXp7pJ75vyNi/tuLbLSQbwqNcEo+jBXPysGdA==
            -----END CERTIFICATE-----

   -  The |acquia-product:ui| fills the **SSL private key** field with
      the private key for this certificate in PEM format. Do not modify
      this key.
   -  If the certificate has any CA intermediate certificates, enter
      them in the **CA intermediate certificates** field in PEM format.
      CA intermediate certificates must be entered in the proper order.

#. Click **Install**.

.. _button:

Installing an SSL certificate not based on an Acquia-generated CSR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install an SSL certificate that is *not* based on an Acquia-generated
CSR:

#. `Sign in <https://cloud.acquia.com>`__ to the |acquia-product:ui|  as
   a user with the necessary
   `permissions </acquia-cloud/ssl#permissions>`__.
#. Select your organization, application, and environment, and then, in
   the left menu, click **SSL**.
#. On the **SSL** page, click **Install SSL Certificate**.

   |Install an SSL certificate|

#. On the **Install SSL certificate** page, enter the following
   information about the certificate:

   -  If you want this certificate to use the `legacy (ELB-based) SSL
      model </acquia-cloud/ssl#sni>`__, select **Install legacy SSL
      certificate**.
   -  In the **Label** field, enter a label that will help you identify
      this certificate in the |acquia-product:ui|. If you selected
      **Install legacy SSL certificate**, there is no label field, since
      you can only have a single legacy SSL certificate on an
      environment.
   -  In the **SSL certificate** field, enter the SSL certificate in PEM
      format. The certificate should look something like this, but much
      longer:

      .. code-block:: none

            -----BEGIN CERTIFICATE-----
            MIIFWzCCBEOgAwIG1bBouS1O/ob8scTviFvVCKVzzANBgkqhkiG9w0BAQsFADBw
            MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3
            d3cuZGlnaWNlcnQuY29tMS8wLQYDVQQDEyZEaWdpQ2VydCBTSEEyIEhpZ2ggQXNz
            dXJhbmNlIFNlcnZlciBDQTAeFw0xNjA5MTUwMDAwMDBaFw0xNzEyMDgxMjAwMDBa
            MGYxCzAJBgNVBAYTAlVTMRYwFAYDVQQIEw1NYXNzYWNodXNldHRzMQ8wDQYDVQQH
            Us8/azXp7pJ75vyNi/tuLbLSQbwqNcEo+jBXPysGdA==
            -----END CERTIFICATE-----

   -  In the **SSL private key** field, enter the private key for this
      certificate in PEM format.
   -  If the certificate has any CA intermediate certificates, enter
      them in the **CA intermediate certificates** field in PEM format.
      CA intermediate certificates must be entered in the proper order.

#. Click **Install**.

.. note::  

   Intermediate certificates need to be entered in a single file, in the
   proper order, beginning with the intermediate certificate closest to
   your website's certificate and ending with the intermediate certificate
   closest to the root certificate. This should be the same as the order
   that they were provided to you by your certificate vendor.

.. _view:

Viewing an SSL certificate
--------------------------

After you have installed an SSL certificate on an environment, you can
view it on the **SSL** page. The **SSL certificates** section lists all
the installed certificates, their active status, and any associated CSR.
Click **View** to see details about an SSL certificate, including:

-  The certificate's label (the name you identified it with when you
   installed it)
-  Whether the certificate is a `legacy
   certificate </acquia-cloud/ssl#sni>`__
-  The certificate's active status
-  The certificate's expiration date
-  The domains associated with the certificate

Click **Show** to view the PEM encoded certificate, CA chain (CA
intermediate certificates), or private key.

.. _activate:

Activating an SSL certificate
-----------------------------

After you have installed an SSL certificate on an environment, you must
activate it before it starts working with HTTPS requests to the
environment. An environment can have only one active SSL certificate at
a time. Activating a new certificate will deactivate all other
certificates on the environment.

To activate an SSL certificate:

.. note::  

   -  Standard (SNI) certificates must be activated before use.
   -  Legacy certificates installed on the elastic load balancer (ELB) will
      immediately override the previous certificate on the ELB.
   -  It is possible to have a standard and a legacy certificate active at
      the same time. Activating a standard certificate will deactivate any
      other non-legacy certificates.

#. On the **SSL** page, under **SSL certificates**, locate the
   certificate you want to activate and click **Activate**.
#. In the **Activate certificate** dialog, enter your Acquia account
   password to confirm, and then click **Activate**.

   |Activating an SSL certificate|

The SSL certificate activation should take less than five minutes, after
which the SSL webpage will display the certificate's active status.

.. _deactivate:

Deactivating an SSL certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can deactivate an active SSL certificate at any time. You must
deactivate an active certificate before you can remove it.

To deactivate an SSL certificate:

#. On the **SSL** page, under SSL certificates, locate the active
   certificate you want to deactivate and click **Deactivate**.
#. In the **Deactivate certificate** dialog, enter your Acquia account
   password to confirm, and then click **Deactivate**.

.. _remove:

Removing an SSL certificate
---------------------------

You can delete an inactive SSL certificate from an environment at any
time. Before you remove an active SSL certificate, you must first
`deactivate <#deactivate>`__ it.

.. important:: 

   Removing certificates from |acquia-product:ac| is *permanent*, and will
   deprovision the Elastic Load Balancer (ELB) assigned to the
   subscription.

   Before you remove a `legacy certificate </acquia-cloud/ssl#sni>`__, be
   sure to point the DNS on all domains to your load balancers, as using
   CNAME to point DNS to the ELB can cause downtime for your environment.

To remove an SSL certificate, complete the following steps:

#. Sign in to the |acquia-product:ac| interface, and then go to the
   application you want to modify.
#. Select the environment from which you want to remove a certificate,
   and click **SSL** in the left menu.
#. In the **SSL certificates** section, locate the certificate that you
   want to remove, and then click its **Remove** link.
   |acquia-product:ac| displays a **Remove certificate** dialog box.
#. In the available field, enter your Acquia account password to confirm
   the deletion of the certificate.
#. Click **Remove** in the dialog box to permanently remove the
   certificate from |acquia-product:ac|.

.. _revoke:

Revoking a certificate
~~~~~~~~~~~~~~~~~~~~~~

If you no longer want a removed SSL certificate to function, you should
also revoke the old certificate to prevent an attacker’s website from
masquerading as your own. Each SSL certificate vendor has different
procedures to perform an certificate revocation. Please follow the
instructions your SSL certificate vendor provides. Here are the
procedures for two common vendors:

-  *Verisign* - `Revoke an ECA
   Certificate <https://eca.verisign.com/client/revoke.htm>`__
-  *Digicert* - `EV SSL Certificate Revocation
   Requests <http://www.digicert.com/ev-ssl-revocation.htm>`__

.. _dns:

Configuring DNS settings with legacy SSL
----------------------------------------

If you install a legacy SSL certificate, |acquia-product:ac| creates a
new DNS domain name for your environment that ends with
``elb.amazonaws.com``. You then need to configure your DNS settings to
create a CNAME record pointing your environment's domain name to the
|acquia-product:ac| domain name. For example:

.. code-block:: none

   www.example.com CNAME 1234-4321.us-east-1.elb.amazonaws.com

This |acquia-product:ac| domain name is the name of your website's
Amazon Elastic Load Balancer (ELB) instance and is listed in the
|acquia-product:ui| Domain page for the environment. Don't use a DNS A
Record to point to the underlying IP address of the ELB, since the IP
address may change from time to time.

The ELB routes traffic to the |acquia-product:ac| load balancers for
your Production environment. If your other environments (Dev and Stage)
use the same load balancers, then the ELB and SSL certificate will work
for those environments as well.

.. |Install an SSL certificate| image:: https://cdn3.webdamdb.com/md_Y9mxLVU10QI0.png?1526475777
   :alt: Install an SSL certificate
.. |Activating an SSL certificate| image:: https://cdn3.webdamdb.com/md_gXCXH2xVdrW8.png?1526475462
   :alt: Activating an SSL certificate

.. |cloud-ui| replace:: \ |acquia-product:ui|\ 
.. _cloud-ui: https://cloud.acquia.com
