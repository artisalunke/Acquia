.. include:: /common/global.rst

Information security and Acquia Support
=======================================

Information security is critical to maintaining the integrity of
websites. There may be occasions when you need to provide secure
information (such as passwords or SSL certificates) to Acquia's Support
team to provide access or installation, or for troubleshooting. These
items themselves must be kept secure and not be transmitted insecurely.

.. important::  To help ensure the security of your systems, **do not**:

                -  Email SSL certificate or passwords.
                -  Attach your files to a support ticket.

You can upload your new files (certificate, chain certs, and private
key) to the server itself, using one of the following methods:

-  `SFTP </acquia-cloud/manage/sftp>`__ - Connect, change to the
   correct directory, and then upload the files.
-  `SSH </acquia-cloud/ssh>`__ - Connect, change to the correct
   directory, create the files with a text editor, and then copy and
   paste the contents.

An example of a secure directory you can use is:

``/mnt/gfs/sitename.prod/ssl/new_cert``

After you have completed this, you can file a new support request to
have the files moved.

If you are still unsure where to place your files, `contact Acquia
Support </support#contact>`__ and we will advise you how to upload your
SSL certificate and private key securely.

.. note:: If you send your SSL certificate and private key through email or attach
          them to a ticket, you may be asked to `revoke and rekey your
          certificate </acquia-cloud/ssl/cert#revoke>`__ for your own protection.
