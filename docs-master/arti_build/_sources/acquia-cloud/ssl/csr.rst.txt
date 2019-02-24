.. include:: /common/global.rst

Generating a certificate signing request (CSR)
==============================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/ssl/csr/*

.. container:: internal-navigation

   **Using SSL**

   * :doc:`Introduction </acquia-cloud/ssl>`
   * Generate
   * :doc:`Purchase </acquia-cloud/ssl/purchase>`
   * :doc:`Manage </acquia-cloud/ssl/cert>`


The first step in obtaining an SSL certificate to use with
|acquia-product:ac| is to generate a Certificate Signing Request, or
CSR. The CSR contains information about your organization and website
that a Certificate Authority can use to generate the appropriate SSL
certificate for your website.

If you already have an SSL certificate, or if you choose to generate a
CSR some other way (such as `using the command
line </acquia-cloud/ssl/csr/cli>`__), you can skip this page. However,
only CSRs generated using the |acquia-product:ui| are managed and
displayed in the |acquia-product:ui| on the **SSL** page.

To generate a CSR:

#. Sign in to the |cloud-ui| as
   a user with the necessary
   `permissions </acquia-cloud/ssl#permissions>`__.
#. Select your organization, application, and environment and then, in
   the left menu, click **SSL**.
#. On the SSL page, click **Generate CSR**.

   |Enter information to generate a CSR|

#. On the **Generate new certificate signing request** page, enter the
   following information:

   -  **Country** - Use the standard two-letter ISO country code for the
      country where your organization is located. For example, *US* or
      *ZA*
   -  **State, province, or region** - Use the full state or province
      name, without abbreviation. For example, *California*, not *CA*,
      and *New Brunswick*, not *NB*
   -  **Locality** - Use the city or town name, without abbreviation
   -  **Organization or company** - Use the full legal name of the
      organization or company that owns the domain name
   -  **Department or organizational unit** - Optional. Use the name of
      the department or organizational unit for the domain
   -  **Common name** (domain name) - Enter the fully qualified domain
      name that visitors use to reach your website, without the
      ``http://`` or ``https://`` protocol element. For example, to
      secure ``https://www.example.com``, enter ``www.example.com`` or
      ``*.example.com`` for a wildcard certificate
   -  **Subject alternative name(s)** - Optional. Enter additional
      domain names, separated by commas — for example,
      ``www.example.net, www.example.org``. Adding additional domain
      names will generate a CSR appropriate for a UCC (Unified
      Communications Certificate) SSL certificate

#. Click **Generate CSR**.

|acquia-product:ac| generates a CSR, based on the information you
provided.

.. _pem:

Using a CSR to obtain an SSL certificate
----------------------------------------

All the CSRs that have been generated for an environment are listed on
the **SSL** page. You need to provide the CSR in encoded format to your
SSL certificate vendor in order to obtain an SSL certificate. To get the
CSR in encoded format:

#. On the **SSL** page, under **Certificate signing requests**, click
   **View** to view the CSR.
#. On the **SSL certificate signing request** page, on the PEM line,
   click **Show**.

   |Displaying the encoded CSR|

#. |acquia-product:ac| displays the encoded CSR. Copy the encoded CSR
   and provide it to your SSL certificate vendor in the vendor's
   certificate purchase process.

.. _next:

Next step
---------

After you generate and copy the CSR, use it to `obtain an SSL
certificate </acquia-cloud/ssl/purchase>`__.

.. |Enter information to generate a CSR| image:: https://cdn3.webdamdb.com/md_MHEvFEDxs9C8.png?1526476095
   :alt: Enter information to generate a CSR
.. |Displaying the encoded CSR| image:: https://cdn2.webdamdb.com/md_cPF3hPoe4e36.png?1526476081
   :alt: Displaying the encoded SSR

.. |cloud-ui| replace:: \ |acquia-product:ui|\ 
.. _cloud-ui: https://cloud.acquia.com

