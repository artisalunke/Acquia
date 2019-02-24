.. include:: /common/global.rst

Generating an SSH key
=====================

To synchronize a local website with `Acquia Cloud </acquia-cloud>`__, you need to register an SSH key in your Acquia user profile. If you don't already have one, you can generate a public/private key pair using |acquia-product:add|.

.. note::

   You will need to update to a version of |acquia-product:add| released on March 21, 2016 or later to generate the 4096 bit keys required to connect to |acquia-product:ac|.

To generate an SSH key pair in |acquia-product:add|, complete the following steps:

#. On the **Acquia Dev Desktop** menu, click **Preferences**.
#. On the **General** tab, click **Generate**.

   |Generating a key pair|

   The SSH key pair dialog box appears with your new public key.

   |Copy the public key|

#. Click **Copy public key to clipboard**. You can use the copied public key to register it with |acquia-product:ac|.
#. Use the **Key password** field to enter an optional password for your key.

   .. note::

      Entering a key password makes your SSH key more secure by requiring you to use the key password whenever you use the key. If you do not associate a password with your key, someone who obtains your key could use it to access certain resources, including your |acquia-product:ac| websites. Additionally, you may need a password for your key for `Payment Card Industry Data Security Standard (PCI DSS) compliance </acquia-cloud/ssh/generate#requirements>`__.

#. Click **Save key pair**, and in the dialog box that appears, determine the location and file name of the key pair.
#. Click **Save** to save the key pair file.
#. Click **Close** to close the SSH key pair dialog box.

You now have an SSH key pair that you can use with other services, including |acquia-product:ac|.

For information about adding the key that you created to |acquia-product:ac|, see `Adding a public key </acquia-cloud/ssh/enable/add-key>`__. If you copied the key to your clipboard in step 3, you can skip step 5 in the |acquia-product:ac|-key adding process.

.. _replace:

Replacing old keys
------------------

If you previously had SSH keys and used the preceding process to create new keys, you may need to refresh your |acquia-product:ac| websites in |acquia-product:add|.

To refresh your websites, complete the following steps:

#. If the **Settings** dialog box is still being displayed, click **Cancel**.
#. In the bottom left corner, click **More**.
#. In the list, click **Refresh Acquia Cloud sites**.

After the refresh process successfully completes, your local environments should be able to synchronize with your |acquia-product:ac| websites.

.. |Generating a key pair| image:: https://cdn3.webdamdb.com/1280_6M4547qCv3z4.png?-62169955200
   :width: 590px
   :height: 414px
.. |Copy the public key| image:: https://cdn2.webdamdb.com/1280_wrstvdjIBDv8.png?-62169955200
   :width: 564px
   :height: 344px
