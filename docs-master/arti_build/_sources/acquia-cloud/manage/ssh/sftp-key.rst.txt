.. include:: /common/global.rst

Converting SSH keys for WinSCP
==============================

If you want to `use WinSCP as an SFTP
client </acquia-cloud/manage/sftp>`__ to connect to your
|acquia-product:ac| servers, you may need to convert your SSH key into a
format compatible with WinSCP. You can use PuTTYgen to convert your key
into the ``.ppk`` format required by WinSCP.

PuTTYgen is included in the `WinSCP installation
package <http://winscp.net/eng/docs/ui_installer_selectcomponents>`__.

To convert a key into the ``.ppk`` format using PuTTYgen:

#. Start PuTTYgen, and in the **Conversions** menu, click **Import
   key**.

   |Select Conversions > Import key|

#. In the **Load private key** window, browse to your SSH private key,
   select it, and then click **Open**. Your SSH private key is probably
   located in ``Users\[user_name]\.ssh``.

   |Select your private key and click Open|

#. Enter the passphrase associated with the private key. Note that the
   key fingerprint confirms the number of bits is 4096.

   |Enter the key's passphrase|

#. In the **File** menu, click **Save private key** to save the key in
   ``.ppk`` format.

Use this ``.ppk`` file as your key when you use WinSCP.

For more information, see the `PuTTYgen
documentation <https://winscp.net/eng/docs/ui_puttygen>`__, including
this `note about key
formats <https://winscp.net/eng/docs/ui_puttygen#other_formats>`__.

.. |Select Conversions > Import key| image:: https://cdn2.webdamdb.com/1280_2e0h8YQ0XRi3.png?1526475805
   :width: 493px
   :height: 477px
   :alt: Select Conversions > Import key
.. |Select your private key and click Open| image:: https://cdn3.webdamdb.com/1280_yLgIRnCfn91.png?1526476069
   :width: 625px
   :height: 434px
   :alt: Select your private key and click Open
.. |Enter the key's passphrase| image:: https://cdn4.webdamdb.com/md_2VLmq35F0dB8.png?1526476075
   :width: 226px
   :height: 136px
   :alt: Enter the key's passphrase
