.. include:: /common/global.rst

Understanding the Insight score and alerts
==========================================

.. container:: internal-navigation

   **Using Acquia Insight**

   * :doc:`Intro </acquia-cloud/insight>`
   * :doc:`Using </acquia-cloud/insight/using>`
   * Alerts
   * :doc:`Modules </acquia-cloud/insight/code>`
   * :doc:`Connector </acquia-cloud/insight/install>`
   * :doc:`Configure </acquia-cloud/insight/config>`
   
Insight inspects each of the environments that you've connected to
Acquia and rates them based on their performance, security, and
adherence to Acquia's identified best practices for Drupal applications.
Insight displays an alert for each of the items that it examines and
creates an overall rating or score for the environment based on the
types of alerts it encountered.

|Overall Insight rating|

Your Insight score is made up of two parts:

-  **Percentage score**

   Because Insight assigns different weights to each alert, the
   percentage and number of resolved issues don't directly relate to one
   another. Even if Insight reports that only one alert is unresolved,
   if this one alert is a priority critical alert, your Insight score
   can be red, and your environment's performance or security can be
   greatly affected.

-  **Color**, defined as follows:

   -  Green - Your application is operating normally. Although you can 
      still have critical or warning alerts for your application, the 
      number and severity of the alerts are not enough to significantly 
      affect your application. No immediate action is needed.
   -  Yellow - Your application's performance or security may be affected by the alerts reported by Insight. Schedule a time to
      resolve the alerts reported on the **Insight** page to improve your application's Insight score.
   -  Red - Your application is affected by at least one issue that greatly impacts the application's performance or security.
      Immediately resolve any reported critical alerts on the
      **Insight** page to improve your application's overall Insight
      score.

.. _interval:

Data intervals
--------------

The |acquia-product:anc| module sends information to
|acquia-product:ais| when your environment runs cron, and
|acquia-product:ais| updates your environment's scores and alerts every
30 minutes. Because of this, you can expect that the changes you make to
your environment will be reflected in your |acquia-product:ais| scores
after 30 minutes plus your environment's cron interval.

When visiting |acquia-product:ais| for the first time, you may not see
any data. If situations where there is no data to display,
|acquia-product:ac| will display one of the following messages:

-  **No data available** - Your website is not connected to
   |acquia-product:ais| or has not yet received any data.
-  **Data has not processed yet** - Your website has connected, but has
   not yet sent any data to |acquia-product:ais| for processing.

You can also trigger your environment to send information to Insight
manually using either of the following methods:

-  On your website's **Admin > Reports > Status report** page, in the
   **Acquia SPI** section, click **manually send SPI data**
-  Run cron

.. _feedback:

Applying Insight feedback to your application
---------------------------------------------

When Insight identifies an issue or improvement for your application, it
creates an alert to inform you of the problem, which includes
instructions on how to fix it. Insight categorizes alerts into the
following groups:

-  Performance
-  Security
-  Best practices
-  Modules

You can click the **View** link in each category to view details about
alerts.

The title of an alert message briefly describes the issue. If you click
the expand arrow, you can see additional information about the issue,
including how to resolve it.

Types of alert messages
~~~~~~~~~~~~~~~~~~~~~~~

Insight displays four different alerts on the **Analysis** page:

-  **Critical alerts - Red**

   |Insight critical alert|

   Your application is experiencing a serious condition that you should
   immediately address and resolve. Critical alerts have a greater
   effect on your overall Insight rating.

-  **Warning alerts - Yellow or Orange**

   |Insight warning alert Yellow| |Insight warning alert Orange|

   Your application is experiencing a condition that you should address
   and resolve when convenient. Orange warning alerts affect your
   application's rating more than yellow warning alerts. While warning
   alerts affect your application's Insight rating less than critical
   alerts, a high number of warning alerts can have a similar effect as
   a critical alert on your rating.

-  **Resolved alerts - Green**

   |Insight resolved alert|

   If you resolve an issue associated with a warning or critical alert,
   the alert changes into a resolved alert after the next cron run.

-  **Ignored alerts - Grey**

   |Ignored alert|

   If you click the |ignore icon| button for any of the other alert
   types, the alert turns grey and moves to the bottom of its category's
   alert list. Ignored alerts do not affect a website's overall Insight
   rating. To stop ignoring an alert, click the **Restore** link for the
   alert.

.. |Overall Insight rating| image:: https://cdn4.webdamdb.com/100th_sm_cOo4zdd3wgg0.png?1527031053
   :class: logo-pp
   :alt: Acquia Insight overall score example

.. |Insight critical alert| image:: https://cdn3.webdamdb.com/md_EQi0efaW7Q03.png?1527032350
   :alt: Insight critical alert

.. |Insight warning alert Orange| image:: https://cdn4.webdamdb.com/md_MnoIdje12fP1.png?1526476111
    :alt: Insight orange warning alert

.. |Insight warning alert Yellow| image:: https://cdn2.webdamdb.com/md_oMe1FMG1Ln29.png?1527031529
    :alt: Insight yellow warning alert

.. |Insight resolved alert| image:: https://cdn3.webdamdb.com/md_gnfCYSXcVP80.png?1526475906
  :alt: Insight resolved alert

.. |Ignored alert| image:: https://cdn3.webdamdb.com/md_cRqFgZOwN5I9.png?1526475686
   :alt: Insight ignored alert

.. |ignore icon| image:: https://cdn4.webdamdb.com/100th_sm_o7J3GjIjs12.png?1526476018
   :width: 14px
   :height: 14px
   :alt: Ignore icon
