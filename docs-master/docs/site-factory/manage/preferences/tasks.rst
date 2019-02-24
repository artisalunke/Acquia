.. include:: /common/global.rst

Scheduling site tasks with cron
===============================

.. toctree::
   :hidden:
   :glob:

   /site-factory/manage/preferences/tasks/*

To help your website run more efficiently, you should conduct regular
website maintenance. By using cron, you can automate several of these
maintenance tasks to run at scheduled intervals, based on your website's
needs.

|acquia-product:edg| provides two methods that you can use to modify the
interval and function of the scheduled tasks:

-  Create and manage scheduled tasks from the |acquia-product:sfi|
-  Control how often cron executes maintenance tasks on a per-website
   basis


Managing tasks using the |acquia-product:sfi|
---------------------------------------------

If you are a PaaS subscription customer, `using the Cron job page in the
|acquia-product:sfi| </site-factory/manage/tasks/factory>`__ enables you
to create and manage Drush commands that can control many aspects of
your websites' maintenance and operation.

.. admonition::  Note for SaaS+ subscription customers

   If you need to schedule cron tasks based on a particular schedule,
   `contact Acquia Support </support#contact>`__ or your Technical Account
   Manager to add cron jobs to your |acquia-product:edg| environments.


Running cron on your site
-------------------------

If you want to configure how often cron runs on a single website (which
is used for tasks that include checking for updates and indexing), you
can `modify the interval at which the websites run cron, or even run
cron manually </site-factory/manage/tasks/cron>`__.

.. note::  

   Because the website-based cron is triggered by website activity,
   configuring the cron interval from the website does not guarantee that
   cron will run on the schedule that you define. To ensure a greater
   likelihood of a particular cron execution schedule, use the 
   `Cron job page </site-factory/manage/tasks/factory>`__ in the 
   |acquia-product:sfi|.
