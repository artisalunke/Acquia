.. include:: /common/global.rst

Viewing reports in |acquia-product:lpm|
=======================================

.. container:: internal-navigation

   **Using reports dashboards in Profile Manager**

   * :doc:`Intro </lift/profile-mgr/analytics/dashboards>`
   * :doc:`Overview </lift/profile-mgr/analytics/dashboards/operational>`
   * Details
   * :doc:`Config </lift/profile-mgr/analytics/dashboards/config>`
   * :doc:`Custom </lift/profile-mgr/analytics/dashboards/custom>`
   * :doc:`Fields </lift/profile-mgr/analytics/dashboards/custom/fields>`

In the **Analytics** tab, |acquia-product:lpm| displays reports that
present information relating to visitors' interaction with and behavior
on your websites and optionally on other channels such as email. These
reports are organized into the following sections:

-  `Content <#content-reports>`__
-  `Conversion <#conversion-reports>`__
-  `Engagement <#engagement-reports>`__
-  `Events <#events-reports>`__
-  `People <#people-reports>`__
-  `Segment <#segment-reports>`__
-  `Touches <#touches-reports>`__

Detailed report list
--------------------

Viewing the Content reports
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Content** section contains several reports that display data
related to visitors' viewing of content on your website. By default, all
of the reports in this section display data from the previous 30 days.

+-----------------------------------+-----------------------------------+
| Dashboard                         | Description                       |
+===================================+===================================+
| **Content by content section**    | Content view events, organized by |
|                                   | the content sections that         |
|                                   | visitors viewed most frequently   |
+-----------------------------------+-----------------------------------+
| **Content by content title**      | Content view events, organized by |
|                                   | the titles of the pieces of       |
|                                   | content that visitors viewed the  |
|                                   | most                              |
+-----------------------------------+-----------------------------------+
| **Content by content type**       | Content view events, organized by |
|                                   | the content types that visitors   |
|                                   | viewed most often                 |
+-----------------------------------+-----------------------------------+

.. _conversion-reports:

Viewing the Conversion report section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Conversion** section contains several reports that display the
campaign actions and click-throughs.

+-----------------------+-----------------------+-----------------------+
| Dashboard             | Description           | Reporting period      |
+=======================+=======================+=======================+
| **People who reached  | Number of unique      | Previous 90 days      |
| an event**            | people who reached a  |                       |
|                       | specified event, and  |                       |
|                       | average amount of     |                       |
|                       | time needed to reach  |                       |
|                       | it                    |                       |
+-----------------------+-----------------------+-----------------------+
| **People who reached  | Number of unique      | Previous 90 days      |
| an event by favorite  | people who reached a  |                       |
| keyword**             | specified event, and  |                       |
|                       | average amount of     |                       |
|                       | time needed to reach  |                       |
|                       | it, sorted by keyword |                       |
+-----------------------+-----------------------+-----------------------+
| **People who reached  | Number of unique      | Previous 90 days      |
| an event by persona** | people who reached a  |                       |
|                       | specified event, and  |                       |
|                       | average amount of     |                       |
|                       | time needed to reach  |                       |
|                       | it, sorted by persona |                       |
+-----------------------+-----------------------+-----------------------+
| **Rules pages         | Table of all running  | Previous 30 days      |
| summary**             | rules based on        |                       |
|                       | collected events,     |                       |
|                       | including page URL    |                       |
|                       | and number of         |                       |
|                       | decisions             |                       |
+-----------------------+-----------------------+-----------------------+
| **Rules in use        | Number of unique      | Previous 90 days      |
| trend**               | rules based on the    |                       |
|                       | underlying distinct   |                       |
|                       | decision events,      |                       |
|                       | organized by month    |                       |
+-----------------------+-----------------------+-----------------------+
| **Rules segment       | Table of all running  | Previous 30 days      |
| performance**         | rules based on        |                       |
|                       | collected events,     |                       |
|                       | including decision    |                       |
|                       | segment, goal name,   |                       |
|                       | number of decisions,  |                       |
|                       | number of goals, and  |                       |
|                       | total value of goals  |                       |
+-----------------------+-----------------------+-----------------------+
| **Rules summary**     | Table of all running  | Previous 30 days      |
|                       | rules based on        |                       |
|                       | collected events,     |                       |
|                       | including decision    |                       |
|                       | segment, goal name,   |                       |
|                       | number of decisions,  |                       |
|                       | number of goals,      |                       |
|                       | total value of goals  |                       |
+-----------------------+-----------------------+-----------------------+

