.. include:: /common/global.rst

Adding a public key to an Acquia profile
========================================

An SSH public key is required to connect to |acquia-product:ac|
environments using SSH. You can add a public key to your Acquia profile.
If you have the proper role and permission as a member of a team, you
can then use your public key to SSH to environments of applications that
your team is assigned to. You can also use your public key to access
your |acquia-product:ac| environments using SFTP or rsync, or to access
your Git repository.

If you do not already have an SSH private/public key pair, you can
create a new one. Your SSH public key must be at least 4096 bits. For
more information, see `Generating an SSH public
key </acquia-cloud/ssh/generate>`__.

After you have added your SSH public key to your profile, you can use it
to access an |acquia-product:ac| environment, if:

-  You are a member of a team that is assigned to the server's
   application, and you have a role that includes the appropriate SSH
   permissions, or
-  You are either the *Owner* or an *Administrator* for the application.

Acquia provides the following permissions related to SSH keys:

-  Add SSH key to Git repository
-  Add SSH key to non-Production environments
-  Add SSH key to the Production environment

So, if you have just the **Add SSH key to git repository** and **Add SSH
key to non-Production environments** permissions, you can check code
into and out of your application's Git repository, as well as use SSH to
connect to your application's Development and Staging environments, but
you cannot connect to your application's Production environment using
SSH. Learn more about `teams and permissions </acquia-cloud/teams>`__.

To add a public key to your account, either click `your account page for
adding SSH keys <https://cloud.acquia.com/app/profile/ssh-keys>`__, or
complete the following steps:

#. `Click here <https://cloud.acquia.com/app/develop>`__ to open your
   Acquia account.
#. In your Acquia profile, click **SSH keys**.
#. On the SSH Keys page, click **Add SSH Keys**.
#. Enter the SSH key **Label**, such as the name of the person who owns
   the key.

   |Add SSH key|

#. Using a text editor, open your SSH public key file, and then copy the
   contents of the file to the clipboard, ensuring that you don't add
   any extra lines or spaces to the copied key.
   By default, the file name is ``~/.ssh/id_dsa.pub`` or
   ``~/.ssh/id_rsa.pub``.
   If you can't either view or edit your public key file using a text
   editor, use a command like one of the following to copy the contents
   of the key file directly to the clipboard:

   -  *Mac*

      ``pbcopy < ~/.ssh/id_dsa.pub``

   -  *Linux*

      ``sudo apt-get install xclip xclip -sel clip < ~/.ssh/id_dsa.pub``

   -  *Windows, with GitBash*

      ``clip < ~/.ssh/id_dsa.pub``

#. Paste the OpenSSH-formatted key into the **Public key** field.
   OpenSSH public keys start with ``ssh-dss`` or ``ssh-rsa``, and appear
   similar to the following example:

   .. code-block:: none
   
      ssh-dss  AAAAG1bB0us3MAAACBALFF6+dpSkO6bwbJ6BCCwbGavQPqR3JSwGWWm1ZCg2i43xz
      DTonY6+PZavGYbgbYgGySDVBbSxKIKSMGUWE8EVHiYzwiUYYaFdTYpkEyqOw/6FlDN sVjL+hb
      454dPgdYOhvjVCI683KrvTP6OMmQTCxInQpeYmyYql7dhhbg4B7AAAAFQDjLv0eP hqNrlPyX6j
      76nxF0dAf3wAAAIB4boChX4eU8YQT0Og023q44f0dlTvJFgKHa6UZDVUBDpw9 ZsVvkk703HBj
      FPxDaOJPjurZtMuGIkw8XhA4a8gWj5v9WppY8EQZcmxHoI73czcCJ53WfRrqOwM3HHZddoxEcw
      z0sTdQ3BkG7G1z0ln92raOnFPC0Ju7YCCV82yswAAAIBjGPas8fU7ycfT0dMwtQmUetcj+5qUa
      m7imzwNZ9EB29JVLbo90oVSjWJHrGMst2tGEw3VQm+a1o/ICq+nSG I9/trLbbEoTISO8MnDi/
      5UEiPApo4636EKkIahE8QKZlhlqtGZPfp0hDmn1vgKgFkp95em+Zb6r1IZJmx+/ORjcg==
      user@hostname

#. Click **Add key**.

After you add a key, there can be a delay of approximately a minute
before you can use the key to connect to your environments or
repository.

.. _team-keys:

Keys added by team members
--------------------------

If a member of your `team </acquia-cloud/teams>`__ adds an SSH key for
you, you will receive an email with the subject line
``Acquia: An SSH key labeled [labelname] was added to your Acquia account.``
informing you that the key was added.

.. _related:

Related topics
--------------

-  `Enabling SSH access </acquia-cloud/ssh/enable>`__
-  `About permissions </acquia-cloud/teams/permissions>`__

.. |Add SSH key| image:: https://cdn3.webdamdb.com/1280_MjQ5dAF1z5y6.png?1526476152
   :width: 900px
   :height: 558px
