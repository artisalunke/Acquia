.. include:: /common/global.rst

File permissions and symlinks while using |acquia-product:ac|
=============================================================

File permissions on both |acquia-product:ac| and other Acquia offerings
require careful handling when you are changing code or other files on
your website. For security reasons, write permissions are disabled in
both the live website and in the website repository, which prevents
malicious individuals from attacking either of them.

Your website has the following three major areas:

-  *docroot* - Where the website is actually served from
-  *repository* - Where a duplicate of your codebase and PHP files are
   stored
-  *Gluster area*

The docroot is not a writable area. Any folder with an active
``settings.php`` file (often found in ``sites/default/files``) will `add
a
symlink </articles/adding-flexibility-your-server-structure-using-symlinks>`__
to the Gluster area. With the symlink in place, files placed in Gluster
appear as though they are located in the file directories where Drupal
expects them to be, without requiring write access to the code
repository files in the docroot.

Note

To ensure that links remain correct across server environments, Acquia
recommends that you use relative symlinks on |acquia-product:ac|.

.. _anatomy:

Anatomy of your website
-----------------------

The following diagram indicates the directory structure of a generic
website, from repository to docroot, and where the symlink lies in that
docroot:

|docroot-anatomy.gif|

Understanding how this works is important because without the right
permissions, your website may fail to work. This can be a problem when
you expect things to stay the way that you set them in version control.
Git, for example, does not store any permissions (aside from the
executable bit). Read and write, sticky, or Access Control List (ACL)
bits are lost when you commit changes. For more information, see `What
does git do to files that are a symbolic
link? <http://stackoverflow.com/questions/954560/what-does-git-do-to-files-that-are-a-symbolic-link>`__

If you are experiencing a problem with permissions, the following error
message may be displayed:

``file system: The selected file /mnt/tmp/mystg/filemyfile could not be uploaded, because the destination sites/default/files/js/myjsfile.js could not be found, or because its permissions do not allow the file to be written.``

Multisite installations can be a bit trickier, because all of the
websites can share the same codebase, and the same symlinks.

Note

If you have one website directory symlinked to another in
|acquia-product:ac|, when a symlink is created it will take on the name
of the first website in the directory by alphabet. This means that if
you have two websites, *docroot/sites/test*, and *docroot/sites/a-test*,
regardless of which website the symlink was initially created under, the
symlink will use the path *docroot/sites/a-test*.

The best practice is to symlink *only* the directory that needs write
access. As an example, to create the correct links for a module that
needs its own cache directory, you would use commands similar to the
following (where
``yoursitename@yourserver.hosting.acquia.com:yoursitename.git`` is your
Git URL, which can be found on the `**Cloud >
Workflow** </acquia-cloud/develop/checkout>`__ page):

Important

These instructions delete a directory; before you process the delete
(``rm -rf``), ensure that you have copied the files to the new location
or to local storage for later replacement.

``git clone yoursitename@yourserver.hosting.acquia.com:yoursitename.git cd yoursitename/docroot/sites/all/modules/examplemodule rm -rf cache ln -s ../../../default/files/cache cache git add cache git commit -m "creating symlink for examplemodule cache" git push origin master``

After completing this process, you will need to access the server and
create the new ``cache`` directory in your ``files`` directory. If not,
when the code is deployed, the symlink will point at a non-existent
target. After you have created the directory, use either SCP (Secure
Copy) or SFTP (Secure File Transfer Protocol) to transfer any files you
had temporarily stored and need to replace.

.. _problem:

Known problem modules
---------------------

With the |acquia-product:ac| setup, several modules are known to have
problems because they require the ability to write to their own module
folder. You will need to link modules to the files area.

-  `CKFinder <https://www.drupal.org/project/WYSIWYG-CKFinder>`__
-  `TCPDF <https://www.drupal.org/project/tcpdf>`__
-  `Contact
   Importer <https://www.drupal.org/project/contact_importer>`__ (due to
   its reliance on `Open Inviter <http://openinviter.com/>`__)
-  `HTML Purifier <https://www.drupal.org/project/htmlpurifier>`__
-  `WURFL <https://www.drupal.org/project/wurfl>`__
-  `SimpleSAMLPHP
   Authentication <https://www.drupal.org/project/simplesamlphp_auth>`__

This is by no means a complete list, and you may also need to link
additional modules to the files area.

.. |docroot-anatomy.gif| image:: https://cdn3.webdamdb.com/1280_wsiKMfDS1E71.jpg?1526476092
   :class: no-sb

