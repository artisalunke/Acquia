.. include:: /common/global.rst

Running cron on your site
=========================

There are certain tasks, such as checking for updates and indexing, that
must be run occasionally for your website to operate correctly, but do
not need to run all of the time.

To ensure that these tasks are run based on a regular schedule,
|acquia-product:edg| websites use *cron* (also called *Poor man's
cron*). Cron runs at a scheduled configured interval, and executes any
management tasks that are directed to it by other website modules and
features.

.. note::  Because cron is triggered by website activity, configuring the cron
   interval from the website does not guarantee that cron will run on the
   schedule that you define. To ensure a greater likelihood of a particular
   cron execution schedule, use the |cronsfi|_.

.. |cronsfi| replace:: Cron job page in the \ |acquia-product:sfi|\ 
.. _cronsfi: /site-factory/manage/tasks/factory

Setting a cron schedule
-----------------------

To configure how frequently cron runs on your website:

#. Go to **Configuration > Cron**.
#. In the **Run cron every** list, select the amount of time you want to
   elapse before cron runs again.

   We suggest that you select **1 day** for your websites. For most
   websites, it is a bad idea to select **Never** for the cron run
   frequency.

#. Click **Save configuration**.

Running cron manually
---------------------

To manually run cron immediately, even if it has not reached its
scheduled run time, select one of the following methods:

Cron configuration page
~~~~~~~~~~~~~~~~~~~~~~~

If you are signed in to your website as an administrator, to manually
run cron:

#. Go to **Configuration > Cron**.
#. Click **Run cron**.

.. _url:

Cron URL
~~~~~~~~

You can also run cron on your website by visiting a specific cron URL.
Your website's cron URL is located on the Cron configuration page at
**Configuration > Cron**.

|Cron URL|

Visiting the URL with your unique cron key appended to the URL will run
cron on your website, even if you are not signed in.

.. |Cron URL| image:: https://cdn4.webdamdb.com/1280_QqcxjFtOcrf7.png?1526475541
   :width: 590px
   :height: 245px
