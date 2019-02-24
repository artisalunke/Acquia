.. include:: /common/global.rst

Starting with an |acquia-product:ac| site
=========================================

If you already have a Drupal website that's hosted on
|acquia-product:ac|, you can import it into |acquia-product:add| so you
can develop it locally, then sync your changes back to
|acquia-product:ac|.

.. _import:

Importing from |acquia-product:ac|
----------------------------------

To import a website from |acquia-product:ac|:

#. Click the **+** button, and then click **Add Acquia Cloud sites**. If
   you are starting from the Welcome window shown in `Getting
   started </dev-desktop/start>`__, you will skip this step.
#. Enter the email address and password that you use to log in to your
   |acquia-product:ac| subscription, and then click **Log in**.

   |acquia-product:add| displays all of the websites you can access on
   |acquia-product:ac|.

   |Select a website|

#. Select the |acquia-product:ac| website name and environment, and then
   click **Clone this site locally and use it in Dev Desktop**.

   The **Clone Acquia Cloud Site Locally** dialog appears.

   |Cloning a local site copy|

#. Accept or modify the following values:

   -  **Local site name**
   -  **Use PHP**
   -  **New database name**

#. Optionally, clear the **Clone Cloud database** check box, the **Clone
   Cloud files** check box, or both check boxes. If your
   |acquia-product:ac| website has a very large database or has many
   files, it can take a long time to copy the website into your local
   |acquia-product:add| website. By clearing these check boxes, you can
   avoid this delay if you don't need local copies of the database or
   files.
#. Optionally, select the **Sanitize database** check box to scrub the
   database of user emails and passwords. This is a best practice for
   security, so that your local website never includes real user emails
   and passwords. For more information, see `Sanitizing the database on
   import </dev-desktop/start/scrub>`__.
#. Click **OK**.
#. If you have not already done so, enter the location of your **Private
   key file**, and then click **OK**.

   |Enter private key location|

   Communication with your |acquia-product:ac| server is protected with
   a private key. For more information, see `|acquia-product:ac|
   credentials </dev-desktop/cloud/key>`__.

|acquia-product:add| then checks your local computer for the location of
your version control system (Git).

Important Windows note

Windows does not support using the colon character (:) in file paths.
Also, Git on Windows does not support paths longer than 260 characters.
If the website you are importing either uses any colons in a file or
directory name or has any paths longer than 260 characters in the code
repository or file storage, the import will fail with a message similar
to ``Git Error: Invalid path for filesystem``.

|acquia-product:add| then imports the website from |acquia-product:ac|
into |acquia-product:add|. You can now work with the website either
locally, in |acquia-product:add|, or on the cloud in
|acquia-product:ac|. Read `Working with your
sites </dev-desktop/sites>`__ and `Working with sites on
|acquia-product:ac| </dev-desktop/cloud/working>`__ for more
information.

|Site after import|

Note

One instance of |acquia-product:add| can connect to just one
|acquia-product:ac| account. If you need to work with more than one
|acquia-product:ac| account, you can install a second instance of
|acquia-product:add| using a different installation folder, a different
Apache web server port, and a different MySQL database server port.

.. |Select a website| image:: https://cdn2.webdamdb.com/1280_YMwSRuaNuHY0.png?1526475640
   :width: 590px
   :height: 282px
.. |Cloning a local site copy| image:: https://cdn3.webdamdb.com/1280_IciH4EChodd2.png?1526475761
   :width: 590px
   :height: 318px
.. |Enter private key location| image:: https://cdn3.webdamdb.com/1280_cjxA1Wd5Iu12.png?1526475855
   :class: shadow bord
   :width: 590px
   :height: 146px
.. |Site after import| image:: https://cdn3.webdamdb.com/1280_oOPw43Bz3VW6.png?1526476024
   :width: 590px
   :height: 446px
