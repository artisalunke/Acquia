.. include:: /common/global.rst

Issue connecting with SSH in PHP using keys with passphrases
============================================================

`A bug exists in PHP <https://bugs.php.net/bug.php?id=58573%7C>`__ that
prevents users from connecting to a remote server using SSH with a
passphrase. You are able to connect using the command line, but may
encounter problems with the same key pair when connecting using PHP.
This can also potentially be a problem if you're using `SSH tunneling
for server-side
applications <%5Bacquia-product:kb%5Darticles/ssh-tunneling-server-side-applications>`__.

.. note::  

   You can not SSH directly into |acquia-product:ac| database servers
   (``fsdb`` and ``fsdbmesh`` machines), but you can SSH into web servers.

The version of PHP that is making this connection (whether it's running
locally or on a remote server) needs the `SSH2 PHP
extension <http://php.net/manual/en/book.ssh2.php>`__.

Here's an example of some PHP you might use to try to connect to an
|acquia-product:ac| server:

.. code-block:: php

   <?php 
   
      $conn_id = ssh2_connect("srv-NNNN.devcloud.hosting.acquia.com",22, array('hostkey'=>'ssh-rsa'));
      
      if (ssh2_auth_pubkey_file($conn_id, 'username','/Users/usename/.ssh/key.pub','/Users/username/.ssh/key','passphrase')) {
         echo "Public Key Authentication Successful\n";
         } else {
         die('Public Key Authentication Failed');
      }
   
   ?>

If the ``key.pub`` file requires a passphrase, the connection attempt
can fail with this error:

.. code-block:: none

   PHP Warning:  ssh2_auth_pubkey_file(): Authentication failed for <username> 
   using public key: Callback returned error in <path_to_script> 
   line <line_number>

This is still an open bug with PHP. To work around this on
|acquia-product:ac|, create a public/private key pair without a
passphrase. Then, `add it to your Acquia
profile </acquia-cloud/ssh/enable/add-key>`__ using the
|acquia-product:ui|. You can then use the key, using
``ssh2_auth_pubkey_file()`` (as in the preceding example) without the
optional passphrase parameter.
