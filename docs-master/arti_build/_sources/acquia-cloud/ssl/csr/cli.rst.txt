.. include:: /common/global.rst

Creating CSR files from the command line
========================================

A `Certificate Signing
Request <https://en.wikipedia.org/wiki/Certificate_signing_request>`__
(CSR) file is a block of encrypted text that is generated on the server
that the certificate will be used on. It contains information that will
be included in your SSL certificate, such as your organization name,
common name (domain name), locality, and country. You cannot create an
SSL certificate without first generating a CSR file.

.. admonition:: Recommended method

   CSRs generated from the command line are neither managed nor displayed
   on the |acquia-product:ac| interface's SSL page. For information on
   creating CSRs by using the SSL Setup wizard in |acquia-product:ac|, see
   `Generating a Certificate Signing Request </acquia-cloud/ssl/csr>`__.

.. _steps:

Steps for creating a command-line CSR
-------------------------------------

To generate a CSR, complete the following steps:

#. In the directory ``/mnt/gfs/[sitename].prod/ssl`` (where
   ``[sitename]`` is your sitename in |acquia-product:ac|), copy the
   following two files (if they exist) into a new directory for backup:

   -  ``[sitename].conf``
   -  ``private.key``

#. Create a file named ``domains.txt`` that contains a list of all the
   domains that you want covered by your SSL certificate.
#. Edit the ``[sitename].conf`` file, and then delete everything
   following the ``[alt_names]`` section header.
#. Save the ``[sitename].conf`` file.
#. Run the following command to add the updated list of domains to the
   ``[sitename].conf`` file:

   .. code-block:: none

     i=1; for domain in $(cat domains.txt) ; do echo "DNS.$i = $domain" ; ((i++)) ;  done >> [sitename].conf

#. To generate the CSR file, run the following command:

   .. code-block:: none

      openssl req –new –nodes –sha256 –out [sitename].csr –config [sitename].conf –key private.key

   Even though the information in the ``[sitename].conf`` file has
   prepopulated the default fields with data, you are prompted to enter
   details for the CSR file. To continue, press the Enter key.

#. Use the following commands to ensure that your ``private.key`` and
   CSR files match.

   .. code-block:: none

      openssl req noout modulus in [sitename].csr | openssl md5
      openssl rsa noout modulus in private.key | openssl md5

   The files should have matching hashes similar to the following
   example:

   .. code-block:: none

      (stdin)= 9fb4c34545e3f8140db44b250cd001e0