.. _engagement-reports:

Viewing the Engagement reports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Engagement** section contains several reports that display data
relating to visitors' engagement with your website. By default, all of
the reports in this section display data from the previous six months.

+-----------------------------------+-----------------------------------+
| Dashboard                         | Description                       |
+===================================+===================================+
| **Engagement score trend**        | Average engagement score,         |
|                                   | organized by month                |
+-----------------------------------+-----------------------------------+
| **Number of page views trend**    | Number of page views each month   |
+-----------------------------------+-----------------------------------+
| **Time on site trend**            | Average touch duration in         |
|                                   | minutes, organized by month       |
+-----------------------------------+-----------------------------------+

.. _events-reports:

Viewing the Events reports
~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Events** section contains several reports that display data
related to visitor `events </lift/profile-mgr/event/category>`__ on your
website. By default, all of the reports in this section display data
from the previous 30 days.

+-----------------------------------+-----------------------------------+
| Dashboard                         | Description                       |
+===================================+===================================+
| **Events**                        | Number of unique events per day   |
+-----------------------------------+-----------------------------------+
| **Events by event name**          | Number of events per day,         |
|                                   | organized by event name           |
+-----------------------------------+-----------------------------------+
| **Events by segment**             | Number of events by segment,      |
|                                   | organized by event name           |
+-----------------------------------+-----------------------------------+
| **Rule decisions**                | Number of decisions by rule name, |
|                                   | organized by both slot name and   |
|                                   | rule name                         |
+-----------------------------------+-----------------------------------+

.. _people-reports:

Viewing the People reports
~~~~~~~~~~~~~~~~~~~~~~~~~~

The **People** section contains reports about your visitors, including
information about their identities and their preferences on your
website. Each report is based on a different organization scheme or
reportable item, and uses the number of visitors captured by
|acquia-product:cha| per day. By default, all of the reports in this
section display data from the previous 30 days.

