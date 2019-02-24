.. include:: /common/global.rst

Hosting a site on |acquia-product:ac|
=====================================

.. toctree::
   :hidden:
   :glob:

   /dev-desktop/cloud/*

After you have created a local website in |acquia-product:add|, you can host it on |acquia-product:ac|. Because |acquia-product:add| is integrated with |acquia-product:ac|, you can develop your website locally and synchronize it with the versions on |acquia-product:ac|, pushing and pulling your code, database, and files in a way that makes the most sense for your workflow.

To host a local |acquia-product:add| website on |acquia-product:ac|:

#. Select the local website that you want to host on |acquia-product:ac|.
#. Click **Host this site on Acquia Cloud**.

   |Host on Acquia Cloud|

#. If you have already linked your installation of |acquia-product:add| to an |acquia-product:ac| account, skip to `Adding a website to an existing Acquia Cloud subscription <#existing>`__.
#. If you already have an |acquia-product:ac| subscription, enter the email address and Acquia Cloud password, and click **Log in**.

   |Sign in to Acquia Cloud|

#. If you don't have an |acquia-product:ac| subscription, click the **Get one for free** link.

For more information about what happens when you click **Host this site on Acquia Cloud**, see `How Acquia Dev Desktop works with Acquia Cloud </dev-desktop/cloud/details>`__.

.. _existing:

Adding a website to an existing |acquia-product:ac| subscription
----------------------------------------------------------------

#. If you have access to more than one |acquia-product:ac| subscription, select which subscription you want to add this website to. By default, |acquia-product:add| hides subscriptions from which you've already cloned an environment.

   |Select a subscription|

#. Select the environment to overwrite. An |acquia-product:ac| site has three environments: dev (Development), stage (Staging), and prod (Production). An |acquia-product:acfs| site has two environments: dev (Development) and stage (Staging). In most cases, you should select the Dev environment to overwrite.
#. Enter the location of your private key file, and click **OK**. If you have already connected from |acquia-product:add| to |acquia-product:ac|, |acquia-product:add| skips this step.

   |Enter private key file location|

   Communication with your |acquia-product:ac| site is protected with a private/public key pair. You also need the right role and permissions to sync |acquia-product:add| with |acquia-product:ac|. For more information, see `Acquia Cloud credentials and permissions </dev-desktop/cloud/key>`__.

|acquia-product:add| creates a Drupal site archive and imports it into |acquia-product:ac|. When it's finished, click **Close**.

Your website now exists in two locations: locally on your computer in |acquia-product:add|, and on |acquia-product:ac|. You can now work on your website locally and continuously sync it with the version of your site on |acquia-product:ac|. For more information, see `Working with sites on Acquia Cloud </dev-desktop/cloud/working>`__.

.. admonition:: Note for Drupal 8 users

   If your |acquia-product:ac| environment is not configured to use PHP 5.5 or later, you may not be able to sync Drupal 8 websites between |acquia-product:add| and |acquia-product:ac|.

`Learn more about configuring PHP versions </acquia-cloud/manage/php>`__ on |acquia-product:ac|.

.. |Host on Acquia Cloud| image:: https://cdn3.webdamdb.com/1280_2E5F1kOspz71.png?1527363860
   :width: 590px
   :height: 279px
.. |Sign in to Acquia Cloud| image:: https://cdn3.webdamdb.com/1280_s1Wo4W1kZ3M8.png?-62169955200
   :width: 582px
   :height: 334px
.. |Select a subscription| image:: https://cdn4.webdamdb.com/1280_crfJcIRimyI6.png?-62169955200
   :width: 590px
   :height: 344px
.. |Enter private key file location| image:: https://cdn2.webdamdb.com/1280_oR9iRbH64Et3.png?-62169955200
   :width: 590px
   :height: 147px
