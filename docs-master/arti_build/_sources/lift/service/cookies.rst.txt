.. include:: /common/global.rst

Cookies used by |acquia-product:cha|
====================================

|acquia-product:cha| (including |acquia-product:alt|) uses the following types 
of cookies when displaying targeted or recommended content to visitors, based on
persistent, session, and temporary cookie types.

Types of cookies in |acquia-product:cha|
----------------------------------------

Unless otherwise noted, the following cookies are required by
|acquia-product:cha|.

Persistent cookies in |acquia-product:cha|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Name                  | Description           | Duration              |
+=======================+=======================+=======================+
| ``tc_3dnt``           | Third-party cookie    | 10 years              |
|                       | for do not track —    |                       |
|                       | *Optional*            |                       |
+-----------------------+-----------------------+-----------------------+
| ``tc_3ptid_``         | Third-party person    | 2 years (configurable |
|                       | identifier, where     | in                    |
|                       | ```` is the           | |acquia-product:alw|  |
|                       | customer’s identifier | at **Admin > Manage   |
|                       | in                    | JavaScript**)         |
|                       | |acquia-product:alw|  |                       |
|                       | — *Optional*          |                       |
+-----------------------+-----------------------+-----------------------+
| ``tc_3ptidexpiry_``   | Tracking cookie       | 2 years (configurable |
|                       | expiration value,     | in                    |
|                       | where ```` is the     | |acquia-product:alw|  |
|                       | customer’s identifier | at **Admin > Manage   |
|                       | in                    | JavaScript**)         |
|                       | |acquia-product:alw|  |                       |
|                       | — *Optional*          |                       |
+-----------------------+-----------------------+-----------------------+
| ``tc_dnt``            | Set if a visitor has  | 10 years              |
|                       | opted out of tracking |                       |
|                       | and personalization — |                       |
|                       | *Optional*            |                       |
+-----------------------+-----------------------+-----------------------+
| ``tc_nu``             | New visitor indicator | 30 minutes            |
|                       | (does not yet have a  |                       |
|                       | person identifier) —  |                       |
|                       | *Optional*            |                       |
+-----------------------+-----------------------+-----------------------+
| ``tc_ptid``           | Randomly generated    | 2 years (configurable |
|                       | person identifier     | in Acquia Lift Web    |
|                       | (used to associate a  | at **Admin > Manage   |
|                       | visitor with their    | JavaScript**)         |
|                       | profile)              |                       |
+-----------------------+-----------------------+-----------------------+
| ``tc_q``              | Local queue to store  | 2 years (configurable |
|                       | captures until they   | in                    |
|                       | can be sent (because  | |acquia-product:alw|  |
|                       | sometimes events do   | at **Admin > Manage   |
|                       | not have time to be   | JavaScript**)         |
|                       | submitted to the      |                       |
|                       | server, due to user   |                       |
|                       | or client actions)    |                       |
+-----------------------+-----------------------+-----------------------+
| ``tc_ttid``           | Touch identifier      | 30 minutes after the  |
|                       |                       | last page view        |
+-----------------------+-----------------------+-----------------------+
| ``tc_wq``             | List of captures (or  | 30 minutes after the  |
|                       | identifiers) for the  | last page view        |
|                       | current touch         |                       |
+-----------------------+-----------------------+-----------------------+
| ``tc_ws``             | Tomcat session ID     | 30 minutes after the  |
|                       |                       | last page view        |
+-----------------------+-----------------------+-----------------------+

Session cookies in |acquia-product:cha|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| ``acquiaLiftQueue``               | Local queue to store goal events  |
|                                   | when there isn't time for them to |
|                                   | be processed immediately (used    |
|                                   | only by |acquia-product:alt|)     |
+-----------------------------------+-----------------------------------+
| ``drupal-personalize``            | Session identifier for the user   |
|                                   | (used only by                     |
|                                   | |acquia-product:alt|)             |
+-----------------------------------+-----------------------------------+
| ``has_js``                        | Determines if JavaScript is       |
|                                   | enabled                           |
+-----------------------------------+-----------------------------------+

Temporary cookies in |acquia-product:cha|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Name                  | Description           | Duration              |
+=======================+=======================+=======================+
| ``tc_trackenabledtest | Testing cookie (used  | Immediately deleted   |
| ``                    | to ensure browser can |                       |
|                       | set cookies)          |                       |
+-----------------------+-----------------------+-----------------------+
| ``lift_access``       | Contains the          | Expires when the user |
|                       | temporary token's     | signs out of          |
|                       | access key and secret | |acquia-product:lpm|  |
|                       | key                   |                       |
+-----------------------+-----------------------+-----------------------+

Third-party cookies and |acquia-product:cha|
--------------------------------------------

First-party cookies are enabled by default on |acquia-product:cha|, and
are created using the domain of the website that the visitor is
currently viewing. Third-party cookies are optional in
|acquia-product:cha|, and if enabled, are created with the
``acquia.com`` domain.

Third-party cookies are useful if you maintain multiple websites that
use different domain names, and want to track users across all of your
domains. However, some browsers may prevent the creation of third-party
cookies or limit their life span. For example, browsers using Webkit's
`Intelligent Tracking
Prevention <https://webkit.org/blog/7675/intelligent-tracking-prevention/>`__,
such as Safari, will delete cookies and browsing data if a website
visitor has not interacted with your website in 30 days.