+-----------------------------------+-----------------------------------+
| Dashboard                         | Description                       |
+===================================+===================================+
| **People**                        | Number of visitors per day        |
+-----------------------------------+-----------------------------------+
| **People by country**             | Number of visitors per day,       |
|                                   | organized by country              |
+-----------------------------------+-----------------------------------+
| **People by favorite content      | Number of visitors per day,       |
| section**                         | organized by favorite content     |
|                                   | section                           |
+-----------------------------------+-----------------------------------+
| **People by favorite content      | Number of visitors per day,       |
| type**                            | organized by favorite content     |
|                                   | type                              |
+-----------------------------------+-----------------------------------+
| **People by favorite keyword**    | Number of visitors per day,       |
|                                   | organized by favorite keyword     |
+-----------------------------------+-----------------------------------+
| **People by identifier type**     | Number of visitors per day,       |
|                                   | organized by the identifiers the  |
|                                   | visitor has provided to           |
|                                   | |acquia-product:cha| (for         |
|                                   | example, email address) or that   |
|                                   | |acquia-product:cha| has assigned |
|                                   | to the visitor (for example,      |
|                                   | tracking ID                       |
+-----------------------------------+-----------------------------------+
| **People by persona**             | Number of visitors per day,       |
|                                   | organized by the persona tags you |
|                                   | assigned to the content the       |
|                                   | visitor viewed                    |
+-----------------------------------+-----------------------------------+
| **People by region**              | Number of visitors per day,       |
|                                   | organized by country and region   |
+-----------------------------------+-----------------------------------+
| **People by segment**             | Number of visitors per day,       |
|                                   | organized by the segments into    |
|                                   | which each visitor falls          |
+-----------------------------------+-----------------------------------+
| **People trend**                  | Number of unique visitors,        |
|                                   | organized by month                |
+-----------------------------------+-----------------------------------+

.. _segment-reports:

Viewing the Segment reports
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Segment** section contains several reports that display data
relating to the segments into which your visitors fell when they
accessed your website. By default, all of the reports in this section
display data from the previous 30 days, except the **Segment trend** and
**Segments in use trend** reports, which display data from the past six
months.

+-----------------------------------+-----------------------------------+
| Dashboard                         | Description                       |
+===================================+===================================+
| **Segment performance**           | Engagement score, average goal    |
|                                   | value and total goal value by     |
|                                   | segment, organized by event name  |
|                                   | and segment name                  |
+-----------------------------------+-----------------------------------+
| **Segment trend**                 | Number of website visitors that   |
|                                   | fell into a specific segment,     |
|                                   | organized by month                |
+-----------------------------------+-----------------------------------+
| **Segments in common with         | Number of unique visitors who     |
| people**                          | matched both to a specified       |
|                                   | segment and all other segments    |
+-----------------------------------+-----------------------------------+
| **Segments in common with         | Number of unique visitors who     |
| touches**                         | matched both to a specified       |
|                                   | segment and all other segments    |
|                                   | within the same touch             |
+-----------------------------------+-----------------------------------+
| **Segments in use trend**         | Number of unique segments,        |
|                                   | organized by month                |
+-----------------------------------+-----------------------------------+

.. _touches-reports:

Viewing the Touches reports
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Touches** section contains several reports that display data
relating to the `touches </lift/profile-mgr/person#activity>`__ your
visitors perform and their methods of accessing your website. By
default, all of the reports in this section display data from the
previous 30 days.

+-----------------------------------+-----------------------------------+
| Dashboard                         | Description                       |
+===================================+===================================+
| **Touches**                       | Number of touches per day         |
+-----------------------------------+-----------------------------------+
| **Touches by browser**            | Number of touches per day,        |
|                                   | organized by the browsers that    |
|                                   | visitors used to access your      |
|                                   | website                           |
+-----------------------------------+-----------------------------------+
| **Touches by channel type**       | Number of touches per day,        |
|                                   | organized by the channels from    |
|                                   | which the data has come (for      |
|                                   | example, ``Web`` for data coming  |
|                                   | from your website or ``API`` for  |
|                                   | data passed using an API)         |
+-----------------------------------+-----------------------------------+
| **Touches by platform**           | Number of touches per day,        |
|                                   | organized by the devices that     |
|                                   | visitors used to access your      |
|                                   | website                           |
+-----------------------------------+-----------------------------------+
| **Touches by referrer domain**    | Number of touches per day,        |
|                                   | organized by the host name of the |
|                                   | external domain that referred the |
|                                   | visitor to the first webpage      |
|                                   | visited on your website           |
+-----------------------------------+-----------------------------------+
| **Touches by segment**            | Number of touches by segment,     |
|                                   | organized by event name           |
+-----------------------------------+-----------------------------------+
| **Touches by UTM content**        | Number of touches per day,        |
|                                   | organized by the Google Analytics |
|                                   | parameter for A/B testing and     |
|                                   | content-targeted ads              |
+-----------------------------------+-----------------------------------+
| **Touches by UTM medium**         | Number of touches per day,        |
|                                   | organized by the Google Analytics |
|                                   | parameter indicating the medium   |
|                                   | on which the link was used        |
|                                   | (examples include ``banner`` and  |
|                                   | ``email``)                        |
+-----------------------------------+-----------------------------------+
| **Touches by UTM name**           | Number of touches per day,        |
|                                   | organized by the Google Analytics |
|                                   | parameter that indicates the      |
|                                   | campaign name for paid search,    |
|                                   | email, or other inbound marketing |
|                                   | campaigns                         |
+-----------------------------------+-----------------------------------+
| **Touches by UTM referrer**       | Number of touches per day,        |
|                                   | organized by the Google Analytics |
|                                   | parameter for a campaign referrer |
|                                   | (for example, ``Newsletters``)    |
+-----------------------------------+-----------------------------------+
| **Touches by UTM terms**          | Number of touches per day,        |
|                                   | organized by the Google Analytics |
|                                   | parameter identifying paid        |
|                                   | keywords used                     |
+-----------------------------------+-----------------------------------+

Modifying report filters
------------------------

You can filter the information displayed in each report by configuring
certain settings. For information about how to do this, see `Configuring
report settings in
Lift Profile Manager </lift/profile-mgr/analytics/dashboards/config>`__.
