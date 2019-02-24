.. include:: /common/global.rst

SSH and RSA key warnings after a server relaunch
================================================

Every server with SSH capabilities has a unique RSA key fingerprint.
When a server is relaunched, this key can change because of a network
card change, or more likely, because the server was replaced and it is
running on entirely new hardware. When this happens and you attempt to
connect to the server using SSH, you may see a warning similar to the
following message:


.. code-block:: none

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
    @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!                                                    @ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
    IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY! Someone could be 
    eavesdropping on you right now (man-in-the-middle attack)! It is also 
    possible that a host key has just been changed. The fingerprint for the RSA
    key sent by the remote host is 
    aa:bb:cc:dd:ee:ff:11:22:33:44:55:66:77:88:99:00. Please contact your 
    system administrator. Add correct host key in 
    /home/username/.ssh/known_hosts to get rid of this message. Offending RSA 
    key in /home/username/.ssh/known_hosts:24 Password authentication is 
    disabled to avoid man-in-the-middle attacks. Keyboard-interactive 
    authentication is disabled to avoid man-in-the-middle attacks. Agent 
    forwarding is disabled to avoid man-in-the-middle attacks.

This warning sounds much more dire than the issue is. In most cases, the
only thing that happened is just a change to the server hardware. Use
one of the following methods to prevent this message from recurring:

-  **Remove the original host key using ssh-keygen.**

   Run the following command to remove the RSA fingerprint for the
   previous hardware:

   ``ssh-keygen -R [hostname]``

   where ``[hostname]`` is the hostname for your previous server.

-  **Edit or remove the known_hosts file.**

   On a UNIX system, you can remove the file ``~/.ssh/known_hosts``
   entirely; however, this will cause every server you SSH into to
   prompt you for a key acceptance. You can instead edit the file and
   remove the old server key. Be sure to back up the file before you
   edit it. Windows users may find the same file at
   ``c:\users\username\.ssh\known_hosts``, especially if you are using
   something like `Git
   Bash <https://openhatch.org/missions/windows-setup/install-git-bash‎>`__.

-  **Turn off StrictHostKeyChecking.**

   Add ``StrictHostKeyChecking no`` to your ``~/.ssh/config`` file, or
   ``-o StrictHostKeyChecking=no`` to the SSH command line.

`Contact Acquia Support </support#contact>`__ if you wish to verify the
fingerprint.

The next time you sign in, you should see a prompt asking you to approve
adding the new RSA key fingerprint to your list of known hosts.
